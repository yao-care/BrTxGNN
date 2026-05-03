---
layout: default
title: Donepezil
parent: 僅模型預測 (L5)
nav_order: 228
evidence_level: L5
indication_count: 8
---

# Donepezil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

Usando o skill `txgnn-pipeline` para contextualização do pipeline TxGNN. Agora vou gerar o relatório completo com base no Evidence Pack fornecido.

---

# Donepezil: Da Doença de Alzheimer aos Transtornos Psicogênicos do Movimento

## Resumo

Donepezil é um inibidor seletivo da acetilcolinesterase (AChEI) amplamente utilizado no tratamento da doença de Alzheimer, atuando ao aumentar os níveis de acetilcolina no sistema nervoso central. O modelo TxGNN prevê eficácia potencial em **8 indicações** dentro do espectro de transtornos do movimento — com pontuações entre 99,02% e 99,23% —, sendo a **discinesia lingual-facial-bucinadora (rank 8)** a indicação com maior respaldo científico atual (nível L3, incluindo 2 revisões sistemáticas Cochrane). A maioria das indicações previstas carece de evidências clínicas diretas (L5), e existe um sinal de segurança crítico e bidirecional: os próprios AChEIs podem **induzir ou agravar** transtornos do movimento, exigindo avaliação criteriosa antes de qualquer avanço.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Doença de Alzheimer |
| Nova Indicação Prevista (Rank 1) | Transtornos Psicogênicos do Movimento (Psychogenic Movement Disorders) |
| Pontuação de Previsão TxGNN | 99,23% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Visão Geral de Todas as Indicações Previstas

| Rank | Indicação | Score TxGNN | Nível | Decisão |
|------|-----------|-------------|-------|---------|
| 1 | Transtornos Psicogênicos do Movimento | 99,23% | L5 | Hold |
| 2 | Distúrbio de Tique Crônico | 99,19% | L4 | Research Question |
| 3 | Tremor Ortostático Primário | 99,17% | L5 | Hold |
| 4 | Ataques de Tremor Benigno | 99,16% | L5 | Hold |
| 5 | Doenças Extrapiramidais e do Movimento | 99,16% | L4 | Hold |
| 6 | Síndrome de Tremor–Nistagmo–Úlcera Duodenal | 99,15% | L5 | Hold |
| 7 | Desvio Ocular Tônico Paroxístico Benigno da Infância com Ataxia | 99,12% | L5 | Hold |
| 8 | Discinesia Lingual-Facial-Bucinadora | 99,02% | L3 | Research Question |

---

## Por que Esta Previsão é Razoável?

Donepezil é um inibidor seletivo e reversível da acetilcolinesterase (AChEI), enzima responsável pela degradação da acetilcolina (ACh) na fenda sináptica. Ao inibir essa enzima, o fármaco eleva os níveis de ACh no sistema nervoso central — mecanismo que fundamenta sua eficácia comprovada na doença de Alzheimer, onde há perda progressiva de neurônios colinérgicos no prosencéfalo basal.

O sistema colinérgico exerce papel modulatório relevante nos gânglios da base: os interneurônios colinérgicos estriatais (*tonically active neurons*, TAN) regulam a liberação de dopamina e participam do controle motor fino. Esse substrato neurobiológico estabelece uma ponte teórica entre o mecanismo do Donepezil e condições de transtorno do movimento com desequilíbrio colinérgico-dopaminérgico — especialmente discinesias tardias, distúrbios de tique e formas de hipercinesia relacionadas à hiperdopaminergia estriatal. O TxGNN captura essas proximidades de rede no grafo de conhecimento, gerando pontuações elevadas para todo o espectro de transtornos do movimento.

Contudo, para a **indicação de rank 1 — transtornos psicogênicos do movimento** — a conexão mecanística é fraca: esses transtornos são distúrbios neurológicos *funcionais*, cuja fisiopatologia envolve dissociação psicológica-neurológica e não déficit colinérgico sináptico. O alto score do TxGNN para essa indicação provavelmente reflete vizinhança topológica no grafo com outras doenças neuromotoras, e não uma relação mecanística genuína. Acrescenta-se um sinal de segurança importante documentado em revisão sistemática de 2025 (PMID 40224553): os próprios AChEIs podem **induzir ou exacerbar** transtornos do movimento em pacientes com Alzheimer, configurando risco bidirecional que exige precaução especial no contexto de reposicionamento.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para **Transtornos Psicogênicos do Movimento** com Donepezil.

> Também não foram identificados ensaios clínicos registrados para nenhuma das demais 7 indicações previstas neste relatório.

---

## Evidências da Literatura

### Rank 1 — Transtornos Psicogênicos do Movimento

Atualmente não há literatura relacionada para esta indicação específica.

---

