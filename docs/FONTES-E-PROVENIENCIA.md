# Fontes e proveniência

[Início](../README.md) · [Metodologia](METODOLOGIA.md)

Registro do que entrou no acervo vindo das notas de estudo do Notion e do que ficou de fora. Importação feita em **24/10/2026** a partir da página de notas "Threat Modeling", que fica sob "Threat Intelligence" no espaço de pesquisa.

## O que virou recurso (`origin: notion`)

| Item da nota | Recurso | Observação |
|---|---|---|
| ThreatModCon | [`threatmodcon`](../data/resources.json) | Conferência dedicada a threat modeling; a nota pede extrair ideias das talks |
| Threat Modeling Intro (guisso.dev) | `guisso-threat-modeling-intro` | O caminho original retornou **404** em 24/10/2026; o registro aponta para a raiz do site |
| CTI Academy | `cti-academy` | Plataforma de estudo; parte exige conta |
| Anvilogic e Tidal Cyber | `anvilogic`, `tidal-cyber` | Plataformas comerciais anotadas para estudo; grau C; não avaliadas aqui |
| Artigo na ScienceDirect (Heliyon) | `tatam-apt-modelling-review` | Título e autoria resolvidos pelo DOI via Crossref |
| Artigo na ScienceDirect (Computer Networks) | `zhang-attack-apt-risk-propagation` | Título e DOI resolvidos via Crossref; autoria como "Zhang et al." |
| Keynote sobre IA agêntica (YouTube) | `sans-keynote-agentic-ai-tm` | Título e canal pelo oEmbed do YouTube |

## O que ficou de fora

- **Capturas de tela** (blocos "Prints" de CTIA e "CTI Tools"): são imagens de material de terceiros e não foram republicadas. Se o conteúdo virar recurso, entra como link para a fonte.
- **Busca no Google** ("ATT&CK Persistent Threat Modelling (APT Modelling)"): é uma pista de pesquisa, não uma fonte. Os dois artigos acima são o resultado desse caminho.
- **Marcação de estudo** ("voltar no minuto 2h12, Aula 03"): anotação pessoal sobre um curso, sem fonte pública para citar.

## Adições de curadoria (`origin: curadoria`)

Para ligar o acervo ao trabalho com IA agêntica e ao [LLMInjection](https://github.com/Ridd1kulusC0d3r/LLmInjection), esta rodada acrescentou OWASP Top 10 para LLM, MITRE ATLAS, PLOT4ai, MAESTRO, OWASP Threat Dragon, Threagile, pytm, o próprio LLMInjection e, para a camada de psicologia da análise, o *Tradecraft Primer* da CIA. São sugestões de leitura, passam pelo mesmo validador e podem ser removidas ou regradadas por quem mantém o acervo.

## Referencial ampliado (`origin: referencial`)

Em **30/10/2026** entraram 144 obras vindas de uma pesquisa bibliográfica sobre modelagem de ameaças, grafos de ataque, CTI, detecção, risco, predição e método de pesquisa. Cada obra teve título, autoria, ano, veículo, DOI ou ISBN e link conferidos em fontes primárias ou indexadores (editora, página do DOI, ACM DL, IEEE Xplore, USENIX, arXiv, sites oficiais). Bases como Crossref, OpenAlex e dblp não puderam ser consultadas diretamente; nesses casos a conferência usou outras fontes.

- **Verificação parcial:** 15 obras têm algum metadado não confirmado. O campo `limit` de cada uma termina com "Metadados verificados em parte; conferir antes de citar".
- **Ficaram de fora por falta de link oficial:** *Threats* (Shostack, 2023), AJP-2.1 (OTAN), *Practical Cyber Intelligence* (Bautista, 2018), *The Goal Question Metric Approach* (Basili et al., 1994) e as normas ABNT NBR ISO/IEC 27001:2022 e 27002:2022. Entram quando houver URL estável.
- **Correções feitas na verificação:** ordem de autoria da 3ª edição de *Structured Analytic Techniques* (Pherson e Heuer), páginas de Verendel (37–49), edição de 2023 da Doutrina da ABIN, separação entre a diretiva BOD 22-01 e o catálogo KEV, versões atuais do CAF (v4.0) e do CPG (2.0).
- **Atenção a versões:** o NIST IR 8286 ganhou a Rev. 1 em dez. 2025; o Decreto 10.222/2020 (E-Ciber) foi, na prática, substituído pelo Decreto 12.573/2025; o status da ABNT NBR ISO/IEC 27005:2023 aparece contraditório em catálogos de terceiros.

## Importar de novo

As notas do Notion são a fonte de origem, não um espelho. Para trazer novas entradas: copie o link para uma issue com o formulário de novo recurso, ou edite `data/resources.json` com `origin: "notion"` e `added` com a data da importação, e rode `make check`.
