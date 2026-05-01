---
layout: default
title: Anastrozole
parent: 僅模型預測 (L5)
nav_order: 64
evidence_level: L5
indication_count: 10
---

# Anastrozole
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

# Anastrozole: Da inibição da aromatase ao carcinoma mamário feminino

## Resumo em Uma Frase

Anastrozole é um inibidor de aromatase de terceira geração utilizado globalmente como tratamento hormonal de primeira linha para câncer de mama receptor hormonal positivo (ER+/HER2−) em mulheres pós-menopausa. O modelo TxGNN prevê que pode ser eficaz para **Carcinoma Mamário Feminino (Female Breast Carcinoma)**, atualmente com **mais de 50 ensaios clínicos** e **20 publicações** apoiando esta direção. Embora esta seja a indicação internacionalmente consolidada do medicamento, Anastrozole não possui registro no mercado brasileiro, configurando uma lacuna de acesso crítica.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Câncer de mama ER+/HER2− em pós-menopausa (aprovado nos EUA e Europa; sem registro no Brasil) |
| Nova Indicação Prevista | Carcinoma Mamário Feminino (Female Breast Carcinoma) |
| Pontuação de Previsão TxGNN | 99,68% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Anastrozole atua inibindo seletivamente a enzima CYP19A1 (aromatase), responsável pela conversão de andrógenos em estrógenos nos tecidos periféricos — principal fonte de estrógeno após a menopausa. Esta inibição resulta em redução superior a 96% nos níveis circulantes de estradiol, privando as células tumorais estrógeno-dependentes de seu principal estímulo proliferativo. Seu mecanismo difere fundamentalmente do tamoxifeno: enquanto este bloqueia o receptor tumoral, Anastrozole age "na fonte", reduzindo a disponibilidade do hormônio em nível sistêmico.

A conexão entre o mecanismo de ação e o carcinoma mamário feminino é direta e biologicamente bem estabelecida. Aproximadamente 70–80% dos cânceres de mama femininos expressam receptores de estrógeno (ER+) e dependem deste hormônio para crescimento e progressão. Ao eliminar a produção periférica de estrógeno, Anastrozole suprime o sinal proliferativo nas células ER+ tumorais — mecanismo de "privação hormonal" com eficácia comprovada tanto no cenário adjuvante quanto na doença avançada.

