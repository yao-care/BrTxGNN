---
layout: default
title: Gadoteridol
parent: 僅模型預測 (L5)
nav_order: 260
evidence_level: L5
indication_count: 10
---

# Gadoteridol
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

# Gadoteridol: Do diagnóstico por imagem à suscetibilidade à osteoartrite

## Resumo em Uma Frase

Gadoteridol (ProHance®) é um quelato de gadolínio não-iônico, originalmente utilizado como agente de contraste intravenoso para exames de ressonância magnética (MRI), amplamente empregado no diagnóstico de doenças do sistema nervoso central e corpo.
O modelo TxGNN prevê que pode ser eficaz para **Suscetibilidade à Osteoartrite (Osteoarthritis Susceptibility)**,
porém **não há ensaios clínicos nem publicações** apoiando esta direção terapêutica — trata-se de uma previsão baseada exclusivamente em proximidade topológica no grafo de conhecimento, sem qualquer suporte mecanístico de atividade terapêutica.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Agente de contraste para ressonância magnética (MRI) |
| Nova Indicação Prevista | Suscetibilidade à Osteoartrite (Osteoarthritis Susceptibility) |
| Pontuação de Previsão TxGNN | 98,90% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Gadoteridol (ProHance®) é um agente de contraste paramagnético composto por gadolínio quelado com HP-DO3A (ácido 10-(2-hidroxipropil)-1,4,7,10-tetraazaciclododecano-1,4,7-triacético). Seu mecanismo de ação é estritamente **físico-químico**: ao encurtar o tempo de relaxamento T1 dos prótons de água nos tecidos adjacentes, intensifica o sinal nas imagens de ressonância magnética. Gadoteridol **não possui mecanismo de ação farmacológica terapêutica** — é um agente diagnóstico de administração única por via intravascular, sem atividade biológica conhecida sobre processos patológicos como inflamação, degradação de cartilagem ou remodelamento ósseo.

A previsão do TxGNN para suscetibilidade à osteoartrite provavelmente decorre da **proximidade no grafo de conhecimento** entre o Gadoteridol e nós associados a tecidos ósseos e cartilaginosos. Na literatura científica, Gadoteridol é de fato amplamente citado em estudos de imagem de cartilagem articular — tomografia computadorizada com duplo contraste (CA4+ + gadoteridol), microCT por sincrotron e CT com contagem de fótons —, utilizados para quantificar proteoglicanos e avaliar composição da cartilagem em contextos de osteoartrite. No entanto, toda essa literatura descreve **uso diagnóstico do contraste**, não intervenção terapêutica.

A previsão deve ser interpretada como um **artefato de topologia do modelo**: a conectividade entre Gadoteridol e nós de "osso/cartilagem" no grafo de conhecimento gera uma pontuação elevada (98,90%), mas não reflete qualquer atividade biológica capaz de tratar, prevenir ou modificar a progressão da osteoartrite. Este padrão — alta pontuação TxGNN sem suporte mecanístico ou clínico — é consistente com previsões L5 de baixa confiabilidade para agentes diagnósticos.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Não disponível na consulta | Gadoteridol | Não disponível na consulta | Agente de contraste paramagnético para MRI (detalhes completos da bula não obtidos nesta consulta) |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Gadoteridol é um agente de contraste para diagnóstico por imagem — não um fármaco com atividade terapêutica. Todas as 10 indicações previstas pelo TxGNN são classificadas como L5 (previsão de modelo apenas), sem ensaios clínicos nem literatura de intervenção terapêutica. A literatura encontrada para osteoartrite (12 publicações, indicação de rank 2) e artrite reumatoide (4 publicações, rank 3) descreve exclusivamente estudos de imagem onde o Gadoteridol é utilizado como **ferramenta diagnóstica**, não como agente de tratamento. Não há base científica para reposicionamento terapêutico deste fármaco em nenhuma das indicações previstas.

**Para prosseguir (caso haja interesse em investigação futura), é necessário:**
- Obter dados completos de segurança da bula ANVISA, com atenção especial ao risco de **Fibrose Sistêmica Nefrogênica (NSF)** — risco documentado da classe GBCA em pacientes com insuficiência renal, altamente relevante para as populações alvo das indicações previstas (osteoartrite, artrite reumatoide, insuficiência cardíaca congestiva)
- Verificar se há dados de MOA documentados no DrugBank (atualmente em lacuna de dados)
- Investigar se há qualquer hipótese mecanística publicada que sugira atividade terapêutica do gadolínio quelado além do uso como contraste
- Considerar que o acúmulo de gadolínio em tecido ósseo (documentado na literatura, PMID [21305156](https://pubmed.ncbi.nlm.nih.gov/21305156/)) representa uma preocupação de segurança — não uma oportunidade terapêutica
- Reavaliar o pipeline TxGNN para identificar e filtrar agentes de contraste e outros compostos não-terapêuticos que geram falsos positivos por proximidade topológica no grafo de conhecimento
---

