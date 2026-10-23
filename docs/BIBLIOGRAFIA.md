# Bibliografia comentada

[Início](../README.md) · [Engenharia de detecção](ENGENHARIA-DE-DETECCAO.md) · [Conferências](CONFERENCIAS.md)

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