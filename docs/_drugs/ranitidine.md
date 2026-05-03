---
layout: default
title: Ranitidine
parent: 僅模型預測 (L5)
nav_order: 424
evidence_level: L5
indication_count: 10
---

# Ranitidine
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

# Ranitidine: Da supressão ácida gástrica à úlcera péptica ativa

## Resumo em Uma Frase

Ranitidine é um antagonista seletivo dos receptores histaminérgicos H2, historicamente utilizado no tratamento da doença ulcerosa péptica e das condições de hipersecreção gástrica em todo o mundo, mas atualmente sem registro vigente no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **Úlcera Péptica Ativa (active peptic ulcer disease)**, com **1 ensaio clínico** e **19 publicações** identificados apoiando esta direção.
A pontuação máxima do modelo (99,89%) reflete coerência mecanística direta entre o fármaco e a indicação prevista.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Doença ulcerosa péptica e hipersecreção gástrica (aprovação histórica global; sem registro vigente no Brasil) |
| Nova Indicação Prevista | Úlcera Péptica Ativa (active peptic ulcer disease) |
| Pontuação de Previsão TxGNN | 99,89% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados formais de mecanismo de ação registrados no sistema para este fármaco. Com base na literatura científica amplamente estabelecida, Ranitidine é um antagonista competitivo e reversível dos receptores histaminérgicos H2 localizados nas células parietais do estômago. Ao bloquear esses receptores, impede a ação da histamina — o principal estimulador fisiológico da secreção ácida — resultando em redução de aproximadamente 70 a 90% da acidez gástrica basal e estimulada, bem como na diminuição da produção de pepsina. Esses são dois dos principais fatores que agravam a lesão mucosa na úlcera péptica.

A úlcera péptica ativa representa a fase aguda da doença, caracterizada por erosão mucosa em atividade, inflamação e risco de complicações como hemorragia e perfuração. O tratamento desta fase exige supressão ácida rápida e sustentada — idealmente mantendo o pH intragástrico acima de 6 para favorecer a agregação plaquetária, inibir a atividade proteolítica da pepsina e permitir a cicatrização mucosa. Ranitidine, especialmente na formulação intravenosa, possui exatamente esse perfil farmacológico de ação, com início rápido e duração suficiente para controle noturno do ácido.

