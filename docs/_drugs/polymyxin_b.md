---
layout: default
title: Polymyxin B
parent: Evidência Moderada (L3-L4)
nav_order: 534
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-28
description: "Polymyxin B: nova indicação prevista, Bronquite (bronchitis) (nível de evidência L5). Indicação original: Antibióticos sistêmicos simples"
monitor_inn: "Polymyxin B"
predicted_indications: ["bronchitis", "laryngotracheitis"]
---

# Polymyxin B
{: .fs-9 }

Nível de evidência: **L4** | Indicações previstas: **2** 
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

## Polimixina B: De antibiótico sistêmico e tópico para bronquite (predição principal do TxGNN)
{: .text-alpha }

## Resumo em Uma Frase

A polimixina B é um antibiótico polipeptídico, originalmente usado como antibacteriano sistêmico e em associações tópicas (oftálmicas, otológicas e dermatológicas) contra bactérias Gram-negativas.
O modelo TxGNN prevê que pode ser eficaz para **bronquite (bronchitis)**, mas essa direção conta com **0 ensaios clínicos** e apenas **12 publicações**, em sua maioria históricas, experimentais ou de segurança.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antibióticos sistêmicos simples |
| Nova Indicação Prevista | Bronquite (bronchitis) |
| Pontuação de Previsão TxGNN | 0,9987 |
| Nível de Evidência | L4 (para bronquite) |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: pelo menos 20) |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |


---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada. Segundo informações conhecidas, a polimixina B é um agente bactericida contra bactérias Gram-negativas: liga-se ao lipídeo A do lipopolissacarídeo (LPS) e rompe a membrana externa bacteriana. É um agente de último recurso contra patógenos multirresistentes (por exemplo, *Pseudomonas aeruginosa* e *Acinetobacter baumannii*).

A relação com a nova indicação é plausível apenas para quadros **bacterianos** das vias respiratórias causados por Gram-negativos resistentes (traqueobronquite associada à ventilação, pneumonia). A literatura sobre bronquite é majoritariamente antiga (década de 1970) e trata de uso endobrônquico/inalatório, além de estudos em que a polimixina B inalada **provoca broncoconstrição** em pacientes com asma e bronquite crônica, por degranulação de mastócitos e basófilos. Vários estudos usam a polimixina B como agente de provocação brônquica ou para induzir bronquite eosinofílica em modelos animais, o que não é evidência de benefício terapêutico.

Para a outra previsão respiratória de alta pontuação (laringotraqueíte, 0,9962), a pontuação vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica. Essa doença é, em geral, viral ou tem tratamento de primeira linha estabelecido.

---

## Evidências de Ensaios Clínicos

Para a bronquite (indicação principal), atualmente não há ensaios clínicos relacionados registrados.

