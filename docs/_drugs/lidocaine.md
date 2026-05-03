---
layout: default
title: Lidocaine
parent: 僅模型預測 (L5)
nav_order: 323
evidence_level: L5
indication_count: 10
---

# Lidocaine
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

# Lidocaína: De Anestésico Local a Distúrbio Conjuntival

## Resumo em Uma Frase

Lidocaína é um anestésico local e antiarrítmico de classe IB amplamente utilizado em procedimentos cirúrgicos, bloqueios nervosos regionais e manejo de arritmias ventriculares refratárias.
O modelo TxGNN prevê que pode ser eficaz para **Distúrbio Conjuntival (Conjunctival Disorder)** — indicação com mecanismo de ação diretamente aplicável ao segmento ocular anterior —, atualmente com **17 ensaios clínicos** e **20 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anestesia local e regional; arritmia ventricular |
| Nova Indicação Prevista | Distúrbio Conjuntival (Conjunctival Disorder) |
| Pontuação de Previsão TxGNN | 99.84% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | Não localizado no sistema ANVISA (verificação manual recomendada) |
| Número de Registros | 0 (não encontrado no sistema) |
| Decisão Recomendada | Proceed with Guardrails |

> **Nota sobre a previsão TxGNN:** A indicação com maior pontuação absoluta no modelo é *punctate epithelial keratoconjunctivitis* (99.99%, rank 1), porém sem qualquer evidência clínica ou laboratorial identificada (L5, Hold). A indicação *Conjunctival Disorder* (rank 6) apresenta a melhor combinação de pontuação e evidências, sendo adotada como foco deste relatório.

---

## Por que Esta Previsão é Razoável?

Atualmente não há dados detalhados sobre o mecanismo de ação extraídos do DrugBank para este ciclo de análise. Com base no conhecimento farmacológico estabelecido, a lidocaína é um bloqueador de canais de sódio voltagem-dependentes (Nav1.x) da classe aminoamida. Ao se ligar ao estado inativado do canal, impede a geração e propagação de potenciais de ação em fibras nervosas sensitivas e motoras. Sistemicamente, esse mecanismo confere também propriedades antiarrítmicas (classe IB) e anti-inflamatórias mediadas pela supressão da atividade ectópica neuronal.

A relação entre lidocaína e distúrbios conjuntivais não é especulativa: trata-se de uma aplicação **clinicamente estabelecida**. A lidocaína tópica em gel 2% ou colírio é utilizada rotineiramente como anestésico padrão em cirurgias conjuntivais — excisão de pterígio, injeções intravítreas, trabeculectomia e vitrectomia posterior —, agindo diretamente sobre as terminações nervosas do epitélio conjuntival e escleral. O TxGNN reconhece essa ligação estrutural no grafo de conhecimento ao associar o composto à entidade anatômica "conjunctiva".

