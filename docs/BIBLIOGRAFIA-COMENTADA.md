# Bibliografia comentada — Threat Modeling

Referencial organizado por eixo, em ABNT NBR 6023:2018, com chave BibTeX para cada obra. Consolidado em **22/10/2026** a partir de pesquisa em indexadores (ACM DL, IEEE Xplore, dblp, Semantic Scholar, arXiv, ACL Anthology) e sites oficiais.

A inclusão indica pertinência ao estudo de modelagem de ameaças e de disciplinas vizinhas, não endosso. O arquivo BibTeX completo está em [`referencias/referencias.bib`](../referencias/referencias.bib).

## Como ler

| Marca | Significado |
|---|---|
| ✅ verificada | Metadados conferidos em fonte primária ou indexador nesta edição |
| 📘 canônica · conferir metadados | Obra amplamente citada; DOI, ISBN ou edição **não** reconferidos. Confira antes de citar |
| ⚠️ não verificada | Dado incerto (edição, título exato ou disponibilidade). Não cite sem confirmar |
| ⭐ | Faz parte do [núcleo essencial](TRILHA-DE-LEITURA.md#núcleo-essencial) |

Preprints (arXiv) não passaram por revisão por pares: use como indício, não como conclusão.

## Eixos

1. [Fundamentos e métodos de modelagem de ameaças](#1-fundamentos) — 6 obras
2. [Modelagem do ambiente corporativo e linguagens de ataque](#2-empresarial) — 5 obras
3. [Árvores e grafos de ataque, caminhos e hardening](#3-grafos) — 18 obras
4. [Modelagem de ameaças para IA e agentes](#4-ia) — 3 obras
5. [Inteligência de ameaças e análise estruturada](#5-cti) — 29 obras
6. [Da modelagem à detecção e à telemetria](#6-deteccao) — 16 obras
7. [Risco, priorização e quantificação](#7-risco) — 19 obras
8. [Predição e defesa preemptiva](#8-predicao) — 10 obras
9. [Arquitetura, zero trust e missão](#9-arquitetura) — 6 obras
10. [Ontologias e grafos de conhecimento](#10-ontologias) — 3 obras
11. [IA e LLMs como apoio ao analista](#11-ia-apoio) — 4 obras
12. [Fator humano](#12-fator-humano) — 2 obras
13. [Método de pesquisa](#13-metodo) — 10 obras

<a id="1-fundamentos"></a>

## 1. Fundamentos e métodos de modelagem de ameaças

- SHOSTACK, Adam. **Threat modeling**: designing for security. Indianapolis: Wiley, 2014. ISBN 978-1-118-80999-0. ⭐  
  **Use para:** Obra de referência do processo em quatro perguntas, STRIDE e fronteiras de confiança. · 📘 canônica · conferir metadados · `shostack2014threat`

- SHOSTACK, Adam. **Threats**: what every engineer should learn from Star Wars. Hoboken: Wiley, 2023.  
  **Use para:** Vocabulário acessível de ameaças para treinar times de engenharia. · 📘 canônica · conferir metadados · `shostack2023threats`

- TARANDACH, Izar; COLES, Matthew J. **Threat modeling**: a practical guide for development teams. Sebastopol: O'Reilly, 2020.  
  **Use para:** Modelagem contínua em times de desenvolvimento e threat modeling as code (pytm). · 📘 canônica · conferir metadados · `tarandach2020threat`

- UCEDAVÉLEZ, Tony; MORANA, Marco M. **Risk centric threat modeling**: process for attack simulation and threat analysis. Hoboken: Wiley, 2015.  
  **Use para:** PASTA: parte dos objetivos de negócio e chega a impacto, simulação e risco. · 📘 canônica · conferir metadados · `ucedavelez2015pasta`

- THREAT MODELING MANIFESTO. **Threat Modeling Manifesto**. [S. l.], 2020. Disponível em: https://www.threatmodelingmanifesto.org. Acesso em: 22 out. 2026. ⭐  
  **Use para:** Valores, princípios e as quatro perguntas (no que trabalhamos, o que pode dar errado, o que faremos, fizemos o suficiente). · ✅ verificada · `tmmanifesto2020`

- XIONG, Wenjun; LAGERSTRÖM, Robert. Threat modeling – a systematic literature review. **Computers & Security**, v. 84, p. 53-69, jul. 2019. DOI: 10.1016/j.cose.2019.03.010. ⭐  
  **Use para:** Revisão sistemática de 54 trabalhos; mostra definições fragmentadas e validação fraca. Ponto de partida acadêmico. · ✅ verificada · `xiong2019threat`

<a id="2-empresarial"></a>

## 2. Modelagem do ambiente corporativo e linguagens de ataque

- JOHNSON, Pontus; LAGERSTRÖM, Robert; EKSTEDT, Mathias. A meta language for threat modeling and attack simulations. In: INTERNATIONAL CONFERENCE ON AVAILABILITY, RELIABILITY AND SECURITY (ARES), 13., 2018, Hamburg. **Proceedings** [...]. New York: ACM, 2018. Art. 38, p. 1-8. DOI: 10.1145/3230833.3232799. ⭐  
  **Use para:** MAL: gera grafos de ataque a partir de modelos de domínio; base da modelagem do ambiente inteiro. · ✅ verificada · `johnson2018mal`

- XIONG, Wenjun; LEGRAND, Emeline; ÅBERG, Oscar; LAGERSTRÖM, Robert. Cyber security threat modeling based on the MITRE Enterprise ATT&CK Matrix. **Software and Systems Modeling**, v. 21, n. 1, p. 157-177, 2022. ⭐  
  **Use para:** enterpriseLang: ATT&CK como linguagem de modelagem de ativos, passos de ataque e defesas (DOI a conferir). · ✅ verificada · `xiong2022enterpriselang`

- WIDEŁ, Wojciech; HACKS, Simon; EKSTEDT, Mathias; JOHNSON, Pontus; LAGERSTRÖM, Robert. The meta attack language – a formal description. **Computers & Security**, 2023. DOI: 10.1016/j.cose.2023.103284.  
  **Use para:** Especificação formal da MAL; útil para quem desenha um esquema de grafo de ambiente. · ✅ verificada · `widel2023mal`

- JOHNSON, Pontus; VERNOTTE, Alexandre; EKSTEDT, Mathias; LAGERSTRÖM, Robert. pwnPr3d: an attack-graph-driven probabilistic threat-modeling approach. In: ARES 2016. **Proceedings** [...]. IEEE, 2016. p. 278-283.  
  **Use para:** Modelagem probabilística com tempo até comprometimento. · ✅ verificada · `johnson2016pwnpr3d`

- SOMMESTAD, Teodor; EKSTEDT, Mathias; HOLM, Hannes. The cyber security modeling language (CySeMoL): a tool for assessing the vulnerability of enterprise system architectures. **IEEE Systems Journal**, v. 7, n. 3, 2013.  
  **Use para:** Probabilidades de sucesso calibradas por especialistas em arquiteturas corporativas. · 📘 canônica · conferir metadados · `sommestad2013cysemol`

<a id="3-grafos"></a>

## 3. Árvores e grafos de ataque, caminhos e hardening

- SCHNEIER, Bruce. Attack trees. **Dr. Dobb's Journal**, v. 24, n. 12, 1999.  
  **Use para:** Origem das árvores de ataque: decomposição de objetivos do atacante. · 📘 canônica · conferir metadados · `schneier1999attack`

- MAUW, Sjouke; OOSTDIJK, Martijn. Foundations of attack trees. In: INFORMATION SECURITY AND CRYPTOLOGY (ICISC 2005). **Lecture Notes in Computer Science**, v. 3935. Berlin: Springer, 2006.  
  **Use para:** Semântica formal das árvores de ataque. · 📘 canônica · conferir metadados · `mauw2005foundations`

- KORDY, Barbara; MAUW, Sjouke; RADOMIROVIĆ, Saša; SCHWEITZER, Patrick. Foundations of attack–defense trees. In: FORMAL ASPECTS OF SECURITY AND TRUST (FAST 2010). **Lecture Notes in Computer Science**, v. 6561, p. 80-95, 2011. DOI: 10.1007/978-3-642-19751-2_6.  
  **Use para:** Modela ataque e contramedida no mesmo artefato. · ✅ verificada · `kordy2011adtrees`

- KORDY, Barbara; PIÈTRE-CAMBACÉDÈS, Ludovic; SCHWEITZER, Patrick. DAG-based attack and defense modeling: don't miss the forest for the attack trees. **Computer Science Review**, v. 13-14, p. 1-38, 2014. DOI: 10.1016/j.cosrev.2014.07.001. ⭐  
  **Use para:** Survey de mais de 30 formalismos em DAG; ajuda a escolher entre árvore e grafo. · ✅ verificada · `kordy2014dag`

- SHEYNER, Oleg; HAINES, Joshua; JHA, Somesh; LIPPMANN, Richard; WING, Jeannette M. Automated generation and analysis of attack graphs. In: IEEE SYMPOSIUM ON SECURITY AND PRIVACY, 2002. **Proceedings** [...]. IEEE, 2002. p. 273-284. ⭐  
  **Use para:** Geração automática de grafos de ataque por model checking. · 📘 canônica · conferir metadados · `sheyner2002automated`

- JHA, Somesh; SHEYNER, Oleg; WING, Jeannette. Two formal analyses of attack graphs. In: IEEE COMPUTER SECURITY FOUNDATIONS WORKSHOP (CSFW), 2002.  
  **Use para:** Conjunto mínimo de medidas que corta caminhos: fundamento de choke points. · 📘 canônica · conferir metadados · `jha2002two`

- AMMANN, Paul; WIJESEKERA, Duminda; KAUSHIK, Saket. Scalable, graph-based network vulnerability analysis. In: ACM CONFERENCE ON COMPUTER AND COMMUNICATIONS SECURITY (CCS), 2002.  
  **Use para:** Hipótese de monotonicidade que torna a análise escalável. · 📘 canônica · conferir metadados · `ammann2002scalable`

- OU, Xinming; GOVINDAVAJHALA, Sudhakar; APPEL, Andrew W. MulVAL: a logic-based network security analyzer. In: USENIX SECURITY SYMPOSIUM, 14., 2005. ⭐  
  **Use para:** Grafos lógicos em Datalog; regras declarativas de interação. · 📘 canônica · conferir metadados · `ou2005mulval`

- INGOLS, Kyle; LIPPMANN, Richard; PIWOWARSKI, Keith. Practical attack graph generation for network defense. In: ANNUAL COMPUTER SECURITY APPLICATIONS CONFERENCE (ACSAC), 2006. IEEE, 2006. p. 121-130.  
  **Use para:** NetSPA: escala com regras reais de firewall. · ✅ verificada · `ingols2006netspa`

- NOEL, Steven; JAJODIA, Sushil. Managing attack graph complexity through visual hierarchical aggregation. In: ACM WORKSHOP ON VISUALIZATION AND DATA MINING FOR COMPUTER SECURITY (VizSEC/DMSEC), 2004.  
  **Use para:** Agregação e visualização de grafos grandes para o analista. · 📘 canônica · conferir metadados · `noel2004managing`

- WANG, Lingyu; NOEL, Steven; JAJODIA, Sushil. Minimum-cost network hardening using attack graphs. **Computer Communications**, v. 29, n. 18, 2006.  
  **Use para:** Hardening de custo mínimo sobre grafos: base de priorização de mitigação sob orçamento. · 📘 canônica · conferir metadados · `wang2006minimum`

- DEWRI, Rinku; POOLSAPPASIT, Nayot; RAY, Indrajit; WHITLEY, Darrell. Optimal security hardening using multi-objective optimization on attack tree models of networks. In: ACM CONFERENCE ON COMPUTER AND COMMUNICATIONS SECURITY (CCS), 2007.  
  **Use para:** Trade-off custo × risco residual (páginas e DOI a conferir). · ✅ verificada · `dewri2007optimal`

- POOLSAPPASIT, Nayot; DEWRI, Rinku; RAY, Indrajit. Dynamic security risk management using Bayesian attack graphs. **IEEE Transactions on Dependable and Secure Computing**, v. 9, n. 1, p. 61-74, 2012. DOI: 10.1109/TDSC.2011.34. ⭐  
  **Use para:** Grafos bayesianos atualizados com evidência e plano de mitigação com restrição de recursos. · ✅ verificada · `poolsappasit2012dynamic`

- FRIGAULT, Marcel; WANG, Lingyu. Measuring network security using Bayesian network-based attack graphs. In: ACM WORKSHOP ON QUALITY OF PROTECTION (QoP), 2008. DOI: 10.1145/1456362.1456368.  
  **Use para:** Métrica probabilística de segurança sobre grafo. · ✅ verificada · `frigault2008measuring`

- MUÑOZ-GONZÁLEZ, Luis; SGANDURRA, Daniele; BARRÈRE, Martín; LUPU, Emil C. Exact inference techniques for the analysis of Bayesian attack graphs. **IEEE Transactions on Dependable and Secure Computing**, v. 16, n. 2, p. 231-244, 2019.  
  **Use para:** Inferência exata e escalável em grafos bayesianos. · ✅ verificada · `munozgonzalez2019exact`

- LALLIE, Harjinder Singh; DEBATTISTA, Kurt; BAL, Jay. A review of attack graph and attack tree visual syntax in cyber security. **Computer Science Review**, v. 35, 100219, 2020. DOI: 10.1016/j.cosrev.2019.100219. ⭐  
  **Use para:** Padronização visual de árvores e grafos de ataque. · ✅ verificada · `lallie2020review`

- KAYNAR, Kerem. A taxonomy for attack graph generation and usage in network security. **Journal of Information Security and Applications**, v. 29, p. 27-56, 2016.  
  **Use para:** Taxonomia de geração e uso de grafos de ataque. · 📘 canônica · conferir metadados · `kaynar2016taxonomy`

- BARIK, Mridul Sankar; SENGUPTA, Anirban; MAZUMDAR, Chandan. Attack graph generation and analysis techniques. **Defence Science Journal**, v. 66, n. 6, 2016.  
  **Use para:** Survey complementar de técnicas de geração e análise. · ✅ verificada · `barik2016attack`

<a id="4-ia"></a>

## 4. Modelagem de ameaças para IA e agentes

- MITRE. **ATLAS**: Adversarial Threat Landscape for Artificial-Intelligence Systems. McLean: MITRE. Disponível em: https://atlas.mitre.org. Acesso em: 22 out. 2026.  
  **Use para:** Táticas e técnicas contra sistemas de IA, no formato do ATT&CK. · ✅ verificada · `mitreatlas`

- OWASP FOUNDATION. **OWASP Top 10 for LLM Applications 2025**. [S. l.]: OWASP GenAI Security Project, 2025. Disponível em: https://genai.owasp.org/llm-top-10/. Acesso em: 22 out. 2026.  
  **Use para:** Riscos de aplicações com LLM (prompt injection, envenenamento, agência excessiva). · ✅ verificada · `owasp2025llm`

- HUANG, Ken. Agentic AI threat modeling framework: MAESTRO. **Cloud Security Alliance Blog**, 6 fev. 2025. Disponível em: https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro. Acesso em: 22 out. 2026.  
  **Use para:** Modelagem de ameaças por camadas para IA agêntica (sete camadas de referência). · ✅ verificada · `huang2025maestro`

<a id="5-cti"></a>

## 5. Inteligência de ameaças e análise estruturada

- HEUER JR., Richards J. **Psychology of intelligence analysis**. Washington, DC: Center for the Study of Intelligence, CIA, 1999. ⭐  
  **Use para:** Vieses cognitivos e Análise de Hipóteses Concorrentes (ACH). · 📘 canônica · conferir metadados · `heuer1999psychology`

- HEUER JR., Richards J.; PHERSON, Randolph H. **Structured analytic techniques for intelligence analysis**. 3. ed. Thousand Oaks: CQ Press, 2020. ⭐  
  **Use para:** Técnicas estruturadas (ACH, checagem de premissas) para hipóteses de ameaça. · 📘 canônica · conferir metadados · `heuer2020sat`

- KENT, Sherman. Words of estimative probability. **Studies in Intelligence**, v. 8, n. 4, 1964. ⭐  
  **Use para:** Correspondência entre termos verbais e faixas de probabilidade. · 📘 canônica · conferir metadados · `kent1964words`

- OFFICE OF THE DIRECTOR OF NATIONAL INTELLIGENCE. **Intelligence Community Directive 203**: analytic standards. Washington, DC: ODNI, 2015. ⭐  
  **Use para:** Padrões de proveniência, incerteza e confiança analítica. · 📘 canônica · conferir metadados · `odni2015icd203`

- NORTH ATLANTIC TREATY ORGANIZATION. **AJP-2.1**: allied joint doctrine for intelligence procedures. Bruxelas: NATO Standardization Office. (Citar a edição efetivamente consultada.)  
  **Use para:** Escala de confiabilidade da fonte (A–F) e credibilidade da informação (1–6), de origem STANAG 2511. · ⚠️ não verificada · `nato_ajp21`

- CALTAGIRONE, Sergio; PENDERGAST, Andrew; BETZ, Christopher. **The diamond model of intrusion analysis**. [S. l.]: Center for Cyber Intelligence Analysis and Threat Research, 2013. (DTIC ADA586960). ⭐  
  **Use para:** Adversário, capacidade, infraestrutura e vítima para estruturar evidência. · 📘 canônica · conferir metadados · `caltagirone2013diamond`

- HUTCHINS, Eric M.; CLOPPERT, Michael J.; AMIN, Rohan M. Intelligence-driven computer network defense informed by analysis of adversary campaigns and intrusion kill chains. In: INTERNATIONAL CONFERENCE ON INFORMATION WARFARE AND SECURITY (ICIW), 6., 2011. ⭐  
  **Use para:** Cyber Kill Chain e defesa orientada por inteligência. · 📘 canônica · conferir metadados · `hutchins2011killchain`

- BIANCO, David J. The pyramid of pain. **Enterprise Detection & Response** (blog), 2013.  
  **Use para:** Priorizar comportamentos (TTPs) sobre indicadores efêmeros. · 📘 canônica · conferir metadados · `bianco2013pyramid`

- STROM, Blake E. et al. **MITRE ATT&CK**: design and philosophy. McLean: The MITRE Corporation, 2018 (rev. mar. 2020). ⭐  
  **Use para:** Modelo de táticas, técnicas e subtécnicas e seus usos em detecção, inteligência e risco. · ✅ verificada · `strom2018attack`

- STROM, Blake E. et al. **Finding cyber threats with ATT&CK-based analytics**. McLean: The MITRE Corporation, 2017. (MTR170202).  
  **Use para:** Desenvolvimento de analíticas e avaliação de cobertura (lista completa de autores a conferir). · ✅ verificada · `strom2017finding`

- OASIS. **STIX Version 2.1**. OASIS Standard, 2021; **TAXII Version 2.1**. OASIS Standard, 2021.  
  **Use para:** Padrões de representação e troca de CTI em grafo de objetos. · 📘 canônica · conferir metadados · `oasis2021stix`

- ROBERTS, Scott J.; BROWN, Rebekah. **Intelligence-driven incident response**. 2. ed. Sebastopol: O'Reilly, 2023.  
  **Use para:** F3EAD e requisitos de inteligência (PIRs). · 📘 canônica · conferir metadados · `roberts2023idir`

- COSTA-GAZCÓN, Valentina. **Practical threat intelligence and data-driven threat hunting**. Birmingham: Packt, 2021.  
  **Use para:** CTI aplicada a hunting com ATT&CK. · 📘 canônica · conferir metadados · `costagazcon2021practical`

- ROBERTS, Aaron. **Cyber threat intelligence**: the no-nonsense guide for CISOs and security managers. Berkeley: Apress, 2021.  
  **Use para:** Programa de CTI do ponto de vista de gestão. · 📘 canônica · conferir metadados · `roberts2021cti`

- BAUTISTA JR., Wilson. **Practical cyber intelligence**. Birmingham: Packt, 2018.  
  **Use para:** Operacionalização de inteligência em SOC. · 📘 canônica · conferir metadados · `bautista2018practical`

- DAHJ, Jean Nestor M. **Mastering cyber intelligence**. Birmingham: Packt, 2022.  
  **Use para:** Ciclo de inteligência e integração com operações de segurança. · 📘 canônica · conferir metadados · `dahj2022mastering`

- TOUNSI, Wiem; RAIS, Helmi. A survey on technical threat intelligence in the age of sophisticated cyber attacks. **Computers & Security**, v. 72, p. 212-233, 2018.  
  **Use para:** Limites de IOCs e problemas de qualidade da CTI técnica. · 📘 canônica · conferir metadados · `tounsi2018survey`

- WAGNER, Thomas D.; MAHBUB, Khaled; PALOMAR, Esther; ABDALLAH, Ali E. Cyber threat intelligence sharing: survey and research directions. **Computers & Security**, v. 87, 101589, nov. 2019. DOI: 10.1016/j.cose.2019.101589. ⭐  
  **Use para:** Confiança, relevância e anonimato no compartilhamento de CTI. · ✅ verificada · `wagner2019cti`

- SCHLETTE, Daniel; CASELLI, Marco; PERNUL, Günther. A comparative study on cyber threat intelligence: the security incident response perspective. **IEEE Communications Surveys & Tutorials**, v. 23, n. 4, p. 2525-2556, 2021. DOI: 10.1109/COMST.2021.3117338. ⭐  
  **Use para:** Compara 18 conceitos e 6 formatos de CTI; justifica STIX 2.1. · ✅ verificada · `schlette2021comparative`

- SCHLETTE, Daniel; BÖHM, Fabian; CASELLI, Marco; PERNUL, Günther. Measuring and visualizing cyber threat intelligence quality. **International Journal of Information Security**, v. 20, p. 21-38, 2021.  
  **Use para:** Dimensões mensuráveis de qualidade de CTI. · ✅ verificada · `schlette2021quality`

- LI, Vector Guo; DUNN, Matthew; PEARCE, Paul; MCCOY, Damon; VOELKER, Geoffrey M.; SAVAGE, Stefan; LEVCHENKO, Kirill. Reading the tea leaves: a comparative analysis of threat intelligence. In: USENIX SECURITY SYMPOSIUM, 28., 2019, Santa Clara. **Proceedings** [...]. USENIX Association, 2019. p. 851-867. ISBN 978-1-939133-06-9. ⭐  
  **Use para:** Feeds têm pouca sobreposição; trate-os como evidência ponderada, não como verdade. · ✅ verificada · `li2019tealeaves`

- GRIFFIOEN, Harm; BOOIJ, Tim; DOERR, Christian. Quality evaluation of cyber threat intelligence feeds. In: APPLIED CRYPTOGRAPHY AND NETWORK SECURITY (ACNS 2020). **Lecture Notes in Computer Science**. Springer, 2020. p. 277-296.  
  **Use para:** Pontualidade e precisão de feeds; base para decaimento temporal. · ✅ verificada · `griffioen2020quality`

- PAINE, K.; WHITEHOUSE, O.; SELLWOOD, J.; SHAW, A. **Indicators of compromise (IoCs) and their role in attack defence**. RFC 9424. [S. l.]: IETF, ago. 2023.  
  **Use para:** Ciclo de vida e fragilidade de IOCs. · ✅ verificada · `rfc9424`

- SUN, Nan et al. Cyber threat intelligence mining for proactive cybersecurity defense: a survey and new perspectives. **IEEE Communications Surveys & Tutorials**, v. 25, n. 3, 2023.  
  **Use para:** Mineração de CTI para defesa proativa. · 📘 canônica · conferir metadados · `sun2023cti`

- BRASIL. Agência Brasileira de Inteligência. **Doutrina da atividade de inteligência**. Brasília: ABIN, 2016. (Confirmar edição vigente.)  
  **Use para:** Terminologia nacional de inteligência e avaliação de fontes. · ⚠️ não verificada · `abin_doutrina`

- BRASIL. Decreto nº 8.793, de 29 de junho de 2016. Fixa a Política Nacional de Inteligência. **Diário Oficial da União**, Brasília, 30 jun. 2016.  
  **Use para:** Marco normativo brasileiro de inteligência. · 📘 canônica · conferir metadados · `brasil2016pni`

- WENDT, Emerson. Ciberguerra, inteligência cibernética e segurança virtual: alguns aspectos. **Revista Brasileira de Inteligência**, Brasília, n. 6, p. 15-26, 2011.  
  **Use para:** Inteligência cibernética como produção de conhecimento para decisão preventiva. · ✅ verificada · `wendt2011ciberguerra`

- AMBROS, Christiano Cruz. Guerra cognitiva e operações cibernéticas de influência: vieses cognitivos como tática de combate. **Revista Brasileira de Inteligência**, n. 19, 2024. DOI: 10.58960/rbi.2024.19.252.  
  **Use para:** Vieses cognitivos explorados em operações cibernéticas. · ✅ verificada · `ambros2024guerra`

- SERPA, Diego. Transformação digital da inteligência nacional brasileira. **Revista Brasileira de Inteligência**, n. 19, dez. 2024. DOI: 10.58960/rbi.2024.19.258.  
  **Use para:** Contexto de transformação digital na inteligência de Estado. · ✅ verificada · `serpa2024transformacao`

<a id="6-deteccao"></a>

## 6. Da modelagem à detecção e à telemetria

- RODDIE, Megan; DEYALSINGH, Jason; KATZ, Gary J. **Practical threat detection engineering**: a hands-on guide to planning, developing, and validating detection capabilities. Birmingham: Packt, 2023. 328 p. ISBN 978-1-80107-671-5. ⭐  
  **Use para:** Ciclo requisitos → desenvolvimento → validação → métricas de detecção. · ✅ verificada · `roddie2023practical`

- BEJTLICH, Richard. **The practice of network security monitoring**. San Francisco: No Starch Press, 2013.  
  **Use para:** Coleta orientada por necessidade, precursora de requisitos de telemetria. · 📘 canônica · conferir metadados · `bejtlich2013nsm`

- SANDERS, Chris; SMITH, Jason. **Applied network security monitoring**. Waltham: Syngress, 2013.  
  **Use para:** Coleta, detecção e análise em NSM. · 📘 canônica · conferir metadados · `sanders2013ansm`

- BOLLINGER, Jeff; ENRIGHT, Brandon; VALITES, Matthew. **Crafting the InfoSec playbook**. Sebastopol: O'Reilly, 2015.  
  **Use para:** Playbooks de detecção a partir de objetivos e dados. · 📘 canônica · conferir metadados · `bollinger2015playbook`

- PALANTIR. **Alerting and Detection Strategy (ADS) framework**. 2017. Disponível em: https://github.com/palantir/alerting-detection-strategy-framework. Acesso em: 22 out. 2026.  
  **Use para:** Modelo de especificação de detecção (objetivo, premissas, pontos cegos, validação). · ✅ verificada · `palantir2017ads`

- KALOROUMAKIS, Peter E.; SMITH, Michael J. **Toward a knowledge graph of cybersecurity countermeasures**. Annapolis Junction: The MITRE Corporation, 2021. Disponível em: https://d3fend.mitre.org/resources/D3FEND.pdf. ⭐  
  **Use para:** D3FEND: ontologia que liga contramedidas a técnicas ofensivas. · ✅ verificada · `kaloroumakis2021d3fend`

- MITRE CENTER FOR THREAT-INFORMED DEFENSE. **Attack Flow**. Disponível em: https://center-for-threat-informed-defense.github.io/attack-flow/.  
  **Use para:** Representação de sequências de técnicas como fluxo. · 📘 canônica · conferir metadados · `ctid_attackflow`

- MITRE CENTER FOR THREAT-INFORMED DEFENSE. **Summiting the Pyramid**. v. 2, dez. 2024. Disponível em: https://ctid.mitre.org/projects/summiting-the-pyramid-v2.  
  **Use para:** Robustez de analíticas frente a evasão. · ✅ verificada · `ctid_summiting`

- RABOBANK CDC. **DeTT&CT**: detect tactics, techniques & combat threats. Disponível em: https://github.com/rabobank-cdc/DeTTECT. Acesso em: 22 out. 2026.  
  **Use para:** Pontua qualidade de fontes de dados, visibilidade e detecção por técnica. · ✅ verificada · `dettect`

- VIRKUD, Apurva; INAM, Muhammad Adil; RIDDLE, Andy; LIU, Jason; WANG, Gang; BATES, Adam. How does endpoint detection use the MITRE ATT&CK framework? In: USENIX SECURITY SYMPOSIUM, 33., 2024. **Proceedings** [...]. p. 3891-3908. ⭐  
  **Use para:** Mostra os limites de “cobertura ATT&CK” como métrica. · ✅ verificada · `virkud2024edr`

- ALAHMADI, Bushra A.; AXON, Louise; MARTINOVIC, Ivan. 99% false positives: a qualitative study of SOC analysts' perspectives on security alarms. In: USENIX SECURITY SYMPOSIUM, 31., 2022, Boston. **Proceedings** [...]. p. 2783-2800. ⭐  
  **Use para:** Propriedades de um bom alarme e fadiga de alertas no SOC. · ✅ verificada · `alahmadi2022falsepositives`

- SUNDARAMURTHY, Sathya Chandran et al. A human capital model for mitigating security analyst burnout. In: SYMPOSIUM ON USABLE PRIVACY AND SECURITY (SOUPS), 2015. p. 347-359.  
  **Use para:** Burnout e capital humano em SOCs. · ✅ verificada · `sundaramurthy2015burnout`

- HOLEMAN, R.; HASTINGS, J.; VAIDYAN, V. M. Beyond collection: measuring the detection efficacy of modern security logging standards. **arXiv**, 2605.05531, 2026. Preprint.  
  **Use para:** Coletar não é ver: só 20% das cadeias completas de RCE detectadas com CIM, OCSF e ECS (preprint). · ✅ verificada · `holeman2026beyond`

- TAN, Z.; GUO, W.; LUO, J.; BRIERLEY, T.; SINGER, J.; ANAGNOSTOPOULOS, C. An empirical study of observability limits in advanced software supply chain attacks. **arXiv**, 2603.16694v2, 2026. Preprint.  
  **Use para:** Nenhuma fonte isolada recupera 40% dos passos esperados; lacunas de fase inteira (preprint). · ✅ verificada · `tan2026observability`

- CROSBY, Scott A.; WALLACH, Dan S. Efficient data structures for tamper-evident logging. In: USENIX SECURITY SYMPOSIUM, 18., 2009.  
  **Use para:** Integridade de logs: se o log não é examinado, a adulteração não é detectada. · ✅ verificada · `crosby2009tamper`

- PACCAGNELLA, Riccardo et al. Custos: practical tamper-evident auditing of operating systems using trusted execution. In: NETWORK AND DISTRIBUTED SYSTEM SECURITY SYMPOSIUM (NDSS), 2020.  
  **Use para:** Detecção de truncamento de logs: a ausência como sinal. · ✅ verificada · `paccagnella2020custos`

<a id="7-risco"></a>

## 7. Risco, priorização e quantificação

- NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. **SP 800-30 Rev. 1**: guide for conducting risk assessments. Gaithersburg: NIST, 2012. DOI: 10.6028/NIST.SP.800-30r1.  
  **Use para:** Separa probabilidade, impacto e incerteza na avaliação de risco. · 📘 canônica · conferir metadados · `nist80030`

- NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. **SP 800-53 Rev. 5**: security and privacy controls for information systems and organizations. Gaithersburg: NIST, 2020.  
  **Use para:** Catálogo de controles; mapeável a ATT&CK. · 📘 canônica · conferir metadados · `nist80053`

- NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. **NISTIR 8286**: integrating cybersecurity and enterprise risk management (ERM). Gaithersburg: NIST, 2020.  
  **Use para:** Liga risco técnico ao registro de riscos corporativo. · 📘 canônica · conferir metadados · `nistir8286`

- NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. **The NIST Cybersecurity Framework (CSF) 2.0**. Gaithersburg: NIST, 2024. (NIST CSWP 29).  
  **Use para:** Funções Govern/Identify/Protect/Detect/Respond/Recover; DE.CM para monitoramento contínuo. · 📘 canônica · conferir metadados · `nist2024csf`

- INTERNATIONAL ORGANIZATION FOR STANDARDIZATION; INTERNATIONAL ELECTROTECHNICAL COMMISSION. **ISO/IEC 27005:2022**: information security, cybersecurity and privacy protection — guidance on managing information security risks. Genebra: ISO, 2022.  
  **Use para:** Cenários de risco baseados em eventos e em ativos. · 📘 canônica · conferir metadados · `iso27005_2022`

- ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR ISO/IEC 27005:2023**: segurança da informação, segurança cibernética e proteção à privacidade — orientações para gestão de riscos de segurança da informação. Rio de Janeiro: ABNT, 2023. (Confirmar status vigente no catálogo ABNT.)  
  **Use para:** Versão brasileira da ISO/IEC 27005. · ✅ verificada · `abnt27005_2023`

- ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR ISO 31000:2018**: gestão de riscos — diretrizes. Rio de Janeiro: ABNT, 2018.  
  **Use para:** Princípios gerais de gestão de riscos. · 📘 canônica · conferir metadados · `abnt31000_2018`

- FORUM OF INCIDENT RESPONSE AND SECURITY TEAMS. **Common Vulnerability Scoring System v4.0**: specification document. [S. l.]: FIRST, 2023.  
  **Use para:** Severidade técnica de vulnerabilidades (não é probabilidade de exploração). · 📘 canônica · conferir metadados · `first2023cvss4`

- CYBERSECURITY AND INFRASTRUCTURE SECURITY AGENCY. **Binding Operational Directive 22-01** e **Known Exploited Vulnerabilities Catalog**. Washington, DC: CISA, 2021.  
  **Use para:** Sinal de exploração confirmada para priorização. · 📘 canônica · conferir metadados · `cisa_kev`

- JACOBS, Jay; ROMANOSKY, Sasha; EDWARDS, Benjamin; ADJERID, Idris; ROYTMAN, Michael. Exploit Prediction Scoring System (EPSS). **Digital Threats: Research and Practice**, v. 2, n. 3, art. 20, p. 1-17, 2021. DOI: 10.1145/3436242. ⭐  
  **Use para:** Probabilidade de exploração em 12 meses; exemplo de escore validado (ROC AUC 0,838). · ✅ verificada · `jacobs2021epss`

- JACOBS, Jay; ROMANOSKY, Sasha; SUCIU, Octavian; EDWARDS, Benjamin; SARABI, Armin. Enhancing vulnerability prioritization: data-driven exploit predictions with community-driven insights. In: WORKSHOP ON THE ECONOMICS OF INFORMATION SECURITY (WEIS), 2023. arXiv:2302.14172. ⭐  
  **Use para:** EPSS v3 e trade-off cobertura × eficiência de remediação. · ✅ verificada · `jacobs2023epss`

- SPRING, Jonathan M.; HATLEBACK, Eric; HOUSEHOLDER, Allen; MANION, Art; SHICK, Deana. **Prioritizing vulnerability response**: a stakeholder-specific vulnerability categorization. Pittsburgh: Carnegie Mellon University, Software Engineering Institute, 2019. (v2.0, 2021.) ⭐  
  **Use para:** SSVC: árvores de decisão em vez de escore único. · ✅ verificada · `spring2019ssvc`

- LE, Triet H. M.; CHEN, Huaming; BABAR, M. Ali. A survey on data-driven software vulnerability assessment and prioritization. **ACM Computing Surveys**, 2022. DOI: 10.1145/3529757.  
  **Use para:** Survey de priorização de vulnerabilidades orientada por dados. · ✅ verificada · `le2022survey`

- HUBBARD, Douglas W.; SEIERSEN, Richard. **How to measure anything in cybersecurity risk**. 2. ed. Hoboken: Wiley, 2023. ISBN 978-1-119-89230-4. ⭐  
  **Use para:** Calibração de especialistas e crítica às matrizes ordinais de risco. · ✅ verificada · `hubbard2023measure`

- FREUND, Jack; JONES, Jack. **Measuring and managing information risk**: a FAIR approach. Oxford: Butterworth-Heinemann, 2014.  
  **Use para:** FAIR: quantificação de risco em termos financeiros. · 📘 canônica · conferir metadados · `freund2014fair`

- JAQUITH, Andrew. **Security metrics**: replacing fear, uncertainty, and doubt. Upper Saddle River: Addison-Wesley, 2007.  
  **Use para:** Métricas de segurança úteis para decisão. · 📘 canônica · conferir metadados · `jaquith2007metrics`

- VERENDEL, Vilhelm. Quantified security is a weak hypothesis: a critical survey of results and assumptions. In: NEW SECURITY PARADIGMS WORKSHOP (NSPW), 2009. p. 37-50. ⭐  
  **Use para:** Crítica central: a maioria dos métodos quantitativos não foi validada contra dados. · 📘 canônica · conferir metadados · `verendel2009quantified`

- TETLOCK, Philip E.; GARDNER, Dan. **Superforecasting**: the art and science of prediction. New York: Crown, 2015.  
  **Use para:** Avaliação de previsões e Brier score. · 📘 canônica · conferir metadados · `tetlock2015superforecasting`

- BRIER, Glenn W. Verification of forecasts expressed in terms of probability. **Monthly Weather Review**, v. 78, n. 1, p. 1-3, 1950.  
  **Use para:** Origem do Brier score para medir calibração. · 📘 canônica · conferir metadados · `brier1950verification`

<a id="8-predicao"></a>

## 8. Predição e defesa preemptiva

- HUSÁK, Martin; KOMÁRKOVÁ, Jana; BOU-HARB, Elias; ČELEDA, Pavel. Survey of attack projection, prediction, and forecasting in cyber security. **IEEE Communications Surveys & Tutorials**, v. 21, n. 1, p. 640-660, 2019. DOI: 10.1109/COMST.2018.2871866. ⭐  
  **Use para:** Taxonomia de projeção, predição e previsão de ataques. · ✅ verificada · `husak2019survey`

- HUSÁK, Martin et al. Predictive methods in cyber defense: current experience and research challenges. **Future Generation Computer Systems**, v. 115, 2021. DOI: 10.1016/j.future.2020.10.006.  
  **Use para:** Desafios práticos: qualidade dos dados de entrada limita a predição. · ✅ verificada · `husak2021predictive`

- LIU, Yang; SARABI, Armin; ZHANG, Jing; NAGHIZADEH, Parinaz; KARIR, Manish; BAILEY, Michael; LIU, Mingyan. Cloudy with a chance of breach: forecasting cyber security incidents. In: USENIX SECURITY SYMPOSIUM, 24., 2015. **Proceedings** [...]. p. 1009-1024.  
  **Use para:** Previsão de incidentes por sinais externos de higiene. · ✅ verificada · `liu2015cloudy`

- BILGE, Leyla; HAN, Yufei; DELL'AMICO, Matteo. RiskTeller: predicting the risk of cyber incidents. In: ACM CONFERENCE ON COMPUTER AND COMMUNICATIONS SECURITY (CCS), 2017.  
  **Use para:** Predição de risco por máquina a partir de telemetria. · 📘 canônica · conferir metadados · `bilge2017riskteller`

- SUCIU, Octavian et al. Expected exploitability: predicting the development of functional vulnerability exploits. In: USENIX SECURITY SYMPOSIUM, 31., 2022. arXiv:2102.07869.  
  **Use para:** Previsão da chance de surgir exploit funcional. · ✅ verificada · `suciu2022expected`

- GORDON, Lawrence A.; LOEB, Martin P. The economics of information security investment. **ACM Transactions on Information and System Security**, v. 5, n. 4, p. 438-457, 2002.  
  **Use para:** Retornos decrescentes do investimento em segurança. · 📘 canônica · conferir metadados · `gordon2002economics`

- TAMBE, Milind. **Security and game theory**: algorithms, deployed systems, lessons learned. Cambridge: Cambridge University Press, 2011.  
  **Use para:** Jogos de Stackelberg para alocação defensiva. · 📘 canônica · conferir metadados · `tambe2011security`

- ALMESHEKAH, Mohammed H.; SPAFFORD, Eugene H. Planning and integrating deception into computer security defenses. In: NEW SECURITY PARADIGMS WORKSHOP (NSPW), 2014.  
  **Use para:** Planejamento de engano (deception) na defesa. · 📘 canônica · conferir metadados · `almeshekah2014deception`

- MITRE. **Engage**: adversary engagement framework. Disponível em: https://engage.mitre.org.  
  **Use para:** Engajamento de adversários e deception defensiva. · 📘 canônica · conferir metadados · `mitre_engage`

- NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. **SP 800-160 Vol. 2 Rev. 1**: developing cyber-resilient systems: a systems security engineering approach. Gaithersburg: NIST, 2021.  
  **Use para:** Técnicas de resiliência cibernética mapeáveis a ações preventivas. · 📘 canônica · conferir metadados · `nist800160v2`

<a id="9-arquitetura"></a>

## 9. Arquitetura, zero trust e missão

- NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. **SP 800-207**: zero trust architecture. Gaithersburg: NIST, 2020. DOI: 10.6028/NIST.SP.800-207.  
  **Use para:** Relações de confiança e pontos de decisão/aplicação de política. · 📘 canônica · conferir metadados · `nist800207`

- CYBERSECURITY AND INFRASTRUCTURE SECURITY AGENCY. **Zero Trust Maturity Model**. Version 2.0. Washington, DC: CISA, 2023.  
  **Use para:** Maturidade de zero trust por pilar. · 📘 canônica · conferir metadados · `cisa2023ztmm`

- SHERWOOD, John; CLARK, Andrew; LYNAS, David. **Enterprise security architecture**: a business-driven approach. San Francisco: CMP Books, 2005.  
  **Use para:** SABSA: rastreia requisitos de negócio até controles. · 📘 canônica · conferir metadados · `sherwood2005sabsa`

- MICROSOFT. **Enterprise access model**. Microsoft Learn. Disponível em: https://learn.microsoft.com/security/privileged-access-workstations/privileged-access-access-model.  
  **Use para:** Identidade como plano de controle e acesso privilegiado em camadas. · 📘 canônica · conferir metadados · `ms_eam`

- MITRE. **Crown jewels analysis**. In: MITRE Systems Engineering Guide. McLean: MITRE.  
  **Use para:** Identificar ativos críticos à missão antes de modelar ameaças. · 📘 canônica · conferir metadados · `mitre_cja`

- SPECTEROPS. **BloodHound** e attack path management. Disponível em: https://github.com/SpecterOps/BloodHound.  
  **Use para:** Identidade e diretório como grafo de caminhos privilegiados (uso defensivo). · 📘 canônica · conferir metadados · `specterops_apm`

<a id="10-ontologias"></a>

## 10. Ontologias e grafos de conhecimento

- SYED, Zareen; PADIA, Ankur; FININ, Tim; MATHEWS, Lisa; JOSHI, Anupam. UCO: a unified cybersecurity ontology. In: AAAI WORKSHOP ON ARTIFICIAL INTELLIGENCE FOR CYBER SECURITY, 2016.  
  **Use para:** Ontologia que integra STIX, CVE e CAPEC. · 📘 canônica · conferir metadados · `syed2016uco`

- OBRST, Leo; CHASE, Penny; MARKELOFF, Richard. Developing an ontology of the cyber security domain. In: SEMANTIC TECHNOLOGIES FOR INTELLIGENCE, DEFENSE, AND SECURITY (STIDS), 2012.  
  **Use para:** Bases de ontologia do domínio de segurança. · 📘 canônica · conferir metadados · `obrst2012ontology`

- SIKOS, Leslie F. Cybersecurity knowledge graphs. **Knowledge and Information Systems**, v. 65, p. 3511-3531, 2023. DOI: 10.1007/s10115-023-01860-3.  
  **Use para:** Grafos de conhecimento, raciocínio e D3FEND em segurança. · ✅ verificada · `sikos2023ckg`

<a id="11-ia-apoio"></a>

## 11. IA e LLMs como apoio ao analista

- XU, Hanxiang et al. Large language models for cyber security: a systematic literature review. **ACM Transactions on Software Engineering and Methodology**, 2025. DOI: 10.1145/3769676.  
  **Use para:** Revisão de 185 artigos sobre LLM em segurança. · ✅ verificada · `xu2025llm4security`

- ZARATIANA, Urchade; TOMEH, Nadi; HOLAT, Pierre; CHARNOIS, Thierry. GLiNER: generalist model for named entity recognition using bidirectional transformer. In: NAACL-HLT 2024, Mexico City. **Proceedings** [...]. ACL, 2024. v. 1, p. 5364-5376. DOI: 10.18653/v1/2024.naacl-long.300.  
  **Use para:** Extração de entidades zero-shot em relatórios de ameaça. · ✅ verificada · `zaratiana2024gliner`

- MITRE CENTER FOR THREAT-INFORMED DEFENSE. **TRAM**: Threat Report ATT&CK Mapper. Disponível em: https://github.com/center-for-threat-informed-defense/tram.  
  **Use para:** Mapeamento assistido de relatórios para técnicas ATT&CK. · ✅ verificada · `ctid_tram`

- PARASURAMAN, Raja; MANZEY, Dietrich H. Complacency and bias in human use of automation: an attentional integration. **Human Factors**, v. 52, n. 3, p. 381-410, 2010.  
  **Use para:** Viés de automação: por que manter revisão humana sobre saídas de IA. · 📘 canônica · conferir metadados · `parasuraman2010complacency`

<a id="12-fator-humano"></a>

## 12. Fator humano

- KAHNEMAN, Daniel. **Rápido e devagar**: duas formas de pensar. Rio de Janeiro: Objetiva, 2012. Título original: Thinking, fast and slow (2011).  
  **Use para:** Sistema 1/2, ancoragem e disponibilidade em decisões de risco. · 📘 canônica · conferir metadados · `kahneman2011thinking`

- KLEIN, Gary. **Sources of power**: how people make decisions. Cambridge: MIT Press, 1998.  
  **Use para:** Decisão naturalística de especialistas. · 📘 canônica · conferir metadados · `klein1998sources`

<a id="13-metodo"></a>

## 13. Método de pesquisa

- HEVNER, Alan R.; MARCH, Salvatore T.; PARK, Jinsoo; RAM, Sudha. Design science in information systems research. **MIS Quarterly**, v. 28, n. 1, p. 75-105, 2004. ⭐  
  **Use para:** Diretrizes para criar e avaliar artefatos (métodos, ferramentas). · 📘 canônica · conferir metadados · `hevner2004design`

- PEFFERS, Ken; TUUNANEN, Tuure; ROTHENBERGER, Marcus A.; CHATTERJEE, Samir. A design science research methodology for information systems research. **Journal of Management Information Systems**, v. 24, n. 3, p. 45-77, 2007. ⭐  
  **Use para:** Processo em seis etapas de Design Science Research. · 📘 canônica · conferir metadados · `peffers2007dsrm`

- WIERINGA, Roel J. **Design science methodology for information systems and software engineering**. Berlin: Springer, 2014. ⭐  
  **Use para:** Ciclo de engenharia e validação de tratamentos. · 📘 canônica · conferir metadados · `wieringa2014design`

- KITCHENHAM, Barbara; CHARTERS, Stuart. **Guidelines for performing systematic literature reviews in software engineering**. Keele: Keele University; Durham: Durham University, 2007. (EBSE Technical Report EBSE-2007-01).  
  **Use para:** Protocolo de revisão sistemática. · 📘 canônica · conferir metadados · `kitchenham2007guidelines`

- PETERSEN, Kai; VAKKALANKA, Sairam; KUZNIARZ, Ludwik. Guidelines for conducting systematic mapping studies in software engineering: an update. **Information and Software Technology**, v. 64, p. 1-18, 2015.  
  **Use para:** Protocolo de mapeamento sistemático. · 📘 canônica · conferir metadados · `petersen2015mapping`

- BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. The goal question metric approach. In: MARCINIAK, John J. (ed.). **Encyclopedia of software engineering**. New York: Wiley, 1994.  
  **Use para:** Derivar métricas de avaliação a partir de objetivos. · 📘 canônica · conferir metadados · `basili1994gqm`

- WOHLIN, Claes et al. **Experimentation in software engineering**. Berlin: Springer, 2012.  
  **Use para:** Desenho de experimentos em engenharia de software. · 📘 canônica · conferir metadados · `wohlin2012experimentation`

- RUNESON, Per; HÖST, Martin. Guidelines for conducting and reporting case study research in software engineering. **Empirical Software Engineering**, v. 14, n. 2, p. 131-164, 2009.  
  **Use para:** Estudo de caso em ambiente real. · 📘 canônica · conferir metadados · `runeson2009case`

- MEAD, Nancy R.; HOUGH, Eric D.; STEHNEY, Theodore R. **Security quality requirements engineering (SQUARE) methodology**. Pittsburgh: CMU/SEI, 2005. (CMU/SEI-2005-TR-009).  
  **Use para:** Engenharia de requisitos de segurança. · 📘 canônica · conferir metadados · `mead2005square`

- HALEY, Charles B.; LANEY, Robin; MOFFETT, Jonathan D.; NUSEIBEH, Bashar. Security requirements engineering: a framework for representation and analysis. **IEEE Transactions on Software Engineering**, v. 34, n. 1, p. 133-153, 2008.  
  **Use para:** Requisitos de segurança como restrições rastreáveis. · 📘 canônica · conferir metadados · `haley2008security`

## Lacunas observadas na literatura

*Interpretação editorial desta seleção, não resultado de revisão sistemática.*

1. **Ausência como objeto de pesquisa.** Há trabalhos sobre integridade de logs e cobertura de técnicas, mas quase nada revisado por pares sobre detectar fontes silenciosas ou eventos esperados que não aparecem. Os dados mais próximos são preprints de 2026 (Holeman et al.; Tan et al.).
2. **Modelagem do ambiente inteiro com inteligência ponderada.** Linguagens como MAL/enterpriseLang e grafos bayesianos modelam o ambiente, mas não incorporam CTI com confiabilidade de fonte e envelhecimento da informação.
3. **Da ameaça modelada à especificação de detecção.** ADS, Sigma e D3FEND existem isolados; faltam métodos publicados que derivem requisitos de telemetria e detecções a partir de cenários priorizados, com rastreabilidade.
4. **Validação de escores.** Verendel (2009) e Husák et al. (2019) apontam falta de validação empírica e de métricas de acurácia; o EPSS é exceção rara, com validação pública.
5. **IA com proveniência.** Pouca pesquisa separa o que um modelo propõe do que o analista aceita, apesar da literatura sobre viés de automação.

Uma proposta autoral que trabalha essas lacunas é mantida no [TCEM](https://github.com/Ridd1kulusC0d3r/Cyber-Threat-Context-Modeling); esta bibliografia não a redefine.

[Início](../README.md) · [Trilha de leitura](TRILHA-DE-LEITURA.md) · [Catálogo](CATALOGO.md)
