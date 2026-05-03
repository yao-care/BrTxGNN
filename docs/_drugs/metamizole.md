---
layout: default
title: Metamizole
parent: 僅模型預測 (L5)
nav_order: 343
evidence_level: L5
indication_count: 10
---

# Metamizole
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

A skill é sobre pipeline técnico (treino, validação, deploy) — não se aplica à geração de relatório. Sigo diretamente o sistema de prompt especializado.

---

# Metamizole: De analgésico e antipirético para artrite reumatoide

## Resumo em Uma Frase

Metamizole (dipirona) é um analgésico não opioide e antipirético amplamente utilizado em países como Alemanha, Brasil, Israel e México para controle de dor aguda e febre, porém sem registro no Brasil. O modelo TxGNN prevê que pode ser eficaz para **Artrite Reumatoide (Rheumatoid Arthritis)**, contando atualmente com **0 ensaios clínicos** e **20 publicações** na literatura que sustentam esta direção. A análise das evidências indica, entretanto, que o Metamizole atua primariamente como analgésico adjuvante na RA — sem capacidade de modificar o curso da doença —, o que justifica uma decisão de espera antes de qualquer avanço clínico.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Analgesia e antitermia — analgésico não opioide (uso reconhecido em outros países, sem registro no Brasil) |
| Nova Indicação Prevista | Artrite Reumatoide (Rheumatoid Arthritis) |
| Pontuação de Previsão TxGNN | 99.78% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Metamizole (também denominado dipirona ou dipyrone) pertence à classe das pirazolonas e atua como analgésico não opioide com propriedades antipiréticas e espasmolíticas. Não há dados detalhados de mecanismo de ação (MOA) registrados no presente Evidence Pack, mas a literatura coletada aponta que sua ação analgésica envolve inibição de COX-1 e COX-2 — reduzindo a síntese de prostaglandinas envolvidas na sinalização de dor e inflamação — além de um componente central de modulação da dor, possivelmente via sistemas endocanabinoide e NO-cGMP, ao nível medular e encefálico.

A artrite reumatoide (RA) é uma doença autoimune sistêmica que cursa com inflamação crônica das articulações, causando dor, rigidez matinal, edema e destruição progressiva da cartilagem. A lógica por trás da previsão TxGNN é plausível no plano sintomático: o Metamizole compartilha o nó de "dor-inflamação" no grafo de conhecimento com a RA, e dados reais de prescrição na Alemanha (Albrecht et al., 2021) confirmam que o fármaco é utilizado na prática clínica como analgésico adjuvante em pacientes com doenças reumáticas. Uma revisão de 1997 (Hackenthal) identificou eficácia do Metamizole em estados de dor crônica, incluindo artrite e osteoartrite.

