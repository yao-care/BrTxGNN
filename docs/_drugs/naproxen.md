---
layout: default
title: Naproxen
parent: 僅模型預測 (L5)
nav_order: 356
evidence_level: L5
indication_count: 4
---

# Naproxen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Verificando o skill relevante — `txgnn-pipeline` carregado. Procedo agora com a geração do relatório de avaliação com base no Evidence Pack fornecido.

---

# Naproxen: De Anti-inflamatório e Analgésico para Síndrome de Braquidactilia-Sindactilia

## Resumo em Uma Frase

Naproxen é um anti-inflamatório não esteroidal (AINE) amplamente utilizado no tratamento da dor aguda e crônica, inflamação e condições reumáticas — uma das classes farmacológicas mais prescritas no mundo. O modelo TxGNN prevê que pode ser eficaz para a **Síndrome de Braquidactilia-Sindactilia (brachydactyly-syndactyly syndrome)**, porém esta direção não conta com **nenhum ensaio clínico** nem **publicação científica** de suporte — apenas a previsão computacional do modelo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Não disponível nos registros ANVISA desta consulta |
| Nova Indicação Prevista | Síndrome de Braquidactilia-Sindactilia (brachydactyly-syndactyly syndrome) |
| Pontuação de Previsão TxGNN | 99,35% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Naproxen é um AINE da classe dos ácidos propiônicos que atua por inibição competitiva das enzimas COX-1 e COX-2, reduzindo a síntese de prostaglandinas, tromboxanos e prostaciclinas. Isso se traduz em efeitos anti-inflamatórios, analgésicos e antipiréticos bem estabelecidos. Os dados completos do mecanismo de ação não estão disponíveis neste Evidence Pack — a recuperação via DrugBank API está pendente e deverá complementar esta análise.

A **Síndrome de Braquidactilia-Sindactilia** é uma rara malformação congênita dos membros, causada primariamente por mutações nos genes de padronização do desenvolvimento dos membros (como *HOXD13* e *GJA1*), que resultam em dedos encurtados e fundidos. Embora a prostaglandina E2 (PGE2) exerça papel modulador no desenvolvimento ósseo embrionário, esta função se insere num contexto estritamente de morfogênese embrionária — muito distante do mecanismo terapêutico anti-inflamatório de Naproxen em pacientes adultos ou pediátricos pós-natais.

A análise técnica inclusa no Evidence Pack indica que **esta associação provavelmente reflete ruído topológico do grafo de conhecimento**: o alto escore TxGNN decorre da proximidade estrutural entre o nó de "fenótipos esqueléticos" — compartilhado com doenças como osteoartrite e artrite reumatoide, onde o Naproxen tem eficácia amplamente documentada — e o nó desta síndrome rara, gerando uma correlação artificial sem respaldo farmacológico real. Nenhuma evidência pré-clínica foi identificada que valide este reposicionamento.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

O Naproxen possui **20 registros ativos na ANVISA**, confirmando disponibilidade comercial consolidada no Brasil. Os detalhes individuais de cada registro (nome comercial, forma farmacêutica, indicação aprovada) não foram retornados nesta consulta e devem ser verificados diretamente no portal da ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
As quatro indicações previstas neste Evidence Pack — Síndrome de Braquidactilia-Sindactilia, Síndrome de Microftalmia Colobomatosa com Displasia Rizomélica, Displasia Acromesomélica tipo Hunter-Thompson e Síndrome de Brachyolmia-Amelogenesis Imperfecta — são todas raras síndromes de desenvolvimento esquelético congênito de base genética, sem qualquer ensaio clínico ou publicação de suporte identificados. O padrão uniforme de predições de alto escore para doenças esqueléticas raras sugere um artefato estrutural do grafo de conhecimento (proximidade topológica com nós de doenças ósseas onde Naproxen já está mapeado), e não um sinal farmacológico genuíno de reposicionamento.

**Para prosseguir, é necessário:**
- Recuperar o mecanismo de ação completo (MOA) do Naproxen via DrugBank API para fundamentar análises mecanísticas
- Consultar a bula ANVISA para advertências, precauções e contraindicações antes de qualquer avaliação de segurança
- Complementar os detalhes dos 20 registros ANVISA (nome comercial, forma farmacêutica, indicação aprovada)
- Consultar especialista em dismorfologia ou genética clínica para avaliar se há qualquer plausibilidade terapêutica de AINEs nas quatro síndromes identificadas
- Considerar análise de ruído do modelo TxGNN para investigar se o padrão de predições em síndromes esqueléticas raras é sistemático para outros AINEs
---

