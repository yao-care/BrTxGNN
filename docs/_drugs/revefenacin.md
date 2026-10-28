---
layout: default
title: Revefenacin
parent: Apenas Predição do Modelo (L5)
nav_order: 564
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-13
description: "Revefenacin: nova indicação prevista, Bronquite (bronchitis) (nível de evidência L4). Indicação original: Anticolinérgicos"
monitor_inn: "revefenacin"
predicted_indications: ["bronchitis"]
---

# Revefenacin
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **1** 
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

## Revefenacina: De anticolinérgico à bronquite
{: .text-alpha }

## Resumo em Uma Frase

A revefenacina (YUPELRI) é um anticolinérgico inalatório, registrado na ANVISA na classe "anticolinérgicos".
O modelo TxGNN prevê que ela pode ser eficaz para **bronquite (bronchitis)**, mas há apenas **1 ensaio clínico** indireto (realizado em DPOC) e **nenhuma publicação** que apoie diretamente esta indicação.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anticolinérgicos (classe terapêutica registrada na ANVISA) |
| Nova Indicação Prevista | Bronquite (bronchitis) |
| Pontuação de Previsão TxGNN | 0,9961 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Os dados compilados para este relatório não trazem o mecanismo de ação detalhado da revefenacina. Segundo informações conhecidas, ela é um antagonista muscarínico de longa ação (LAMA), seletivo para o pulmão e administrado por nebulização uma vez ao dia. Ao bloquear os receptores M3 na musculatura lisa das vias aéreas, produz broncodilatação sustentada.

A relação com a bronquite é plausível, mas indireta. A redução do tônus colinérgico pode diminuir a hipersecreção de muco, o que seria relevante na bronquite crônica. A bronquite crônica é um fenótipo da DPOC, doença em que a revefenacina já tem uso estabelecido.

O único ensaio ligado a esta previsão incluiu pacientes com DPOC, e não uma população específica com bronquite. Não há dados sobre bronquite como indicação isolada, seja aguda ou infecciosa. A pontuação TxGNN muito alta (0,9961) é uma previsão computacional e não constitui evidência clínica.

Uma segunda previsão do modelo, "doença pulmonar obstrutiva", tem evidência muito mais robusta, com vários ensaios de Fase 3 em DPOC. Isso corresponde, porém, a um uso já aprovado em outros países (FDA, 2018) e não a um reposicionamento genuíno.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01704404](https://clinicaltrials.gov/study/NCT01704404) | Phase 2 | Concluído | 62 | Estudo de farmacodinâmica, segurança, tolerabilidade e farmacocinética de doses múltiplas por 7 dias em pacientes com DPOC. Caracteriza a resposta à dose. Não tem desfecho de eficácia em bronquite, portanto o apoio é apenas indireto. |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 188300100 (cancelado) | YUPELRI | Não informada | ANTICOLINÉRGICOS |

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 146 interações, e as 20 principais listadas nos dados compilados são todas de gravidade **moderada**. Os grupos mais relevantes são:
  - Outros anticolinérgicos e antimuscarínicos: hiosciamina, atropina, glicopirrônio, clidínio, diciclomina, trópio, mepenzolato, metescopolamina, propantelina e escopolamina.
  - Outros fármacos: prometazina, cobicistate, eluxadoline, ácido obeticólico, procaloprida, fisostigmina oftálmica, eltrombopague, artesunato e abiraterona.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para bronquite se apoia em um único ensaio de Fase 2 conduzido em DPOC, sem desfecho em bronquite e sem literatura específica. Isso corresponde ao nível de evidência L4.
- O registro brasileiro está cancelado, e a evidência robusta existente refere-se à DPOC, que não é uma nova indicação.

**Para prosseguir, é necessário:**
- Obter da bula na ANVISA as advertências e contraindicações, hoje indisponíveis, para a triagem de segurança.
- Obter dados detalhados do mecanismo de ação (MOA), por exemplo via DrugBank.
- Obter estudos clínicos ou observacionais específicos em bronquite crônica, distinguindo-a de bronquite aguda ou infecciosa.
- Confirmar a situação regulatória e a disponibilidade comercial atuais no Brasil, já que o único registro está cancelado.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

