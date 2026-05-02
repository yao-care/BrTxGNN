---
layout: default
title: Tolterodine
parent: 僅模型預測 (L5)
nav_order: 489
evidence_level: L5
indication_count: 10
---

# Tolterodine
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

O skill confirma o contexto de pipeline TxGNN sem alterar o formato de relatório. Prossigo com a geração do relatório completo conforme o Evidence Pack fornecido.

---

# Tolterodine: Da Bexiga Hiperativa à Bexiga de Baixa Complacência

## Resumo em Uma Frase

Tolterodine é um antagonista dos receptores muscarínicos M2/M3, amplamente utilizado no tratamento da bexiga hiperativa (OAB), atuando diretamente na redução das contrações involuntárias do músculo detrusor.
O modelo TxGNN prevê que pode ser eficaz para **Bexiga de Baixa Complacência (Low Compliance Bladder)**, condição em que a capacidade de acomodação vesical está comprometida — fisiopatologicamente sobreponível à OAB neurogênica.
Atualmente, há **1 ensaio clínico** e **9 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Bexiga hiperativa (OAB) — uso clínico estabelecido internacionalmente; sem registro no Brasil |
| Nova Indicação Prevista | Bexiga de Baixa Complacência (Low Compliance Bladder) |
| Pontuação de Previsão TxGNN | 96,31% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✗ Não registrado no Brasil |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Tolterodine é um antagonista competitivo dos receptores muscarínicos M2 e M3 presentes no músculo detrusor da bexiga. Ao bloquear esses receptores, interrompe a ativação da via Gq/11-PKC, que medeia as contrações involuntárias do detrusor. O resultado funcional é a redução da pressão intravesical durante a fase de enchimento, o que melhora diretamente a relação ΔV/ΔP — a medida clínica central da complacência vesical.

A bexiga de baixa complacência em contexto neurogênico (como nas lesões medulares e na espinha bífida) compartilha a mesma fisiopatologia da bexiga hiperativa: hiperatividade do detrusor com contrações involuntárias que impedem o adequado acomodamento de volume. Nesse sentido, a indicação original (OAB) e a nova indicação prevista (baixa complacência vesical neurogênica) não são entidades biologicamente distintas — representam manifestações de um mesmo espectro de disfunção do detrusor. Watanabe et al. (2010) já avaliaram diretamente a Tolterodine de liberação prolongada em bexiga de baixa complacência, utilizando parâmetros urodinâmicos como desfecho primário.

A força da conexão mecanística é classificada como **direta (Classe I)**: o mesmo alvo molecular (M2/M3) e a mesma via farmacológica que fundamentam o uso na OAB são igualmente relevantes para a correção da baixa complacência vesical neurogênica. Trata-se de uma das previsões de reposicionamento com maior coerência biológica no conjunto avaliado.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT05745584](https://clinicaltrials.gov/study/NCT05745584) | N/A | Desconhecido | 15 | Comparação prospectiva pareada entre Mirabegron e anticolinérgicos (incluindo Tolterodine) em pacientes com bexiga neurogênica de baixa complacência; avalia complacência vesical como desfecho primário. Indica reconhecimento clínico da classe anticolinérgica para esta indicação, embora o status do ensaio seja incerto e o tamanho amostral seja muito pequeno. |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [20969642](https://pubmed.ncbi.nlm.nih.gov/20969642/) | 2010 | Estudo Clínico Prospectivo | Int J Urology | Tolterodine ER 4 mg/dia avaliada por parâmetros urodinâmicos especificamente em bexiga de baixa complacência e/ou hiperatividade neurogênica do detrusor — o estudo mais diretamente relevante para a indicação prevista |
| [26676394](https://pubmed.ncbi.nlm.nih.gov/26676394/) | 2011 | Crossover RCT (piloto) | Lower Urinary Tract Symptoms | Comparação cruzada entre oxibutinina e Tolterodine em pacientes com bexiga neurogênica por espinha bífida; demonstra eficácia anticolinérgica da Tolterodine em população neurológica diretamente relacionada |
| [16465186](https://pubmed.ncbi.nlm.nih.gov/16465186/) | 2006 | Revisão Mecanística | Br J Pharmacology | Base farmacológica dos receptores M2/M3 como alvo terapêutico da bexiga; fundamenta o mecanismo de ação da Tolterodine na complacência vesical |
| [26149965](https://pubmed.ncbi.nlm.nih.gov/26149965/) | 2015 | Revisão Clínica | Current Urology Reports | Tolterodine como padrão-ouro do tratamento antimuscarínico dos sintomas de armazenamento do trato urinário inferior em homens |
| [25656013](https://pubmed.ncbi.nlm.nih.gov/25656013/) | 2015 | Estudo Clínico Retrospectivo | Acta Urologica Japonica | Eficácia do Mirabegron adicionado a anticolinérgicos em bexiga neurogênica resistente; inclui especificamente pacientes com baixa complacência (<10 ml/cmH₂O), relevante para a indicação prevista |
| [17594185](https://pubmed.ncbi.nlm.nih.gov/17594185/) | 2007 | Revisão | Expert Opinion Investig Drugs | Panorama dos tratamentos da bexiga hiperativa em fases iniciais de desenvolvimento; contextualiza a posição da Tolterodine na classe anticolinérgica |
| [15978301](https://pubmed.ncbi.nlm.nih.gov/15978301/) | 2005 | RCT (Tróspium) | Clinical Therapeutics | Ensaio clínico com cloreto de tróspium para bexiga hiperativa com incontinência de urgência; referência comparativa para o espectro farmacológico anticolinérgico na indicação |
| [24703195](https://pubmed.ncbi.nlm.nih.gov/24703195/) | 2014 | RCT Phase III (Mirabegron) | Int J Clinical Practice | Segurança e tolerabilidade de Mirabegron em OAB em 3 ensaios de 12 semanas e 1 ensaio de 1 ano; contexto da alternativa β3-agonista à classe anticolinérgica |
| [32590783](https://pubmed.ncbi.nlm.nih.gov/32590783/) | 2020 | Relato de Caso | Medicine | Baixa complacência vesical secundária a malacoplasia com cistite xantogranulomatosa; ilustra as bases fisiopatológicas e o espectro clínico da indicação prevista |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
A previsão TxGNN é biologicamente coerente com conexão mecanística direta (Classe I) — o mesmo alvo M2/M3 que fundamenta o uso na OAB é relevante para a baixa complacência vesical neurogênica. Existem estudos clínicos prospectivos e um crossover RCT piloto avaliando Tolterodine especificamente nesta população, o que confere suporte de nível L3. O maior obstáculo para o avanço no Brasil é a ausência total de registro na ANVISA e a falta de dados de segurança documentados.

**Para prosseguir, é necessário:**
- **Regulatório**: Iniciar processo de registro na ANVISA (atualmente sem nenhum registro no Brasil)
- **Segurança**: Levantar advertências e contraindicações oficiais da bula internacional (dados ausentes neste pacote)
- **Evidência clínica**: Mapear ou conduzir estudo Phase 2 controlado em pacientes com baixa complacência vesical neurogênica com desfecho urodinâmico (complacência ΔV/ΔP, pressão de enchimento)
- **Interações**: Avaliar DDI relevantes para a população-alvo típica (pacientes com lesão medular, espinha bífida, em uso de múltiplos fármacos)
- **Monitoramento**: Definir protocolo de acompanhamento urológico (cistometria seriada) para avaliar resposta terapêutica e segurança renal a longo prazo
---

