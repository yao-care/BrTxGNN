---
layout: default
title: Erythromycin
parent: 僅模型預測 (L5)
nav_order: 238
evidence_level: L5
indication_count: 10
---

# Erythromycin
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

# Erythromycin: De antibiótico macrolídeo a queratoconjuntivite epitelial punctata

## Resumo em Uma Frase

Erythromycin é um antibiótico macrolídeo clássico com atividade documentada contra *Chlamydia trachomatis*, *Staphylococcus aureus* e outros patógenos bacterianos, disponível em formulação sistêmica e oftálmica (pomada), com uso histórico registrado desde a década de 1950.
O modelo TxGNN prevê que pode ser eficaz para **Queratoconjuntivite Epitelial Punctata (Punctate Epithelial Keratoconjunctivitis)** como indicação mais bem ranqueada entre 10 novas indicações previstas, atualmente com **0 ensaios clínicos** e **2 publicações** apoiando esta direção específica.
Entre todas as indicações previstas, **Linfogranuloma Venéreo (rank 4)** apresenta o maior suporte histórico com uso documentado de erythromycin e evidência de nível L3.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antibiótico macrolídeo para infecções bacterianas (sem registro ANVISA) |
| Nova Indicação Prevista | Queratoconjuntivite Epitelial Punctata (Punctate Epithelial Keratoconjunctivitis) |
| Pontuação de Previsão TxGNN | 99,89% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Painel de Indicações Previstas (Top 10)

| Rank | Indicação | TxGNN Score | Evidência | Ensaios | Literatura | Decisão |
|------|-----------|-------------|-----------|---------|------------|---------|
| 1 | Queratoconjuntivite Epitelial Punctata | 99,89% | L4 | 0 | 2 | Hold |
| 2 | Conjuntivite Aguda Contagiosa | 99,55% | L5 | 0 | 0 | Hold |
| 3 | Ceratite por Exposição | 99,50% | L4 | 0 | 8 | Hold |
| **4** | **Linfogranuloma Venéreo** | **99,05%** | **L3** | **1** | **20** | **Research Question** |
| **5** | **Gengivite Ulcerativa Necrotizante** | **99,00%** | **L3** | **0** | **5** | **Research Question** |
| 6 | Síndrome de Hiperviscosidade Policlonal | 98,84% | L5 | 0 | 0 | Hold |
| 7 | Hiperamilasemia | 98,84% | L5 | 0 | 0 | Hold |
| 8 | Vasculite Pós-infecciosa | 98,77% | L5 | 0 | 0 | Hold |
| 9 | Distúrbio Pós-bacteriano | 98,75% | L3 | ~50* | 0 | Research Question |
| 10 | Síndrome Pós-infecciosa | 98,71% | L3 | ~38* | 4 | Research Question |

> \* Ensaios recuperados por similaridade de classe (principalmente azithromycin); relevância direta variável.

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação registrados nesta base de evidências. Segundo informações conhecidas, Erythromycin é um antibiótico macrolídeo com **duplo mecanismo de ação**: ação antibacteriana por inibição da síntese proteica bacteriana via ligação à subunidade ribossomal 50S, eficaz contra bactérias gram-positivas, *Chlamydia trachomatis* e *Staphylococcus aureus*; e ação imunomoduladora com inibição de NF-κB e IL-8 e regulação da secreção de muco — mecanismo relevante em condições inflamatórias crônicas das mucosas. A formulação oftálmica (pomada 0,5%) com uso documentado em infecções oculares bacterianas reforça a plausibilidade de aplicação ocular.

A queratoconjuntivite epitelial punctata é caracterizada por lesões puntiformes no epitélio corneal e conjuntival. Quando de etiologia bacteriana, os principais agentes envolvidos incluem *Chlamydia trachomatis* e *Staphylococcus aureus* — exatamente os micro-organismos para os quais erythromycin demonstra atividade antimicrobiana documentada. Nesse subgrupo específico, a relação mecanística entre o fármaco e a patologia é coerente.

No entanto, é importante considerar que a maioria das queratoconjuntivites punctatas tem etiologia viral (ex.: adenovírus, herpes) ou não infecciosa (olho seco, hipersensibilidade), para as quais erythromycin não apresenta eficácia direta. A conexão mecanística é considerada **fraca** para a indicação no sentido amplo, e o modelo TxGNN pode estar captando uma associação indireta via grafo de conhecimento fármaco-doença.

---

## Evidências de Ensaios Clínicos — Queratoconjuntivite Epitelial Punctata

Atualmente não há ensaios clínicos relacionados a erythromycin e queratoconjuntivite epitelial punctata registrados.

---

