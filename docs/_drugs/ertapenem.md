---
layout: default
title: Ertapenem
parent: Apenas Predição do Modelo (L5)
nav_order: 296
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Ertapenem: nova indicação prevista, Infecção por Staphylococcus aureus (Staphylococcus aureus infection) (nível de evidência L5). Indicação original: Antibacterianos para uso sistêmico"
monitor_inn: "ertapenem"
predicted_indications: ["bacterial arthritis", "staphylococcus aureus infection"]
---

# Ertapenem
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **2** 
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

# Ertapeném: De antibacteriano sistêmico para bacteriemia por Staphylococcus aureus

## Resumo em Uma Frase

Ertapeném é um antibiótico carbapenêmico de uso sistêmico, registrado no Brasil na categoria de antibacterianos para uso sistêmico.
O modelo TxGNN prevê que pode ser eficaz para **infecção por Staphylococcus aureus (Staphylococcus aureus infection)**, com **2 ensaios clínicos** em andamento e **20 publicações** apoiando esta direção, principalmente como parceiro de combinação com cefazolina na bacteriemia persistente por MSSA.

A primeira previsão do modelo, artrite bacteriana (pontuação de 99,72%), tem apenas relatos de casos e coortes, sem ensaios clínicos registrados. Por isso, este relatório prioriza a segunda previsão, que tem mais evidências.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antibacterianos para uso sistêmico |
| Nova Indicação Prevista | Infecção por Staphylococcus aureus (Staphylococcus aureus infection) |
| Pontuação de Previsão TxGNN | 99,28% |
| Nível de Evidência | L2 (conservador: há um ensaio Phase 2 em andamento e dados observacionais, mas nenhum RCT concluído) |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 4 (todos cancelados) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo a farmacologia geral dos carbapenêmicos, o ertapeném inibe a síntese da parede celular bacteriana ao se ligar às proteínas ligadoras de penicilina (PBPs), com ligação preferencial às PBP 2 e 3. Seu espectro é amplo e inclui estreptococos, *S. aureus* sensível à meticilina (MSSA), enterobactérias e anaeróbios.

O ertapeném não é um agente de primeira linha contra estafilococos quando usado isoladamente. O interesse está na **sinergia com a cefazolina**: os dois fármacos saturam PBPs complementares, o que reforça a atividade bactericida. Essa combinação foi usada como terapia de resgate em bacteriemia persistente por MSSA, inclusive em casos de endocardite, com eliminação rápida da bacteremia em séries de casos. Houve também sinergia em modelo animal (endocardite em ratos e infecção cutânea em camundongos).