Adicionalmente, há uma segunda via mecanística relevante: na síndrome SUNCT/SUNA (*Short-lasting Unilateral Neuralgiform headache attacks with Conjunctival injection and Tearing*), a lidocaína intravenosa é empregada para interromper a cascata trigeminal-autonômica que produz, como sintoma cardinal, injeção conjuntival e lacrimejamento ipsilateral. Ensaios prospectivos e meta-análises (PMID 33361408) documentam essa eficácia. A convergência dessas duas vias — anestesia tópica local e bloqueio central trigeminal — explica por que o modelo TxGNN associa consistentemente a lidocaína a múltiplas entidades conjuntivais entre as previsões de rank mais alto.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT05978687](https://clinicaltrials.gov/study/NCT05978687) | Phase 4 | Concluído | 41 | Comparação entre gel de lidocaína tópico (*Ophtesic*) e injeção subconjuntival de xilocaína em excisão de pterígio; gel oferece contato superficial prolongado e proteção contra dessecação corneana |
| [NCT02324166](https://clinicaltrials.gov/study/NCT02324166) | Phase 4 | Desconhecido | 54 | Solução combinada cefazolina-lidocaína para reduzir dor associada à profilaxia antibiótica subconjuntival em cirurgia vítreo-retiniana |
| [NCT01087489](https://clinicaltrials.gov/study/NCT01087489) | N/A | Concluído | 53 | Comparação de dois protocolos anestésicos (swabs com lidocaína 4% em gotas vs gel lidocaína HCl 3,5%) para injeções intravítreas; avaliação de conforto na região conjuntival |
| [NCT02150460](https://clinicaltrials.gov/study/NCT02150460) | Phase 4 | Concluído | 100 | ECR duplo-cego de bloqueio peribulbar com lidocaína (1 vs 2 sítios de injeção) em cirurgia de catarata em pacientes nigerianos; eficácia e segurança anestésica ocular |
| [NCT03397069](https://clinicaltrials.gov/study/NCT03397069) | N/A | Concluído | 90 | Adição de midazolam à lidocaína em bloqueio peribulbar para cirurgia de catarata; avaliação de duração da ação anestésica |
| [NCT03189329](https://clinicaltrials.gov/study/NCT03189329) | Phase 4 | Concluído | 66 | Bloqueio retrobulbar com lidocaína 2% vs levobupivacaína 0,5% em cirurgia vítreo-retiniana; impacto sobre saturação cerebral de O₂ e funções cognitivas pós-operatórias em idosos |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [18989343](https://pubmed.ncbi.nlm.nih.gov/18989343/) | 2009 | ECR | Eye (London) | ECR comparando gel de lidocaína 2% vs tetracaína 1% em cirurgia primária de pterígio; lidocaína gel demonstrou eficácia anestésica equivalente como agente tópico único |
| [15799734](https://pubmed.ncbi.nlm.nih.gov/15799734/) | 2005 | Estudo clínico | Acta Ophthalmol Scand | Gel de lidocaína 2% como anestésico tópico eficaz em cirurgia de pterígio, eliminando necessidade de injeção subconjuntival |
| [16954710](https://pubmed.ncbi.nlm.nih.gov/16954710/) | 2006 | Estudo clínico | Ophthalmologica | Gel de lidocaína 2% (viscosa) reduz significativamente a dor pós-operatória após cirurgia de pterígio |
| [23330822](https://pubmed.ncbi.nlm.nih.gov/23330822/) | 2013 | Estudo clínico | Current Eye Research | Avaliação de diferentes anestésicos tópicos (incluindo lidocaína) e anti-inflamatórios em injeções intravítreas; impacto sobre dor ocular peri-procedimento |
| [10696746](https://pubmed.ncbi.nlm.nih.gov/10696746/) | 2000 | Estudo clínico | Retina | Anestesia tópica com lidocaína como alternativa eficaz à anestesia peribulbar/retrobulbar em vitrectomia posterior |
| [33361408](https://pubmed.ncbi.nlm.nih.gov/33361408/) | 2021 | Prospectivo + meta-análise | J Neurol Neurosurg Psychiatry | Lidocaína IV como opção terapêutica em SUNCT/SUNA (síndrome cujo sintoma cardinal é injeção conjuntival); estudo prospectivo com meta-análise de braço único |
| [34003160](https://pubmed.ncbi.nlm.nih.gov/34003160/) | 2021 | Review | Neurology India | Revisão atualizada de SUNCT/SUNA: papel da lidocaína IV no manejo das crises com injeção conjuntival e lacrimejamento |
| [38415675](https://pubmed.ncbi.nlm.nih.gov/38415675/) | 2024 | Review | Cephalalgia | Atualização sobre SUNHA 2024: lidocaína entre as abordagens terapêuticas para crises com sintomas conjuntivais; debate sobre evidências atuais |
| [21876597](https://pubmed.ncbi.nlm.nih.gov/21876597/) | 2011 | Case series | NEPJOPH | Oftalmomíase humana: lidocaína tópica utilizada na imobilização e remoção de larvas com envolvimento periocular e conjuntival |
| [19250287](https://pubmed.ncbi.nlm.nih.gov/19250287/) | 2009 | Review / Case series | Cephalalgia | Efeitos colaterais neuropsiquiátricos da lidocaína no tratamento de cefaleia refratária; série de 20 pacientes e revisão sistemática |

---

## Informações de Comercialização no Brasil

Nenhum registro foi localizado no sistema ANVISA para Lidocaína neste ciclo de consulta (data de corte: 2026-04-20). Este resultado é inesperado dado o amplo uso clínico e a longa história regulatória do fármaco. Recomenda-se verificação direta no portal da ANVISA (consulta.anvisa.gov.br) para confirmar o status atual dos registros.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
A utilização de lidocaína em distúrbios conjuntivais não configura reposicionamento especulativo: múltiplos ensaios de Fase 4 já completados documentam o uso direto do fármaco em cirurgias conjuntivais, e estudos clínicos prospectivos demonstram eficácia no tratamento de SUNCT/SUNA, condição que tem injeção conjuntival como critério diagnóstico. A previsão TxGNN reflete, portanto, uma aplicação clinicamente estabelecida que carece de indicação formal registrada — cenário favorável para extensão de indicação ou posicionamento de produto dedicado.

**Para prosseguir, é necessário:**
- Confirmar registros ANVISA atualizados com consulta direta ao portal da Agência (discrepância entre uso clínico estabelecido e zero registros no sistema)
- Obter bula completa (PDF ANVISA) para extração de advertências, contraindicações e interações medicamentosas
- Definir qual subtipo específico de "distúrbio conjuntival" representa a maior oportunidade terapêutica não atendida (pterígio, anestesia para injeções intravítreas, SUNCT/SUNA)
- Avaliar viabilidade regulatória de extensão formal de indicação com base nos dados de Fase 4 existentes
- Mapear formulações oftálmicas de lidocaína disponíveis no mercado brasileiro (gel, colírio, solução injetável subconjuntival)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

