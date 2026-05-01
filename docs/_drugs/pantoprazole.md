---
layout: default
title: Pantoprazole
parent: 僅模型預測 (L5)
nav_order: 387
evidence_level: L5
indication_count: 6
---

# Pantoprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Usando o skill `txgnn-pipeline` para guiar a geração do relatório de reposicionamento de fármacos para o mercado brasileiro.

---

# Pantoprazol: Da doença do refluxo gastroesofágico à úlcera péptica ativa

## Resumo em Uma Frase

Pantoprazol é um inibidor irreversível da bomba de prótons (PPI) amplamente utilizado no âmbito internacional para o tratamento de esofagite erosiva e doença do refluxo gastroesofágico (DRGE). O modelo TxGNN prevê que pode ser eficaz para **Úlcera Péptica Ativa (active peptic ulcer disease)**, atualmente com **3 ensaios clínicos** e **19 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não registrado no Brasil; internacionalmente indicado para esofagite erosiva / DRGE |
| Nova Indicação Prevista | Úlcera Péptica Ativa (active peptic ulcer disease) |
| Pontuação de Previsão TxGNN | 99,69% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Pantoprazol pertence à classe dos benzimidazóis substituídos e atua por ligação covalente irreversível à H⁺/K⁺-ATPase (a "bomba de prótons") das células parietais gástricas. Diferentemente dos bloqueadores H2, atua na via final comum da secreção ácida — independente do estímulo ser histamina, gastrina ou acetilcolina — suprimindo a produção de ácido de forma sustentada (>90%). Essa característica confere duração de ação relativamente longa em comparação com outros PPIs e baixa propensão de ativação em compartimentos corporais levemente ácidos.

A úlcera péptica ativa tem como principal fator patogênico a agressão da mucosa gastroduodenal pelo ácido gástrico, frequentemente potencializada pela infecção por *Helicobacter pylori* ou pelo uso crônico de AINEs. A supressão ácida potente e prolongada promovida pelo pantoprazol cria o ambiente de pH elevado necessário para a cicatrização mucosa e também serve como elemento-base das terapias de erradicação de *H. pylori* (terapia tripla: PPI + dois antibióticos). Múltiplos RCTs confirmam taxas de cicatrização superiores às dos antagonistas H2 para úlceras gástricas e duodenais.

