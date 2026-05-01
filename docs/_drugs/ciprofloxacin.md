---
layout: default
title: Ciprofloxacin
parent: 僅模型預測 (L5)
nav_order: 187
evidence_level: L5
indication_count: 10
---

# Ciprofloxacin
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

O skill TxGNN Pipeline é de escopo geral. O sistema de prompt já contém todas as instruções detalhadas de formatação do relatório. Vou agora gerar o relatório completo a partir do Evidence Pack.

---

# Ciprofloxacin: De infecções bacterianas à esclerodermia difusa

## Resumo em Uma Frase

Ciprofloxacin é um antibiótico fluoroquinolônico de amplo espectro, amplamente utilizado no tratamento de infecções bacterianas graves do trato urinário, respiratório, gastrointestinal e de outros sítios.
O modelo TxGNN prevê que pode ser eficaz para **Esclerodermia Difusa (Diffuse Scleroderma)**, com pontuação de **99,87%**.
Atualmente, **não há ensaios clínicos nem publicações** que suportem diretamente esta direção de reposicionamento — a previsão é considerada provável falso positivo do grafo de conhecimento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções bacterianas (trato urinário, respiratório, gastrointestinal, pele, ossos e articulações) |
| Nova Indicação Prevista | Esclerodermia Difusa (Diffuse Scleroderma) |
| Pontuação de Previsão TxGNN | 99,87% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste pacote. Por conhecimento geral da farmacologia, o Ciprofloxacin pertence à classe das fluoroquinolonas e atua inibindo as enzimas DNA girase (Topoisomerase II) e Topoisomerase IV bacterianas, bloqueando a replicação e a transcrição do DNA de bactérias gram-negativas e gram-positivas. Sua eficácia no tratamento de infecções bacterianas é amplamente estabelecida.

A conexão teórica com a esclerodermia difusa baseia-se na hipótese de **gatilho infeccioso**: existe literatura esparsa associando agentes como *Borrelia burgdorferi* e *Helicobacter pylori* como possíveis desencadeadores da resposta autoimune e fibrótica na esclerose sistêmica. Sob essa lógica, a eliminação de cargas infecciosas por um antibiótico de amplo espectro poderia, em tese, atenuar o processo.

No entanto, esta ligação é excessivamente indireta. A análise do modelo indica que a alta pontuação do TxGNN provavelmente reflete uma **conexão distante entre nós de infecção e imunidade no grafo de conhecimento**, sem suporte mecanístico direto para a esclerodermia. A ausência completa de evidências clínicas e pré-clínicas, aliada ao perfil de doença autoimune fibrótica com mecanismos independentes de infecção ativa, posiciona esta previsão como **potencial falso positivo do modelo**.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

O Ciprofloxacin possui **20 registros** na ANVISA com situação **Comercializado**. Os detalhes individuais de cada registro (nome comercial, forma farmacêutica, indicação aprovada) não estão disponíveis nos dados deste pacote de evidências e devem ser consultados diretamente no portal da ANVISA.

---

## Considerações de Segurança

> ⚠️ **Alerta de Segurança Identificado na Análise de Reposicionamento**: O Ciprofloxacin possui **Black Box Warning do FDA** (em vigor desde 2013) para **neuropatia periférica grave e potencialmente irreversível**. Esta informação, identificada na análise das candidatas deste pacote, é clinicamente relevante para qualquer avaliação de novas indicações. Adicionalmente, há relatos de pancreatite medicamentosa (hiperamylasemia) como reação adversa ao Ciprofloxacin — um sinal negativo que deve ser considerado em qualquer indicação que envolva o pâncreas.

Para as demais advertências e contraindicações formais, consulte a bula registrada na ANVISA.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não existe nenhuma evidência clínica ou pré-clínica que sustente o uso de Ciprofloxacin para esclerodermia difusa. A previsão elevada do TxGNN (99,87%) provavelmente representa uma conexão indireta no grafo de conhecimento entre nós de infecção e imunidade, sem correspondência biológica direta para esta indicação. A recomendação é não avançar sem evidência mínima de plausibilidade.

**Para prosseguir, seria necessário:**
- Estudos pré-clínicos demonstrando atividade anti-fibrótica ou imunomoduladora do Ciprofloxacin em modelos de esclerodermia
- Confirmação laboratorial de agentes infecciosos (ex.: *Borrelia*, *H. pylori*) como gatilho causal em subgrupos específicos de pacientes com esclerodermia difusa
- Dados completos de MOA (mecanismo de ação) via DrugBank API para análise formal de plausibilidade mecanística
- Dados de segurança completos (bula ANVISA, advertências formais) antes de qualquer avaliação de risco-benefício
---

