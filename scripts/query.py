#!/usr/bin/env python3
"""Search the library from the terminal.

    python scripts/query.py search "apt provenance"
    python scripts/query.py list --topic psychology --max-grade B
    python scripts/query.py list --type tool --access free --level intro
    python scripts/query.py show holmes
    python scripts/query.py method stride
    python scripts/query.py stats
    python scripts/query.py export --format csv > acervo.csv
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import ACCESS, GRADES, LEVELS, TOPICS, TYPES, methods, resources  # noqa: E402


def haystack(item: dict) -> str:
    parts = [item["id"], item["title"], item["authors"], item["summary"], item["limit"], *item["topics"], item["type"]]
    return " ".join(str(p) for p in parts).lower()


def search(items, query: str):
    terms = query.lower().split()
    scored = []
    for item in items:
        text = haystack(item)
        if all(re.search(rf"\b{re.escape(t)}", text) for t in terms):
            title = item["title"].lower()
            scored.append((-sum(t in title for t in terms), item["grade"], title, item))
    return [s[-1] for s in sorted(scored, key=lambda s: s[:3])]


def filtered(items, args):
    out = items
    if args.topic:
        out = [i for i in out if args.topic in i["topics"]]
    if args.type:
        out = [i for i in out if i["type"] == args.type]
    if args.access:
        out = [i for i in out if i["access"] == args.access]
    if args.level:
        out = [i for i in out if i["level"] == args.level]
    if args.max_grade:
        out = [i for i in out if i["grade"] <= args.max_grade]
    if args.lang:
        out = [i for i in out if i["lang"] == args.lang]
    return sorted(out, key=lambda i: (i["grade"], i["title"].lower()))


def line(i: dict) -> str:
    return f"[{i['grade']}] {i['id']:<38} {i['type']:<10} {i['title'][:70]}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search")
    s.add_argument("query")
    s.add_argument("--limit", type=int, default=15)
    lst = sub.add_parser("list")
    lst.add_argument("--topic", choices=sorted(TOPICS))
    lst.add_argument("--type", choices=sorted(TYPES))
    lst.add_argument("--access", choices=sorted(ACCESS))
    lst.add_argument("--level", choices=sorted(LEVELS))
    lst.add_argument("--max-grade", choices=sorted(GRADES), help="keep grades up to this letter (A is best)")
    lst.add_argument("--lang", choices=["en", "pt"])
    sh = sub.add_parser("show")
    sh.add_argument("id")
    me = sub.add_parser("method")
    me.add_argument("id", nargs="?")
    sub.add_parser("stats")
    ex = sub.add_parser("export")
    ex.add_argument("--format", choices=["json", "csv"], default="json")
    args = parser.parse_args()

    items = resources()
    if args.cmd == "search":
        hits = search(items, args.query)
        for i in hits[: args.limit]:
            print(line(i))
        print(f"\n{len(hits)} resultado(s)" + (f", mostrando {args.limit}" if len(hits) > args.limit else ""))
    elif args.cmd == "list":
        hits = filtered(items, args)
        for i in hits:
            print(line(i))
        print(f"\n{len(hits)} recurso(s)")
    elif args.cmd == "show":
        match = next((i for i in items if i["id"] == args.id), None)
        if not match:
            print(f"id não encontrado: {args.id}", file=sys.stderr)
            return 1
        print(json.dumps(match, ensure_ascii=False, indent=2))
    elif args.cmd == "method":
        meths = methods()
        if not args.id:
            for m in meths:
                print(f"{m['id']:<16} {m['status']:<13} {m['name']}")
            return 0
        match = next((m for m in meths if m["id"] == args.id), None)
        if not match:
            print(f"método não encontrado: {args.id}", file=sys.stderr)
            return 1
        print(json.dumps(match, ensure_ascii=False, indent=2))
    elif args.cmd == "stats":
        print(f"recursos: {len(items)}  métodos: {len(methods())}")
        for label, key in (("grau", "grade"), ("tipo", "type"), ("acesso", "access"), ("nível", "level"), ("origem", "origin")):
            counts = Counter(i[key] for i in items)
            print(f"{label:<7}", "  ".join(f"{k}={v}" for k, v in sorted(counts.items())))
        topics = Counter(t for i in items for t in i["topics"])
        print("temas  ", "  ".join(f"{k}={v}" for k, v in topics.most_common()))
    elif args.cmd == "export":
        if args.format == "json":
            json.dump(items, sys.stdout, ensure_ascii=False, indent=2)
            print()
        else:
            fields = ["id", "title", "url", "authors", "year", "type", "topics", "access", "grade", "level", "lang", "origin", "added", "checked", "summary", "limit"]
            writer = csv.DictWriter(sys.stdout, fieldnames=fields, extrasaction="ignore")
            writer.writeheader()
            for i in items:
                writer.writerow({**i, "topics": ";".join(i["topics"])})
    return 0


if __name__ == "__main__":
    sys.exit(main())
