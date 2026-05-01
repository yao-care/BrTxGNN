---
layout: default
title: Clindamycin
parent: 僅模型預測 (L5)
nav_order: 191
evidence_level: L5
indication_count: 10
---

# Clindamycin
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

Usando o skill `txgnn-pipeline` para contextualizar o relatório BrTxGNN. Gerando o relatório agora com base no Evidence Pack fornecido.

---

# Clindamycin: De infecções bacterianas à ceratoconjuntivite epitelial punctata

## Resumo em Uma Frase

Clindamycin é um antibiótico da classe das lincosamidas, historicamente utilizado no tratamento de infecções por bactérias gram-positivas e anaeróbios.
O modelo TxGNN prevê que pode ser eficaz para **Ceratoconjuntivite Epitelial Punctata (Punctate Epithelial Keratoconjunctivitis)**, porém atualmente há **0 ensaios clínicos** e **0 publicações** apoiando diretamente esta direção — a previsão baseia-se exclusivamente no modelo, sem suporte empírico identificado.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Sem registro nacional disponível |
| Nova Indicação Prevista | Ceratoconjuntivite Epitelial Punctata (Punctate Epithelial Keratoconjunctivitis) |
| Pontuação de Previsão TxGNN | 99.97% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Clindamycin é um antibiótico lincosamida com atividade contra bactérias gram-positivas (incluindo *Staphylococcus aureus* sensível à meticilina) e anaeróbios. Seu mecanismo de ação envolve a inibição da síntese proteica bacteriana pela ligação reversível à subunidade ribossomal 50S, bloqueando a translocação peptídica. Os dados detalhados de MOA desta entrada específica do DrugBank não estavam disponíveis no momento da análise.

A ceratoconjuntivite epitelial punctata tem como principal etiologia infecções virais (adenovírus, HSV) ou síndrome do olho seco, com proporção muito baixa de casos de origem bacteriana primária. A cobertura antimicrobiana de Clindamycin — focada em gram-positivos e anaeróbios — não se alinha ao mecanismo patológico predominante dessa condição ocular.

A alta pontuação do TxGNN (99,97%) provavelmente decorre de compartilhamento de nós vizinhos no grafo do conhecimento com outros agentes anti-infecciosos oftálmicos, e não de uma relação mecanística direta. Trata-se de um **risco elevado de falso positivo por inferência gráfica** — padrão reconhecido em modelos GNN quando o fármaco pertence a uma classe bem representada no grafo.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada à indicação principal (ceratoconjuntivite epitelial punctata).

> **Nota sobre indicações secundárias:** A segunda indicação prevista (ceratite de exposição — rank 2, score 99,79%) conta com **4 publicações** de suporte indireto, relacionadas a infecções oculares por *S. aureus* e *Bacillus cereus*. Nenhuma avalia Clindamycin diretamente para ceratite de exposição; a evidência é apenas de plausibilidade microbiológica. As demais indicações previstas (ranks 3–10) incluem doenças veterinárias, condições neurológicas e patologias sem mecanismo antibiótico aplicável — todas com decisão **Hold**.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para ceratoconjuntivite epitelial punctata é classificada como **L5** (apenas modelo, sem estudos reais) e apresenta baixa plausibilidade mecanística, pois a doença tem etiologia predominantemente viral ou relacionada ao olho seco — contextos em que Clindamycin não possui atividade estabelecida. Todas as 10 indicações previstas receberam recomendação **Hold**, nenhuma atingiu o nível mínimo de evidência para avançar.

**Para reavaliar, é necessário:**
- Obter o MOA detalhado do DrugBank (DG002) para análise de relevância mecanística
- Levantar advertências e contraindicações da bula oficial (DG001) antes de qualquer avaliação de segurança
- Investigar se Clindamycin possui formulações oftálmicas tópicas registradas em outros mercados (ex.: colírio), o que poderia reabrir a análise de ceratite de exposição com infecção bacteriana secundária confirmada
- Considerar redirecionar a busca de reposicionamento para indicações com maior suporte biológico (ex.: infecções de pele e tecidos moles, infecções pélvicas anaeróbias, ou vaginose bacteriana — usos já estabelecidos na literatura internacional para Clindamycin)
---

