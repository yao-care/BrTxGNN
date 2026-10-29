---
layout: default
title: Spironolactone
parent: Apenas Predição do Modelo (L5)
nav_order: 598
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-29
description: "Spironolactone: nova indicação prevista, Hipotricose simples do couro cabeludo (hypotrichosis simplex of the s… (nível de evidência L5). Indicação original: Diuréticos simples"
monitor_inn: "SPIRONOLACTONE"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia"]
---

# Spironolactone
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

## Espironolactona: De diurético a hipotricose simples do couro cabeludo
{: .text-alpha }

## Resumo em Uma Frase

A espironolactona foi originalmente registrada no Brasil como diurético.
O modelo TxGNN prevê que pode ser eficaz para **hipotricose simples do couro cabeludo (hypotrichosis simplex of the scalp)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; a previsão se baseia apenas no modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Diuréticos simples |
| Nova Indicação Prevista | Hipotricose simples do couro cabeludo (hypotrichosis simplex of the scalp) |
| Pontuação de Previsão TxGNN | 0,9926 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 7 de 8) |
| Número de Registros | 8 (ativos: 7) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo conhecimento farmacológico geral, a espironolactona é um antagonista do receptor mineralocorticoide e também tem atividade antiandrogênica (bloqueio do receptor de androgênio e redução da síntese de androgênios). Seu efeito diurético está bem estabelecido, e ela é usada fora da bula em alopecia de padrão feminino.

A hipotricose simples do couro cabeludo, porém, é uma condição hereditária rara, geralmente associada a variantes em genes como CDSN, APCDD1 ou RPL21, e não é primariamente dependente de androgênios. A relação com a indicação original (diurético) é indireta, e a ligação mecanística é **especulativa**: baseia-se apenas na pontuação elevada do TxGNN, sem estudos que a sustentem.

Uma segunda indicação prevista, **hipotricose congênita com milia** (pontuação de 0,9904), apresenta o mesmo cenário: nível L5, sem ensaios nem literatura, e base mecanística ainda mais fraca por se tratar de distúrbio genético com origem estrutural/de desenvolvimento do folículo.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

Todos os 8 registros estão válidos; o medicamento é comercializado no Brasil, com 8 licenças válidas de 8.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 154230266 | Espironolactona | Não informada | Diuréticos simples |
| Registro nº 113430155 | Espironolactona | Não informada | Diuréticos simples |
| Registro nº 121100419 | Aldactone | Não informada | Diuréticos |
| Registro nº 100431399 | Diacqua | Não informada | Diuréticos simples |
| Registro nº 105830285 | Espironolactona | Não informada | Diuréticos simples |

(Exibidos os 5 primeiros de 8 registros.)

## Considerações de Segurança

- **Contraindicações (grafo de conhecimento TxGNN/PrimeKG, não derivadas da bula)**: doença renal, anúria, pancreatite, lúpus eritematoso sistêmico (inclusive pediátrico), deficiência de potássio, diabetes mellitus, cetoacidose diabética, hiperuricemia, gota, hiperparatireoidismo, osteíte fibrosa, coma hepático, encefalopatia hepática, icterícia neonatal, hipercalcemia, nefrocalcinose, distúrbios do metabolismo do fósforo e piureter.
- **Interações Medicamentosas** (100 interações identificadas; amostra de 20 exibida):
  - **Grave**: loperamida.
  - **Moderada**: hidrocortisona, metformina, bupropiona, triamcinolona, morfina, dexametasona, betametasona, bisacodil, budesonida, canagliflozina, óleo de rícino, dapagliflozina, dronabinol, empagliflozina, ertugliflozina, exenatida.
  - **Leve**: doxiciclina, ácido acetilsalicílico, fidaxomicina.

As advertências e contraindicações da bula não estavam disponíveis nos dados compilados; consulte a bula aprovada pela ANVISA.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão tem pontuação alta no modelo TxGNN (deep learning), mas nível de evidência L5, sem ensaios ou literatura, e com base mecanística especulativa para uma condição genética rara. O medicamento é comercializado no Brasil, com 8 licenças válidas de 8, e os dados de segurança da bula estão ausentes.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança.
- Complementar os dados do mecanismo de ação (MOA) a partir do DrugBank.
- Realizar busca sistemática de literatura e de registros de ensaios clínicos para hipotricose hereditária.
- Avaliar estudos pré-clínicos que testem se o bloqueio androgênico é relevante para as variantes genéticas envolvidas.
- Esclarecer a situação regulatória (registros cancelados) e a via de administração adequada (por exemplo, oral vs. tópica).
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

