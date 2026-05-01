---
layout: default
title: Ticlopidina Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 442
evidence_level: L5
indication_count: 0
---

# Ticlopidina Hydrochloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Ticlopidina Cloridrato: Avaliação Indisponível por Dados Insuficientes

## Resumo

Ticlopidina é um antiagregante plaquetário da classe das tienopiridinas, historicamente utilizado na prevenção secundária de acidentes vasculares cerebrais (AVC) e eventos isquêmicos. O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco no ciclo atual, possivelmente em razão da ausência de indicações cadastradas e dados regulatórios. Com **0 registros na ANVISA** e informações de segurança indisponíveis, não é possível realizar uma avaliação de reposicionamento completa neste momento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Prevenção de AVC isquêmico e eventos tromboembólicos |
| Nova Indicação Prevista | Não disponível |
| Pontuação de Previsão TxGNN | Não disponível |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no Evidence Pack. Segundo informações conhecidas, ticlopidina faz parte da classe das tienopiridinas — a mesma do clopidogrel —, e sua eficácia na prevenção de eventos tromboembólicos foi comprovada historicamente. Mecanisticamente, atua inibindo de forma irreversível o receptor purinérgico **P2Y12** nas plaquetas, bloqueando a ativação mediada por ADP e, consequentemente, a cascata de agregação plaquetária.

O fármaco foi amplamente utilizado nas décadas de 1990 e 2000 para prevenção secundária de AVC isquêmico e síndrome coronariana aguda. Entretanto, foi gradualmente substituído por clopidogrel — da mesma classe terapêutica, com perfil de segurança mais favorável — em razão de efeitos adversos graves documentados com ticlopidina, como neutropenia severa e púrpura trombocitopênica trombótica (PTT).

O modelo TxGNN não gerou candidatos de reposicionamento neste ciclo. A ausência de indicações originais cadastradas no sistema e de registros regulatórios no Brasil provavelmente impediu o processamento adequado do candidato. Uma análise de reposicionamento significativa só será possível após o preenchimento das lacunas de dados identificadas (DG001, DG002).

---

## Informações de Comercialização no Brasil

Ticlopidina Cloridrato **não possui registros ativos na ANVISA**. O fármaco não está comercializado no Brasil. Recomenda-se verificar se houve registros históricos que possam ter sido cancelados ou retirados do mercado, bem como consultar bulas de mercados onde o produto permanece aprovado (ex.: referências do FDA ou EMA) para obter informações regulatórias complementares.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> **Nota:** Como o fármaco não está registrado no Brasil, recomenda-se consultar o DrugBank (ID esperado: DB01124) e referências internacionais para informações sobre advertências, contraindicações e interações medicamentosas — em especial o risco de neutropenia e PTT, efeitos adversos historicamente associados a este fármaco.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não gerou previsões de reposicionamento para ticlopidina, e a ausência de registros regulatórios no Brasil, de indicações cadastradas e de dados de segurança impede qualquer avanço na avaliação neste momento.

**Para prosseguir, é necessário:**
- Verificar a padronização do nome: o INN correto é **ticlopidine** (inglês) / **ticlopidina** (português); confirmar mapeamento para o DrugBank ID correspondente
- Obter dados de mecanismo de ação (MOA) via consulta ao DrugBank (lacuna **DG002**)
- Baixar e analisar bula de referência internacional para extrair advertências e contraindicações (lacuna **DG001**)
- Verificar histórico de registros na ANVISA — o fármaco pode ter tido licença anterior que foi cancelada
- Cadastrar as indicações originais no sistema antes de reprocessar a previsão TxGNN
- Avaliar a relevância clínica atual do candidato, considerando que clopidogrel e prasugrel são amplamente preferidos na prática clínica contemporânea, o que pode limitar o interesse em reposicionamento
---

