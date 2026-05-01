---
layout: default
title: Imiglucerase
parent: 僅模型預測 (L5)
nav_order: 279
evidence_level: L5
indication_count: 10
---

# Imiglucerase
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

Usando o skill `txgnn-pipeline` como referência de contexto do projeto, vou agora gerar o relatório com base no Evidence Pack fornecido.

---

# Imiglucerase: Da doença de Gaucher à síndrome de Hurler

## Resumo em Uma Frase

Imiglucerase (Cerezyme®) é uma formulação recombinante da glucocerebrosidase humana, aprovada como terapia de reposição enzimática (ERT) para o tratamento da doença de Gaucher.
O modelo TxGNN prevê que pode ser eficaz para a **Síndrome de Hurler (Hurler syndrome)**, atualmente com **0 ensaios clínicos** e **2 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Doença de Gaucher |
| Nova Indicação Prevista | Síndrome de Hurler (Hurler syndrome) |
| Pontuação de Previsão TxGNN | 99.52% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 3 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis no Evidence Pack. Com base na literatura coletada, imiglucerase é uma glucocerebrosidase ácida recombinante (análogo da beta-glicosidase lisossômica humana), produzida em células de ovário de hamster chinês (CHO) e administrada por infusão intravenosa. Sua eficácia na doença de Gaucher está comprovada: ao substituir a enzima GBA deficiente, reduz o acúmulo de glucosilceramida nos macrófagos do baço, fígado e medula óssea, revertendo as manifestações hematológicas, viscerais e esqueléticas da doença.

A síndrome de Hurler (Mucopolissacaridose tipo I, MPS I) é causada por deficiência de α-L-iduronidase (IDUA) — uma enzima lisossômica completamente diferente da glucocerebrosidase. Enquanto na Gaucher acumula-se glucosilceramida, na Hurler acumulam-se heparan sulfato e dermatan sulfato. Os dois substratos e as duas enzimas deficientes não se sobrepõem funcionalmente; portanto, imiglucerase não possui capacidade de substituir a IDUA nem de corrigir o depósito característico da MPS I. A terapia de ERT aprovada para a síndrome de Hurler é a laronidase (Aldurazyme®).

O alto escore do TxGNN (99,52%) reflete a proximidade topológica entre doença de Gaucher e síndrome de Hurler no grafo de conhecimento biológico: ambas são doenças de depósito lisossômico (LSD) com manifestações sistêmicas sobrepostas (hepatoesplenomegalia, comprometimento ósseo, envolvimento multissistêmico). Entretanto, essa similaridade fenotípica e de classe não se traduz em aplicabilidade terapêutica — o modelo captura afinidade de categoria de doença, não equivalência enzimática. Esta previsão representa um falso-positivo mecanístico característico de modelos baseados em grafos de doenças raras.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para imiglucerase na síndrome de Hurler.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [20534487](https://pubmed.ncbi.nlm.nih.gov/20534487/) | 2010 | Imaging Study | Proc Natl Acad Sci USA | Demonstração de PET imaging para rastrear ERT in vivo em múltiplas LSD (Gaucher, Fabry, Hurler, Hunter, Pompe); não avalia eficácia específica do imiglucerase na Hurler |
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | Rev Med Interne | Revisão geral das ERTs disponíveis para LSD; imiglucerase (Cerezyme®) citado como paradigma para Gaucher; menciona Hurler apenas no contexto panorâmico da classe terapêutica |

---

## Informações de Comercialização no Brasil

O imiglucerase possui **3 registros** na ANVISA com situação **comercializado**. Os detalhes específicos de cada registro (número, nome comercial, forma farmacêutica e texto de indicação aprovada) não estão disponíveis no Evidence Pack atual — é necessário consultar diretamente o portal ANVISA para obter essas informações.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Imiglucerase não possui mecanismo de ação aplicável à síndrome de Hurler: a doença requer reposição de α-L-iduronidase (laronidase), não de glucocerebrosidase. A previsão do TxGNN reflete similaridade de classe entre LSD no grafo de conhecimento, mas não há base enzimática, ensaios clínicos direcionados, nem dados pré-clínicos que suportem esta indicação. As 2 publicações disponíveis são revisões gerais de ERT em LSD, sem dados de eficácia do imiglucerase especificamente em MPS I.

**Para prosseguir, é necessário:**
- Identificação de hipótese mecanística alternativa que justifique investigação (ex.: efeito indireto via modulação lisossômica ou vias compartilhadas)
- Dados pré-clínicos em modelos animais de MPS I tratados com imiglucerase
- Recuperação dos dados completos de MOA do DrugBank (gap DG002)
- Recuperação das advertências e contraindicações da bula ANVISA (gap DG001)
- Confirmação dos detalhes dos 3 registros ANVISA (número, nome comercial, indicação aprovada)

> ⚠️ **Aviso**: Este relatório é gerado para fins de pesquisa em reposicionamento de fármacos e **não constitui recomendação clínica ou terapêutica**. Qualquer aplicação clínica requer validação por profissionais de saúde habilitados e aprovação regulatória adequada.
---

