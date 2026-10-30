# Contribuir

Esta biblioteca aceita recursos e métodos que ajudam a produzir um modelo de ameaças, uma hipótese ou uma detecção com **evidência**.

## O que queremos

- Livros, papers, guias, manifestos e métodos com fonte original e autoria.
- Ferramentas, datasets e repositórios que alguém usou para modelar ou testar detecções, com o limite conhecido.
- Conferências e talks, com a edição, e o exercício que se pode derivar.
- Correções: link quebrado, grau mal atribuído, limite que faltou, autoria errada.
- Métodos com a pergunta que respondem, e o que não respondem.

## Campos obrigatórios de um recurso

| Campo | Regra |
|---|---|
| `id` | Minúsculas, números e hífen; único |
| `title`, `authors`, `url` | Fonte original; `https` obrigatório; sem URL repetida |
| `type` | `manifesto`, `guide`, `method`, `book`, `paper`, `article`, `conference`, `course`, `tool` ou `dataset` |
| `topics` | Um ou mais de `threat-modeling`, `detection-engineering`, `cti`, `apt`, `ai`, `ics-cps`, `privacy`, `psychology`, `emulation`, `provenance`, `cloud`, `supply-chain`, `attack-graphs`, `risk`, `architecture`, `research-methods` |
| `access` | `free`, `open-access`, `preprint`, `mixed` ou `paid` |
| `grade` | A–E, conforme a [metodologia](docs/METODOLOGIA.md#graus-de-fonte) |
| `level`, `lang` | `intro`, `intermediate` ou `advanced`; `en` ou `pt` |
| `summary` | O que a fonte contém, sem opinião nossa |
| `limit` | O que a fonte **não** demonstra ou onde a aplicação exige cuidado |
| `origin`, `added` | De onde veio; data ISO |
| `checked`, `featured` | `null` até verificar o link; `false` por padrão |
| `venue`, `doi`, `isbn`, `essential` | Opcionais; alimentam as referências ABNT e o BibTeX ([regras](docs/METODOLOGIA.md#campos-de-citação)) |

## Fluxo

```bash
# 1. edite data/resources.json (ou data/methods.json)
make build     # regenera AWESOME, TEMAS, METODOS, REFERENCIAS-ABNT, referencias.bib e os blocos dos READMEs
make check     # valida, testa e confere se os arquivos gerados estão em dia
python scripts/check_links.py --id seu-id --write   # opcional, precisa de rede
```

Não edite os arquivos gerados à mão: o CI recusa PR cujos arquivos gerados não correspondam aos dados.

## Disciplina de evidência

- Prefira a **fonte primária** a agregadores e resumos.
- Separe fato, inferência e hipótese. O resumo descreve a fonte.
- Preprint, artigo publicado e apresentação não recebem o mesmo peso; use o grau e o campo `access`.
- Material de fornecedor é grau C, ainda que útil.
- Sem endosso por presença: listar não é avaliar.
- Se o grau, a autoria ou o ano forem incertos, deixe o campo conservador (`year: null`) e diga no `limit`.

## Material que não aceitamos

- Cópias de livros, slides, gravações ou PDFs de terceiros. Aponte para a fonte.
- Credenciais, dados privados de vítimas, tokens ou instruções para comprometer sistemas de terceiros.
- Atribuição de ataques a atores sem fonte.

Uso defensivo: técnicas ofensivas aparecem aqui para entender e testar defesas, com autorização.
