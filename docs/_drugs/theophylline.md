---
layout: default
title: Theophylline
parent: Apenas Predição do Modelo (L5)
nav_order: 629
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-13
description: "Theophylline: nova indicação prevista, Doença trombótica (thrombotic disease) (nível de evidência L5). Indicação original: Broncodilatadores"
monitor_inn: "THEOPHYLLINE"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "pharyngitis", "acute laryngopharyngitis"]
---

# Theophylline
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **7** 
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

# Teofilina: De broncodilatador para doença tromboembólica (doença trombótica)

> Nota: o relatório avalia a primeira indicação prevista (rank 1: doença trombótica), conforme as instruções. As demais previsões são mencionadas apenas quando necessário para contextualizar a leitura dos dados.

## Resumo em Uma Frase

A teofilina é um broncodilatador, registrado no Brasil como "BRONCODILATADORES", usado historicamente em doenças obstrutivas das vias aéreas.
O modelo TxGNN prevê que ela possa ser eficaz para **doença trombótica (thrombotic disease)**, mas **não há ensaios clínicos** e a literatura recuperada **não avalia a teofilina como tratamento** dessa condição. A previsão é puramente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Broncodilatadores |
| Nova Indicação Prevista | Doença trombótica (thrombotic disease) |
| Pontuação de Previsão TxGNN | 99,62% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações farmacológicas conhecidas, a teofilina é um inibidor não seletivo de fosfodiesterases (PDE) e antagonista de receptores de adenosina. Esses mecanismos explicam seu efeito broncodilatador.

Em teoria, a inibição de PDE eleva o AMPc nas plaquetas e poderia reduzir a agregação plaquetária, o que daria alguma plausibilidade biológica à previsão. Porém, o antagonismo da adenosina pode anular esse efeito, já que a própria adenosina tem ação antiplaquetária. O saldo mecanístico é, portanto, incerto.

A relação entre a indicação original (doença das vias aéreas) e a nova (trombose) é distante. A pontuação alta do modelo reflete proximidade na rede de conhecimento, sem respaldo clínico demonstrado.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para esta indicação.

## Evidências da Literatura

As publicações recuperadas não demonstram eficácia da teofilina em doença trombótica. Abaixo, as mais próximas do tema:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Revisão farmacocinética | Clinical Pharmacokinetics | Trata da ticlopidina (outro antiplaquetário), não da teofilina |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Revisão | CRC Critical Reviews in Biochemistry | Prostaglandinas, plaquetas e aterosclerose; não específica da teofilina |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Estudo in vitro | General Pharmacology | Milrinona e adenosina na inibição da resposta plaquetária humana (outro fármaco) |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | Método laboratorial | Platelets | Medição de CLEC-2 solúvel como marcador de ativação plaquetária |
| [29220362](https://pubmed.ncbi.nlm.nih.gov/29220362/) | 2017 | Método laboratorial | PLoS One | Preparo de plasma para monitorar moléculas plaquetárias |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Método laboratorial | British Journal of Haematology | Radioimunoensaio do fator plaquetário 4; a teofilina é usada apenas como componente do anticoagulante de coleta |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Método analítico | Analytica Chimica Acta | Biossensor para detecção de teofilina, sem relevância clínica |
| [4776567](https://pubmed.ncbi.nlm.nih.gov/4776567/) | 1973 | Estudo clínico antigo | Minerva Cardioangiologica | Derivado nicotinato de teofilina em arteriopatia periférica obliterante (sem resumo disponível) |

Nenhum dos estudos testa a teofilina como tratamento de trombose.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 105530305 (cancelado) | TEOLONG | Não informada | Broncodilatadores |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não extraídas da bula)**: hipertensão, insuficiência hepática, epilepsia, transtornos de ansiedade e psicóticos, porfiria, doença renal, doença hepática, doenças da vesícula biliar, trombocitopenia, hipotireoidismo, úlcera péptica, glaucoma de ângulo aberto, diabetes e cetoacidose diabética, hiperplasia prostática benigna, neutropenia e agranulocitose. Esta lista não substitui a bula.
- **Interações medicamentosas**: foram registradas 100 interações. Entre as exibidas, destaca-se a de **gravidade maior com bupropiona**. Há interações moderadas com antagonistas H2 e inibidores de bomba de prótons (famotidina, ranitidina, cimetidina, omeprazol, rabeprazol), tetraciclinas (doxiciclina, tetraciclina, minociclina), claritromicina, corticosteroides (hidrocortisona, dexametasona, betametasona, triamcinolona, budesonida), carvão ativado, picossulfato e polietilenoglicol. A interação com efedrina é de gravidade menor.
- **Índice terapêutico estreito**: a literatura recuperada para outras indicações reforça a necessidade de monitorização terapêutica.

Consulte a bula para advertências e contraindicações formais.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem pontuação alta no modelo, mas nenhum ensaio clínico e nenhuma literatura que sustente a teofilina como tratamento de doença trombótica. O mecanismo é ambíguo, porque o antagonismo da adenosina pode neutralizar o efeito antiplaquetário da inibição de PDE. O único registro no Brasil está cancelado.

**Para prosseguir, é necessário:**
- Dados de mecanismo de ação documentados e análise de como o balanço PDE/adenosina se comporta em plaquetas.
- Estudos pré-clínicos de agregação plaquetária e trombose com teofilina.
- Bula da ANVISA com advertências e contraindicações, para a triagem de segurança.
- Avaliação de viabilidade regulatória, dado que o registro está cancelado.

**Observação sobre outras previsões:** entre as indicações previstas, a doença pulmonar obstrutiva (rank 5) tem o maior respaldo clínico (nível L1), mas corresponde ao uso original do fármaco e não a um reposicionamento. Rinite alérgica/doença da cavidade nasal (rank 2) e doença traqueal (rank 4) têm evidência indireta (nível L3) e podem merecer avaliação como questões de pesquisa.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

