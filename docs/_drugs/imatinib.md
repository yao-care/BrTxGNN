---
layout: default
title: Imatinib
parent: Apenas Predição do Modelo (L5)
nav_order: 362
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Imatinib: nova indicação prevista, Fibrossarcoma cardíaco (heart fibrosarcoma) (nível de evidência L5). Indicação original: Mastocitose sistêmica, GIST…"
---

# Imatinib
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

# Imatinibe: Da leucemia mieloide crônica ao fibrossarcoma cardíaco

## Resumo em Uma Frase

Imatinibe é um inibidor de tirosina quinase, originalmente usado no tratamento de doenças como leucemia mieloide crônica BCR-ABL1 positiva, tumor estromal gastrointestinal (GIST) e mastocitose sistêmica.
O modelo TxGNN prevê que pode ser eficaz para **fibrossarcoma cardíaco (heart fibrosarcoma)**,
mas atualmente há **0 ensaios clínicos** e apenas **1 publicação** (uma revisão geral sobre novas indicações do imatinibe) ligada a esta previsão, ou seja, a evidência direta é muito fraca.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Mastocitose sistêmica, GIST, leucemia mieloide crônica BCR-ABL1 positiva, dermatofibrossarcoma protuberante, síndrome hipereosinofílica, entre outras (conforme o grafo de conhecimento; não há registro de bula no Brasil) |
| Nova Indicação Prevista | Fibrossarcoma cardíaco (heart fibrosarcoma) |
| Pontuação de Previsão TxGNN | 99,94% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado (nos dados compilados) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o imatinibe inibe as quinases PDGFR, KIT e ABL, e sua eficácia em leucemia mieloide crônica, GIST e dermatofibrossarcoma protuberante (DFSP) está estabelecida.

Alguns tumores do tipo fibrossarcoma podem ser dependentes de PDGFB, como ocorre no DFSP, que apresenta a fusão COL1A1-PDGFB. Isso oferece uma ligação mecanística plausível com a inibição de PDGFR pelo imatinibe.

Contudo, não há dados específicos sobre tumores cardíacos. A única publicação associada é um comentário geral sobre novas indicações do imatinibe, publicado em 2008, que conclui que as novas indicações não têm evidência robusta. A previsão, portanto, baseia-se essencialmente na pontuação do modelo.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Revisão | Prescrire International | Comentário sobre as novas indicações do imatinibe (por exemplo, leucemia linfoblástica aguda Ph+, com taxa de resposta hematológica maior que a quimioterapia em um ensaio com 55 pacientes), concluindo que as evidências não são robustas. Não trata de tumores cardíacos |

## Considerações de Segurança

- **Contraindicações no grafo de conhecimento** (não são texto de bula): o grafo associa o imatinibe a condições como insuficiência hepática, doença renal, insuficiência cardíaca congestiva, doença arterial coronariana, derrame pericárdico, trombocitopenia, neutropenia, agranulocitose, anemia, hipofosfatemia e edema pulmonar, entre outras. Esses itens exigem confirmação na bula oficial.
- **Interações Medicamentosas**: foram identificadas 100 interações, e os principais exemplos disponíveis são:
  - **Maior gravidade**: eliglustate e naloxegol.
  - **Gravidade moderada**: corticosteroides (hidrocortisona, dexametasona, betametasona, budesonida, triancinolona), pioglitazona, glimepirida, saxagliptina, aprepitanto, morfina, cimetidina, claritromicina, lansoprazol, dexlansoprazol, naltrexona, naldemedina e metreleptina.

Dado o alvo cardíaco da indicação prevista, as condições cardiovasculares listadas acima merecem atenção especial.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem pontuação alta no modelo, mas não há ensaios clínicos nem estudos específicos em fibrossarcoma cardíaco (nível L5). O fármaco também não está registrado no Brasil nos dados compilados.

**Para prosseguir, é necessário:**
- Obter e analisar a bula aprovada pela ANVISA (advertências e contraindicações), pois a lacuna de dados de segurança impede a triagem de segurança.
- Complementar os dados de mecanismo de ação do imatinibe (por exemplo, via DrugBank).
- Buscar relatos de caso ou séries sobre sarcomas cardíacos tratados com imatinibe e avaliar a presença de alterações em PDGFR/KIT nesses tumores.
- Avaliar a situação regulatória do imatinibe no Brasil, já que os dados compilados indicam ausência de registros.
- Considerar que o dermatofibrossarcoma protuberante (já indicação original) e os sarcomas de tecidos moles de forma geral têm evidências mais consistentes do que o fibrossarcoma cardíaco, e podem ser alvos prioritários de investigação.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

