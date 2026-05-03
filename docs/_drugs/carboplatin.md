---
layout: default
title: Carboplatin
parent: 僅模型預測 (L5)
nav_order: 169
evidence_level: L5
indication_count: 10
---

# Carboplatin
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

# Carboplatin: Do câncer de ovário ao carcinoma de mama feminino

## Resumo em Uma Frase

Carboplatin é um agente quimioterápico à base de platina, originalmente utilizado no tratamento do câncer de ovário e outros tumores sólidos avançados.
O modelo TxGNN prevê que pode ser eficaz para **Carcinoma de Mama Feminino (Female Breast Carcinoma)**,
atualmente com **mais de 40 ensaios clínicos registrados, incluindo 5 estudos de Phase 3**, e **20 publicações científicas** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Câncer de ovário (dados detalhados de registro não disponíveis no pacote de evidências) |
| Nova Indicação Prevista | Carcinoma de Mama Feminino (Female Breast Carcinoma) |
| Pontuação de Previsão TxGNN | 99,86% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Carboplatin é um agente alquilante à base de platina que exerce sua ação citotóxica por meio da formação de adutos de DNA intrafita e interfita (*crosslinks*), bloqueando a replicação e transcrição do DNA e induzindo apoptose celular. Seu mecanismo é particularmente eficaz em células que apresentam déficit de reparo por recombinação homóloga (HRD, *Homologous Recombination Deficiency*), pois estas são incapazes de reverter os danos ao DNA promovidos pelo fármaco. Embora os dados formais de mecanismo de ação (MOA) não estejam disponíveis no pacote de evidências atual, o perfil bioquímico do Carboplatin como platinante clássico é amplamente documentado na literatura.

A previsão para carcinoma de mama feminino é altamente plausível do ponto de vista mecanístico e clínico. O câncer de mama triplo negativo (TNBC) e os subtipos com mutações germinais em BRCA1/2 apresentam alta frequência de HRD — justamente o ponto fraco explorado pelos crosslinks do Carboplatin. Nesses tumores, a incapacidade de reparar os danos induzidos pelo fármaco resulta em morte celular seletiva, conferindo uma janela terapêutica favorável. No subtipo HER2-positivo, a combinação Carboplatin + Trastuzumab (esquema TCH: Docetaxel + Carboplatin + Trastuzumab) demonstrou sinergia na indução de danos ao DNA, e este esquema já integra as diretrizes internacionais NCCN como alternativa ao regime com antraciclinas, especialmente em pacientes com risco cardíaco.

