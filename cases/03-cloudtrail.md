# Alteração de auditoria e perda de visibilidade

[Cases](README.md) · [Template](../templates/CASE-DETECCAO.md)

> **Proposta documental — não executada.** Não há regra pronta, dataset local ou resultado validado neste roteiro.

## Missão e pergunta
**Domínio:** Nuvem / AWS. Distinguir mudança administrativa, falha de entrega e possível evasão.

## Modelo e fronteiras
Sessão privilegiada → alteração de auditoria → redução da visibilidade.

Identificar quem autoriza, onde a autorização é verificada e quais relações atravessam fronteiras de confiança. Não atribuir o cenário a ator específico sem fonte.

## Evidência e pressupostos
- [Referência principal](https://securitylabs.datadoghq.com/cloud-security-atlas/attacks/stopping-cloudtrail-trail/)
- [Material complementar](https://stratus-red-team.cloud/user-guide/getting-started/)

Comportamentos são informados pelas fontes. Inventário, permissões, janela e configuração são pressupostos locais a confirmar. Registrar versão, trechos de evidência, contradições e desconhecidos.

## Contrato de telemetria
**Fontes:** Eventos administrativos, estado de configuração e monitoramento independente da entrega.

**Campos e condições:** Conta, região, identidade/sessão, operação, alvo, resultado, event time e ingest time. Definir expectativa verificável de entrega.

Definir retenção, janela e atraso tolerável segundo o ambiente. Não há limiares universais fixados neste roteiro.

## Hipótese analítica
Separar alerta de alteração e monitor de saúde. Ausência significa perda de visibilidade até haver evidência de causa.

## Experimento
| Classe | Entrada / condição | Resultado esperado |
|---|---|---|
| Positivo | Replay identificado ou teste Stratus em conta isolada. | Sinal e entidades conforme hipótese |
| Benigno próximo | Manutenção aprovada e janela sem atividade esperada. | Tratamento justificado sem exclusões amplas |
| Variante | Variar atraso e duplicação. | Resultado consistente ou limite documentado |
| Degradação | Interromper só ingestão e comparar com alteração na origem. | Estado explícito de capacidade insuficiente |

Começar com fixture, avançar a replay e depois emulação ponta a ponta autorizada. Registrar pré-requisitos, configuração, limpeza e custos. Nenhuma etapa foi executada nesta edição.

## Entrega e aceitação
Matriz de causas e evidências de falha/evasão.

Exigir contrato verificado, implementação versionada, entradas/saídas preservadas, benignos, variantes, degradação e métricas com denominadores. Lint não é prova de eficácia. Replay não comprova coleta atual.

## Resultado e decisão
**Pendente de execução.** Preencher esperado/observado, hashes, versões, horários e evidências. Decidir implementar, coletar dados, reformular ou rejeitar. Não generalizar um teste à técnica inteira. Revalidar após mudança de arquitetura, sensor, parser, regra ou inteligência.
