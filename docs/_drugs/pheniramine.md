---
layout: default
title: Pheniramine
parent: Evidência Moderada (L3-L4)
nav_order: 519
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-13
description: "Pheniramine: nova indicação prevista, Urticária Alérgica (Allergic Urticaria) (nível de evidência L4). Indicação original: Descongestionantes oftálmicos"
monitor_inn: "pheniramine"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis"]
---

# Pheniramine
{: .fs-9 }

Nível de evidência: **L4** | Indicações previstas: **3** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relatório de avaliação farmacêutica

</div>

# Feniramina: De descongestionante oftálmico para urticária alérgica

## Resumo em Uma Frase

Feniramina é um anti-histamínico H1 de primeira geração (alquilamina), registrado no Brasil como descongestionante oftálmico.
O modelo TxGNN prevê que pode ser eficaz para **Urticária Alérgica (Allergic Urticaria)**,
mas atualmente há **0 ensaios clínicos** e **4 publicações** (nenhuma com evidência de eficácia: três relatos de caso e uma revisão sobre outro anti-histamínico) associadas a esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Descongestionantes oftálmicos |
| Nova Indicação Prevista | Urticária Alérgica (Allergic Urticaria) |
| Pontuação de Previsão TxGNN | 99,67% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Apenas registros cancelados |
| Número de Registros | 7 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada. Segundo informações conhecidas, a feniramina é um anti-histamínico H1 de primeira geração da classe das alquilaminas, usado há muito tempo em condições alérgicas. No Brasil, aparece em colírios, geralmente associada à nafazolina (como o maleato de feniramina).

A urticária alérgica é mediada em grande parte pela histamina. Bloquear receptores H1 é, portanto, mecanisticamente plausível, e isso é coerente com a pontuação elevada do TxGNN. A indicação original (alívio da congestão ocular, muitas vezes de causa alérgica) também envolve um componente histaminérgico, o que aproxima as duas indicações.

Há, porém, uma ressalva importante: a literatura recuperada não traz evidência de eficácia. Os registros são relatos de caso de eventos adversos ou hipersensibilidade (inclusive à própria feniramina), um caso de edema facial que simulava reação alérgica e uma revisão sobre outro anti-histamínico (astemizol). Além disso, os produtos registrados são oftálmicos, o que não corresponde à via sistêmica normalmente usada na urticária.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [40324831](https://pubmed.ncbi.nlm.nih.gov/40324831/) | 2025 | Relato de caso | Indian J Pharmacol | Perda de consciência após administração intravenosa concomitante de feniramina e hidrocortisona no manejo de reação a outro fármaco |
| [40125237](https://pubmed.ncbi.nlm.nih.gov/40125237/) | 2025 | Relato de caso | Cureus | Reação de hipersensibilidade imediata à própria feniramina em paciente com síndrome de hipersensibilidade a múltiplos fármacos |
| [16854350](https://pubmed.ncbi.nlm.nih.gov/16854350/) | 2006 | Relato de caso | Allergol Immunopathol | Edema facial grave por ingestão de lagarta processionária do pinheiro, simulando evento alérgico |
| [2859711](https://pubmed.ncbi.nlm.nih.gov/2859711/) | 1985 | Revisão | Z Hautkr | Revisão de 39 estudos com astemizol (anti-histamínico diferente) em rinite, conjuntivite e urticária crônica; feniramina aparece apenas como um dos comparadores |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 104971282 | Cristalin | Não informada | Descongestionantes oftálmicos |
| Registro nº 100681115 | Claril | Não informada | Descongestionantes oftálmicos |
| Registro nº 154230193 | Cloridrato de nafazolina + maleato de feniramina | Não informada | Descongestionantes oftálmicos |
| Registro nº 155840212 | Clanistil | Não informada | Descongestionantes oftálmicos |
| Registro nº 186200022 | Colírio Moura Brasil Aliv | Não informada | Descongestionantes oftálmicos |

Todos os 7 registros encontrados estão cancelados; a tabela lista apenas os 5 principais.

## Considerações de Segurança

- **Contraindicações sugeridas pelo grafo de conhecimento (não provêm da bula):** o grafo de conhecimento do TxGNN (PrimeKG) associa a feniramina a diversas condições como possíveis contraindicações, entre elas:
  - Cardiovasculares e metabólicas: hipertensão, diabetes mellitus, cetoacidose diabética, hiperglicemia, hipotireoidismo/mixedema.
  - Hepáticas, renais e gastrointestinais: insuficiência e doença hepática, doença renal, pancreatite, doença da vesícula biliar, úlcera gástrica/péptica, gastrite, doença inflamatória intestinal.
  - Neuropsiquiátricas: epilepsia, insônia, transtornos psicóticos e esquizoafetivos.
  - Respiratórias e outras: DPOC, bronquite, hiperplasia prostática benigna, trombocitopenia, dermatite herpetiforme.

  Esses itens devem ser confirmados na bula, pois não são texto de rotulagem.
- Os relatos de caso recuperados descrevem hipersensibilidade à feniramina e um evento adverso grave (perda de consciência) com uso intravenoso combinado a hidrocortisona.

Consulte a bula para as advertências e interações medicamentosas oficiais; não foram encontradas interações no levantamento realizado.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A pontuação do TxGNN é alta e o mecanismo anti-histamínico é plausível, mas não há ensaios clínicos nem literatura de eficácia (nível L4), e todos os registros brasileiros estão cancelados, o que reduz o valor prático do desenvolvimento.
- As demais previsões (doença da cavidade nasal e laringofaringite aguda) estão em L5, sem qualquer estudo, e também em Hold.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), etapa bloqueante para a triagem de segurança.
- Complementar os dados de mecanismo de ação via DrugBank.
- Realizar busca dirigida por estudos de eficácia da feniramina em urticária (ensaios clínicos e revisões sistemáticas).
- Avaliar a compatibilidade de via de administração, já que os produtos registrados são oftálmicos e a urticária costuma exigir uso sistêmico.
- Verificar se há interesse regulatório e comercial, dado que não há registro válido no Brasil.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

