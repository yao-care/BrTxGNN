---
layout: default
title: Pegvaliase
parent: 僅模型預測 (L5)
nav_order: 390
evidence_level: L5
indication_count: 10
---

# Pegvaliase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Using `txgnn-pipeline` to orient context, and now proceeding to generate the drug repurposing evaluation report per the v5 prompt format.

---

# Pegvaliase: Da Fenilcetonúria à Retinopatia Diabética

## Resumo em Uma Frase

Pegvaliase (Palynziq) é uma enzima terapêutica de substituição originalmente indicada para o tratamento da **Fenilcetonúria (PKU)** em adultos, atuando na degradação do excesso de fenilalanina no sangue.
O modelo TxGNN prevê que pode ser eficaz para a **Retinopatia Diabética (Diabetic Retinopathy)**, com pontuação de 99,17% — porém **sem nenhum ensaio clínico** e **sem publicações** apoiando esta direção.
A conexão mecanística é considerada indireta e fraca, e a recomendação atual é de espera até que surjam evidências concretas.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Fenilcetonúria (PKU) em adultos |
| Nova Indicação Prevista | Retinopatia Diabética (Diabetic Retinopathy) |
| Pontuação de Previsão TxGNN | 99,17% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Pegvaliase é uma fenilalanina amônia liase (PAL) recombinante derivada de *Anabaena variabilis*, que converte a fenilalanina (Phe) em amônia e ácido trans-cinâmico. Em pacientes com PKU — nos quais a enzima fenilalanina hidroxilase (PAH) está ausente ou deficiente — o acúmulo de Phe causa neurotoxicidade progressiva. Ao reduzir os níveis plasmáticos de Phe, Pegvaliase restaura a homeostase metabólica e atenua o comprometimento neurológico crônico.

A hipótese de aplicação na retinopatia diabética baseia-se em um mecanismo indireto e biologicamente frágil: em pacientes com PKU, o excesso de Phe compete com a tirosina (Tyr), reduzindo a síntese de dopamina e potencialmente prejudicando a neuromodulação da retina. Esse raciocínio é válido no contexto da PKU, mas a retinopatia diabética tem patogênese totalmente distinta — hiperglicemia crônica, ativação da via do poliol, PKC, acúmulo de produtos finais de glicação avançada (AGEs) e superexpressão de VEGF —, todos mecanismos independentes do metabolismo da fenilalanina.

Em pacientes diabéticos com níveis normais de Phe, não há embasamento teórico para que a redução de Phe por Pegvaliase produza efeito sobre a vasculopatia retiniana diabética. O alto score TxGNN (99,17%) reflete proximidade no grafo de conhecimento farmacológico, mas não implica relevância biológica direta. Esta previsão deve ser interpretada com cautela significativa.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Há **1 registro** de Pegvaliase no Brasil. Os detalhes de número de registro, nome comercial, forma farmacêutica e texto de indicação aprovada não estão disponíveis neste pacote de evidências. Consulte o portal da ANVISA para informações completas do registro.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Apesar do score elevado do TxGNN (99,17%), a análise mecanística revela uma conexão indireta e biologicamente implausível entre o mecanismo de ação de Pegvaliase — redução de fenilalanina em pacientes com PKU — e a patogênese da retinopatia diabética, que é inteiramente conduzida pela hiperglicemia. A ausência total de ensaios clínicos e publicações científicas configura nível de evidência L5, o mais baixo possível.

**Para prosseguir, é necessário:**
- Dados de mecanismo de ação (MOA) completos via DrugBank API
- Advertências, contraindicações e perfil de segurança da bula registrada na ANVISA
- Hipótese mecanística plausível que conecte a redução de Phe à patologia vascular retiniana em pacientes diabéticos (não-PKU)
- Estudos pré-clínicos (*in vitro* / *in vivo*) demonstrando efeito de Pegvaliase em modelos de retinopatia diabética antes de qualquer consideração de ensaio clínico
---

