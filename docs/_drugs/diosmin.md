---
layout: default
title: Diosmin
parent: 僅模型預測 (L5)
nav_order: 224
evidence_level: L5
indication_count: 10
---

# Diosmin
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

Com base no Evidence Pack fornecido, aqui está o relatório de avaliação completo:

---

# Diosmin: Da Insuficiência Venosa Crônica à Amenorreia

## Resumo em Uma Frase

Diosmin é um flavonoide venotônico amplamente utilizado no tratamento de insuficiência venosa crônica e hemorroidas.
O modelo TxGNN prevê que pode ser eficaz para **Amenorreia (Amenorrhea)**, com pontuação de 99,42%.
Atualmente, **não há ensaios clínicos nem publicações** que apoiem esta direção — a previsão carece de respaldo clínico e a ligação mecanística é biologicamente implausível.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Insuficiência venosa crônica, hemorroidas e varizes |
| Nova Indicação Prevista | Amenorreia (Amenorrhea) |
| Pontuação de Previsão TxGNN | 99,42% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Diosmin é um flavonoide derivado da hesperidina, com perfil farmacológico venotônico e venoativo. Embora os dados de mecanismo de ação detalhado não estejam disponíveis no Evidence Pack atual, o conhecimento farmacológico consolidado indica que o Diosmin atua reduzindo a hiperpermeabilidade capilar, inibindo a ativação de células endoteliais, suprimindo a inflamação vascular e exercendo atividade antiplaquetária leve. Sua aplicação clínica estabelecida está restrita ao sistema venoso periférico.

A ligação mecanística entre Diosmin e amenorreia é biologicamente fraca. Amenorreia resulta de causas hormonais (ex: insuficiência ovariana, hiperprolactinemia), estruturais (ex: síndrome de Asherman) ou funcionais (ex: amenorreia hipotalâmica por estresse), todas afetando o eixo hipotálamo-hipófise-ovário — espectro completamente distinto do perfil venotônico do Diosmin. A previsão TxGNN provavelmente capturou um caminho topológico indireto no grafo de conhecimento ("congestão venosa uterina" → "irregularidade menstrual"), constituindo um falso positivo do modelo.

Destaca-se que, entre as 10 indicações avaliadas neste lote, **Trombofilia (rank 7, score 92,94%)** apresenta a conexão mecanística mais robusta e é a candidata mais promissora: o Diosmin possui atividade antiplaquetária documentada, protege o endotélio vascular (fator de risco trombótico primário) e exerce efeito anti-inflamatório que reduz o estado pró-coagulante. O estudo RIDILOTT DVT (PubMed 32348101) testou a combinação Diosmin + Rivaroxabana em trombose venosa profunda, oferecendo suporte clínico indireto relevante.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Diosmin em amenorreia.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para Diosmin em amenorreia.

---

## Informações de Comercialização no Brasil

O Diosmin possui **20 registros** ativos junto à ANVISA e está atualmente comercializado no Brasil. Os detalhes específicos dos produtos (nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis nesta versão do Evidence Pack. Recomenda-se consulta direta ao portal da ANVISA (https://consultas.anvisa.gov.br/) para obter a listagem completa.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão TxGNN de Diosmin para amenorreia apresenta nível de evidência L5 — baseada exclusivamente no modelo, sem qualquer suporte de ensaios clínicos ou literatura, e com mecanismo de ação biologicamente improvável. O alto score (99,42%) reflete conectividade topológica no grafo de conhecimento, não relevância clínica real. A indicação prioritária para investigação futura é **Trombofilia (rank 7)**, a única com evidência L4 e plausibilidade mecanística credível entre as 10 previsões avaliadas.

**Para prosseguir, é necessário:**
- Redirecionar a investigação para **Trombofilia** como indicação principal, com busca ativa de ensaios clínicos em DVT, trombofilia hereditária e síndrome antifosfolipídio
- Obter dados completos de mecanismo de ação (MOA) via DrugBank API (lacuna classificada como severidade *High* no Evidence Pack)
- Obter a bula via portal da ANVISA para preenchimento das advertências, contraindicações e forma farmacêutica dos 20 registros (lacuna classificada como *Blocking*)
- Avaliar o estudo RIDILOTT DVT (PubMed 32348101) como ponto de partida para o dossiê de evidências em trombofilia
- Reavaliar as previsões de rank 2–6 (distúrbios plaquetários e coagulopatias) com cautela: o perfil antiplaquetário do Diosmin pode representar **risco de agravamento** nessas indicações, não benefício
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

