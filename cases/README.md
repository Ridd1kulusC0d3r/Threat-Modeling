# Cases de modelagem para detecção

[Início](../README.md) · [Guia de engenharia](../docs/ENGENHARIA-DE-DETECCAO.md) · [Template](../templates/CASE-DETECCAO.md)

**Seis roteiros documentais; nenhum executado ou validado nesta edição.**

| Case | Domínio | Entrega |
|---|---|---|
| [DCSync e contexto de replicação](01-dcsync.md) | Identidade / AD | https://attack.mitre.org/detectionstrategies/DET0594/ |
| [Consentimento OAuth e uso de permissões](02-oauth.md) | Identidade / SaaS | https://learn.microsoft.com/en-us/security/operations/incident-response-playbook-app-consent |
| [Alteração de auditoria e perda de visibilidade](03-cloudtrail.md) | Nuvem / AWS | https://securitylabs.datadoghq.com/cloud-security-atlas/attacks/stopping-cloudtrail-trail/ |
| [Movimento lateral versus administração](04-movimento-lateral.md) | Endpoint / Rede | https://github.com/mitre-attack/bzar |
| [Fronteira de confiança em CI/CD](05-cicd.md) | Supply chain | https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target |
| [Regra habilitada, capacidade degradada](06-degradacao.md) | Qualidade / Detection as Code | https://github.com/rabobank-cdc/DeTTECT/wiki/data-quality-scoring |

## Ordem de trabalho
DCSync → CloudTrail → degradação → OAuth → movimento lateral → CI/CD.

## Estados
Proposta → implementado → testado em laboratório → avaliado no ambiente → manutenção.
Uma mudança pode devolver o case ao estado degradado. Cada transição exige evidências; revisão documental não é validação operacional.
