---
layout: default
title: Gadobutrol
parent: 僅模型預測 (L5)
nav_order: 259
evidence_level: L5
indication_count: 10
---

# Gadobutrol
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

# Gadobutrol: De Agente de Contraste para RM à Hiperplasia Prostática Benigna

## Resumo em Uma Frase

Gadobutrol (Gadovist®) é um agente de contraste paramagnético à base de gadolínio de alta concentração (1,0 mol/L), aprovado exclusivamente para uso diagnóstico em ressonância magnética — sem qualquer indicação terapêutica conhecida.
O modelo TxGNN prevê possível associação com **Hiperplasia Prostática Benigna (Benign Prostatic Hyperplasia)**,
porém atualmente há **0 ensaios clínicos** e **0 publicações** apoiando essa direção terapêutica — e a análise mecanística indica tratar-se de falsa associação gerada por co-ocorrência no grafo de conhecimento.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Agente de contraste para RM (uso diagnóstico) |
| Nova Indicação Prevista | Hiperplasia Prostática Benigna (Benign Prostatic Hyperplasia) |
| Pontuação de Previsão TxGNN | 83,24% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Gadobutrol é um quelato macrocíclico de gadolínio em formulação de alta molaridade (1,0 mol/L). Seu mecanismo de ação é estritamente físico-químico: ao ser administrado por via intravenosa, o íon gadolínio quelado encurta o tempo de relaxamento longitudinal (T1) dos tecidos adjacentes, intensificando o sinal de RM e gerando maior contraste nas imagens. Não há qualquer efeito farmacológico sistêmico que atue sobre células, receptores ou vias de sinalização de doenças.

A previsão para hiperplasia prostática benigna (HPB) **não possui embasamento mecanístico**. A HPB envolve proliferação de células musculares lisas e epiteliais da zona de transição prostática; seu tratamento farmacológico requer antagonistas alfa-1 adrenérgicos, inibidores da 5-alfa-redutase ou antimuscarínicos — classes sem qualquer sobreposição com o perfil de um quelato de gadolínio. Gadobutrol não possui atividade antiproliferativa, anti-inflamatória ou hormonal.

A alta pontuação TxGNN (83,24%, a mais elevada entre todas as previsões para este fármaco) é provavelmente um artefato de co-ocorrência no grafo de conhecimento: gadobutrol é amplamente utilizado em RM multiparamétrica da próstata (mp-MRI) para diagnóstico e estadiamento da HPB e do câncer de próstata. Essa frequente co-ocorrência entre fármaco e doença no KG é de natureza diagnóstica, não terapêutica — e o modelo interpretou erroneamente a associação como potencial reposicionamento.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para o uso terapêutico de Gadobutrol em Hiperplasia Prostática Benigna.

---

## Evidências da Literatura

Atualmente não há literatura relacionada ao uso terapêutico de Gadobutrol em Hiperplasia Prostática Benigna.

---

## Informações de Comercialização no Brasil

O Gadobutrol possui **1 registro ativo** no Brasil (situação: comercializado). Os detalhes específicos — número de registro, nome comercial, forma farmacêutica e texto de indicação aprovada — não estão disponíveis nos dados fornecidos. Recomenda-se consultar diretamente o portal da ANVISA (https://consultas.anvisa.gov.br/) para informações completas do produto registrado.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Gadobutrol é um agente de contraste diagnóstico para RM, sem qualquer mecanismo de ação terapêutico — o que torna inviável qualquer reposicionamento para HPB ou para as demais 9 indicações previstas pelo TxGNN, todas com recomendação "Hold". A previsão de alta pontuação é um artefato sistemático do grafo de conhecimento decorrente do amplo uso diagnóstico do fármaco em múltiplas condições, não de evidência de eficácia terapêutica.

**Para prosseguir, seria necessário:**
- Identificação de mecanismo farmacológico terapêutico plausível (atualmente inexistente para qualquer indicação)
- Dados pré-clínicos demonstrando efeito biológico ativo em HPB ou outra condição-alvo
- Reavaliação estrutural do pipeline TxGNN para **excluir agentes de diagnóstico** (quelatos de gadolínio, meios de contraste iodados, radiofármacos) do escopo de reposicionamento terapêutico, evitando falsos positivos sistemáticos gerados por co-ocorrência diagnóstica no KG
---

