---
layout: default
title: Ramipril
parent: 僅模型預測 (L5)
nav_order: 423
evidence_level: L5
indication_count: 10
---

# Ramipril
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

Usando o skill `txgnn-pipeline` como contexto. Agora vou gerar o relatório completo com base no Evidence Pack fornecido para o Ramipril.

---

# Ramipril: Da hipertensão arterial à hipertensão pulmonar por doença pulmonar e/ou hipóxia

## Resumo em Uma Frase

Ramipril é um inibidor da enzima conversora de angiotensina (IECA), amplamente utilizado no tratamento de hipertensão arterial, insuficiência cardíaca e redução de risco cardiovascular.
O modelo TxGNN prevê que pode ser eficaz para **Hipertensão Pulmonar por Doença Pulmonar e/ou Hipóxia (pulmonary hypertension owing to lung disease and/or hypoxia)**,
atualmente com **0 ensaios clínicos** e **20 publicações** identificadas — contudo, toda a literatura levantada aborda mecanismos gerais de hipóxia sem relação direta com o uso de ramipril nesta indicação específica.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hipertensão arterial, insuficiência cardíaca, proteção cardiovascular |
| Nova Indicação Prevista | Hipertensão Pulmonar por Doença Pulmonar e/ou Hipóxia |
| Pontuação de Previsão TxGNN | 99,93% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Ramipril é um IECA que bloqueia a conversão de angiotensina I em angiotensina II (Ang II) pela enzima conversora de angiotensina. Ao reduzir os níveis de Ang II, promove vasodilatação sistêmica e pulmonar, diminui a resistência vascular e atenua o processo de remodelamento da parede vascular. Um dado anatomofisiológico relevante é que o leito vascular pulmonar expressa de forma particularmente elevada a ECA, o que coloca os IECAs em posição teórica para interferir na vasoconstrição pulmonar e no remodelamento vascular característicos da hipertensão pulmonar (HP) do Grupo 3 (OMS).

A relação entre a indicação original e a nova indicação reside no eixo SRAA (sistema renina-angiotensina-aldosterona). Tanto na hipertensão sistêmica quanto na HP por doença pulmonar crônica, há ativação de Ang II mediando vasoconstrição e fibrose vascular — portanto, a base mecanística da previsão é biologicamente plausível.

Porém, é necessário destacar uma limitação crítica: as 20 publicações identificadas pelo pipeline de evidências são artigos de revisão sobre vias gerais de hipóxia (envelhecimento cerebral, câncer, altitude, esclerose múltipla), sem nenhuma relação direta com o uso de ramipril nesta condição. O próprio racional de reposicionamento classifica esta literatura como "falso positivo por co-ocorrência de palavras-chave". Na prática clínica atual, IECAs não integram os algoritmos de tratamento recomendados para HP do Grupo 3.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

> ⚠️ **Nota de qualidade**: As 20 publicações identificadas são artigos de revisão sobre mecanismos gerais de hipóxia. Nenhuma avalia diretamente ramipril em hipertensão pulmonar por doença pulmonar e/ou hipóxia. A listagem abaixo é apresentada para transparência do processo de busca.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Research Reviews | Hipóxia e envelhecimento cerebral: neuroproteção vs. neurodegeneração em altitude e doenças pulmonares |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metabolic Brain Disease | Déficit cognitivo por hipóxia aguda e crônica: evidências clínicas e mecanismos moleculares |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Review | Redox Biology | Hipóxia na esclerose múltipla: inflamação, disfunção vascular e progressão da doença |
| [31961750](https://pubmed.ncbi.nlm.nih.gov/31961750/) | 2020 | Review | Annual Review of Immunology | Hipóxia e imunidade inata: papel do HIF na inflamação fisiológica e patológica |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clinical Oncology | Modificação terapêutica da hipóxia em tumores sólidos: resistência à radioterapia |
| [27423661](https://pubmed.ncbi.nlm.nih.gov/27423661/) | 2016 | Review | Cell and Tissue Research | Hipóxia no reparo tecidual e fibrose: papel do HIF-1 na regeneração vascular |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | Journal of Cellular Biochemistry | Controle biológico mediado por hipóxia: crescimento, metabolismo e angiogênese |
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respiratory Care Clinics | Mecanismos de hipoxemia: hipoventilação, mismatch V/Q, shunt direita-esquerda |
| [36100192](https://pubmed.ncbi.nlm.nih.gov/36100192/) | 2022 | Review | Journal of Controlled Release | Nanomedicina baseada em hipóxia tumoral para terapia do câncer |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Review | Rev Med IMSS | Hipóxia hipobarica em altitude: aclimatação morfofisiológica em populações de altitude |

---

## Informações de Comercialização no Brasil

O ramipril possui **20 registros ativos** no Brasil (ANVISA). Os detalhes individuais dos registros — nome comercial, forma farmacêutica e indicação aprovada — não estão disponíveis neste Evidence Pack (campos em branco na fonte TFDA/ANVISA consultada). Recomenda-se consulta direta ao [portal ANVISA](https://consultas.anvisa.gov.br/) para verificação das indicações aprovadas constantes nas bulas registradas.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> As informações de advertências, contraindicações e interações medicamentosas não estão disponíveis neste Evidence Pack (itens DG001 e DG002 pendentes de remediação via download de bula ANVISA e consulta à API DrugBank).

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A pontuação TxGNN de 99,93% provavelmente reflete co-ocorrência topológica no grafo de conhecimento (nós compartilhados entre SRAA e vias de hipóxia), e não uma associação clínica estabelecida. Não há nenhum ensaio clínico registrado avaliando ramipril especificamente em HP do Grupo 3, e as 20 publicações identificadas são artigos de revisão sobre hipóxia geral — o próprio racional de reposicionamento classifica este conjunto como "falso positivo por co-ocorrência de palavras-chave". Na prática clínica atual, IECAs não são agentes recomendados para HP por doença pulmonar e/ou hipóxia.

**Para prosseguir, é necessário:**
- Realizar busca bibliográfica dirigida especificamente para "ramipril OR ACEI AND pulmonary hypertension Group 3" com filtro de relevância clínica
- Sanar DG001: baixar e analisar bula ANVISA (PDF) para advertências, contraindicações e precauções de uso
- Sanar DG002: consultar DrugBank API para obter MOA detalhado e categorias do fármaco
- Avaliar se o mecanismo vasodilatador pulmonar do ramipril justifica estudo em modelos pré-clínicos de HP-hipóxia (seria o ponto de entrada para L4 → L3)
- Verificar potenciais riscos de segurança em pacientes com doença pulmonar crônica avançada (hipotensão, tosse por IECA, angioedema)
---

