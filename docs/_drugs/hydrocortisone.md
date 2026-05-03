---
layout: default
title: Hydrocortisone
parent: 僅模型預測 (L5)
nav_order: 274
evidence_level: L5
indication_count: 10
---

# Hydrocortisone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Usando o skill `txgnn-pipeline` para orientação sobre o pipeline de relatórios. Procedendo agora com a geração do relatório a partir do Evidence Pack.

---

# Hidrocortisona: De condições inflamatórias à alopecia areata

## Resumo em Uma Frase

Hidrocortisona é um glucocorticoide amplamente utilizado no controle de insuficiência adrenal, condições inflamatórias e alérgicas, e diversas dermatoses.
O modelo TxGNN prevê que pode ser eficaz para **Alopecia Areata (alopecia areata / pelada)**,
atualmente com **4 ensaios clínicos** e **20 publicações** apoiando esta direção.
A previsão é sustentada por um ensaio de Fase 3 concluído que comparou diretamente a hidrocortisona 1% com clobetasol em crianças com esta condição.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não registrado no Brasil (uso farmacológico reconhecido: insuficiência adrenal; tópico: condições inflamatórias cutâneas) |
| Nova Indicação Prevista | Alopecia Areata (*alopecia areata* / pelada) |
| Pontuação de Previsão TxGNN | 99,97% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

A hidrocortisona é a forma sintética do cortisol — o principal glucocorticoide endógeno do córtex adrenal. Embora os dados detalhados de mecanismo de ação (MOA) não estejam disponíveis no Evidence Pack atual, seu mecanismo é amplamente estabelecido na literatura: a hidrocortisona se liga a receptores intracelulares de glucocorticoide (GR), inibindo a fosfolipase A2 e suprimindo a produção de citocinas pró-inflamatórias como IL-1, TNF-α e IL-6. Isso resulta em potente modulação da resposta imune local e sistêmica.

A alopecia areata é uma doença autoimune mediada por linfócitos CD8+, que atacam a zona de "privilégio imunológico" do folículo piloso, interrompendo o ciclo capilar normal. A hidrocortisona tópica atua suprimindo o microambiente inflamatório perifolicular, contribuindo para restaurar esse privilégio imunológico local. Corticosteroides de maior potência (como clobetasol 0,05%) demonstram eficácia clínica superior à hidrocortisona 1%, porém esta última apresenta vantagens de segurança relevantes em crianças, em áreas de pele delicada e em casos leves, onde os riscos de atrofia cutânea e supressão do eixo HPA devem ser minimizados.