### Rank 2 — Distúrbio de Tique Crônico (5 publicações)

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [18343255](https://pubmed.ncbi.nlm.nih.gov/18343255/) | 2008 | Ensaio aberto (crianças/adolescentes) | Clinical Therapeutics | Estudo prospectivo de 18 semanas com escalada de dose; explora papel da disfunção colinérgica estriatal em tiques e TDAH; resultados preliminares favoráveis ao uso de Donepezil |
| [16045972](https://pubmed.ncbi.nlm.nih.gov/16045972/) | 2005 | Estudo animal (camundongos) | Pharmacology, Biochemistry and Behavior | Donepezil atenua a resposta de abalos cefálicos induzida por DOI (modelo murino de tiques na Síndrome de Tourette) via interação com sistema serotoninérgico 5-HT2A |
| [14643839](https://pubmed.ncbi.nlm.nih.gov/14643839/) | 2003 | Estudo animal (camundongos) | Pharmacology, Biochemistry and Behavior | Donepezil atenua *head twitch response* em modelo de tiques na Síndrome de Tourette, com efeito similar ao da nicotina; apoia hipótese colinérgica |
| [16986157](https://pubmed.ncbi.nlm.nih.gov/16986157/) | 2006 | Relato de caso / Comunicação | Movement Disorders | Comunicação clínica sugerindo possível eficácia de Donepezil na Síndrome de Tourette |
| [10440471](https://pubmed.ncbi.nlm.nih.gov/10440471/) | 1999 | Relato de caso | J Clinical Psychopharmacology | Uso de Donepezil em Síndrome de Tourette associada a TDAH; relato pioneiro sem dados quantitativos |

---

### Rank 5 — Doenças Extrapiramidais e do Movimento (4 publicações)

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [40224553](https://pubmed.ncbi.nlm.nih.gov/40224553/) | 2025 | ⚠️ Revisão sistemática (sinal de segurança) | Brain Circulation | Revisão sobre transtornos do movimento **associados** a AChEIs (incluindo Donepezil) em Alzheimer — documenta risco bidirecional: o fármaco pode induzir ou exacerbar o transtorno que se pretende tratar |
| [15669896](https://pubmed.ncbi.nlm.nih.gov/15669896/) | 2005 | Série de casos / Estudo clínico pequeno | J Clinical Psychiatry | Efeito benéfico do Donepezil em transtornos tardios do movimento em idosos, incluindo discinesia tardia e distonia tardia |
| [14676467](https://pubmed.ncbi.nlm.nih.gov/14676467/) | 2004 | Revisão clínica | Dementia and Geriatric Cognitive Disorders | Manejo farmacológico da Demência com Corpos de Lewy; AChEIs são indicados para sintomas motores semelhantes ao Parkinson nesta condição |
| [12671528](https://pubmed.ncbi.nlm.nih.gov/12671528/) | 2003 | Estudo clínico pequeno | Clinical Neuropharmacology | Donepezil como adjuvante para sintomas psicóticos em Alzheimer; inclui análise de sintomas extrapiramidais em 12 pacientes hospitalizados |

---

### Rank 8 — Discinesia Lingual-Facial-Bucinadora (top 10 de 20 publicações)

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [29553158](https://pubmed.ncbi.nlm.nih.gov/29553158/) | 2018 | Cochrane — Revisão sistemática | Cochrane Database Syst Rev | Avaliação de drogas colinérgicas (incluindo AChEI) para discinesia tardia induzida por antipsicóticos; explora a hipótese de déficit colinérgico central como alvo terapêutico |
| [12137608](https://pubmed.ncbi.nlm.nih.gov/12137608/) | 2002 | Cochrane — Revisão sistemática | Cochrane Database Syst Rev | Avaliação de drogas colinérgicas para discinesia tardia induzida por neurolépticos; inclui Donepezil entre os agentes analisados |
| [15610922](https://pubmed.ncbi.nlm.nih.gov/15610922/) | 2004 | Revisão sistemática + meta-análise | Prog Neuropsychopharmacol Biol Psychiatry | Meta-análise de RCTs sobre drogas colinérgicas (incluindo Donepezil) para discinesia tardia induzida por neurolépticos |
| [40791064](https://pubmed.ncbi.nlm.nih.gov/40791064/) | 2025 | Revisão sistemática | Journal of Huntington's Disease | Avaliação de AChEI e memantina para sintomas cognitivos e motores na doença de Huntington; sem medicação aprovada para sintomas cognitivos até o momento |
| [24127392](https://pubmed.ncbi.nlm.nih.gov/24127392/) | 2014 | ⚠️ Estudo de farmacovigilância (FDA FAERS) | Pharmacotherapy | AChEIs (Donepezil, Rivastigmina, Galantamina) associados a Síndrome de Pisa (forma de distonia); razões de notificação ajustadas sugerem sinal de risco real |
| [12611743](https://pubmed.ncbi.nlm.nih.gov/12611743/) | 2003 | Recomendações baseadas em evidências | Am J Geriatric Psychiatry | Revisão das evidências e recomendações práticas para uso clínico de AChEI, incluindo perfil de efeitos extrapiramidais |
| [19142126](https://pubmed.ncbi.nlm.nih.gov/19142126/) | 2009 | Relato de caso / Estudo pequeno | J Clinical Psychopharmacology | Efeito do Donepezil sobre discinesia tardia; dados clínicos preliminares |
| [18321753](https://pubmed.ncbi.nlm.nih.gov/18321753/) | 2008 | ⚠️ Relato de caso (efeito adverso) | Parkinsonism & Related Disorders | Donepezil causando tremor mandibular de novo — sinal adverso direto de transtorno do movimento induzido pelo fármaco |
| [15689723](https://pubmed.ncbi.nlm.nih.gov/15689723/) | 2005 | Relato de caso | J Am Acad Child Adolesc Psychiatry | Relato de caso sobre Donepezil e discinesia tardia |
| [23917951](https://pubmed.ncbi.nlm.nih.gov/23917951/) | 2013 | Revisão clínica | Drugs | Tratamentos não-dopaminérgicos para controle motor na Doença de Parkinson; aborda papel do sistema colinérgico no controle motor |

---

## Informações de Comercialização no Brasil

Donepezil possui **20 registros** no banco de dados regulatório e está **comercialmente disponível** no mercado brasileiro. Os dados individuais de cada registro (nome comercial, forma farmacêutica, texto de indicação aprovada) não estão disponíveis no Evidence Pack atual.

> Para consultar os registros individuais, acesse o portal ANVISA: [https://consultas.anvisa.gov.br/#/medicamentos/](https://consultas.anvisa.gov.br/#/medicamentos/)

---

## Considerações de Segurança

**Sinal de Segurança Crítico — Efeito Bidirecional:**

A revisão sistemática publicada em 2025 (PMID [40224553](https://pubmed.ncbi.nlm.nih.gov/40224553/), *Brain Circulation*) documenta que os próprios AChEIs — incluindo Donepezil — podem **induzir ou agravar transtornos do movimento** em pacientes com doença de Alzheimer. Este achado representa um alerta direto para o contexto de reposicionamento: o mesmo fármaco previsto para tratar transtornos do movimento pode, em determinados contextos clínicos, provocá-los.

Sinais adversos motores específicos documentados na literatura:

- **Tremor mandibular de novo** induzido por Donepezil (PMID [18321753](https://pubmed.ncbi.nlm.nih.gov/18321753/))
- **Síndrome de Pisa** (distonia axial) associada a AChEIs em dados de farmacovigilância FDA (PMID [24127392](https://pubmed.ncbi.nlm.nih.gov/24127392/))
- **Status mioclônico** em combinação com olanzapina (PMID [15965316](https://pubmed.ncbi.nlm.nih.gov/15965316/))

> Advertências e contraindicações completas não estão disponíveis neste Evidence Pack. Consulte a bula ANVISA para informações de segurança detalhadas.

---

## Conclusão e Próximos Passos

**Decisão Global: Hold**

**Justificativa:**
Das 8 indicações previstas pelo TxGNN, 6 têm nível de evidência L5 (apenas previsão do modelo, sem estudos clínicos reais) e a indicação de rank 1 — transtornos psicogênicos do movimento — não possui conexão mecanística convincente com o AChEI. Existe um sinal de segurança bidirecional relevante e bem documentado que contraindicação o avanço sem dados de segurança robustos. As únicas duas indicações com status *Research Question* são o **distúrbio de tique crônico (L4)** e a **discinesia lingual-facial-bucinadora (L3)**, esta última respaldada por duas revisões Cochrane, mas com evidências ainda insuficientes para avanço clínico direto.

**Para prosseguir, é necessário:**

- Recuperar dados completos de segurança da bula ANVISA (advertências, contraindicações, interações — itens DG001 e DG002 do Evidence Pack)
- Recuperar mecanismo de ação detalhado via DrugBank API (DrugBank ID: DB00843)
- Para **discinesia lingual-facial-bucinadora**: realizar leitura aprofundada das duas revisões Cochrane (PMIDs 29553158 e 12137608) e da meta-análise (PMID 15610922) como base para avaliação de *Research Question*
- Para **distúrbio de tique crônico**: mapear todos os estudos disponíveis e avaliar viabilidade de protocolo piloto pediátrico, considerando o único ensaio aberto existente (PMID 18343255)
- Avaliação por especialista em **neurologia do movimento** para validação da hipótese mecanística e do perfil de risco-benefício
- Definição de um protocolo de Phase 2 controlado antes de qualquer consideração comercial
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