Anastrozole foi aprovado pelo FDA em 1995 e tornou-se padrão global de tratamento adjuvante, superando o tamoxifeno no emblemático estudo ATAC (9.366 pacientes) em sobrevida livre de doença, tempo para recorrência distante e câncer contralateral — benefício sustentado após mais de 10 anos de seguimento. A pontuação TxGNN de 99,68% reflete precisamente a robustez dessas evidências acumuladas ao longo de três décadas.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00849030](https://clinicaltrials.gov/study/NCT00849030) | Phase 3 | Concluído | 9.358 | ATAC: Anastrozole isolado superior ao tamoxifeno e à combinação como adjuvante em câncer de mama pós-menopausa; maior RCT cabeça-a-cabeça de referência histórica |
| [NCT00066573](https://clinicaltrials.gov/study/NCT00066573) | Phase 3 | Concluído | 7.576 | MA.27: Anastrozole vs Exemestane em câncer de mama ER+ pós-cirurgia; avaliação de recorrência e sobrevida em maior RCT entre IAs de 3ª geração |
| [NCT00556374](https://clinicaltrials.gov/study/NCT00556374) | Phase 3 | Concluído | 3.420 | Denosumabe vs placebo em câncer de mama não-metastático sob terapia com IA (anastrozole/letrozole) para prevenção de fraturas clínicas |
| [NCT00248170](https://clinicaltrials.gov/study/NCT00248170) | Phase 3 | Concluído | 4.172 | Letrozole vs Anastrozole adjuvante por 5 anos em pós-menopausa ER+ com linfonodo positivo; comparação direta entre IAs de 3ª geração |
| [NCT00072462](https://clinicaltrials.gov/study/NCT00072462) | Phase 3 | Concluído | 2.980 | IBIS-II DCIS: Anastrozole vs tamoxifeno para prevenção de recorrência locoregional e câncer contralateral em DCIS ER+ pós-menopausa |
| [NCT00301457](https://clinicaltrials.gov/study/NCT00301457) | Phase 3 | Concluído | 1.914 | Avaliação de 6 vs 3 anos de anastrozole adjuvante após tamoxifeno sequencial; otimização da duração da terapia endócrina |
| [NCT00143390](https://clinicaltrials.gov/study/NCT00143390) | Phase 3 | Concluído | 298 | Exemestane vs Anastrozole como terapia hormonal inicial em câncer de mama avançado/recorrente pós-menopausa; validação de não-inferioridade do exemestane |
| [NCT00256698](https://clinicaltrials.gov/study/NCT00256698) | Phase 3 | Concluído | 514 | FACT: Anastrozole monoterapia vs bloqueio máximo de estrógeno (anastrozole + fulvestrant) na primeira recaída de câncer de mama HR+ |
| [NCT06311383](https://clinicaltrials.gov/study/NCT06311383) | N/A | Concluído | 2.610 | Estudo observacional real-world (Alemanha): efetividade de ribociclib + IA/fulvestrant vs terapia endócrina isolada em câncer de mama HR+/HER2− metastático na 1ª linha |
| [NCT01151215](https://clinicaltrials.gov/study/NCT01151215) | Phase 2 | Encerrado | 482 | MINT: AZD8931 + Anastrozole vs Anastrozole isolado em câncer de mama HR+ localmente avançado/metastático sem tratamento endócrino prévio; encerrado por razão não divulgada |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [31839281](https://pubmed.ncbi.nlm.nih.gov/31839281/) | 2020 | RCT (seguimento longo prazo) | Lancet | IBIS-II: Anastrozole reduziu incidência de câncer de mama em 49% em mulheres de alto risco ao longo de 131 meses de seguimento médio; benefício preventivo sustentado após término do tratamento |
| [15639680](https://pubmed.ncbi.nlm.nih.gov/15639680/) | 2005 | RCT (grande ensaio pivô) | Lancet | ATAC: Anastrozole prolongou significativamente a sobrevida livre de doença vs tamoxifeno (RR 0,87; p=0,01) com menor taxa de câncer contralateral e de recorrência distante |
| [26686313](https://pubmed.ncbi.nlm.nih.gov/26686313/) | 2016 | RCT | Lancet | IBIS-II DCIS: Anastrozole superior ao tamoxifeno na prevenção de recorrência locoregional e câncer contralateral em DCIS ER+ pós-menopausa; ensaio duplo-cego de alta qualidade |
| [28415634](https://pubmed.ncbi.nlm.nih.gov/28415634/) | 2017 | Meta-análise de RCTs | Oncotarget | Meta-análise de RCTs confirmando superioridade do anastrozole vs tamoxifeno em sobrevida livre de doença no câncer de mama ER+, com análise sistemática de benefícios e toxicidades |
| [20923259](https://pubmed.ncbi.nlm.nih.gov/20923259/) | 2010 | Revisão abrangente | Expert Opinion on Drug Safety | Síntese de múltiplos ensaios adjuvantes demonstrando maior eficácia do anastrozole vs tamoxifeno; discussão detalhada do perfil de segurança em longo prazo |
| [16761927](https://pubmed.ncbi.nlm.nih.gov/16761927/) | 2006 | Revisão | Expert Review of Anticancer Therapy | Análise dos desenvolvimentos clínicos do anastrozole com foco no estudo ATAC; eficácia e tolerabilidade no cenário adjuvante e na doença avançada |
| [16439860](https://pubmed.ncbi.nlm.nih.gov/16439860/) | 2006 | Revisão | Oncology | Papel do anastrozole ao longo do contínuo do câncer de mama: doença avançada (segunda e primeira linha), câncer precoce e prevenção primária |
| [28614542](https://pubmed.ncbi.nlm.nih.gov/28614542/) | 2017 | Revisão de literatura | Revista da AMB | Revisão em português sobre quimioprevenção e tratamento com anastrozole; discussão de farmacodinâmica, farmacocinética e variabilidade interindividual |
| [19445563](https://pubmed.ncbi.nlm.nih.gov/19445563/) | 2009 | Revisão comparativa | Expert Opinion on Pharmacotherapy | Comparação dos três IAs de 3ª geração (anastrozole, letrozole, exemestane) em câncer de mama precoce; todos superiores ao tamoxifeno com diferentes nuances de eficácia e tolerabilidade |
| [12113022](https://pubmed.ncbi.nlm.nih.gov/12113022/) | 2001 | Perfil clínico | Expert Review of Anticancer Therapy | Perfil farmacológico e clínico do anastrozole em pós-menopausa; atividade superior ao megestrol e à aminoglutetimida no câncer de mama avançado, com base para uso adjuvante |

---

## Informações de Comercialização no Brasil

Anastrozole **não possui registros aprovados pela ANVISA** e não está disponível comercialmente no Brasil. O medicamento possui aprovação regulatória em mais de 60 países — incluindo EUA (FDA, 1995), União Europeia (EMA) e Japão (PMDA) — para o tratamento adjuvante e de primeira linha do câncer de mama ER+/HER2− em mulheres pós-menopausa, além de aprovação específica para prevenção em populações de alto risco. A ausência de registro nacional contrasta com a ampla disponibilidade internacional e o robusto perfil de evidências do fármaco.

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia alvo hormonal – inibidor seletivo da aromatase (endocrinoterapia; não é quimioterapia citotóxica convencional) |
| Risco de Mielossupressão | Baixo (mecanismo hormonal sem ação direta sobre células hematopoiéticas; não causa supressão de medula óssea) |
| Classificação de Emetogenicidade | Baixa (agente oral com emetogenicidade mínima, inferior a regimes citotóxicos convencionais) |
| Itens de Monitoramento | Densidade mineral óssea/DEXA (risco de osteoporose e fraturas), perfil lipídico (colesterol total, LDL), função hepática (AST/ALT), sintomas musculoesqueléticos (artralgia, mialgia) |
| Proteção no Manuseio | Precauções padrão para medicamentos orais; protocolos específicos de citotóxicos geralmente não são necessários para inibidores de aromatase orais (verificar regulamentações locais da ANVISA) |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Anastrozole possui um dos perfis de evidências mais robustos já documentados em oncologia: múltiplos ensaios Phase 3 concluídos — com destaque para o ATAC (9.358 pacientes) e o MA.27 (7.576 pacientes) —, aprovação regulatória em mais de 60 países e três décadas de uso clínico confirmando eficácia e segurança no tratamento adjuvante do câncer de mama ER+/HER2− em pós-menopausa. A ausência de registro no Brasil representa uma lacuna de acesso significativa, dado que o câncer de mama é o tumor de maior incidência em mulheres no país.

**Para prosseguir, é necessário:**
- Obter dados completos de segurança (bula, advertências e contraindicações formais) para a avaliação de segurança S1 — atualmente classificada como bloqueante (DG001)
- Submeter dossiê de registro à ANVISA, avaliando a viabilidade de via acelerada por comparabilidade com produtos referência com aprovação global consolidada
- Verificar disponibilidade de formulações genéricas internacionais com equivalência comprovada que possam agilizar o processo regulatório
- Estabelecer protocolo de monitoramento de densidade mineral óssea (DEXA basal e seguimento periódico) para pacientes em tratamento
- Avaliar custo-efetividade comparativo com tamoxifeno (disponível no SUS) para definir populações-alvo prioritárias no contexto do sistema de saúde brasileiro
---

