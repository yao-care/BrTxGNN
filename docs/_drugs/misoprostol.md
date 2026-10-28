---
layout: default
title: Misoprostol
parent: Apenas Predição do Modelo (L5)
nav_order: 463
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-13
description: "Misoprostol: nova indicação prevista, Amenorreia (amenorrhea) (nível de evidência L4). Indicação original: Não disponível nos dados compilados"
monitor_inn: "MISOPROSTOL"
predicted_indications: ["amenorrhea (disease)", "atypical coarctation of aorta"]
---

# Misoprostol
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

## Misoprostol: Da indicação original não registrada à amenorreia
{: .text-alpha }

## Resumo em Uma Frase

Misoprostol é um análogo da prostaglandina E1 que induz contração uterina e amadurecimento do colo do útero. Não há indicação original registrada nos dados compilados para este relatório.
O modelo TxGNN prevê que pode ser eficaz para **amenorreia (amenorrhea)**, mas atualmente há **0 ensaios clínicos** e **7 publicações** relacionadas, nenhuma delas avaliando o tratamento da amenorreia em si (a maioria trata de aborto medicamentoso com mifepristona + misoprostol).

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível nos dados compilados (nenhuma indicação registrada na ANVISA) |
| Nova Indicação Prevista | Amenorreia (amenorrhea) |
| Pontuação de Previsão TxGNN | 0,9964 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 2) |
| Número de Registros | 2 (ativos: 1) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o misoprostol é um análogo sintético da prostaglandina E1 que estimula contrações uterinas e promove o amadurecimento cervical.

Existe um elo plausível, porém indireto, com a amenorreia: o fármaco atua sobre o endométrio e o sangramento uterino, sendo usado na interrupção da gestação, na evacuação de restos ovulares e na indução de sangramento de privação. A gravidez e seu término estão ligados à interrupção do ciclo menstrual, o que pode explicar a associação captada pelo modelo.

É importante ressaltar que a literatura recuperada trata sobretudo de aborto medicamentoso (mifepristona + misoprostol), e **não** do tratamento da amenorreia. Nesses estudos, a amenorreia aparece apenas como critério de idade gestacional (por exemplo, "amenorreia ≤ 35 dias"). A pontuação elevada do TxGNN é uma previsão computacional, sem respaldo de dados clínicos diretos.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT | Reproductive Sciences | Mifepristona em baixa dose + misoprostol autoadministrado para aborto medicamentoso ultraprecoce (744 mulheres, amenorreia ≤35 dias); avaliação de eficácia, segurança e aceitabilidade |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT (dose-ranging) | Reproductive Sciences | 2.500 mulheres com gravidez ultraprecoce receberam doses decrescentes de mifepristona (150 a 50 mg) seguidas de 200 µg de misoprostol oral; desfecho primário: aborto completo sem cirurgia |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Coorte | Human Reproduction | Avaliação da viabilidade e eficácia de mifepristona em baixa dose + misoprostol antes da menstruação esperada para prevenir gravidez não planejada |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Coorte | J Obstet Gynaecol Res | Segurança e eficácia de mifepristona em baixa dose + misoprostol autoadministrado para interrupção de gravidez precoce |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Revisão | BMJ | Manejo medicamentoso de aborto retido e gestação anembrionária |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Revisão | J Obstet Gynaecol Can | Ablação endometrial no manejo do sangramento uterino anormal (relação indireta com misoprostol) |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Relato de caso | Cureus | Esteatose hepática aguda da gravidez: desafio diagnóstico (a amenorreia é citada apenas como sintoma de apresentação) |

---

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (TxGNN/PrimeKG, não derivadas de bula):** hipertensão, insuficiência e doenças hepáticas, doença da vesícula biliar, insuficiência cardíaca congestiva, doença inflamatória intestinal, asma (incluindo intrínseca e alérgica), dependência/abuso de substâncias, distúrbios da coagulação, AVC e doenças cerebrovasculares, infarto cerebral, infarto do miocárdio e trombose coronariana, hemoglobinopatias, anemias (incluindo macrocítica), lesão hepática induzida por fármacos, doenças cardiovasculares e cardíacas, úlcera péptica ativa e meningite não infecciosa.
- **Interações medicamentosas** (100 interações registradas; principais exemplos):
  - **Grave:** dinoprostona (tópica).
  - **Moderada:** óxido de magnésio, hidróxido de magnésio, carbonato de magnésio, magaldrato e quinapril.
  - **Leve:** citrato de sódio, hidróxido de alumínio, carbonato de cálcio, bicarbonato de sódio e naproxeno.
  - **Nível não classificado:** goserelina, ciclosporina, cianocobalamina, calcitriol, ácido fólico, pravastatina, valsartana, ramipril e lorazepam.
- **Gestação:** o misoprostol tem perfil uterotônico, com preocupações conhecidas de teratogenicidade e ruptura uterina na gravidez, o que é particularmente relevante para uma indicação ligada à saúde reprodutiva feminina.

Consulte a bula para informações adicionais de advertências e contraindicações.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos e a literatura disponível trata de aborto medicamentoso, não do tratamento da amenorreia. A pontuação do TxGNN (0,9964) é apenas uma previsão computacional, e o fármaco não possui registro ativo no Brasil nos dados compilados.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança.
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank).
- Esclarecer a situação regulatória e as indicações aprovadas do misoprostol no Brasil.
- Buscar estudos que avaliem diretamente o misoprostol no tratamento da amenorreia (por exemplo, sangramento de privação), com análise de risco-benefício em mulheres em idade fértil.
- Avaliar a segunda previsão do modelo (coarctação atípica da aorta), que não tem ensaios nem literatura (nível L5) e para a qual o perfil de segurança do misoprostol desfavorece o uso; ela não deve avançar sem evidências novas.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

