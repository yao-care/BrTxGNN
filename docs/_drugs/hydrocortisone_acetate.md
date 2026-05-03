---
layout: default
title: Hydrocortisone Acetate
parent: 僅模型預測 (L5)
nav_order: 275
evidence_level: L5
indication_count: 10
---

# Hydrocortisone Acetate
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

A skill foi verificada. Agora vou gerar o relatório com base no Evidence Pack fornecido.

---

# Hydrocortisone Acetate: De inflamação cutânea para Alopecia Areata

## Resumo em Uma Frase

Hydrocortisone Acetate é um corticosteroide tópico de baixa potência, classicamente utilizado no tratamento de condições inflamatórias da pele como dermatite de contato e eczema.
O modelo TxGNN prevê que pode ser eficaz para **Alopecia Areata (alopecia areata)**, com **1 ensaio clínico** e **2 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Inflamação cutânea / dermatites (sem registro formal no Brasil) |
| Nova Indicação Prevista | Alopecia Areata (alopecia areata) |
| Pontuação de Previsão TxGNN | 99.94% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Hydrocortisone Acetate é a forma éster acetato do cortisol (hidrocortisona natural), um glicocorticoide endógeno. Embora os dados detalhados de mecanismo de ação não estejam disponíveis no pacote de evidências, sabe-se que o fármaco age ligando-se ao receptor de glucocorticoide (GR), suprimindo a via NF-κB e reduzindo a produção de citocinas pró-inflamatórias como IL-1, IL-2 e TNF-α. Essa ação imunossupressora está bem estabelecida na literatura dermatológica.

A alopecia areata é uma doença autoimune em que linfócitos CD8⁺ perdem a tolerância ao folículo piloso, destruindo o seu "privilégio imune" e causando queda de cabelo em placas. Ao suprimir a ativação das células T e reduzir a inflamação perifolicular, os glicocorticoides agem diretamente sobre esse mecanismo patológico — tornando a previsão do TxGNN biologicamente plausível.

A principal ressalva é que o hydrocortisone acetate pertence à classe de **corticosteroides de baixa potência** (Classe VI–VII na escala americana), o que pode limitar sua eficácia terapêutica comparado a agentes de maior potência como o clobetasol propionato. O único ensaio clínico de Fase 3 identificado posiciona o hydrocortisone 1% como grupo de comparação contra o clobetasol 0,05% em crianças, o que sugere que ele pode funcionar melhor como referência de segurança do que como tratamento de primeira linha.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | Concluído | 41 | Ensaio randomizado comparando clobetasol propionato 0,05% creme vs. hydrocortisone 1% creme em crianças com alopecia areata. Avalia qual potência de corticoide tópico é segura e eficaz para uso pediátrico. Hydrocortisone atua como controle de menor potência. |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [4755919](https://pubmed.ncbi.nlm.nih.gov/4755919/) | 1973 | Case Series / Observacional | Przeglad dermatologiczny | Relata tratamento de formas graves de alopecia areata com injeções subcutâneas intralesionais de suspensão de hydrocortisone acetate, demonstrando aplicação direta do fármaco na indicação prevista. |
| [153470](https://pubmed.ncbi.nlm.nih.gov/153470/) | 1979 | Revisão Narrativa | MMW Münchener Med. Wochenschrift | Revisão de terapias tópicas para doenças dermatológicas; aborda hydrocortisone acetate como referência anti-inflamatória e compara ao novo corticoide fluocortina butil éster, com destaque para perfil de efeitos sistêmicos. |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Existe um ensaio clínico de Fase 3 concluído que avaliou diretamente o hydrocortisone 1% em alopecia areata pediátrica, e a ligação mecanística entre o glicocorticoide e a fisiopatologia autoimune da doença é biologicamente sólida. No entanto, a baixa potência do fármaco, a ausência total de registro na ANVISA e a falta de dados de segurança disponíveis impõem cautela antes de qualquer avanço clínico no Brasil.

**Para prosseguir, é necessário:**
- Obter os resultados completos do ensaio NCT01453686 para confirmar se o hydrocortisone demonstrou eficácia independente ou funcionou apenas como controle inferior ao clobetasol
- Levantar dados de segurança (advertências, contraindicações) via bula em outros mercados (ex.: EMA, FDA) ou DrugBank, dado que os dados locais estão indisponíveis
- Avaliar a viabilidade de registro na ANVISA antes de qualquer protocolo de estudo clínico no Brasil
- Definir a via de administração mais adequada para alopecia areata: tópica (creme 1%), intralesional (suspensão injetável) ou combinada
- Considerar se o desenvolvimento clínico faz mais sentido posicionando o fármaco como **opção de menor risco em crianças** ou populações com contraindicação a corticosteroides de alta potência
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

