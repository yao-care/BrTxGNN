---
layout: default
title: Desogestrel
parent: 僅模型預測 (L5)
nav_order: 215
evidence_level: L5
indication_count: 10
---

# Desogestrel
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

Usando `txgnn-pipeline` para produzir o relatório de avaliação de reposicionamento de Desogestrel.

---

# Desogestrel: Da contracepção à amenorreia

## Resumo em Uma Frase

Desogestrel é um progestogênio de terceira geração utilizado como componente de anticoncepcionais orais combinados (com etinilestradiol) e como pílula de progestogênio isolado (minipílula 75 µg).
O modelo TxGNN prevê que pode ser eficaz para **Amenorreia (Amenorrhea)**, atualmente com **2 ensaios clínicos** e **16 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Contracepção (anticoncepcional oral) |
| Nova Indicação Prevista | Amenorreia (Amenorrhea) |
| Pontuação de Previsão TxGNN | 99,96% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente não há dados formais de mecanismo de ação (MOA) disponíveis no Evidence Pack. Com base no conhecimento clínico consolidado, desogestrel é um progestogênio gonano com alta seletividade pelo receptor de progesterona e baixa atividade androgênica intrínseca. Na formulação combinada com etinilestradiol (EE), atua suprimindo a secreção hipofisária de LH e FSH, inibindo a ovulação e modulando o eixo hipotálamo-hipófise-ovário (HPO axis). Na formulação de progestogênio isolado (75 µg/dia), o efeito antigonadotrópico é suficiente para inibir a ovulação na maioria dos ciclos.

A relação mecanística com a amenorreia é bidirecional e clinicamente relevante. Por um lado, a minipílula de desogestrel pode **induzir** amenorreia como efeito sobre o endométrio e o ciclo menstrual — conforme documentado no PMID 35261299 (2022). Por outro, a combinação EE+desogestrel pode **tratar** a amenorreia hipotalâmica funcional (como a observada em atletas de alto rendimento e mulheres com restrição calórica severa), fornecendo reposição estrogênica que restaura o feedback negativo do eixo HPO e protege a densidade óssea. É nesse segundo papel — terapêutico — que o modelo TxGNN identifica o potencial de reposicionamento.

