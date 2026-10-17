---
layout: default
title: Dimenhydrinate
parent: Evidência Moderada (L3-L4)
nav_order: 270
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-13
description: "Dimenhydrinate: nova indicação prevista, Urticária Alérgica (Allergic Urticaria) (nível de evidência L4). Indicação original: Antieméticos e antinauseantes"
monitor_inn: "DIMENHYDRINATE"
predicted_indications: ["allergic urticaria", "cold urticaria"]
---

# Dimenhydrinate
{: .fs-9 }

Nível de evidência: **L4** | Indicações previstas: **2** 
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

# Dimenidrinato: Do uso antiemético à urticária alérgica

## Resumo em Uma Frase

Dimenidrinato é um sal de difenidramina e 8-cloroteofilina, originalmente usado como antiemético e antinauseante.
O modelo TxGNN prevê que pode ser eficaz para **Urticária Alérgica (Allergic Urticaria)**,
mas atualmente há **nenhum ensaio clínico** e apenas **1 publicação** (estudo farmacocinético em cães) relacionada a esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antieméticos e antinauseantes |
| Nova Indicação Prevista | Urticária Alérgica (Allergic Urticaria) |
| Pontuação de Previsão TxGNN | 99,74% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Apenas registros cancelados |
| Número de Registros | 14 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação do medicamento. Segundo informações conhecidas, o dimenidrinato é o sal da difenidramina (anti-histamínico H1 de primeira geração) com a 8-cloroteofilina. Sua eficácia como antiemético e antinauseante está estabelecida, e mecanisticamente pode ser aplicável à urticária alérgica.

Na urticária alérgica, a histamina liberada pelos mastócitos age nos receptores H1 e provoca o aparecimento de urticas (vergões) e eritema. O componente difenidramina bloqueia esses receptores, de modo que o vínculo biológico é plausível e coerente com a pontuação elevada do TxGNN. Esse vínculo, porém, foi inferido da farmacologia conhecida da difenidramina, e não de dados específicos do dimenidrinato.

A indicação original (náusea e vômito, inclusive cinetose) e a nova indicação (urticária) são distintas do ponto de vista clínico, mas ambas dependem do bloqueio de receptores H1. Essa é a ponte mecanística entre elas.

Uma segunda previsão do modelo, **urticária ao frio** (pontuação de 99,24%), tem o mesmo racional mecanístico, mas não conta com ensaios nem literatura (nível L5). As diretrizes atuais preferem anti-histamínicos de segunda geração, que causam menos sedação, de modo que um agente de primeira geração oferece pouca vantagem.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | Estudo farmacocinético (cães) | Veterinary Dermatology | Estudo piloto sobre a farmacocinética da difenidramina após administração oral e intravenosa, e do dimenidrinato por via oral, em cães saudáveis, com avaliação do efeito sobre a formação de urticas induzidas por histamina. O dimenidrinato foi descrito como capaz de proporcionar melhor absorção oral da difenidramina. Oferece apoio indireto quanto à exposição, mas não traz dados de eficácia em urticária. |

## Informações de Comercialização no Brasil

Todos os 14 registros encontrados estão **cancelados**; não há registro válido no momento. Os cinco principais:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 155840550 | Dimenidrinato | — | Antieméticos e antinauseantes |
| Registro nº 104971530 | Dimenidrinato | — | Antieméticos e antinauseantes |
| Registro nº 178170901 | Dramin | — | Antieméticos e antinauseantes |
| Registro nº 155840559 | Dramavit | — | Antieméticos e antinauseantes |
| Registro nº 104971536 | Nausicalm cápsula mole | — | Antieméticos e antinauseantes |

## Considerações de Segurança

- **Contraindicações sugeridas pelo grafo de conhecimento (não extraídas da bula):** doenças hipertensivas e hipotensivas, doença hepática, doença da vesícula biliar, trombocitopenia, distúrbios de coagulação, hiperglicemia, diabetes mellitus e cetoacidose diabética, úlcera péptica, estenose pilórica, hiperplasia prostática benigna, obstrução do colo vesical, gota, abuso/dependência de substâncias, síndrome coronariana aguda, doença arterial coronariana, infarto do miocárdio, trombose coronariana, hemoglobinopatias, hipertensão ocular, glaucoma de ângulo fechado, hipertireoidismo (doença de Graves, tireotoxicose) e hipofosfatemia.
- **Interações medicamentosas:** foram identificadas 67 interações; as principais:
  - **Graves:** cloreto de potássio e citrato de potássio.
  - **Moderadas:** anticolinérgicos (atropina, escopolamina, hioscina/hiosciamina, glicopirrônio, diciclomina, clidínio, trospio, mepenzolato, metescopolamina, propantelina), opioides e antidiarreicos (morfina, ópio, loperamida, eluxadolina), além de metoclopramida, procaloprida e nabilona.

As advertências e contraindicações da bula não estavam disponíveis nos dados compilados; consulte a bula para as informações oficiais de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão é mecanisticamente plausível e tem pontuação alta, mas se apoia em um único estudo farmacocinético veterinário, sem ensaios clínicos em humanos (nível L4). Além disso, o produto não tem registro válido no Brasil e existem alternativas de segunda geração com melhor perfil de tolerabilidade.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois a lacuna atual impede a triagem de segurança.
- Obter dados do mecanismo de ação no DrugBank.
- Buscar estudos clínicos em humanos que avaliem eficácia em urticária, em comparação com anti-histamínicos de segunda geração.
- Avaliar a viabilidade regulatória, já que todos os registros estão cancelados.
- Revisar a carga anticolinérgica e sedativa em populações vulneráveis (idosos, pacientes com glaucoma, hiperplasia prostática ou doença cardiovascular).
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

