---
layout: default
title: Phenylalanine
parent: 僅模型預測 (L5)
nav_order: 394
evidence_level: L5
indication_count: 2
---

# Phenylalanine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

Usando o skill `txgnn-pipeline` para contexto do projeto, e agora gerando o relatório conforme o Evidence Pack fornecido.

---

# Fenilalanina: De aminoácido essencial à colangite esclerosante

## Resumo em Uma Frase

Fenilalanina (Phenylalanine, DB00120) é um aminoácido essencial sem indicação terapêutica aprovada registrada no Brasil.
O modelo TxGNN prevê que pode ser eficaz para **Colangite Esclerosante (Sclerosing Cholangitis)**, com pontuação de 99,43% — porém atualmente com **0 ensaios clínicos** e apenas **4 publicações de relevância indireta**, sendo que ao menos uma delas apresenta achados mecanisticamente desfavoráveis ao reposicionamento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Sem indicação terapêutica aprovada registrada |
| Nova Indicação Prevista | Colangite Esclerosante (Sclerosing Cholangitis) |
| Pontuação de Previsão TxGNN | 99,43% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros ANVISA | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente não há dados detalhados sobre o mecanismo de ação terapêutico de fenilalanina. Como aminoácido essencial, ela é precursor direto da tirosina — que por sua vez origina catecolaminas (dopamina, noradrenalina, adrenalina) e hormônio tireoidiano. Em condições hepatobiliares crônicas como a colangite esclerosante primária (CEP) e a cirrose biliar primária (CBP), estudos observacionais documentaram desequilíbrios nos padrões de aminoácidos plasmáticos — incluindo a razão tirosina/fenilalanina — correlacionados com fadiga, sugerindo que o metabolismo de fenilalanina está alterado nessas doenças.

Contudo, existe um sinal de alerta crítico que deve ser considerado antes de qualquer avanço: peptídeos bacterianos quimiotáticos contendo resíduos de fenilalanina — especificamente fMLP (N-formil-Met-Leu-Phe) e fMLT (N-formil-Met-Leu-Tir) — foram identificados como **agentes indutores** de colangite em modelos animais e demonstraram circulação entero-hepática em humanos, com absorção aumentada em contextos de colite. Isso significa que a relação mecanística identificada na literatura aponta fenilalanina (em forma peptídica) como **causadora** da lesão biliar, não como potencial terapêutico.

A alta pontuação do TxGNN (99,43%) provavelmente reflete a forte presença de fenilalanina nos processos biológicos associados à colangite esclerosante, sem discriminar entre associação patológica e efeito terapêutico. A ausência total de ensaios clínicos e a natureza exclusivamente indireta da literatura confirmam que esta previsão, no momento, não sustenta progressão clínica.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Observacional transversal | BMC Gastroenterology | Pacientes com CEP/CBP apresentam desequilíbrios nos padrões de aminoácidos plasmáticos (incluindo tirosina, derivada de fenilalanina) correlacionados com fadiga — relação de associação, não de causalidade terapêutica |
| [32025163](https://pubmed.ncbi.nlm.nih.gov/32025163/) | 2020 | Metabolômica / Biomarcador | J Clin Exp Hepatology | Perfis metabolômicos séricos em colangiocarcinoma e doenças hepatobiliares benignas; estudo de identificação de biomarcadores diagnósticos, sem implicação terapêutica direta |
| [8000512](https://pubmed.ncbi.nlm.nih.gov/8000512/) | 1994 | Estudo animal (modelo em ratos) | J Gastroenterology | Administração retal de fMLT (peptídeo bacteriano contendo resíduo de fenilalanina) **induziu colangite de pequenos ductos** em ratos — sinal mecanístico negativo para reposicionamento |
| [2103382](https://pubmed.ncbi.nlm.nih.gov/2103382/) | 1990 | Ciência básica / Animal | J Gastroenterol Hepatol | Demonstração de circulação entero-hepática de peptídeos fMet (contendo fenilalanina) em humanos; absorção biliar aumentada em contexto de colite — informativo para patogênese, sem utilidade terapêutica direta |

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
As evidências disponíveis não sustentam o reposicionamento de fenilalanina para colangite esclerosante. Além da ausência completa de ensaios clínicos (nível L5), a literatura identificada inclui um sinal mecanístico desfavorável: peptídeos bacterianos contendo fenilalanina são agentes **causadores** de lesão biliar em modelos experimentais — o oposto do efeito terapêutico esperado. A pontuação elevada do TxGNN reflete associação biológica, não potencial terapêutico.

**Para prosseguir, é necessário:**
- Levantamento de evidências sobre o papel da **fenilalanina livre** (não peptídica) em modelos de colangite — distinção fundamental do sinal negativo identificado
- Estudos pré-clínicos diretos que demonstrem efeito protetor ou terapêutico em modelos de CEP
- Esclarecimento do paradoxo mecanístico (aminoácido livre vs. peptídeo bacteriano quimiotático)
- Revisão da arquitetura do modelo TxGNN para avaliar se está distinguindo adequadamente associações patológicas de relações terapêuticas
- Obtenção de dados completos de segurança (MOA, advertências, contraindicações via DrugBank/ANVISA) antes de qualquer consideração clínica adicional
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

