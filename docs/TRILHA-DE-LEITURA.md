# Trilha de leitura — Threat Modeling

Um caminho de 15 semanas pela [bibliografia comentada](BIBLIOGRAFIA.md), uma leitura por vez. Cada passo tem uma ação e uma saída. Marque a caixa quando registrar a saída.

## Como usar cada passo

1. Abra a fonte original (links e DOIs estão na [bibliografia](BIBLIOGRAFIA.md)).
2. Leia só o trecho indicado.
3. Registre em três linhas: **o que ensina**, **para qual contexto foi escrito** e **qual dúvida ficou**.

O objetivo é formar critério, não acumular leituras.

## Núcleo essencial

Obras marcadas com ⭐ na bibliografia. Se o tempo for curto, leia estas antes de qualquer outra.

| Tema | Obras |
|---|---|
| Processo e estado da arte | Shostack (2014) · Threat Modeling Manifesto · Xiong & Lagerström (2019) |
| Ambiente corporativo | Johnson, Lagerström & Ekstedt (2018) — MAL · Xiong et al. (2022) — enterpriseLang |
| Árvores e grafos | Kordy, Piètre-Cambacédès & Schweitzer (2014) · Sheyner et al. (2002) · Ou et al. (2005) — MulVAL · Poolsappasit, Dewri & Ray (2012) · Lallie, Debattista & Bal (2020) |
| Análise de inteligência | Heuer (1999) · Heuer & Pherson (2020) · Kent (1964) · ICD 203 · Diamond Model (2013) · Kill Chain (2011) · Strom et al. — ATT&CK |
| Qualidade de CTI | Wagner et al. (2019) · Schlette, Caselli & Pernul (2021) · Li et al. (2019) |
| Detecção | Roddie, Deyalsingh & Katz (2023) · D3FEND (2021) · Virkud et al. (2024) · Alahmadi, Axon & Martinovic (2022) |
| Risco e priorização | EPSS (2021; 2023) · SSVC (2019) · Hubbard & Seiersen (2023) · Verendel (2009) |
| Predição | Husák et al. (2019) |
| Método de pesquisa | Hevner et al. (2004) · Peffers et al. (2007) · Wieringa (2014) |

## Bloco 1 — Fundamentos (semanas 1–3)

- [ ] **Semana 1.** Leia o [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org) e os capítulos 1–3 de Shostack (2014). Saída: as quatro perguntas aplicadas a um sistema que você conhece.
- [ ] **Semana 2.** Leia Xiong & Lagerström (2019). Saída: uma tabela com cinco métodos citados e o tipo de validação que cada um teve.
- [ ] **Semana 3.** Leia *MITRE ATT&CK: Design and Philosophy* (Strom et al.). Saída: a diferença entre tática, técnica e procedimento em suas palavras.

## Bloco 2 — O ambiente como grafo (semanas 4–6)

- [ ] **Semana 4.** Leia Kordy et al. (2014), seções de introdução e taxonomia. Saída: quando usar árvore e quando usar grafo.
- [ ] **Semana 5.** Leia Johnson et al. (2018) e Xiong et al. (2022). Saída: quais objetos do seu ambiente virariam ativos, passos e defesas.
- [ ] **Semana 6.** Leia Poolsappasit, Dewri & Ray (2012) e Wang, Noel & Jajodia (2006). Saída: como cada um escolhe mitigações com orçamento limitado.

## Bloco 3 — Inteligência e incerteza (semanas 7–9)

- [ ] **Semana 7.** Leia Heuer (1999), capítulos sobre vieses e ACH. Saída: uma matriz ACH com três hipóteses para um incidente real ou público.
- [ ] **Semana 8.** Leia Kent (1964) e a ICD 203. Saída: uma régua de termos de probabilidade para usar nos seus relatórios.
- [ ] **Semana 9.** Leia Li et al. (2019) e Wagner et al. (2019). Saída: três critérios para decidir quanto confiar em um feed.

## Bloco 4 — Da ameaça à detecção (semanas 10–12)

- [ ] **Semana 10.** Leia Roddie, Deyalsingh & Katz (2023), capítulos sobre requisitos e validação, e o Palantir ADS. Saída: uma especificação de detecção para uma técnica do seu modelo.
- [ ] **Semana 11.** Leia Virkud et al. (2024) e Alahmadi, Axon & Martinovic (2022). Saída: por que “porcentagem de cobertura ATT&CK” engana.
- [ ] **Semana 12.** Leia Holeman et al. (2026) e Tan et al. (2026), ambos preprints, e veja o DeTT&CT. Saída: uma lista de passos do seu modelo que hoje não deixariam rastro.

## Bloco 5 — Risco, predição e calibração (semanas 13–15)

- [ ] **Semana 13.** Leia Hubbard & Seiersen (2023), partes sobre calibração, e Verendel (2009). Saída: o que falta para um escore de risco ser defensável.
- [ ] **Semana 14.** Leia Jacobs et al. (2021; 2023) e SSVC. Saída: como o EPSS foi validado e o que você copiaria dessa validação.
- [ ] **Semana 15.** Leia Husák et al. (2019) e Liu et al. (2015). Saída: a diferença entre projeção, predição e previsão, com um exemplo de cada.

## Em paralelo, para quem vai publicar

- [ ] Hevner et al. (2004) e Peffers et al. (2007): estrutura de Design Science.
- [ ] Wieringa (2014): como validar um artefato.
- [ ] Kitchenham & Charters (2007) ou Petersen et al. (2015): protocolo de revisão ou mapeamento.
- [ ] Basili et al. (1994): métricas a partir de objetivos (GQM).

[Início](../README.md) · [Bibliografia](BIBLIOGRAFIA.md) · [Catálogo](CATALOGO.md)
