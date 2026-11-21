#!/usr/bin/env python3
"""Sugere candidatos para data/resources.json a partir do OPML do repositório `feeds`.

Só lê e sugere: nunca escreve em data/. Um humano revisa, ajusta grau/limite e cola em resources.json.

    python scripts/ingest_feeds.py ../feeds/feeds.opml                  # relatório offline dos feeds
    python scripts/ingest_feeds.py ../feeds/feeds.opml --fetch --topic cti --since 30 --out candidatos.json
    python scripts/ingest_feeds.py feeds.opml --fetch --keyword "threat model" --keyword provenance

Offline: lista domínios do OPML que ainda não aparecem no acervo. Com --fetch (rede): lê RSS/Atom,
filtra entradas recentes por palavras-chave do tema e gera registros candidatos que passam em
`validate.check_resources`. Candidatos recebem grau D, `origin: curadoria` e limite explícito de
"pendente de revisão". Não afirmam que o conteúdo é bom, só que casou com as palavras-chave.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import TOPICS, resources  # noqa: E402
import validate  # noqa: E402

UA = {"User-Agent": "threat-modeling-library-ingest/1.0"}
MAX_BYTES = 5 * 1024 * 1024
KEYWORDS = {
    "threat-modeling": ["threat model", "stride", "attack tree", "attack graph", "dfd"],
    "detection-engineering": ["detection engineering", "sigma rule", "detection rule", "threat hunting", "telemetry"],
    "cti": ["threat intelligence", "cti", "intrusion set", "ioc", "threat actor"],
    "apt": ["apt", "campaign", "nation-state", "espionage"],
    "osint": ["osint", "open source intelligence", "geolocation", "attribution", "investigation"],
    "psychology": ["cognitive bias", "psychology", "social engineering", "deception", "heuristic"],
    "supply-chain": ["supply chain", "dependency confusion", "sbom", "ci/cd"],
    "cloud": ["cloudtrail", "iam", "entra", "oauth", "kubernetes"],
    "ai": ["llm", "prompt injection", "agentic", "ai security"],
}


def host(url: str) -> str:
    h = (urlsplit(url).hostname or "").lower()
    return h[4:] if h.startswith("www.") else h


def read_opml(path: Path) -> list[dict]:
    """Return [{url, category}] for every outline carrying xmlUrl."""
    out = []

    def walk(node, category):
        for child in node:
            if child.tag != "outline":
                continue
            if child.get("xmlUrl"):
                out.append({"url": child.get("xmlUrl").strip(), "category": category, "title": child.get("title") or child.get("text") or ""})
            else:
                walk(child, child.get("title") or child.get("text") or category)

    root = ET.parse(path).getroot()
    body = root.find("body")
    walk(body if body is not None else root, "")
    return out


def new_domains(feeds: list[dict], known_urls: set[str]) -> dict[str, list[str]]:
    known_hosts = {host(u) for u in known_urls}
    result: dict[str, list[str]] = {}
    for f in feeds:
        h = host(f["url"])
        if h and h not in known_hosts:
            result.setdefault(h, []).append(f["url"])
    return result


def slug(text: str, limit: int = 56) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")[:limit].strip("-")
    return text if len(text) >= 2 else "item"


def parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    value = value.strip()
    try:
        dt = parsedate_to_datetime(value)
    except (TypeError, ValueError):
        try:
            dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            return None
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def local(tag: str) -> str:
    return tag.split("}")[-1]


def entries(data: bytes) -> tuple[str, list[dict]]:
    """Parse RSS/Atom/RDF into (feed title, [{title, url, summary, published}])."""
    root = ET.fromstring(data)
    feed_title = next((c.text or "" for c in root.iter() if local(c.tag) == "title"), "").strip()
    out = []
    for item in root.iter():
        if local(item.tag) not in {"item", "entry"}:
            continue
        fields = {local(c.tag): c for c in item}
        link = ""
        for c in item:
            if local(c.tag) == "link":
                link = (c.get("href") or c.text or "").strip()
                if c.get("rel", "alternate") == "alternate":
                    break
        text = lambda k: re.sub(r"<[^>]+>", " ", (fields[k].text or "")) if k in fields else ""  # noqa: E731
        published = next((fields[k].text for k in ("pubDate", "published", "updated", "date") if k in fields), None)
        out.append(
            {
                "title": " ".join(text("title").split()),
                "url": link,
                "summary": " ".join((text("description") or text("summary") or text("content")).split())[:280],
                "published": parse_date(published),
            }
        )
    return feed_title, out


def fetch(url: str, timeout: float = 15.0) -> bytes:
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as resp:
        data = resp.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise ValueError("resposta excede 5 MiB")
    return data


def matches(entry: dict, words: list[str]) -> list[str]:
    haystack = f"{entry['title']} {entry['summary']}".lower()
    return [w for w in words if re.search(rf"\b{re.escape(w.lower())}", haystack)]


def candidate(entry: dict, feed_title: str, topics: list[str], hit: list[str], today: date) -> dict:
    published = entry["published"]
    return {
        "id": slug(entry["title"] or entry["url"]),
        "title": entry["title"],
        "url": entry["url"],
        "authors": feed_title or host(entry["url"]),
        "year": published.year if published else None,
        "type": "article",
        "topics": topics,
        "access": "free",
        "grade": "D",
        "level": "intermediate",
        "lang": "en",
        "summary": entry["summary"] or f"Entrada de feed: {entry['title']}",
        "limit": f"Candidato automático de feed (palavras: {', '.join(hit)}); grau, nível e limite pendentes de revisão humana.",
        "origin": "curadoria",
        "added": today.isoformat(),
        "checked": None,
        "featured": False,
    }


def collect(feeds: list[dict], topics: list[str], extra: list[str], since_days: int, today: date, existing: list[dict]) -> list[dict]:
    words = {t: KEYWORDS[t] for t in topics}
    all_words = sorted({w for ws in words.values() for w in ws} | set(extra))
    cutoff = datetime.now(timezone.utc) - timedelta(days=since_days)
    seen_urls = {r["url"].rstrip("/") for r in existing}
    seen_ids = {r["id"] for r in existing}

    def one(feed):
        try:
            return feed, entries(fetch(feed["url"]))
        except (urllib.error.URLError, OSError, ValueError, ET.ParseError) as err:
            print(f"aviso: {feed['url']}: {type(err).__name__}", file=sys.stderr)
            return feed, ("", [])

    with ThreadPoolExecutor(max_workers=8) as pool:
        fetched = list(pool.map(one, feeds))

    out = []
    for _feed, (feed_title, items) in fetched:
        for entry in items:
            if not entry["url"].startswith("https://") or entry["url"].rstrip("/") in seen_urls:
                continue
            if entry["published"] and entry["published"] < cutoff:
                continue
            hit = matches(entry, all_words)
            if not hit:
                continue
            tops = [t for t, ws in words.items() if any(w in hit for w in ws)] or list(topics[:1]) or ["cti"]
            cand = candidate(entry, feed_title, tops, hit, today)
            if cand["id"] in seen_ids:
                cand["id"] = f"{cand['id'][:50]}-{today.strftime('%y%m%d')}"
            seen_ids.add(cand["id"])
            seen_urls.add(cand["url"].rstrip("/"))
            out.append(cand)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("opml", type=Path)
    parser.add_argument("--fetch", action="store_true", help="ler os feeds (rede) e gerar candidatos")
    parser.add_argument("--topic", action="append", choices=sorted(KEYWORDS), help="tema com palavras-chave embutidas (repetível)")
    parser.add_argument("--keyword", action="append", default=[], help="palavra-chave extra (repetível)")
    parser.add_argument("--since", type=int, default=30, help="dias para trás (padrão 30)")
    parser.add_argument("--category", help="só feeds desta categoria do OPML")
    parser.add_argument("--limit-feeds", type=int, default=0, help="limitar nº de feeds lidos (0 = todos)")
    parser.add_argument("--out", type=Path, help="gravar candidatos em JSON (fora de data/)")
    args = parser.parse_args()

    if not args.opml.exists():
        print(f"OPML não encontrado: {args.opml}", file=sys.stderr)
        return 2
    feeds = read_opml(args.opml)
    if args.category:
        feeds = [f for f in feeds if f["category"].lower() == args.category.lower()]
    existing = resources()
    print(f"feeds no OPML: {len(feeds)}")
    fresh = new_domains(feeds, {r["url"] for r in existing})
    print(f"domínios ainda ausentes do acervo: {len(fresh)}")

    if not args.fetch:
        for h in sorted(fresh):
            print(f"  {h}")
        return 0

    topics = args.topic or []
    if not topics and not args.keyword:
        print("--fetch exige --topic ou --keyword", file=sys.stderr)
        return 2
    selected = feeds[: args.limit_feeds] if args.limit_feeds else feeds
    cands = collect(selected, topics, args.keyword, args.since, date.today(), existing)
    errors = validate.check_resources(cands)
    if errors:
        print("candidatos inválidos:", *errors, sep="\n  ", file=sys.stderr)
        return 1
    text = json.dumps(cands, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.write_text(text, encoding="utf-8")
        print(f"{len(cands)} candidato(s) gravados em {args.out}")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
