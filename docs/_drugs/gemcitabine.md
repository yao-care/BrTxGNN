---
layout: default
title: Gemcitabine
parent: 僅模型預測 (L5)
nav_order: 264
evidence_level: L5
indication_count: 10
---

# Gemcitabine
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

# Gemcitabine: Do câncer pancreático ao carcinoma de mama feminino

## Resumo em Uma Frase

Gemcitabine é um análogo de nucleosídeo citotóxico (antimetabólito), amplamente reconhecido como quimioterapia de referência para cânceres pancreático e pulmonar em âmbito internacional.
O modelo TxGNN prevê que pode ser eficaz para **Carcinoma de Mama Feminino (Female Breast Carcinoma)**,
atualmente com **mais de 50 ensaios clínicos** e **20 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Câncer pancreático e câncer de pulmão (reconhecidos internacionalmente; sem registros no Brasil neste banco de dados) |
| Nova Indicação Prevista | Carcinoma de Mama Feminino (Female Breast Carcinoma) |
| Pontuação de Previsão TxGNN | 99.98% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✗ Não comercializado (sem registros ANVISA no banco de dados atual) |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Gemcitabine é um análogo de nucleosídeo da classe dos antimetabólitos que atua em dois mecanismos coordenados: incorpora-se à cadeia de DNA em síntese na fase S do ciclo celular e inibe a enzima ribonucleotídeo redutase (RRM2), reduzindo o pool intracelular de dCTP necessário para replicação. Este duplo bloqueio é especialmente eficaz em tumores com alta taxa proliferativa. O transportador hENT1 (human equilibrative nucleoside transporter 1) regula a captação celular do fármaco e emerge como biomarcador preditivo de resposta, relevante para estratificação de pacientes.

O carcinoma de mama feminino, em particular os subtipos Triplo-Negativo (TNBC) e hormônio-receptor-negativo (HR-), compartilha com o câncer pancreático a dependência crítica da fase S do ciclo celular para proliferação, tornando ambos os tumores sensíveis à inibição da síntese de DNA. No câncer de mama, Gemcitabine demonstrou sinergia comprovada com taxanos (paclitaxel, nab-paclitaxel, docetaxel), cujos mecanismos complementares — estabilização de microtúbulos — potencializam o efeito antiproliferativo. A combinação Gemcitabine + Paclitaxel recebeu aprovação da FDA em 2004 especificamente para câncer de mama metastático, consolidando a base regulatória internacional da indicação.

