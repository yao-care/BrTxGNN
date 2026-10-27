---
layout: default
title: Artemether
parent: Apenas Predição do Modelo (L5)
nav_order: 78
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Artemether: nova indicação prevista, Angioedema adquirido (acquired angioedema) (nível de evidência L5). Indicação original: Antimaláricos"
monitor_inn: "artemether"
predicted_indications: ["acquired angioedema", "Plasmodium falciparum malaria", "angioedema", "hereditary angioedema", "nephrogenic syndrome of inappropriate antidiuresis", "acute contagious conjunctivitis", "scleroderma (disease)", "conjunctivitis", "renin-angiotensin-aldosterone system-blocker-induced angioedema"]
---

# Artemether
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relatório de avaliação farmacêutica

</div>

## Artemeter: Do antimalárico à reafirmação da indicação em malária por *Plasmodium falciparum*
{: .text-alpha }

## Resumo em Uma Frase

Artemeter é um derivado da artemisinina, originalmente registrado no Brasil como antimalárico (marca COARTEM).
O modelo TxGNN atribuiu a maior pontuação a **angioedema adquirido (acquired angioedema)**, sem nenhuma evidência de apoio. A indicação com evidências robustas é **malária por *Plasmodium falciparum***, que na prática confirma o uso original e não representa um reposicionamento novo, com **30 ensaios clínicos** e **20 publicações** nos dados compilados.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antimaláricos |
| Nova Indicação Prevista (1ª colocada no modelo) | Angioedema adquirido (acquired angioedema) |
| Indicação com evidências (2ª colocada) | Malária por *Plasmodium falciparum* (indicação já estabelecida) |
| Pontuação de Previsão TxGNN | 99,90% (angioedema adquirido); 99,77% (malária por *P. falciparum*) |
| Nível de Evidência | L5 (angioedema adquirido); L1 (malária por *P. falciparum*, confirmação do uso original) |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 1 (cancelado) |
| Decisão Recomendada | Hold para angioedema adquirido; Proceed with Guardrails apenas para a malária (uso já estabelecido) |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados de mecanismo de ação nos campos do fármaco. Segundo informações conhecidas, o artemeter é um derivado da artemisinina. Sua ponte endoperóxido é ativada pelo ferro do heme no parasita, gerando radicais livres que alquilam proteínas do *Plasmodium*. Costuma ser usado em combinação fixa com lumefantrina como tratamento de primeira linha da malária não complicada por *P. falciparum*.

**Angioedema adquirido (previsão nº 1):** não há vínculo mecanístico plausível. O angioedema envolve a via da bradicinina e do inibidor de C1 do complemento, sobre as quais o artemeter não tem ação conhecida. A pontuação alta (0,999) reflete apenas proximidade no grafo de conhecimento. Não há ensaios clínicos nem literatura. As previsões para angioedema (geral, hereditário e induzido por bloqueadores do sistema renina-angiotensina-aldosterona) seguem o mesmo padrão.

**Malária:** as previsões nº 2 (*P. falciparum*) e nº 3 (malária) coincidem com o uso original. Isso valida o modelo, mas não traz uma nova indicação. A análise de reposicionamento real deveria se concentrar em hipóteses como esclerodermia (efeitos antifibróticos e imunomoduladores pré-clínicos das artemisininas, via TGF-β), ainda puramente especulativa e sem estudos recuperados.

---

## Evidências de Ensaios Clínicos

