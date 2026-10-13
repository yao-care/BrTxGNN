---
layout: default
title: Filgrastim
parent: Apenas Predição do Modelo (L5)
nav_order: 317
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: De neutropenia constitucional a distúrbio de liberação plaquetária primário

## Resumo em Uma Frase

Filgrastim é um análogo do fator estimulador de colônias de granulócitos (G-CSF), originalmente usado em neutropenias constitucionais, como a neutropenia congênita grave e a hematopoese cíclica.
O modelo TxGNN prevê que pode ser eficaz para **distúrbio de liberação primário das plaquetas (primary release disorder of platelets)**, mas **não há ensaios clínicos nem publicações** apoiando essa previsão específica; trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Neutropenia constitucional, neutropenia congênita grave, hematopoese cíclica, neutropenia crônica familiar (segundo o grafo de conhecimento do TxGNN) |
| Nova Indicação Prevista | Distúrbio de liberação primário das plaquetas (primary release disorder of platelets) |
| Pontuação de Previsão TxGNN | 99,998% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o filgrastim é um análogo do G-CSF que atua sobre progenitores da linhagem neutrofílica por meio do receptor de G-CSF, e sua eficácia em neutropenias constitucionais está estabelecida.

A relação entre a indicação original e a nova é fraca. Os distúrbios de liberação plaquetária são defeitos intrínsecos da função das plaquetas, enquanto o filgrastim atua sobre a linhagem de neutrófilos. Não há mecanismo estabelecido que ligue o fármaco à correção desses defeitos. A pontuação alta do TxGNN (0,99998) reflete uma previsão baseada em grafo, sem respaldo de ensaios ou literatura.

**Outras indicações previstas (todas nível L5, decisão Hold):**

| Posição | Indicação prevista | Pontuação TxGNN | Observação |
|---|---|---|---|
| 2 | Pseudo-doença de von Willebrand | 99,997% | Defeito de ganho de função da GPIbα plaquetária; sem efeito conhecido do G-CSF |
| 3 | Trombastenia de Glanzmann | 99,996% | Deficiência da integrina αIIbβ3; fora da via do filgrastim |
| 4 | Síndrome de Scott | 99,956% | Defeito de TMEM16F/ANO6; sem conexão mecanística documentada |
| 5 | Distúrbio hemorrágico por trombocitopenia constitucional | 99,911% | G-CSF não impulsiona a megacariopoese; relevância apenas indireta |
| 6 | Diátese hemorrágica por defeito de receptor de colágeno | 99,910% | Sem ação conhecida sobre GPVI ou α2β1 |
| 7 | Deficiência de inibidor de C1 | 99,843% | Via do complemento/sistema de contato; sem papel do G-CSF |
| 8 | Serpinopatia com polimerização tóxica de serpina | 99,815% | Não atua sobre dobramento incorreto de proteínas |
| 9 | Trombocitopenia aloimune fetal e neonatal | 99,768% | Manejo baseado em IVIG e transfusão; G-CSF sem papel conhecido |
| 10 | Distúrbio hemorrágico do tipo plaquetário | 99,690% | Único com ensaios associados (indiretos, transplante) |

## Evidências de Ensaios Clínicos

Não há ensaios clínicos registrados para a indicação principal (distúrbio de liberação primário das plaquetas).

Para fins de contexto, o único item da lista com ensaios associados é o distúrbio hemorrágico do tipo plaquetário (posição 10). Os ensaios são de transplante de células-tronco hematopoéticas, nos quais o filgrastim tem papel de suporte. Todos foram classificados como de baixa relevância (grau C):

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00296023](https://clinicaltrials.gov/study/NCT00296023) | NA | Concluído | 25 | Transplante alogênico de células-tronco do sangue periférico em baixa dose para neoplasias hematológicas de baixo grau e alto risco; população com neoplasia, não com distúrbio plaquetário |
| [NCT00004232](https://clinicaltrials.gov/study/NCT00004232) | Phase 1 | Concluído | Não informado | Aumento da medula óssea com células CD34 enriquecidas em transplante alogênico para neoplasias hematológicas |
| [NCT00054236](https://clinicaltrials.gov/study/NCT00054236) | Phase 1 | Concluído | 55 | Transplante de múltiplas unidades de sangue de cordão após condicionamento não mieloablativo, em doenças hematológicas ou anemia aplástica grave |
| [NCT00301912](https://clinicaltrials.gov/study/NCT00301912) | Phase 2 | Retirado | 0 | Bussulfano e fludarabina como terapia preparatória em transplante de doador não aparentado compatível; retirado sem inclusão de participantes, sem dados |
| [NCT00295997](https://clinicaltrials.gov/study/NCT00295997) | NA | Desconhecido | 35 | Transplante alogênico não mieloablativo com doadores não aparentados compatíveis, para neoplasias hematológicas, carcinoma de células renais e anemia aplástica |
| [NCT00080925](https://clinicaltrials.gov/study/NCT00080925) | Phase 1 | Concluído | 20 | Transplante haploidêntico com depleção de células T e intensidade reduzida para neoplasias hematológicas |
| [NCT00004904](https://clinicaltrials.gov/study/NCT00004904) | Phase 1 | Concluído | Não informado | Transplante de doador parcialmente compatível com depleção de células T e células CD34 "veto" em megadose, para doenças hematológicas de alto risco |

## Informações de Comercialização no Brasil

O filgrastim não possui registros ativos nos dados compilados para este relatório (situação: não comercializado; 0 registros).

## Considerações de Segurança

**Interações Medicamentosas:** a consulta de interações foi concluída e identificou 100 interações no total. Os principais exemplos listados, todos de gravidade **moderada** (fonte: DDInter), incluem:

- Radiofármacos e anticorpos radiomarcados: iobenguano (I-131), fludesoxiglicose (18F), ibritumomabe tiuxetana, tositumomabe (I-131) e tositumomabe
- Quimioterápicos e antineoplásicos: levamisol, trimetrexato, mercaptopurina, paclitaxel, altretamina, trióxido de arsênio, asparaginase (E. coli), azacitidina, bendamustina
- Inibidores de quinase e outros alvos: abemaciclibe, acalabrutinibe, avapritinibe
- Imunoterapias e conjugados: aldesleucina, alentuzumabe, belantamabe mafodotina

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para distúrbio de liberação primário das plaquetas é apenas computacional (L5), sem ensaios nem literatura, e não há mecanismo plausível que ligue o G-CSF a defeitos intrínsecos da função plaquetária. Além disso, o fármaco não está comercializado no Brasil.

**Para prosseguir, é necessário:**
- Obter os dados de mecanismo de ação (MOA) para permitir análise da ligação mecanística
- Obter advertências e contraindicações da bula (ANVISA), indispensáveis para a triagem de segurança
- Realizar revisão sistemática da literatura e estudos pré-clínicos que sustentem um papel do filgrastim em distúrbios plaquetários
- Esclarecer a situação regulatória no Brasil, já que não há registros ativos
- Se houver interesse em outra indicação, priorizar o distúrbio hemorrágico do tipo plaquetário (posição 10, L4), embora a evidência seja apenas indireta, via contexto de transplante
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

