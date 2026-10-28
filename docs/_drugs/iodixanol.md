---
layout: default
title: Iodixanol
parent: Apenas Predição do Modelo (L5)
nav_order: 370
evidence_level: L5
indication_count: 2
monitor_inn: "Iodixanol"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis"]
last_modified_at: 2026-10-23
description: "Iodixanol: nova indicação prevista, Osteoartrite (nível de evidência L5). Indicação original: Não consta texto de indicação nos registros da ANVISA compilados para…"
---

# Iodixanol
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

## Iodixanol: De agente de contraste radiológico para osteoartrite
{: .text-alpha }

## Resumo em Uma Frase

Iodixanol é um meio de contraste radiográfico iodado, iso-osmolar, usado em exames de imagem. O modelo TxGNN prevê que ele possa ser eficaz para **osteoartrite**, mas atualmente há **0 ensaios clínicos** e **5 publicações**, todas sobre uso diagnóstico ou métodos de imagem e nenhuma sobre tratamento da doença.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta texto de indicação nos registros da ANVISA compilados para este relatório |
| Nova Indicação Prevista | Osteoartrite |
| Pontuação de Previsão TxGNN | 0,9907 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 5) |
| Número de Registros | 5 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação do iodixanol. Segundo informações conhecidas, ele é um contraste iodado iso-osmolar, usado para visualizar estruturas em exames de imagem, e não possui ação modificadora de doença conhecida.

A literatura recuperada trata do iodixanol como agente diagnóstico: tomografia computadorizada com contraste da cartilagem, difusão de nanopartículas e de solutos pela cartilagem e pela interface osteocondral, e um estudo in vitro sobre plasma rico em plaquetas. Nada disso demonstra efeito terapêutico na osteoartrite.

A pontuação alta do TxGNN (0,9907) vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica. Portanto, a previsão não tem sustentação mecanística nem clínica nos dados disponíveis.

Também foi prevista a artrite reumatoide (pontuação de 0,9900), mas o único artigo recuperado é um relato de caso sobre dessensibilização a outro contraste (iohexol), sem relação com tratamento. Essa previsão também não tem respaldo.

## Evidências da Literatura

Os estudos abaixo envolvem a osteoartrite ou a cartilagem, mas são metodológicos, computacionais ou in vitro. Nenhum avalia o iodixanol como tratamento.

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | Estudo metodológico de imagem | Annals of Biomedical Engineering | Agente de contraste duplo (nanopartículas e componente molecular) em tomografia com contagem de fótons para avaliar a saúde da cartilagem articular |
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | Estudo metodológico de imagem | Annals of Biomedical Engineering | Imagem de difusão de nanopartículas por tomografia e modelagem de elementos finitos para revelar a função da cartilagem |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | Estudo in vitro | Journal of Experimental Orthopaedics | Contrastes iodados não influenciaram a função do plasma rico em plaquetas em fase inicial in vitro |
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | Modelagem computacional | Journal of Biomechanics | Iodixanol (~1550 Da) usado como contraste de difusão neutra para estudar a permeabilidade da interface osteocondral em amostras equinas e humanas |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | Modelagem computacional | Journal of Biomechanics | Modelo de elementos finitos do transporte de solutos neutros pela interface osteocondral, com tomografia |

Para artrite reumatoide, a única publicação é o relato de caso [36628042](https://pubmed.ncbi.nlm.nih.gov/36628042/) (2022, Cureus) sobre dessensibilização ao contraste iohexol em paciente com amiloidose secundária à artrite reumatoide, sem relação com tratamento.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada | Situação |
|---------|------|------|-----------|------|
| Registro 183960002 | VISIPAQUE | Não informada | Não informada | Válido |
| Registro 172870392 | VISIPAQUE | Não informada | Não informada | Cancelado |
| Registro 178170099 | VISIPAQUE | Não informada | Não informada | Cancelado |
| Registro 120330010 | IODIXANOL | Não informada | Não informada | Cancelado |
| Registro 103940518 | VISIPAQUE | Não informada | Não informada | Cancelado |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 100 interações no total; abaixo, as principais de gravidade maior:
  - Metformina
  - Anfotericina B (incluindo as formulações lipídicas, lipossomal e de sulfato de colesterila)
  - Mesalazina, balsalazida, olsalazina e sulfassalazina
  - Vancomicina
  - Aminoglicosídeos: canamicina, neomicina e estreptomicina
  - Polimixina B
- Há também interação de gravidade moderada com manitol.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Nenhum estudo avalia o iodixanol como tratamento da osteoartrite. A literatura limita-se a seu uso como contraste em imagem, e a pontuação vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica. O nível de evidência é L5.

**Para prosseguir, é necessário:**
- Estudos pré-clínicos que demonstrem algum efeito terapêutico na osteoartrite, com hipótese mecanística plausível
- Dados de mecanismo de ação do fármaco
- Advertências e contraindicações da bula na ANVISA, para a triagem de segurança
- Avaliação de via de administração compatível (por exemplo, intra-articular), hoje não definida
- Dados de indicação aprovada nos registros brasileiros, que não constam nas informações compiladas
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

