---
layout: default
title: Brinzolamide
parent: Apenas Predição do Modelo (L5)
nav_order: 153
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Brinzolamide: nova indicação prevista, Glaucoma hereditário primário (primary hereditary glaucoma) (nível de evidência L5). Indicação original: Antiglaucomatoso"
---

# Brinzolamide
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

# Brinzolamida: De antiglaucomatoso a glaucoma hereditário primário

## Resumo em Uma Frase

Brinzolamida é um inibidor da anidrase carbônica de uso tópico ocular, originalmente registrado como antiglaucomatoso.
O modelo TxGNN prevê que pode ser eficaz para **glaucoma hereditário primário (primary hereditary glaucoma)**, mas, para essa indicação específica, **não há nenhum ensaio clínico nem publicação** que apoie a previsão.
Já as indicações vizinhas (glaucoma de ângulo aberto e glaucoma em geral) contam com dezenas de ensaios clínicos e publicações, mas correspondem ao uso já aprovado do fármaco, e não a um reposicionamento propriamente dito.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antiglaucomatoso |
| Nova Indicação Prevista | Glaucoma hereditário primário (primary hereditary glaucoma) |
| Pontuação de Previsão TxGNN | 99,48% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Somente registros cancelados |
| Número de Registros | 3 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada para este relatório. Segundo informações conhecidas, a brinzolamida inibe a anidrase carbônica II no epitélio ciliar, reduzindo a secreção de humor aquoso e, consequentemente, a pressão intraocular (PIO).

Como a elevação da PIO é o principal fator de risco modificável em diversos tipos de glaucoma, é plausível que o mesmo mecanismo seja útil no glaucoma hereditário primário. Essa é, porém, uma inferência mecanística: a pontuação do TxGNN não foi acompanhada de qualquer estudo específico.

Vale destacar que as demais indicações previstas pelo modelo com evidência robusta (glaucoma de ângulo aberto, glaucoma em geral) são usos já aprovados e, portanto, não representam reposicionamento. Outras previsões de alta pontuação, como fístula labial comissural, leucoedema oral, síndrome da ardência bucal e osteorradionecrose da mandíbula, não têm vínculo mecanístico identificado e provavelmente são artefatos do grafo de conhecimento.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para glaucoma hereditário primário.

Como contexto, para as indicações vizinhas (uso já aprovado), os dados compilados incluem, por exemplo:

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT05022004](https://clinicaltrials.gov/study/NCT05022004) | Phase 3 | Concluído | 599 | Equivalência terapêutica de brinzolamida 1% genérica vs. Azopt em glaucoma primário de ângulo aberto ou hipertensão ocular |
| [NCT04944290](https://clinicaltrials.gov/study/NCT04944290) | Phase 3 | Concluído | 447 | Brinzolamida/brimonidina vs. Simbrinza, duplo-cego, controlado por comparador ativo |
| [NCT01297920](https://clinicaltrials.gov/study/NCT01297920) | Phase 3 | Concluído | 1.062 | Combinação fixa brinzolamida/brimonidina vs. componentes isolados na redução da PIO |
| [NCT01309204](https://clinicaltrials.gov/study/NCT01309204) | Phase 3 | Concluído | 1.184 | Combinação fixa brinzolamida/brimonidina vs. uso concomitante dos dois colírios |
| [NCT02512042](https://clinicaltrials.gov/study/NCT02512042) | Phase 3 | Concluído | 973 | Bioequivalência clínica de brinzolamida 1% genérica vs. Azopt |
| [NCT00061516](https://clinicaltrials.gov/study/NCT00061516) | Phase 3 | Concluído | 78 | Segurança e eficácia de Azopt 1,0% vs. Betaxon em pacientes pediátricos com glaucoma ou hipertensão ocular |

Esses estudos referem-se a glaucoma de ângulo aberto/hipertensão ocular e a glaucoma em geral, não ao glaucoma hereditário primário.

## Evidências da Literatura

Atualmente não há literatura relacionada específica para glaucoma hereditário primário.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 100681114 | AZOPT | Não informada | Antiglaucomatosos |
| Registro nº 100681131 | SIMBRINZA | Não informada | Antiglaucomatosos |
| Registro nº 100681108 | AZORGA | Não informada | Antiglaucomatosos |

Os três registros constam como **cancelados**; não há registro vigente no Brasil.

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 32 interações potenciais, todas com nível de gravidade não classificado. Entre as principais citadas estão inibidores de bomba de prótons (pantoprazol, omeprazol, lansoprazol), corticosteroides (prednisona, prednisolona, dexametasona, triancinolona), estatinas (sinvastatina, rosuvastatina), varfarina, clopidogrel e cloreto de potássio.
- **Sinal de segurança na literatura**: relato de caso de efusão do corpo ciliar induzida por brinzolamida tópica, com fechamento secundário do ângulo e mudança miópica, que se resolveu após a suspensão do fármaco. Isso é relevante para pacientes com predisposição anatômica.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para glaucoma hereditário primário baseia-se apenas no modelo TxGNN (nível L5), sem ensaios clínicos nem literatura específica; o mecanismo de redução da PIO é plausível, mas não comprovado nesta forma de glaucoma.
- Os registros no Brasil estão todos cancelados, o que limita qualquer avanço prático imediato.

**Para prosseguir, é necessário:**
- Confirmar a situação regulatória atual no Brasil (registros cancelados) e a existência de outras apresentações ou fabricantes vigentes.
- Obter a bula da ANVISA para completar advertências e contraindicações.
- Complementar os dados do mecanismo de ação (MOA) no DrugBank.
- Realizar busca dirigida de literatura e de ensaios em glaucoma hereditário/congênito, incluindo avaliação de segurança pediátrica, já que o tratamento clínico costuma ser apenas uma ponte para a cirurgia.
- Se houver interesse nas indicações já bem sustentadas (glaucoma de ângulo aberto, nível L1), tratá-las como uso aprovado, com "Proceed with Guardrails" condicionado à verificação do status de comercialização. O glaucoma de ângulo fechado (nível L2) deve ser tratado como questão de pesquisa, dado o risco de fechamento angular induzido por sulfonamidas.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

