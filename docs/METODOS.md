# Métodos de modelagem

[Início](../README.md) · [Acervo completo](AWESOME.md) · [Por tema](TEMAS.md)

> Arquivo **gerado** por `scripts/build_readme.py` a partir de [`data/methods.json`](../data/methods.json). Cada método cita as fontes do acervo que o sustentam; escolher um método é decisão do problema, não de moda.

| Método | Abordagem | Pergunta que responde | Estado |
|---|---|---|---|
| [Quatro perguntas de Shostack](#quatro-perguntas-de-shostack) | processo | O que estamos construindo? O que pode dar errado? O que vamos fazer a respeito? Fizemos um bom trabalho? | núcleo |
| [STRIDE](#stride) | software | O que pode dar errado em cada elemento e fronteira do desenho? | núcleo |
| [PASTA](#pasta) | risco | Qual ataque realista causa impacto de negócio, dado o contexto técnico? | núcleo |
| [ATASM](#atasm) | arquitetura | Quais superfícies de ataque a arquitetura expõe e quais mitigações se aplicam? | núcleo |
| [LINDDUN](#linddun) | privacidade | Quais ameaças de privacidade existem no fluxo de dados? | núcleo |
| [Árvores de ataque](#árvores-de-ataque) | atacante | Como um atacante alcança este objetivo e quais condições o impedem? | núcleo |
| [Modelo Diamante](#modelo-diamante) | inteligência | Quem fez o quê, com qual capacidade, infraestrutura e contra qual vítima? | núcleo |
| [Intrusion Kill Chain](#intrusion-kill-chain) | inteligência | Em que fase uma campanha pode ser interrompida? | núcleo |
| [Threat Modeling com ATT&CK](#threat-modeling-com-attck) | atacante | Que comportamentos adversários são relevantes para esta arquitetura? | núcleo |
| [Attack Flow](#attack-flow) | atacante | Em que sequência os comportamentos se encadeiam? | núcleo |
| [TARA (MITRE)](#tara-mitre) | risco | Quais ameaças priorizar e quais contramedidas selecionar? | núcleo |
| [enterpriseLang / MAL](#enterpriselang--mal) | simulação | Quais caminhos de ataque a arquitetura permite, dado o modelo de ativos? | emergente |
| [Análise de Hipóteses Concorrentes](#análise-de-hipóteses-concorrentes) | inteligência | Qual hipótese é menos inconsistente com a evidência? | complementar |
| [DREAD](#dread) | risco | Qual a gravidade relativa desta ameaça? | legado |
| [STRIDE-LM](#stride-lm) | software | O que pode dar errado, incluindo movimento lateral? | legado |
| [MITRE ATLAS](#mitre-atlas) | ia | Que técnicas adversárias visam sistemas de IA? | emergente |
| [OWASP Top 10 para LLM](#owasp-top-10-para-llm) | ia | Quais riscos comuns afetam aplicações com LLM? | emergente |
| [PLOT4ai](#plot4ai) | ia | Quais ameaças de IA, privacidade e responsabilidade se aplicam? | emergente |
| [MAESTRO](#maestro) | ia | Que ameaças existem em cada camada de um sistema de IA agêntica? | emergente |

## Quatro perguntas de Shostack

**Pergunta:** O que estamos construindo? O que pode dar errado? O que vamos fazer a respeito? Fizemos um bom trabalho?

- **Centrado em:** processo
- **Produz:** Modelo, lista de ameaças, respostas e revisão
- **Use quando:** Como esqueleto de qualquer sessão de modelagem, antes de escolher técnica.
- **Limite:** É um quadro de processo, não uma técnica de enumeração.
- **Estado:** núcleo
- **Fontes:** [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/) [B]; [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) [B]; [Threat Modeling: What, Why, and How?](https://shostack.org/resources/whitepapers/threat-modeling-what-why-how) [B]

## STRIDE

**Pergunta:** O que pode dar errado em cada elemento e fronteira do desenho?

- **Centrado em:** software
- **Produz:** Ameaças por categoria (spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege)
- **Use quando:** Desenhos de software com diagrama de fluxo de dados e fronteiras de confiança.
- **Limite:** Categoriza, mas não prioriza risco; depende da qualidade do diagrama.
- **Estado:** núcleo
- **Fontes:** [Microsoft STRIDE](https://learn.microsoft.com/pt-br/azure/security/develop/threat-modeling-tool-threats) [E]; [Threat Modeling: Designing for Security](https://threatmodelingbook.com/books) [B]; [Elevation of Privilege](https://github.com/adamshostack/eop) [E]; [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/) [B]

## PASTA

**Pergunta:** Qual ataque realista causa impacto de negócio, dado o contexto técnico?

- **Centrado em:** risco
- **Produz:** Cenários de ataque ligados a objetivos de negócio e impacto, em sete etapas
- **Use quando:** Quando é preciso ligar arquitetura, ameaça e impacto de negócio.
- **Limite:** Processo pesado; material de proponentes não é comparação independente.
- **Estado:** núcleo
- **Fontes:** [Risk Centric Threat Modeling: Process for Attack Simulation and Threat Analysis](https://onlinelibrary.wiley.com/doi/book/10.1002/9781118988374) [B]; [PASTA — VerSprite](https://versprite.com/blog/what-is-pasta-threat-modeling/) [E]

## ATASM

**Pergunta:** Quais superfícies de ataque a arquitetura expõe e quais mitigações se aplicam?

- **Centrado em:** arquitetura
- **Produz:** Arquitetura, ameaças, superfícies de ataque e mitigações
- **Use quando:** Revisão de arquitetura de segurança antes da implementação.
- **Limite:** Exige arquitetura real documentada.
- **Estado:** núcleo
- **Fontes:** [ATASM](https://brookschoenfield.com/?page_id=341) [B]; [Securing Systems: Applied Security Architecture and Threat Models](https://brookschoenfield.com/?page_id=245) [B]

## LINDDUN

**Pergunta:** Quais ameaças de privacidade existem no fluxo de dados?

- **Centrado em:** privacidade
- **Produz:** Ameaças de vinculação, identificação, não repúdio, detecção, divulgação, desconhecimento e não conformidade
- **Use quando:** Sistemas que tratam dados pessoais.
- **Limite:** Vai além de confidencialidade; exige conhecimento do domínio de dados.
- **Estado:** núcleo
- **Fontes:** [LINDDUN](https://linddun.org/) [B]; [Threat Models over Space and Time: A Case Study of E2EE Messaging Applications](https://arxiv.org/abs/2301.05653) [B]

## Árvores de ataque

**Pergunta:** Como um atacante alcança este objetivo e quais condições o impedem?

- **Centrado em:** atacante
- **Produz:** Árvore com objetivo, caminhos alternativos e condições
- **Use quando:** Decompor um objetivo adversário em caminhos comparáveis.
- **Limite:** A árvore não prova probabilidade real; custos e chances são estimativas.
- **Estado:** núcleo
- **Fontes:** [Attack Trees](https://www.schneier.com/academic/archives/1999/12/attack_trees.html) [B]

## Modelo Diamante

**Pergunta:** Quem fez o quê, com qual capacidade, infraestrutura e contra qual vítima?

- **Centrado em:** inteligência
- **Produz:** Eventos descritos por adversário, capacidade, infraestrutura e vítima, e pivôs entre eles
- **Use quando:** Análise e correlação de intrusões.
- **Limite:** Correlação não confirma atribuição.
- **Estado:** núcleo
- **Fontes:** [The Diamond Model of Intrusion Analysis](https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf) [B]

## Intrusion Kill Chain

**Pergunta:** Em que fase uma campanha pode ser interrompida?

- **Centrado em:** inteligência
- **Produz:** Campanha descrita em fases e pontos de interrupção
- **Use quando:** Pensar defesas por fase de uma intrusão.
- **Limite:** Não force todos os casos a uma sequência linear.
- **Estado:** núcleo
- **Fontes:** [Intelligence-Driven Computer Network Defense Informed by Analysis of Adversary Campaigns and Intrusion Kill Chains](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf) [B]

## Threat Modeling com ATT&CK

**Pergunta:** Que comportamentos adversários são relevantes para esta arquitetura?

- **Centrado em:** atacante
- **Produz:** Modelo de ameaças ancorado em técnicas ATT&CK relevantes
- **Use quando:** Quando já existe arquitetura e se precisa de vocabulário de comportamento.
- **Limite:** ATT&CK não substitui a análise da arquitetura; há críticas fundamentadas.
- **Estado:** núcleo
- **Fontes:** [Threat Modeling with ATT&CK](https://center-for-threat-informed-defense.github.io/threat-modeling-with-attack/) [A]; [MITRE ATT&CK](https://attack.mitre.org/) [A]; [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) [A]; [MITRE ATT&CK: Threat Model Thursday](https://shostack.org/blog/mitre-attack-threat-modeling-threat-model-thursday/) [B]

## Attack Flow

**Pergunta:** Em que sequência os comportamentos se encadeiam?

- **Centrado em:** atacante
- **Produz:** Grafo de comportamentos e pré-condições
- **Use quando:** Comunicar e comparar cadeias de comportamento.
- **Limite:** Um grafo não prova que a sequência foi executada.
- **Estado:** núcleo
- **Fontes:** [Attack Flow](https://center-for-threat-informed-defense.github.io/attack-flow/) [A]; [The Procedural Semantics Gap in Structured CTI: A Measurement-Driven STIX Analysis for APT Emulation](https://arxiv.org/abs/2512.12078) [B]

## TARA (MITRE)

**Pergunta:** Quais ameaças priorizar e quais contramedidas selecionar?

- **Centrado em:** risco
- **Produz:** Avaliação de ameaças e seleção de contramedidas
- **Use quando:** Seleção de contramedidas em sistemas.
- **Limite:** Não confundir com TARA automotiva.
- **Estado:** núcleo
- **Fontes:** [TARA — Threat Assessment and Remediation Analysis](https://www.mitre.org/news-insights/publication/threat-assessment-and-remediation-analysis-tara) [A]

## enterpriseLang / MAL

**Pergunta:** Quais caminhos de ataque a arquitetura permite, dado o modelo de ativos?

- **Centrado em:** simulação
- **Produz:** Simulação de caminhos de ataque sobre modelo de ativos baseado em ATT&CK
- **Use quando:** Pesquisa e análise quantitativa de caminhos.
- **Limite:** Resultados dependem dos parâmetros do modelo.
- **Estado:** emergente
- **Fontes:** [Cyber security threat modeling based on the MITRE Enterprise ATT&CK Matrix](https://doi.org/10.1007/s10270-021-00898-7) [A]; [Threat modeling — A systematic literature review](https://doi.org/10.1016/j.cose.2019.03.010) [A]

## Análise de Hipóteses Concorrentes

**Pergunta:** Qual hipótese é menos inconsistente com a evidência?

- **Centrado em:** inteligência
- **Produz:** Matriz hipótese × evidência, com destaque ao que discrimina
- **Use quando:** Reduzir viés de confirmação em análise de inteligência e investigação digital.
- **Limite:** Método de análise de inteligência, não de modelagem de ameaças.
- **Estado:** complementar
- **Psicologia da análise:** método voltado a reduzir vieses cognitivos.
- **Fontes:** [Psychology of Intelligence Analysis](https://www.cia.gov/resources/csi/books-monographs/psychology-of-intelligence-analysis-2/) [A]; [A Tradecraft Primer: Structured Analytic Techniques for Improving Intelligence Analysis](https://www.cia.gov/resources/csi/static/Tradecraft-Primer-apr09.pdf) [A]

## DREAD

**Pergunta:** Qual a gravidade relativa desta ameaça?

- **Centrado em:** risco
- **Produz:** Pontuação por dano, reprodutibilidade, exploração, usuários afetados e descoberta
- **Use quando:** Apenas como referência histórica.
- **Limite:** Pontuações subjetivas e pouco repetíveis; não recomendado como padrão.
- **Estado:** legado
- **Fontes:** [DREAD — Threat Model Your Security Risks](https://learn.microsoft.com/en-us/archive/msdn-magazine/2003/november/resource-file-threat-model-your-security-risks) [E]

## STRIDE-LM

**Pergunta:** O que pode dar errado, incluindo movimento lateral?

- **Centrado em:** software
- **Produz:** STRIDE acrescido da categoria de movimento lateral
- **Use quando:** Quando o movimento lateral é central ao cenário.
- **Limite:** Fonte herdada; confirme a origem da extensão.
- **Estado:** legado
- **Fontes:** [STRIDE-LM](https://csf.tools/reference/stride-lm/) [E]

## MITRE ATLAS

**Pergunta:** Que técnicas adversárias visam sistemas de IA?

- **Centrado em:** ia
- **Produz:** Táticas, técnicas e estudos de caso contra sistemas de IA
- **Use quando:** Mapear ameaças a sistemas com modelos de aprendizado.
- **Limite:** Cobertura de técnicas não equivale a cobertura de detecção.
- **Estado:** emergente
- **Fontes:** [MITRE ATLAS](https://atlas.mitre.org/) [A]; [LLMInjection](https://github.com/Ridd1kulusC0d3r/LLmInjection) [B]

## OWASP Top 10 para LLM

**Pergunta:** Quais riscos comuns afetam aplicações com LLM?

- **Centrado em:** ia
- **Produz:** Lista de riscos para enumeração inicial
- **Use quando:** Ponto de partida para aplicações com LLM.
- **Limite:** Lista de riscos não é modelo de ameaças do seu sistema.
- **Estado:** emergente
- **Fontes:** [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) [B]; [Threat Modeling LLMs: The PHANTOM-B model](https://shostack.org/blackhat) [B]

## PLOT4ai

**Pergunta:** Quais ameaças de IA, privacidade e responsabilidade se aplicam?

- **Centrado em:** ia
- **Produz:** Biblioteca de ameaças e baralho de discussão
- **Use quando:** Sessões de modelagem de sistemas de IA.
- **Limite:** Confirme versão e licença antes de redistribuir.
- **Estado:** emergente
- **Fontes:** [PLOT4ai](https://plot4.ai/) [B]

## MAESTRO

**Pergunta:** Que ameaças existem em cada camada de um sistema de IA agêntica?

- **Centrado em:** ia
- **Produz:** Modelo em camadas para IA agêntica
- **Use quando:** Sistemas agênticos com múltiplos agentes e ferramentas.
- **Limite:** Publicação recente de blog; acompanhe revisões.
- **Estado:** emergente
- **Fontes:** [MAESTRO — Agentic AI Threat Modeling Framework](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro) [B]; [Keynote \| Threat Modeling Agentic AI Systems: Proactive Strategies for Security and Resilience](https://www.youtube.com/watch?v=R49Cv7pJ2KA) [B]
