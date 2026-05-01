---
layout: default
title: Dienogest
parent: 僅模型預測 (L5)
nav_order: 221
evidence_level: L5
indication_count: 10
---

# Dienogest
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

---

# Dienogest: Da endometriose à amenorreia

## Resumo em Uma Frase

Dienogest é um progestágeno sintético de 4ª geração aprovado no Brasil para o tratamento da endometriose, com alta seletividade pelo receptor de progesterona e mínima atividade androgênica.
O modelo TxGNN prevê que pode ser eficaz para **Amenorreia (Amenorrhea)**, com **4 ensaios clínicos** e **6 publicações** identificadas nesta direção.
Contudo, a análise mecanística indica que esta previsão é provavelmente um **falso positivo**: a amenorreia é um efeito adverso bem documentado do Dienogest (ocorrência em ~20–30% das pacientes), e não uma condição que o fármaco se propõe a tratar.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Endometriose (inferida a partir do contexto clínico; dados de bula não disponíveis neste pacote) |
| Nova Indicação Prevista | Amenorreia (Amenorrhea) |
| Pontuação de Previsão TxGNN | 99.71% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste pacote de evidências (gap de dados classificado como High). Com base nas informações consolidadas na literatura, Dienogest é um progestágeno de 4ª geração que atua inibindo fortemente o pico de secreção de LH, suprimindo a ovulação e induzindo um ambiente hipestrogênico local. Esse mecanismo reduz a proliferação do tecido endometrial ectópico, sendo a base de sua aprovação para o tratamento da endometriose em múltiplos países, incluindo o Brasil.

Como consequência direta desse mecanismo de supressão do eixo hipotálamo-hipófise-ovário (HPO), a amenorreia ocorre em aproximadamente 20–30% das pacientes em uso de Dienogest — efeito documentado como adverso e confirmado pela revisão sistemática com meta-análise (PMID 39090694). O estudo farmacodinâmico mais recente (PMID 41329046, 2026) reforça que a indução de amenorreia e hipoestrogenismo é um objetivo farmacológico esperado no tratamento da endometriose.

A alta pontuação TxGNN provavelmente deriva da associação grafo-farmacológica entre Dienogest e a regulação do ciclo menstrual, mas a **direção causal é invertida**: o fármaco **provoca** amenorreia, não a **trata**. Dienogest não possui mecanismo capaz de corrigir as etiologias primárias da amenorreia (disfunção hipotalâmica, hiperprolactinemia, insuficiência ovariana, anomalias uterinas). Esta previsão constitui um **falso positivo mecanístico** do modelo.

---

## Evidências de Ensaios Clínicos

