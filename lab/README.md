# Laboratório de detecção

Regras e fixtures **sintéticas** para três cases. Verificam a lógica da regra e o comportamento quando falta telemetria; não comprovam cobertura real, qualidade de coleta nem ruído de produção.

| Case | Regra | Documento |
|---|---|---|
| `dcsync` | `lab/dcsync/rule.json` | [01-dcsync](../cases/01-dcsync.md) |
| `oauth` | `lab/oauth/rule.json` | [02-oauth](../cases/02-oauth.md) |
| `cloudtrail` | `lab/cloudtrail/rule.json` | [03-cloudtrail](../cases/03-cloudtrail.md) |

```bash
make lab                              # roda todos e falha se algo divergir do esperado
python scripts/lab.py run --case dcsync
```

## Formato

`rule.json` é um subconjunto de Sigma em JSON (stdlib, sem dependências): `selections` com operadores `contains`, `startswith`, `endswith`, `exists`; `condition` com `and`, `or`, `not` e parênteses; `required_fields` é o contrato de telemetria.

`fixtures.jsonl` traz uma linha por evento: `name`, `class` (`positive`, `variant`, `benign`, `degraded`), `expect` (`match`, `no_match`, `degraded`) e `event`.

## Degradação explícita

Se um campo de `required_fields` falta, o resultado é `degraded` e nunca "sem alerta". É o estado "regra habilitada, capacidade degradada" do [case 06](../cases/06-degradacao.md).

## Limites

- Campos são nomes normalizados e simplificados, não o esquema nativo de cada plataforma; mapear antes de portar.
- Aprovações (replicadores, papel de automação) estão fixas nas regras como exemplo; em produção vêm de inventário.
- Próximo degrau: replay de captura rotulada e emulação autorizada (ver [guia](../docs/ENGENHARIA-DE-DETECCAO.md)).
