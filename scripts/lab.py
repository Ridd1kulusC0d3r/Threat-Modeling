#!/usr/bin/env python3
"""Laboratório de detecção: avalia regras (subconjunto Sigma-like em JSON) contra fixtures sintéticas.

Cada case em `lab/<case>/` tem `rule.json` e `fixtures.jsonl`. Uma linha de fixture declara o
resultado esperado: `match`, `no_match` ou `degraded`. `degraded` significa que um campo exigido
pelo contrato de telemetria está ausente: a regra NÃO responde "sem alerta" em silêncio.

    python scripts/lab.py run                 # todos os cases
    python scripts/lab.py run --case dcsync   # um case
    python scripts/lab.py run --json          # saída para automação

Escopo: fixtures sintéticas verificam a lógica, não a telemetria real nem o ruído de produção.
Operadores de campo: (igual), contains, startswith, endswith, exists. Listas são OR; texto sem distinção
de maiúsculas, como no Sigma. A condição aceita and, or, not e parênteses.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import ROOT  # noqa: E402

LAB = ROOT / "lab"
OUTCOMES = {"match", "no_match", "degraded"}
OPERATORS = {"equals", "contains", "startswith", "endswith", "exists"}
TOKEN = re.compile(r"\s*(\(|\)|[A-Za-z_][\w-]*)")


def _present(event: dict, field: str) -> bool:
    return field in event and event[field] is not None


def _norm(value) -> str:
    return str(value).lower()


def _test(op: str, actual, expected) -> bool:
    if op == "exists":
        return (actual is not None) == bool(expected)
    if actual is None:
        return False
    values = actual if isinstance(actual, list) else [actual]
    wanted = expected if isinstance(expected, list) else [expected]
    for v in map(_norm, values):
        for w in map(_norm, wanted):
            if (
                (op == "equals" and v == w)
                or (op == "contains" and w in v)
                or (op == "startswith" and v.startswith(w))
                or (op == "endswith" and v.endswith(w))
            ):
                return True
    return False


def selection_matches(selection: dict, event: dict) -> bool:
    """Todos os campos da seleção precisam bater (AND); valores em lista são alternativas (OR)."""
    for key, expected in selection.items():
        field, _, op = key.partition("|")
        op = op or "equals"
        if op not in OPERATORS:
            raise ValueError(f"operador desconhecido: {op}")
        if not _test(op, event.get(field), expected):
            return False
    return True


def tokenize(condition: str) -> list[str]:
    out, pos = [], 0
    while pos < len(condition):
        m = TOKEN.match(condition, pos)
        if not m:
            raise ValueError(f"condição inválida perto de: {condition[pos:pos + 12]!r}")
        out.append(m.group(1))
        pos = m.end()
    return out


def evaluate_condition(condition: str, results: dict[str, bool]) -> bool:
    tokens = tokenize(condition)
    index = 0

    def peek():
        return tokens[index] if index < len(tokens) else None

    def take():
        nonlocal index
        index += 1
        return tokens[index - 1]

    def parse_or():
        value = parse_and()
        while peek() == "or":
            take()
            right = parse_and()
            value = value or right
        return value

    def parse_and():
        value = parse_not()
        while peek() == "and":
            take()
            right = parse_not()
            value = value and right
        return value

    def parse_not():
        if peek() == "not":
            take()
            return not parse_not()
        return parse_atom()

    def parse_atom():
        tok = peek()
        if tok is None:
            raise ValueError("condição incompleta")
        take()
        if tok == "(":
            value = parse_or()
            if peek() != ")":
                raise ValueError("parêntese não fechado")
            take()
            return value
        if tok not in results:
            raise ValueError(f"seleção inexistente na condição: {tok}")
        return results[tok]

    value = parse_or()
    if index != len(tokens):
        raise ValueError("tokens sobrando na condição")
    return value


def evaluate(rule: dict, event: dict) -> str:
    """Retorna match, no_match ou degraded (campo exigido ausente)."""
    if any(not _present(event, f) for f in rule["required_fields"]):
        return "degraded"
    results = {name: selection_matches(sel, event) for name, sel in rule["selections"].items()}
    return "match" if evaluate_condition(rule["condition"], results) else "no_match"


def check_rule(rule: dict) -> list[str]:
    errors = []
    for key in ("id", "title", "case", "required_fields", "selections", "condition"):
        if key not in rule:
            errors.append(f"regra sem {key}")
    if errors:
        return errors
    if not rule["required_fields"]:
        errors.append("required_fields vazio: a regra não declara o contrato de telemetria")
    for name, sel in rule["selections"].items():
        for key in sel:
            field, _, op = key.partition("|")
            if op and op not in OPERATORS:
                errors.append(f"{name}: operador desconhecido {op}")
    try:
        evaluate_condition(rule["condition"], {n: True for n in rule["selections"]})
    except ValueError as err:
        errors.append(str(err))
    return errors


def load_case(name: str) -> tuple[dict, list[dict]]:
    base = LAB / name
    rule = json.loads((base / "rule.json").read_text(encoding="utf-8"))
    fixtures = [
        json.loads(line)
        for line in (base / "fixtures.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    return rule, fixtures


def cases() -> list[str]:
    return sorted(p.name for p in LAB.iterdir() if (p / "rule.json").exists()) if LAB.exists() else []


def run_case(name: str) -> dict:
    rule, fixtures = load_case(name)
    rows = []
    for fx in fixtures:
        got = evaluate(rule, fx["event"])
        rows.append({"name": fx["name"], "class": fx["class"], "expect": fx["expect"], "got": got, "ok": got == fx["expect"]})
    tp = sum(r["got"] == "match" and r["expect"] == "match" for r in rows)
    fn = sum(r["got"] != "match" and r["expect"] == "match" for r in rows)
    fp = sum(r["got"] == "match" and r["expect"] != "match" for r in rows)
    return {
        "case": name,
        "rule": rule["id"],
        "rows": rows,
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "degraded": sum(r["got"] == "degraded" for r in rows),
        "failures": [r for r in rows if not r["ok"]],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    run = sub.add_parser("run")
    run.add_argument("--case", choices=cases() or None)
    run.add_argument("--json", action="store_true")
    args = parser.parse_args()

    reports = [run_case(c) for c in ([args.case] if args.case else cases())]
    if args.json:
        print(json.dumps(reports, ensure_ascii=False, indent=2))
    else:
        for rep in reports:
            print(f"== {rep['case']} ({rep['rule']})")
            for r in rep["rows"]:
                mark = "ok  " if r["ok"] else "FAIL"
                print(f"  {mark} {r['class']:<9} esperado={r['expect']:<8} obtido={r['got']:<8} {r['name']}")
            print(f"  TP={rep['tp']} FP={rep['fp']} FN={rep['fn']} degradados={rep['degraded']}")
        print("\nFixtures sintéticas: validam a lógica da regra, não a telemetria real nem o ruído de produção.")
    return 1 if any(rep["failures"] for rep in reports) else 0


if __name__ == "__main__":
    sys.exit(main())
