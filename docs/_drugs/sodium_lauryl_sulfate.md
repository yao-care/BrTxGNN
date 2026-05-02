---
layout: default
title: Sodium Lauryl Sulfate
parent: 僅模型預測 (L5)
nav_order: 445
evidence_level: L5
indication_count: 10
---

# Sodium Lauryl Sulfate
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

# Lauril Sulfato de Sódio (SLS): De Excipiente Tensoativo à Agenesia da Valva Tricúspide

## Resumo em Uma Frase

Lauril Sulfato de Sódio (SLS) é um tensoativo aniônico amplamente utilizado como excipiente farmacêutico e agente de limpeza em produtos de higiene pessoal, sem indicação terapêutica aprovada registrada.
O modelo TxGNN prevê que pode ser eficaz para **Agenesia da Valva Tricúspide (Tricuspid Valve Agenesis)** como principal candidato, porém com pontuação mínima de **50%** — correspondente ao limite inferior do modelo — **sem nenhum ensaio clínico** e **sem publicações** que apoiem esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Nenhuma indicação terapêutica aprovada (uso como excipiente farmacêutico e agente tensoativo) |
| Nova Indicação Prevista | Agenesia da Valva Tricúspide (Tricuspid Valve Agenesis) |
| Pontuação de Previsão TxGNN | 50,00% (limite inferior absoluto do modelo) |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Lauril Sulfato de Sódio é um tensoativo aniônico sem mecanismo de ação terapêutico documentado. Seu uso é predominantemente como excipiente em formulações farmacêuticas (agente umectante, emulsificante e solubilizante), em dentifrícios, xampus e produtos de higiene — não como agente ativo com finalidade clínica definida. Os dados de MOA estão ausentes neste Evidence Pack, o que inviabiliza qualquer análise de relacionamento mecanístico formal.

A agenesia da valva tricúspide é uma malformação cardíaca congênita causada por falha no desenvolvimento embrionário do coração direito. Trata-se de um defeito estrutural cuja origem envolve distúrbios na morfogênese valvular durante a embriogênese — um processo mediado por vias moleculares complexas (como sinalização Notch, BMP e GATA) completamente alheias à ação de surfactantes. O SLS não possui qualquer registro na literatura de modulação dessas vias de desenvolvimento.

A pontuação de 0,5 (50%) representa o **limite inferior do modelo TxGNN**, sinalizando ausência de sinal preditivo real. A interpretação mais provável é que este fármaco simplesmente não foi mapeado de forma significativa no grafo de conhecimento, resultando em predições de baixíssima confiança para múltiplas indicações sem relação biológica coerente. Esta análise abrange as 10 indicações previstas, todas com pontuação idêntica de 50% e classificação L5.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada à indicação prevista de maior ranking (Agenesia da Valva Tricúspide).

> **Nota de Análise**: Para a 7ª indicação prevista (Necrólise Epidérmica Tóxica — TEN), foram recuperadas 4 publicações, porém **nenhuma** apoia o uso de SLS como tratamento. Três delas (PMID 1262065, 129438, 4271807) tratam de genética e purificação de toxinas estafilocócicas. A quarta (PMID 6499417) utiliza o próprio SLS como **modelo experimental de irritante cutâneo** para testar cremes protetores de barreira — reforçando que o SLS é reconhecido como agente lesivo à pele, não como tratamento.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> **Alerta de Segurança Baseado em Análise de Indicações**: A análise das rationale de reposicionamento identificou dois contextos em que o SLS pode representar **risco de dano adicional**, configurando potencial contraindicação — não indicação terapêutica:
>
> - **Necrólise Epidérmica Tóxica (TEN)**: O SLS é reconhecido como irritante de pele e mucosas. Em pacientes com TEN, onde a barreira cutânea está gravemente comprometida, sua aplicação pode agravar a lesão epitelial.
> - **Síndrome do Intestino Curto Secundária**: O SLS é documentado como agente lesivo à mucosa intestinal. Em pacientes com intestino curto, cuja mucosa é vulnerável, o uso pode aprofundar o dano à barreira entérica.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Todas as 10 indicações previstas pelo TxGNN apresentam pontuação mínima (50%), nível de evidência L5 e ausência total de ensaios clínicos ou literatura de suporte. A análise mecanística confirma que o SLS — um tensoativo sem alvo terapêutico definido — não possui plausibilidade biológica para nenhuma das indicações listadas. Em pelo menos dois casos (TEN e síndrome do intestino curto), o perfil irritante do composto indica risco de dano, tornando o reposicionamento contraindicado, não indicado.

**Para prosseguir, seria necessário:**
- Confirmar se existe algum contexto de uso terapêutico estabelecido para o SLS (ex.: espermicida, agente esclerosante, tratamento de infecções orais) e reiniciar a análise com essa indicação original como âncora
- Coletar dados de MOA via DrugBank API para verificar se há alvos moleculares mapeáveis
- Investigar a causa da pontuação mínima uniforme no TxGNN: o mais provável é que o SLS não tenha representação adequada no grafo de conhecimento do modelo, invalidando as predições atuais
- Avaliar se o DrugBank ID DB00815 corresponde corretamente ao SLS na versão do grafo utilizada
---

