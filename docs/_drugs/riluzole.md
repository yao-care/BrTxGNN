---
layout: default
title: Riluzole
parent: Apenas Predição do Modelo (L5)
nav_order: 567
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Riluzole: nova indicação prevista, Polimicrogiria parieto-occipital parassagital bilateral (bilateral pa… (nível de evidência L5). Indicação original: Outros produtos que atuam sobre o sistema nervos"
monitor_inn: "riluzole"
predicted_indications: ["bilateral parasagittal parieto-occipital polymicrogyria", "axial spondylometaphyseal dysplasia", "lower motor neuron syndrome with late-adult onset", "trichomegaly-retina pigmentary degeneration-dwarfism syndrome", "lethal arthrogryposis-anterior horn cell disease syndrome", "monomelic amyotrophy", "Mills syndrome", "autosomal dominant mitochondrial myopathy with exercise intolerance", "amyotrohpic lateral sclerosis type 22"]
---

# Riluzole
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

# Riluzol: Do sistema nervoso a uma malformação cortical rara (polimicrogiria parieto-occipital parassagital bilateral)

## Resumo em Uma Frase

Riluzol foi registrado no Brasil na categoria "outros produtos que atuam sobre o sistema nervoso" e é conhecido como tratamento da esclerose lateral amiotrófica (ELA).
O modelo TxGNN prevê que pode ser eficaz para **polimicrogiria parieto-occipital parassagital bilateral (bilateral parasagittal parieto-occipital polymicrogyria)**, mas **não há ensaios clínicos nem publicações** apoiando esta previsão específica; trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outros produtos que atuam sobre o sistema nervoso |
| Nova Indicação Prevista | Polimicrogiria parieto-occipital parassagital bilateral (bilateral parasagittal parieto-occipital polymicrogyria) |
| Pontuação de Previsão TxGNN | 99,99% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Somente registros cancelados |
| Número de Registros | 8 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o riluzol modula a transmissão glutamatérgica e reduz a excitotoxicidade, e é o tratamento de referência para a ELA.

Para a polimicrogiria parieto-occipital parassagital, porém, **não há vínculo mecanístico sustentado pelos dados**. Trata-se de uma malformação do desenvolvimento cortical, e a ação do riluzol sobre a excitotoxicidade não tem relevância demonstrada para ela. A pontuação muito alta provavelmente reflete um artefato do grafo de conhecimento, e não um sinal biológico real.

Outras previsões do modelo são mais plausíveis por analogia com a ELA, como a síndrome do neurônio motor inferior de início tardio, a síndrome de Mills e a amiotrofia monomélica. Ainda assim, nenhuma delas conta com ensaios ou literatura nos dados compilados.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada para a indicação prevista principal.

## Informações de Comercialização no Brasil

Todos os 8 registros estão cancelados; não há produto atualmente comercializado.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 126250104 | LFM-RILUZOL | Não informada | Outros produtos que atuam sobre o sistema nervoso |
| Registro 102351037 | RILUZOL | Não informada | Outros produtos que atuam sobre o sistema nervoso |
| Registro 126250103 | RILUZOL | Não informada | Outros produtos que atuam sobre o sistema nervoso |
| Registro 146820031 | RILUZOL | Não informada | Outros produtos que atuam sobre o sistema nervoso |
| Registro 102980402 | RILUZOL | Não informada | Outros produtos que atuam sobre o sistema nervoso |

## Considerações de Segurança

- **Contraindicações (associações do grafo de conhecimento, não texto de bula)**: neutropenia, agranulocitose, abuso/dependência de substâncias, hiperbilirrubinemia (inclusive hereditária), síndrome de Gilbert, doença pulmonar intersticial e lesão hepática induzida por fármacos.
- **Interações Medicamentosas**: 44 interações identificadas. Entre as listadas, as de gravidade **moderada** incluem ácido obeticólico, naltrexona, deferasirox, osilodrostato, anagrelida, asparaginase (E. coli), brentuximabe vedotina, clofarabina, metotrexato e epirrubicina. As de gravidade leve incluem omeprazol, cafeína, teofilina e aminofilina.
- **Contexto hepático**: a literatura compilada indica que cerca de 50% dos pacientes com ELA em uso de riluzol oral apresentam ALT acima do limite superior da normalidade (8% acima de 3× e 2% acima de 5×), o que reforça a necessidade de monitorar a função hepática.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para polimicrogiria parieto-occipital parassagital bilateral é apenas computacional (nível L5), sem ensaios, sem literatura e sem vínculo mecanístico plausível.
- Além disso, não há registro ativo do riluzol no Brasil (todos os 8 estão cancelados), e faltam dados de bula sobre advertências e contraindicações.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações).
- Completar os dados do mecanismo de ação (por exemplo, via DrugBank).
- Realizar estudos pré-clínicos ou de mecanismo que justifiquem a relação entre riluzol e a polimicrogiria.
- Avaliar candidatas mais plausíveis por analogia com a ELA (síndrome do neurônio motor inferior de início tardio, síndrome de Mills, amiotrofia monomélica), buscando ensaios ou literatura específicos.
- Verificar de forma independente as evidências do riluzol na ELA (por exemplo, ensaios pivotais de Fase 3), sem extrapolá-las para subtipos genéticos específicos.
- Esclarecer a situação regulatória: motivos dos cancelamentos e possibilidade de novo registro.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

