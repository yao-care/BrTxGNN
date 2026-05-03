---
layout: default
title: Vancomycin
parent: 僅模型預測 (L5)
nav_order: 501
evidence_level: L5
indication_count: 10
---

# Vancomycin
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

O skill é sobre pipeline operacional (treino, validação, deploy). A geração de relatório segue o formato já definido no prompt do sistema. Prossigo diretamente.

---

# Vancomycin: Das infecções bacterianas à esclerodermia difusa

## Resumo em Uma Frase

Vancomycin é um antibiótico glicopeptídeo consolidado no tratamento de infecções graves causadas por bactérias gram-positivas, incluindo infecções por MRSA e Enterococcus resistente.
O modelo TxGNN prevê que pode ser eficaz para **Esclerodermia Difusa (Diffuse Scleroderma)**,
atualmente com **0 ensaios clínicos** e **1 publicação** apoiando esta direção — sendo essa publicação sem relação direta com a indicação prevista.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Infecções graves por bactérias gram-positivas (não registrado no Brasil) |
| Nova Indicação Prevista | Esclerodermia Difusa (Diffuse Scleroderma) |
| Pontuação de Previsão TxGNN | 99,92% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação registrados neste dossiê. Com base em conhecimento consolidado na literatura científica, Vancomycin é um antibiótico glicopeptídeo que inibe a síntese da parede celular bacteriana pela ligação ao dipeptídeo D-ala–D-ala dos precursores do peptidoglicano — mecanismo exclusivamente ativo contra bactérias gram-positivas. Seu uso clínico está bem estabelecido para infecções por MRSA, enterococos resistentes à vancomicina (VRE em contextos profiláticos) e infecções por Clostridioides difficile (via oral).

A hipótese que fundamenta a previsão do TxGNN é o **eixo microbioma–imunidade**: há evidências preliminares de pesquisa básica indicando que a disbiose intestinal (*gut dysbiosis*) pode contribuir para a patogênese da esclerose sistêmica difusa, via ativação imune sistêmica. Como Vancomycin altera profundamente a composição da microbiota intestinal gram-positiva (especialmente por via oral), teoricamente poderia modular indiretamente a resposta imune envolvida na fibrose e vasculopatia da esclerodermia.

No entanto, esta conexão é **altamente indireta e especulativa**. A única publicação recuperada (relato de caso de eritrodermia com sepse) não apresenta qualquer relação com o diagnóstico ou tratamento de esclerodermia difusa. A previsão do modelo provavelmente origina-se de associações indiretas no grafo de conhecimento (p. ex., nós compartilhados entre antibióticos e doenças autoimunes), sem suporte clínico direto.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Case Report | The American Journal of Case Reports | Relato de paciente de 56 anos com eritrodermia esfoliativa difusa, sepse e eosinofilia, previamente tratado com antibióticos (Augmentin, Clindamicina, Bactrim). Sem relação com esclerodermia difusa ou uso de Vancomycin para fins imunorregulatórios. |

---

## Informações de Comercialização no Brasil

Vancomycin não possui registros ativos na ANVISA. O fármaco **não está comercializado no Brasil** com base nos dados disponíveis neste dossiê.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão é de nível **L5** — gerada exclusivamente pelo modelo TxGNN, sem qualquer suporte em ensaios clínicos reais. A única publicação recuperada é um relato de caso clinicamente não relacionado à esclerodermia, e o mecanismo de ação proposto (modulação da microbiota intestinal como via imunomoduladora) é especulativo e altamente indireto. Associado à ausência de registro da Vancomycin no Brasil, não há base para avançar nesta indicação no momento.

**Para prosseguir, é necessário:**
- Identificar estudos pré-clínicos (modelos animais de esclerodermia) que demonstrem alteração favorável de marcadores de fibrose ou imunidade após modulação da microbiota por Vancomycin
- Confirmar o mecanismo de ação completo via DrugBank API (remediation pendente: DG002)
- Recuperar dados de segurança (advertências e contraindicações) da bula via ANVISA (remediation pendente: DG001), como pré-requisito para qualquer avaliação S1
- Verificar literatura de estudos com antibióticos como proxy de modulação do eixo gut–imunidade em doenças do tecido conjuntivo
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

