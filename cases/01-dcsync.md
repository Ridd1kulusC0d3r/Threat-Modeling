# DCSync e contexto de replicação

[Cases](README.md) · [Template](../templates/CASE-DETECCAO.md)

> **Proposta documental — não executada.** Não há regra pronta, dataset local ou resultado validado neste roteiro.

## Missão e pergunta
**Domínio:** Identidade / AD. Distinguir replicação autorizada de abuso incompatível com identidade ou origem.

## Modelo e fronteiras
Identidade com permissões → solicitação ao controlador → acesso potencial a credenciais.

Identificar quem autoriza, onde a autorização é verificada e quais relações atravessam fronteiras de confiança. Não atribuir o cenário a ator específico sem fonte.

## Evidência e pressupostos
- [Referência principal](https://attack.mitre.org/detectionstrategies/DET0594/)
- [Material complementar](https://github.com/splunk/security_content/blob/develop/detections/endpoint/windows_ad_replication_request_initiated_by_user_account.yml)

Comportamentos são informados pelas fontes. Inventário, permissões, janela e configuração são pressupostos locais a confirmar. Registrar versão, trechos de evidência, contradições e desconhecidos.

## Contrato de telemetria
**Fontes:** Auditoria do controlador e/ou rede; inventário de controladores e integrações autorizadas.

**Campos e condições:** Identidade, alvo, tempo, operação e origem quando disponível. Configurar auditoria e não presumir IP no evento do controlador.

Definir retenção, janela e atraso tolerável segundo o ambiente. Não há limiares universais fixados neste roteiro.

## Hipótese analítica
Sinalizar replicação fora do contexto autorizado; comparar estratégia de auditoria e de rede. Joins não devem eliminar silenciosamente eventos incompletos.

## Experimento
| Classe | Entrada / condição | Resultado esperado |
|---|---|---|
| Positivo | Captura rotulada de replicação suspeita. | Sinal e entidades conforme hipótese |
| Benigno próximo | Replicação e integrações aprovadas. | Tratamento justificado sem exclusões amplas |
| Variante | Variar implementação preservando comportamento. | Resultado consistente ou limite documentado |
| Degradação | Retirar inventário, origem ou campo de operação. | Estado explícito de capacidade insuficiente |

Começar com fixture, avançar a replay e depois emulação ponta a ponta autorizada. Registrar pré-requisitos, configuração, limpeza e custos. Nenhuma etapa foi executada nesta edição.

## Entrega e aceitação
Comparar estratégias e registrar lacunas.

Exigir contrato verificado, implementação versionada, entradas/saídas preservadas, benignos, variantes, degradação e métricas com denominadores. Lint não é prova de eficácia. Replay não comprova coleta atual.

## Resultado e decisão
**Pendente de execução.** Preencher esperado/observado, hashes, versões, horários e evidências. Decidir implementar, coletar dados, reformular ou rejeitar. Não generalizar um teste à técnica inteira. Revalidar após mudança de arquitetura, sensor, parser, regra ou inteligência.
