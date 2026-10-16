---
layout: default
title: Aztreonam
parent: Apenas Predição do Modelo (L5)
nav_order: 103
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Aztreonam: nova indicação prevista, Síndrome de hiperviscosidade policlonal (polyclonal hyperviscosity sy… (nível de evidência L5). Indicação original: Infecção do trato urinário, infecção por Pseudo…"
---

# Aztreonam
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

# Aztreonam: De infecções por bactérias gram-negativas à síndrome de hiperviscosidade policlonal

## Resumo em Uma Frase

Aztreonam é um antibiótico monobactâmico, originalmente usado em infecções por bactérias gram-negativas, como infecção do trato urinário, infecção por *Pseudomonas aeruginosa*, peritonite e infecção por *Escherichia coli*.
O modelo TxGNN prevê que pode ser eficaz para **síndrome de hiperviscosidade policlonal (polyclonal hyperviscosity syndrome)**, mas **não há ensaios clínicos nem publicações** apoiando esta previsão. A pontuação alta parece ser um artefato do grafo de conhecimento.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecção do trato urinário, infecção por *Pseudomonas aeruginosa*, peritonite, rinoscleroma, infecção por *E. coli*, endometrite (segundo o grafo de conhecimento do TxGNN; não há texto de indicação registrado no Brasil) |
| Nova Indicação Prevista | Síndrome de hiperviscosidade policlonal (polyclonal hyperviscosity syndrome) |
| Pontuação de Previsão TxGNN | 99,73% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o aztreonam é um monobactâmico que inibe a síntese da parede celular bacteriana ao se ligar à PBP3 em aeróbios gram-negativos, e sua eficácia em infecções como as do trato urinário e a peritonite está estabelecida.

Para a nova indicação, **não existe um vínculo mecanístico plausível**. A síndrome de hiperviscosidade é um distúrbio hematológico, ligado a proteínas, e não uma infecção. A pontuação elevada do TxGNN (99,73%) parece refletir apenas proximidade na rede do grafo, sem respaldo em ensaios ou literatura.

Outras previsões do mesmo modelo também têm pontuações muito altas. Entre elas, a **uretrite gonocócica** (99,59%) é a única biologicamente plausível, com atividade contra *Neisseria gonorrhoeae*. Ela é apresentada abaixo como alternativa de pesquisa, mas a indicação principal deste relatório permanece a de maior pontuação.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para a síndrome de hiperviscosidade policlonal.

## Evidências da Literatura

Atualmente não há literatura relacionada para a síndrome de hiperviscosidade policlonal.

## Outras Previsões Relevantes (Para Referência)

| Indicação Prevista | Pontuação | Nível | Comentário |
|------|------|------|------|
| Uretrite gonocócica | 99,59% | L3 | Plausível; estudos de braço único e não randomizados (incluindo um ensaio aberto de 2020 com 2 g IM, PMID [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/)) mostram eficácia; há relatos de resistência |
| Epiglotite | 99,53% | L4 | Evidência indireta (série pediátrica de 1986, PMID [3766490](https://pubmed.ncbi.nlm.nih.gov/3766490/)) |
| Gamopatia monoclonal | 99,50% | L4 | Apenas uso de suporte em infecções de pacientes hematológicos (PMID [4079014](https://pubmed.ncbi.nlm.nih.gov/4079014/)) |
| Uretrite por *Ureaplasma* | 99,59% | L5 | Mecanismo contradito: *Ureaplasma* não tem parede celular |
| Pielonefrite xantogranulomatosa | 99,49% | L5 | Plausível, mas sem evidência específica; o tratamento definitivo costuma ser cirúrgico |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento** (não são texto de bula): doença renal, piureter, doença hepática, doença da vesícula biliar, colite por *Clostridium difficile*, enterocolite necrosante perinatal e doença brônquica.
- **Interações Medicamentosas**: foram identificadas 27 interações no total. As de nível moderado são com **ácido picosulfúrico**, **dicumarol** e **varfarina** (atenção ao monitoramento da coagulação). As demais, entre elas vancomicina, anfotericina B, amicacina, tacrolimo, heparina, ácido acetilsalicílico, morfina, inibidores de bomba de prótons (omeprazol, pantoprazol, lansoprazol), metronidazol, fluconazol, aciclovir e corticoides, têm gravidade não classificada.

Consulte a bula para as advertências e contraindicações oficiais.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para síndrome de hiperviscosidade policlonal não tem vínculo mecanístico, ensaios nem literatura (nível L5). O aztreonam não está comercializado no Brasil.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), pois a triagem de segurança não pôde ser concluída.
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank).
- Se houver interesse em reposicionamento, redirecionar a análise para a **uretrite gonocócica**, a candidata mais plausível. Isso exigiria ensaios controlados e randomizados, avaliação de resistência e comparação com as alternativas das diretrizes atuais.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

