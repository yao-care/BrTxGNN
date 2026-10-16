---
layout: default
title: Pemigatinib
parent: Apenas Predição do Modelo (L5)
nav_order: 515
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Pemigatinib: nova indicação prevista, Neoplasia Endócrina Múltipla (Multiple Endocrine Neoplasia) (nível de evidência L5). Indicação original: Outros antineoplásicos"
---

# Pemigatinib
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

# Pemigatinibe: De outros antineoplásicos para neoplasia endócrina múltipla

## Resumo em Uma Frase

Pemigatinibe é um inibidor de quinase antineoplásico, registrado no Brasil na categoria "outros antineoplásicos".
O modelo TxGNN prevê que pode ser eficaz para **Neoplasia Endócrina Múltipla (Multiple Endocrine Neoplasia)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção específica; trata-se apenas de uma previsão do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outros antineoplásicos |
| Nova Indicação Prevista | Neoplasia Endócrina Múltipla (Multiple Endocrine Neoplasia) |
| Pontuação de Previsão TxGNN | 99,71% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Apenas registros cancelados |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada. Segundo informações conhecidas, o pemigatinibe é um inibidor seletivo dos receptores do fator de crescimento de fibroblastos (FGFR1-3), utilizado como antineoplásico.

A sinalização FGF/FGFR já foi associada a alguns tumores endócrinos. No entanto, não há ligação direta estabelecida com os principais genes causadores da neoplasia endócrina múltipla (MEN1, RET, CDKN1B). A relação com a indicação original é, portanto, apenas de natureza geral (ambas são doenças tumorais), e a previsão permanece sem comprovação.

**Outras previsões do modelo (todas L5, sem ensaios clínicos):**

- **Câncer de mama HER2 positivo (99,49%)**: biologicamente plausível, pois a sinalização de FGFR é uma via descrita de resistência a terapias anti-HER2 e endócrinas, o que poderia justificar pesquisas em combinação. Há uma publicação, mas é uma revisão geral de inibidores de quinase aprovados, sem evidência específica para a indicação.
- **Esclerose lateral amiotrófica e variantes (99,41% a 99,25%)**: a direção do efeito é incerta, pois a sinalização de FGF costuma ser neurotrófica e sua inibição poderia ser desfavorável. A exposição no sistema nervoso central não está estabelecida. As variantes são redundantes entre si.
- **Displasia espondilometafisária axial (99,25%)**: vínculo mecanístico fraco, pois a doença está associada a variantes do gene CFAP410, e não do FGFR; além disso, há preocupações de segurança em esqueleto em crescimento.
- **Amenorreia, infecção por citomegalovírus, rinotraqueíte infecciosa bovina e catarro maligno**: provavelmente artefatos do grafo do modelo ou sinais de eventos adversos, sem racional terapêutico plausível.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Para a indicação principal (neoplasia endócrina múltipla), atualmente não há literatura relacionada. A única publicação identificada, para a indicação alternativa de câncer de mama HER2 positivo, é:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/) | 2021 | Revisão | Pharmacological Research | Atualização de 2021 sobre propriedades dos inibidores de proteína quinase de moléculas pequenas aprovados pela FDA; revisão geral, sem evidência clínica específica para a indicação |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 125760040 (cancelado) | PEMAZYRE | Não informada | Outros antineoplásicos |

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia alvo (inibidor de quinase FGFR1-3) |
| Risco de Mielossupressão | Consulte as advertências e precauções na bula |
| Classificação de Emetogenicidade | Consulte as advertências e precauções na bula |
| Itens de Monitoramento | Consulte a bula; sabe-se que a inibição de FGFR pode causar hiperfosfatemia, portanto o monitoramento de fosfato sérico é pertinente |
| Proteção no Manuseio | Consulte as advertências e precauções na bula |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 50 interações no total; entre as listadas, destacam-se as de gravidade **maior** com:
  - Aprepitanto
  - Dexametasona
  - Claritromicina
  - Cobicistate
  - Lumacaftor
  - Cloranfenicol
  - Eritromicina
  - Cetoconazol
  - Fluconazol

  Também há interações de gravidade **moderada** com cimetidina, metreleptina, clotrimazol, fenilbutirato de glicerol, troglitazona, deferasirox, ivacaftor, zafirlucaste, griseofulvina, elagolix e osilodrostat. Em geral, o padrão sugere interação com inibidores/indutores do metabolismo (especialmente CYP3A4), o que exige revisão cuidadosa da medicação concomitante.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão para neoplasia endócrina múltipla baseia-se apenas no modelo (nível L5), sem ensaios clínicos nem literatura de apoio e sem vínculo mecanístico direto estabelecido. Além disso, o único registro no Brasil está cancelado.

**Para prosseguir, é necessário:**
- Obter dados do mecanismo de ação (MOA) em fonte confiável, como o DrugBank
- Baixar e analisar a bula na ANVISA para obter advertências e contraindicações (lacuna que bloqueia a triagem de segurança)
- Realizar busca sistemática de literatura e ensaios clínicos sobre inibição de FGFR em neoplasia endócrina múltipla
- Avaliar estudos pré-clínicos que relacionem a via FGFR aos genes MEN1, RET e CDKN1B
- Verificar a situação regulatória atual do produto no Brasil, dado o cancelamento do registro
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

