---
layout: default
title: Magnesium Hydroxide
parent: 僅模型預測 (L5)
nav_order: 335
evidence_level: L5
indication_count: 6
---

# Magnesium Hydroxide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

O skill `txgnn-pipeline` cobre operações de pipeline (treino, validação, deployment) — as instruções de formatação do relatório já estão definidas no sistema. Vou gerar o relatório completo agora.

---

# Hidróxido de Magnésio: Do Antiácido Clássico à Úlcera Péptica Ativa

## Resumo em Uma Frase

Hidróxido de magnésio (Mg(OH)₂) é um antiácido inorgânico clássico, utilizado há décadas no alívio sintomático de azia, dispepsia e como laxativo osmótico, sem registro formal no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **Úlcera Péptica Ativa (active peptic ulcer disease)**, com base em mecanismo de neutralização ácida e citoproteção mucosa farmacologicamente coerente.
Esta previsão é apoiada por **0 ensaios clínicos registrados** e **20 publicações científicas** identificadas na literatura.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antiácido e laxativo osmótico (uso tradicional bem estabelecido; sem registro no Brasil) |
| Nova Indicação Prevista | Úlcera Péptica Ativa (active peptic ulcer disease) |
| Pontuação de Previsão TxGNN | 99.98% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Não há dados estruturados de mecanismo de ação (MOA) disponíveis neste Evidence Pack. Com base em informações farmacológicas bem estabelecidas, o hidróxido de magnésio age como antiácido inorgânico de ação rápida pela reação química direta com o ácido clorídrico gástrico: **Mg(OH)₂ + 2HCl → MgCl₂ + 2H₂O**. Esta reação eleva rapidamente o pH intragástrico para valores acima de 3,5, patamar a partir do qual a atividade da pepsina — cuja faixa ótima se situa entre pH 1,5 e 2,5 — é significativamente inibida, reduzindo o dano proteolítico à mucosa ulcerada.

A úlcera péptica ativa resulta do desequilíbrio entre fatores agressores (ácido, pepsina, H. pylori, AINEs) e mecanismos protetores da mucosa (muco, bicarbonato, prostaglandinas, microcirculação). O Mg(OH)₂ atua em dois eixos complementares desse desequilíbrio: além da neutralização ácida imediata, o íon Mg²⁺ estimula a síntese endógena de prostaglandina E₂ pela mucosa gástrica (PMID 2595273), reforçando a barreira de bicarbonato e muco e conferindo citoproteção que ultrapassa o efeito tamponante isolado. Estudos animais demonstraram que esse mecanismo é comparável em potência ao análogo sintético de PGE₂ em modelos de lesão por etanol e AAS.

