---
layout: default
title: Pibrentasvir
parent: 僅模型預測 (L5)
nav_order: 397
evidence_level: L5
indication_count: 10
---

# Pibrentasvir
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

# Pibrentasvir: Da Hepatite C à Infecção pelo Vírus da Hepatite B

## Resumo em Uma Frase

Pibrentasvir é um inibidor de NS5A do vírus da hepatite C (HCV), comercializado em combinação com glecaprevir (Maviret®) para o tratamento da hepatite C crônica genótipos 1 a 6.
O modelo TxGNN prevê que pode ser eficaz para **Infecção pelo Vírus da Hepatite B (Hepatitis B Virus Infection)**, com **14 ensaios clínicos** e **20 publicações** indexadas levantadas como base de evidências — contudo, todos os estudos existentes abordam o tratamento do HCV, não do HBV, sendo a previsão mecanisticamente frágil.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hepatite C crônica (genótipos 1–6) |
| Nova Indicação Prevista | Infecção pelo Vírus da Hepatite B (Hepatitis B Virus Infection) |
| Pontuação de Previsão TxGNN | 99,84% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Pibrentasvir é um inibidor pan-genotípico da proteína não estrutural NS5A do HCV. Essa proteína atua como plataforma de montagem do complexo de replicação viral — sem atividade enzimática própria, mas essencial para organizar as proteínas do complexo replicase. Pibrentasvir liga-se à NS5A com alta afinidade e potência picomolar, bloqueando sua função e impedindo a produção de novos vírus em todos os genótipos do HCV (GT1 a GT6). Em combinação com glecaprevir (inibidor de NS3/4A protease), alcança taxas de resposta virológica sustentada (SVR12) superiores a 97% em oito semanas de tratamento.

O obstáculo mecanístico para o HBV é fundamental: o HBV **não possui a proteína NS5A nem qualquer estrutura homóloga**. O HBV é um vírus de DNA de cadeia parcialmente dupla (hepadnavírus), que se replica por transcrição reversa a partir de um RNA pré-genômico intermediário, dependendo exclusivamente da sua própria DNA polimerase com atividade de transcriptase reversa. Este mecanismo é radicalmente diferente do HCV (flavivírus de RNA de cadeia simples positiva). Portanto, pibrentasvir não possui alvo biológico conhecido no ciclo replicativo do HBV.

A alta pontuação TxGNN (99,84%) reflete, provavelmente, a conectividade do grafo de conhecimento entre nós biológicos compartilhados de "hepatite viral" — HBV e HCV compartilham o órgão-alvo hepático, vias de lesão imunomediada e contextos epidemiológicos de co-infecção — e não uma relação farmacológica direta. Um dado clinicamente revelador aponta na direção oposta: nos ensaios de GLE/PIB para HCV, a **reativação do HBV** foi identificada como preocupação de **segurança** em pacientes co-infectados, reforçando que a relação entre pibrentasvir e HBV é de risco a monitorar, não de eficácia terapêutica a explorar.

---

## Evidências de Ensaios Clínicos

