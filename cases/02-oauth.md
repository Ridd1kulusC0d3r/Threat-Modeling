# Consentimento OAuth e uso de permissões

[Cases](README.md) · [Template](../templates/CASE-DETECCAO.md)

> **Proposta documental — não executada.** Não há regra pronta, dataset local ou resultado validado neste roteiro.

## Missão e pergunta
**Domínio:** Identidade / SaaS. Distinguir concessão sensível, uso observado e comprometimento confirmado.

## Modelo e fronteiras
Consentimento → permissão → aplicação → recurso.

Identificar quem autoriza, onde a autorização é verificada e quais relações atravessam fronteiras de confiança. Não atribuir o cenário a ator específico sem fonte.

## Evidência e pressupostos
- [Referência principal](https://learn.microsoft.com/en-us/security/operations/incident-response-playbook-app-consent)
- [Material complementar](https://learn.microsoft.com/en-us/entra/architecture/security-operations-applications)

Comportamentos são informados pelas fontes. Inventário, permissões, janela e configuração são pressupostos locais a confirmar. Registrar versão, trechos de evidência, contradições e desconhecidos.

## Contrato de telemetria
**Fontes:** Auditoria de consentimento, contexto da aplicação e atividade do serviço.

**Campos e condições:** Tenant, app/service principal, concedente, permissões, recurso, resultado e tempos. Resolver diferenças entre client ID e object ID.

Definir retenção, janela e atraso tolerável segundo o ambiente. Não há limiares universais fixados neste roteiro.

## Hipótese analítica
Manter alerta independente de concessão de alto risco e acrescentar contexto de uso. Ausência de evidência não prova ausência de uso.

## Experimento
| Classe | Entrada / condição | Resultado esperado |
|---|---|---|
| Positivo | Consentimento não aprovado e atividade correspondente em laboratório. | Sinal e entidades conforme hipótese |
| Benigno próximo | Integração corporativa aprovada. | Tratamento justificado sem exclusões amplas |
| Variante | Alterar nome da aplicação mantendo identificador. | Resultado consistente ou limite documentado |
| Degradação | Remover auditoria do destino. | Estado explícito de capacidade insuficiente |

Começar com fixture, avançar a replay e depois emulação ponta a ponta autorizada. Registrar pré-requisitos, configuração, limpeza e custos. Nenhuma etapa foi executada nesta edição.

## Entrega e aceitação
Linha do tempo separando concessão, uso e confirmação.

Exigir contrato verificado, implementação versionada, entradas/saídas preservadas, benignos, variantes, degradação e métricas com denominadores. Lint não é prova de eficácia. Replay não comprova coleta atual.

## Resultado e decisão
**Pendente de execução.** Preencher esperado/observado, hashes, versões, horários e evidências. Decidir implementar, coletar dados, reformular ou rejeitar. Não generalizar um teste à técnica inteira. Revalidar após mudança de arquitetura, sensor, parser, regra ou inteligência.