> ⚠️ Todos os ensaios identificados estudam Dienogest no tratamento da **endometriose**. A amenorreia aparece apenas como evento adverso monitorado, nunca como desfecho terapêutico primário — o que confirma a natureza falso-positiva da previsão.

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT04495855](https://clinicaltrials.gov/study/NCT04495855) | N/A | Concluído | 968 | Estudo observacional de Dienogest em prática clínica real para endometriose (VISANNE OS); avalia alívio de dor pélvica e qualidade de vida. Amenorreia registrada apenas como evento adverso, não como desfecho terapêutico. |
| [NCT02425462](https://clinicaltrials.gov/study/NCT02425462) | N/A | Concluído | 895 | Coorte prospectiva multicêntrica em mulheres asiáticas com endometriose; avalia eficácia de Dienogest na qualidade de vida e segurança a longo prazo. Amenorreia monitorada como evento adverso. |
| [NCT07164183](https://clinicaltrials.gov/study/NCT07164183) | Phase 3 | Recrutando | 290 | Único ensaio Phase 3 identificado: RCT de não-inferioridade comparando Indinol Forto® 200 mg vs. Visanne® (Dienogest 2 mg) para endometriose (Russia). Amenorreia avaliada como desfecho de segurança secundário, não como indicação. |
| [NCT07204093](https://clinicaltrials.gov/study/NCT07204093) | N/A | Ativo (não recrutando) | 138 | Comparação de Dienogest + estradiol transdérmico vs. drospirenona + estradiol para endometriose; foco em satisfação e tolerabilidade do regime. Nenhum desfecho relacionado ao tratamento da amenorreia. |

---

## Evidências da Literatura

> ⚠️ As publicações identificadas abordam Dienogest no contexto da endometriose ou de seus efeitos farmacodinâmicos. A amenorreia aparece como efeito farmacológico esperado/adverso, não como condição sendo tratada. Os dois últimos estudos têm relevância periférica ao tema.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Revisão Sistemática + Meta-análise | BMC Pharmacology & Toxicology | Sistematiza evidências dos efeitos adversos do Dienogest no tratamento de endometriose e adenomiose; confirma amenorreia como efeito adverso prevalente (~20–30%), não como indicação terapêutica. |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Revisão Narrativa | Reviews in Endocrine & Metabolic Disorders | Revisão do tratamento hormonal da endometriose; descreve o papel central do Dienogest na supressão estrogênica e seus efeitos sobre o ciclo menstrual. |
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Estudo Farmacodinâmico | European Journal of Contraception & Reproductive Health Care | Demonstra alta taxa de inibição ovulatória e índice de transformação endometrial do Dienogest 2 mg; indução de amenorreia é consequência farmacológica intencional na endometriose, não desfecho terapêutico para amenorreia primária. |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Coorte Prospectiva | Reproductive Sciences | Avaliação de eficácia e segurança do uso prolongado (>12 meses) de Dienogest em endometrioma ovariano; 514 pacientes em 7 hospitais universitários. Sem avaliação da amenorreia como indicação. |
| [34918698](https://pubmed.ncbi.nlm.nih.gov/34918698/) | 2021 | Relato de Caso | Medicine | Tumor de células da granulosa ovariana em paciente com síndrome dos ovários policísticos; relevância periférica e indireta para Dienogest. |
| [40543564](https://pubmed.ncbi.nlm.nih.gov/40543564/) | 2025 | Estudo Clínico | Journal of Pediatric and Adolescent Gynecology | Visualização 3D e realidade virtual para anomalias Müllerianas obstrutivas; sem relação direta com Dienogest ou com o tratamento da amenorreia. |

---

## Informações de Comercialização no Brasil

O Dienogest possui **20 registros ativos** no Brasil com situação de comercialização confirmada. Os dados detalhados individuais de cada registro (número ANVISA, nome comercial, forma farmacêutica e indicação aprovada em bula) não estavam disponíveis neste pacote de evidências e constituem uma lacuna de dados bloqueante para a avaliação de segurança completa (DG001).

> Para consulta completa dos registros: [Consultas de Produtos — ANVISA](https://consultas.anvisa.gov.br/#/medicamentos/)

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN para amenorreia é classificada como **falso positivo mecanístico**: o Dienogest **induz** amenorreia como efeito adverso do tratamento da endometriose, mas não possui mecanismo de ação para tratar as causas subjacentes da amenorreia primária ou secundária. Adicionalmente, os dados de segurança (bula ANVISA, advertências e contraindicações) estão indisponíveis, configurando um bloqueio formal à progressão para a fase S1 de avaliação. O mesmo padrão de Hold se repete nas demais 9 indicações previstas pelo modelo para Dienogest, sendo a maioria associações de grafos distantes (aberrações cromossômicas, BPES, deficiência de GH isolada) sem qualquer suporte mecanístico ou clínico.

**Para prosseguir, é necessário:**
- **[Bloqueante]** Obter e analisar a bula completa da ANVISA (advertências, contraindicações, interações medicamentosas) — requisito obrigatório para entrada na fase S1
- **[Alta prioridade]** Confirmar o mecanismo de ação detalhado via DrugBank API (DB09123), especialmente dados de receptor-alvo e vias de sinalização
- Verificar junto à ANVISA se algum dos 20 registros inclui indicações além de endometriose (ex.: adenomiose, dismenorreia)
- Considerar **reclassificação da previsão** de amenorreia como falso positivo no pipeline TxGNN para refinamento do modelo — o padrão "efeito adverso confundido com indicação" deve ser documentado para evitar recorrência em outros candidatos
---

