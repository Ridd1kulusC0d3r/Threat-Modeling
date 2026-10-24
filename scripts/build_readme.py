#!/usr/bin/env python3
"""Generate the browsable lists from data/*.json.

Writes docs/AWESOME.md, docs/TEMAS.md and docs/METODOS.md in full, and refreshes the
`<!-- gen:NAME:start -->` ... `<!-- gen:NAME:end -->` blocks in README.md and README.en.md.
Use --check in CI: it exits 1 when a generated file is out of date.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (  # noqa: E402
    ACCESS, GRADES, LEVELS, METHOD_STATUS, ROOT, TOPICS, TYPES, methods, resources,
)

TYPE_ORDER = list(TYPES)
EN_TYPES = {
    "manifesto": "Manifestos and principles", "guide": "Guides and frameworks", "method": "Methods and models",
    "book": "Books", "paper": "Papers", "article": "Articles and posts", "conference": "Talks and conferences",
    "course": "Courses", "tool": "Tools and repositories", "dataset": "Datasets and catalogs",
}
EN_TOPICS = {
    "threat-modeling": "Threat modeling", "detection-engineering": "Detection engineering",
    "cti": "Cyber threat intelligence", "apt": "APT and persistent campaigns", "ai": "AI and agentic systems",
    "ics-cps": "ICS and cyber-physical systems", "privacy": "Privacy", "psychology": "Psychology, bias and analysis",
    "emulation": "Adversary emulation", "provenance": "Provenance and graphs", "cloud": "Cloud",
    "supply-chain": "Supply chain",
}
EN_GRADES = {
    "A": "Primary or institutional: standard, public body, peer-reviewed or the method's maintainer.",
    "B": "Primary without formal review: book, preprint, community guide, author page or maintainer repository.",
    "C": "Vendor or commercial proponent material, or a third-party tool.",
    "D": "Commentary or secondary source.",
    "E": "Legacy: inherited from the earlier collection and not yet revalidated.",
}


def cell(text: str) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def anchor(heading: str) -> str:
    slug = re.sub(r"[^\w\s-]", "", heading.lower(), flags=re.UNICODE)
    return re.sub(r"\s", "-", slug.strip())


def link(item: dict) -> str:
    return f"[{cell(item['title'])}]({item['url']})"


def sort_key(item: dict):
    return (item["grade"], -(item["year"] or 0), item["title"].lower())


def by_type(items):
    for t in TYPE_ORDER:
        group = sorted((i for i in items if i["type"] == t), key=sort_key)
        if group:
            yield t, group


def render_awesome(items: list[dict]) -> str:
    out = [
        "# Acervo completo",
        "",
        "[Início](../README.md) · [Por tema](TEMAS.md) · [Métodos](METODOS.md) · [Metodologia](METODOLOGIA.md)",
        "",
        "> Arquivo **gerado** por `scripts/build_readme.py` a partir de [`data/resources.json`](../data/resources.json). "
        "Edite os dados, não este arquivo.",
        "",
        "Cada linha traz o **grau da fonte** (A–E, [o que significa](METODOLOGIA.md#graus-de-fonte)), o acesso, "
        "o nível e o **limite** conhecido. Grau mede o tipo de fonte, não a qualidade das ideias.",
        "",
        "| Tipo | Recursos |",
        "|---|---|",
    ]
    for t, group in by_type(items):
        out.append(f"| [{TYPES[t]}](#{anchor(TYPES[t])}) | {len(group)} |")
    for t, group in by_type(items):
        out += ["", f"## {TYPES[t]}", "", "| Recurso | Autoria | Acesso | Grau | Nível | Por que ler | Limite |", "|---|---|---|---|---|---|---|"]
        for i in group:
            year = f" ({i['year']})" if i.get("year") else ""
            out.append(
                f"| {link(i)} | {cell(i['authors'])}{year} | {ACCESS[i['access']]} | **{i['grade']}** | "
                f"{LEVELS[i['level']]} | {cell(i['summary'])} | {cell(i['limit'])} |"
            )
    out.append("")
    return "\n".join(out)


def render_topics(items: list[dict]) -> str:
    out = [
        "# Recursos por tema",
        "",
        "[Início](../README.md) · [Acervo completo](AWESOME.md) · [Métodos](METODOS.md)",
        "",
        "> Arquivo **gerado** por `scripts/build_readme.py`. Um recurso pode aparecer em mais de um tema. "
        "A letra entre colchetes é o [grau da fonte](METODOLOGIA.md#graus-de-fonte).",
        "",
        "| Tema | Recursos |",
        "|---|---|",
    ]
    present = [t for t in TOPICS if any(t in i["topics"] for i in items)]
    for t in present:
        out.append(f"| [{TOPICS[t]}](#{anchor(TOPICS[t])}) | {sum(t in i['topics'] for i in items)} |")
    for t in present:
        out += ["", f"## {TOPICS[t]}", ""]
        for i in sorted((i for i in items if t in i["topics"]), key=sort_key):
            tags = f"{TYPES[i['type']].split(' e ')[0].lower()}, {ACCESS[i['access']]}"
            out.append(f"- {link(i)} **[{i['grade']}]** — {cell(i['summary'])} _({tags})_")
    out.append("")
    return "\n".join(out)


def render_methods(meths: list[dict], items: list[dict]) -> str:
    by_id = {i["id"]: i for i in items}
    out = [
        "# Métodos de modelagem",
        "",
        "[Início](../README.md) · [Acervo completo](AWESOME.md) · [Por tema](TEMAS.md)",
        "",
        "> Arquivo **gerado** por `scripts/build_readme.py` a partir de [`data/methods.json`](../data/methods.json). "
        "Cada método cita as fontes do acervo que o sustentam; escolher um método é decisão do problema, não de moda.",
        "",
        "| Método | Abordagem | Pergunta que responde | Estado |",
        "|---|---|---|---|",
    ]
    for m in meths:
        out.append(f"| [{cell(m['name'])}](#{anchor(m['name'])}) | {m['approach']} | {cell(m['question'])} | {METHOD_STATUS[m['status']]} |")
    for m in meths:
        out += ["", f"## {m['name']}", "",
                f"**Pergunta:** {m['question']}", "",
                f"- **Centrado em:** {m['centered_on']}",
                f"- **Produz:** {m['outputs']}",
                f"- **Use quando:** {m['use_when']}",
                f"- **Limite:** {m['limits']}",
                f"- **Estado:** {METHOD_STATUS[m['status']]}"]
        if m.get("psychology"):
            out.append("- **Psicologia da análise:** método voltado a reduzir vieses cognitivos.")
        out.append("- **Fontes:** " + "; ".join(f"{link(by_id[r])} [{by_id[r]['grade']}]" for r in m["resources"]))
    out.append("")
    return "\n".join(out)


def stats_block(items, meths, lang: str) -> str:
    checked = sum(1 for i in items if i.get("checked"))
    grades = Counter(i["grade"] for i in items)
    topics = {t for i in items for t in i["topics"]}
    ptypes = Counter(i["type"] for i in items)
    gl = EN_GRADES if lang == "en" else GRADES
    if lang == "en":
        head = ["| Resources | Methods | Types | Topics | Links checked |", "|:---:|:---:|:---:|:---:|:---:|"]
        gh = ["| Grade | Resources | Meaning |", "|:---:|:---:|---|"]
    else:
        head = ["| Recursos | Métodos | Tipos | Temas | Links verificados |", "|:---:|:---:|:---:|:---:|:---:|"]
        gh = ["| Grau | Recursos | Significado |", "|:---:|:---:|---|"]
    row = f"| **{len(items)}** | **{len(meths)}** | **{len(ptypes)}** | **{len(topics)}** | **{checked}** |"
    grade_rows = [f"| **{g}** | {grades.get(g, 0)} | {gl[g]} |" for g in GRADES]
    return "\n".join(head + [row, ""] + gh + grade_rows)


def featured_block(items, lang: str) -> str:
    types = EN_TYPES if lang == "en" else TYPES
    if lang == "en":
        rows = ["| Start with | Type | Grade | Why |", "|---|---|:---:|---|"]
    else:
        rows = ["| Comece por | Tipo | Grau | Por quê |", "|---|---|:---:|---|"]
    for i in sorted((i for i in items if i["featured"]), key=lambda i: (TYPE_ORDER.index(i["type"]), i["title"].lower())):
        rows.append(f"| {link(i)} | {types[i['type']]} | **{i['grade']}** | {cell(i['summary'])} |")
    return "\n".join(rows)


def topics_block(items, lang: str) -> str:
    labels = EN_TOPICS if lang == "en" else TOPICS
    rows = ["| Topic | Resources |", "|---|:---:|"] if lang == "en" else ["| Tema | Recursos |", "|---|:---:|"]
    for t in TOPICS:
        n = sum(t in i["topics"] for i in items)
        if n:
            rows.append(f"| [{labels[t]}](docs/TEMAS.md#{anchor(TOPICS[t])}) | {n} |")
    return "\n".join(rows)


def replace_block(text: str, name: str, body: str) -> str:
    pattern = re.compile(rf"(<!-- gen:{name}:start -->)(.*?)(<!-- gen:{name}:end -->)", re.S)
    if not pattern.search(text):
        raise SystemExit(f"marcador gen:{name} ausente")
    return pattern.sub(lambda m: m.group(1) + "\n\n" + body + "\n\n" + m.group(3), text)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated files are out of date")
    args = parser.parse_args()

    items, meths = resources(), methods()
    outputs: dict[Path, str] = {
        ROOT / "docs/AWESOME.md": render_awesome(items),
        ROOT / "docs/TEMAS.md": render_topics(items),
        ROOT / "docs/METODOS.md": render_methods(meths, items),
    }
    for readme, lang in ((ROOT / "README.md", "pt"), (ROOT / "README.en.md", "en")):
        text = readme.read_text(encoding="utf-8")
        for name, body in (
            ("stats", stats_block(items, meths, lang)),
            ("featured", featured_block(items, lang)),
            ("topics", topics_block(items, lang)),
        ):
            text = replace_block(text, name, body)
        outputs[readme] = text

    stale = [p for p, content in outputs.items() if not p.exists() or p.read_text(encoding="utf-8") != content]
    if args.check:
        if stale:
            print("desatualizado (rode `make build`):", *[str(p.relative_to(ROOT)) for p in stale], sep="\n  ")
            return 1
        print("ok: arquivos gerados estão em dia")
        return 0
    for path, content in outputs.items():
        path.write_text(content, encoding="utf-8")
    print("escrito:", *[str(p.relative_to(ROOT)) for p in outputs], sep="\n  ")
    return 0


if __name__ == "__main__":
    sys.exit(main())