Do ponto de vista da similaridade com indicações estabelecidas, a ponte entre o câncer de ovário — onde o Carboplatin é pilar do tratamento — e o câncer de mama é sustentada pela biologia compartilhada entre tumores associados a BRCA1/2, que frequentemente coexistem nas mesmas linhagens hereditárias. Ensaios como o BROCADE3 (Phase 3, BRCA-mutado avançado) e o GeparOcto (Phase 3, 961 pacientes) consolidaram esta expansão terapêutica, tornando a previsão do TxGNN não apenas plausível, mas confirmada por amplo corpo de evidências clínicas.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00047255](https://clinicaltrials.gov/study/NCT00047255) | Phase 3 | Concluído | 263 | Ensaio randomizado comparando TCH (Docetaxel + Carboplatin + Trastuzumab) vs. Docetaxel + Trastuzumab em câncer de mama HER2+ avançado; resultado consolidou o esquema TCH como alternativa sem antraciclina |
| [NCT00532727](https://clinicaltrials.gov/study/NCT00532727) | Phase 3 | Desconhecido | 400 | Triple Negative Trial: comparação direta de Carboplatin vs. Docetaxel em TNBC metastático/recorrente (ER-, PR-, HER2-); maior estudo Phase 3 testando Carboplatin em monofármaco em TNBC |
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Phase 3 | Concluído | 961 | GeparOcto: esquema ETC vs. PM(Cb) dose-densa em neoadjuvante de alto risco; avaliação de Carboplatin em combinação semanal com duplo bloqueio HER2 |
| [NCT02003209](https://clinicaltrials.gov/study/NCT02003209) | Phase 3 | Concluído | 315 | TCHP ± privação estrogênica em HR+/HER2+ localmente avançado neoadjuvante; Carboplatin como componente central do esquema TCHP |
| [NCT03168880](https://clinicaltrials.gov/study/NCT03168880) | Phase 3 | Ativo (não recrutando) | 720 | Paclitaxel semanal vs. Paclitaxel + Carboplatin semanal em TNBC localmente avançado neoadjuvante; avaliação direta do benefício incremental do Carboplatin |
| [NCT07327021](https://clinicaltrials.gov/study/NCT07327021) | Phase 2 | Recrutando | 54 | NOGA: descalonamento neoadjuvante guiado por RMN em TNBC stage II-III; Carboplatin como componente padrão do braço de controle |
| [NCT06291064](https://clinicaltrials.gov/study/NCT06291064) | Phase 2 | Recrutando | 85 | TARMAC: EC seguida de Docetaxel + Carboplatin em mulheres com TNBC na Nigéria; avaliação de resposta patológica completa e marcadores ômicos de resistência |
| [NCT00117442](https://clinicaltrials.gov/study/NCT00117442) | Phase 2 | Concluído | 61 | Carboplatin/Paclitaxel dose-intensivo com suporte de pegfilgrastim e reinfusão de progenitores em câncer de mama; dados de eficácia e cinética da combinação platina-taxano |
| [NCT04771871](https://clinicaltrials.gov/study/NCT04771871) | Phase 2 | Desconhecido | 42 | TNBC recebendo quimioterapia padrão incluindo Carboplatin; perfis de microRNA como biomarcadores de resposta e resistência ao tratamento |
| [NCT05843292](https://clinicaltrials.gov/study/NCT05843292) | Phase 4 | Ainda não recrutando | 48 | Sintilimab de curto prazo + Taxane + Carboplatin como neoadjuvante em TNBC precoce; exploração de imunoterapia combinada ao backbone platina-taxano |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [39671272](https://pubmed.ncbi.nlm.nih.gov/39671272/) | 2025 | RCT (Phase 3) | JAMA | CamRelief: Camrelizumab (anti-PD-1) + quimioterapia padrão (antraciclina + ciclofosfamida + taxano + platina) em TNBC neoadjuvante precoce/localmente avançado; bloqueio PD-1 melhora eficácia do esquema contendo Carboplatin |
| [40593759](https://pubmed.ncbi.nlm.nih.gov/40593759/) | 2025 | RCT (Phase 2b) | Nature Communications | MUKDEN 06: ARX788 + Pyrotinib vs. TCbHP (docetaxel, carboplatin, trastuzumab, pertuzumab) neoadjuvante em HER2+; valida TCbHP como braço de controle padrão de referência |
| [38309017](https://pubmed.ncbi.nlm.nih.gov/38309017/) | 2024 | RCT (Phase 3) | European Journal of Cancer | BROCADE3 — resultados finais de sobrevida global: Veliparib + Carboplatin + Paclitaxel vs. placebo + Carboplatin + Paclitaxel em BRCA1/2-mutado HER2-negativo avançado; melhora em PFS mas não OS; confirma Carboplatin como backbone na população BRCA-mutada |
| [16720915](https://pubmed.ncbi.nlm.nih.gov/16720915/) | 2006 | Revisão Sistemática | Medical Oncology | Revisão abrangente de sinergismo, eficácia e segurança de Paclitaxel-Carboplatin em câncer de mama avançado; evidência de sinergismo pré-clínico e atividade clínica em múltiplas linhas |
| [25247558](https://pubmed.ncbi.nlm.nih.gov/25247558/) | 2014 | Meta-análise | PLoS ONE | Meta-análise demonstrando que Carboplatin melhora significativamente a taxa de resposta patológica completa (pCR) no tratamento neoadjuvante de TNBC; suporte quantitativo para incorporação rotineira |
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Phase 2 RCT | Breast Cancer Research | Carboplatin + Gemcitabina + Mifepristone em câncer de mama e ovário avançado; demonstra que antagonismo do receptor de glicocorticoide (GR) pode potencializar citotoxicidade do Carboplatin em tumores GR-positivos |
| [33256829](https://pubmed.ncbi.nlm.nih.gov/33256829/) | 2020 | Phase 2 Trial | Breast Cancer Research | Bevacizumab + Carboplatin em pacientes com metástases cerebrais de câncer de mama; evidência de atividade em nicho de difícil tratamento com segurança manejável |
| [40817986](https://pubmed.ncbi.nlm.nih.gov/40817986/) | 2025 | Phase 2 RCT | Breast Cancer Research | Carboplatin vs. Carboplatin + Everolimus em TNBC avançado; avaliação do papel da via mTOR na sensibilização ao Carboplatin em tumores com perda de PTEN |
| [39944694](https://pubmed.ncbi.nlm.nih.gov/39944694/) | 2025 | Estudo de Coorte Genômica | Frontiers in Immunology | Assinatura prognóstica de genes de reparo do DNA (DDR) associados à resistência ao Carboplatin; correlação com infiltração imune e sensibilidade farmacológica em câncer de mama |
| [8893899](https://pubmed.ncbi.nlm.nih.gov/8893899/) | 1996 | Série Clínica (Phase 2) | Seminars in Oncology | Avaliação histórica da atividade de Paclitaxel, Carboplatin e sua combinação em câncer de mama avançado; dados fundadores que estabeleceram a rationale para o desenvolvimento da combinação platina-taxano |

---

## Informações de Comercialização no Brasil

O Carboplatin está comercializado no Brasil com **20 registros ativos** confirmados. As informações detalhadas sobre nomes comerciais, formas farmacêuticas, fabricantes e indicações aprovadas para cada produto não estão disponíveis no pacote de evidências atual (todos os campos de registro retornaram em branco). Recomenda-se consulta direta ao banco de dados da ANVISA — Consulta de Medicamentos — para obtenção da listagem completa dos produtos registrados e respectivas bulas.

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Citotóxico convencional — agente alquilante à base de platina (Platinum Compound / Platinante de 2ª geração) |
| Risco de Mielossupressão | **Alto** — trombocitopenia é a toxicidade dose-limitante característica do Carboplatin (nadir plaquetário esperado nos dias 21–28); leucopenia e anemia são frequentes e podem requerer suporte transfusional ou uso de fatores de crescimento |
| Classificação de Emetogenicidade | **Moderada a Alta** — classificado como agente de alto potencial emetogênico em doses padrão (AUC ≥ 4); exige pré-medicação antiemética profilática com antagonistas de 5-HT3 ± dexametasona ± antagonista NK1 |
| Itens de Monitoramento | Hemograma completo com diferencial (antes de cada ciclo), creatinina sérica e clearance de creatinina — indispensável para cálculo de dose individualizada pela **fórmula de Calvert** (Dose = AUC × [ClCr + 25]), função hepática |
| Proteção no Manuseio | Obrigatório seguir regulamentos de manuseio de citotóxicos: uso de EPIs adequados (luvas duplas, óculos de proteção, avental impermeável), preparo em câmara de fluxo laminar vertical, descarte de resíduos conforme RDC ANVISA vigente |

---

## Considerações de Segurança

Consulte a bula para informações de segurança. Os dados de advertências e contraindicações não estão disponíveis no pacote de evidências atual (identificados como lacuna de dados de severidade alta — DG001). Recomenda-se obtenção da bula aprovada pela ANVISA antes de qualquer aplicação clínica ou análise regulatória.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
O Carboplatin possui evidência de Nível L1 para carcinoma de mama feminino, sustentada por múltiplos ensaios clínicos de Phase 3 concluídos com centenas a quase mil pacientes (GeparOcto: 961; NCT03168880: 720; NCT02003209: 315; NCT00047255: 263), meta-análise e revisão sistemática corroborando o uso nos subtipos TNBC e HER2-positivo. O esquema TCH já integra diretrizes NCCN e o Carboplatin neoadjuvante em TNBC é prática clínica estabelecida — esta previsão do TxGNN reflete, portanto, uma realidade já incorporada na oncologia clínica, e não uma extrapolação especulativa.

**Para prosseguir, é necessário:**
- Obtenção da bula ANVISA completa para preenchimento das lacunas de segurança (advertências, contraindicações e instruções de uso)
- Levantamento de interações medicamentosas (DDI) para a população-alvo, especialmente em combinações com trastuzumab, pertuzumab e inibidores de PARP
- Confirmação do mecanismo de ação formal via DrugBank API (DG002) para formalização da análise de relacionamento mecanístico
- Especificação dos subtipos de mama elegíveis para uso prioritário: TNBC neoadjuvante, HER2-positivo (esquema TCH/TCHP), portadoras de mutação BRCA — cada subpopulação requer guardrail clínica própria
- Verificação da função renal de base dos pacientes para cálculo individualizado de dose pela fórmula de Calvert (ClCr obrigatório)
- Recuperação dos dados detalhados dos 20 registros ANVISA para confirmação de indicações aprovadas, formas farmacêuticas disponíveis e restrições de uso no contexto brasileiro
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

