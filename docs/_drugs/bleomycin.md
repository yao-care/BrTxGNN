---
layout: default
title: Bleomycin
parent: Apenas Predição do Modelo (L5)
nav_order: 145
evidence_level: L5
indication_count: 6
---

# Bleomycin
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **6** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relatório de avaliação farmacêutica

</div>

# Bleomicina: De antineoplásico citotóxico para neoplasia de cauda equina (previsão do modelo)

## Resumo em Uma Frase

A bleomicina é um antibiótico antineoplásico citotóxico, registrado no Brasil como sulfato de bleomicina para o tratamento de câncer.
O modelo TxGNN prevê que ela pode ser eficaz para **Neoplasia da Cauda Equina (Cauda Equina Neoplasm)**, mas essa previsão tem **0 ensaios clínicos** e apenas **1 publicação** indireta como apoio. Entre as seis indicações previstas, a de **sarcoma de células reticulares (linfoma)** é a que reúne mais evidências.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antibióticos antineoplásicos (classe terapêutica registrada na ANVISA) |
| Nova Indicação Prevista | Neoplasia da Cauda Equina (Cauda Equina Neoplasm) |
| Pontuação de Previsão TxGNN | 99,30% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 5 (todos cancelados) |
| Decisão Recomendada | Hold |

> Observação: o texto de indicação nos registros é apenas a classe terapêutica ("antibióticos antineoplásicos" / "antineoplásicos citotóxicos"), sem indicação clínica específica.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a bleomicina é um antibiótico glicopeptídico citotóxico que causa quebras na fita de DNA, e sua atividade antitumoral é reconhecida em linfomas, tumores de células germinativas e outros cânceres. Mecanisticamente, essa citotoxicidade poderia ser aplicável a outros tumores.

A pontuação do TxGNN é muito alta (0,993), mas não há vínculo direto entre a bleomicina e a neoplasia da cauda equina. A única publicação recuperada trata de radioterapia para germinoma do SNC recidivado após quimioterapia (que incluiu carboplatina, etoposídeo e bleomicina), um cenário tumoral diferente. Além disso, a penetração da bleomicina no sistema nervoso central é baixa, o que enfraquece a justificativa para tumores espinhais ou do SNC.

Vale destacar que a avaliação das demais indicações previstas mostra um quadro mais consistente para linfomas (sarcoma de células reticulares), descrito na seção de conclusão.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para a neoplasia da cauda equina.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [9440744](https://pubmed.ncbi.nlm.nih.gov/9440744/) | 1998 | Coorte | Journal of Clinical Oncology | Avaliação retrospectiva da radioterapia como resgate em germinoma do SNC recidivado após quimioterapia primária (PEB: carboplatina, etoposídeo e bleomicina). Cenário diferente da indicação prevista. |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 100431498 | Sulfato de Bleomicina | Não informada | Antibióticos antineoplásicos (cancelado) |
| Registro nº 155370141 | Sulfato de Bleomicina | Não informada | Antibióticos antineoplásicos (cancelado) |
| Registro nº 115410008 | Cinaleo | Não informada | Antineoplásicos citotóxicos (cancelado) |
| Registro nº 100431509 | Blesto | Não informada | Antibióticos antineoplásicos (cancelado) |
| Registro nº 105730676 | Bonar | Não informada | Antibióticos antineoplásicos (cancelado) |

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Citotóxico convencional (antibiótico antineoplásico) |
| Risco de Mielossupressão | Baixo (relato histórico de efeito poupador de medula óssea; PMID 4109401) |
| Classificação de Emetogenicidade | Baixa a média |
| Itens de Monitoramento | Função pulmonar (toxicidade pulmonar é o principal risco), hemograma completo, função hepática e renal |
| Proteção no Manuseio | Necessário seguir os regulamentos de manuseio de citotóxicos |

## Considerações de Segurança

- **Toxicidade pulmonar**: a literatura recuperada descreve pneumonite intersticial associada à bleomicina e risco de toxicidade pulmonar, que aumenta com a idade e com radioterapia torácica associada. É particularmente relevante para indicações pulmonares.
- **Hipertermia**: há relato de reação hiperpirética fatal, o que motiva a recomendação de dose-teste antes do tratamento.
- **Interações medicamentosas**: foram identificadas 205 interações no total. As principais listadas incluem levofloxacino (menor) e, com gravidade não classificada, pantoprazol, palonosetrona, lactulose, aprepitanto, morfina, omeprazol, lansoprazol, vancomicina, prednisona, hidrocortisona, manitol, cloreto de potássio, prednisolona, ranitidina, granisetrona, ondansetrona, famotidina, claritromicina e metoclopramida.

Para advertências e contraindicações formais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Para neoplasia da cauda equina, a previsão se apoia apenas na pontuação do modelo, sem ensaios clínicos e sem estudo direto, além da baixa penetração da bleomicina no SNC.
- Nenhum registro está ativo no Brasil (todos os 5 estão cancelados).

**Panorama das demais indicações previstas:**

| Indicação prevista | Pontuação TxGNN | Nível de Evidência | Recomendação |
|------|------|------|------|
| Neoplasia da cauda equina | 99,30% | L5 | Hold |
| Tumor astrocítico do adulto | 99,28% | L3 | Questão de pesquisa |
| Sarcoma de células reticulares | 99,14% | L1 | Questão de pesquisa |
| Linfoma pulmonar primário | 99,10% | L4 | Questão de pesquisa |
| Blastoma pulmonar | 99,04% | L4 | Hold |
| Adenocarcinoma fetal bem diferenciado do pulmão | 99,03% | L5 | Hold |

- **Sarcoma de células reticulares (termo histórico para linfomas não Hodgkin)**: dois ensaios de Fase 3 concluídos (NCT00002565, NCT00002835) testaram regimes com bleomicina em linfoma, e relatos antigos descrevem seu uso em reticuloses. Porém, os ensaios compararam combinações e não isolam o efeito da bleomicina, e o tratamento padrão atual (R-CHOP, DA-EPOCH-R) não a inclui. O valor é sobretudo histórico.
- **Tumor astrocítico do adulto**: há um ensaio de Fase I de infusão intratumoral contínua em glioblastoma recorrente (PMID 12416544) e estudos antigos e pequenos; um estudo randomizado não mostrou potencialização da sobrevida com bleomicina (PMID 6164465). A barreira hematoencefálica exigiria administração local.
- **Linfoma pulmonar primário, blastoma pulmonar e adenocarcinoma fetal do pulmão**: evidência indireta ou inexistente, e a toxicidade pulmonar da bleomicina desfavorece o uso em doenças do pulmão.

**Para prosseguir, é necessário:**
- Obter a bula da ANVISA com advertências e contraindicações (lacuna de dados bloqueante para a triagem de segurança)
- Obter dados do mecanismo de ação (por exemplo, via DrugBank)
- Realizar revisão sistemática da literatura direcionada à neoplasia da cauda equina e a tumores espinhais
- Avaliar viabilidade de via de administração local (intratumoral ou intratecal), dada a baixa penetração no SNC
- Verificar a situação regulatória atual no Brasil, já que todos os registros foram cancelados
- Priorizar, se houver interesse em reposicionamento, a indicação em linfoma, com análise de que a bleomicina agrega valor frente aos regimes modernos
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

