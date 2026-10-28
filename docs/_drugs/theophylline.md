---
layout: default
title: Theophylline
parent: Apenas Predição do Modelo (L5)
nav_order: 629
evidence_level: L5
indication_count: 6
monitor_inn: "THEOPHYLLINE"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "pharyngitis", "acute laryngopharyngitis"]
last_modified_at: 2026-10-28
description: "Theophylline: nova indicação prevista, Doença trombótica (thrombotic disease) (nível de evidência L5). Indicação original: BRONCODILATADORES"
---

# Theophylline
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **6** 
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

## Theophylline: Doença trombótica (thrombotic disease)
{: .text-alpha }

## Resumo em Uma Frase

Teofilina é uma xantina usada originalmente como broncodilatador.
O modelo TxGNN prevê que pode ser eficaz para **doença trombótica (thrombotic disease)**, mas atualmente há **0 ensaios clínicos** e nenhuma publicação que estude a teofilina diretamente nesta doença. A previsão se apoia apenas no modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | BRONCODILATADORES |
| Nova Indicação Prevista | Doença trombótica (thrombotic disease) |
| Pontuação de Previsão TxGNN | 0.9962 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada. Segundo informações conhecidas, a teofilina é um inibidor não seletivo de fosfodiesterases e antagonista de receptores de adenosina. Sua eficácia como broncodilatador está registrada na licença brasileira.

Em teoria, a inibição de fosfodiesterases eleva o AMPc plaquetário, o que poderia reduzir a agregação plaquetária. Por outro lado, o antagonismo da adenosina atua contra o efeito antiplaquetário da própria adenosina. Os dois efeitos se opõem, e o benefício líquido é incerto.

A literatura recuperada não trata da teofilina no tratamento de trombose. Ela aborda a farmacocinética da ticlopidina, ensaios de biomarcadores plaquetários, o processamento de amostras para microRNA e um sensor para detecção de teofilina. A pontuação elevada do TxGNN é uma predição, sem suporte clínico nos dados compilados.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Nenhum dos artigos recuperados avalia a teofilina como tratamento de doença trombótica. Os mais relevantes por tipo estão listados abaixo, apenas como contexto.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Revisão | Clinical Pharmacokinetics | Farmacocinética da ticlopidina, antiplaquetário; não envolve teofilina |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Revisão | CRC Critical Reviews in Biochemistry | Papel de prostaglandinas, tromboxano A2 e prostaciclina na função plaquetária e na aterosclerose |
| [8318681](https://pubmed.ncbi.nlm.nih.gov/8318681/) | 1993 | Relato de caso | J Am Soc Nephrol | Eritrocitose pós-transplante renal e tratamentos; sem relação direta com teofilina |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Outro | General Pharmacology | Milrinona e adenosina inibem a resposta plaquetária via AMPc; estudo com outro fármaco |
| [32824700](https://pubmed.ncbi.nlm.nih.gov/32824700/) | 2020 | Outro | Cells | Efeito da anticoagulação e do processamento de amostras na quantificação de microRNA sanguíneo |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | Outro | Platelets | Medição de sCLEC-2 plasmático como marcador de ativação plaquetária |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 105530305 | TEOLONG | Não informada | Broncodilatadores |

## Considerações de Segurança

- **Contraindicações (relações registradas no grafo de conhecimento, não texto de bula):** hipertensão, insuficiência e doenças hepáticas, epilepsia, transtornos de ansiedade e psicóticos, porfiria, doença renal, doença da vesícula biliar, trombocitopenia, neutropenia e agranulocitose, hipotireoidismo, úlcera péptica, glaucoma de ângulo aberto, diabetes mellitus e cetoacidose diabética, hiperplasia prostática benigna e dermatite herpetiforme.
- **Interações Medicamentosas:** foram registradas 100 interações. A principal interação de gravidade maior listada é com **bupropiona**. As de gravidade moderada incluem famotidina, ranitidina, cimetidina, omeprazol, rabeprazol, claritromicina, doxiciclina, tetraciclina, minociclina, corticosteroides (hidrocortisona, dexametasona, betametasona, budesonida, triamcinolona), carvão ativado, picossulfato e polietilenoglicol. Efedrina tem interação de gravidade menor.
- A teofilina tem janela terapêutica estreita, e o monitoramento de níveis séricos costuma ser necessário.

Os dados de advertências e contraindicações da bula da ANVISA não estavam disponíveis na base compilada. Consulte a bula para informações de segurança completas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não há ensaios clínicos nem estudos que avaliem a teofilina diretamente em doença trombótica. A previsão do TxGNN (0,9962) não tem suporte clínico, e o mecanismo teórico é contraditório (inibição de fosfodiesterases versus antagonismo da adenosina). Além disso, a teofilina tem índice terapêutico estreito e muitas interações medicamentosas.

**Para prosseguir, é necessário:**
- Obter dados detalhados do mecanismo de ação (MOA).
- Obter e analisar a bula da ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança.
- Realizar estudos pré-clínicos e clínicos que avaliem a teofilina diretamente na agregação plaquetária e na trombose.
- Avaliar o perfil de segurança diante da interação com bupropiona e das contraindicações cardiovasculares e hematológicas registradas.

### Observação sobre outras indicações previstas

Outras previsões do TxGNN para a teofilina foram avaliadas, e todas estão em **Hold**:

- **Doença da cavidade nasal (nasal cavity disease, 0.9953):** um estudo clínico pequeno de provocação nasal com teofilina de liberação lenta em rinite alérgica (PMID 9648963), mais um modelo animal. A evidência é indireta e o nível é L5 pela regra do protocolo, pois não há ensaio de eficácia.
- **Doença traqueal (tracheal disease, 0.9949):** há relaxamento traqueal in vitro, revisões sobre metilxantinas na extubação de prematuros e um estudo veterinário retrospectivo em cães. Não há estudos em humanos com doença traqueal. Nível L5.
- **Pharyngitis (0.9946):** sem mecanismo plausível; a literatura trata de antibióticos macrolídeos. Nível L5.
- **Laringotraqueíte (0.9951) e laringofaringite aguda (0.9935):** sem ensaios nem literatura. Nível L5.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