Embora o pantoprazol seja amplamente utilizado para doenças ácido-pépticas em outros países (com indicação FDA para esofagite erosiva e extenso uso off-label para úlcera péptica), sua ausência de registro formal no Brasil justifica a avaliação pelo TxGNN como candidato à regularização no mercado brasileiro. A convergência entre o mecanismo de ação biologicamente plausível e o expressivo volume de evidências clínicas sustenta a razoabilidade da previsão.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Concluído | 323 | Estudo multicêntrico, randomizado, duplo-cego e ativo-controlado comparando ilaprazol vs. pantoprazol em terapia tripla por 7 dias para erradicação de *H. pylori* em pacientes com úlcera gástrica e/ou duodenal com infecção positiva |
| [NCT02197039](https://clinicaltrials.gov/study/NCT02197039) | N/A | Concluído | 316 | Estudo prospectivo para identificar fatores de risco preditores de ressangramento precoce ou apagamento deficiente dos estigmas hemorrágicos após hemostasia endoscópica bem-sucedida com infusão de PPI em alta dose em úlcera péptica sangrante |
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Concluído | 320 | Avaliação do efeito de diferentes PPIs (incluindo pantoprazol) e estatinas sobre a atividade antiplaquetária do clopidogrel em pacientes com stents coronarianos em terapia antiplaquetária dupla |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [18824852](https://pubmed.ncbi.nlm.nih.gov/18824852/) | 2008 | RCT | Digestion | Infusão intermitente vs. contínua de pantoprazol em sangramento por úlcera péptica após terapia endoscópica: ambas as modalidades reduziram ressangramento, destacando o papel central da supressão ácida no prognóstico |
| [16677158](https://pubmed.ncbi.nlm.nih.gov/16677158/) | 2006 | RCT | J Gastroenterol Hepatol | Infusão adjuvante de pantoprazol após hemostasia endoscópica bem-sucedida em úlcera péptica hemorrágica reduziu significativamente a taxa de ressangramento (20% sem PPI vs. melhora com pantoprazol) |
| [12752349](https://pubmed.ncbi.nlm.nih.gov/12752349/) | 2003 | RCT | Aliment Pharmacol Ther | Comparação de três regimes de terapia tripla à base de pantoprazol para erradicação de *H. pylori* e cicatrização de úlcera gástrica; todos os regimes demonstraram eficácia satisfatória |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | RCT | Hepatogastroenterology | Comparação direta de lansoprazol vs. pantoprazol no tratamento de úlcera duodenal ativa e na erradicação de *H. pylori*; eficácia equivalente entre os dois PPIs |
| [10632647](https://pubmed.ncbi.nlm.nih.gov/10632647/) | 2000 | RCT | Aliment Pharmacol Ther | Pantoprazol + amoxicilina + azitromicina ou claritromicina em terapia tripla de 1 semana para erradicação de *H. pylori* em úlcera duodenal; taxa de cura elevada na maioria dos pacientes |
| [38384180](https://pubmed.ncbi.nlm.nih.gov/38384180/) | 2024 | RCT | Gut Liver | Tegoprazan vs. pantoprazol para úlceras artificiais pós-ESD (dissecção submucosa endoscópica): estudo multicêntrico, randomizado, ativo-controlado validando o papel do pantoprazol como referência de tratamento |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | Estudo pré-clínico/clínico | Inflammopharmacology | Efeito combinado de pantoprazol e células-tronco mesenquimais derivadas de tecido adiposo em úlcera gástrica experimental em ratos: pantoprazol atuou nas vias de estresse oxidativo, inflamação e apoptose, promovendo cicatrização |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Revisão Sistemática | Am J Gastroenterol | Metanálise em rede (P-CAB vs. PPIs incluindo pantoprazol) na esofagite grau C/D: P-CABs mostraram vantagem em cicatrização inicial, enquanto PPIs mantêm posição como referência estabelecida |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Revisão | Clin Drug Investig | Monografia abrangente de pantoprazol: ligação irreversível e específica à bomba de prótons; duração de ação prolongada; ausência de interações medicamentosas identificadas; eficaz no tratamento de DRGE, úlcera péptica e síndrome de Zollinger-Ellison |
| [9017763](https://pubmed.ncbi.nlm.nih.gov/9017763/) | 1997 | Revisão | Pharmacotherapy | Mecanismo dos PPIs: acúmulo no espaço ácido da célula parietal, conversão para sulfenamida ativa e inibição covalente da H⁺/K⁺-ATPase — mais eficazes que bloqueadores H2 no controle da secreção ácida |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
As evidências para uso de pantoprazol na úlcera péptica ativa são robustas, sustentadas por um ensaio de Fase 3 com n=323, múltiplos RCTs de alta qualidade e vasta literatura farmacológica que abrange mais de três décadas — com o mecanismo de ação (inibição da H⁺/K⁺-ATPase) diretamente relacionado à fisiopatologia da condição. A ausência de registro na ANVISA representa a principal barreira para a comercialização no Brasil.

**Para prosseguir, é necessário:**
- Verificar o status regulatório atualizado na ANVISA e confirmar se há registros vigentes não capturados na consulta de 2026
- Obter a bula oficial (SmPC ou package insert) para documentar advertências, contraindicações e interações medicamentosas
- Mapear as formas farmacêuticas e vias de administração disponíveis (oral e intravenosa) e verificar compatibilidade com as necessidades do mercado brasileiro
- Avaliar a necessidade de estudo de bioequivalência ou bridging study para submissão de registro na ANVISA
- Conduzir revisão de farmacovigilância para populações especiais (insuficiência hepática, metabolizadores CYP2C19)
---

