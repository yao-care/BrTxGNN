---
layout: default
title: Atenolol
parent: Apenas Predição do Modelo (L5)
nav_order: 85
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-13
description: "Atenolol: nova indicação prevista, Infarto do miocárdio posterolateral (posterolateral myocardial infarc… (nível de evidência L5). Indicação original: Hipertensão arterial e infarto do miocárdio"
monitor_inn: "ATENOLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "chronic pulmonary heart disease"]
---

# Atenolol
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **9** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relatório de avaliação farmacêutica

</div>

# Atenolol: Da hipertensão e do infarto do miocárdio ao infarto do miocárdio posterolateral

## Resumo em Uma Frase

Atenolol é um betabloqueador cardiosseletivo (beta-1), originalmente usado no tratamento da hipertensão arterial e do infarto do miocárdio.
O modelo TxGNN prevê que pode ser eficaz para **infarto do miocárdio posterolateral (posterolateral myocardial infarction)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção específica. A previsão reflete sobretudo a proximidade com uma indicação já existente (infarto do miocárdio), e não um sinal novo de reposicionamento.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hipertensão arterial e infarto do miocárdio (conforme as indicações do grafo de conhecimento; não há texto de indicação de registro na ANVISA) |
| Nova Indicação Prevista | Infarto do miocárdio posterolateral (posterolateral myocardial infarction) |
| Pontuação de Previsão TxGNN | 99,87% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado (segundo os dados compilados) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o atenolol é um betabloqueador beta-1 seletivo: ao reduzir a frequência cardíaca e a demanda de oxigênio do miocárdio, tem eficácia estabelecida no infarto do miocárdio e na hipertensão.

O infarto posterolateral é um subtipo anatômico do infarto do miocárdio, indicação que o atenolol já possui. Assim, a pontuação alta (0,9987) reflete principalmente a proximidade na ontologia de doenças com uma indicação existente, e não uma descoberta nova. O potencial de novidade do reposicionamento é baixo, e a plausibilidade mecanística é alta apenas por extensão da indicação já conhecida.

Outras previsões do modelo, com menor sustentação, incluem a hipertensão renovascular maligna, a hipertensão pulmonar e a cor pulmonale crônico. Nelas, a lógica mecanística é fraca ou há ressalvas de segurança (ver abaixo).

## Informações de Comercialização no Brasil

Segundo os dados compilados, não há registros de atenolol com situação de comercialização no Brasil (0 registros). Por isso, não há tabela de registros.

## Considerações de Segurança

- **Contraindicações (com base em relações do grafo de conhecimento, não em texto de bula)**: o grafo associa o atenolol a contraindicação ou cautela nas seguintes condições: bloqueio atrioventricular, asma (incluindo as formas intrínseca e alérgica), doença de Raynaud, anafilaxia, diabetes mellitus (tipos 1 e 2) e cetoacidose diabética, insuficiência hepática, anúria, lúpus eritematoso sistêmico, psoríase e parapsoríase, pancreatite, gota e hiperuricemia, hipercalcemia, nefrocalcinose, distúrbios do metabolismo do fósforo, deficiência de potássio, transtornos de ansiedade, transtorno neurótico e distimia.
- **Interações Medicamentosas**: foram identificadas 100 interações na consulta; as 20 listadas nos dados compilados são, em sua maioria, de gravidade moderada:
  - Moderadas: epinefrina, hidrocortisona, hiosciamina, bupropiona, triancinolona, morfina, acetoexamida, atropina, betametasona, budesonida e sais de cálcio (acetato, carbonato, citrato, glubionato, gluconato, lactato e fosfato).
  - Leves: ácido acetilsalicílico, hidróxido de alumínio e attapulgita.
- **Cautelas específicas das previsões**: na hipertensão renovascular, betabloqueadores exigem cautela em estenose bilateral de artéria renal; na hipertensão pulmonar e em doença pulmonar crônica, há risco de piora de estados hipóxicos ou broncoespasmo.

As advertências e contraindicações da bula brasileira não estavam disponíveis; consulte a bula para informações de segurança completas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A indicação prevista (infarto posterolateral) é um subtipo de uma indicação já existente, sem ensaios clínicos nem literatura específica; o nível de evidência é L5, e a alta pontuação reflete proximidade na ontologia, não novidade terapêutica.
- Não há registro do atenolol no Brasil segundo os dados compilados, e a bula brasileira não foi analisada, o que impede a triagem de segurança.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações) e confirmar a situação regulatória do atenolol no Brasil.
- Completar os dados de mecanismo de ação a partir do DrugBank.
- Verificar se a indicação já está coberta pela aprovação de infarto do miocárdio, o que tornaria desnecessário tratá-la como reposicionamento.
- Para a previsão com alguma literatura de apoio (infarto posteroinferior), há apenas um estudo cruzado pequeno de 1985 (atenolol vs. diltiazem); seria necessária evidência mais robusta e específica ao subtipo.
- Para as demais previsões (hipertensão renovascular maligna, hipertensão pulmonar, cor pulmonale crônico), a literatura é indireta, pré-clínica ou fora do tema, e não sustenta recomendação.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

