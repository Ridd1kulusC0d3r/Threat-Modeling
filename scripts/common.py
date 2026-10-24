"""Shared constants and loaders for the Threat Modeling library (standard library only)."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

GRADES = {
    "A": "Fonte primária ou institucional: padrão, órgão público, publicação com revisão por pares ou mantenedor do método.",
    "B": "Fonte primária sem revisão formal: livro, preprint, guia de comunidade, página do autor ou repositório do mantenedor.",
    "C": "Material de fornecedor, proponente comercial ou ferramenta de terceiros.",
    "D": "Comentário ou fonte secundária.",
    "E": "Legado: herdado do acervo anterior e ainda não revalidado.",
}
TYPES = {
    "manifesto": "Manifestos e princípios",
    "guide": "Guias e frameworks",
    "method": "Métodos e modelos",
    "book": "Livros",
    "paper": "Papers e trabalhos técnicos",
    "article": "Artigos e posts",
    "conference": "Conferências e talks",
    "course": "Cursos e plataformas de estudo",
    "tool": "Ferramentas e repositórios",
    "dataset": "Datasets e catálogos",
}
TOPICS = {
    "threat-modeling": "Modelagem de ameaças",
    "detection-engineering": "Engenharia de detecção",
    "cti": "Inteligência de ameaças (CTI)",
    "apt": "APT e campanhas persistentes",
    "ai": "IA e sistemas agênticos",
    "ics-cps": "ICS e sistemas ciberfísicos",
    "privacy": "Privacidade",
    "psychology": "Psicologia, vieses e análise",
    "emulation": "Emulação adversária",
    "provenance": "Proveniência e grafos",
    "cloud": "Nuvem",
    "supply-chain": "Cadeia de suprimentos",
}
ACCESS = {
    "free": "gratuito",
    "open-access": "acesso aberto",
    "preprint": "preprint",
    "mixed": "parcial",
    "paid": "pago",
}
LEVELS = {"intro": "introdutório", "intermediate": "intermediário", "advanced": "avançado"}
LANGS = {"en": "EN", "pt": "PT"}
ORIGINS = {"bibliografia", "engenharia", "conferencias", "catalogo", "acervo", "referencias", "notion", "curadoria"}
APPROACHES = {"processo", "software", "risco", "arquitetura", "privacidade", "atacante", "inteligência", "simulação", "ia"}
METHOD_STATUS = {
    "core": "núcleo",
    "emerging": "emergente",
    "complementary": "complementar",
    "legacy": "legado",
}
MAX_FEATURED = 20


def load(name: str):
    with (DATA / name).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def resources() -> list[dict]:
    return load("resources.json")


def methods() -> list[dict]:
    return load("methods.json")
