---
layout: default
title: Phenylbutazone
parent: 僅模型預測 (L5)
nav_order: 395
evidence_level: L5
indication_count: 10
---

# Phenylbutazone
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

Using `txgnn-pipeline` como contexto para geração de relatório de reposicionamento.

---

# Fenilbutazona: De anti-inflamatório clássico à artrite reumatoide

## Resumo em Uma Frase

Fenilbutazona (Phenylbutazone) é um anti-inflamatório não esteroidal (AINE) da classe pirazolínica, historicamente utilizado no tratamento de doenças reumáticas, mas atualmente sem registro no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **Artrite Reumatoide (Rheumatoid Arthritis)**, com pontuação de previsão de **99,82%**.
Atualmente, há **0 ensaios clínicos registrados** e **20 publicações** apoiando esta direção, com evidências clínicas históricas que remontam à década de 1950.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Sem registro no Brasil (AINE pirazolínico de uso histórico em doenças reumáticas) |
| Nova Indicação Prevista | Artrite Reumatoide (Rheumatoid Arthritis) |
| Pontuação de Previsão TxGNN | 99,82% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Fenilbutazona pertence à classe dos AINEs pirazolínicos e atua primariamente pela inibição das enzimas ciclo-oxigenase (COX-1 e COX-2), reduzindo a síntese de prostaglandinas na membrana sinovial. Essa ação resulta em diminuição do edema, da dor e da rigidez articular — mecanismo diretamente relevante para a artrite reumatoide, uma doença caracterizada por inflamação sinovial crônica mediada por prostaglandinas e citocinas pró-inflamatórias. Além disso, fenilbutazona possui propriedades uricosúricas (aumento da excreção renal de ácido úrico), o que amplia seu espectro de ação no contexto de doenças reumáticas.

A artrite reumatoide (AR) é uma doença autoimune sistêmica que compromete progressivamente as articulações sinoviais. O papel das prostaglandinas na amplificação da cascata inflamatória sinovial e na erosão cartilaginosa é bem estabelecido na literatura, tornando a inibição de COX uma estratégia terapêutica mecanisticamente racional. A previsão do TxGNN reflete essa coerência biológica: o modelo identifica fenilbutazona como candidata de alto potencial para AR com base nas relações do conhecimento de grafo — relação confirmada pela extensa produção científica histórica.

