---
layout: default
title: Iodixanol
parent: Apenas Predição do Modelo (L5)
nav_order: 370
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Iodixanol: nova indicação prevista, Suscetibilidade à osteoartrite (osteoarthritis susceptibility) (nível de evidência L5). Indicação original: Não disponível nos dados compilados"
---

# Iodixanol
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

# Iodixanol: De meio de contraste iodado para osteoartrite (previsão do modelo)

## Resumo em Uma Frase

Iodixanol é um meio de contraste iodado, usado em exames de imagem; os dados compilados para este relatório não trazem indicação aprovada registrada no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **suscetibilidade à osteoartrite (osteoarthritis susceptibility)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção específica.
As previsões seguintes, como osteoartrite e artrite reumatoide, também não têm suporte terapêutico real.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível nos dados compilados (sem registro na ANVISA); uso conhecido como meio de contraste para imagem |
| Nova Indicação Prevista | Suscetibilidade à osteoartrite (osteoarthritis susceptibility) |
| Pontuação de Previsão TxGNN | 99,16% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, o iodixanol é um meio de contraste radiológico iodado, de alta osmolaridade reduzida, usado para visualizar estruturas em exames de imagem e sem papel conhecido na modificação de doenças.

A pontuação do modelo é alta (99,16%), mas não há ensaios nem literatura que sustentem a previsão. Não existe vínculo mecanístico demonstrado entre o iodixanol e a suscetibilidade genética à osteoartrite. Muito provavelmente, trata-se de um artefato do grafo de conhecimento, e não de um sinal terapêutico real.

Para a segunda previsão, **osteoartrite** (99,07%), a literatura recuperada mostra o iodixanol apenas como sonda de imagem e de difusão na cartilagem (tomografia computadorizada, modelagem de transporte de solutos na interface osteocondral) e em um estudo in vitro de compatibilidade com plasma rico em plaquetas. Isso indica uso diagnóstico, não efeito terapêutico. A associação do fármaco com imagem de cartilagem no grafo explica provavelmente a pontuação alta.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Para a indicação principal (suscetibilidade à osteoartrite), não há literatura relacionada. Abaixo, a literatura recuperada para a previsão vizinha de **osteoartrite**:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | Método de imagem/diagnóstico | Annals of Biomedical Engineering | Imagem de difusão de nanopartículas por tomografia e elementos finitos para revelar a função da cartilagem |
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | Método de imagem/diagnóstico | Annals of Biomedical Engineering | Agente de contraste duplo (nanopartícula + molecular) em tomografia com contagem de fótons para avaliar a saúde da cartilagem articular |
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | Estudo experimental/computacional | Journal of Biomechanics | Iodixanol (~1550 Da) usado para estudar a permeabilidade da interface osteocondral em amostras equinas e humanas |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | Modelagem computacional | Journal of Biomechanics | Modelo de elementos finitos do transporte de solutos neutros através da cartilagem e da placa óssea subcondral |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | Estudo in vitro | Journal of Experimental Orthopaedics | Contrastes iodados não alteraram a função do plasma rico em plaquetas em fase precoce in vitro |

Para **artrite reumatoide** (previsão rank 3), há apenas um relato de caso ([36628042](https://pubmed.ncbi.nlm.nih.gov/36628042/), 2022, Cureus) sobre dessensibilização ao iohexol, outro contraste, sem relação com eficácia terapêutica nem com o iodixanol.

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 100 interações no total. As de gravidade **Major** incluem:
  - Metformina
  - Anfotericina B (e formulações lipídica, de sulfato de colesterila e lipossomal)
  - Mesalazina, balsalazida, olsalazina e sulfassalazina
  - Vancomicina
  - Aminoglicosídeos (canamicina, neomicina, estreptomicina)
  - Polimixina B

  A interação com manitol é de gravidade **Moderada**. Várias outras (por exemplo, famotidina, ácido acetilsalicílico, morfina, omeprazol e prednisona) estão sem classificação de gravidade.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Todas as previsões têm nível de evidência L5, sem ensaios clínicos. A literatura disponível trata o iodixanol como agente de imagem, não como tratamento, e não há mecanismo plausível. O fármaco também não tem registro vigente no Brasil.

**Para prosseguir, é necessário:**
- Dados de bula da ANVISA (advertências e contraindicações), hoje ausentes
- Dados do mecanismo de ação, hoje ausentes
- Evidência pré-clínica ou clínica de efeito terapêutico (não diagnóstico) em osteoartrite, antes de qualquer reconsideração
- Esclarecer a situação regulatória do iodixanol no Brasil (sem registro nos dados compilados)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

