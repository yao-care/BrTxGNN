---
layout: default
title: Desloratadine
parent: Apenas Predição do Modelo (L5)
nav_order: 256
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Desloratadine: nova indicação prevista, Urticária ao frio (Cold Urticaria) (nível de evidência L5). Indicação original: Anti-histamínicos para uso sistêmico"
---

# Desloratadine
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

# Desloratadina: De anti-histamínico sistêmico para urticária ao frio

## Resumo em Uma Frase

Desloratadina é um anti-histamínico sistêmico de segunda geração, originalmente registrado no Brasil na classe dos anti-histamínicos para uso sistêmico.
O modelo TxGNN prevê que pode ser eficaz para **Urticária ao Frio (Cold Urticaria)**,
atualmente com **2 ensaios clínicos** e **6 publicações** retornadas na busca (3 RCTs diretamente relacionados à desloratadina na urticária ao frio).

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anti-histamínicos para uso sistêmico |
| Nova Indicação Prevista | Urticária ao frio (Cold Urticaria) |
| Pontuação de Previsão TxGNN | 99,94% |
| Nível de Evidência | L1 (conforme classificação dos dados compilados; ressalva abaixo) |
| Situação no Mercado Brasileiro | ✗ Apenas registros cancelados |
| Número de Registros | 20 (todos cancelados) |
| Decisão Recomendada | Proceed with Guardrails |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação na base compilada. Segundo informações conhecidas, a desloratadina é um agonista inverso seletivo do receptor H1 periférico, e sua eficácia como anti-histamínico sistêmico em doenças alérgicas está estabelecida.

A urticária ao frio é uma urticária física mediada por mastócitos e histamina. Como o bloqueio de H1 atua diretamente na via efetora, o mecanismo é plausível. O aumento de dose de anti-histamínicos de segunda geração (até 4 vezes a dose padrão) é coerente com o manejo recomendado em diretrizes para esta condição.

Os estudos disponíveis testam justamente essa estratégia de escalonamento de dose (5, 10 e 20 mg), o que reforça a coerência entre a previsão do modelo e a prática clínica.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Phase 4 | Concluído | 30 | Estudo multicêntrico, duplo-cego, com escalonamento de dose (5, 10 e 20 mg) em urticária ao frio adquirida; objetivo: identificar a dose que inibe os sintomas |
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Phase 4 | Concluído | 33 | Estudo cruzado, randomizado, duplo-cego e controlado por placebo comparando 5 mg vs. 20 mg na urticária ao frio induzida experimentalmente (termografia, volumetria e fotografia) |

Observação: ambos são de Fase 4 e com amostras pequenas; não se enquadram como Fase 3 clássica.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | RCT | J Allergy Clin Immunol | Desloratadina em dose alta reduziu o volume das pápulas e melhorou os limiares de provocação pelo frio em comparação à dose padrão (cruzado, controlado por placebo) |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | RCT | Br J Dermatol | Estudo randomizado de escalonamento de dose de anti-histamínico H1 medindo o limiar crítico de temperatura na urticária ao frio |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | RCT | J Dermatol Treat | Desloratadina 5 mg por 4 dias, testada com cubos de gelo antes e depois do tratamento em 12 pacientes com urticária ao frio |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Revisão | Drugs | Revisão sobre etiologia, manejo e opções de tratamento da urticária crônica |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Relato de caso | Qatar Med J | Urticária ao frio após anafilaxia por picada de formiga (contexto da doença, sem avaliação da desloratadina) |

## Informações de Comercialização no Brasil

Todos os 20 registros encontrados estão cancelados; não há registro válido atualmente. Principais registros (5 de 20):

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 154230334 | Hystalor | — | Anti-histamínicos sistêmicos |
| Registro nº 167730689 | Deslorana | — | Anti-histamínicos sistêmicos |
| Registro nº 100431302 | Superhist ODT | — | Anti-histamínicos para uso sistêmico |
| Registro nº 125680360 | Ikaros | — | Anti-histamínicos sistêmicos |
| Registro nº 105730465 | Esalerg Gotas | — | Anti-histamínicos sistêmicos |

## Considerações de Segurança

- **Contraindicações descritas no grafo de conhecimento (PrimeKG, não derivadas de bula)**: hipertensão, doença renal, doença hepática, doença da vesícula biliar, diabetes mellitus e cetoacidose diabética, hiperplasia prostática benigna, doença arterial coronariana e aterosclerose, glaucoma de ângulo fechado, e hipertireoidismo (doença de Graves/tireotoxicose). Devem ser confirmadas na bula, pois não provêm do texto regulatório.
- **Interações Medicamentosas**: a consulta identificou 100 interações potenciais (exemplos: calcitriol, fentermina, pantoprazol, doxiciclina, clotrimazol, morfina, metformina, omeprazol, cimetidina, prednisona, sinvastatina, epinefrina), todas com nível de gravidade não classificado. Não permitem conclusão clínica sem revisão adicional.

Consulte a bula para advertências e contraindicações oficiais.

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
- Há dois ensaios de Fase 4 concluídos e três RCTs publicados testando diretamente a desloratadina (incluindo doses elevadas) na urticária ao frio, com mecanismo plausível via bloqueio de H1. Contudo, as amostras são pequenas, os ensaios não são de Fase 3 e o nível L1 deve ser interpretado com cautela.
- Nenhum dos 20 registros brasileiros está válido, o que limita a viabilidade imediata.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois estes dados estão ausentes e bloqueiam a triagem de segurança.
- Confirmar o mecanismo de ação em fonte consultável (ex.: DrugBank).
- Verificar a situação regulatória: um registro válido de desloratadina (ou nova submissão) é necessário para uso no Brasil.
- Definir plano de segurança para doses acima da aprovada (até 4 vezes), incluindo populações com doença renal, hepática ou cardiovascular.
- Revisar as interações medicamentosas sem classificação de gravidade.

### Outras indicações previstas (sem evidência suficiente — Hold)

Indicações de menor prioridade, todas com decisão **Hold**: doença da cavidade nasal (L4, apenas estudos em animais e com outros fármacos), cefaleia (L4, literatura sem relação direta), e laringofaringite aguda, dermatite atópica recalcitrante, responsividade atópica de IgE, conjuntivite da rosácea, cefalalgia autonômica trigeminal, ceratoconjuntivite epitelial punctata e síndrome de Angelucci (todas L5, apenas previsão do modelo).
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