Os ensaios abaixo se referem à malária por *P. falciparum*, a indicação original. Para angioedema adquirido não há ensaios registrados.

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00422084](https://clinicaltrials.gov/study/NCT00422084) | Phase 3 | Concluído | 1272 | Pironaridina-artesunato vs. Coartem (artemeter-lumefantrina) em crianças e adultos com malária por *P. falciparum* |
| [NCT01082705](https://clinicaltrials.gov/study/NCT01082705) | Phase 3 | Concluído | 323 | Eficácia de combinações com artemisinina em crianças de 6 a 59 meses na Tanzânia |
| [NCT00677833](https://clinicaltrials.gov/study/NCT00677833) | Phase 2/3 | Concluído | 361 | Azitromicina + cloroquina vs. artemeter-lumefantrina em crianças africanas (não inferioridade) |
| [NCT05951595](https://clinicaltrials.gov/study/NCT05951595) | Phase 3 | Recrutando | 1680 | Combinação tripla artemeter-lumefantrina-amodiaquina vs. ACTs de primeira linha |
| [NCT02020330](https://clinicaltrials.gov/study/NCT02020330) | Phase 3 | Concluído | 150 | Esquema de 3 vs. 5 dias de artemeter-lumefantrina em Mianmar |
| [NCT00529867](https://clinicaltrials.gov/study/NCT00529867) | Phase 4 | Concluído | 267 | Suspensão vs. comprimidos de artemeter-lumefantrina em crianças no Quênia |
| [NCT03453840](https://clinicaltrials.gov/study/NCT03453840) | Phase 4 | Concluído | 305 | Esquema estendido de artemeter-lumefantrina em crianças (inclui HIV em uso de efavirenz) |
| [NCT01017770](https://clinicaltrials.gov/study/NCT01017770) | Phase 4 | Concluído | 340 | Artemeter-lumefantrina vs. artesunato + amodiaquina em Burkina Faso |
| [NCT02637128](https://clinicaltrials.gov/study/NCT02637128) | Phase 4 | Concluído | 452 | Eficácia in vivo de artemeter-lumefantrina e artesunato-amodiaquina no Malawi |
| [NCT01103830](https://clinicaltrials.gov/study/NCT01103830) | Phase 1 | Concluído | 287 | Efeito sobre o intervalo QT/QTc de Eurartesim vs. Riamet (artemeter-lumefantrina), placebo e moxifloxacino em voluntários saudáveis |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [35271592](https://pubmed.ncbi.nlm.nih.gov/35271592/) | 2022 | Revisão sistemática/meta-análise | PloS one | Eficácia terapêutica de artemeter-lumefantrina, artesunato-amodiaquina e di-hidroartemisinina-piperaquina na África Subsaariana |
| [31210357](https://pubmed.ncbi.nlm.nih.gov/31210357/) | 2019 | Revisão Cochrane | Cochrane Database Syst Rev | Artemeter intramuscular vs. quinina e artesunato na malária grave |
| [25209020](https://pubmed.ncbi.nlm.nih.gov/25209020/) | 2014 | Revisão Cochrane | Cochrane Database Syst Rev | Versão anterior da revisão sobre artemeter na malária grave |
| [17402835](https://pubmed.ncbi.nlm.nih.gov/17402835/) | 2007 | Revisão | Expert Rev Anti Infect Ther | Artemeter não mostrou vantagem convincente de mortalidade sobre a quinina; artesunato foi superior à quinina no estudo SEAQUAMAT |
| [22548983](https://pubmed.ncbi.nlm.nih.gov/22548983/) | 2012 | Revisão sistemática | Malaria Journal | Segurança e eficácia de artemeter-lumefantrina na gravidez |
| [34983552](https://pubmed.ncbi.nlm.nih.gov/34983552/) | 2022 | Revisão sistemática/meta-análise de RCTs | Malaria Journal | Segurança de di-hidroartemisinina-piperaquina vs. artemeter-lumefantrina em crianças africanas |
| [40660279](https://pubmed.ncbi.nlm.nih.gov/40660279/) | 2025 | Estudo de eficácia terapêutica | Malaria Journal | Eficácia de artemeter-lumefantrina e de outras combinações em Moçambique (2022) |
| [27430374](https://pubmed.ncbi.nlm.nih.gov/27430374/) | 2016 | Ensaio randomizado Phase 4 | Lancet Infect Dis | Artesunato-mefloquina vs. artemeter-lumefantrina em crianças menores de 5 anos na África Subsaariana |
| [40138574](https://pubmed.ncbi.nlm.nih.gov/40138574/) | 2025 | Coorte | J Infect Dis | O tratamento com artemeter-lumefantrina seleciona aumento do número de cópias de *pfmdr1*; eficácia reduzida surgiu recentemente na África |
| [29137664](https://pubmed.ncbi.nlm.nih.gov/29137664/) | 2017 | Meta-análise | Infect Dis Poverty | Eficácia de artemeter-lumefantrina na malária não complicada na Etiópia |

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 100680103 (cancelado) | COARTEM | Não informada | Antimaláricos |

---

## Citotoxicidade

Não aplicável: o artemeter é um antimalárico, não um antineoplásico. Esta seção foi omitida.

---

## Considerações de Segurança

- **Advertências e contraindicações da bula (ANVISA):** não disponíveis nos dados compilados. Consulte a bula para informações de segurança.
- **Condições associadas a contraindicação no grafo de conhecimento** (não provêm de bula): síndrome do QT longo, síndrome do QT longo familiar, *torsades de pointes* e deficiência de potássio. Isso coincide com o estudo de QT/QTc listado entre os ensaios e indica necessidade de cautela cardíaca.
- **Interações medicamentosas:** foram identificadas **95 interações** no total; as principais, entre as 20 listadas, são:
  - **Graves (Major):** claritromicina, cobicistate, amprenavir, apalutamida, atazanavir, boceprevir.
  - **Moderadas (Moderate):** dexametasona, miconazol, troglitazona, deferasirox, iodeto I-123 e I-131, fostamatinibe, abametapir (tópico), aminoglutetimida, amobarbital, armodafinil, bexaroteno, bosentana, brigatinibe.

---

## Conclusão e Próximos Passos

**Decisão: Hold** (para as previsões de reposicionamento real, a começar pelo angioedema adquirido). Para a malária por *P. falciparum*, **Proceed with Guardrails** vale apenas como confirmação do uso já estabelecido.

**Justificativa:**
- A previsão de maior pontuação (angioedema adquirido, 99,90%) não tem ensaios, literatura nem vínculo mecanístico plausível, ficando em L5.
- As evidências robustas (L1) dizem respeito à malária, indicação original, e não constituem reposicionamento. Além disso, o único registro brasileiro está cancelado.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), lacuna que bloqueia a triagem de segurança.
- Obter dados do mecanismo de ação no DrugBank.
- Esclarecer a situação regulatória: o registro COARTEM está cancelado, sem registro válido de monoterapia ou combinação.
- Para qualquer hipótese de reposicionamento (por exemplo, esclerodermia), gerar evidências pré-clínicas e justificar o mecanismo antes de avançar.
- Avaliar o risco cardíaco (QT) e o plano de manejo das interações graves, especialmente com inibidores de CYP3A4 e antirretrovirais.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

