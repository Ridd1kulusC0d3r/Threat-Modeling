# Acervo completo

[Início](../README.md) · [Por tema](TEMAS.md) · [Métodos](METODOS.md) · [Metodologia](METODOLOGIA.md)

> Arquivo **gerado** por `scripts/build_readme.py` a partir de [`data/resources.json`](../data/resources.json). Edite os dados, não este arquivo.

Cada linha traz o **grau da fonte** (A–E, [o que significa](METODOLOGIA.md#graus-de-fonte)), o acesso, o nível e o **limite** conhecido. Grau mede o tipo de fonte, não a qualidade das ideias.

| Tipo | Recursos |
|---|---|
| [Manifestos e princípios](#manifestos-e-princípios) | 1 |
| [Guias e frameworks](#guias-e-frameworks) | 28 |
| [Métodos e modelos](#métodos-e-modelos) | 12 |
| [Livros](#livros) | 10 |
| [Papers e trabalhos técnicos](#papers-e-trabalhos-técnicos) | 17 |
| [Artigos e posts](#artigos-e-posts) | 3 |
| [Conferências e talks](#conferências-e-talks) | 8 |
| [Cursos e plataformas de estudo](#cursos-e-plataformas-de-estudo) | 1 |
| [Ferramentas e repositórios](#ferramentas-e-repositórios) | 21 |
| [Datasets e catálogos](#datasets-e-catálogos) | 5 |

## Manifestos e princípios

| Recurso | Autoria | Acesso | Grau | Nível | Por que ler | Limite |
|---|---|---|---|---|---|---|
| [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/) | Comunidade de autores (2020) | gratuito | **B** | introdutório | Valores, princípios e antipadrões. | Base filosófica, não procedimento passo a passo. |

## Guias e frameworks

| Recurso | Autoria | Acesso | Grau | Nível | Por que ler | Limite |
|---|---|---|---|---|---|---|
| [Shifting the Balance of Cybersecurity Risk](https://www.cisa.gov/sites/default/files/2023-06/principles_approaches_for_security-by-design-default_508c.pdf) | CISA e parceiros (2023) | gratuito | **A** | introdutório | Segurança desde o projeto. | Publicação inicial; conferir atualização posterior. |
| [A Tradecraft Primer: Structured Analytic Techniques for Improving Intelligence Analysis](https://www.cia.gov/resources/csi/static/Tradecraft-Primer-apr09.pdf) | Governo dos EUA (CIA, Sherman Kent School) (2009) | gratuito | **A** | introdutório | Técnicas estruturadas de análise para desafiar julgamentos, expor modelos mentais e lidar com incerteza; inclui verificação de premissas e análise de hipóteses concorrentes. | Literatura de inteligência, não de threat modeling; aplicação a ciberameaças exige adaptação. |
| [ATT&CK Detection Strategies](https://attack.mitre.org/detectionstrategies/) | MITRE | gratuito | **A** | intermediário | Estratégias por comportamento. | Adaptar à arquitetura local. |
| [Developing Cyber-Resilient Systems](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final) | NIST SP 800-160 Vol. 2 Rev. 1 | gratuito | **A** | intermediário | Engenharia de resiliência. | Não é catálogo de regras. |
| [Microsoft STRIDE](https://learn.microsoft.com/pt-br/azure/security/develop/threat-modeling-tool-threats) | Microsoft | gratuito | **A** | intermediário | Categorias de ameaça em desenho de sistemas | Link herdado; conferir versão atual |
| [Minimum Telemetry Requirements](https://center-for-threat-informed-defense.github.io/summiting-the-pyramid/data-readiness/min-telemetry-reqs/) | MITRE CTID | gratuito | **A** | intermediário | Requisitos mínimos de dados. | Documentar campos ausentes. |
| [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) | NIST | gratuito | **A** | intermediário | Catálogo de controles de segurança e privacidade. | Catálogo de controles; selecione conforme o modelo de ameaças. |
| [NIST SSDF — Secure Software Development Framework](https://csrc.nist.gov/projects/ssdf) | NIST | gratuito | **A** | intermediário | Práticas de desenvolvimento seguro ao longo do ciclo de vida de software. | Conjunto de práticas; não é método de modelagem. |
| [SDL Threat Modeling](https://www.microsoft.com/en-us/securityengineering/sdl/threatmodeling) | Microsoft | gratuito | **A** | intermediário | Refinamento no ciclo de vida. | Não se limita ao design inicial. |
| [Sensor Mappings to ATT&CK](https://center-for-threat-informed-defense.github.io/sensor-mappings-to-attack/) | MITRE CTID | gratuito | **A** | intermediário | Sensores, eventos e visibilidade. | Preservar versão; estrutura ATT&CK evolui. |
| [Threat Modelling](https://www.ncsc.gov.uk/collection/risk-management/threat-modelling) | NCSC | gratuito | **A** | introdutório | Integração com risco. | Contexto institucional. |
| [Threat Modeling at Scale](https://safecode.org/resource-publications/threat-modeling-at-scale/) | SAFECode (2023) | gratuito | **B** | introdutório | Institucionalização da modelagem. | Adaptar à organização. |
| [Threat Modeling Capabilities](https://www.threatmodelingmanifesto.org/capabilities/) | Autores do Manifesto (2020) | gratuito | **B** | introdutório | Estratégia, educação, ação e medição. | Mais capacidades não implica maior maturidade. |
| [DeTT&CT — Data quality](https://github.com/rabobank-cdc/DeTTECT/wiki/data-quality-scoring) | Rabobank CDC | gratuito | **B** | intermediário | Completude, atraso, consistência e retenção. | Pontuação não substitui teste. |
| [OWASP Developer Guide — Threat Modeling](https://devguide.owasp.org/en/04-design/01-threat-modeling/) | OWASP | gratuito | **B** | intermediário | Relacionar modelagem ao desenvolvimento; fonte localizada nesta edição | Confira versão e condições de uso na fonte. |
| [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) | OWASP | gratuito | **B** | introdutório | Entender o processo e suas perguntas fundamentais; fonte consultada nesta edição | Confira versão e condições de uso na fonte. |
| [OWASP Threat Modeling Project](https://owasp.github.io/www-project-threat-modeling/) | OWASP | gratuito | **B** | introdutório | Processo e métodos. | Escolher segundo o problema. |
| [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) | OWASP GenAI Security Project | gratuito | **B** | intermediário | Catálogo de riscos para aplicações com LLM; ponto de partida para enumerar o que pode dar errado. | Lista de riscos não é modelo de ameaças do seu sistema. |
| [Sigma Correlation Specification](https://sigmahq.io/sigma-specification/specification/sigma-correlation-rules-specification.html) | SigmaHQ | gratuito | **B** | intermediário | Agrupamento, contagem e ordem temporal. | Backend pode não preservar semântica. |
| [Threat Model Library](https://devguide.owasp.org/en/04-design/01-threat-modeling/06-threat-model-library/) | OWASP | gratuito | **B** | intermediário | Comparar entregáveis. | Não comprova segurança local. |
| [Threat Modeling in Practice](https://devguide.owasp.org/en/04-design/01-threat-modeling/07-practical-threat-modeling/) | OWASP | gratuito | **B** | intermediário | Aplicação iterativa. | Adaptar ao ciclo da equipe. |
| [Threat Modeling: What, Why, and How?](https://shostack.org/resources/whitepapers/threat-modeling-what-why-how) | Adam Shostack | gratuito | **B** | intermediário | Introdução e propósito. | Aprofundar com casos. |
| [AWS Threat Modeling Workshop](https://catalog.workshops.aws/threatmodel/en-US/introduction/what-is-threat-modeling) | AWS | gratuito | **C** | intermediário | Aplicação em exercícios | Link herdado; conferir requisitos |
| [Detection Engineering Maturity Matrix](https://detectionengineering.io/) | detectionengineering.io | gratuito | **C** | intermediário | Capacidades da função de detecção. | Maturidade não equivale a eficácia. |
| [GitLab AppSec Threat Modeling](https://handbook.gitlab.com/handbook/security/product-security/security-platforms-architecture/application-security/runbooks/threat-modeling/) | GitLab | gratuito | **C** | intermediário | Processo de uma equipe de produto | Processo de uma organização específica; o handbook foi reorganizado e o endereço antigo retornava 404, então fixe a versão que usar. |
| [PASTA — VerSprite](https://versprite.com/blog/what-is-pasta-threat-modeling/) | VerSprite | gratuito | **C** | intermediário | Abordagem orientada a risco e análise de ataques | Material do proponente; não comparação independente |
| [MITRE ATT&CK: Threat Model Thursday](https://shostack.org/blog/mitre-attack-threat-modeling-threat-model-thursday/) | Adam Shostack | gratuito | **D** | intermediário | Avaliar abordagem CTID. | Opinião fundamentada, não benchmark. |
| [OpenStack Threat Analysis](https://wiki.openstack.org/wiki/Security/Threat_Analysis) | OpenStack | gratuito | **E** | intermediário | Exemplo de processo em plataforma | Material histórico; conferir atualidade |

## Métodos e modelos

| Recurso | Autoria | Acesso | Grau | Nível | Por que ler | Limite |
|---|---|---|---|---|---|---|
| [Attack Flow](https://center-for-threat-informed-defense.github.io/attack-flow/) | MITRE CTID | gratuito | **A** | intermediário | Sequência de comportamentos. | Grafo não prova execução. |
| [D3FEND](https://d3fend.mitre.org/) | MITRE | gratuito | **A** | intermediário | Técnicas e artefatos defensivos. | Mapeamento não comprova eficácia. |
| [MITRE ATLAS](https://atlas.mitre.org/) | MITRE | gratuito | **A** | intermediário | Base de conhecimento de táticas e técnicas adversárias contra sistemas de IA, no estilo ATT&CK. | Cobertura de técnicas não equivale a cobertura de detecção. |
| [MITRE ATT&CK](https://attack.mitre.org/) | MITRE | gratuito | **A** | introdutório | Vocabulário de comportamentos adversários observados; base para mapear hipóteses e cobertura. | Não substitui um método de modelagem; mapear somente o que a evidência sustenta. |
| [Summiting the Pyramid](https://center-for-threat-informed-defense.github.io/summiting-the-pyramid/) | MITRE CTID | gratuito | **A** | intermediário | Robustez, decomposição e cobertura. | Medir implementações testadas, não etiquetas. |
| [TARA — Threat Assessment and Remediation Analysis](https://www.mitre.org/news-insights/publication/threat-assessment-and-remediation-analysis-tara) | MITRE | gratuito | **A** | intermediário | Avaliar e selecionar contramedidas. | Distinguir de TARA automotiva. |
| [Threat Modeling with ATT&CK](https://center-for-threat-informed-defense.github.io/threat-modeling-with-attack/) | MITRE CTID | gratuito | **A** | intermediário | Comportamento adversário na modelagem. | ATT&CK não substitui arquitetura. |
| [MAESTRO — Agentic AI Threat Modeling Framework](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro) | Cloud Security Alliance (2025) | gratuito | **B** | intermediário | Framework em camadas para modelar ameaças a sistemas de IA agêntica. | Publicação de blog de 2025; acompanhe revisões do framework. |
| [ATASM](https://brookschoenfield.com/?page_id=341) | Brook Schoenfield | gratuito | **B** | intermediário | Arquitetura, ameaças, superfícies e mitigação. | Adaptar ao ambiente. |
| [LINDDUN](https://linddun.org/) | KU Leuven | gratuito | **B** | intermediário | Ameaças de privacidade. | Vai além de confidencialidade. |
| [PLOT4ai](https://plot4.ai/) | PLOT4ai | gratuito | **B** | intermediário | Biblioteca de ameaças e baralho para threat modeling de sistemas de IA, com foco em privacidade e responsabilidade. | Verifique versão e licença do baralho antes de redistribuir. |
| [STRIDE-LM](https://csf.tools/reference/stride-lm/) | CSF Tools | gratuito | **E** | intermediário | Extensão do STRIDE que acrescenta movimento lateral (Lateral Movement) às categorias. | Link herdado; confira a fonte original da extensão. |

## Livros

| Recurso | Autoria | Acesso | Grau | Nível | Por que ler | Limite |
|---|---|---|---|---|---|---|
| [Psychology of Intelligence Analysis](https://www.cia.gov/resources/csi/books-monographs/psychology-of-intelligence-analysis-2/) | Richards J. Heuer Jr. CIA (1999) | gratuito | **A** | intermediário | Vieses, hipóteses e incerteza. | Literatura de inteligência, não método de threat modeling. |
| [Intelligence-Driven Incident Response](https://www.oreilly.com/library/view/intelligence-driven-incident-response/9781098120672/) | Rebekah Brown e Scott J. Roberts. 2ª ed., O’Reilly (2023) | pago | **B** | intermediário | Inteligência e operação. | Avaliar relevância local da CTI. |
| [Designing Secure Software: A Guide for Developers](https://designingsecuresoftware.com/) | Loren Kohnfelder. No Starch Press (2022) | pago | **B** | intermediário | Pressupostos e escolhas de design. | Não é catálogo de detecções. |
| [Security Engineering: A Guide to Building Dependable Distributed Systems](https://www.cl.cam.ac.uk/archive/rja14/book.html) | Ross Anderson. 3ª ed (2020) | parcial | **B** | intermediário | Confiança, dependências e incentivos. | Selecionar capítulos para o caso. |
| [Threat Modeling: A Practical Guide for Development Teams](https://www.oreilly.com/library/view/threat-modeling/9781492056546/) | Izar Tarandach e Matthew J. Coles. O’Reilly (2020) | pago | **B** | intermediário | Automação e modelagem contínua. | Revisar versões das ferramentas. |
| [Risk Centric Threat Modeling: Process for Attack Simulation and Threat Analysis](https://onlinelibrary.wiley.com/doi/book/10.1002/9781118988374) | Tony UcedaVélez e Marco M. Morana. Wiley (2015) | pago | **B** | intermediário | PASTA; negócio, ameaça e risco. | Justificar escalas locais. |
| [Securing Systems: Applied Security Architecture and Threat Models](https://brookschoenfield.com/?page_id=245) | Brook S. E. Schoenfield. CRC Press (2015) | pago | **B** | intermediário | Arquitetura, superfícies e mitigação. | Requer arquitetura real documentada. |
| [Threat Modeling: Designing for Security](https://threatmodelingbook.com/books) | Adam Shostack. Wiley (2014) | pago | **B** | intermediário | Fundamentos e abordagens. | Citação da edição de 2014; conferir edição adquirida. |
| [Automating Security Detection Engineering](https://github.com/PacktPublishing/Automating-Security-Detection-Engineering) | Dennis Chow. Packt | pago | **B** | intermediário | Detection as Code e pipelines. | Parte dos labs depende de serviços específicos. |
| [Practical Threat Detection Engineering](https://github.com/PacktPublishing/Practical-Threat-Detection-Engineering) | Megan Roddie, Jason Deyalsingh e Gary J. Katz. Packt | pago | **B** | intermediário | Planejar, desenvolver e validar. | Código público não implica livro gratuito. |

## Papers e trabalhos técnicos

| Recurso | Autoria | Acesso | Grau | Nível | Por que ler | Limite |
|---|---|---|---|---|---|---|
| [ATT&CK-based Advanced Persistent Threat attacks risk propagation assessment model for zero trust networks](https://doi.org/10.1016/j.comnet.2024.110376) | Zhang et al. (2024) | gratuito | **A** | avançado | Modelo de avaliação de propagação de risco de APTs baseado em ATT&CK para redes zero trust (Computer Networks). | Modelo acadêmico; validar premissas antes de usar em produção. |
| [A review of threat modelling approaches for APT-style attacks](https://doi.org/10.1016/j.heliyon.2021.e05969) | Tatam, Shanmugam, Azam, Kannoorpatti (2021) | acesso aberto | **A** | avançado | Revisão de abordagens de modelagem de ameaças para ataques do tipo APT (Heliyon). | Revisão de 2021; confira abordagens posteriores. |
| [Cyber security threat modeling based on the MITRE Enterprise ATT&CK Matrix](https://doi.org/10.1007/s10270-021-00898-7) | Wenjun Xiong, Emeline Legrand, Oscar Åberg e Robert Lagerström. Software and Systems Modeling 21, 157–177 (2021) | acesso aberto | **A** | avançado | enterpriseLang/MAL, ativos e caminhos. | Simulação depende de parâmetros. |
| [HOLMES: Real-Time APT Detection through Correlation of Suspicious Information Flows](https://www.seclab.cs.sunysb.edu/seclab/pubs/holmes19.pdf) | Sadegh M. Milajerdi et al. IEEE S&P (2019) | gratuito | **A** | avançado | Fluxos e correlação contextual. | Pesquisa, não regra pronta de SIEM. |
| [Threat modeling — A systematic literature review](https://doi.org/10.1016/j.cose.2019.03.010) | Wenjun Xiong e Robert Lagerström. Computers & Security 84, 53–69 (2019) | gratuito | **A** | avançado | Mapear métodos e trabalhos relacionados. | Complementar recorte de 2019. |
| [Publish Your Threat Models! The benefits far outweigh the dangers](https://arxiv.org/abs/2511.08295) | Loren Kohnfelder e Adam Shostack (2025) | preprint | **B** | intermediário | Publicar pressupostos e decisões. | Posicionamento, não avaliação de eficácia. |
| [The Procedural Semantics Gap in Structured CTI: A Measurement-Driven STIX Analysis for APT Emulation](https://arxiv.org/abs/2512.12078) | Ágney Lopes Roth Ferraz et al (2025) | preprint | **B** | avançado | Ordem, pré-condições e suposições. | Não promover inferências a fatos. |
| [Red Team Redemption: A Structured Comparison of Open-Source Tools for Adversary Emulation](https://arxiv.org/abs/2408.15645) | Max Landauer et al (2024) | preprint | **B** | avançado | Critérios de seleção de emulação. | Resultados vinculados às versões. |
| [Security Modelling for Cyber-Physical Systems: A Systematic Literature Review](https://arxiv.org/abs/2404.07527) | Shaofei Huang, Christopher M. Poskitt e Lwin Khin Shar (2024) | preprint | **B** | avançado | Ameaças versus ataques em CPS. | Considerar safety e processo físico. |
| [Threat Models over Space and Time: A Case Study of E2EE Messaging Applications](https://arxiv.org/abs/2301.05653) | Partha Das Chowdhury et al (2023) | preprint | **B** | avançado | Contexto temporal e fronteiras de confiança. | Generalização exige avaliação. |
| [Threat Modeling of Cyber-Physical Systems in Practice](https://arxiv.org/abs/2103.04226) | Ameerah-Muhsinah Jamil, Lotfi ben Othmane e Altaz Valani (2021) | preprint | **B** | avançado | Prática e atualização de modelos CPS. | Entrevistas não são testes de eficácia. |
| [UNICORN: Runtime Provenance-Based Detector for Advanced Persistent Threats](https://arxiv.org/abs/2001.01525) | Xueyuan Han et al (2020) | preprint | **B** | avançado | Anomalias e proveniência. | Anomalia não equivale a malícia. |
| [POIROT: Aligning Attack Behavior with Kernel Audit Records for Cyber Threat Hunting](https://arxiv.org/abs/1910.00056) | Sadegh M. Milajerdi et al (2019) | preprint | **B** | avançado | Grafo de CTI e proveniência. | Depende da auditoria disponível. |
| [Towards Realistic Threat Modeling: Attack Commodification, Irrelevant Vulnerabilities, and Unrealistic Assumptions](https://arxiv.org/abs/1801.04569) | Luca Allodi e Sandro Etalle (2018) | preprint | **B** | avançado | Plausibilidade e limitações do atacante. | Explicitar pressupostos. |
| [The Diamond Model of Intrusion Analysis](https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf) | Sergio Caltagirone, Andrew Pendergast e Christopher Betz (2013) | gratuito | **B** | avançado | Adversário, capacidade, infraestrutura e vítima. | Correlação não confirma atribuição. |
| [Intelligence-Driven Computer Network Defense Informed by Analysis of Adversary Campaigns and Intrusion Kill Chains](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf) | Eric M. Hutchins, Michael J. Cloppert e Rohan M. Amin (2011) | gratuito | **B** | avançado | Campanhas e interrupção de ataques. | Não forçar todos os casos a sequência linear. |
| [Attack Trees](https://www.schneier.com/academic/archives/1999/12/attack_trees.html) | Bruce Schneier. Dr. Dobb’s Journal (1999) | gratuito | **B** | introdutório | Objetivos e condições de ataque. | Árvore não prova probabilidade real. |

## Artigos e posts

| Recurso | Autoria | Acesso | Grau | Nível | Por que ler | Limite |
|---|---|---|---|---|---|---|
| [Threat Modeling Express: guia prático](https://guisso.dev/blog/threat-modeling-intro/) | Guisso (2024) | gratuito | **B** | introdutório | Guia prático em português: como engajar o time, mapear ativos críticos e aplicar controles rápidos com o Threat Modeling Express. | Post de blog de 2024 de um único autor; não é revisado por pares nem compara métodos. |
| [Detection Engineering: A Case Study — GitGuardian](https://blog.gitguardian.com/detection-engineering-case-study/) | GitGuardian | gratuito | **C** | intermediário | Exemplo de detecção de execução remota DCOM. | Telemetria e plataforma específicas. |
| [DREAD — Threat Model Your Security Risks](https://learn.microsoft.com/en-us/archive/msdn-magazine/2003/november/resource-file-threat-model-your-security-risks) | Microsoft (MSDN Magazine) (2003) | gratuito | **E** | intermediário | Artigo histórico que descreve a pontuação DREAD. | Arquivo de 2003; pontuações subjetivas. Preservado por referência histórica, sem recomendação de adoção. |

## Conferências e talks

| Recurso | Autoria | Acesso | Grau | Nível | Por que ler | Limite |
|---|---|---|---|---|---|---|
| [Building Space Attack Chains using SPARTA](https://sparta.aerospace.org/resources/OTR-2023-00989_SPARTA_DefCon2023.pdf) | The Aerospace Corporation (SPARTA) | gratuito | **A** | intermediário | Aerospace Village, DEF CON 2023; slides. | Apresentação ou slides não são benchmark de produção; confirme se há gravação pública e a edição do evento. |
| [HOLMES — IEEE S&P 2019](https://www.ieee-security.org/TC/SP2019/SP19-Slides-pdfs/Sadegh_Momeni_-_13-Sadegh-Momeni-Real_time_APT_Detection_through_Correlation_of_Suspicious_Information_Flows.pdf) | Sadegh M. Milajerdi et al. (IEEE S&P 2019) | gratuito | **A** | avançado | Slides de pesquisa. | Apresentação ou slides não são benchmark de produção; confirme se há gravação pública e a edição do evento. |
| [Threat Modeling with ATT&CK — BSides Connecticut](https://center-for-threat-informed-defense.github.io/threat-modeling-with-attack/presentations/tmwa-bsides-ct.pdf) | MITRE CTID | gratuito | **A** | intermediário | Slides CTID. | Apresentação ou slides não são benchmark de produção; confirme se há gravação pública e a edição do evento. |
| [DC’s Next Top Threat Model](https://threatmodel.us/) | DEF CON (competição da comunidade) | gratuito | **B** | intermediário | Competição DEF CON. | Apresentação ou slides não são benchmark de produção; confirme se há gravação pública e a edição do evento. |
| [Keynote \| Threat Modeling Agentic AI Systems: Proactive Strategies for Security and Resilience](https://www.youtube.com/watch?v=R49Cv7pJ2KA) | SANS Institute (canal) | gratuito | **B** | intermediário | Keynote gravada sobre modelagem de ameaças para sistemas de IA agêntica. | Vídeo; extraia afirmações e confronte com fontes primárias antes de citar. |
| [Threat Modeling LLMs: The PHANTOM-B model](https://shostack.org/blackhat) | Adam Shostack | gratuito | **B** | intermediário | Página do autor; agenda Black Hat / DEF CON AppSec Village 2026 e links de material. | Apresentação ou slides não são benchmark de produção; confirme se há gravação pública e a edição do evento. |
| [ThreatModCon](https://www.threatmodcon.com/) | ThreatModCon (comunidade e palestrantes de threat modeling) | gratuito | **B** | intermediário | Conferência dedicada exclusivamente a threat modeling; fonte de talks para extrair ideias e exercícios. | Qualidade varia por talk; o site lista palestrantes de fornecedores. Organização do evento não verificada; confira se há gravação pública antes de planejar o estudo. |
| [Threat Modeling Connect — On Demand](https://www.threatmodelingconnect.com/resources/on-demand) | Threat Modeling Connect | gratuito | **C** | intermediário | Acervo de experiências e apresentações. | Apresentação ou slides não são benchmark de produção; confirme se há gravação pública e a edição do evento. |

## Cursos e plataformas de estudo

| Recurso | Autoria | Acesso | Grau | Nível | Por que ler | Limite |
|---|---|---|---|---|---|---|
| [CTI Academy](https://ctiacademy.io/) | CTI Academy | parcial | **C** | introdutório | Plataforma de estudo para perfilamento de ameaças (threat profiling) e inteligência; módulos com lições online. | Conteúdo da plataforma não foi avaliado aqui; parte exige conta. |

## Ferramentas e repositórios

| Recurso | Autoria | Acesso | Grau | Nível | Por que ler | Limite |
|---|---|---|---|---|---|---|
| [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) | MITRE | gratuito | **A** | intermediário | Interface para anotar e visualizar camadas da matriz ATT&CK (cobertura, hipóteses, priorização). | Camada colorida não comprova detecção. |
| [BZAR](https://github.com/mitre-attack/bzar) | MITRE ATT&CK | gratuito | **A** | intermediário | Análise de rede com Zeek. | Revisar compatibilidade de versões. |
| [CTID Adversary Emulation Library](https://ctid.mitre.org/resources/adversary-emulation-library/) | MITRE CTID | gratuito | **A** | intermediário | Planos de emulação. | Adaptar pré-condições ao laboratório. |
| [CTID Micro Emulation Plans](https://ctid.mitre.org/projects/micro-emulation-plans/) | MITRE CTID | gratuito | **A** | intermediário | Validação de recortes. | Conclusões limitadas ao exercitado. |
| [OTRF SimuLand](https://github.com/OTRF/SimuLand) | Open Threat Research Forge (OTRF) | gratuito | **B** | intermediário | Infraestrutura e coleta. | Configuração influencia rastros. |
| [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/) | OWASP | gratuito | **B** | introdutório | Ferramenta open source de diagramação e geração de ameaças (STRIDE e outras). | Ferramenta de apoio; a qualidade do modelo depende do desenho. |
| [Palantir ADS Framework](https://github.com/palantir/alerting-detection-strategy-framework) | Palantir | gratuito | **B** | intermediário | Documentar estratégia de detecção. | Registrar resposta e limitações. |
| [pytm](https://github.com/OWASP/pytm) | OWASP | gratuito | **B** | intermediário | Framework Python para descrever o sistema em código e gerar diagramas e ameaças. | Biblioteca de ameaças generalista; adapte ao seu contexto. |
| [Sigma Rules](https://github.com/SigmaHQ/sigma) | SigmaHQ | gratuito | **B** | intermediário | Regras compartilháveis. | Mapear campos e avaliar benignos. |
| [Threagile](https://threagile.io/) | Christian Schneider | gratuito | **B** | intermediário | Threat modeling como código: o modelo em YAML gera riscos e relatórios. | Regras de risco embutidas exigem curadoria para o seu contexto. |
| [Threat Hunter Playbook](https://github.com/OTRF/ThreatHunter-Playbook) | Open Threat Research Forge (OTRF) | gratuito | **B** | intermediário | Notebooks de hipótese, consultas e evidências. | Revisar dependências antes de executar. |
| [Anvilogic](https://www.anvilogic.com/) | Anvilogic | gratuito | **C** | intermediário | Plataforma comercial de detecção e hunting listada para estudo comparativo. | Material de fornecedor; não avaliado por este repositório. |
| [Atomic Red Team](https://www.atomicredteam.io/docs/atomic-red-team) | Atomic Red Team (Red Canary e comunidade) | gratuito | **C** | intermediário | Testes individuais. | Teste atômico não cobre campanha. |
| [Chainsaw](https://github.com/WithSecureOpenSource/chainsaw) | WithSecure | gratuito | **C** | intermediário | Análise EVTX / Sigma. | Verificar campos e compatibilidade. |
| [Elastic Detection Rules](https://github.com/elastic/detection-rules) | Elastic | gratuito | **C** | intermediário | Desenvolvimento e validação de regras. | Lint não comprova eficácia. |
| [Elastic — Validate and test rules](https://www.elastic.co/docs/solutions/security/detect-and-alert/validate-and-test-rules) | Elastic | gratuito | **C** | intermediário | Categorias de testes. | Distinguir schema, lógica e ponta a ponta. |
| [Splunk Attack Range](https://github.com/splunk/attack_range) | Splunk | gratuito | **C** | intermediário | Ambiente instrumentado. | Infraestrutura pode gerar custos. |
| [Splunk Security Content](https://github.com/splunk/security_content) | Splunk | gratuito | **C** | intermediário | Analytic Stories e detecções. | Separar narrativa e implementação específica. |
| [Stratus Red Team](https://stratus-red-team.cloud/) | Datadog | gratuito | **C** | intermediário | Emulação em nuvem. | Conta de testes; não detectar só o user agent da ferramenta. |
| [Tidal Cyber](https://www.tidalcyber.com/) | Tidal Cyber | gratuito | **C** | intermediário | Plataforma de threat-informed defense que operacionaliza ATT&CK; listada para estudo comparativo. | Material de fornecedor; não avaliado por este repositório. |
| [Elevation of Privilege](https://github.com/adamshostack/eop) | Adam Shostack | gratuito | **E** | introdutório | Facilitação com cartas | Ferramenta de discussão; não substitui análise |

## Datasets e catálogos

| Recurso | Autoria | Acesso | Grau | Nível | Por que ler | Limite |
|---|---|---|---|---|---|---|
| [NIST 800-53 Controls to ATT&CK Mapping](https://mitre-engenuity.org/cybersecurity/center-for-threat-informed-defense/our-work/nist-800-53-control-mappings/) | MITRE Engenuity CTID | gratuito | **A** | intermediário | Mapeamento entre controles do NIST 800-53 e técnicas do ATT&CK. | Mapeamento não comprova eficácia do controle. |
| [EVTX-ATTACK-SAMPLES](https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES) | Samir Bousseaden | gratuito | **B** | intermediário | Eventos Windows gravados. | Replay não valida coleta atual. |
| [LLMInjection](https://github.com/Ridd1kulusC0d3r/LLmInjection) | Ridd1kulusC0d3r | gratuito | **B** | intermediário | Panorama de ameaças a sistemas LLM e agênticos, com evidência, graus de fonte e níveis de confiança por afirmação. | Projeto irmão; mesma metodologia de graus A–E. |
| [OTRF Security Datasets](https://github.com/OTRF/Security-Datasets) | Open Threat Research Forge (OTRF) | gratuito | **B** | intermediário | Dados maliciosos e benignos. | Fixar arquivo, hash e licença; README tem indicações divergentes de licença, conferir LICENSE do snapshot antes de redistribuir. |
| [Splunk Attack Data](https://github.com/splunk/attack_data) | Splunk | gratuito | **C** | intermediário | Dados de teste. | Dados só de ataques não medem ruído de produção. |
