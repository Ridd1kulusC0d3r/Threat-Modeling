#!/usr/bin/env python3
"""Dependency-free validation for the resource and method datasets."""

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (  # noqa: E402
    ACCESS, APPROACHES, GRADES, LANGS, LEVELS, MAX_FEATURED, METHOD_STATUS, ORIGINS, TOPICS, TYPES,
    methods, resources,
)

ID = re.compile(r"^[a-z0-9][a-z0-9-]{1,59}$")
RESOURCE_FIELDS = {
    "id", "title", "url", "authors", "year", "type", "topics", "access", "grade", "level", "lang",
    "summary", "limit", "origin", "added", "checked", "featured", "exercise",
    "doi", "venue", "isbn", "essential",
}
RESOURCE_REQUIRED = RESOURCE_FIELDS - {"exercise", "year", "checked", "doi", "venue", "isbn", "essential"}
DOI = re.compile(r"^10\.\d{4,9}/\S+$")
ISBN = re.compile(r"^[0-9Xx-]{10,17}$")
METHOD_FIELDS = {
    "id", "name", "approach", "question", "centered_on", "outputs", "use_when", "limits", "status",
    "resources", "psychology",
}
METHOD_REQUIRED = METHOD_FIELDS - {"psychology"}


def valid_date(value) -> bool:
    try:
        date.fromisoformat(value)
        return True
    except (TypeError, ValueError):
        return False


def nonblank(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def check_resources(items: list[dict]) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    seen_urls: dict[str, str] = {}
    for item in items:
        rid = item.get("id", "<sem id>")
        where = f"resource {rid}"
        extra = set(item) - RESOURCE_FIELDS
        missing = RESOURCE_REQUIRED - set(item)
        if extra:
            errors.append(f"{where}: campos desconhecidos {sorted(extra)}")
        if missing:
            errors.append(f"{where}: campos ausentes {sorted(missing)}")
            continue
        if not ID.match(rid):
            errors.append(f"{where}: id inválido")
        if rid in seen_ids:
            errors.append(f"{where}: id duplicado")
        seen_ids.add(rid)
        for field in ("title", "authors", "summary", "limit"):
            if not nonblank(item[field]):
                errors.append(f"{where}: {field} vazio")
        url = item["url"]
        if not (isinstance(url, str) and url.startswith("https://")):
            errors.append(f"{where}: url precisa ser https")
        elif url.rstrip("/") in seen_urls:
            errors.append(f"{where}: url repetida em {seen_urls[url.rstrip('/')]}")
        else:
            seen_urls[url.rstrip("/")] = rid
        if item["type"] not in TYPES:
            errors.append(f"{where}: type '{item['type']}' desconhecido")
        if item["grade"] not in GRADES:
            errors.append(f"{where}: grade '{item['grade']}' desconhecido")
        if item["access"] not in ACCESS:
            errors.append(f"{where}: access '{item['access']}' desconhecido")
        if item["level"] not in LEVELS:
            errors.append(f"{where}: level '{item['level']}' desconhecido")
        if item["lang"] not in LANGS:
            errors.append(f"{where}: lang '{item['lang']}' desconhecido")
        if item["origin"] not in ORIGINS:
            errors.append(f"{where}: origin '{item['origin']}' desconhecido")
        if not isinstance(item["topics"], list) or not item["topics"]:
            errors.append(f"{where}: topics precisa ser lista não vazia")
        else:
            bad = [t for t in item["topics"] if t not in TOPICS]
            if bad:
                errors.append(f"{where}: topics desconhecidos {bad}")
            if len(set(item["topics"])) != len(item["topics"]):
                errors.append(f"{where}: topics repetidos")
        year = item.get("year")
        if year is not None and not (isinstance(year, int) and 1960 <= year <= date.today().year + 1):
            errors.append(f"{where}: year fora do intervalo")
        if not valid_date(item["added"]):
            errors.append(f"{where}: added não é data ISO")
        if item.get("checked") is not None and not valid_date(item["checked"]):
            errors.append(f"{where}: checked não é data ISO")
        if not isinstance(item["featured"], bool):
            errors.append(f"{where}: featured precisa ser booleano")
        if item["featured"] and item["grade"] in {"D", "E"}:
            errors.append(f"{where}: destaque exige grau A, B ou C")
        if "doi" in item and not (isinstance(item["doi"], str) and DOI.match(item["doi"])):
            errors.append(f"{where}: doi inválido (use a forma 10.xxxx/…, sem https://doi.org/)")
        if "isbn" in item and not (isinstance(item["isbn"], str) and ISBN.match(item["isbn"])):
            errors.append(f"{where}: isbn inválido")
        if "venue" in item and not nonblank(item["venue"]):
            errors.append(f"{where}: venue vazio")
        if "essential" in item and not isinstance(item["essential"], bool):
            errors.append(f"{where}: essential precisa ser booleano")
        if item.get("essential") and item["grade"] in {"D", "E"}:
            errors.append(f"{where}: núcleo essencial exige grau A, B ou C")
    featured = sum(1 for item in items if item.get("featured"))
    if featured > MAX_FEATURED:
        errors.append(f"destaques demais: {featured} (máximo {MAX_FEATURED})")
    return errors


def check_methods(items: list[dict], resource_ids: set[str]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for item in items:
        mid = item.get("id", "<sem id>")
        where = f"method {mid}"
        extra = set(item) - METHOD_FIELDS
        missing = METHOD_REQUIRED - set(item)
        if extra:
            errors.append(f"{where}: campos desconhecidos {sorted(extra)}")
        if missing:
            errors.append(f"{where}: campos ausentes {sorted(missing)}")
            continue
        if not ID.match(mid):
            errors.append(f"{where}: id inválido")
        if mid in seen:
            errors.append(f"{where}: id duplicado")
        seen.add(mid)
        for field in ("name", "question", "centered_on", "outputs", "use_when", "limits"):
            if not nonblank(item[field]):
                errors.append(f"{where}: {field} vazio")
        if item["approach"] not in APPROACHES:
            errors.append(f"{where}: approach '{item['approach']}' desconhecido")
        if item["status"] not in METHOD_STATUS:
            errors.append(f"{where}: status '{item['status']}' desconhecido")
        refs = item["resources"]
        if not isinstance(refs, list) or not refs:
            errors.append(f"{where}: resources precisa citar ao menos uma fonte")
        else:
            for ref in refs:
                if ref not in resource_ids:
                    errors.append(f"{where}: resource '{ref}' não existe")
    return errors


def main() -> int:
    res = resources()
    meth = methods()
    errors = check_resources(res) + check_methods(meth, {r["id"] for r in res if "id" in r})
    unchecked = sum(1 for r in res if r.get("checked") is None)
    if errors:
        print(f"{len(errors)} erro(s):")
        for err in errors:
            print(f"  - {err}")
        return 1
    print(f"ok: {len(res)} recursos, {len(meth)} métodos ({unchecked} recursos sem verificação de link)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