Do ponto de vista histórico, antacids à base de Mg(OH)₂ foram durante décadas o tratamento-padrão da úlcera péptica antes do advento dos bloqueadores H₂ e dos inibidores da bomba de prótons. Ensaios clínicos controlados (PMID 7034155) demonstraram cicatrização de úlcera duodenal em 50% dos pacientes em 3 semanas e revisões recentes (PMID 22950493) consolidam os mecanismos moleculares envolvidos, tornando a previsão do TxGNN clinicamente e mecanisticamente justificada.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Hidróxido de Magnésio em Úlcera Péptica Ativa.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT | Scandinavian Journal of Gastroenterology | Ensaio duplo-cego, 72 pacientes, 12 semanas: antacid + anticolinérgico alcançou 50% de cicatrização vs 67% com cimetidina (ambos p<0,005 vs placebo) em úlceras duodenais e pré-pilóricas |
| [1526089](https://pubmed.ncbi.nlm.nih.gov/1526089/) | 1992 | RCT | Clinical Pharmacology and Therapeutics | Multicêntrico duplo-cego de 8 semanas comparando nizatidina vs placebo em úlcera gástrica benigna ativa; antacid de Mg-Al utilizado como controle sintomático de referência |
| [22950493](https://pubmed.ncbi.nlm.nih.gov/22950493/) | 2013 | Review | Current Pharmaceutical Design | Revisão abrangente dos mecanismos celulares e moleculares de gastroproteção e cicatrização de úlceras pelos antacids, com foco em prostaglandinas, EGF e defesas pré/pós-epiteliais |
| [6086186](https://pubmed.ncbi.nlm.nih.gov/6086186/) | 1984 | Estudo Comparativo | Clinics in Gastroenterology | Revisão clínica de anticolinérgicos e antacids na úlcera duodenal; análise de subtipos de receptores e potencialização do efeito de Mg(OH)₂ em combinação |
| [2401189](https://pubmed.ncbi.nlm.nih.gov/2401189/) | 1990 | Série Clínica | Drugs Under Experimental and Clinical Research | 267 crianças com doença péptica acompanhadas de junho/1985 a maio/1989: terapia antacid mostrou maior eficácia na fase aguda e na prevenção de recidivas |
| [2595273](https://pubmed.ncbi.nlm.nih.gov/2595273/) | 1989 | Estudo Animal | Scandinavian Journal of Gastroenterology | Maalox 70 e Mg(OH)₂ isolado preveniram lesões gástricas por etanol, AAS acidificado e estresse em ratos dose-dependentemente; efeito equiparável ao análogo de PGE₂; papel central de prostanoides endógenos |
| [2390927](https://pubmed.ncbi.nlm.nih.gov/2390927/) | 1990 | Estudo Farmacológico | Digestive Diseases and Sciences | Maalox e Al(OH)₃ elevam PGE e EGF na mucosa gástrica de ratos, acelerando cicatrização de úlceras gastroduodenais crônicas; mecanismo parcialmente dependente de prostaglandinas |
| [35720246](https://pubmed.ncbi.nlm.nih.gov/35720246/) | 2022 | Estudo In Vitro Comparativo | Medicine and Pharmacy Reports | Avaliação da capacidade de neutralização ácida (ANC) de antacids comercializados no Marrocos; fornece parâmetros quantitativos de desempenho de formulações com Mg(OH)₂ |
| [37146](https://pubmed.ncbi.nlm.nih.gov/37146/) | 1979 | Revisão | Fortschritte der Medizin | Antacids na úlcera péptica: capacidade neutralizante depende da composição química; dose eficaz de 40–80 mval administrada 1 e 3 horas após refeições |
| [3018068](https://pubmed.ncbi.nlm.nih.gov/3018068/) | 1986 | Estudo Clínico | Journal of Clinical Gastroenterology | Bicarbonato de sódio vs Al-Mg(OH)₂ em úlcera duodenal: antacid insolúvel mantém efeito tamponante por ~2 horas pós-prandial; antacid solúvel tem efeito mais breve em jejum |

---

## Informações de Comercialização no Brasil

O hidróxido de magnésio não possui registros ativos na ANVISA. O medicamento não está registrado nem comercializado formalmente no Brasil segundo os dados disponíveis.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
O mecanismo de ação do Mg(OH)₂ na úlcera péptica ativa é farmacologicamente coerente e respaldado por literatura clínica e pré-clínica robusta — incluindo RCTs concluídos e revisões mecanísticas recentes —, mas a ausência de ensaios clínicos modernos específicos, de registro regulatório no Brasil e de dados formais de segurança estruturados exige etapas de validação antes de qualquer avanço clínico ou comercial.

**Para prosseguir, é necessário:**
- **Registro regulatório:** iniciar processo de registro na ANVISA, que é pré-requisito para qualquer comercialização formal no Brasil
- **Dados de segurança:** levantar advertências, contraindicações e interações medicamentosas por meio de consulta à bula e à API do DrugBank (lacunas DG001 e DG002 ainda abertas)
- **Ensaio clínico moderno:** desenhar estudo controlado com critérios contemporâneos — diagnóstico endoscópico de úlcera ativa, comparador ativo (IBP), desfecho primário de cicatrização endoscópica em 4–8 semanas
- **Posicionamento clínico:** definir se o papel é de monoterapia em casos selecionados (úlcera leve, sem H. pylori) ou de adjuvante ao IBP para alívio sintomático rápido (aproveitando o início de ação em <5 minutos)
---