O estudo farmacodinâmico de Cullberg (PMID 3161265, 1985) já apontava que o desogestrel reduz androgênios circulantes e suprime o eixo HPO, e Nappi et al. (PMID 2956138, 1987) demonstraram diretamente que EE+desogestrel reduz LH, FSH, androstenediona e testosterona em adolescentes com oligomenorreia e hiperandrogenismo ovariano — população com alta sobreposição com amenorreia hipotalâmica/hiperandrogênica.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00946192](https://clinicaltrials.gov/study/NCT00946192) | Phase 3 | Concluído | 121 | Investiga mudanças hormonais e de composição corporal que diferenciam atletas que perdem o ciclo menstrual daquelas que mantêm; avalia estrogênio transdérmico vs oral para melhora de densidade óssea em atletas adolescentes com amenorreia hipotalâmica e deficiência estrogênica |
| [NCT01588873](https://clinicaltrials.gov/study/NCT01588873) | Phase 4 | Desconhecido | 42 | Compara uso prolongado (59 semanas) de anticoncepcional vaginal e oral sobre secreção androgênica, metabolismo de insulina e glicose, perfil lipídico e SHBG em mulheres com SOP; relevante para amenorreia hiperandrogênica |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [18843653](https://pubmed.ncbi.nlm.nih.gov/18843653/) | 2008 | Cochrane Review | Cochrane Database Syst Rev | Revisão sistemática comparando COCs com 20 µg vs >20 µg de estrogênio; avalia eficácia contraceptiva e padrões de sangramento — relevante para formulações de desogestrel de baixa dose |
| [21249657](https://pubmed.ncbi.nlm.nih.gov/21249657/) | 2011 | Cochrane Review | Cochrane Database Syst Rev | Atualização da revisão Cochrane 2008; confirma que redução do estrogênio impacta o controle do ciclo, incluindo risco de amenorreia |
| [8218004](https://pubmed.ncbi.nlm.nih.gov/8218004/) | 1993 | RCT Comparativo | Br J Obstet Gynaecol | Compara Mercilon (150 µg desogestrel + 20 µg EE) vs Marvelon (150 µg desogestrel + 30 µg EE) quanto a eficácia, controle do ciclo e perfil de efeitos adversos em ensaio randomizado |
| [35261299](https://pubmed.ncbi.nlm.nih.gov/35261299/) | 2022 | Observacional | Gynecol Endocrinol | Compara perfil de sangramento de drospirenona 4 mg vs desogestrel 75 µg em mulheres com risco cardiovascular; documenta que desogestrel 75 µg apresenta controle de ciclo deficiente com alta taxa de amenorreia |
| [3161265](https://pubmed.ncbi.nlm.nih.gov/3161265/) | 1985 | Estudo Farmacodinâmico | Acta Obstet Gynecol Scand Suppl | Avalia androgenicidade do desogestrel vs outros progestogênios; contexto de SOP com amenorreia como modelo de comparação clínica |
| [8447356](https://pubmed.ncbi.nlm.nih.gov/8447356/) | 1993 | Estudo Clínico | Am J Obstet Gynecol | Perfil de tolerabilidade do desogestrel/EE; documenta benefícios não contraceptivos incluindo dismenorreia, endometriose e doença mamária benigna |
| [8324604](https://pubmed.ncbi.nlm.nih.gov/8324604/) | 1993 | Revisão | Br Med Bull | Revisão sobre aceitabilidade e uso efetivo de COCs; discute triagem, seleção e monitoramento de usuárias com base em estudos de coorte e caso-controle |
| [1436906](https://pubmed.ncbi.nlm.nih.gov/1436906/) | 1992 | Revisão | Obstet Gynecol Surv | Caracteriza desogestrel como pró-hormônio que precisa ser metabolizado à sua forma biologicamente ativa; descreve vantagens dos novos progestogênios de terceira geração |
| [1604074](https://pubmed.ncbi.nlm.nih.gov/1604074/) | 1992 | Revisão | Rev Med Liege | Revisão sobre contracepção hormonal, abordando mecanismos e indicações dos progestogênios |
| [7838435](https://pubmed.ncbi.nlm.nih.gov/7838435/) | 1994 | Revisão | Nurse Practitioner | Revisão clínica sobre anticoncepcionais orais combinados, incluindo impacto no ciclo menstrual e amenorreia associada |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Embora o TxGNN atribua pontuação muito elevada (99,96%) e exista 1 ensaio Phase 3 concluído (NCT00946192, n=121), as evidências disponíveis são ainda indiretas — o ensaio avalia reposição estrogênica geral em atletas com amenorreia hipotalâmica, sem confirmar desogestrel como agente interventor principal. A literatura disponível documenta o efeito do desogestrel sobre o ciclo menstrual, mas não estabelece eficácia terapêutica específica no tratamento da amenorreia como indicação primária.

**Para prosseguir, é necessário:**
- Revisar o protocolo completo do NCT00946192 para confirmar se desogestrel é o componente ativo avaliado na intervenção principal
- Obter dados de MOA via DrugBank API (DG002) para fundamentar a análise de plausibilidade mecanística
- Recuperar as advertências e contraindicações da bula ANVISA (DG001) antes de qualquer iniciativa clínica
- Definir o subtipo-alvo de amenorreia: hipotalâmica funcional (atletas/restrição calórica) vs. hiperandrogênica (SOP) — os mecanismos e as populações são distintos
- Conduzir revisão sistemática focada especificamente em EE+desogestrel como intervenção para amenorreia hipotalâmica, separando dos estudos gerais de anticoncepção
---

