---
layout: default
title: Piroxicam
parent: Apenas Predição do Modelo (L5)
nav_order: 529
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Piroxicam: nova indicação prevista, Síndrome de microftalmia colobomatosa-displasia rizomélica (primeira… (nível de evidência L5). Indicação original: Artrite reumatoide, osteoartrite, artropatia"
monitor_inn: "Piroxicam"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "WHIM syndrome", "rheumatoid nodulosis", "juvenile idiopathic arthritis"]
---

# Piroxicam
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

## Piroxicam: Da artrite reumatoide à artrite idiopática juvenil
{: .text-alpha }

## Resumo em Uma Frase

Piroxicam é um anti-inflamatório não esteroidal (AINE) originalmente usado no tratamento da artrite reumatoide, da osteoartrite e de outras artropatias.
Entre as indicações previstas pelo modelo TxGNN, a que tem maior sustentação nos dados é a **Artrite Idiopática Juvenil (Juvenile Idiopathic Arthritis)**, com **11 publicações** e **nenhum ensaio clínico registrado**. As demais previsões de maior pontuação (doenças genéticas raras do esqueleto) não têm nenhuma evidência.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Artrite reumatoide, osteoartrite, artropatia |
| Nova Indicação Prevista | Síndrome de microftalmia colobomatosa-displasia rizomélica (primeira da lista por pontuação). A mais bem sustentada é a Artrite Idiopática Juvenil (10ª na lista) |
| Pontuação de Previsão TxGNN | 99,996% (primeira da lista); 99,93% (artrite idiopática juvenil) |
| Nível de Evidência | L5 (primeira da lista); L3 (artrite idiopática juvenil) |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold (primeira da lista); Hold com questão de pesquisa para artrite idiopática juvenil |

> **Observação:** a indicação classificada em primeiro lugar pelo TxGNN não tem qualquer evidência de apoio nem plausibilidade biológica. Por isso, este relatório detalha a evidência da **artrite idiopática juvenil**, a única previsão com literatura relevante. As indicações originais vêm das relações de indicação do grafo de conhecimento do TxGNN (PrimeKG), e não de texto de bula.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o piroxicam é um inibidor não seletivo da ciclo-oxigenase (COX), com efeito anti-inflamatório e analgésico, e sua utilidade em artrite reumatoide e osteoartrite é reconhecida.

A artrite idiopática juvenil é uma doença inflamatória articular muito próxima da artrite reumatoide, indicação original do fármaco. A inibição da COX é compatível com o controle sintomático da inflamação articular, o que sustenta a previsão. Trata-se, porém, de controle de sintomas, e não de modificação da doença.

Para as demais previsões de topo, a análise dos dados não encontrou vínculo mecanístico:

