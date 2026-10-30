"""Citation rendering (BibTeX and ABNT NBR 6023) from data/resources.json, standard library only.

The output is generated, not hand-checked: it follows ABNT NBR 6023:2018 closely enough to start a reference
list, but punctuation for edge cases (organizations as authors, laws, standards) must be reviewed before deposit.
"""

from __future__ import annotations

import re
import unicodedata

MONTHS = ["jan.", "fev.", "mar.", "abr.", "maio", "jun.", "jul.", "ago.", "set.", "out.", "nov.", "dez."]
ORG_HINTS = re.compile(
    r"\b(MITRE|NIST|OWASP|Microsoft|CISA|NCSC|ENISA|SANS|AWS|Amazon|Google|Splunk|Elastic|Palantir|Rabobank|OASIS|FIRST|IETF|"
    r"ABNT|ISO|IEC|Brasil|ABIN|Agência|Associação|Organização|Organization|Union|Joint Task Force|National|Commission|Comissão|Forum|Special Interest|Comunidade|Autores|Foundation|Center|Centre|Agency|Institute|Project|Projeto|Inc\.?|"
    r"Corporation|SAFECode|OTRF|SigmaHQ|Red Canary|DataDog|Lockheed|CTID|Office|KU Leuven|Cloud Security Alliance|"
    r"Universit|Team|Group|Labs?|Community|Software Engineering|Carnegie|Department|Ministério|Presidência)\b",
    re.I,
)
CONFERENCE_HINTS = re.compile(r"\b(Proceedings|Symposium|Conference|Workshop|Congress|Meeting|USENIX|NDSS|CCS|S&P|ACSAC|NSPW|SOUPS|NAACL|ARES|ICSE|SAC)\b")


def split_authors(raw: str) -> list[str]:
    text = re.sub(r"\.\s*\d+[ªa]?\s*ed\.?$", "", raw.strip())
    text = re.sub(r"\s*\((?:[^)]*)\)\s*$", "", text)
    if ";" in text:
        parts = text.split(";")
    elif ORG_HINTS.search(text) and not re.search(r",|\s+e\s+", text):
        parts = [text]
    else:
        parts = re.split(r",\s*|\s+e\s+|\s+and\s+|\s*&\s*", text)
    return [p.strip().rstrip(".") for p in parts if p.strip() and p.strip().rstrip(".")]


def is_org(name: str) -> bool:
    tokens = name.split()
    acronym = any(len(t) >= 2 and t.isupper() and t.isalpha() for t in tokens)
    return bool(ORG_HINTS.search(name)) or len(tokens) == 1 or acronym


def is_et_al(name: str) -> bool:
    return name.lower().replace(" ", "") in {"etal", "etal."} or name.lower().startswith("et al")


def _people(raw: str) -> tuple[list[str], bool]:
    names = split_authors(raw)
    etal = any(is_et_al(n) or n.lower().endswith(" et al") for n in names)
    clean = []
    for n in names:
        n = re.sub(r"\s+et al\.?$", "", n, flags=re.I).strip()
        if n and not is_et_al(n):
            clean.append(n)
    return clean, etal


# ---------------------------------------------------------------- BibTeX

def bib_escape(text: str) -> str:
    return str(text).replace("\\", "\\\\").replace("&", "\\&").replace("%", "\\%").replace("#", "\\#").replace("_", "\\_")


def bib_author(raw: str) -> str:
    names, etal = _people(raw)
    out = []
    for n in names:
        out.append("{" + bib_escape(n) + "}" if is_org(n) else bib_escape(n))
    if etal:
        out.append("others")
    return " and ".join(out) or "{Anônimo}"


def bib_type(item: dict) -> str:
    venue = item.get("venue", "")
    if item["type"] == "book":
        return "book"
    if item["type"] == "paper":
        if not venue:
            return "misc"
        return "inproceedings" if CONFERENCE_HINTS.search(venue) else "article"
    return "misc"


def bib_key(item: dict) -> str:
    return item["id"]


def render_bib(items: list[dict]) -> str:
    out = [
        "% Gerado por scripts/build_readme.py a partir de data/resources.json. Não edite à mão.",
        "% keywords = temas, grau da fonte (grade-A..E) e 'essential' quando a obra está no núcleo essencial.",
        "",
    ]
    for item in sorted(items, key=lambda i: i["id"]):
        btype = bib_type(item)
        fields: list[tuple[str, str]] = [("author", bib_author(item["authors"])), ("title", "{" + bib_escape(item["title"]) + "}")]
        venue = item.get("venue")
        if venue:
            key = {"article": "journal", "inproceedings": "booktitle", "book": "publisher"}.get(btype, "howpublished")
            fields.append((key, bib_escape(venue)))
        if item.get("year"):
            fields.append(("year", str(item["year"])))
        if item.get("isbn"):
            fields.append(("isbn", item["isbn"]))
        if item.get("doi"):
            fields.append(("doi", item["doi"]))
        fields.append(("url", item["url"]))
        stamp = item.get("checked") or item["added"]
        fields.append(("urldate", stamp))
        fields.append(("langid", "portuguese" if item["lang"] == "pt" else "english"))
        kw = list(item["topics"]) + [f"grade-{item['grade']}"] + (["essential"] if item.get("essential") else [])
        fields.append(("keywords", ", ".join(kw)))
        out.append(f"@{btype}{{{bib_key(item)},")
        out += [f"  {k:<12} = {{{v}}}," for k, v in fields]
        out[-1] = out[-1].rstrip(",")
        out += ["}", ""]
    return "\n".join(out)