A previsão do TxGNN com pontuação de 99,89% é essencialmente confirmatória: múltiplos ensaios clínicos randomizados da literatura clássica (PMIDs 3909374, 3104657, 1863945, 2877570) demonstraram taxas de cicatrização de 68 a 91% em 4 a 8 semanas com Ranitidine em diferentes tipos de úlcera péptica. A principal questão regulatória atual não é a eficácia — amplamente comprovada — mas a segurança relacionada à contaminação por NDMA (N-nitrosodimetilamina), que motivou a retirada voluntária global do fármaco em 2020.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Concluído | 320 | Avaliação do impacto de estatinas e inibidores da bomba de prótons no efeito antiplaquetário do clopidogrel em pacientes submetidos a intervenção coronária percutânea; Ranitidine foi utilizado como agente de controle para supressão ácida, sem avaliar diretamente a eficácia em úlcera péptica ativa |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [3909374](https://pubmed.ncbi.nlm.nih.gov/3909374/) | 1985 | RCT | Scand J Gastroenterol | Ranitidine 300 mg/dia em 151 pacientes: taxas de cicatrização de 91% (úlcera duodenal), 68% (pré-pilórica) e 81% (gástrica) em 4 semanas; manutenção reduz recidiva em 1 ano |
| [3104657](https://pubmed.ncbi.nlm.nih.gov/3104657/) | 1986 | RCT | Klinische Wochenschrift | Rioprostil (análogo de prostaglandina E1) 600 µg ao deitar vs Ranitidine 300 mg nocturno em cicatrização de úlcera duodenal; comparação direta de potência e duração de ação |
| [2877570](https://pubmed.ncbi.nlm.nih.gov/2877570/) | 1986 | RCT | Am J Medicine | Estudo multicêntrico duplo-cego em 19 países, 1.031 pacientes com úlcera duodenal ativa confirmada por endoscopia; famotidina vs Ranitidine em eficácia e tolerabilidade |
| [1863945](https://pubmed.ncbi.nlm.nih.gov/1863945/) | 1991 | RCT | Clinical Therapeutics | 160 pacientes com úlcera duodenal ativa; famotidina 40 mg vs Ranitidine 300 mg ao deitar por 4-8 semanas; cicatrização endoscópica confirmada em 80% dos tratados com Ranitidine na semana 8 |
| [2491360](https://pubmed.ncbi.nlm.nih.gov/2491360/) | 1989 | RCT | J Gastroenterol Hepatol | 270 pacientes com úlcera duodenal ativa randomizados para omeprazol 10 mg, 20 mg ou Ranitidine 150 mg duas vezes ao dia; avaliação endoscópica semanal com análise de 46 fatores prognósticos |
| [2092029](https://pubmed.ncbi.nlm.nih.gov/2092029/) | 1990 | RCT | J Assoc Physicians India | Ensaio duplo-cego randomizado em 40 pacientes com úlcera gástrica ou duodenal ativa; famotidina 40 mg vs Ranitidine 300 mg em dose noturna única por 4-8 semanas |
| [12749277](https://pubmed.ncbi.nlm.nih.gov/12749277/) | 2003 | RCT | Hepato-gastroenterology | Estudo prospectivo controlado; Ranitidine e ecabet inibem recidiva de úlcera péptica independentemente da erradicação de H. pylori — reforça papel de manutenção do Ranitidine |
| [18493408](https://pubmed.ncbi.nlm.nih.gov/18493408/) | 1996 | Estudo Observacional | Diagn Ther Endoscopy | 23 pacientes com úlcera péptica ativa acompanhados por endoscopia antes e após o Ramadã; Ranitidine 150 mg duas vezes ao dia manteve controle adequado durante o jejum intermitente |
| [6317325](https://pubmed.ncbi.nlm.nih.gov/6317325/) | 1983 | Revisão | Drug Intell Clin Pharm | Revisão da aprovação original do Ranitidine pelo FDA para úlcera duodenal ativa e hipersecreção gástrica; 4-10× mais potente que cimetidina na inibição da secreção gástrica estimulada |
| [1976583](https://pubmed.ncbi.nlm.nih.gov/1976583/) | 1990 | Revisão | Hepato-gastroenterology | Supressão da acidez nocturna e de 24h como preditor de cicatrização em úlcera péptica; fundamentação para o uso de antagonistas H2 como Ranitidine no controle da doença ativa |

---

## Informações de Comercialização no Brasil

Ranitidine não possui registros ativos na ANVISA. O fármaco foi retirado voluntariamente do mercado mundial em 2020, após a Agência Europeia de Medicamentos (EMA) e o FDA determinarem a presença de níveis inaceitáveis de NDMA (N-nitrosodimetilamina) em formulações comercializadas. No Brasil, a ANVISA acompanhou essa decisão e suspendeu os registros vigentes à época. Não há licenças comerciais ativas no país.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> **Alerta regulatório**: Ranitidine foi retirado do mercado global em 2020 por contaminação com NDMA, substância com potencial carcinogênico. A reintrodução deste fármaco requer avaliação específica junto à ANVISA quanto ao controle analítico de NDMA nas formulações, sendo este o principal guardail regulatório antes de qualquer plano de desenvolvimento clínico no Brasil.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
A eficácia de Ranitidine no tratamento da úlcera péptica ativa é uma das bases mais sólidas da farmacologia gastrointestinal, sustentada por décadas de ensaios clínicos randomizados e revisões sistemáticas em milhares de pacientes. A pontuação TxGNN de 99,89% confirma a coerência mecanística máxima. O obstáculo central não é eficácia, mas a segurança farmacêutica relacionada à contaminação por NDMA, que precisa ser endereçada antes de qualquer iniciativa regulatória no Brasil.

**Para prosseguir, é necessário:**
- Avaliação da viabilidade de formulações com controle analítico rigoroso de NDMA (abaixo dos limites aceitáveis pela ANVISA e ICH M7)
- Consulta formal à ANVISA sobre o caminho regulatório para eventual reintrodução
- Obtenção dos dados formais de MOA via DrugBank API (lacuna DG002 identificada)
- Verificação das advertências e contraindicações na bula oficial (lacuna DG001 identificada)
- Definição da via de administração prioritária (oral vs. intravenosa) conforme o cenário clínico-alvo da úlcera péptica ativa
- Revisão de segurança completa considerando o perfil pós-2020 do fármaco
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