A razoabilidade desta previsão é reforçada por décadas de uso clínico documentado: ensaios clínicos com fenilbutazona em pacientes com AR foram conduzidos desde os anos 1950, incluindo estudos duplo-cegos publicados em periódicos de referência. Embora o fármaco tenha sido amplamente retirado do mercado humano em países como EUA e Reino Unido devido a efeitos adversos graves (anemia aplástica, agranulocitose, hepatotoxicidade), sua eficácia anti-inflamatória em AR é clinicamente comprovada. O desafio de reposicionamento, portanto, não é a eficácia — é a gestão do risco.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados (ClinicalTrials.gov e ICTRP consultados em 24/03/2026).

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [6345427](https://pubmed.ncbi.nlm.nih.gov/6345427/) | 1983 | Ensaio duplo-cego | Int J Tissue Reactions | 150 pacientes com AR; suxibuzone vs. fenilbutazona 300 mg/dia por 6 semanas; eficácia equivalente em rigidez, dor e força de preensão; menos eventos GI no grupo suxibuzone |
| [6884415](https://pubmed.ncbi.nlm.nih.gov/6884415/) | 1983 | Ensaio duplo-cego | Eur J Clin Pharmacol | Estudo de dose em 32 pacientes com AR; dose ótima identificada: 300 mg/dia; doses superiores não conferem benefício adicional; 7/32 desenvolveram reações adversas |
| [4903691](https://pubmed.ncbi.nlm.nih.gov/4903691/) | 1969 | Ensaio comparativo | Can Med Assoc J | Monobutazona vs. fenilbutazona em pacientes ambulatoriais com AR; eficácia equivalente; perfil de efeitos adversos mais favorável com monobutazona |
| [788739](https://pubmed.ncbi.nlm.nih.gov/788739/) | 1976 | Estudo PK/Clínico | Br J Clin Pharmacol | Doses de 50–300 mg/dia em 7 pacientes com AR (duplo-cego, cross-over); correlação demonstrada entre concentração plasmática e resposta clínica (rigidez matinal, dor, força de preensão) |
| [913873](https://pubmed.ncbi.nlm.nih.gov/913873/) | 1977 | Estudo PK/Clínico | J Int Med Res | Doses de 50–400 mg/dia em 7 pacientes com AR; avaliação por índice articular, força de preensão e escores de dor; resposta dose-dependente documentada |
| [334476](https://pubmed.ncbi.nlm.nih.gov/334476/) | 1977 | Ensaio duplo-cego | Curr Med Res Opin | Flurbiprofeno 300 mg vs. fenilbutazona 400 mg em 12 pacientes com AR por 2 semanas; 2 pacientes do grupo fenilbutazona desenvolveram rash cutâneo |
| [13009482](https://pubmed.ncbi.nlm.nih.gov/13009482/) | 1952 | Estudo clínico | California Medicine | Avaliação de fenilbutazona e Butapyrin® em 409 pacientes com doenças reumáticas; efeito supressivo em alta proporção dos casos; eficácia confirmada independente da aminopirina |
| [786193](https://pubmed.ncbi.nlm.nih.gov/786193/) | 1976 | Revisão | Arch Intern Med | Revisão de abordagens terapêuticas para AR; fenilbutazona posicionada como referência na classe dos AINEs; destaca necessidade de programa de tratamento individualizado |
| [1145012](https://pubmed.ncbi.nlm.nih.gov/1145012/) | 1975 | Série de casos | Rheumatol Rehabil | Relato de hepatite leve em paciente com AR durante ensaio de fenilbutazona; revisão de história natural baseada em 41 casos de hepatite por fenilbutazona |
| [14302557](https://pubmed.ncbi.nlm.nih.gov/14302557/) | 1965 | Revisão | Clin Obstet Gynecol | Artrite reumatoide e gravidez; considerações sobre uso de fenilbutazona e outros AINEs em populações especiais |

---

## Informações de Comercialização no Brasil

Nenhum registro de Fenilbutazona foi localizado na ANVISA. O medicamento **não está comercializado no Brasil** (consulta realizada em 24/03/2026, resultado: 0 registros ativos).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> **Nota importante:** Fenilbutazona possui histórico documentado de toxicidade grave em humanos — incluindo anemia aplástica, agranulocitose e hepatotoxicidade — que motivou a retirada voluntária e regulatória do fármaco em diversos mercados (EUA, Reino Unido, entre outros). Esses riscos devem ser avaliados com rigor antes de qualquer consideração de reposicionamento.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Embora as evidências históricas de eficácia anti-inflamatória em artrite reumatoide sejam robustas (L3 — múltiplos ensaios comparativos e duplo-cegos publicados entre 1952 e 1983), o perfil de segurança de fenilbutazona é reconhecidamente desfavorável: eventos adversos graves como anemia aplástica e agranulocitose levaram à retirada do fármaco da maioria dos mercados humanos. Sem registro no Brasil, sem ensaios clínicos modernos e sem dados formais de segurança disponíveis neste pacote, não é possível avançar para avaliação de viabilidade clínica.

**Para prosseguir, é necessário:**
- Obter e revisar a bula completa de fenilbutazona (dados de advertências, contraindicações e interações medicamentosas estão ausentes neste pacote)
- Realizar análise formal de benefício-risco frente às alternativas modernas estabelecidas para AR (DMARDs convencionais, biológicos, JAK inibidores)
- Verificar o status regulatório global atual: fenilbutazona ainda possui registro para uso veterinário em vários países — avaliar se existe via regulatória para indicação humana no Brasil
- Investigar se há ensaios clínicos modernos planejados ou em andamento com formulações ou análogos de fenilbutazona de perfil de segurança melhorado
- Consultar profissional de farmacovigilância para avaliação do risco de aplasia medular no contexto regulatório brasileiro
---

