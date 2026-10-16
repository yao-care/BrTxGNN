---
layout: default
title: Relebactam
parent: Apenas Predição do Modelo (L5)
nav_order: 562
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Relebactam: nova indicação prevista, Síndrome de hiperviscosidade policlonal (polyclonal hyperviscosity sy… (nível de evidência L5). Indicação original: Infecção do trato urinário e pielonefrite"
monitor_inn: "Relebactam"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "hematopoietic and lymphoid system neoplasm", "congenital hematological disorder", "septicemic plague"]
---

# Relebactam
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

# Relebactam: Da infecção do trato urinário à síndrome de hiperviscosidade policlonal

## Resumo em Uma Frase

Relebactam é um inibidor de beta-lactamases, usado em associação com imipenem/cilastatina e originalmente indicado para infecção do trato urinário e pielonefrite.
O modelo TxGNN prevê que pode ser eficaz para **síndrome de hiperviscosidade policlonal (polyclonal hyperviscosity syndrome)**, mas **não há ensaios clínicos nem publicações** que apoiem esta previsão. Trata-se apenas de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecção do trato urinário e pielonefrite (segundo as relações do grafo de conhecimento do TxGNN; não há texto de indicação de registro na ANVISA) |
| Nova Indicação Prevista | Síndrome de hiperviscosidade policlonal (polyclonal hyperviscosity syndrome) |
| Pontuação de Previsão TxGNN | 99,22% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada. Segundo informações conhecidas, o relebactam é um inibidor de beta-lactamases das classes A e C (serina beta-lactamases), sem atividade antibacteriana intrínseca. É usado em combinação com imipenem/cilastatina para proteger o carbapenêmico da degradação enzimática em infecções por bactérias Gram-negativas.

Na prática, **esta previsão não parece razoável do ponto de vista biológico**. A hiperviscosidade causada pela elevação policlonal de imunoglobulinas não depende de nenhuma via relacionada às beta-lactamases, e não foi identificado nenhum vínculo mecanístico plausível. A pontuação alta provavelmente reflete artefatos do grafo de conhecimento, e não uma relação biológica real.

### Outras previsões do modelo

As demais previsões de alta pontuação também não têm respaldo em ensaios clínicos ou literatura (todas L5, exceto a última):

| Posição | Doença prevista | Pontuação | Avaliação |
|------|------|------|------|
| 2 | Hiperamilasemia | 99,22% | Sem justificativa mecanística; reflete lesão pancreática/salivar ou redução da depuração |
| 3 | Analbuminemia congênita | 99,08% | Distúrbio genético (mutações em ALB); sem efeito plausível |
| 4 | Incompatibilidade de grupo sanguíneo | 98,92% | Processo imunomediado por aloanticorpos; pontuação provavelmente por proximidade na rede |
| 5 | Doença hematológica pré-maligna | 98,81% | Sem vínculo mecanístico |
| 6 | Gamopatia monoclonal | 98,76% | Sem atividade conhecida sobre plasmócitos |
| 7 | Doença hematológica associada a neuropatia periférica adquirida | 98,59% | Sem mecanismo plausível |
| 8 | Neoplasia do sistema hematopoiético e linfoide | 98,48% | Sem ação antineoplásica; no máximo, suporte contra infecções em neutropênicos |
| 9 | Distúrbio hematológico congênito | 98,39% | Sem justificativa mecanística |
| 10 | Peste septicêmica | 97,94% | **Única com racional antibacteriano coerente (L4)**; classificada como questão de pesquisa |

Sobre a peste septicêmica: *Yersinia pestis* é um patógeno Gram-negativo e o imipenem tem atividade in vitro contra muitos Gram-negativos. Contudo, *Y. pestis* normalmente não apresenta resistência mediada por beta-lactamases, de modo que o benefício adicional do relebactam é incerto. Seriam necessários dados in vitro e em modelos animais antes de qualquer avanço.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Considerações de Segurança

Consulte a bula para informações de segurança. Não há dados compilados de advertências, contraindicações ou interações medicamentosas para este fármaco.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão principal (síndrome de hiperviscosidade policlonal) não tem ensaios, literatura nem mecanismo plausível; a pontuação alta do TxGNN provavelmente é um artefato do grafo de conhecimento. O relebactam não está comercializado no Brasil.

**Para prosseguir, é necessário:**
- Obter e analisar a bula (advertências e contraindicações), pois a ausência desses dados impede a triagem de segurança.
- Complementar os dados de mecanismo de ação.
- Se houver interesse em uma linha de pesquisa, priorizar a peste septicêmica, com estudos in vitro e em modelos animais antes de qualquer avaliação clínica.
- Verificar a compatibilidade de vias de administração e a situação regulatória do medicamento no Brasil.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

