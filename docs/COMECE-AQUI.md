# Comece aqui

[Início](../README.md) · [Bibliografia](BIBLIOGRAFIA.md) · [Trilha de leitura](TRILHA-DE-LEITURA.md) · [Cases](../cases/README.md)

## Rota 1 — fundamentos
1. Manifesto: formular escopo, ameaças, respostas e revisão.
2. Shostack: estruturar o processo.
3. PASTA e Schoenfield: ligar negócio, arquitetura e risco.
4. Threat Modeling with ATT&CK: contextualizar comportamento adversário.

**Entregável:** modelo com missão, fronteiras, evidências e pressupostos.

## Rota 2 — análise de inteligência
Ler Diamond Model, Heuer e Intelligence-Driven Incident Response. Depois, Attack Flow e Threat Models over Space and Time.

**Entregável:** hipótese com suporte, contradições, confiança e gatilhos de revisão.

## Rota 3 — engenharia de detecção
Estudar Threat Hunter Playbook, Summiting the Pyramid, Sensor Mappings e DeTT&CT no [guia](ENGENHARIA-DE-DETECCAO.md). Escolher [DCSync](../cases/01-dcsync.md), [CloudTrail](../cases/03-cloudtrail.md) ou [degradação](../cases/06-degradacao.md).

**Entregável:** contrato de telemetria, implementação identificada e testes positivos/benignos/variantes/degradação.

## Rota 4 — aprofundamento científico
Revisão de Xiong e Lagerström → enterpriseLang → HOLMES → POIROT → UNICORN → Procedural Semantics Gap. Os links e limitações estão na [bibliografia](BIBLIOGRAFIA.md).

**Entregável:** comparação de abordagens, dependências de dados e limites de generalização.

## Rota 5 — vieses e análise de hipóteses
Ler Heuer e o Tradecraft Primer da CIA; depois aplicar o Modelo Diamante a um caso e montar uma matriz de hipóteses concorrentes ([método](METODOS.md#análise-de-hipóteses-concorrentes)). Útil em investigação digital, onde o viés de confirmação custa caro.

**Entregável:** matriz hipótese × evidência, com a evidência que mais discrimina e o que mudaria a conclusão.

## Rota 6 — sistemas de IA e agentes
Keynote da SANS sobre IA agêntica → MAESTRO → MITRE ATLAS → OWASP Top 10 para LLM; o panorama de evidência está no [LLMInjection](https://github.com/Ridd1kulusC0d3r/LLmInjection). Veja os [métodos de IA](METODOS.md#mitre-atlas).

**Entregável:** modelo que separa modelo, ferramentas, memória e permissões, com as fronteiras de confiança entre eles.

## Rota 7 — a organização inteira
Stevens et al. (*The Battle for New York*) → MAL e enterpriseLang → grafos de ataque (MulVAL) → grafos bayesianos. Os métodos estão em [Grafos de ataque](METODOS.md#grafos-de-ataque) e [Modelagem empresarial por centro de gravidade](METODOS.md#modelagem-empresarial-por-centro-de-gravidade).

**Entregável:** mapa de ativos, identidades e relações de confiança até os ativos críticos, com os pontos onde vários caminhos convergem.

## Rota 8 — risco, priorização e validação de escores
Verendel → Allodi e Massacci → EPSS → SSVC → Hubbard e Seiersen. Leia antes de criar qualquer escala ou peso.

**Entregável:** critério de priorização com a fonte de cada dado e um plano para medir se o critério acerta.

## Para estudar em profundidade
Siga a [trilha de leitura](TRILHA-DE-LEITURA.md): 16 semanas, uma leitura e uma saída por vez. Para citar, use as [referências ABNT](REFERENCIAS-ABNT.md) ou o [BibTeX](../referencias/referencias.bib).

## Sessão inicial
Escolha uma pergunta concreta, leia uma fonte e preencha missão, hipótese e lacunas no [template](../templates/CASE-DETECCAO.md). Não preencha resultados antes de executar.

## Fronteira editorial
Esta biblioteca contém referências e propostas de exercício. A metodologia formal [TCEM](https://github.com/Ridd1kulusC0d3r/Cyber-Threat-Context-Modeling) permanece em seu repositório.
