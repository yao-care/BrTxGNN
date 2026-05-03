---
layout: default
title: Mometasone
parent: 僅模型預測 (L5)
nav_order: 355
evidence_level: L5
indication_count: 10
---

# Mometasone
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

Usando o skill `txgnn-pipeline` para contextualizar a geração de relatório de reposicionamento. Agora gero o relatório com base no Evidence Pack fornecido.

---

# Mometasone: De Corticosteroide Tópico a Linfoma Cutâneo Primário de Células T

## Resumo em Uma Frase

Mometasone furoato é um corticosteroide tópico sintético de alta potência (Classe III), amplamente utilizado no tratamento de condições inflamatórias cutâneas como dermatite atópica, psoríase e rinite alérgica.
O modelo TxGNN prevê que pode ser eficaz para o **Linfoma Cutâneo Primário de Células T (primary cutaneous T-cell lymphoma)**,
atualmente com **0 ensaios clínicos** e **2 publicações** apoiando esta direção — embora a fundamentação mecanística seja clinicamente robusta, com suporte de diretrizes NCCN.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Condições inflamatórias cutâneas (dermatite, psoríase) e rinite alérgica |
| Nova Indicação Prevista | Linfoma Cutâneo Primário de Células T (primary cutaneous T-cell lymphoma) |
| Pontuação de Previsão TxGNN | 99.36% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✗ Não registrado na ANVISA (dados disponíveis: 0 registros) |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Mometasone furoato atua como agonista do receptor de glicocorticoides (GR), e este mecanismo está diretamente relacionado à sua ação sobre linfócitos T malignos: a ativação do GR induz apoptose em células T por meio da regulação positiva de BIM e negativa de Bcl-2, além de inibir a sinalização de NF-κB e a produção de IL-2 — bloqueando efetivamente a proliferação de clones T neoplásicos na pele.

O linfoma cutâneo primário de células T (CTCL), especialmente em seus subtipos de estágios iniciais como Micose Fungoides (MF) Stage IA-IIA, manifesta-se como manchas e placas eritematosas que clinicamente podem mimetizar dermatite inflamatória — a indicação original do fármaco. Ambas as condições compartilham o mesmo compartimento anatômico (a pele) e envolvem mecanismos imunológicos mediados por células T. Não por acaso, as diretrizes do NCCN recomendam corticosteroides tópicos de alta potência como terapia cutânea-dirigida de primeira linha para MF Stage IA-IIA, com nível de evidência **Categoria 1**.

Mometasone, classificado como corticosteroide Classe III de alta potência, possui exatamente o perfil farmacológico indicado nestas diretrizes. A previsão do TxGNN não representa uma extrapolação mecanística distante, mas sim a extensão natural de um uso tópico já bem estabelecido em inflamação cutânea para um contexto linfoproliferativo de mesmo compartimento. A escassez de ensaios clínicos específicos com Mometasone em CTCL reflete muito mais uma lacuna de pesquisa do que ausência de plausibilidade biológica.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [25442255](https://pubmed.ncbi.nlm.nih.gov/25442255/) | 2015 | Case Report | Journal of Cutaneous Pathology | Relato de Micose Fungoides CD8+CD56+ de fenótipo citotóxico em criança de 11 anos com 7 anos de evolução; manchas e placas eritematosas em tronco e extremidades; destaca a dificuldade diagnóstica em crianças e a apresentação clínica atípica do CTCL |
| [40821495](https://pubmed.ncbi.nlm.nih.gov/40821495/) | 2025 | Case Report | Proceedings (Baylor University Medical Center) | Pseudolinfoma cutâneo refratário em mulher de 62 anos tratado com tapinarof após falha terapêutica com mometasone e tacrolimus; ilustra o uso de corticosteroides tópicos no espectro linfoproliferativo cutâneo e os limites de suas respostas |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Mometasone é um corticosteroide Classe III de alta potência cujo mecanismo de ação — indução de apoptose em linfócitos T via ativação do receptor GR — é diretamente relevante ao CTCL; corticosteroides tópicos de alta potência figuram como recomendação **NCCN Categoria 1** para Micose Fungoides Stage IA-IIA, conferindo base clínica sólida à previsão do TxGNN, mesmo na ausência de ensaios controlados com Mometasone especificamente.

**Para prosseguir, é necessário:**
- Verificar registros ANVISA diretamente no portal (os dados disponíveis indicam 0 registros, o que pode refletir lacuna de coleta — Mometasone é comercializado globalmente sob marcas como Nasonex® e Elocom®)
- Obter dados completos de MOA e categorias DrugBank (DB00764) via API
- Levantar advertências, contraindicações e interações medicamentosas da bula ANVISA e/ou FDA
- Buscar ensaios clínicos específicos de Mometasone em CTCL em bases complementares (EU Clinical Trials Register, ICTRP regional)
- Delimitar a indicação ao subgrupo com maior benefício esperado: **Micose Fungoides Stage IA-IIA** com lesões em placa/mancha, para eventual desenho de estudo de viabilidade prospectivo
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

