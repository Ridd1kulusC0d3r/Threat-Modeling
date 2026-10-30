# Bibliografia comentada

[Início](../README.md) · [Engenharia de detecção](ENGENHARIA-DE-DETECCAO.md) · [Conferências](CONFERENCIAS.md)

> **Lista estruturada:** os links desta tabela também estão em [`data/resources.json`](../data/resources.json), com grau, acesso e limite, e na [lista gerada](AWESOME.md). Este texto mantém o comentário editorial.

Consolidada em **23/10/2026** a partir da pesquisa desta conversa. Consulta não significa leitura integral de todos os livros nem validação operacional. As relações com cases são sínteses editoriais. Manifestos completos permanecem nas fontes; obras não são redistribuídas. Acesso aberto e licença de reutilização são coisas diferentes.

## Manifestos e princípios

| Obra / autoria | Tipo / acesso | Contribuição | Limite |
|---|---|---|---|
| [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/) — Comunidade de autores | Manifesto | Valores, princípios e antipadrões. | Base filosófica, não procedimento passo a passo. |
| [Threat Modeling Capabilities](https://www.threatmodelingmanifesto.org/capabilities/) — Autores do Manifesto | Catálogo | Estratégia, educação, ação e medição. | Mais capacidades não implica maior maturidade. |
| [Threat Modeling at Scale](https://safecode.org/resource-publications/threat-modeling-at-scale/) — SAFECode, 2023 | Guia | Institucionalização da modelagem. | Adaptar à organização. |
| [Shifting the Balance of Cybersecurity Risk](https://www.cisa.gov/sites/default/files/2023-06/principles_approaches_for_security-by-design-default_508c.pdf) — CISA e parceiros, 2023 | Princípios institucionais | Segurança desde o projeto. | Publicação inicial; conferir atualização posterior. |
| [Publish Your Threat Models! The benefits far outweigh the dangers](https://arxiv.org/abs/2511.08295) — Loren Kohnfelder e Adam Shostack, 2025 | Preprint consultado | Publicar pressupostos e decisões. | Posicionamento, não avaliação de eficácia. |

## Livros

| Obra / autoria | Tipo / acesso | Contribuição | Limite |
|---|---|---|---|
| [Threat Modeling: Designing for Security](https://threatmodelingbook.com/books) — Adam Shostack. Wiley, 2014 | Comercial | Fundamentos e abordagens. | Citação da edição de 2014; conferir edição adquirida. |
| [Risk Centric Threat Modeling: Process for Attack Simulation and Threat Analysis](https://onlinelibrary.wiley.com/doi/book/10.1002/9781118988374) — Tony UcedaVélez e Marco M. Morana. Wiley, 2015 | Comercial | PASTA; negócio, ameaça e risco. | Justificar escalas locais. |
| [Securing Systems: Applied Security Architecture and Threat Models](https://brookschoenfield.com/?page_id=245) — Brook S. E. Schoenfield. CRC Press, 2015 | Comercial | Arquitetura, superfícies e mitigação. | Requer arquitetura real documentada. |
| [Threat Modeling: A Practical Guide for Development Teams](https://www.oreilly.com/library/view/threat-modeling/9781492056546/) — Izar Tarandach e Matthew J. Coles. O’Reilly, 2020 | Comercial | Automação e modelagem contínua. | Revisar versões das ferramentas. |
| [Security Engineering: A Guide to Building Dependable Distributed Systems](https://www.cl.cam.ac.uk/archive/rja14/book.html) — Ross Anderson. 3ª ed., 2020 | Livro com material do autor | Confiança, dependências e incentivos. | Selecionar capítulos para o caso. |
| [Designing Secure Software: A Guide for Developers](https://designingsecuresoftware.com/) — Loren Kohnfelder. No Starch Press, 2022 | Comercial | Pressupostos e escolhas de design. | Não é catálogo de detecções. |
| [Intelligence-Driven Incident Response](https://www.oreilly.com/library/view/intelligence-driven-incident-response/9781098120672/) — Rebekah Brown e Scott J. Roberts. 2ª ed., O’Reilly, 2023 | Comercial | Inteligência e operação. | Avaliar relevância local da CTI. |
| [Psychology of Intelligence Analysis](https://www.cia.gov/resources/csi/books-monographs/psychology-of-intelligence-analysis-2/) — Richards J. Heuer Jr. CIA, 1999 | Gratuito | Vieses, hipóteses e incerteza. | Literatura de inteligência, não método de threat modeling. |
| [Practical Threat Detection Engineering](https://github.com/PacktPublishing/Practical-Threat-Detection-Engineering) — Megan Roddie, Jason Deyalsingh e Gary J. Katz. Packt | Livro comercial + código público | Planejar, desenvolver e validar. | Código público não implica livro gratuito. |
| [Automating Security Detection Engineering](https://github.com/PacktPublishing/Automating-Security-Detection-Engineering) — Dennis Chow. Packt | Livro comercial + código público | Detection as Code e pipelines. | Parte dos labs depende de serviços específicos. |

## Papers e trabalhos técnicos

| Obra / autoria | Tipo / acesso | Contribuição | Limite |
|---|---|---|---|
| [Threat modeling — A systematic literature review](https://doi.org/10.1016/j.cose.2019.03.010) — Wenjun Xiong e Robert Lagerström. Computers & Security 84, 53–69, 2019 | Revisão publicada | Mapear métodos e trabalhos relacionados. | Complementar recorte de 2019. |
| [Cyber security threat modeling based on the MITRE Enterprise ATT&CK Matrix](https://doi.org/10.1007/s10270-021-00898-7) — Wenjun Xiong, Emeline Legrand, Oscar Åberg e Robert Lagerström. Software and Systems Modeling 21, 157–177, 2022; online 2021 | Artigo aberto | enterpriseLang/MAL, ativos e caminhos. | Simulação depende de parâmetros. |
| [Attack Trees](https://www.schneier.com/academic/archives/1999/12/attack_trees.html) — Bruce Schneier. Dr. Dobb’s Journal, 1999 | Artigo técnico | Objetivos e condições de ataque. | Árvore não prova probabilidade real. |
| [The Diamond Model of Intrusion Analysis](https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf) — Sergio Caltagirone, Andrew Pendergast e Christopher Betz, 2013 | Relatório técnico | Adversário, capacidade, infraestrutura e vítima. | Correlação não confirma atribuição. |
| [Intelligence-Driven Computer Network Defense Informed by Analysis of Adversary Campaigns and Intrusion Kill Chains](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf) — Eric M. Hutchins, Michael J. Cloppert e Rohan M. Amin, 2011 | Trabalho técnico | Campanhas e interrupção de ataques. | Não forçar todos os casos a sequência linear. |
| [Towards Realistic Threat Modeling: Attack Commodification, Irrelevant Vulnerabilities, and Unrealistic Assumptions](https://arxiv.org/abs/1801.04569) — Luca Allodi e Sandro Etalle, 2018 | Versão no arXiv | Plausibilidade e limitações do atacante. | Explicitar pressupostos. |
| [Threat Models over Space and Time: A Case Study of E2EE Messaging Applications](https://arxiv.org/abs/2301.05653) — Partha Das Chowdhury et al., 2023 | Versão no arXiv | Contexto temporal e fronteiras de confiança. | Generalização exige avaliação. |
| [Threat Modeling of Cyber-Physical Systems in Practice](https://arxiv.org/abs/2103.04226) — Ameerah-Muhsinah Jamil, Lotfi ben Othmane e Altaz Valani, 2021 | Estudo; arXiv | Prática e atualização de modelos CPS. | Entrevistas não são testes de eficácia. |
| [Security Modelling for Cyber-Physical Systems: A Systematic Literature Review](https://arxiv.org/abs/2404.07527) — Shaofei Huang, Christopher M. Poskitt e Lwin Khin Shar, 2024 | Revisão; arXiv | Ameaças versus ataques em CPS. | Considerar safety e processo físico. |
| [HOLMES: Real-Time APT Detection through Correlation of Suspicious Information Flows](https://www.seclab.cs.sunysb.edu/seclab/pubs/holmes19.pdf) — Sadegh M. Milajerdi et al. IEEE S&P, 2019 | Artigo científico | Fluxos e correlação contextual. | Pesquisa, não regra pronta de SIEM. |
| [POIROT: Aligning Attack Behavior with Kernel Audit Records for Cyber Threat Hunting](https://arxiv.org/abs/1910.00056) — Sadegh M. Milajerdi et al., 2019 | Artigo; versão arXiv | Grafo de CTI e proveniência. | Depende da auditoria disponível. |
| [UNICORN: Runtime Provenance-Based Detector for Advanced Persistent Threats](https://arxiv.org/abs/2001.01525) — Xueyuan Han et al., 2020 | Artigo; versão arXiv | Anomalias e proveniência. | Anomalia não equivale a malícia. |
| [Red Team Redemption: A Structured Comparison of Open-Source Tools for Adversary Emulation](https://arxiv.org/abs/2408.15645) — Max Landauer et al., 2024 | Estudo; arXiv | Critérios de seleção de emulação. | Resultados vinculados às versões. |
| [The Procedural Semantics Gap in Structured CTI: A Measurement-Driven STIX Analysis for APT Emulation](https://arxiv.org/abs/2512.12078) — Ágney Lopes Roth Ferraz et al., 2025 | Preprint consultado | Ordem, pré-condições e suposições. | Não promover inferências a fatos. |

## Métodos, frameworks e guias

| Obra / autoria | Tipo / acesso | Contribuição | Limite |
|---|---|---|---|
| [Threat Modeling with ATT&CK](https://center-for-threat-informed-defense.github.io/threat-modeling-with-attack/) — MITRE CTID | Integração metodológica | Comportamento adversário na modelagem. | ATT&CK não substitui arquitetura. |
| [TARA — Threat Assessment and Remediation Analysis](https://www.mitre.org/news-insights/publication/threat-assessment-and-remediation-analysis-tara) — MITRE | Metodologia | Avaliar e selecionar contramedidas. | Distinguir de TARA automotiva. |
| [ATASM](https://brookschoenfield.com/?page_id=341) — Brook Schoenfield | Abordagem | Arquitetura, ameaças, superfícies e mitigação. | Adaptar ao ambiente. |
| [SDL Threat Modeling](https://www.microsoft.com/en-us/securityengineering/sdl/threatmodeling) — Microsoft | Prática | Refinamento no ciclo de vida. | Não se limita ao design inicial. |
| [LINDDUN](https://linddun.org/) — KU Leuven | Método de privacidade | Ameaças de privacidade. | Vai além de confidencialidade. |
| [Attack Flow](https://center-for-threat-informed-defense.github.io/attack-flow/) — MITRE CTID | Linguagem | Sequência de comportamentos. | Grafo não prova execução. |
| [D3FEND](https://d3fend.mitre.org/) — MITRE | Ontologia | Técnicas e artefatos defensivos. | Mapeamento não comprova eficácia. |
| [Developing Cyber-Resilient Systems](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final) — NIST SP 800-160 Vol. 2 Rev. 1, 2021 | Publicação técnica | Engenharia de resiliência. | Não é catálogo de regras. |
| [Threat Modeling: What, Why, and How?](https://shostack.org/resources/whitepapers/threat-modeling-what-why-how) — Adam Shostack, 2017 | Artigo | Introdução e propósito. | Aprofundar com casos. |
| [OWASP Threat Modeling Project](https://owasp.github.io/www-project-threat-modeling/) — OWASP | Guia | Processo e métodos. | Escolher segundo o problema. |
| [Threat Modeling in Practice](https://devguide.owasp.org/en/04-design/01-threat-modeling/07-practical-threat-modeling/) — OWASP | Guia | Aplicação iterativa. | Adaptar ao ciclo da equipe. |
| [Threat Model Library](https://devguide.owasp.org/en/04-design/01-threat-modeling/06-threat-model-library/) — OWASP | Exemplos | Comparar entregáveis. | Não comprova segurança local. |
| [Threat Modelling](https://www.ncsc.gov.uk/collection/risk-management/threat-modelling) — NCSC | Guia institucional | Integração com risco. | Contexto institucional. |
| [MITRE ATT&CK: Threat Model Thursday](https://shostack.org/blog/mitre-attack-threat-modeling-threat-model-thursday/) — Adam Shostack, 2024 | Comentário crítico | Avaliar abordagem CTID. | Opinião fundamentada, não benchmark. |
---

# Referencial ampliado

Seções adicionadas em **30/10/2026**. Metadados conferidos em fontes primárias e indexadores por cinco verificações independentes; quando algo não pôde ser confirmado, o campo **Limite** diz. ⭐ indica o [núcleo essencial](TRILHA-DE-LEITURA.md#núcleo-essencial). As referências completas estão em [ABNT](REFERENCIAS-ABNT.md) e em [BibTeX](../referencias/referencias.bib).

## Modelagem da organização inteira

Para sair do diagrama de uma aplicação e modelar a empresa: ativos, identidades, relações de confiança e missão.

| Obra / autoria | Tipo / acesso · grau | Contribuição | Limite |
|---|---|---|---|
| [The Battle for New York: A Case Study of Applied Digital Threat Modeling at the Enterprise Level](https://www.usenix.org/conference/usenixsecurity18/presentation/stevens) — Rock Stevens; Daniel Votipka; Elissa M. Redmiles; Colin Ahern; Patrick Sweeney; Michelle L. Mazurek, 2018 ⭐ | Artigo, acesso aberto · **A** | Estudo de caso de modelagem de ameaças aplicada a toda uma organização (NYC Cyber Command). | Um único caso, com o método Center of Gravity. |
| [A Meta Language for Threat Modeling and Attack Simulations](https://doi.org/10.1145/3230833.3232799) — Pontus Johnson; Robert Lagerström; Mathias Ekstedt, 2018 ⭐ | Artigo, gratuito · **A** | MAL: gera grafos de ataque a partir de modelos de domínio; base da modelagem do ambiente inteiro. | Gerar grafos depende de linguagens de domínio bem modeladas; não valida probabilidades. |
| [The meta attack language – a formal description](https://doi.org/10.1016/j.cose.2023.103284) — Wojciech Wideł; Simon Hacks; Mathias Ekstedt; Pontus Johnson; Robert Lagerström, 2023 | Artigo, gratuito · **A** | Especificação formal da MAL; útil para quem desenha um esquema de grafo de ambiente. | Especificação formal; pouco útil sem praticar a linguagem. |
| [pwnPr3d: An Attack-Graph-Driven Probabilistic Threat-Modeling Approach](https://doi.org/10.1109/ARES.2016.77) — Pontus Johnson; Alexandre Vernotte; Mathias Ekstedt; Robert Lagerström, 2016 | Artigo, pago · **A** | Modelagem probabilística com tempo até comprometimento. | Valores de tempo até comprometimento dependem de estimativas de especialistas. |
| [The Cyber Security Modeling Language: A Tool for Assessing the Vulnerability of Enterprise System Architectures](https://doi.org/10.1109/JSYST.2012.2221853) — Teodor Sommestad; Mathias Ekstedt; Hannes Holm, 2013 | Artigo, pago · **A** | Probabilidades de sucesso calibradas por especialistas em arquiteturas corporativas. | Calibração por especialistas datada; arquiteturas atuais exigem reavaliação. |
| [Crown Jewels Analysis](https://www.mitre.org/our-impact/intellectual-property/crown-jewels-analysis) — The MITRE Corporation, 2014 | Método, gratuito · **A** | Identificar ativos críticos à missão antes de modelar ameaças. | Guia de engenharia de sistemas; exige adaptação a ambientes corporativos. |
| [Guide to Data-Centric System Threat Modeling](https://csrc.nist.gov/pubs/sp/800/154/ipd) — Murugiah Souppaya; Karen Scarfone, 2016 | Guia ou norma, gratuito · **A** | Rascunho do NIST para modelagem de ameaças centrada em dados. | Rascunho de 2016 nunca finalizado. |
| [Introducing OCTAVE Allegro: Improving the Information Security Risk Assessment Process](https://doi.org/10.1184/R1/6574790.v1) — Richard A. Caralli; James F. Stevens; Lisa R. Young; William R. Wilson, 2007 | Método, gratuito · **A** | Processo de avaliação de risco centrado em ativos de informação. | Foco organizacional; não enumera ameaças técnicas. |
| [Secrets of a Cyber Security Architect](https://www.routledge.com/Secrets-of-a-Cyber-Security-Architect/Schoenfield/p/book/9781032475028) — Brook S. E. Schoenfield, 2019 | Livro, pago · **B** | Prática do arquiteto de segurança, incluindo modelagem em organizações. | Relato de experiência. |

## Fundamentos e estudos empíricos da prática

Origem dos métodos e o que os estudos dizem sobre como equipes realmente modelam.

| Obra / autoria | Tipo / acesso · grau | Contribuição | Limite |
|---|---|---|---|
| [The Threats to Our Products](https://shostack.org/files/microsoft/The-Threats-To-Our-Products.docx) — Loren Kohnfelder; Praerit Garg, 1999 | Artigo técnico, gratuito · **B** | Memorando interno que deu origem às categorias STRIDE. | Documento histórico; o uso atual do STRIDE evoluiu muito. |
| [Uncover Security Design Flaws Using The STRIDE Approach](https://learn.microsoft.com/en-us/archive/msdn-magazine/2006/november/uncover-security-design-flaws-using-the-stride-approach) — Shawn Hernan; Scott Lambert; Tomasz Ostwald; Adam Shostack, 2006 | Artigo técnico, gratuito · **C** | Aplicação de STRIDE por elemento de diagrama de fluxo de dados. | Artigo de 2006 voltado a produtos Microsoft. |
| [Elevation of Privilege: Drawing Developers into Threat Modeling](https://www.usenix.org/conference/3gse14/summit-program/presentation/shostack) — Adam Shostack, 2014 | Artigo, acesso aberto · **A** | Como o jogo Elevation of Privilege leva desenvolvedores a modelar ameaças. | Relato de experiência, não avaliação controlada. |
| [A descriptive study of Microsoft's threat modeling technique](https://doi.org/10.1007/s00766-013-0195-2) — Riccardo Scandariato; Kim Wuyts; Wouter Joosen, 2015 | Artigo, pago · **A** | Estudo empírico de como equipes aplicam a técnica de modelagem da Microsoft (STRIDE). | Amostra de estudantes; generalizar com cuidado. |
| [Threat analysis of software systems: A systematic literature review](https://doi.org/10.1016/j.jss.2018.06.073) — Katja Tuma; Gül Çalikli; Riccardo Scandariato, 2018 | Artigo, pago · **A** | Revisão sistemática de técnicas de análise de ameaças em software. | Recorte até 2017. |
| [Threat modeling: from infancy to maturity](https://doi.org/10.1145/3377816.3381741) — Koen Yskout; Thomas Heyman; Dimitri Van Landuyt; Laurens Sion; Kim Wuyts; Wouter Joosen, 2020 | Artigo, pago · **A** | Posição sobre a maturidade da modelagem de ameaças e desafios de pesquisa. | Artigo curto de posição (NIER). |
| [Adopting threat modelling in agile software development projects](https://doi.org/10.1016/j.jss.2021.111090) — Karin Bernsmed; Daniela Soares Cruzes; Martin Gilje Jaatun; Monica Iovan, 2022 | Artigo, pago · **A** | Estudo de adoção de modelagem de ameaças em projetos ágeis. | Casos de empresas nórdicas. |
| [Solution-aware data flow diagrams for security threat modeling](https://doi.org/10.1145/3167132.3167285) — Laurens Sion; Koen Yskout; Dimitri Van Landuyt; Wouter Joosen, 2018 | Artigo, pago · **A** | Diagramas de fluxo de dados que incluem soluções de segurança na análise. | Proposta acadêmica; suporte de ferramenta limitado. |
| [Trike v.1 Methodology Document [Draft]](https://trike.sourceforge.net/papers/Trike_v1_Methodology_Document-draft.pdf) — Paul Saitta; Brenda Larcom; Michael Eddington, 2005 | Método, gratuito · **B** | Metodologia de modelagem baseada em requisitos e modelo de risco. | Documento inacabado; pouca adoção e manutenção. |
| [Secrets and Lies: Digital Security in a Networked World](https://www.schneier.com/books/secrets-and-lies/) — Bruce Schneier, 2000 | Livro, pago · **B** | Livro que populariza árvores de ataque e pensamento sistêmico em segurança. | Exemplos tecnológicos de 2000. |
| [Threat Modeling Gameplay with EoP: A reference manual for spotting threats in software architecture](https://www.packtpub.com/en-us/product/threat-modeling-gameplay-with-eop-9781804618974) — Brett Crawley, 2024 | Livro, pago · **B** | Livro sobre facilitação com o jogo Elevation of Privilege e variantes. | Foco em facilitação, não em método completo. |
| [Alice and Bob Learn Application Security](https://www.oreilly.com/library/view/alice-and-bob/9781119687351/) — Tanya Janca, 2020 | Livro, pago · **B** | Introdução à segurança de aplicações, com capítulo de modelagem. | Visão ampla, pouca profundidade em modelagem. |
| [Agile Application Security: Enabling Security in a Continuous Delivery Pipeline](https://www.oreilly.com/library/view/agile-application-security/9781491938836/) — Laura Bell; Michael Brunton-Spall; Rich Smith; Jim Bird, 2017 | Livro, pago · **B** | Segurança em equipes ágeis, incluindo modelagem incremental. | Exemplos de 2017. |

## Privacidade

| Obra / autoria | Tipo / acesso · grau | Contribuição | Limite |
|---|---|---|---|
| [A privacy threat analysis framework: supporting the elicitation and fulfillment of privacy requirements](https://doi.org/10.1007/s00766-010-0115-7) — Mina Deng; Kim Wuyts; Riccardo Scandariato; Bart Preneel; Wouter Joosen, 2011 | Artigo, pago · **A** | Artigo que define o LINDDUN e seu processo de análise de privacidade. | Versão original; o método foi revisado depois (LINDDUN GO e PRO). |
| [LINDDUN GO: A Lightweight Approach to Privacy Threat Modeling](https://doi.org/10.1109/EuroSPW51379.2020.00047) — Kim Wuyts; Laurens Sion; Wouter Joosen, 2020 | Artigo, pago · **A** | Versão leve do LINDDUN com cartas para sessões curtas. | Simplificação troca profundidade por velocidade. |
| [Lei nº 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de Dados Pessoais (LGPD)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) — Brasil, 2018 | Guia ou norma, gratuito · **A** | Lei Geral de Proteção de Dados Pessoais. | Lei, não método; modelagem de privacidade precisa de LINDDUN ou similar. |

## Árvores e grafos de ataque

Representar caminhos e escolher onde cortar. Em ordem cronológica, do formalismo à revisão.

| Obra / autoria | Tipo / acesso · grau | Contribuição | Limite |
|---|---|---|---|
| [Foundations of Attack Trees](https://doi.org/10.1007/11734727_17) — Sjouke Mauw; Martijn Oostdijk, 2006 | Artigo, parcial · **A** | Semântica formal das árvores de ataque. | Formalismo matemático; não ensina a construir árvores na prática. |
| [Foundations of Attack–Defense Trees](https://doi.org/10.1007/978-3-642-19751-2_6) — Barbara Kordy; Sjouke Mauw; Savsa Radomirović; Patrick Schweitzer, 2011 | Artigo, gratuito · **A** | Modela ataque e contramedida no mesmo artefato. | Formal; aplicação prática exige ferramenta e dados de custo. |
| [DAG-based attack and defense modeling: Don't miss the forest for the attack trees](https://doi.org/10.1016/j.cosrev.2014.07.001) — Barbara Kordy; Ludovic Piètre-Cambacédès; Patrick Schweitzer, 2014 ⭐ | Artigo, gratuito · **A** | Survey de mais de 30 formalismos em DAG; ajuda a escolher entre árvore e grafo. | Recorte até 2014; formalismos posteriores ficam de fora. |
| [Automated Generation and Analysis of Attack Graphs](https://doi.org/10.1109/SECPRI.2002.1004377) — Oleg Sheyner; Joshua Haines; Somesh Jha; Richard Lippmann; Jeannette M. Wing, 2002 ⭐ | Artigo, pago · **A** | Geração automática de grafos de ataque por model checking. | Model checking não escala para ambientes grandes; marco histórico. |
| [Two Formal Analyses of Attack Graphs](https://pages.cs.wisc.edu/~jha/jha-papers/security/CSFW_2002_1.html) — Somesh Jha; Oleg Sheyner; Jeannette Wing, 2002 | Artigo, parcial · **A** | Conjunto mínimo de medidas que corta caminhos: fundamento de choke points. | Análise formal sobre grafos pequenos; custos de medidas não são reais. |
| [Scalable, Graph-Based Network Vulnerability Analysis](https://doi.org/10.1145/586110.586140) — Paul Ammann; Duminda Wijesekera; Saket Kaushik, 2002 | Artigo, pago · **A** | Hipótese de monotonicidade que torna a análise escalável. | A hipótese de monotonicidade ignora perda de privilégio e defesas ativas. |
| [Managing Attack Graph Complexity Through Visual Hierarchical Aggregation](https://doi.org/10.1145/1029208) — Steven Noel; Sushil Jajodia, 2004 | Artigo, pago · **A** | Agregação e visualização de grafos grandes para o analista. | Visualização não resolve a qualidade do grafo subjacente. Metadados verificados em parte; conferir antes de citar. |
| [MulVAL: A Logic-based Network Security Analyzer](https://www.usenix.org/conference/14th-usenix-security-symposium/mulval-logic-based-network-security-analyzer) — Xinming Ou; Sudhakar Govindavajhala; Andrew W. Appel, 2005 ⭐ | Artigo, gratuito · **A** | Grafos lógicos em Datalog; regras declarativas de interação. | Regras de interação precisam de manutenção; não cobre identidade em nuvem. |
| [Practical Attack Graph Generation for Network Defense](https://doi.org/10.1109/ACSAC.2006.39) — Kyle Ingols; Richard Lippmann; Keith Piwowarski, 2006 | Artigo, pago · **A** | NetSPA: escala com regras reais de firewall. | Foco em alcançabilidade de rede; identidade e SaaS ficam de fora. |
| [Minimum-cost network hardening using attack graphs](https://doi.org/10.1016/j.comcom.2006.06.018) — Lingyu Wang; Steven Noel; Sushil Jajodia, 2006 | Artigo, pago · **A** | Hardening de custo mínimo sobre grafos: base de priorização de mitigação sob orçamento. | Custos de hardening são entradas do analista, não medidas. |
| [Optimal security hardening using multi-objective optimization on attack tree models of networks](https://doi.org/10.1145/1315245.1315272) — Rinku Dewri; Nayot Poolsappasit; Indrajit Ray; Darrell Whitley, 2007 | Artigo, pago · **A** | Trade-off custo × risco residual (páginas e DOI a conferir). | Otimização depende de custos e probabilidades estimados. |
| [Measuring Network Security Using Bayesian Network-Based Attack Graphs](https://doi.org/10.1145/1456362.1456368) — Marcel Frigault; Lingyu Wang, 2008 | Artigo, gratuito · **A** | Métrica probabilística de segurança sobre grafo. | Métrica relativa; não indica probabilidade real de ataque. |
| [Dynamic Security Risk Management Using Bayesian Attack Graphs](https://doi.org/10.1109/TDSC.2011.34) — Nayot Poolsappasit; Rinku Dewri; Indrajit Ray, 2012 ⭐ | Artigo, gratuito · **A** | Grafos bayesianos atualizados com evidência e plano de mitigação com restrição de recursos. | Probabilidades iniciais são subjetivas; inferência cresce com o grafo. |
| [Exact Inference Techniques for the Analysis of Bayesian Attack Graphs](https://doi.org/10.1109/TDSC.2016.2627033) — Luis Muñoz-González; Daniele Sgandurra; Martín Barrère; Emil C. Lupu, 2019 | Artigo, pago · **A** | Inferência exata e escalável em grafos bayesianos. | Matemática exigente; útil quando o grafo já existe. Metadados verificados em parte; conferir antes de citar. |
| [A taxonomy for attack graph generation and usage in network security](https://doi.org/10.1016/j.jisa.2016.02.001) — Kerem Kaynar, 2016 | Artigo, pago · **A** | Taxonomia de geração e uso de grafos de ataque. | Recorte até 2016. |
| [Attack Graph Generation and Analysis Techniques](https://doi.org/10.14429/dsj.66.10795) — Mridul Sankar Barik; Anirban Sengupta; Chandan Mazumdar, 2016 | Artigo, acesso aberto · **A** | Survey complementar de técnicas de geração e análise. | Survey curto; complementar a Kaynar e Lallie. |
| [A review of attack graph and attack tree visual syntax in cyber security](https://doi.org/10.1016/j.cosrev.2019.100219) — Harjinder Singh Lallie; Kurt Debattista; Jay Bal, 2020 ⭐ | Artigo, gratuito · **A** | Padronização visual de árvores e grafos de ataque. | Trata de sintaxe visual, não de eficácia dos modelos. |
| [BloodHound and Attack Path Management](https://github.com/SpecterOps/BloodHound) — SpecterOps | Guia ou norma, gratuito · **C** | Identidade e diretório como grafo de caminhos privilegiados (uso defensivo). | Ferramenta de fornecedor; caminhos de diretório não cobrem todo o ambiente. Metadados verificados em parte; conferir antes de citar. |

## Inteligência, incerteza e qualidade da fonte

Como pesar evidência e fontes antes de mudar a prioridade de um cenário.

| Obra / autoria | Tipo / acesso · grau | Contribuição | Limite |
|---|---|---|---|
| [Words of Estimative Probability](https://www.cia.gov/resources/csi/studies-in-intelligence/archives/vol-8-no-4/words-of-estimative-probability) — Sherman Kent, 1964 ⭐ | Artigo, gratuito · **A** | Correspondência entre termos verbais e faixas de probabilidade. | Faixas propostas em 1964; equipes precisam acordar a própria régua. |
| [Intelligence Community Directive 203: Analytic Standards](https://www.dni.gov/files/documents/ICD/ICD-203.pdf) — Office of the Director of National Intelligence, 2015 ⭐ | Guia ou norma, gratuito · **A** | Padrões de proveniência, incerteza e confiança analítica. | Padrão da comunidade de inteligência dos EUA; adaptar ao contexto corporativo. Metadados verificados em parte; conferir antes de citar. |
| [Structured Analytic Techniques for Intelligence Analysis](https://in.sagepub.com/en-in/sas/structured-analytic-techniques-for-intelligence-analysis/book255432) — Randolph H. Pherson; Richards J. Heuer Jr., 2020 ⭐ | Livro, pago · **B** | Técnicas estruturadas (ACH, checagem de premissas) para hipóteses de ameaça. | Técnicas exigem prática e facilitação; não automatizam julgamento. |
| [MITRE ATT&CK: Design and Philosophy](https://www.mitre.org/news-insights/publication/mitre-attck-design-and-philosophy) — Blake E. Strom; Andy Applebaum; Douglas P. Miller; Kathryn C. Nickels; Adam G. Pennington; Cody B. Thomas, 2018 ⭐ | Artigo, gratuito · **A** | Modelo de táticas, técnicas e subtécnicas e seus usos em detecção, inteligência e risco. | Explica a estrutura do ATT&CK, não como priorizar técnicas para um ambiente. |
| [Finding Cyber Threats with ATT&CK-Based Analytics](https://www.mitre.org/news-insights/publication/finding-cyber-threats-attck-based-analytics) — Blake E. Strom; Joseph A. Battaglia; Michael S. Kemmerer; William Kupersanin; Douglas P. Miller; Craig Wampler; Sean M. Whitley; Ross D. Wolf, 2017 | Artigo, gratuito · **A** | Desenvolvimento de analíticas e avaliação de cobertura (lista completa de autores a conferir). | Metodologia de 2017; detecções e fontes de dados mudaram desde então. |
| [The Pyramid of Pain](https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html) — David J. Bianco, 2013 | Artigo técnico, gratuito · **B** | Priorizar comportamentos (TTPs) sobre indicadores efêmeros. | Post de blog; heurística, não medida. |
| [The Unified Kill Chain: Designing a Unified Kill Chain for analyzing, comparing and defending against cyber attacks](https://www.unifiedkillchain.com/) — Paul Pols, 2017 | Método, gratuito · **B** | Kill chain unificada que combina Kill Chain e ATT&CK em fases ampliadas. | Proposta individual; adoção variável. Metadados verificados em parte; conferir antes de citar. |
| [STIX Version 2.1; TAXII Version 2.1](https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html) — Bret Jordan; Rich Piazza; Trey Darley; Drew Varner, 2021 | Guia ou norma, gratuito · **A** | Padrões de representação e troca de CTI em grafo de objetos. | Padrão de formato; não garante qualidade nem semântica de procedimento. |
| [Indicators of Compromise (IoCs) and Their Role in Attack Defence](https://doi.org/10.17487/RFC9424) — Kirsty Paine; Ollie Whitehouse; James Sellwood; Andrew Shaw, 2023 | Guia ou norma, gratuito · **A** | Ciclo de vida e fragilidade de IOCs. | RFC informativo; não define formato nem métrica. |
| [A survey on technical threat intelligence in the age of sophisticated cyber attacks](https://doi.org/10.1016/j.cose.2017.09.001) — Wiem Tounsi; Helmi Rais, 2018 | Artigo, pago · **A** | Limites de IOCs e problemas de qualidade da CTI técnica. | Recorte até 2017; foco em indicadores técnicos. |
| [Cyber threat intelligence sharing: Survey and research directions](https://doi.org/10.1016/j.cose.2019.101589) — Thomas D. Wagner; Khaled Mahbub; Esther Palomar; Ali E. Abdallah, 2019 ⭐ | Artigo, gratuito · **A** | Confiança, relevância e anonimato no compartilhamento de CTI. | Survey; não mede a qualidade de feeds específicos. |
| [Reading the Tea leaves: A Comparative Analysis of Threat Intelligence](https://www.usenix.org/conference/usenixsecurity19/presentation/li) — Vector Guo Li; Matthew Dunn; Paul Pearce; Damon McCoy; Geoffrey M. Voelker; Stefan Savage; Kirill Levchenko, 2019 ⭐ | Artigo, gratuito · **A** | Feeds têm pouca sobreposição; trate-os como evidência ponderada, não como verdade. | Feeds analisados em 2017–2018; o mercado mudou. |
| [Quality Evaluation of Cyber Threat Intelligence Feeds](https://doi.org/10.1007/978-3-030-57878-7_14) — Harm Griffioen; Tim Booij; Christian Doerr, 2020 | Artigo, pago · **A** | Pontualidade e precisão de feeds; base para decaimento temporal. | Amostra limitada de feeds abertos. |
| [A Comparative Study on Cyber Threat Intelligence: The Security Incident Response Perspective](https://doi.org/10.1109/COMST.2021.3117338) — Daniel Schlette; Marco Caselli; Günther Pernul, 2021 ⭐ | Artigo, gratuito · **A** | Compara 18 conceitos e 6 formatos de CTI; justifica STIX 2.1. | Comparação de formatos, não de plataformas ou feeds. |
| [Measuring and visualizing cyber threat intelligence quality](https://doi.org/10.1007/s10207-020-00490-y) — Daniel Schlette; Fabian Böhm; Marco Caselli; Günther Pernul, 2021 | Artigo, acesso aberto · **A** | Dimensões mensuráveis de qualidade de CTI. | Métricas propostas; adoção em produção não demonstrada. |
| [Cyber Threat Intelligence Mining for Proactive Cybersecurity Defense: A Survey and New Perspectives](https://doi.org/10.1109/COMST.2023.3273282) — Nan Sun et al., 2023 | Artigo, acesso aberto · **A** | Mineração de CTI para defesa proativa. | Survey amplo; usar como mapa, não como avaliação. |
| [ENISA Threat Landscape 2025](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025) — European Union Agency for Cybersecurity (ENISA), 2025 | Guia ou norma, gratuito · **A** | Panorama anual de ameaças na Europa. | Panorama regional; relevância local exige análise. |
| [Top ATT&CK Techniques](https://ctid.mitre.org/projects/top-attack-techniques) — MITRE Center for Threat-Informed Defense, 2024 | Método, gratuito · **A** | Metodologia do CTID para priorizar técnicas ATT&CK por prevalência, chokepoint e acionabilidade. | Prevalência agregada; ajustar ao ambiente. |
| [Practical Threat Intelligence and Data-Driven Threat Hunting: A hands-on guide to threat hunting with the ATT&CK Framework and open source tools](https://packtpub.com/product/practical-threat-intelligence-and-data-driven-threat-hunting/9781838556372) — Valentina Costa-Gazcón, 2021 | Livro, pago · **B** | CTI aplicada a hunting com ATT&CK. | Exemplos ligados a ferramentas da época. |
| [Cyber Threat Intelligence: The No-Nonsense Guide for CISOs and Security Managers](https://doi.org/10.1007/978-1-4842-7220-6) — Aaron Roberts, 2021 | Livro, pago · **B** | Programa de CTI do ponto de vista de gestão. | Visão de gestão; pouco técnico. |
| [Mastering Cyber Intelligence](https://packtpub.com/en-si/product/mastering-cyber-intelligence-9781800209404) — Jean Nestor M. Dahj, 2022 | Livro, pago · **B** | Ciclo de inteligência e integração com operações de segurança. | Livro de visão geral; aprofundar com fontes primárias. |

## ICS e sistemas ciberfísicos

| Obra / autoria | Tipo / acesso · grau | Contribuição | Limite |
|---|---|---|---|
| [The Industrial Control System Cyber Kill Chain](https://www.giac.org/research-papers/36297) — Michael J. Assante; Robert M. Lee, 2015 | Artigo, gratuito · **B** | Kill chain adaptada a ataques a sistemas de controle industrial. | White paper; fases são heurística, não sequência obrigatória. |
| [MITRE ATT&CK for Industrial Control Systems: Design and Philosophy](https://attack.mitre.org/docs/ATTACK_for_ICS_Philosophy_March_2020.pdf) — Otis Alexander; Misha Belisle; Jacob Steele, 2020 | Guia ou norma, gratuito · **A** | Desenho e filosofia do ATT&CK para sistemas de controle industrial. | Explica a estrutura, não como priorizar para uma planta. |

## Da modelagem à detecção: visibilidade e ausência

Do cenário modelado ao que precisa ser observável, e ao que acontece quando a evidência não aparece.

| Obra / autoria | Tipo / acesso · grau | Contribuição | Limite |
|---|---|---|---|
| [Toward a Knowledge Graph of Cybersecurity Countermeasures](https://d3fend.mitre.org/resources/D3FEND.pdf) — Peter E. Kaloroumakis; Michael J. Smith, 2021 ⭐ | Artigo, gratuito · **A** | D3FEND: ontologia que liga contramedidas a técnicas ofensivas. | Mapear contramedidas não comprova eficácia. |
| [Mappings Explorer](https://ctid.mitre.org/projects/mappings-explorer/) — MITRE Center for Threat-Informed Defense, 2024 | Catálogo, gratuito · **A** | Mapeamentos de controles e capacidades de segurança para ATT&CK (Mappings Explorer). | Mapeamento não comprova eficácia. |
| [The Practice of Network Security Monitoring: Understanding Incident Detection and Response](https://nostarch.com/nsm) — Richard Bejtlich, 2013 | Livro, pago · **B** | Coleta orientada por necessidade, precursora de requisitos de telemetria. | Foco em rede; endpoint, identidade e nuvem exigem outras fontes. |
| [Applied Network Security Monitoring: Collection, Detection, and Analysis](https://shop.elsevier.com/books/applied-network-security-monitoring/sanders/978-0-12-417208-1) — Chris Sanders; Jason Smith, 2013 | Livro, pago · **B** | Coleta, detecção e análise em NSM. | Ferramentas da época; princípios permanecem. |
| [Crafting the InfoSec Playbook: Security Monitoring and Incident Response Master Plan](https://www.oreilly.com/library/view/crafting-the-infosec/9781491913598/) — Jeff Bollinger; Brandon Enright; Matthew Valites, 2015 | Livro, pago · **B** | Playbooks de detecção a partir de objetivos e dados. | Casos de uma organização específica. |
| [How does Endpoint Detection use the MITRE ATT&CK Framework?](https://www.usenix.org/conference/usenixsecurity24/presentation/virkud) — Apurva Virkud; Muhammad Adil Inam; Andy Riddle; Jason Liu; Gang Wang; Adam Bates, 2024 ⭐ | Artigo, gratuito · **A** | Mostra os limites de “cobertura ATT&CK” como métrica. | Estuda regras de EDR públicas; regras proprietárias podem diferir. |
| [99% False Positives: A Qualitative Study of SOC Analysts' Perspectives on Security Alarms](https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi) — Bushra A. Alahmadi; Louise Axon; Ivan Martinovic, 2022 ⭐ | Artigo, gratuito · **A** | Propriedades de um bom alarme e fadiga de alertas no SOC. | Estudo qualitativo com amostra de analistas. |
| [A Human Capital Model for Mitigating Security Analyst Burnout](https://www.usenix.org/conference/soups2015/proceedings/presentation/sundaramurthy) — Sathya Chandran Sundaramurthy et al., 2015 | Artigo, gratuito · **A** | Burnout e capital humano em SOCs. | Contexto acadêmico de SOCs; generalizar com cuidado. |
| [Efficient Data Structures for Tamper-Evident Logging](https://www.usenix.org/conference/usenixsecurity09/technical-sessions/presentation/efficient-data-structures-tamper-evident) — Scott A. Crosby; Dan S. Wallach, 2009 | Artigo, gratuito · **A** | Integridade de logs: se o log não é examinado, a adulteração não é detectada. | Trata de integridade, não de ausência de eventos. |
| [Custos: Practical Tamper-Evident Auditing of Operating Systems Using Trusted Execution](https://doi.org/10.14722/ndss.2020.24065) — Riccardo Paccagnella et al., 2020 | Artigo, gratuito · **A** | Detecção de truncamento de logs: a ausência como sinal. | Requer execução confiável (SGX); implantação específica. |
| [Beyond Collection: Measuring the Detection Efficacy of Modern Security Logging Standards](https://arxiv.org/abs/2605.05531) — Ryan Holeman; John Hastings; Varghese Mathew Vaidyan, 2026 | Artigo, preprint · **B** | Coletar não é ver: só 20% das cadeias completas de RCE detectadas com CIM, OCSF e ECS (preprint). | Preprint sem revisão por pares; cenários Linux de RCE. |
| [An Empirical Study of Observability Limits in Advanced Software Supply Chain Attacks](https://arxiv.org/abs/2603.16694) — Zhuoran Tan; Wenbo Guo; Jiewen Luo; Taylor Brierley; Jeremy Singer; Christos Anagnostopoulos, 2026 | Artigo, preprint · **B** | Nenhuma fonte isolada recupera 40% dos passos esperados; lacunas de fase inteira (preprint). | Preprint; dataset sintético de cadeia de suprimentos. |
| [Planning and Integrating Deception into Computer Security Defenses](https://www.cerias.purdue.edu/apps/reports_and_papers/view/4777) — Mohammed H. Almeshekah; Eugene H. Spafford, 2014 | Artigo, gratuito · **A** | Planejamento de engano (deception) na defesa. | Framework conceitual; eficácia depende da operação. |
| [MITRE Engage](https://engage.mitre.org) — MITRE | Guia ou norma, gratuito · **A** | Engajamento de adversários e deception defensiva. | Planejamento de engajamento exige autorização e operação madura. Metadados verificados em parte; conferir antes de citar. |

## Risco, priorização e validação de escores

Leitura obrigatória antes de inventar pesos: o que já foi medido, e o que nunca foi.

| Obra / autoria | Tipo / acesso · grau | Contribuição | Limite |
|---|---|---|---|
| [Guide for Conducting Risk Assessments](https://doi.org/10.6028/NIST.SP.800-30r1) — Joint Task Force Transformation Initiative, 2012 | Guia ou norma, gratuito · **A** | Separa probabilidade, impacto e incerteza na avaliação de risco. | Metodologia genérica; escalas qualitativas exigem calibração local. Metadados verificados em parte; conferir antes de citar. |
| [Integrating Cybersecurity and Enterprise Risk Management (ERM)](https://doi.org/10.6028/NIST.IR.8286) — Kevin Stine; Stephen Quinn; Greg Witte; R. K. Gardner, 2020 | Guia ou norma, gratuito · **A** | Liga risco técnico ao registro de riscos corporativo. | Foco em governança; não ensina modelagem técnica. A Rev. 1 (dez. 2025) substitui esta versão. |
| [The NIST Cybersecurity Framework (CSF) 2.0](https://doi.org/10.6028/NIST.CSWP.29) — National Institute of Standards and Technology, 2024 | Guia ou norma, gratuito · **A** | Funções Govern/Identify/Protect/Detect/Respond/Recover; DE.CM para monitoramento contínuo. | Estrutura de resultados, não método de modelagem. |
| [ISO/IEC 27005:2022 — Information security, cybersecurity and privacy protection — Guidance on managing information security risks](https://www.iso.org/standard/80585.html) — International Organization for Standardization; International Electrotechnical Commission, 2022 | Guia ou norma, pago · **A** | Cenários de risco baseados em eventos e em ativos. | Norma paga; orientação, não método fechado. |
| [ABNT NBR ISO/IEC 27005:2023 — Segurança da informação, segurança cibernética e proteção à privacidade — Orientações para gestão de riscos de segurança da informação](https://normas.com.br/visualizar/abnt-nbr-nm/27395/abnt-nbriso-iec27005-seguranca-da-informacao-seguranca-cibernetica-e-protecao-a-privacidade-orientacoes-para-gestao-de-riscos-de-seguranca-da-informacao) — Associação Brasileira de Normas Técnicas, 2023 | Guia ou norma, pago · **A** | Versão brasileira da ISO/IEC 27005. | Norma paga; confirmar edição vigente no catálogo ABNT. Metadados verificados em parte; conferir antes de citar. |
| [ABNT NBR ISO 31000:2018 — Gestão de riscos — Diretrizes](https://www.abntcatalogo.com.br/) — Associação Brasileira de Normas Técnicas (ABNT), 2018 | Guia ou norma, pago · **A** | Princípios gerais de gestão de riscos. | Gestão de riscos geral, não específica de cibersegurança. |
| [Common Vulnerability Scoring System Version 4.0: Specification Document](https://www.first.org/cvss/v4.0/specification-document) — FIRST CVSS Special Interest Group, 2023 | Guia ou norma, gratuito · **A** | Severidade técnica de vulnerabilidades (não é probabilidade de exploração). | Severidade técnica não é probabilidade de exploração nem risco de negócio. |
| [Binding Operational Directive 22-01: Reducing the Significant Risk of Known Exploited Vulnerabilities](https://www.cisa.gov/sites/default/files/publications/Reducing_the_Significant_Risk_of_Known_Exploited_Vulnerabilities_211103.pdf) — Cybersecurity and Infrastructure Security Agency (CISA), 2021 | Guia ou norma, gratuito · **A** | Sinal de exploração confirmada para priorização. | Só cobre exploração conhecida e reportada à CISA. |
| [Exploit Prediction Scoring System (EPSS)](https://doi.org/10.1145/3436242) — Jay Jacobs; Sasha Romanosky; Benjamin Edwards; Idris Adjerid; Michael Roytman, 2021 ⭐ | Artigo, gratuito · **A** | Probabilidade de exploração em 12 meses; exemplo de escore validado (ROC AUC 0,838). | Prevê exploração em geral, não contra a sua organização. |
| [Enhancing Vulnerability Prioritization: Data-Driven Exploit Predictions with Community-Driven Insights](https://arxiv.org/abs/2302.14172) — Jay Jacobs; Sasha Romanosky; Octavian Suciu; Benjamin Edwards; Armin Sarabi, 2023 ⭐ | Artigo, preprint · **B** | EPSS v3 e trade-off cobertura × eficiência de remediação. | Desempenho depende das fontes de exploração usadas no treino. |
| [Prioritizing Vulnerability Response: A Stakeholder-Specific Vulnerability Categorization](https://www.sei.cmu.edu/library/prioritizing-vulnerability-response-a-stakeholder-specific-vulnerability-categorization-version-20/) — Jonathan M. Spring; Eric Hatleback; Allen D. Householder; Art Manion; Deana Shick, 2019 ⭐ | Artigo, gratuito · **A** | SSVC: árvores de decisão em vez de escore único. | Árvores precisam de ajuste aos atores e decisões locais. Metadados verificados em parte; conferir antes de citar. |
| [Comparing Vulnerability Severity and Exploits Using Case-Control Studies](https://doi.org/10.1145/2630069) — Luca Allodi; Fabio Massacci, 2014 | Artigo, pago · **A** | Estudo caso-controle que mostra a fraca relação entre CVSS e exploração real. | Dados de 2012–2013. |
| [Empirical Analysis of System-Level Vulnerability Metrics through Actual Attacks](https://doi.org/10.1109/TDSC.2012.66) — Hannes Holm; Mathias Ekstedt; Dennis Andersson, 2012 | Artigo, pago · **A** | Avalia métricas de vulnerabilidade contra ataques reais em ambiente controlado. | Experimento em competição de ataque; ambiente limitado. |
| [Vulnerability Disclosure in the Age of Social Media: Exploiting Twitter for Predicting Real-World Exploits](https://www.usenix.org/biblio/vulnerability-disclosure-age-social-media-exploiting-twitter-predicting-real-world-exploits) — Carl Sabottke; Octavian Suciu; Tudor Dumitraș, 2015 | Artigo, gratuito · **A** | Previsão de exploração real a partir de sinais em redes sociais. | Twitter mudou de acesso e uso; repetir exige outras fontes. |
| [A Survey on Data-driven Software Vulnerability Assessment and Prioritization](https://doi.org/10.1145/3529757) — Triet H. M. Le; Huaming Chen; M. Ali Babar, 2022 | Artigo, gratuito · **A** | Survey de priorização de vulnerabilidades orientada por dados. | Survey acadêmico; foco em vulnerabilidade de software. |
| [Quantified Security is a Weak Hypothesis: A critical survey of results and assumptions](https://doi.org/10.1145/1719030.1719036) — Vilhelm Verendel, 2009 ⭐ | Artigo, pago · **A** | Crítica central: a maioria dos métodos quantitativos não foi validada contra dados. | Recorte até 2008; a crítica continua atual, os métodos avaliados não. |
| [How to Measure Anything in Cybersecurity Risk](https://www.oreilly.com/library/view/how-to-measure/9781119892304/) — Douglas W. Hubbard; Richard Seiersen, 2023 ⭐ | Livro, pago · **B** | Calibração de especialistas e crítica às matrizes ordinais de risco. | Exige disciplina estatística; não traz parâmetros prontos. |
| [Measuring and Managing Information Risk: A FAIR Approach](https://www.oreilly.com/library/view/measuring-and-managing/9780124202313/) — Jack Freund; Jack Jones, 2014 | Livro, pago · **B** | FAIR: quantificação de risco em termos financeiros. | Quantificação depende de estimativas; requer treino em FAIR. |
| [Security Metrics: Replacing Fear, Uncertainty, and Doubt](https://www.informit.com/store/security-metrics-replacing-fear-uncertainty-and-doubt-9780321349989) — Andrew Jaquith, 2007 | Livro, pago · **B** | Métricas de segurança úteis para decisão. | Exemplos de 2007. |
| [Superforecasting: The Art and Science of Prediction](https://www.penguinrandomhouse.com/books/227815/superforecasting-by-philip-e-tetlock-and-dan-gardner/) — Philip E. Tetlock; Dan Gardner, 2015 | Livro, pago · **B** | Avaliação de previsões e Brier score. | Previsões geopolíticas, não de segurança; transferir com cuidado. |
| [Verification of Forecasts Expressed in Terms of Probability](https://doi.org/10.1175/1520-0493%281950%29078%3C0001%3AVOFEIT%3E2.0.CO%3B2) — Glenn W. Brier, 1950 | Artigo, gratuito · **A** | Origem do Brier score para medir calibração. | Artigo curto de meteorologia; a métrica é o que importa. |
| [Cyber Assessment Framework (CAF) v4.0](https://www.ncsc.gov.uk/collection/cyber-assessment-framework) — UK) National Cyber Security Centre (NCSC, 2025 | Guia ou norma, gratuito · **A** | Framework de avaliação de resiliência para operadores de serviços essenciais. | Contexto regulatório do Reino Unido. |
| [Cross-Sector Cybersecurity Performance Goals (CPG 2.0)](https://www.cisa.gov/cybersecurity-performance-goals-2-0-cpg-2-0) — Cybersecurity and Infrastructure Security Agency (CISA), 2025 | Guia ou norma, gratuito · **A** | Metas mínimas de desempenho em cibersegurança para infraestrutura crítica. | Linha de base, não modelo de ameaças. |

## Predição e defesa preemptiva

| Obra / autoria | Tipo / acesso · grau | Contribuição | Limite |
|---|---|---|---|
| [Survey of Attack Projection, Prediction, and Forecasting in Cyber Security](https://doi.org/10.1109/COMST.2018.2871866) — Martin Husák; Jana Komárková; Elias Bou-Harb; Pavel vCeleda, 2019 ⭐ | Artigo, gratuito · **A** | Taxonomia de projeção, predição e previsão de ataques. | Revisão até 2018; aponta, mas não resolve, a falta de métricas comuns. |
| [Predictive methods in cyber defense: Current experience and research challenges](https://doi.org/10.1016/j.future.2020.10.006) — Martin Husák et al., 2021 | Artigo, gratuito · **A** | Desafios práticos: qualidade dos dados de entrada limita a predição. | Experiência de um grupo de pesquisa; generalização limitada. |
| [Cloudy with a Chance of Breach: Forecasting Cyber Security Incidents](https://www.usenix.org/conference/usenixsecurity15/technical-sessions/presentation/liu) — Yang Liu; Armin Sarabi; Jing Zhang; Parinaz Naghizadeh; Manish Karir; Michael Bailey; Mingyan Liu, 2015 | Artigo, acesso aberto · **A** | Previsão de incidentes por sinais externos de higiene. | Sinais externos de higiene, não telemetria interna. |
| [RiskTeller: Predicting the Risk of Cyber Incidents](https://doi.org/10.1145/3133956.3134022) — Leyla Bilge; Yufei Han; Matteo Dell'Amico, 2017 | Artigo, pago · **A** | Predição de risco por máquina a partir de telemetria. | Dados de telemetria de um fornecedor. |
| [Expected Exploitability: Predicting the Development of Functional Vulnerability Exploits](https://www.usenix.org/conference/usenixsecurity22/presentation/suciu) — Octavian Suciu; Connor Nelson; Zhuoer Lyu; Tiffany Bao; Tudor Dumitraș, 2022 | Artigo, acesso aberto · **A** | Previsão da chance de surgir exploit funcional. | Prevê desenvolvimento de exploit, não uso contra uma organização. |
| [The Economics of Information Security Investment](https://doi.org/10.1145/581271.581274) — Lawrence A. Gordon; Martin P. Loeb, 2002 | Artigo, pago · **A** | Retornos decrescentes do investimento em segurança. | Modelo econômico estilizado; pressupostos fortes. |
| [Security and Game Theory: Algorithms, Deployed Systems, Lessons Learned](https://doi.org/10.1017/CBO9780511973031) — Milind Tambe, 2011 | Livro, pago · **B** | Jogos de Stackelberg para alocação defensiva. | Aplicações em segurança física; adaptar à cibersegurança. |

## Arquitetura, zero trust e identidade

| Obra / autoria | Tipo / acesso · grau | Contribuição | Limite |
|---|---|---|---|
| [Zero Trust Architecture](https://doi.org/10.6028/NIST.SP.800-207) — Scott Rose; Oliver Borchert; Stu Mitchell; Sean Connelly, 2020 | Guia ou norma, gratuito · **A** | Relações de confiança e pontos de decisão/aplicação de política. | Arquitetura de referência, não plano de migração. Metadados verificados em parte; conferir antes de citar. |
| [Zero Trust Maturity Model, Version 2.0](https://www.cisa.gov/zero-trust-maturity-model) — Cybersecurity and Infrastructure Security Agency (CISA), 2023 | Guia ou norma, gratuito · **A** | Maturidade de zero trust por pilar. | Modelo de maturidade de órgãos federais dos EUA. |
| [Enterprise Security Architecture: A Business-Driven Approach](https://www.routledge.com/products/9781578203185) — John Sherwood; Andrew Clark; David Lynas, 2005 | Livro, pago · **B** | SABSA: rastreia requisitos de negócio até controles. | Método extenso; aplicar por partes. |
| [Enterprise access model](https://learn.microsoft.com/security/privileged-access-workstations/privileged-access-access-model) — Microsoft | Guia ou norma, gratuito · **C** | Identidade como plano de controle e acesso privilegiado em camadas. | Documentação de fornecedor; centrada em Microsoft. Metadados verificados em parte; conferir antes de citar. |

## IA: ameaças e apoio ao analista

| Obra / autoria | Tipo / acesso · grau | Contribuição | Limite |
|---|---|---|---|
| [Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations](https://doi.org/10.6028/NIST.AI.100-2e2025) — Apostol Vassilev; Alina Oprea; Alie Fordyce; Hyrum Anderson; Xander Davies; Maia Hamin, 2025 | Guia ou norma, gratuito · **A** | Taxonomia e terminologia de ataques e mitigações contra aprendizado de máquina. | Taxonomia, não método de modelagem; muda a cada edição. |
| [Threat Modeling AI/ML Systems and Dependencies](https://learn.microsoft.com/en-us/security/engineering/threat-modeling-aiml) — Andrew Marshall; Jugal Parikh; Emre Kiciman; Ram Shankar Siva Kumar, 2019 | Guia ou norma, gratuito · **C** | Orientação da Microsoft para modelar ameaças em sistemas de IA/ML e suas dependências. | Material de fornecedor. |
| [STRIDE GPT: AI-powered threat modeling using the STRIDE methodology](https://github.com/mrwadams/stride-gpt) — Matthew Adams, 2023 | Ferramenta, gratuito · **B** | Ferramenta open source que gera modelos STRIDE com LLM. | Saída de LLM exige revisão; pode inventar ameaças irrelevantes. Metadados verificados em parte; conferir antes de citar. |
| [Large Language Models for Cyber Security: A Systematic Literature Review](https://doi.org/10.1145/3769676) — Hanxiang Xu; Shenao Wang; Ningke Li; Kailong Wang; Yanjie Zhao; Kai Chen; Ting Yu; Yang Liu; Haoyu Wang, 2025 | Artigo, gratuito · **A** | Revisão de 185 artigos sobre LLM em segurança. | Campo muda rápido; revisão pode desatualizar em meses. |
| [GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer](https://doi.org/10.18653/v1/2024.naacl-long.300) — Urchade Zaratiana; Nadi Tomeh; Pierre Holat; Thierry Charnois, 2024 | Artigo, gratuito · **A** | Extração de entidades zero-shot em relatórios de ameaça. | Modelo de NER genérico; precisa de avaliação em textos de CTI. |
| [TRAM: Threat Report ATT&CK Mapper](https://github.com/center-for-threat-informed-defense/tram) — MITRE Center for Threat-Informed Defense | Guia ou norma, gratuito · **A** | Mapeamento assistido de relatórios para técnicas ATT&CK. | Sugestões de mapeamento exigem revisão humana. |
| [Complacency and Bias in Human Use of Automation: An Attentional Integration](https://doi.org/10.1177/0018720810376055) — Raja Parasuraman; Dietrich H. Manzey, 2010 | Artigo, parcial · **A** | Viés de automação: por que manter revisão humana sobre saídas de IA. | Estudos de automação em geral, não de ferramentas de segurança. |

## Ontologias e grafos de conhecimento

| Obra / autoria | Tipo / acesso · grau | Contribuição | Limite |
|---|---|---|---|
| [UCO: A Unified Cybersecurity Ontology](https://cdn.aaai.org/ocs/ws/ws0163/12574-57427-1-PB.pdf) — Zareen Syed; Ankur Padia; Tim Finin; Lisa Mathews; Anupam Joshi, 2016 | Artigo, gratuito · **A** | Ontologia que integra STIX, CVE e CAPEC. | Ontologia acadêmica; adoção limitada. |
| [Developing an Ontology of the Cyber Security Domain](https://ceur-ws.org/Vol-966/STIDS2012_T06_ObrstEtAl_CyberOntology.pdf) — Leo Obrst; Penny Chase; Richard Markeloff, 2012 | Artigo, acesso aberto · **A** | Bases de ontologia do domínio de segurança. | Proposta inicial de 2012. |
| [Cybersecurity knowledge graphs](https://doi.org/10.1007/s10115-023-01860-3) — Leslie F. Sikos, 2023 | Artigo, gratuito · **A** | Grafos de conhecimento, raciocínio e D3FEND em segurança. | Survey; não fornece um grafo pronto. |

## Fator humano

| Obra / autoria | Tipo / acesso · grau | Contribuição | Limite |
|---|---|---|---|
| [Rápido e devagar: duas formas de pensar](https://www.companhiadasletras.com.br/livro/9788539003839/rapido-e-devagar) — Daniel Kahneman, 2012 | Livro, pago · **B** | Sistema 1/2, ancoragem e disponibilidade em decisões de risco. | Livro de divulgação; parte dos estudos citados teve problemas de replicação. |
| [Sources of Power: How People Make Decisions](https://mitpress.mit.edu/) — Gary Klein, 1998 | Livro, pago · **B** | Decisão naturalística de especialistas. | Estudos com bombeiros e militares; transferência ao SOC é inferência. |

## Brasil

Marcos legais, doutrina e produção nacional.

| Obra / autoria | Tipo / acesso · grau | Contribuição | Limite |
|---|---|---|---|
| [Decreto nº 8.793, de 29 de junho de 2016. Fixa a Política Nacional de Inteligência](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2016/decreto/d8793.htm) — Brasil. Presidência da República, 2016 | Guia ou norma, gratuito · **A** | Marco normativo brasileiro de inteligência. | Marco político, não método. |
| [Decreto nº 11.856, de 26 de dezembro de 2023. Institui a Política Nacional de Cibersegurança e o Comitê Nacional de Cibersegurança](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/decreto/D11856.htm) — Brasil, 2023 | Guia ou norma, gratuito · **A** | Política Nacional de Cibersegurança. | Marco político, não método. |
| [Decreto nº 10.222, de 5 de fevereiro de 2020. Aprova a Estratégia Nacional de Segurança Cibernética](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/decreto/D10222impressao.htm) — Brasil, 2020 | Guia ou norma, gratuito · **A** | Estratégia Nacional de Segurança Cibernética (E-Ciber). | Na prática substituída pelo Decreto 12.573/2025 (nova E-Ciber); revogação expressa do 10.222 não confirmada. |
| [Doutrina da Atividade de Inteligência](https://www.gov.br/abin/pt-br/centrais-de-conteudo/publicacoes/doutrina) — Agência Brasileira de Inteligência (ABIN), 2023 | Guia ou norma, gratuito · **A** | Terminologia nacional de inteligência e avaliação de fontes. | Doutrina de Estado (edição de 2023); terminologia precisa de adaptação ao setor privado. |
| [Ciberguerra, inteligência cibernética e segurança virtual: alguns aspectos](https://repositorio.enap.gov.br/handle/1/4648) — Emerson Wendt, 2011 | Artigo, gratuito · **A** | Inteligência cibernética como produção de conhecimento para decisão preventiva. | Texto conceitual de 2011. |
| [Guerra cognitiva e operaç~oes cibernéticas de influência: vieses cognitivos como tática de combate](https://doi.org/10.58960/rbi.2024.19.252) — Christiano Cruz Ambros, 2024 | Artigo, gratuito · **A** | Vieses cognitivos explorados em operações cibernéticas. | Foco em influência e guerra cognitiva, não em modelagem técnica. |
| [Transformação digital da inteligência nacional brasileira](https://doi.org/10.58960/rbi.2024.19.258) — Diego Serpa, 2024 | Artigo, gratuito · **A** | Contexto de transformação digital na inteligência de Estado. | Contexto institucional; pouco operacional. |

## Método de pesquisa

Para quem vai publicar sobre modelagem de ameaças ou avaliar um método.

| Obra / autoria | Tipo / acesso · grau | Contribuição | Limite |
|---|---|---|---|
| [Design science in information systems research](https://doi.org/10.2307/25148625) — Alan R. Hevner; Salvatore T. March; Jinsoo Park; Sudha Ram, 2004 ⭐ | Artigo, pago · **A** | Diretrizes para criar e avaliar artefatos (métodos, ferramentas). | Diretrizes gerais; exigem operacionalização no projeto. |
| [A Design Science Research Methodology for Information Systems Research](https://doi.org/10.2753/MIS0742-1222240302) — Ken Peffers; Tuure Tuunanen; Marcus A. Rothenberger; Samir Chatterjee, 2007 ⭐ | Artigo, pago · **A** | Processo em seis etapas de Design Science Research. | Processo genérico de DSR. |
| [Design Science Methodology for Information Systems and Software Engineering](https://doi.org/10.1007/978-3-662-43839-8) — Roel J. Wieringa, 2014 ⭐ | Livro, pago · **B** | Ciclo de engenharia e validação de tratamentos. | Denso; ler capítulos de validação primeiro. |
| [Guidelines for performing Systematic Literature Reviews in Software Engineering](https://keele-repository.worktribe.com/OutputFile/460665) — Barbara Kitchenham; Stuart Charters, 2007 | Artigo, gratuito · **B** | Protocolo de revisão sistemática. | Atualizações posteriores existem; conferir versão. Metadados verificados em parte; conferir antes de citar. |
| [Guidelines for conducting systematic mapping studies in software engineering: An update](https://doi.org/10.1016/j.infsof.2015.03.007) — Kai Petersen; Sairam Vakkalanka; Ludwik Kuzniarz, 2015 | Artigo, pago · **A** | Protocolo de mapeamento sistemático. | Específico para mapeamento sistemático. |
| [Experimentation in Software Engineering](https://doi.org/10.1007/978-3-642-29044-2) — Claes Wohlin; Per Runeson; Martin Höst; Magnus C. Ohlsson; Björn Regnell; Anders Wesslén, 2012 | Livro, pago · **B** | Desenho de experimentos em engenharia de software. | Foco em experimentos controlados. |
| [Guidelines for conducting and reporting case study research in software engineering](https://doi.org/10.1007/s10664-008-9102-8) — Per Runeson; Martin Höst, 2009 | Artigo, pago · **A** | Estudo de caso em ambiente real. | Diretrizes; não substituem protocolo do estudo. |
| [Security Quality Requirements Engineering (SQUARE) Methodology](https://kilthub.cmu.edu/articles/report/Security_Quality_Requirements_Engineering_SQUARE_Methodology/6583673) — Nancy R. Mead; Eric D. Hough; Theodore R. Stehney II, 2005 | Método, gratuito · **A** | Engenharia de requisitos de segurança. | Processo de requisitos, não de modelagem de ameaças. |
| [Security Requirements Engineering: A Framework for Representation and Analysis](https://doi.org/10.1109/TSE.2007.70754) — Charles B. Haley; Robin Laney; Jonathan D. Moffett; Bashar Nuseibeh, 2008 | Artigo, pago · **A** | Requisitos de segurança como restrições rastreáveis. | Formalismo de requisitos; curva de aprendizado alta. |

## Lacunas observadas na literatura

*Interpretação editorial desta seleção, não resultado de revisão sistemática.*

1. **Ausência como objeto de pesquisa.** Há trabalhos sobre integridade de logs (Crosby e Wallach; Custos) e sobre cobertura de técnicas (Virkud et al.; DeTT&CT), mas quase nada revisado por pares sobre detectar fontes silenciosas ou eventos esperados que não aparecem. Os dados mais próximos vêm de dois preprints de 2026 (Holeman et al.; Tan et al.).
2. **Organização inteira com inteligência ponderada.** MAL, enterpriseLang e grafos bayesianos modelam o ambiente, mas não incorporam CTI com confiabilidade de fonte e envelhecimento da informação. A literatura de qualidade de CTI (Li et al.; Schlette et al.; Griffioen et al.) não projeta essa qualidade sobre caminhos de ataque.
3. **Da ameaça modelada à especificação de detecção.** ADS, Sigma, D3FEND e Mappings Explorer existem isolados; faltam métodos publicados que derivem requisitos de telemetria e detecções a partir de cenários priorizados, com rastreabilidade.
4. **Validação de escores.** Verendel (2009), Holm et al. (2012) e Allodi e Massacci (2014) mostram que escores de segurança raramente são validados contra dados. O EPSS é exceção rara, com validação pública.
5. **Prática empresarial.** Quase todos os estudos empíricos olham equipes de produto (Scandariato et al.; Bernsmed et al.). O estudo de Stevens et al. (2018) é um dos poucos sobre a organização inteira.
6. **IA com proveniência.** Pouca pesquisa separa o que um modelo propõe do que o analista aceita, apesar da literatura sobre viés de automação (Parasuraman e Manzey).

Uma proposta autoral que trabalha essas lacunas é mantida no [TCEM](https://github.com/Ridd1kulusC0d3r/Cyber-Threat-Context-Modeling); esta bibliografia não a redefine.