Portanto, o papel previsto é de **parceiro adjuvante em um nicho definido** (bacteriemia persistente por MSSA), e não de monoterapia. Como o mecanismo original não está disponível, esta ligação mecanística baseia-se na literatura publicada.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT04886284](https://clinicaltrials.gov/study/NCT04886284) | Phase 2 | Recrutando | 60 | Testa cefazolina + ertapeném em bacteriemia por MSSA. É um subestudo do ensaio de plataforma SNAP. Sem resultados ainda; conclusão prevista para 07/2027 |
| [NCT07148960](https://clinicaltrials.gov/study/NCT07148960) | Phase 4 | Inscrição por convite | 300 | Terapia IV dupla precoce versus terapia única em bacteriemia por *S. aureus*, buscando reduzir a duração da bacteremia (< 6 dias). O regime pode não se limitar ao ertapeném. Sem resultados; conclusão prevista para 07/2027 |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [31773134](https://pubmed.ncbi.nlm.nih.gov/31773134/) | 2020 | Coorte | Clin Infect Dis | Cefazolina + ertapeném como resgate em 11 casos de bacteriemia persistente por MSSA (6 com endocardite); eliminação imediata (≤24 h) em 8 casos |
| [38946294](https://pubmed.ncbi.nlm.nih.gov/38946294/) | 2024 | Coorte | J Antimicrob Chemother | Compara terapia combinada com carbapenêmico versus tratamento padrão em bacteriemia persistente por MSSA |
| [40448546](https://pubmed.ncbi.nlm.nih.gov/40448546/) | 2025 | Coorte | J Antimicrob Chemother | Impacto da hipoalbuminemia em pacientes que recebem terapia combinada com ertapeném; a combinação foi associada a esterilização mais rápida das hemoculturas |
| [41759962](https://pubmed.ncbi.nlm.nih.gov/41759962/) | 2026 | Coorte | Infect Dis Now | Série multicêntrica de ertapeném com penicilina M ou cefazolina em bacteriemia por MSSA na prática real |
| [27572414](https://pubmed.ncbi.nlm.nih.gov/27572414/) | 2016 | Série de casos | Antimicrob Agents Chemother | Sinergia cefazolina + ertapeném in vitro e em modelo murino; eliminação de bacteremia persistente |
| [39230345](https://pubmed.ncbi.nlm.nih.gov/39230345/) | 2025 | Revisão | Am J Health Syst Pharm | Revisão das opções de combinação para bacteriemia persistente por MSSA |
| [11772242](https://pubmed.ncbi.nlm.nih.gov/11772242/) | 2001 | Revisão | Expert Opin Investig Drugs | Descreve o ertapeném como carbapenêmico estável à desidropeptidase, com ligação às PBP 2 e 3 e boa atividade contra MSSA |
| [15150179](https://pubmed.ncbi.nlm.nih.gov/15150179/) | 2004 | Revisão | J Antimicrob Chemother | Revisão da atividade in vitro do ertapeném contra bactérias Gram-positivas, Gram-negativas e anaeróbias |
| [39777519](https://pubmed.ncbi.nlm.nih.gov/39777519/) | 2025 | In vitro | J Infect Dis | Carbapenêmicos (ertapeném ou meropeném) potencializam a morte de MRSA por ceftarolina ou vancomicina |
| [34599521](https://pubmed.ncbi.nlm.nih.gov/34599521/) | 2021 | Série de casos | J Card Surg | Cefazolina + ertapeném como resgate em infecção refratária de dispositivo de assistência ventricular por MSSA |

---

## Informações de Comercialização no Brasil

Todos os 4 registros encontrados estão cancelados; não há registro válido atualmente.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 174200004 | Ertapeném Sódico | Não informada | Antibióticos sistêmicos simples |
| Registro 155620061 | Ertapeném Sódico | Não informada | Antibacterianos para uso sistêmico |
| Registro 102010064 | Ertapeném Sódico | Não informada | Antibióticos sistêmicos simples |
| Registro 101710224 | Invanz | Não informada | Antibióticos sistêmicos simples |

---

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não é texto de bula)**: epilepsia, doença renal, piureter, colite por *Clostridium difficile* e enterocolite necrosante perinatal.
- **Interações medicamentosas**: foram identificadas 38 interações. Entre as principais:
  - **Grave (Major)**: bupropiona (risco convulsivo).
  - **Moderada**: ácido picossulfúrico, polietilenoglicol 3350 com eletrólitos e sulfato de sódio.
  - **Gravidade não classificada**: calcitriol, pantoprazol, doxiciclina, morfina, metformina, omeprazol, rosiglitazona, vancomicina, prednisona, sinvastatina, ranitidina, ondansetrona, metronidazol, famotidina, ácido acetilsalicílico e metoclopramida, entre outros.
- **Pontos de atenção da literatura**: a exposição a carbapenêmicos pode selecionar resistência e aumentar o risco de infecção por *C. difficile*. A ligação elevada às proteínas torna possível uma exposição subótima na hipoalbuminemia (albumina < 2,5 g/dL).

Para advertências e contraindicações oficiais, consulte a bula.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Existe racional mecanístico e dados observacionais promissores para a combinação cefazolina + ertapeném, mas o único ensaio Phase 2 diretamente relevante ainda está recrutando e não há RCT concluído. Além disso, o ertapeném não tem registro válido no Brasil. Por isso, a direção deve ser tratada como questão de pesquisa até que haja resultados.

**Para prosseguir, é necessário:**
- Resultados do ensaio NCT04886284 (cefazolina + ertapeném) e, se possível, do NCT07148960.
- Confirmação do mecanismo de ação e da bula oficial (advertências e contraindicações), hoje indisponíveis.
- Avaliação da situação regulatória: todos os registros no Brasil estão cancelados, então é preciso verificar a disponibilidade do produto e a necessidade de novo registro.
- Plano de segurança que contemple interação com bupropiona, risco convulsivo, função renal, colite por *C. difficile* e estratégia de controle de resistência (stewardship).
- Quanto à artrite bacteriana (primeira previsão), trata-se mais de extensão de espectro antibacteriano já conhecido do que de reposicionamento verdadeiro; as evidências se limitam a relatos de casos e coortes (nível L4), e vários artigos recuperados são alheios ao tema.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