Para a indicação **infecção do trato respiratório** (4ª previsão, 98,89%), foram identificados os ensaios abaixo:

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT07086391](https://clinicaltrials.gov/study/NCT07086391) | N/A | Recrutando | 144 | Randomizado, aberto: nebulização por jato vs. malha vibratória de polimixina B em pneumonia por Gram-negativos resistentes a carbapenêmicos em ventilação mecânica; sem resultados |
| [NCT05685615](https://clinicaltrials.gov/study/NCT05685615) | Phase 2 | Concluído | 39 | BV100 intravenoso + polimixina B vs. melhor terapia disponível em pneumonia associada à ventilação por *A. baumannii* resistente a carbapenêmicos; estudo de farmacocinética, eficácia e segurança |
| [NCT06076603](https://clinicaltrials.gov/study/NCT06076603) | N/A | Desconhecido | 30 | Farmacocinética/farmacodinâmica no fluido de revestimento epitelial: polimixina B IV vs. IV + nebulizada em pneumonia associada à ventilação |
| [NCT04839653](https://clinicaltrials.gov/study/NCT04839653) | N/A | Desconhecido | 60 | Descontaminação digestiva seletiva em UTI (prevenção, não tratamento de infecção estabelecida) |
| [NCT02134106](https://clinicaltrials.gov/study/NCT02134106) | Phase 2/3 | Retirado | 0 | Terapia combinada em infecções por Gram-negativos extensivamente resistentes; nenhum participante incluído, sem evidência |

---

## Evidências da Literatura

**Bronquite (indicação principal)**

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [23124906](https://pubmed.ncbi.nlm.nih.gov/23124906/) | 2013 | Revisão/Meta-análise | Infection | Comparação da polimixina B com outros antimicrobianos em pneumonia e traqueobronquite associadas à ventilação por *P. aeruginosa* ou *A. baumannii* |
| [17350201](https://pubmed.ncbi.nlm.nih.gov/17350201/) | 2007 | Coorte | Diagn Microbiol Infect Dis | Polimixina B inalada em 19 pacientes com infecções respiratórias por bacilos Gram-negativos multirresistentes (resgate em pneumonia e tratamento inicial de traqueobronquite) |
| [4322737](https://pubmed.ncbi.nlm.nih.gov/4322737/) | 1971 | Relato de segurança | Ann Intern Med | Alerta sobre os perigos da inalação de polimixina B |
| [231152](https://pubmed.ncbi.nlm.nih.gov/231152/) | 1979 | Estudo fisiológico (segurança) | Lung | Reatividade brônquica à polimixina B inalada em asma e bronquite obstrutiva crônica |
| [4319158](https://pubmed.ncbi.nlm.nih.gov/4319158/) | 1970 | Experimental/Observacional | Chest | Observações experimentais com polimixina B endobrônquica em bronquite crônica |
| [11359434](https://pubmed.ncbi.nlm.nih.gov/11359434/) | 2001 | Estudo animal | Clin Exp Allergy | Acúmulo de eosinófilos nas vias aéreas induzido por polimixina B reduz a responsividade brônquica em cobaias |
| [2984629](https://pubmed.ncbi.nlm.nih.gov/2984629/) | 1985 | Estudo fisiológico (provocação) | Orv Hetil | Provocação brônquica inespecífica com polimixina B em asma e bronquite crônica |
| [4373513](https://pubmed.ncbi.nlm.nih.gov/4373513/) | 1974 | Relato clínico | J Kans Med Soc | Traqueobronquite por *Pseudomonas* tratada com gentamicina sistêmica e aerossol de polimixina B |


| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [23092529](https://pubmed.ncbi.nlm.nih.gov/23092529/) | 2013 | RCT | J Pediatr | Polimixina B-trimetoprima vs. moxifloxacino em conjuntivite aguda em crianças |
| [19043945](https://pubmed.ncbi.nlm.nih.gov/19043945/) | 2008 | RCT multicêntrico | J Pediatr Ophthalmol Strabismus | Velocidade de eficácia clínica: polimixina B/trimetoprima vs. moxifloxacino 0,5% em conjuntivite bacteriana |
| [19043943](https://pubmed.ncbi.nlm.nih.gov/19043943/) | 2008 | RCT | J Pediatr Ophthalmol Strabismus | Moxifloxacino vs. polimixina B/trimetoprima em conjuntivite bacteriana pediátrica |
| [6188739](https://pubmed.ncbi.nlm.nih.gov/6188739/) | 1983 | Estudo clínico randomizado, duplo-cego | J Antimicrob Chemother | Em 230 pacientes, trimetoprima-polimixina B foi eficaz e comparável a neomicina-polimixina B-gramicidina e ao cloranfenicol |
| [2850891](https://pubmed.ncbi.nlm.nih.gov/2850891/) | 1988 | Estudo randomizado, duplo-cego | Curr Med Res Opin | Pomada de trimetoprima-polimixina B vs. cloranfenicol: sem diferenças significativas em erradicação bacteriana e melhora clínica (42 pacientes) |
| [2540136](https://pubmed.ncbi.nlm.nih.gov/2540136/) | 1989 | Revisão de 4 estudos | J Antimicrob Chemother | 528 pacientes com conjuntivite bacteriana; pomada de trimetoprima-polimixina B comparada ao cloranfenicol |
| [11270936](https://pubmed.ncbi.nlm.nih.gov/11270936/) | 2001 | Revisão | Drugs | Revisão comparativa de antibacterianos oftálmicos tópicos; a polimixina B atua sobre Gram-negativos |
| [26922212](https://pubmed.ncbi.nlm.nih.gov/26922212/) | 2016 | Relato de caso | Ann Allergy Asthma Immunol | Anafilaxia a colírio de polimixina B-trimetoprima |

---

## Informações de Comercialização no Brasil

Há 20 registros válidos e o medicamento é comercializado no país. Principais registros:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 188300026 | POLIXIL B | Não informada | Antibióticos sistêmicos simples |
| Registro nº 100430918 | SULFATO DE POLIMIXINA B | Não informada | Antibióticos sistêmicos simples |
| Registro nº 155620062 | SULFATO DE POLIMIXINA B | Não informada | Antibacterianos para uso sistêmico |
| Registro nº 104971311 | MAXINOM | Não informada | Anti-infecciosos tópicos para uso oftálmico |
| Registro nº 100681106 | MAXITROL | Não informada | Anti-infecciosos tópicos – associações medicamentosas |

---

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 73 interações no total. Entre as principais, de gravidade **maior**: amicacina, cidofovir, cisatracurio, toxina botulínica tipo A, deferasirox, imunoglobulinas humanas (incluindo IgG intravenosa e imunoglobulina anti-citomegalovírus) e contrastes iodados (ácido iotalâmico, diatrizoato). De gravidade **moderada**: capreomicina, etinilestradiol, estradiol, mestranol, mesalazina, balsalazida, ibandronato, clofarabina e ácido picossulfúrico. As combinações com aminoglicosídeos, bloqueadores neuromusculares e outros nefrotóxicos exigem atenção especial.
- **Riscos descritos na literatura compilada**: nefrotoxicidade e neurotoxicidade (principais preocupações com o uso sistêmico); broncoconstrição por degranulação de mastócitos/basófilos com uso inalatório, sobretudo em asma e bronquite crônica; anafilaxia com colírio de polimixina B-trimetoprima (relato de caso).

Para advertências e contraindicações formais, consulte a bula.

---

## Conclusão e Próximos Passos

**Decisão: Hold** (para a indicação principal, bronquite)

**Justificativa:**
- A pontuação alta do TxGNN (0,9987) não é acompanhada de ensaios clínicos nem de evidência de eficácia; a literatura sobre bronquite é antiga e inclui sinais de segurança relevantes (broncoconstrição), e não benefício demonstrado. O medicamento é comercializado no Brasil, com 20 registros válidos.

**Para prosseguir, é necessário:**
- Confirmar a disponibilidade local e o status regulatório (20 registros válidos; medicamento comercializado).
- Obter as advertências e contraindicações da bula na ANVISA, hoje ausentes (lacuna bloqueante para a triagem de segurança).
- Obter dados do mecanismo de ação via DrugBank.
- Para a via respiratória: aguardar resultados dos ensaios de nebulização (NCT07086391, NCT06076603) e definir estratégia de mitigação do risco de broncoespasmo e nefro/neurotoxicidade.
- Para conjuntivite: confirmar evidências para a associação polimixina B/trimetoprima (sem registros NCT nos dados compilados) e restringir a indicação à conjuntivite bacteriana (não viral/alérgica).
- Descartar a previsão sem base (laringotraqueíte) ou mantê-la apenas como hipótese computacional.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

