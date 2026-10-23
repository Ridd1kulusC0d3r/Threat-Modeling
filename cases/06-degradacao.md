# Regra habilitada, capacidade degradada

[Cases](README.md) · [Template](../templates/CASE-DETECCAO.md)

> **Proposta documental — não executada.** Não há regra pronta, dataset local ou resultado validado neste roteiro.

## Missão e pergunta
**Domínio:** Qualidade / Detection as Code. Identificar regressão após mudança de parser, campos ou coleta.

## Modelo e fronteiras
Comportamento permanece → evento muda → regra perde correspondência.

Identificar quem autoriza, onde a autorização é verificada e quais relações atravessam fronteiras de confiança. Não atribuir o cenário a ator específico sem fonte.

## Evidência e pressupostos
- [Referência principal](https://github.com/rabobank-cdc/DeTTECT/wiki/data-quality-scoring)
- [Material complementar](https://www.elastic.co/docs/solutions/security/detect-and-alert/validate-and-test-rules)

Comportamentos são informados pelas fontes. Inventário, permissões, janela e configuração são pressupostos locais a confirmar. Registrar versão, trechos de evidência, contradições e desconhecidos.

## Contrato de telemetria
**Fontes:** Fixtures, saídas do parser, execução da regra e saúde do pipeline.

**Campos e condições:** Versões de regra/parser/schema, campos obrigatórios, tempos e identificadores deduplicáveis.

Definir retenção, janela e atraso tolerável segundo o ambiente. Não há limiares universais fixados neste roteiro.

## Hipótese analítica
Testes de contrato independentes do alerta; dados inválidos geram estado degradado, não sucesso silencioso.

## Experimento
| Classe | Entrada / condição | Resultado esperado |
|---|---|---|
| Positivo | Positivo conhecido como controle do experimento. | Sinal e entidades conforme hipótese |
| Benigno próximo | Benignos estáveis e mudanças opcionais compatíveis. | Tratamento justificado sem exclusões amplas |
| Variante | Combinar falhas e preservar rastreabilidade. | Resultado consistente ou limite documentado |
| Degradação | Remover campo obrigatório, renomear schema, atrasar e duplicar eventos. | Estado explícito de capacidade insuficiente |

Começar com fixture, avançar a replay e depois emulação ponta a ponta autorizada. Registrar pré-requisitos, configuração, limpeza e custos. Nenhuma etapa foi executada nesta edição.

## Entrega e aceitação
Histórico de saúde e decisão sobre cobertura.

Exigir contrato verificado, implementação versionada, entradas/saídas preservadas, benignos, variantes, degradação e métricas com denominadores. Lint não é prova de eficácia. Replay não comprova coleta atual.

## Resultado e decisão
**Pendente de execução.** Preencher esperado/observado, hashes, versões, horários e evidências. Decidir implementar, coletar dados, reformular ou rejeitar. Não generalizar um teste à técnica inteira. Revalidar após mudança de arquitetura, sensor, parser, regra ou inteligência.