No entanto, a previsão merece cautela interpretativa. Metamizole **não é um DMARD (Fármaco Modificador do Curso da Doença)** — não interfere nos mecanismos imunológicos subjacentes da RA, como ativação de linfócitos T, produção de TNF-α ou IL-6, ou autoanticorpos (anti-CCP, fator reumatoide). Portanto, pode controlar a dor, mas não altera a progressão da doença. A alta pontuação TxGNN (99,78%) reflete, com maior probabilidade, a proximidade topológica entre nós de analgesia e inflamação no grafo, e não uma relação de tratamento primário modificador de doença.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Metamizole em artrite reumatoide.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [33825975](https://pubmed.ncbi.nlm.nih.gov/33825975/) | 2021 | Análise Retrospectiva | Zeitschrift fur Rheumatologie | Análise de dados de sinistros alemães (2019): documenta a frequência real de prescrição de analgésicos — incluindo Metamizole — em 4 grupos de doenças reumáticas (AR, espondiloartrite axial, artrite psoriásica, LES) |
| [33635407](https://pubmed.ncbi.nlm.nih.gov/33635407/) | 2021 | Análise Retrospectiva | Zeitschrift fur Rheumatologie | Versão em alemão do mesmo estudo de sinistros; confirma o uso do Metamizole como adjuvante analgésico em pacientes com AR na prática clínica real |
| [12799814](https://pubmed.ncbi.nlm.nih.gov/12799814/) | 1997 | Revisão | Schmerz | Revisão de 32 estudos clínicos sobre paracetamol e Metamizole em síndromes de dor crônica, incluindo artrite e osteoartrite; descreve eficácia comparável dos dois agentes em dor articular |
| [6359862](https://pubmed.ncbi.nlm.nih.gov/6359862/) | 1983 | Revisão | Am J Medicine | Uso de analgésicos antipiréticos em pediatria; menciona dipirona como equivalente ao acetaminofeno em eficácia, e salicilatos como opção para artrite reumatoide juvenil — destaca risco de agranulocitose como limitação da dipirona |
| [577870](https://pubmed.ncbi.nlm.nih.gov/577870/) | 1977 | Estudo Animal | Arzneimittel-Forschung | A combinação pentosanpolissulfato + Metamizole reduziu edema de pata em rato em 40% a mais do que o polissulfato isolado, em seis modelos distintos de edema — demonstração pré-clínica do efeito antiflogístico do Metamizole |
| [18236017](https://pubmed.ncbi.nlm.nih.gov/18236017/) | 2007 | Estudo Animal | Inflammopharmacology | Comparação de NSAIDs em úlceras gástricas experimentais em ratos; dipirona apresentou potente ação analgésica com menor efeito ulcerogênico em relação ao celecoxibe — dado relevante para o perfil de segurança gastrointestinal |
| [21412604](https://pubmed.ncbi.nlm.nih.gov/21412604/) | 2011 | Revisão/Análise | Rev Bras Reumatologia | Análise de interações medicamentosas potenciais em pacientes com AR em contexto de polifarmácia; Metamizole figura entre os analgésicos com interações relevantes nesta população |
| [1650070](https://pubmed.ncbi.nlm.nih.gov/1650070/) | 1991 | Revisão | Zeitschrift fur Rheumatologie | Revisão das evidências para mecanismo analgésico central dos AINEs em nível espinal e encefálico; fundamenta a ação antinociceptiva central do Metamizole, além do bloqueio periférico de prostaglandinas |
| [2041854](https://pubmed.ncbi.nlm.nih.gov/2041854/) | 1991 | Relato de Caso | Postgraduate Medical Journal | Síndrome de Lyell (necrose epidérmica tóxica) induzida por Metamizole, seguida de síndrome Sjögren-like — sinal de segurança crítico para avaliação de risco em populações com doenças autoimunes como a RA |
| [18679134](https://pubmed.ncbi.nlm.nih.gov/18679134/) | 2008 | Estudo Comparativo | J Clinical Rheumatology | Comparação da frequência de alergias medicamentosas em LES vs AR; oferece contexto sobre o perfil de reações de hipersensibilidade nessa população, com potencial sobreposição com alergias a analgésicos como Metamizole |

---

## Informações de Comercialização no Brasil

Metamizole não possui nenhum registro ativo na ANVISA e não está comercialmente disponível no Brasil. Não há licenças a listar.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A literatura confirma o uso do Metamizole como analgésico adjuvante em doenças reumáticas na prática clínica real, mas não há ensaios clínicos que avaliem sua eficácia primária em artrite reumatoide, e as evidências disponíveis (L4) não suportam uma relação de modificação da doença — apenas alívio sintomático de dor.

**Para prosseguir, é necessário:**
- Obter o mecanismo de ação completo (MOA) via DrugBank API — lacuna classificada como alta prioridade no Evidence Pack
- Coletar dados completos de segurança (bula ANVISA/EMA/FDA) para preenchimento das advertências, contraindicações e interações medicamentosas atualmente indisponíveis
- Definir com precisão a hipótese terapêutica: **alívio sintomático de dor em RA** (como adjuvante) versus modificação da doença (inviável sem redesenho)
- Iniciar processo de avaliação regulatória para viabilidade de registro na ANVISA, que atualmente não conta com nenhum precedente de licença para Metamizole no Brasil
- Considerar priorizar a indicação de **Transtorno de Enxaqueca (Migraine Disorder)** — ranqueada em 2º pelo TxGNN (score 99,72%), com evidência L1 (1 Phase 3 RCT completo + 19 publicações, incluindo 2 Cochrane Systematic Reviews e 3 RCTs diretos), que apresenta base científica substancialmente mais robusta para desenvolvimento clínico
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