Adicionalmente, evidências emergentes sugerem que ALDH1A1, um marcador de células-tronco tumorais em câncer de mama, promove progressão tumoral por remodulação de células supressoras derivadas de mielócitos (MDSCs), e que Gemcitabine pode exercer efeito imunomodulador parcial nesse contexto. A convergência de múltiplos ensaios clínicos de Fase 3, a aprovação em mercados internacionais e os dados mecanísticos robustos justificam plenamente a previsão do modelo TxGNN.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00039546](https://clinicaltrials.gov/study/NCT00039546) | Phase 3 | Desconhecido | N/A | tAnGo RCT: compara Paclitaxel/Epirrubicina/Ciclofosfamida ± Gemcitabine como quimioterapia adjuvante em câncer de mama ER/PgR-pobre de estágio inicial |
| [NCT00561119](https://clinicaltrials.gov/study/NCT00561119) | Phase 3 | Concluído | 326 | Manutenção com Gemcitabine + Paclitaxel vs observação após resposta clínica em câncer de mama metastático ou recorrente em 1ª linha |
| [NCT00408408](https://clinicaltrials.gov/study/NCT00408440) | Phase 3 | Desconhecido | 1.206 | Neoadjuvância: Docetaxel ± Capecitabine ou Gemcitabine antes de AC ± Bevacizumab; avalia resposta patológica completa e preditores de resposta |
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Phase 3 | Concluído | N/A | Gemcitabine + Paclitaxel vs Paclitaxel em câncer de mama irressecável, localmente recorrente ou metastático |
| [NCT00070278](https://clinicaltrials.gov/study/NCT00070278) | Phase 3 | Desconhecido | 800 | Neoadjuvância: EC sequencial + Paclitaxel ± Gemcitabine em câncer de mama precoce de alto risco |
| [NCT00440622](https://clinicaltrials.gov/study/NCT00440622) | Phase 3 | Encerrado | 90 | Gemcitabine + Herceptin vs Capecitabine + Herceptin em câncer de mama HER2+ metastático pré-tratado; estudo interrompido prematuramente |
| [NCT00110084](https://clinicaltrials.gov/study/NCT00110084) | Phase 2 | Concluído | 50 | nab-Paclitaxel semanal + Gemcitabine em câncer de mama metastático; avalia eficácia e segurança da combinação |
| [NCT02252887](https://clinicaltrials.gov/study/NCT02252887) | Phase 2 | Concluído | 45 | Gemcitabine + Trastuzumab + Pertuzumab em câncer de mama HER2+ metastático após progressão em terapia anti-HER2 prévia |
| [NCT06027268](https://clinicaltrials.gov/study/NCT06027268) | Phase 2 | Ativo (sem novo recrutamento) | 36 | ToPCourT: Trilaciclib + Pembrolizumab + Gemcitabine + Carboplatina em TNBC avançado irressecável ou metastático |
| [NCT00027989](https://clinicaltrials.gov/study/NCT00027989) | Phase 2 | Desconhecido | N/A | Doxorrubicina lipossomal (Doxil) + Gemcitabine em mulheres com câncer de mama metastático; estudo de fase II monobraço |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Phase II | Breast Cancer Res Treat | Carboplatina + Gemcitabine + Mifepristone em câncer de mama avançado GR-positivo; antagonismo do receptor de glicocorticoide potencializa citotoxicidade da combinação |
| [38262235](https://pubmed.ncbi.nlm.nih.gov/38262235/) | 2024 | Phase I | Gynecologic Oncology | Mirvetuximab Soravtansine + Gemcitabine em TNBC FRα-positivo; determinação de MTD e dose recomendada para fase 2 |
| [25398698](https://pubmed.ncbi.nlm.nih.gov/25398698/) | 2015 | Retrospective Cohort | Cancer Chemo Pharmacol | Docetaxel + Gemcitabine + Bevacizumab como quimioterapia de resgate em câncer de mama HER2-negativo metastático pré-tratado |
| [19856651](https://pubmed.ncbi.nlm.nih.gov/19856651/) | 2009 | Phase II | Tumori | Docetaxel + Gemcitabine em câncer de mama metastático pré-tratado com antraciclinas; estudo de determinação de dose |
| [16020974](https://pubmed.ncbi.nlm.nih.gov/16020974/) | 2005 | Phase II | Oncology | Docetaxel + Gemcitabine semanais como 1ª linha em câncer de mama metastático; estudo multicêntrico de fase II |
| [15685819](https://pubmed.ncbi.nlm.nih.gov/15685819/) | 2004 | Review | Oncology | Revisão de Gemcitabine + Paclitaxel em câncer de mama metastático: 52% de resposta objetiva nos estudos de fase II |
| [15685820](https://pubmed.ncbi.nlm.nih.gov/15685820/) | 2004 | Review | Oncology | Gemcitabine + Docetaxel em câncer de mama metastático; revisão de dados de fase II e escalas de dose |
| [15685821](https://pubmed.ncbi.nlm.nih.gov/15685821/) | 2004 | Review/Cohort | Oncology | Gemcitabine + compostos de platina em câncer de mama metastático como alternativa após falha de antraciclinas/taxanos |
| [14768404](https://pubmed.ncbi.nlm.nih.gov/14768404/) | 2003 | Review | Oncology | Combinações de Gemcitabine com antraciclinas e taxanos no câncer de mama avançado; base para desenvolvimento de regimes de combinação |
| [12138397](https://pubmed.ncbi.nlm.nih.gov/12138397/) | 2002 | Review | Seminars Oncology | Gemcitabine como agente único (16–37% de resposta) e em combinação com terapias-alvo em câncer de mama metastático |

---

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Citotóxico convencional (Análogo de nucleosídeo / Antimetabólito — gemcitabina) |
| Risco de Mielossupressão | Alto (neutropenia grau 3–4 e trombocitopenia são toxicidades dose-limitantes frequentes; risco aumentado em combinação com platinas) |
| Classificação de Emetogenicidade | Baixa a média (aumenta para média quando em combinação com carboplatina ou cisplatina) |
| Itens de Monitoramento | Hemograma completo (CBC com diferencial) antes de cada ciclo; função hepática (ALT, AST, bilirrubina); função renal (creatinina, TFG); sinais de neuropatia periférica quando combinado com taxanos |
| Proteção no Manuseio | Obrigatório seguir regulamentos de manuseio de agentes citotóxicos: preparo em câmara de segurança biológica, uso de EPI (luvas duplas, avental impermeável, proteção ocular), descarte conforme normas de resíduo quimioterápico |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Múltiplos ensaios clínicos de Fase 3 — incluindo o tAnGo RCT (adjuvância) e a combinação Gemcitabine + Paclitaxel com aprovação FDA consolidada — associados a mais de 20 publicações científicas, configuram nível de evidência L1 para o uso de Gemcitabine no carcinoma de mama feminino. A base mecanística é robusta e a indicação já é reconhecida em mercados regulatórios internacionais de referência.

**Para prosseguir, é necessário:**
- Verificar diretamente o portal ANVISA para confirmar o status de registro de Gemcitabine no Brasil, dado que o banco de dados atual não contém registros (possível lacuna de dados)
- Obter e analisar a bula ANVISA/DrugBank para preencher os Data Gaps DG001 (advertências e contraindicações) e DG002 (mecanismo de ação detalhado), bloqueadores para a avaliação formal de segurança
- Definir o subtipo molecular-alvo prioritário (TNBC, HER2+, HR+/HER2-) para selecionar o parceiro de combinação mais adequado (nab-Paclitaxel, Docetaxel, Carboplatina ou terapia anti-HER2)
- Avaliar a expressão de hENT1 como biomarcador preditivo de resposta para estratificação de pacientes candidatos
- Mapear disponibilidade de fornecimento e cadeia logística para eventual uso em protocolo institucional no Brasil
---