# ---------------------------------------------------------------- ABNT

def abnt_person(name: str) -> str:
    parts = name.split()
    if len(parts) == 1:
        return parts[0].upper()
    particles = {"de", "da", "do", "dos", "das", "van", "von", "der", "den", "la", "le"}
    suffix = ""
    if parts[-1].lower().rstrip(".") in {"jr", "junior", "júnior", "filho", "neto"} and len(parts) > 2:
        suffix = " " + ("JR." if parts[-1].lower().startswith("jr") else parts[-1].upper())
        parts = parts[:-1]
    surname, given = parts[-1], parts[:-1]
    while given and given[-1].lower() in particles:
        surname = f"{given.pop()} {surname}"
    return f"{surname.upper()}{suffix}, {' '.join(given)}"


def abnt_authors(raw: str) -> str:
    names, etal = _people(raw)
    if not names:
        return ""
    rendered = [n.upper() if is_org(n) else abnt_person(n) for n in names]
    if len(rendered) > 3 or etal:
        return f"{rendered[0]} et al."
    return "; ".join(rendered)


def abnt_date(iso: str) -> str:
    y, m, d = iso.split("-")
    return f"{int(d)} {MONTHS[int(m) - 1]} {y}"


def render_abnt_entry(item: dict) -> str:
    authors = abnt_authors(item["authors"])
    title = item["title"].strip().rstrip(".")
    if ": " in title and item["type"] in {"book", "guide", "method", "tool", "dataset", "manifesto", "course"}:
        main, sub = title.split(": ", 1)
        title_txt = f"**{main.strip()}**: {sub.strip()}"
    elif item["type"] == "paper" and item.get("venue"):
        title_txt = title
    else:
        title_txt = f"**{title}**"
    end = "" if title_txt.rstrip("*").endswith(("?", "!")) else "."
    parts = [f"{authors}." if authors and not authors.endswith(".") else authors, f"{title_txt}{end}"]
    venue = item.get("venue")
    year = item.get("year")
    if item["type"] == "paper" and venue:
        parts.append(f"**{venue.rstrip('.')}**, {year}." if year else f"**{venue.rstrip('.')}**.")
    elif venue:
        parts.append(f"{venue.rstrip('.')}, {year}." if year else f"{venue.rstrip('.')}.")
    elif year:
        parts.append(f"{year}.")
    if item.get("isbn"):
        parts.append(f"ISBN {item['isbn']}.")
    if item.get("doi"):
        parts.append(f"DOI: {item['doi']}.")
    parts.append(f"Disponível em: {item['url']}.")
    parts.append(f"Acesso em: {abnt_date(item.get('checked') or item['added'])}.")
    return " ".join(p for p in parts if p and p != ".")


def sort_name(item: dict) -> str:
    text = abnt_authors(item["authors"]) or item["title"]
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower() + " " + str(item.get("year") or "")


def render_abnt(items: list[dict]) -> str:
    out = [
        "# Referências (ABNT NBR 6023)",
        "",
        "[Início](../README.md) · [Bibliografia comentada](BIBLIOGRAFIA.md) · [Trilha de leitura](TRILHA-DE-LEITURA.md) · "
        "[BibTeX](../referencias/referencias.bib)",
        "",
        "> Arquivo **gerado** por `scripts/build_readme.py` a partir de [`data/resources.json`](../data/resources.json). "
        "Segue a ABNT NBR 6023:2018 de forma aproximada: revise pontuação de autoria institucional, leis e normas antes de "
        "depositar um trabalho. A data de acesso é a da última verificação do link ou, sem ela, a da inclusão no acervo.",
        "",
        "⭐ núcleo essencial · a letra entre colchetes é o [grau da fonte](METODOLOGIA.md#graus-de-fonte).",
        "",
    ]
    for item in sorted(items, key=sort_name):
        star = " ⭐" if item.get("essential") else ""
        out.append(f"- {render_abnt_entry(item)} **[{item['grade']}]**{star}")
    out.append("")
    return "\n".join(out)