- **Displasias esqueléticas e síndromes congênitas** (microftalmia colobomatosa-displasia rizomélica, braquidactilia-sindactilia, displasia acromesomélica tipo Hunter-Thompson, braquiolmia, braquiolmia-amelogênese imperfeita): têm base genética do desenvolvimento, sem relação conhecida com a inibição da COX. A pontuação alta provavelmente reflete proximidade no grafo com termos de artropatia.
- **Pseudoacondroplasia**: o vínculo é apenas indireto e fraco (AINEs para dor articular sintomática).
- **Miosclerose e síndrome WHIM**: sem dados que apoiem a relação.
- **Nodulose reumatoide**: há associação plausível com a artrite reumatoide, mas sem estudos específicos, e AINEs não tratam a formação de nódulos.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Publicações relativas à artrite idiopática juvenil, priorizando as mais diretamente ligadas ao piroxicam e as revisões sistemáticas:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [38680254](https://pubmed.ncbi.nlm.nih.gov/38680254/) | 2024 | Revisão sistemática/meta-análise em rede | World J Clin Cases | Compara diferentes AINEs na artrite idiopática juvenil; busca definir o método ideal, ainda não estabelecido |
| [33632948](https://pubmed.ncbi.nlm.nih.gov/33632948/) | 2021 | Revisão sistemática/meta-análise em rede | Indian Pediatrics | Compara eficácia e segurança de nove AINEs em pacientes com artrite idiopática juvenil |
| [2957205](https://pubmed.ncbi.nlm.nih.gov/2957205/) | 1987 | Estudo clínico randomizado | Eur J Rheumatol Inflamm | 26 pacientes (3 a 25 anos) com artrite reumatoide juvenil receberam piroxicam ou naproxeno; houve redução significativa do número de articulações dolorosas e inchadas |
| [3510686](https://pubmed.ncbi.nlm.nih.gov/3510686/) | 1986 | Estudo multicêntrico comparativo | Br J Rheumatol | Estudo duplo-cego cruzado de 8 semanas com 47 crianças com artrite crônica juvenil soronegativa: sem diferença significativa entre piroxicam e naproxeno; discute dificuldades dos ensaios com AINEs na infância |
| [1782984](https://pubmed.ncbi.nlm.nih.gov/1782984/) | 1991 | Farmacocinética | Eur J Clin Pharmacol | 10 crianças (7 a 16 anos) com dose média de 0,4 mg/kg/dia; meia-vida média de cerca de 32,6 h, compatível com dose única diária |
| [9890680](https://pubmed.ncbi.nlm.nih.gov/9890680/) | 1998 | Estudo de coorte | Clin Rheumatol | Descreve a toxicidade a longo prazo de antirreumáticos e anti-inflamatórios em crianças atendidas em clínica de reumatologia pediátrica |
| [2185374](https://pubmed.ncbi.nlm.nih.gov/2185374/) | 1990 | Revisão | Kinderarztl Prax | Discute a terapia medicamentosa da artrite crônica juvenil, incluindo o piroxicam como medicamento novo |

Outras revisões (nabumetona, oxaprozina, pirprofeno e sistemas de liberação de AINEs) são apenas indiretamente relevantes e não foram detalhadas.

## Informações de Comercialização no Brasil

O piroxicam consta como **não comercializado** e sem registros nos dados compilados para este relatório.

## Considerações de Segurança

- **Contraindicações (grafo de conhecimento, não texto de bula):** hipertensão, doença renal, doença hepática (incluindo insuficiência hepática aguda, hepatite e lesão hepática induzida por fármacos), doença da vesícula biliar, insuficiência cardíaca congestiva, doenças cardiovasculares (infarto do miocárdio, trombose coronariana, AVC, infarto cerebral, doença cerebrovascular), distúrbios da coagulação, doença trombótica, úlcera péptica ativa, anemias e hemoglobinopatias, abuso/dependência de substâncias e distúrbios visuais.
- **Interações medicamentosas (100 registradas; principais):**
  - Moderadas: ácido acetilsalicílico, corticoides (hidrocortisona, dexametasona, betametasona, budesonida, triancinolona), metformina, glimepirida, clorpropamida, mesalazina, balsalazida, aprepitanto, citrato e bicarbonato de potássio, ácido picossulfúrico e polietilenoglicol com eletrólitos.
  - Leves: famotidina, ranitidina, cimetidina e linaclotida.
- **Uso pediátrico:** a segurança gastrointestinal e renal de AINEs em crianças exige atenção especial.

As advertências e contraindicações da bula da ANVISA não estão disponíveis; consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold** (para as previsões de topo); **questão de pesquisa** para a artrite idiopática juvenil.

**Justificativa:**
- As dez indicações previstas têm pontuação TxGNN muito alta (acima de 99,9%), mas nove delas não têm ensaios nem literatura e, na maioria, nenhum vínculo biológico plausível. A artrite idiopática juvenil tem estudos com piroxicam e meta-análises de AINEs, porém antigos, pequenos e sem ensaios registrados. Por isso o nível é L3, e não L1/L2.
- Não há registro no Brasil, o que também dificulta qualquer avanço regulatório.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), lacuna de dados bloqueante para a triagem de segurança.
- Complementar os dados do mecanismo de ação (consulta ao DrugBank).
- Avaliar nas meta-análises de 2021 e 2024 o desempenho específico do piroxicam frente a outros AINEs na artrite idiopática juvenil.
- Definir a situação regulatória e a via de acesso do piroxicam no Brasil, já que não está comercializado.
- Elaborar um plano de segurança pediátrica (trato gastrointestinal, função renal e hepática).
- Descartar as previsões sem vínculo biológico (displasias e síndromes genéticas) ou revisá-las apenas com novas evidências.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

