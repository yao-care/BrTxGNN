---
layout: default
title: Imipenem
parent: Apenas Predição do Modelo (L5)
nav_order: 364
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Imipenem: nova indicação prevista, Esclerodermia difusa (Diffuse Scleroderma) (nível de evidência L5). Indicação original: Antibacteriano / antibióticos sistêmicos (associações medicamentosas)"
monitor_inn: "imipenem"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "sinusitis", "chronic rhinosinusitis", "typhoid fever", "chronic ethmoidal sinusitis", "paranasal sinus neoplasm (disease)", "staphylococcus aureus infection", "eosinophilia-myalgia syndrome"]
---

# Imipenem
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

## Imipenem: De antibacteriano sistêmico a Diffuse Scleroderma (esclerodermia difusa)
{: .text-alpha }

## Resumo em Uma Frase

Imipenem (associado à cilastatina sódica) é um antibiótico carbapenêmico, originalmente usado como antibacteriano sistêmico.
O modelo TxGNN prevê que pode ser eficaz para **esclerodermia difusa (Diffuse Scleroderma)**, mas essa previsão tem **0 ensaios clínicos** e **0 publicações** como apoio, sendo apenas uma previsão computacional sem plausibilidade mecanística.
Entre as demais previsões, as mais bem sustentadas são **infecção por Staphylococcus aureus** (2 ensaios clínicos e 20 publicações) e **febre tifoide/salmonelose** (apenas literatura).

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antibacteriano / antibióticos sistêmicos (associações medicamentosas) |
| Nova Indicação Prevista | Esclerodermia difusa (Diffuse Scleroderma) |
| Pontuação de Previsão TxGNN | 0,9999 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 9 de 9) |
| Número de Registros | 9 (ativos: 9) |
| Decisão Recomendada | Hold |

> Observação: a previsão de maior ranking (esclerodermia difusa) é a de menor sustentação biológica. As indicações infecciosas abaixo são mais plausíveis e merecem prioridade de análise.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o imipenem é um carbapenêmico beta-lactâmico que se liga às proteínas ligadoras de penicilina (PBP) e inibe a síntese da parede celular bacteriana. É administrado com cilastatina, que inibe a degradação renal do imipenem.

Para a esclerodermia difusa, **não há vínculo mecanístico plausível**: trata-se de doença autoimune e fibrótica, sem componente infeccioso que o imipenem possa tratar. A pontuação alta do TxGNN é apenas um resultado computacional, sem ensaios nem literatura.

Já para outras previsões da lista o raciocínio é mais consistente:
- **Febre tifoide, febre paratifoide e salmonelose**: os carbapenêmicos são opção de resgate contra *Salmonella* extensivamente resistente (XDR). A evidência é in vitro, de vigilância e relatos de caso.
- **Infecção por *S. aureus***: há atividade contra cepas sensíveis à meticilina. Para MRSA, o apoio vem de combinações (fosfomicina + imipenem), não do imipenem isolado. Por já ser antibacteriano, é em parte uma extensão dentro da própria classe.
- **Sinusite, rinossinusite crônica e sinusite etmoidal crônica**: o imipenem é de uso intravenoso e de amplo espectro, não adequado à rotina; só se justificaria em casos graves ou resistentes.
- **Neoplasia de seio paranasal e síndrome eosinofilia-mialgia**: sem vínculo mecanístico plausível.

## Evidências de Ensaios Clínicos

Para a indicação principal (esclerodermia difusa), atualmente não há ensaios clínicos relacionados registrados.