A ligação mecanística entre a indicação farmacológica conhecida (modulação inflamatória e imunológica) e a nova indicação prevista (alopecia areata de base autoimune) é direta e biologicamente plausível: ambas compartilham o mesmo alvo primário dos glucocorticoides — a regulação de vias inflamatórias e imunomediadas.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | Concluído | 41 | RCT direto comparando hidrocortisona 1% creme vs. clobetasol propionato 0,05% creme em crianças com alopecia areata (2002–2003); estudo de referência para uso de esteroide de baixa potência nesta indicação pediátrica |
| [NCT06551818](https://clinicaltrials.gov/study/NCT06551818) | NA | Ainda não recrutando | 72 | Estudo dose-resposta de quatro braços, duplo-cego, randomizado, placebo-controlado avaliando formulações de produtos para crescimento capilar em alopecia androgênica Grau I–III; potencial inclusão de formulações com hidrocortisona |
| [NCT00484679](https://clinicaltrials.gov/study/NCT00484679) | Phase 2 | Concluído | 18 | Avalia o impacto da triancinolona acetonida intralesional sobre a função adrenal em pacientes com alopecia areata; relevante indiretamente para o monitoramento do eixo HPA no uso de corticosteroides intralesionais |
| [NCT04343560](https://clinicaltrials.gov/study/NCT04343560) | N/A | Concluído | 380 | Estudo do impacto do metaboloma esteroidal anormal sobre qualidade óssea, densidade e composição corporal em pacientes com secreção autônoma de cortisol; referência de segurança para uso crônico de glicocorticoides |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [24226568](https://pubmed.ncbi.nlm.nih.gov/24226568/) | 2014 | RCT | JAMA Dermatology | Ensaio clínico randomizado comparando clobetasol propionato 0,05% vs. hidrocortisona 1% em crianças com alopecia areata; evidência direta da eficácia e do perfil de segurança da hidrocortisona nesta indicação pediátrica |
| [38501938](https://pubmed.ncbi.nlm.nih.gov/38501938/) | 2024 | Revisão Sistemática | Clinical and Experimental Dermatology | Análise de eficácia e segurança de corticosteroide tópico sob oclusão para alopecia areata grave (incluindo alopecia total e universal) em crianças; avalia opções terapêuticas em casos refratários |
| [36718837](https://pubmed.ncbi.nlm.nih.gov/36718837/) | 2023 | Revisão Sistemática / Meta-análise | Journal of Cosmetic Dermatology | Meta-análise sobre laser fracionado (isolado ou combinado) para alopecia areata; contextualiza o cenário terapêutico atual onde corticosteroides tópicos continuam sendo base de tratamento |
| [28516731](https://pubmed.ncbi.nlm.nih.gov/28516731/) | 2017 | Revisão / Hipótese | Journal of the European Academy of Dermatology and Venereology | Investiga se a hiperatividade do eixo HPA é um mito em pacientes com alopecia areata; avalia os níveis de cortisol e MSH, com implicações para o uso racional de glucocorticoides |
| [39506493](https://pubmed.ncbi.nlm.nih.gov/39506493/) | 2025 | Estudo Clínico Exploratório | Journal of Cosmetic Dermatology | Estresse psicológico crônico e envelhecimento cutâneo; documenta a liberação de cortisol e epinefrina como mediadores em dermatoses incluindo alopecia areata, psoriase e dermatite atópica |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Série de Casos Histórica | Medical Times | Um dos primeiros relatos de tratamento de alopecia areata, parcial e total com cortisona, hidrocortisona, prednisona e prednisolona; estabelece o uso de hidrocortisona nesta indicação desde a década de 1950 |
| [13610145](https://pubmed.ncbi.nlm.nih.gov/13610145/) | 1958 | Estudo Clínico | Der Hautarzt | Crescimento capilar em alopecia areata e maligna após injeção intracutânea de hidrocortisona; documentação histórica precoce da via intralesional |
| [5989830](https://pubmed.ncbi.nlm.nih.gov/5989830/) | 1966 | Estudo Clínico | Vestnik Dermatologii | Tratamento de alopecia areata e alopecia total por injeções intracutâneas de hidrocortisona; série de casos sobre eficácia da formulação intralesional |
| [14158891](https://pubmed.ncbi.nlm.nih.gov/14158891/) | 1963 | Estudo Clínico | Actas Dermo-Sifiliograficas | Tratamento de alopecia areata com injeções intradérmicas de hidrocortisona; relato de resultados com a via de administração intradermal |
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | Relato de Caso | Journal of the American Academy of Dermatology | Quatro casos de alopecia areata congênita com seguimento de 3–5 anos; tratamentos incluindo minoxidil 2% e corticosteroides tópicos em diversas potências |

---

## Informações de Comercialização no Brasil

Hidrocortisona **não possui registros ativos encontrados** na consulta à base regulatória brasileira (0 registros, status: não comercializado).

> **Nota:** A ausência de registros pode refletir limitação da consulta realizada. A hidrocortisona é um fármaco de uso consolidado mundialmente em múltiplas formulações (creme, loção, solução injetável, comprimido). Recomenda-se verificação direta no portal da ANVISA (www.anvisa.gov.br) para confirmar a situação regulatória atualizada antes de qualquer decisão de desenvolvimento ou comercialização.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Existe um ensaio clínico randomizado de Fase 3 concluído (NCT01453686, n=41, publicado no JAMA Dermatology como PMID 24226568) comparando diretamente hidrocortisona 1% com clobetasol em crianças com alopecia areata, complementado por séries históricas de casos com uso intralesional desde os anos 1950 e revisões sistemáticas recentes, configurando base de evidências suficiente para avançar com cautela — particularmente para a subpopulação pediátrica e casos leves onde a segurança do corticoide de baixa potência é a principal vantagem diferencial.

**Para prosseguir, é necessário:**
- Verificar registros da ANVISA para formulações de hidrocortisona tópica (creme 1%) diretamente no portal oficial
- Obter dados de MOA e categorias DrugBank via API para completar a análise de mecanismo
- Levantar advertências, contraindicações e interações medicamentosas da bula brasileira ou referência equivalente
- Definir formulação-alvo (tópico 1% vs. intralesional) e população-alvo (pediátrica vs. adulto; leve vs. moderada/grave)
- Avaliar o posicionamento competitivo frente a corticosteroides de maior potência (clobetasol, triancinolona) e terapias-alvo emergentes (baricitinibe, ritlecitinibe) já aprovadas para alopecia areata moderada/grave
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

