# Fronteira de confiança em CI/CD

[Cases](README.md) · [Template](../templates/CASE-DETECCAO.md)

> **Proposta documental — não executada.** Não há regra pronta, dataset local ou resultado validado neste roteiro.

## Missão e pergunta
**Domínio:** Supply chain. Identificar código não confiável executado em contexto privilegiado.

## Modelo e fronteiras
Contribuição externa → workflow → runner → recurso protegido.

Identificar quem autoriza, onde a autorização é verificada e quais relações atravessam fronteiras de confiança. Não atribuir o cenário a ator específico sem fonte.

## Evidência e pressupostos
- [Referência principal](https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target)
- [Material complementar](https://github.com/elastic/detection-rules)

Comportamentos são informados pelas fontes. Inventário, permissões, janela e configuração são pressupostos locais a confirmar. Registrar versão, trechos de evidência, contradições e desconhecidos.

## Contrato de telemetria
**Fontes:** Workflow versionado, origem de código, contexto de execução e dados do runner.

**Campos e condições:** Repositório, commit, workflow, run ID, gatilho e permissões; verificar disponibilidade por fonte.

Definir retenção, janela e atraso tolerável segundo o ambiente. Não há limiares universais fixados neste roteiro.

## Hipótese analítica
Correlacionar origem, código efetivamente executado e privilégio. Distinguir análise estática de configuração e execução observada.

## Experimento
| Classe | Entrada / condição | Resultado esperado |
|---|---|---|
| Positivo | Workflow de laboratório com marcador inofensivo. | Sinal e entidades conforme hipótese |
| Benigno próximo | PR externo processado sem privilégios sensíveis. | Tratamento justificado sem exclusões amplas |
| Variante | Variar caminho de build sem depender de nome de script. | Resultado consistente ou limite documentado |
| Degradação | Retirar contexto do commit executado. | Estado explícito de capacidade insuficiente |

Começar com fixture, avançar a replay e depois emulação ponta a ponta autorizada. Registrar pré-requisitos, configuração, limpeza e custos. Nenhuma etapa foi executada nesta edição.

## Entrega e aceitação
Separar configuração perigosa, execução e impacto.

Exigir contrato verificado, implementação versionada, entradas/saídas preservadas, benignos, variantes, degradação e métricas com denominadores. Lint não é prova de eficácia. Replay não comprova coleta atual.

## Resultado e decisão
**Pendente de execução.** Preencher esperado/observado, hashes, versões, horários e evidências. Decidir implementar, coletar dados, reformular ou rejeitar. Não generalizar um teste à técnica inteira. Revalidar após mudança de arquitetura, sensor, parser, regra ou inteligência.
