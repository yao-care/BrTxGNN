---
layout: default
title: Amoxicillin
parent: 僅模型預測 (L5)
nav_order: 56
evidence_level: L5
indication_count: 10
---

# Amoxicillin
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

# Amoxicillin: De Infecções Bacterianas à Epiglotite Aguda

## Resumo em Uma Frase

Amoxicillin é um antibiótico beta-lactâmico de amplo espectro amplamente utilizado no tratamento de infecções bacterianas do trato respiratório superior, urinário e odontológico.
O modelo TxGNN prevê que pode ser eficaz para **Epiglotite (Epiglottitis)**, atualmente com **15 publicações** — incluindo **3 diretrizes clínicas** e uma série de casos prospectiva com 24 pacientes — apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções bacterianas (respiratórias, urinárias, odontológicas) |
| Nova Indicação Prevista | Epiglotite (Epiglottitis) |
| Pontuação de Previsão TxGNN | 98.70% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | Não identificado na consulta automática (verificação ANVISA recomendada) |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Não há dados detalhados de mecanismo de ação (MOA) no presente Evidence Pack — este é um gap de alta severidade identificado no processo de coleta. Com base no conhecimento farmacológico estabelecido, Amoxicillin é um antibiótico beta-lactâmico que inibe a síntese da parede celular bacteriana ao se ligar seletivamente às proteínas de ligação à penicilina (PBPs). Esse bloqueio impede a transpeptidação final do peptidoglicano, levando à lise osmótica e morte bacteriana. O fármaco é ativo contra ampla gama de bactérias Gram-positivas (*Streptococcus pyogenes*, *S. pneumoniae*, *Staphylococcus aureus* sensível) e Gram-negativas (*Haemophilus influenzae* não produtor de beta-lactamase, *Moraxella catarrhalis* sensível).

A epiglotite aguda é causada predominantemente por *Haemophilus influenzae* tipo b (Hib) e por *Streptococcus* spp. — exatamente os patógenos-alvo primários do Amoxicillin. A transposição da indicação original (infecções bacterianas do trato respiratório) para epiglotite é mecanisticamente direta e clinicamente lógica: trata-se da mesma classe de patógenos, na mesma via anatômica, com o mesmo mecanismo de ação antibacteriana. A epiglotite representa, portanto, uma extensão natural do espectro clínico já coberto pelo fármaco.

A combinação Amoxicillin-clavulanato (Augmentin) possui posição consolidada em diretrizes internacionais de infecções ORL, sendo recomendada na terapia sequencial (IV → oral) em crianças hospitalizadas e no tratamento de casos de menor gravidade. A adição do clavulanato amplia a cobertura para cepas produtoras de beta-lactamase — variante relevante em *H. influenzae* — tornando a formulação combinada a preferida clinicamente para epiglotite bacteriana documentada.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [37730165](https://pubmed.ncbi.nlm.nih.gov/37730165/) | 2023 | Diretriz Clínica | Infectious Diseases Now | Diretrizes de tratamento antimicrobiano de infecções ORL; define papel do Amoxicillin em infecções bacterianas do trato respiratório superior, incluindo indicações de uso e critérios de escalonamento |
| [29290238](https://pubmed.ncbi.nlm.nih.gov/29290238/) | 2017 | Diretriz Clínica | Archives de Pédiatrie | Diretrizes pediátricas francesas de infecções ORL; posiciona antibióticos beta-lactâmicos como primeira linha em infecções bacterianas supraglóticas confirmadas |
| [26332822](https://pubmed.ncbi.nlm.nih.gov/26332822/) | 2015 | Diretriz Clínica | Ned Tijdschr Geneeskd | Revisão da diretriz holandesa para faringite aguda; inclui critérios de diagnóstico diferencial para epiglotite e orientações de manejo |
| [3571053](https://pubmed.ncbi.nlm.nih.gov/3571053/) | 1987 | Série de Casos Prospectiva | J Antimicrob Chemother | Terapia sequencial IV→oral com Amoxicillin-clavulanato em 71 crianças hospitalizadas, incluindo **24 casos de epiglotite aguda**; desfechos favoráveis com boa tolerabilidade |
| [10893774](https://pubmed.ncbi.nlm.nih.gov/10893774/) | 2000 | Revisão | Anales de Medicina Interna | Manifestações clínicas e tratamento de infecções invasivas por *H. influenzae*; analisa papel dos beta-lactâmicos (incluindo Amoxicillin) na epiglotite e outras infecções supraglóticas |
| [17334726](https://pubmed.ncbi.nlm.nih.gov/17334726/) | 2007 | Coorte Retrospectiva | J Infect Chemother | 52 crianças com infecções invasivas por *H. influenzae* no Japão (1996–2005); epiglotite em 7,7% dos casos; análise de sensibilidade antimicrobiana antes da vacinação Hib |
| [21404603](https://pubmed.ncbi.nlm.nih.gov/21404603/) | 2011 | Estudo Microbiológico | Kansenshogaku Zasshi | CIM e CMB de 8 antibióticos parenterais contra *H. influenzae* invasivo em crianças; inclui casos de epiglotite; confirma sensibilidade dos beta-lactâmicos |
| [15960127](https://pubmed.ncbi.nlm.nih.gov/15960127/) | 2005 | Relato de Caso | Acta Otorrinolaringol Esp | Actinomicose da base da língua com massa epiglótica; resolução clínica completa após incisão cirúrgica e **1 mês de Amoxicillin oral** |
| [8322095](https://pubmed.ncbi.nlm.nih.gov/8322095/) | 1993 | Relato de Caso | Southern Medical Journal | Epiglotite aguda por *S. aureus* no 3º trimestre de gestação; intubação precoce e antibioticoterapia eficaz; discussão sobre diagnóstico diferencial em adultos |
| [1755915](https://pubmed.ncbi.nlm.nih.gov/1755915/) | 1991 | Série de Casos | Laryngo-Rhino-Otologie | 79 adultos com epiglotite aguda; revisão de etiologia bacteriana, apresentação clínica e protocolo de antibioticoterapia em serviço universitário de referência |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
A epiglotite aguda bacteriana é a indicação prevista pelo TxGNN com maior grau de evidência clínica (L3) e com mecanismo biológico direto para o Amoxicillin: três diretrizes clínicas internacionais e uma série de casos prospectiva com 24 pacientes pediátricos sustentam o uso da formulação Amoxicillin-clavulanato na terapia sequencial da epiglotite, atuando diretamente sobre os agentes etiológicos *H. influenzae* e *Streptococcus* spp.

**Para prosseguir, é necessário:**
- Confirmar registro da formulação Amoxicillin e/ou Amoxicillin-clavulanato na ANVISA — a ausência de registros neste Evidence Pack é provavelmente uma falha de consulta, devendo ser verificada manualmente no portal ANVISA
- Obter e analisar a bula ANVISA para levantamento completo de advertências, contraindicações e interações (Data Gap DG001 — severidade Bloqueante)
- Obter dados completos de mecanismo de ação via DrugBank API (Data Gap DG002 — severidade Alta)
- Definir protocolo clínico: Amoxicillin simples vs. Amoxicillin-clavulanato conforme perfil de resistência a beta-lactamase da população-alvo local
- Considerar que a ausência de ensaios clínicos registrados para epiglotite limita a geração de evidência de fase 2/3 — a indicação opera em nível de prática clínica estabelecida, não em nível de investigação formal
---