Como referência, a previsão com ensaios registrados é a infecção por *Staphylococcus aureus*:

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00871104](https://clinicaltrials.gov/study/NCT00871104) | Phase 4 | Concluído | 50 | Fosfomicina + imipenem versus vancomicina (tratamento padrão) em endocardite infecciosa por MRSA; avalia eficácia e segurança |
| [NCT01356472](https://clinicaltrials.gov/study/NCT01356472) | Phase 4 | Desconhecido | 60 | Linezolida isolada ou combinada com carbapenêmico contra MRSA em pneumonia associada à ventilação; o carbapenêmico específico não é confirmado como imipenem |

## Evidências da Literatura

Para esclerodermia difusa, atualmente não há literatura relacionada.

Publicações selecionadas das demais previsões (prioridade para estudos clínicos e relatos diretamente ligados ao imipenem):

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [39991360](https://pubmed.ncbi.nlm.nih.gov/39991360/) | 2025 | Estudo clínico | Cureus | Carbapenêmicos como última linha no tratamento da febre tifoide MDR/XDR em Peshawar, Paquistão |
| [19208884](https://pubmed.ncbi.nlm.nih.gov/19208884/) | 2009 | Estudo in vitro | J Med Microbiol | CIM de carbapenêmicos e tigeciclina contra 210 isolados de *Salmonella* |
| [22204180](https://pubmed.ncbi.nlm.nih.gov/22204180/) | 2011 | In vitro | JPMA | Suscetibilidade de *Salmonella* Typhi e Paratyphi a novos antimicrobianos, incluindo imipenem |
| [15707075](https://pubmed.ncbi.nlm.nih.gov/15707075/) | 2003 | Relato de caso | J Med Liban | Rabdomiólise e insuficiência renal por *S. typhi* tratadas com imipenem/cilastatina e hemodiálise |
| [3460521](https://pubmed.ncbi.nlm.nih.gov/3460521/) | 1986 | Série clínica | Antimicrob Agents Chemother | Imipenem-cilastatina em 23 pacientes com infecções por *S. aureus* (MRSA e MSSA) |
| [33020155](https://pubmed.ncbi.nlm.nih.gov/33020155/) | 2020 | Comentário de caso | Antimicrob Agents Chemother | Imipenem/cilastatina + fosfomicina como combinação nova para MRSA refratário |
| [6421794](https://pubmed.ncbi.nlm.nih.gov/6421794/) | 1983 | Pré-clínico | J Antimicrob Chemother | Imipenem em endocardite experimental por *S. aureus* em coelhos, com atividade in vitro elevada |
| [3859217](https://pubmed.ncbi.nlm.nih.gov/3859217/) | 1985 | Estudo clínico | Am J Med | Potencial do imipenem como monoterapia empírica em pacientes oncológicos com neutropenia febril |
| [10588305](https://pubmed.ncbi.nlm.nih.gov/10588305/) | 1999 | In vitro/in vivo | J Antimicrob Chemother | Efeito sinérgico de vancomicina + imipenem contra MRSA em 34 de 36 isolados |
| [16918048](https://pubmed.ncbi.nlm.nih.gov/16918048/) | 2006 | Revisão | Folia Med | Terapia antimicrobiana das salmoneloses: estado atual e perspectivas |

## Informações de Comercialização no Brasil

Os 9 registros encontrados estão **válidos** (9 de 9); o medicamento está comercializado.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 137040002 | Imipenem + Cilastatina Sódica | Não informada | Antibióticos sistêmicos - associações medicamentosas |
| Registro 100630137 | Tiepem | Não informada | Antibióticos sistêmicos - associações medicamentosas |
| Registro 155620013 | Imipenem + Cilastatina | Não informada | Antibióticos sistêmicos - associações medicamentosas |
| Registro 102010053 | Penexil | Não informada | Antibióticos sistêmicos - associações medicamentosas |
| Registro 104970228 | Imicil | Não informada | Antibióticos sistêmicos - associações medicamentosas |

Há ainda outros 4 registros cancelados, incluindo Recarbrio (indicação: antibacteriano).

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento do TxGNN** (relações fármaco-doença, não texto de bula): epilepsia, doença renal, piureter, colite por *Clostridium difficile* e enterocolite necrosante perinatal.
- **Interações medicamentosas** (15 identificadas):
  - **Maior gravidade**: bupropiona, iohexol e iopamidol.
  - **Gravidade moderada**: varfarina, dicumarol, lindano, aminofilina, difilina, oxtrifilina, teofilina, ciclosporina, etinilestradiol, ácido micofenólico, pemetrexede e polietilenoglicol (3350 com eletrólitos).

Consulte a bula para advertências e contraindicações formais, que não estavam disponíveis nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Para esclerodermia difusa, a previsão é apenas computacional (nível L5), sem ensaios, sem literatura e sem vínculo mecanístico plausível entre um antibiótico beta-lactâmico e uma doença autoimune fibrótica.
- Além disso, não há registro válido no Brasil: os 9 registros estão cancelados.

**Para prosseguir, é necessário:**
- Não priorizar a esclerodermia difusa; redirecionar a análise para indicações infecciosas (febre tifoide/paratifoide por *Salmonella* XDR e infecção por *S. aureus* em combinação), que são mais plausíveis, embora de nível L4 e L2 e ainda sem ensaios controlados do imipenem.
- Obter dados de mecanismo de ação (por exemplo, via DrugBank).
- Obter e analisar a bula na ANVISA para advertências e contraindicações formais.
- Verificar a situação regulatória atual (reativação de registro ou alternativas comercializadas) e a compatibilidade da via de administração, intravenosa, com cada indicação.
- Para qualquer indicação infecciosa, realizar ensaios controlados comparativos e considerar políticas de uso racional de carbapenêmicos diante da resistência antimicrobiana.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

