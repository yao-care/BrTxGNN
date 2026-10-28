---
layout: default
title: Fentanyl
parent: Apenas Predição do Modelo (L5)
nav_order: 314
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Fentanyl: nova indicação prevista, Síndrome Nefrogênica de Antidiurese Inapropriada (Nephrogenic Syndrom… (nível de evidência L5). Indicação original: Analgésicos narcóticos"
monitor_inn: "FENTANYL"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome"]
---

# Fentanyl
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **2** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relatório de avaliação farmacêutica

</div>

## Fentanila: Da analgesia opioide à síndrome nefrogênica de antidiurese inapropriada
{: .text-alpha }

## Resumo em Uma Frase

Fentanila (fentanyl) é um analgésico opioide narcótico, registrado na ANVISA como analgésico narcótico e anestésico opioide.
O modelo TxGNN prevê que pode ser eficaz para **Síndrome Nefrogênica de Antidiurese Inapropriada (Nephrogenic Syndrome of Inappropriate Antidiuresis)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. A previsão se baseia apenas no modelo computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Analgésicos narcóticos |
| Nova Indicação Prevista | Síndrome Nefrogênica de Antidiurese Inapropriada (Nephrogenic Syndrome of Inappropriate Antidiuresis) |
| Pontuação de Previsão TxGNN | 0,9946 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 11 de 11) |
| Número de Registros | 11 (ativos: 11) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a fentanila é um agonista do receptor mu-opioide, com eficácia estabelecida como analgésico e anestésico opioide.

Do ponto de vista mecanístico, **não há um elo crível** que sustente esta previsão. A síndrome nefrogênica de antidiurese inapropriada é causada por mutações de ganho de função no receptor V2 da vasopressina (AVPR2), que atuam no rim independentemente da vasopressina circulante. Os opioides podem influenciar a liberação de vasopressina e o manejo de água pelo organismo, mas isso tenderia a **provocar** antidiurese, e não a tratá-la. Não se espera que a fentanila corrija o defeito do receptor.

A pontuação alta do TxGNN (0,9946) é apenas uma previsão computacional, sem respaldo em evidências clínicas ou da literatura, e pode refletir artefatos da rede de conhecimento, e não biologia real.

*Previsão secundária:* o modelo também previu a **síndrome de Tourette** (pontuação 0,9905), igualmente sem ensaios ou publicações. Embora se especule sobre a ligação entre o sistema opioide endógeno e a modulação de tiques via circuitos dopaminérgicos dos núcleos da base, isso é hipotético para a fentanila. O risco de abuso e dependência, a depressão respiratória e uma população crônica, frequentemente pediátrica, tornam o fármaco um candidato inadequado. Esta previsão também foi classificada como L5 e **Hold**.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

Todos os 11 registros encontram-se **válidos**. Os cinco principais:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 100410166 | Citrato de Fentanila | Não informada | Analgésicos narcóticos |
| Registro 104970264 | Unifental | Não informada | Analgésicos narcóticos |
| Registro 103700587 | Anesfent | Não informada | Analgésicos narcóticos |
| Registro 155730048 | Fentora | Não informada | Analgésicos narcóticos |
| Registro 102980588 | Fentanest Bolsa | Não informada | Anestésicos opioides |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não é texto de bula)**: o grafo de conhecimento do TxGNN associa o fármaco às seguintes condições: hipertensão, hipotensão ortostática, síndrome do QT longo e *torsades de pointes*, insuficiência e doença hepática, doença renal, doença pulmonar obstrutiva crônica, asma, pancreatite, doença da vesícula biliar, doença inflamatória intestinal, hiperplasia prostática benigna, deficiência de potássio, ansiedade e transtornos neuróticos, atrofia de múltiplos sistemas, síndrome de taquicardia postural ortostática, doenças dos núcleos da base, distonia focal da mão, blefaroespasmo e abuso/dependência de substâncias.
- **Interações Medicamentosas**: foram identificadas 100 interações. As principais de gravidade **maior** são: alvimopano, aprepitanto, bupropiona, claritromicina, clotrimazol, dexametasona, dexfenfluramina, dolasetrona, fenfluramina, granisetrona e lorcasserina. De gravidade **moderada**: atropina, cimetidina, clidínio, diciclomina, dronabinol, eluxadolina, fenilbutirato de glicerol, glicopirrônio e hiosciamina.

Consulte a bula para as advertências e contraindicações oficiais.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem publicações, e o mecanismo conhecido da fentanila (tendência a causar antidiurese) vai contra a fisiopatologia da doença. Somam-se a isso o alto perfil de risco, a carga de interações medicamentosas e a ausência de registros vigentes no Brasil.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação (consulta à API do DrugBank)
- Advertências e contraindicações da bula na ANVISA (lacuna bloqueante para a triagem de segurança)
- Evidências pré-clínicas independentes que demonstrem uma ligação biológica plausível com a nova indicação
- Avaliação da compatibilidade de vias de administração e formas farmacêuticas, hoje não informadas
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

