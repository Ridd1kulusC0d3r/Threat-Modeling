# Revisão de graus — 31/10/2026

[Início](../README.md) · [Metodologia](METODOLOGIA.md)

Os graus iniciais saíram de uma regra por domínio e só os destaques tinham sido revistos à mão. Esta revisão passou pelos 106 recursos contra a [definição dos graus](METODOLOGIA.md#graus-de-fonte). Onze registros mudaram de grau e um teve só a autoria corrigida; os demais foram mantidos.

| Recurso | Antes | Depois | Critério |
|---|:---:|:---:|---|
| `stride-microsoft` | E | A | A Microsoft mantém o STRIDE (mantenedor do método); link verificado |
| `sdl-threat-modeling` | C | A | A Microsoft mantém o SDL |
| `bzar` | B | A | Ferramenta institucional do time MITRE ATT&CK |
| `sparta-space-attack-chains` | B | A | A Aerospace Corporation mantém o SPARTA; link não verificável no ambiente da revisão |
| `guisso-threat-modeling-intro` | D | B | Guia prático do próprio autor, não um resumo de terceiros; URL corrigida |
| `pasta-versprite` | E | C | A VerSprite é proponente comercial do PASTA |
| `aws-tm-workshop` | E | C | Material de fornecedor; link verificado |
| `gitlab-appsec-tm` | E | C | Material de fornecedor; endereço atual localizado |
| `elastic-detection-rules` | B | C | Repositório de fornecedor, coerente com `elastic-validate-rules` |
| `chainsaw` | B | C | Ferramenta de fornecedor (WithSecure) |
| `shostack-attack-tmt` | B | D | Comentário crítico sobre trabalho de terceiros |
| `threatmodcon` | B | B | Grau mantido; a autoria anterior ("Threat Modeling Connect") era suposição e foi removida |

## Links corrigidos

- **Guisso:** o caminho da nota do Notion (`/posts/threat-modeling-intro/`) retornava 404. O post existe em `/blog/threat-modeling-intro/`, com o título *Threat Modeling Express: guia prático*, publicado em 28/09/2024.
- **GitLab:** o handbook foi reorganizado; o endereço atual fica sob `security-platforms-architecture/application-security/runbooks/threat-modeling/` (resposta 200).

## O que não mudou, e por quê

- Seguem em **E** os que não pude revalidar: `dread-msdn` (arquivo histórico, preservado como legado), `openstack-threat-analysis`, `stride-lm` e `eop-cards` (links inalcançáveis ou bloqueados no ambiente da revisão).
- Os recursos sem `checked` continuam sem data: bloqueio a robôs ou falha de rede, nunca "quebrado".
- Os graus A–E descrevem o tipo de fonte; um recurso rebaixado não é um recurso pior.
