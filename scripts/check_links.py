#!/usr/bin/env python3
"""Check that resource URLs still answer. Network access required.

A 2xx/3xx answer counts as reachable and, with --write, stamps `checked` with today's date.
401/403/429 usually mean a site refuses automated clients, so they are reported separately and
never stamped. 404/410 and other HTTP errors are reported as broken. Connection errors
(DNS, TLS, timeouts, restricted egress) are reported as unreachable: the result says nothing about
the site itself. Only reachable links are ever stamped.

    python scripts/check_links.py                 # report only
    python scripts/check_links.py --write         # stamp reachable links
    python scripts/check_links.py --id holmes     # one record
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import DATA  # noqa: E402

AGENT = "Mozilla/5.0 (compatible; threat-modeling-library-linkcheck/1.0)"
BLOCKED = {401, 403, 405, 429, 999}


def probe(url: str, timeout: float) -> tuple[str, str]:
    """Return (state, detail) where state is ok, blocked, broken or unreachable."""
    last = ""
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, method=method, headers={"User-Agent": AGENT})
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return "ok", str(response.status)
        except urllib.error.HTTPError as err:
            last = str(err.code)
            if err.code in BLOCKED and method == "HEAD":
                continue
            if err.code in BLOCKED:
                return "blocked", last
            if method == "HEAD" and err.code >= 400:
                continue
            return "broken", last
        except (urllib.error.URLError, TimeoutError, OSError) as err:
            last = type(err).__name__
    return ("broken" if last.isdigit() else "unreachable"), last


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--write", action="store_true", help="stamp `checked` on reachable links")
    parser.add_argument("--id", action="append", help="check only this id (repeatable)")
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()

    path = DATA / "resources.json"
    items = json.loads(path.read_text(encoding="utf-8"))
    todo = [i for i in items if not args.id or i["id"] in args.id]
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(lambda i: probe(i["url"], args.timeout), todo))

    today = date.today().isoformat()
    counts = {"ok": 0, "blocked": 0, "broken": 0, "unreachable": 0}
    for item, (state, detail) in zip(todo, results):
        counts[state] += 1
        if state != "ok":
            print(f"{state.upper():8} {detail:>16}  {item['id']}  {item['url']}")
        elif args.write:
            item["checked"] = today
    print(
        f"\nreachable={counts['ok']} blocked={counts['blocked']} "
        f"unreachable={counts['unreachable']} broken={counts['broken']} of {len(todo)}"
    )
    if args.write:
        path.write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 1 if counts["broken"] else 0


if __name__ == "__main__":
    sys.exit(main())
