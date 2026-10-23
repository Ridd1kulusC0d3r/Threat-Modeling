# Movimento lateral versus administração

[Cases](README.md) · [Template](../templates/CASE-DETECCAO.md)

> **Proposta documental — não executada.** Não há regra pronta, dataset local ou resultado validado neste roteiro.

## Missão e pergunta
**Domínio:** Endpoint / Rede. Justificar relações que distinguem sequência suspeita de administração.

## Modelo e fronteiras
Identidade → acesso remoto → ação no destino → execução.

Identificar quem autoriza, onde a autorização é verificada e quais relações atravessam fronteiras de confiança. Não atribuir o cenário a ator específico sem fonte.

## Evidência e pressupostos
- [Referência principal](https://github.com/mitre-attack/bzar)
- [Material complementar](https://github.com/OTRF/ThreatHunter-Playbook)

Comportamentos são informados pelas fontes. Inventário, permissões, janela e configuração são pressupostos locais a confirmar. Registrar versão, trechos de evidência, contradições e desconhecidos.

## Contrato de telemetria
**Fontes:** Autenticação, rede e atividade no destino.

**Campos e condições:** Origem, destino, identidade, sessão, processo e tempo; definir chaves e tolerância a atraso.

Definir retenção, janela e atraso tolerável segundo o ambiente. Não há limiares universais fixados neste roteiro.

## Hipótese analítica
Comparar evento isolado e cadeia; não exigir todas as etapas para emitir qualquer sinal. Medir perda de recall por fontes ausentes.

## Experimento
| Classe | Entrada / condição | Resultado esperado |
|---|---|---|
| Positivo | Sequência rotulada com evidência por etapa. | Sinal e entidades conforme hipótese |
| Benigno próximo | Distribuição de software e administração remota. | Tratamento justificado sem exclusões amplas |
| Variante | Variar nomes e caminhos mantendo comportamento. | Resultado consistente ou limite documentado |
| Degradação | Remover eventos do destino. | Estado explícito de capacidade insuficiente |

Começar com fixture, avançar a replay e depois emulação ponta a ponta autorizada. Registrar pré-requisitos, configuração, limpeza e custos. Nenhuma etapa foi executada nesta edição.

## Entrega e aceitação
Comparação de regras isoladas e correlação.

Exigir contrato verificado, implementação versionada, entradas/saídas preservadas, benignos, variantes, degradação e métricas com denominadores. Lint não é prova de eficácia. Replay não comprova coleta atual.

## Resultado e decisão
**Pendente de execução.** Preencher esperado/observado, hashes, versões, horários e evidências. Decidir implementar, coletar dados, reformular ou rejeitar. Não generalizar um teste à técnica inteira. Revalidar após mudança de arquitetura, sensor, parser, regra ou inteligência.
