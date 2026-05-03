---
layout: default
title: Azelastina Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 89
evidence_level: L5
indication_count: 0
---

# Azelastina Hydrochloride
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

# Cloridrato de Azelastina: Avaliação de Reposicionamento — Dados Insuficientes para Previsão

## Resumo em Uma Frase

Cloridrato de Azelastina é um anti-histamínico de segunda geração, reconhecido clinicamente no tratamento da rinite alérgica e da conjuntivite alérgica. O modelo TxGNN **não gerou previsões de novas indicações** para este fármaco na execução atual, pois nenhum registro foi localizado na base regulatória consultada com o termo "AZELASTINA HYDROCHLORIDE". São necessários dados complementares antes de prosseguir com qualquer análise de reposicionamento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Rinite alérgica / Conjuntivite alérgica (base de conhecimento farmacológico geral) |
| Nova Indicação Prevista | Não disponível — nenhuma previsão TxGNN gerada |
| Pontuação de Previsão TxGNN | Não disponível |
| Nível de Evidência | L5 (sem previsão gerada pelo modelo) |
| Situação no Mercado Brasileiro | Não comercializado (0 registros encontrados) |
| Número de Registros | 0 |
| Decisão Recomendada | **Hold** |

---

## Contexto Farmacológico Conhecido

Não há dados de mecanismo de ação (MOA) no Evidence Pack, nem registros regulatórios que permitam análise de indicação original. Com base no conhecimento farmacológico disponível na literatura:

A azelastina é um **antagonista seletivo dos receptores H1 de histamina**, pertencente à classe dos anti-histamínicos de segunda geração. Diferentemente dos anti-histamínicos de primeira geração, apresenta menor penetração no sistema nervoso central, com perfil de sedação reduzido. Além do bloqueio H1, demonstra propriedades anti-inflamatórias adicionais, incluindo inibição de mastócitos e redução de mediadores inflamatórios (leucotrienos, citocinas pró-inflamatórias), o que confere ao fármaco potencial terapêutico em condições além da resposta histamínica imediata.

As formulações mais comuns são a solução nasal (spray) para rinite alérgica sazonal e perene, e o colírio para conjuntivite alérgica. Este perfil farmacológico, com ação anti-inflamatória e antianafiláctica documentada, seria o ponto de partida para hipóteses de reposicionamento — contudo, sem dados de previsão TxGNN ativos, não é possível avançar nessa análise dentro do protocolo estabelecido.

---

## Informações de Comercialização no Brasil

Nenhum registro foi encontrado na base de dados regulatória com o termo de busca **"AZELASTINA HYDROCHLORIDE"**. Possíveis razões:

- O fármaco pode estar registrado sob nomenclatura em português: **"Cloridrato de Azelastina"** ou simplesmente **"Azelastina"**
- Pode haver registro apenas por nome comercial (ex.: Allergodil®, Azedine®)
- O registro pode ter sido feito apenas para a combinação com fluticasona (Dymista®), sem entrada isolada

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O modelo TxGNN não produziu nenhuma indicação candidata para este fármaco, e a base regulatória brasileira não retornou registros com o termo de busca utilizado. Sem uma indicação-alvo prevista e sem dados regulatórios confirmados, o protocolo de avaliação não pode avançar para as etapas de análise de evidências e segurança.

**Para prosseguir, é necessário:**
- Repetir a consulta regulatória com termos alternativos: `"Cloridrato de Azelastina"`, `"Azelastina"`, `"Azelastine"`
- Obter o **DrugBank ID** correto (a consulta ao DrugBank retornou 1 resultado — revisar e confirmar o mapeamento)
- Com o DrugBank ID confirmado, **reexecutar o modelo TxGNN** para gerar previsões de reposicionamento
- Coletar dados de **MOA** e **advertências/contraindicações** a partir do DrugBank e da bula registrada
- Verificar se há dados de interações medicamentosas relevantes (DDI retornou `not_found`)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