> ⚠️ **Nota importante**: Todos os ensaios abaixo foram desenhados para HCV (hepatite C), não para HBV. A relevância ao HBV é indireta — alguns estudos incluem pacientes co-infectados HBV/HCV e monitoram parâmetros de segurança do HBV como desfecho secundário ou de vigilância.

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02243293](https://clinicaltrials.gov/study/NCT02243293) | Phase 2/3 | Concluído | 694 | SURVEYOR-II: GLE/PIB ± ribavirina em HCV genótipos 2–6 com e sem cirrose; maior amostra disponível, possível subgrupo HBV/HCV com dados de segurança |
| [NCT02640157](https://clinicaltrials.gov/study/NCT02640157) | Phase 3 | Concluído | 506 | ENDURANCE-3: GLE/PIB vs sofosbuvir + daclatasvir em HCV GT3; pode conter monitoramento de reativação de HBV |
| [NCT02441283](https://clinicaltrials.gov/study/NCT02441283) | Phase 2/3 | Concluído | 384 | Follow-up de longo prazo avaliando durabilidade da SVR, persistência de resistência a DAA e desfechos clínicos |
| [NCT02640482](https://clinicaltrials.gov/study/NCT02640482) | Phase 3 | Concluído | 304 | ENDURANCE-2: GLE/PIB duplo-cego vs placebo em HCV GT2 |
| [NCT02707952](https://clinicaltrials.gov/study/NCT02707952) | Phase 3 | Concluído | 295 | CERTAIN-1: GLE/PIB em adultos japoneses com HCV, naïve e experientes a DAA |
| [NCT02723084](https://clinicaltrials.gov/study/NCT02723084) | Phase 3 | Concluído | 136 | CERTAIN-2: GLE/PIB vs sofosbuvir + ribavirina em HCV GT2 no Japão |
| [NCT02446717](https://clinicaltrials.gov/study/NCT02446717) | Phase 2/3 | Concluído | 141 | GLE/PIB ± ribavirina em pacientes com falha terapêutica prévia a DAA |
| [NCT03219216](https://clinicaltrials.gov/study/NCT03219216) | Phase 3 | Concluído | 100 | GLE/PIB em adultos no Brasil com HCV GT1–6, naïve, com e sem cirrose compensada |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Concluído | 87 | Risco cardiovascular após erradicação de HCV em mono-infectados e co-infectados HIV; background de hepatite viral relevante |
| [NCT01995071](https://clinicaltrials.gov/study/NCT01995071) | Phase 2 | Concluído | 89 | Estudo dose-ranging de ABT-493 e ABT-530 em HCV GT1; dados iniciais de PK e segurança do componente PIB |

---

## Evidências da Literatura

> ⚠️ **Nota**: A maioria das publicações aborda GLE/PIB exclusivamente no contexto do HCV. Os estudos marcados com ★ possuem menção direta ao HBV.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [29485084](https://pubmed.ncbi.nlm.nih.gov/29485084/) ★ | 2018 | Comentário | Lancet Infect Dis | Vacinação contra HBV após tratamento de HCV: alerta sobre risco de reativação do HBV em pacientes tratados com DAA — relação com HBV como preocupação de segurança, não de eficácia |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) ★ | 2021 | Revisão | World J Gastroenterol | Avanços e desafios no manejo de hepatite viral pediátrica (HBV e HCV); descreve DAA disponíveis para crianças e expectativas para tratamento de HBV |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) ★ | 2025 | Coorte Retrospectiva | Klin Mikrobiol Infekc Lek | Avaliação retrospectiva de eficácia e tolerância do tratamento antiviral de hepatite B e C crônicas em crianças em Ostrava |
| [31981264](https://pubmed.ncbi.nlm.nih.gov/31981264/) | 2020 | Coorte Prospectiva | J Viral Hepatitis | GLE/PIB em 108 pacientes com HCV e doença renal crônica grave (estágio 4–5) em Taiwan; alta SVR e boa tolerabilidade |
| [31284039](https://pubmed.ncbi.nlm.nih.gov/31284039/) | 2019 | Meta-análise | Int J Antimicrob Agents | Revisão sistemática e meta-análise de GLE/PIB em HCV GT1–6: SVR12 global de 97,8% em 3.082 pacientes (13 estudos) |
| [30982721](https://pubmed.ncbi.nlm.nih.gov/30982721/) | 2019 | Revisão | Lancet Gastroenterol Hepatol | HCV em crianças e adolescentes; regimes curativos orais de curta duração transformam o tratamento |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Revisão | Semin Liver Dis | Retratamento de HCV após falha a DAA; estratégias e desfechos para pacientes com resposta inadequada |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Revisão | Clin Pharmacokinet | Considerações farmacocinéticas e farmacodinâmicas na terapia de HCV em 2019; cobre GLE/PIB em populações especiais |
| [35431505](https://pubmed.ncbi.nlm.nih.gov/35431505/) | 2022 | Coorte Real-World | World J Gastroenterol | Eficácia de DAA em pacientes HIV/HCV co-infectados com genótipo 6 em Taiwan; dados de uso prático |
| [31129632](https://pubmed.ncbi.nlm.nih.gov/31129632/) | 2019 | Relato de Caso | BMJ Case Reports | Lesão hepática aguda associada a GLE/PIB em HCV sem cirrose e sem co-infecção HBV — alerta de hepatotoxicidade rara |

---

## Informações de Comercialização no Brasil

O fármaco consta como **comercializado** no Brasil com 1 registro ANVISA. Os detalhes individuais do registro (número, nome comercial, forma farmacêutica e texto da indicação aprovada) não estão disponíveis nos dados de entrada deste pacote.

> Pibrentasvir é comercializado no Brasil como parte da combinação fixa **glecaprevir 100 mg / pibrentasvir 40 mg (Maviret®)**, indicada para hepatite C crônica genótipos 1 a 6 em adultos e adolescentes a partir de 12 anos.

---

## Considerações de Segurança

**Alerta Clínico — Reativação do HBV:** Em ensaios clínicos e na prática real com GLE/PIB para tratamento do HCV, foi documentada reativação do vírus da hepatite B em pacientes com co-infecção HBV/HCV. Agências regulatórias (FDA, EMA) incluíram esse risco nas bulas do produto com recomendação de triagem de HBsAg, Anti-HBc e Anti-HBs antes do início do tratamento e monitoramento durante e após o uso. Este dado reforça que a interação clínica entre pibrentasvir e HBV é uma **preocupação de segurança estabelecida**, não um sinal de eficácia.

Consulte a bula para a lista completa de advertências, contraindicações e interações medicamentosas.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Pibrentasvir inibe a proteína NS5A, exclusiva do HCV, que não possui equivalente funcional ou estrutural no HBV. O HBV replica-se por mecanismo completamente diferente (DNA polimerase/transcriptase reversa), sem alvo farmacológico conhecido para este inibidor. Os 14 ensaios clínicos e 20 publicações identificados são estudos de HCV — nenhum foi desenhado para testar pibrentasvir como tratamento de HBV — e a pontuação elevada do TxGNN é interpretada como artefato de conectividade do grafo de conhecimento entre nós de "hepatite viral", não como sinal biológico acionável.

**Para prosseguir, seria necessário:**
- Dados de triagem in vitro de pibrentasvir contra replicação do HBV (ensaio de carga viral HBV DNA em linhagens celulares infectadas)
- Análise de modelagem estrutural (docking molecular) comparando o bolsão de ligação da NS5A do HCV com proteínas do HBV que possam compartilhar similaridade tridimensional
- Identificação de qualquer subgrupo nos ensaios GLE/PIB existentes com dados de resposta virológica do HBV (carga viral HBV DNA antes e depois do tratamento) em pacientes HBV/HCV co-infectados
- Protocolo de Fase 1 específico para HBV apenas após confirmação de pelo menos um dos pontos acima
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