## Evidências da Literatura — Queratoconjuntivite Epitelial Punctata

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [11495307](https://pubmed.ncbi.nlm.nih.gov/11495307/) | 2001 | Review/Case Series | J Pediatric Ophthalmol Strabismus | Diagnóstico e manejo de blefaroqueratoconjuntivite crônica em crianças; discute tratamento da condição, sem focar especificamente em erythromycin |
| [32826651](https://pubmed.ncbi.nlm.nih.gov/32826651/) | 2021 | Case Report | Cornea | Caso de queratoconjuntivite por microsporídios (*Encephalitozoon hellem*) em adulto imunocompetente; diagnóstico por sequenciamento metagenômico profundo; relevância indireta à etiologia infecciosa |

---

## Destaque: Linfogranuloma Venéreo — Indicação com Maior Suporte Histórico

Entre todas as indicações previstas, **Linfogranuloma Venéreo (LGV)** apresenta a evidência mais robusta para uso de erythromycin, com mecanismo direto e uso clínico historicamente documentado.

**Conexão Mecanística**: LGV é causado por *Chlamydia trachomatis* sorovares L1-L3. Erythromycin como macrolídeo tem eficácia comprovada contra clamídia e foi listado historicamente como tratamento alternativo para LGV — especialmente em gestantes quando doxiciclina é contraindicada. O vínculo mecanístico é **claro e direto**.

### Ensaio Clínico Relevante

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT03608774](https://clinicaltrials.gov/study/NCT03608774) | Phase 4 | Concluído | 177 | Azithromycin vs. doxiciclina para *Chlamydia trachomatis* retal em HSH; suporte de classe para macrolídeos no tratamento de infecção clamidial anotretal (Grau B — efeito de classe) |

### Literatura Selecionada

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [13239093](https://pubmed.ncbi.nlm.nih.gov/13239093/) | 1955 | Estudo Clínico Precoce | Antibiotic Medicine & Clinical Therapy | Combinação de erythromycin + tripla sulfonamida no tratamento precoce de LGV — uso direto de erythromycin documentado |
| [22760150](https://pubmed.ncbi.nlm.nih.gov/22760150/) | 2012 | Case Report | Rev Soc Bras Med Trop | Caso de LGV em adolescente tratado com erythromycin; uso direto do fármaco registrado em prática clínica |
| [25870512](https://pubmed.ncbi.nlm.nih.gov/25870512/) | 2015 | Review | Infection and Drug Resistance | Revisão de desafios diagnósticos e terapêuticos do LGV; surtos em HSH na América do Norte, Europa e Austrália; aborda regimes alternativos incluindo macrolídeos |
| [40815293](https://pubmed.ncbi.nlm.nih.gov/40815293/) | 2025 | Cohort/Registry | Sexually Transmitted Diseases | Estudo de prevalência e tratamento de LGV em gbMSM no Canadá (2018–2022); caracteriza perfil epidemiológico atual e práticas de tratamento |
| [33462582](https://pubmed.ncbi.nlm.nih.gov/33462582/) | 2021 | Case Series | Clin Infect Dis | Azithromycin semanal oral 1 g por 3 semanas no tratamento de proctite por LGV; eficácia de macrolídeo de mesma classe |

---

## Destaque: Gengivite Ulcerativa Necrotizante — Uso Histórico em Odontologia

**Conexão Mecanística**: A gengivite ulcerativa necrotizante (Vincent) é causada por flora mista de fusiformes e espiroquetas. Erythromycin demonstra atividade contra essas espécies e foi estudado diretamente para infecções fusoespiroquetais desde 1953 — mecanismo **explicitamente documentado em literatura histórica**.

### Literatura Selecionada

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [13221896](https://pubmed.ncbi.nlm.nih.gov/13221896/) | 1953 | Estudo Clínico Precoce | The Journal-Lancet | "Ilotycin" (erythromycin) para infecções fusoespiroquetais da orofaringe — evidência direta mais antiga identificada |
| [6589179](https://pubmed.ncbi.nlm.nih.gov/6589179/) | 1984 | Review | Dent Clin North Am | Erythromycin como antibiótico de segunda escolha em infecções dentárias; primeira escolha em pacientes alérgicos a penicilina |
| [36268928](https://pubmed.ncbi.nlm.nih.gov/36268928/) | 2022 | Narrative Review | Eur J Transl Myology | Uso de antibióticos em tratamento endodôntico na gestação; erythromycin citado como opção segura em gestantes |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold** (indicação primária) | **Research Question** (LGV e NUG)

**Justificativa:**
Para a indicação primária ranqueada pelo TxGNN (queratoconjuntivite epitelial punctata), as evidências são insuficientes — nível L4, sem ensaios clínicos diretos e apenas 2 publicações periféricas, com mecanismo de ação indiretamente conectado à patologia. Contudo, entre as 10 indicações previstas, Linfogranuloma Venéreo e Gengivite Ulcerativa Necrotizante apresentam suporte histórico clínico direto para erythromycin, com uso documentado desde os anos 1950 e mecanismo plausível, justificando investigação formal.

**Para prosseguir, é necessário:**
- Obter dados de mecanismo de ação (MOA) completos via DrugBank API (item prioritário)
- Obter dados de segurança — bula ANVISA ou FDA — para avaliação de contraindicações, advertências e interações medicamentosas
- Avaliar compatibilidade de via de administração para indicações oftálmicas (pomada) vs. sistêmicas (oral/IV)
- Priorizar investigação clínica para **Linfogranuloma Venéreo** (L3, uso histórico direto de erythromycin, contexto de gestantes como população-alvo sem alternativas seguras) e **Gengivite Ulcerativa Necrotizante** (L3, estudos diretos desde 1953)
- Avaliar possibilidade de registro na ANVISA caso haja interesse em avançar para uso clínico no Brasil — atualmente o fármaco não possui nenhuma autorização ativa
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

