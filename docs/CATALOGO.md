# Biblioteca de manuais e métodos

> **Lista estruturada:** os links desta tabela também estão em [`data/resources.json`](../data/resources.json), com grau, acesso e limite, e na [lista gerada](AWESOME.md). Este texto mantém o comentário editorial.

Seleção organizada por finalidade. Links históricos não consultados nesta rodada estão identificados abaixo. Não são apresentados como validação de disponibilidade ou atualização.

## Processo e introdução

| Manual | Uso |
|---|---|
| [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) | Entender o processo e suas perguntas fundamentais; fonte consultada nesta edição |
| [OWASP Developer Guide — Threat Modeling](https://devguide.owasp.org/en/04-design/01-threat-modeling/) | Relacionar modelagem ao desenvolvimento; fonte localizada nesta edição |

## Métodos e aplicação — acervo a revalidar

| Referência original preservada | Finalidade | Nota editorial |
|---|---|---|
| [Microsoft STRIDE](https://learn.microsoft.com/pt-br/azure/security/develop/threat-modeling-tool-threats) | Categorias de ameaça em desenho de sistemas | Link herdado; conferir versão atual |
| [PASTA — VerSprite](https://versprite.com/blog/what-is-pasta-threat-modeling/) | Abordagem orientada a risco e análise de ataques | Material do proponente; não comparação independente |
| [AWS Threat Modeling Workshop](https://catalog.workshops.aws/threatmodel/en-US/introduction/what-is-threat-modeling) | Aplicação em exercícios | Link herdado; conferir requisitos |
| [GitLab AppSec Threat Modeling](https://handbook.gitlab.com/handbook/security/product-security/application-security/runbooks/threat-modeling/) | Processo de uma equipe de produto | Contexto específico de organização |
| [OpenStack Threat Analysis](https://wiki.openstack.org/wiki/Security/Threat_Analysis) | Exemplo de processo em plataforma | Material histórico; conferir atualidade |
| [Elevation of Privilege](https://github.com/adamshostack/eop) | Facilitação com cartas | Ferramenta de discussão; não substitui análise |

## Livros e leitura acadêmica

Livros, artigos e normas estão na [bibliografia ABNT](BIBLIOGRAFIA-COMENTADA.md) (131 obras em 13 eixos, ABNT + BibTeX), com uma [trilha de leitura](TRILHA-DE-LEITURA.md) de 15 semanas.

## Métodos complementares

| Referência | Finalidade | Nota editorial |
|---|---|---|
| [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/) | Valores, princípios e as quatro perguntas | Consultado em 22/10/2026 |
| [LINDDUN](https://linddun.org/) | Ameaças à privacidade | Site oficial; não foi possível consultar nesta edição |
| PASTA — UcedaVélez & Morana (2015) | Modelagem centrada em risco de negócio | Livro dos proponentes; ver [bibliografia](BIBLIOGRAFIA-COMENTADA.md#1-fundamentos) |

## Modelagem como código e ferramentas

Repositórios públicos confirmados em 22/10/2026. Confirmar maturidade, manutenção e licença antes de adotar.

| Ferramenta | Uso | Nota editorial |
|---|---|---|
| [OWASP pytm](https://github.com/OWASP/pytm) | Descrever o sistema em Python e gerar DFD e ameaças | Usado em Tarandach & Coles (2020) |
| [Threagile](https://threagile.io/) | Modelo em YAML com análise de riscos automatizada | Agile threat modeling as code |
| [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/) | Diagramas e ameaças em interface gráfica | Bom para facilitar sessões |
| [AWS Threat Composer](https://github.com/awslabs/threat-composer) | Declarações de ameaça estruturadas e mitigação | Orientado a times de produto |
| [enterpriseLang (MAL)](https://github.com/mal-lang/enterpriselang) | Simular caminhos de ataque em arquiteturas corporativas | Base de Xiong et al. (2022) |
| [Elevation of Privilege](https://github.com/adamshostack/eop) | Facilitação com cartas | Já listado acima |

## IA e agentes

| Referência | Uso | Nota editorial |
|---|---|---|
| [MITRE ATLAS](https://atlas.mitre.org/) | Táticas e técnicas contra sistemas de IA | Consultado em 22/10/2026 |
| [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/) | Riscos de aplicações com LLM | Edição 2025 confirmada em 22/10/2026 |
| [CSA MAESTRO](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro) | Modelagem por camadas para IA agêntica | Publicado em 06/02/2025; framework recente |

## Pontes com inteligência e detecção

Ajudam a levar o resultado do modelo para monitoramento. Não são métodos de modelagem.

| Referência | Uso | Nota editorial |
|---|---|---|
| [Attack Flow](https://center-for-threat-informed-defense.github.io/attack-flow/) | Representar sequências de técnicas | MITRE CTID |
| [MITRE D3FEND](https://d3fend.mitre.org/) | Contramedidas ligadas a técnicas | Ontologia; ver Kaloroumakis & Smith (2021) |
| [TRAM](https://github.com/center-for-threat-informed-defense/tram) | Mapear relatórios para ATT&CK com apoio de ML | Saída exige revisão humana |
| [DeTT&CT](https://github.com/rabobank-cdc/DeTTECT) | Visibilidade e qualidade de fontes de dados por técnica | Útil para achar lacunas de telemetria |
| [Summiting the Pyramid](https://center-for-threat-informed-defense.github.io/summiting-the-pyramid/) | Robustez de analíticas | v2, dez. 2024 |
| [Palantir ADS](https://github.com/palantir/alerting-detection-strategy-framework) | Modelo de especificação de detecção | Inclui pontos cegos e validação |
| [Sigma specification](https://sigmahq.io/sigma-specification/specification/sigma-correlation-rules-specification.html) | Formato portátil de regras | — |

## Normas e guias oficiais

Links oficiais; conferir a versão vigente antes de citar.

| Referência | Uso |
|---|---|
| [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) | Avaliação de risco |
| [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) | Catálogo de controles |
| [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final) | Arquitetura zero trust |
| [NIST CSF 2.0](https://www.nist.gov/cyberframework) | Estrutura de gestão de cibersegurança |
| ISO/IEC 27005:2022 · ABNT NBR ISO/IEC 27005:2023 | Gestão de riscos de segurança da informação (confirmar status da edição ABNT) |
| [FIRST CVSS v4.0](https://www.first.org/cvss/v4.0/specification-document) | Severidade técnica |
| [FIRST EPSS](https://www.first.org/epss/) | Probabilidade de exploração |
| [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | Vulnerabilidades com exploração confirmada |
| [CERT/CC SSVC](https://certcc.github.io/SSVC/) | Priorização por árvore de decisão |

## Contexto complementar

[MITRE ATT&CK](https://attack.mitre.org/) ajuda a contextualizar comportamentos, mas não equivale a um método completo de modelagem. [NIST SSDF](https://csrc.nist.gov/projects/ssdf) conecta práticas de segurança ao desenvolvimento.

DREAD e demais links do README anterior permanecem no [acervo histórico](ACERVO-ANTERIOR.md), sem recomendação automática de adoção.

## Relação com TCEM

Este repositório organiza manuais de terceiros. O [TCEM](https://github.com/Ridd1kulusC0d3r/Cyber-Threat-Context-Modeling) mantém a especificação do método autoral, a Operational Matrix, exemplos e implementação. Referenciar TCEM não converte este catálogo em uma segunda sede da metodologia.

## Adicionar um manual

Informe autor, URL original, método, nível, contexto, versão/data, razão de inclusão e limitações. Não copie livros ou documentos integrais sem autorização.


## Novas rotas de aplicação

- [Bibliografia comentada](BIBLIOGRAFIA-COMENTADA.md): fundamentos e trabalhos relacionados.
- [Engenharia de detecção](ENGENHARIA-DE-DETECCAO.md): observáveis, datasets e validação.
- [Conferências](CONFERENCIAS.md): apresentações e exercícios.
- [Cases](../cases/README.md): roteiros educacionais, não executados.

Os links históricos acima permanecem identificados como tais; a inclusão de novas fontes não valida automaticamente o acervo anterior.
