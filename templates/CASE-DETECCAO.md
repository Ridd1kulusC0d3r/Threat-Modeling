# Template — case de modelagem para detecção

[Início](../README.md) · [Cases](../cases/README.md)

Modelo educacional; não é schema nem declaração de conformidade TCEM.

## Identificação e decisão
- ID, título, dono, versão, data:
- Status: proposta | implementado | testado em laboratório | avaliado no ambiente | degradado
- Missão, ativo, impacto e decisão apoiada:
- Ambiente e fora de escopo:

## Evidência
| Fonte e versão | Fato da fonte | Inferência local | Confiança e justificativa | Contradições e lacunas |
|---|---|---|---|---|
| Preencher | Preencher | Preencher | Preencher | Preencher |

## Modelo
- Objetivo adversário, capacidade e acesso prévio:
- Entidades, confiança, pré-condições e dependências:
- Caminhos alternativos e pontos de interrupção:
- ATT&CK e versão, apenas quando sustentados:

## Hipótese
Se [comportamento] ocorrer em [condições], esperamos [observáveis] relacionados por [entidade/causalidade]. Explicações benignas: [lista]. Evidência que refuta: [lista].

## Contrato
| Fonte | Campos obrigatórios | Chave de entidade | Configuração | Tempo/atraso | Retenção | Saúde | Ação se faltar |
|---|---|---|---|---|---|---|---|
| Preencher | Preencher | Preencher | Preencher | Preencher | Preencher | Preencher | Preencher |

## Implementação
- Plataforma, versão e revisão da regra:
- Seleções, joins, agrupamento, janela:
- Mapeamento de campos, identidade e ordem:
- Dados nulos, atraso e duplicação:
- Exceções: justificativa, responsável e expiração:
- Triagem e resposta:

## Testes
- Tipo: sintético | replay | emulação ponta a ponta | operação assistida
- Ambiente, autorização, pré-requisitos e limpeza:
- Dataset: URL, licença, revisão, hash e rótulos:
- Versões de regra, parser, sensor e executor:
- Separação de dados de ajuste e avaliação:
- Como evitar reconhecer apenas marcadores da ferramenta:

| ID | Classe | Entrada | Esperado | Observado | Evidência |
|---|---|---|---|---|---|
| P-01 | Positivo | Preencher | Preencher | Não executado | Pendente |
| B-01 | Benigno próximo | Preencher | Preencher | Não executado | Pendente |
| V-01 | Variante | Preencher | Preencher | Não executado | Pendente |
| D-01 | Degradação | Preencher | Preencher | Não executado | Pendente |

## Avaliação
- Recall experimental e denominador:
- Precisão e representatividade:
- Latência e volume:
- Falhas de infraestrutura e cenários não observáveis:
- Limites de generalização:

## Decisão e manutenção
- Ação, justificativa, risco residual, dono e prazo:
- Gatilhos de revalidação:
