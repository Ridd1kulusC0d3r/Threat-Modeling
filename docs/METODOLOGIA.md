# Metodologia

[Início](../README.md) · [Acervo completo](AWESOME.md) · [Contribuir](../CONTRIBUTING.md)

Cada recurso é um registro em [`data/resources.json`](../data/resources.json) e cada método, em [`data/methods.json`](../data/methods.json). O validador (`scripts/validate.py`) recusa registro sem fonte, autoria, tipo, resumo ou limite. As listas deste repositório são geradas desses dados.

## Graus de fonte

O grau descreve **o tipo de fonte**, não a qualidade das ideias. Um guia de comunidade (B) pode ser mais útil que um paper (A).

| Grau | Significado | Exemplos |
|:---:|---|---|
| **A** | Fonte primária ou institucional: padrão, órgão público, publicação com revisão por pares ou mantenedor do método. | NIST, CISA, NCSC, MITRE, periódicos e conferências com revisão |
| **B** | Fonte primária sem revisão formal: livro, preprint, guia de comunidade, página do autor ou repositório do mantenedor. | Livros de Shostack, preprints no arXiv, OWASP |
| **C** | Material de fornecedor, proponente comercial ou ferramenta de terceiros. | Guias de fornecedores, plataformas comerciais |
| **D** | Comentário ou fonte secundária. | Posts que resumem outras fontes |
| **E** | Legado: herdado do acervo anterior e ainda não revalidado. | Links de [Acervo anterior](ACERVO-ANTERIOR.md) |

O grau inicial foi atribuído pelo domínio e pelo tipo de publicação, e revisto à mão nos itens em destaque. Discordou de um grau? Abra uma [correção](https://github.com/Ridd1kulusC0d3r/Threat-Modeling/issues/new/choose) com a razão.

Um recurso de grau **D** ou **E** não pode ser destaque.

## Acesso, nível e idioma

| Campo | Valores |
|---|---|
| `access` | `free` gratuito · `open-access` acesso aberto · `preprint` · `mixed` parcial (livro com material do autor) · `paid` pago |
| `level` | `intro` introdutório · `intermediate` intermediário · `advanced` avançado |
| `lang` | `en` ou `pt`, o idioma da fonte |

Acesso aberto e licença de reutilização são coisas diferentes. Código público de um livro não torna o livro gratuito.

## Campos de citação

Recursos citáveis podem trazer campos opcionais que alimentam as [referências ABNT](REFERENCIAS-ABNT.md) e o [BibTeX](../referencias/referencias.bib), ambos gerados:

| Campo | Regra |
|---|---|
| `venue` | Periódico com volume, número e páginas; evento; editora e cidade; ou órgão e número do relatório |
| `doi` | Forma curta, `10.xxxx/…`, sem `https://doi.org/` |
| `isbn` | Só dígitos, `X` e hífen |
| `essential` | `true` quando a obra faz parte do [núcleo essencial](TRILHA-DE-LEITURA.md#núcleo-essencial); exige grau A, B ou C |

A referência gerada segue a ABNT NBR 6023:2018 de forma aproximada. Autoria institucional, leis e normas pedem revisão antes de depositar um trabalho.

## Limite e fatos

Todo recurso precisa de um **limite**: o que ele não demonstra ou onde a aplicação exige cuidado. Exemplos: "visibilidade não equivale a detecção"; "mapeamento não comprova eficácia"; "material do proponente, não comparação independente". Fato, inferência e hipótese ficam separados; resumos descrevem o que a fonte contém, não o que concluímos dela.

## Verificação de links

`scripts/check_links.py` consulta cada URL. O campo `checked` só recebe a data quando a URL **respondeu** (2xx ou 3xx).

| Resultado | Significado | Grava `checked`? |
|---|---|:---:|
| reachable | A fonte respondeu | sim |
| blocked | 401, 403 ou 429: muitos sites recusam clientes automatizados | não |
| unreachable | Falha de DNS, TLS, tempo esgotado ou saída de rede restrita; não diz nada sobre o site | não |
| broken | 404, 410 ou outro erro HTTP | não |

`checked` vazio significa "não verificado", nunca "quebrado". Links quebrados confirmados são registrados no campo `limit` do recurso até serem corrigidos.

## Métodos

Um método só entra em [`data/methods.json`](../data/methods.json) com a pergunta que responde, em que está centrado, o que produz, quando usar e o limite. Cada método cita ao menos uma fonte do acervo por id; o validador recusa id inexistente. O estado é `core`, `emerging`, `complementary` ou `legacy`. DREAD, por exemplo, permanece como `legacy`: preservado por referência histórica, sem recomendação de adoção.

## Origem dos registros

O campo `origin` conta de onde veio cada registro: `bibliografia`, `engenharia`, `conferencias` e `catalogo` (documentos desta biblioteca), `acervo` e `referencias` (seleções anteriores), `notion` (notas de estudo importadas), `curadoria` (adições de curadoria) e `referencial` (referencial teórico verificado em 30/10/2026). Veja [Fontes e proveniência](FONTES-E-PROVENIENCIA.md).

## O que esta biblioteca não faz

- Não redistribui livros, slides, gravações ou PDFs de terceiros.
- Não declara cobertura de detecção, eficácia de ferramenta nem conformidade com o TCEM.
- Não atribui ameaças a atores específicos sem fonte.
- Não trata presença na lista como endosso.
