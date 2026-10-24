# Da modelagem à engenharia de detecção

[Início](../README.md) · [Cases](../cases/README.md) · [Template](../templates/CASE-DETECCAO.md)

> **Lista estruturada:** os links desta tabela também estão em [`data/resources.json`](../data/resources.json), com grau, acesso e limite, e na [lista gerada](AWESOME.md). Este texto mantém o comentário editorial.

Um case liga missão, cenário plausível, evidência, observáveis, lógica analítica, teste e decisão. Visibilidade possível, dados disponíveis e detecção validada são estados distintos.

## Materiais para produzir casos

| Material original | O que fornece | Limite / aplicação |
|---|---|---|
| [Threat Hunter Playbook](https://github.com/OTRF/ThreatHunter-Playbook) | Notebooks de hipótese, consultas e evidências. | Revisar dependências antes de executar. |
| [OTRF Security Datasets](https://github.com/OTRF/Security-Datasets) | Dados maliciosos e benignos. | Fixar arquivo, hash e licença; README tem indicações divergentes de licença, conferir LICENSE do snapshot antes de redistribuir. |
| [Splunk Security Content](https://github.com/splunk/security_content) | Analytic Stories e detecções. | Separar narrativa e implementação específica. |
| [Splunk Attack Data](https://github.com/splunk/attack_data) | Dados de teste. | Dados só de ataques não medem ruído de produção. |
| [Splunk Attack Range](https://github.com/splunk/attack_range) | Ambiente instrumentado. | Infraestrutura pode gerar custos. |
| [Elastic Detection Rules](https://github.com/elastic/detection-rules) | Desenvolvimento e validação de regras. | Lint não comprova eficácia. |
| [Elastic — Validate and test rules](https://www.elastic.co/docs/solutions/security/detect-and-alert/validate-and-test-rules) | Categorias de testes. | Distinguir schema, lógica e ponta a ponta. |
| [Summiting the Pyramid](https://center-for-threat-informed-defense.github.io/summiting-the-pyramid/) | Robustez, decomposição e cobertura. | Medir implementações testadas, não etiquetas. |
| [Minimum Telemetry Requirements](https://center-for-threat-informed-defense.github.io/summiting-the-pyramid/data-readiness/min-telemetry-reqs/) | Requisitos mínimos de dados. | Documentar campos ausentes. |
| [Sensor Mappings to ATT&CK](https://center-for-threat-informed-defense.github.io/sensor-mappings-to-attack/) | Sensores, eventos e visibilidade. | Preservar versão; estrutura ATT&CK evolui. |
| [DeTT&CT — Data quality](https://github.com/rabobank-cdc/DeTTECT/wiki/data-quality-scoring) | Completude, atraso, consistência e retenção. | Pontuação não substitui teste. |
| [ATT&CK Detection Strategies](https://attack.mitre.org/detectionstrategies/) | Estratégias por comportamento. | Adaptar à arquitetura local. |
| [Sigma Correlation Specification](https://sigmahq.io/sigma-specification/specification/sigma-correlation-rules-specification.html) | Agrupamento, contagem e ordem temporal. | Backend pode não preservar semântica. |
| [Sigma Rules](https://github.com/SigmaHQ/sigma) | Regras compartilháveis. | Mapear campos e avaliar benignos. |
| [Palantir ADS Framework](https://github.com/palantir/alerting-detection-strategy-framework) | Documentar estratégia de detecção. | Registrar resposta e limitações. |
| [Atomic Red Team](https://www.atomicredteam.io/docs/atomic-red-team) | Testes individuais. | Teste atômico não cobre campanha. |
| [CTID Adversary Emulation Library](https://ctid.mitre.org/resources/adversary-emulation-library/) | Planos de emulação. | Adaptar pré-condições ao laboratório. |
| [CTID Micro Emulation Plans](https://ctid.mitre.org/projects/micro-emulation-plans/) | Validação de recortes. | Conclusões limitadas ao exercitado. |
| [Stratus Red Team](https://stratus-red-team.cloud/) | Emulação em nuvem. | Conta de testes; não detectar só o user agent da ferramenta. |
| [OTRF SimuLand](https://github.com/OTRF/SimuLand) | Infraestrutura e coleta. | Configuração influencia rastros. |
| [EVTX-ATTACK-SAMPLES](https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES) | Eventos Windows gravados. | Replay não valida coleta atual. |
| [Chainsaw](https://github.com/WithSecureOpenSource/chainsaw) | Análise EVTX / Sigma. | Verificar campos e compatibilidade. |
| [BZAR](https://github.com/mitre-attack/bzar) | Análise de rede com Zeek. | Revisar compatibilidade de versões. |
| [Detection Engineering Maturity Matrix](https://detectionengineering.io/) | Capacidades da função de detecção. | Maturidade não equivale a eficácia. |
| [Detection Engineering: A Case Study — GitGuardian](https://blog.gitguardian.com/detection-engineering-case-study/) | Exemplo de detecção de execução remota DCOM. | Telemetria e plataforma específicas. |

## Processo guiado
1. Escolher missão, ativo e decisão apoiada.
2. Registrar fonte, data, evidência, hipóteses e desconhecidos.
3. Modelar entidades, pré-condições, confiança e caminhos alternativos.
4. Derivar observáveis do comportamento, sem depender de nome de ferramenta.
5. Especificar campos, entidades, tempo, retenção e saúde da coleta.
6. Implementar a hipótese preservando semântica na plataforma escolhida.
7. Preparar positivos, benignos próximos, variantes e falhas de telemetria.
8. Executar replay identificado ou emulação autorizada; preservar entradas e saídas.
9. Registrar decisão e limites.
10. Revalidar após alterações de arquitetura, regra, parser, sensor ou inteligência.

## O que cada teste comprova

| Teste | Demonstra | Não demonstra |
|---|---|---|
| Schema / lint | Estrutura válida | Detecção do ataque |
| Fixture sintética | Lógica sobre entrada controlada | Telemetria real |
| Replay | Resultado sobre captura preservada | Coleta e transporte atuais |
| Emulação ponta a ponta | Sensor → pipeline → alerta em laboratório | Toda implementação da técnica |
| Operação assistida | Ruído e utilidade no ambiente observado | Cobertura universal |

Proximidade temporal não prova causalidade. Justificar entidade, sessão ou relação. Testar se o resultado depende de marcador da ferramenta em vez do comportamento.

## Métricas
- Recall experimental: positivos detectados / positivos elegíveis executados; relatar separadamente falhas de infraestrutura e cenários não observáveis.
- Precisão: alertas verdadeiros / alertas revisados, com rótulos confiáveis e amostra representativa.
- Latência: ocorrência, coleta, ingestão, execução e alerta; registrar relógios e distribuição.
- Volume por período/população e custo de triagem.
- Robustez por variante e qualidade dos campos, atraso, duplicação e retenção.

Sem dados benignos não estimar ruído de produção. Uma técnica etiquetada não equivale a proteção comprovada.

## Aprofundamento
Na [bibliografia](BIBLIOGRAFIA.md), usar Practical Threat Detection Engineering e Automating Security Detection Engineering para operação; HOLMES, POIROT e UNICORN para proveniência; Procedural Semantics Gap para suposições necessárias à execução.

Este guia é educacional. A especificação oficial do [TCEM](https://github.com/Ridd1kulusC0d3r/Cyber-Threat-Context-Modeling) permanece no projeto de origem; não há declaração de conformidade automática.
