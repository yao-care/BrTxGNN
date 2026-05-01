---
layout: default
title: Fluconazole
parent: 僅模型預測 (L5)
nav_order: 254
evidence_level: L5
indication_count: 10
---

# Fluconazole
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

# Fluconazole: Das infecções fúngicas à ceratoconjuntivite epitelial punctata

## Resumo em Uma Frase

Fluconazole é um antifúngico triazólico amplamente utilizado no tratamento de candidíase (oral, esofágica, vaginal e sistêmica) e meningite criptocócica, sendo um dos antifúngicos mais prescritos globalmente.
O modelo TxGNN prevê que pode ser eficaz para **Ceratoconjuntivite Epitelial Punctata (Punctate Epithelial Keratoconjunctivitis)**, porém atualmente há **0 ensaios clínicos** e **0 publicações** apoiando diretamente esta direção, resultando em evidência de nível mínimo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções fúngicas (candidíase, meningite criptocócica) — *sem registros ANVISA recuperados nesta consulta* |
| Nova Indicação Prevista | Ceratoconjuntivite Epitelial Punctata (Punctate Epithelial Keratoconjunctivitis) |
| Pontuação de Previsão TxGNN | 99,24% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Sem registro encontrado na consulta automatizada ⚠️ |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

> ⚠️ **Nota sobre dados regulatórios:** O Fluconazole consta na Lista de Medicamentos Essenciais da OMS e é amplamente comercializado em mercados globais (incluindo Brasil, onde Diflucan® e genéricos são conhecidos). O resultado de 0 registros ANVISA provavelmente indica uma lacuna na coleta automatizada de dados, e não ausência real de registro. Recomenda-se verificação manual direta no portal ANVISA.

---

## Por que Esta Previsão é Razoável?

Não há dados de mecanismo de ação (MOA) recuperados automaticamente para este relatório. Com base no conhecimento farmacológico estabelecido, o Fluconazole é um antifúngico da classe dos triazóis que atua inibindo seletivamente a enzima CYP51 fúngica (lanosterol 14α-desmetilase), bloqueando a biossíntese de ergosterol — componente essencial da membrana celular dos fungos. Este mecanismo é altamente seletivo para fungos que dependem de ergosterol como esterol de membrana primário, como *Candida spp.* e *Cryptococcus neoformans*.

A ceratoconjuntivite epitelial punctata é uma condição ocular caracterizada por múltiplos microfocos de lesão no epitélio da córnea e conjuntiva. Sua etiologia é predominantemente não fúngica: infecção viral (adenovírus, herpes simplex), síndrome do olho seco, toxicidade por colírios ou blefarite são as causas mais frequentes. Infecções oculares fúngicas verdadeiras — que teoricamente poderiam responder ao Fluconazole — representam uma fração mínima dos casos diagnosticados sob esta categoria e costumam se manifestar como ceratite fúngica (forma mais grave), não como a forma punctata superficial.

A elevada pontuação TxGNN (99,24%) provavelmente reflete a **proximidade topológica** entre nós de infecção ocular e nós de antifúngicos no grafo de conhecimento, e não uma conexão mecanística real e clinicamente relevante. Diante da ausência completa de literatura e ensaios clínicos de suporte, esta previsão não apresenta sustentação empírica para avançar além do estágio exploratório.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para ceratoconjuntivite epitelial punctata com Fluconazole.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para ceratoconjuntivite epitelial punctata com Fluconazole.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> **Observação adicional:** Embora os dados estruturados de segurança não tenham sido recuperados nesta consulta, cabe registrar que o Fluconazole possui perfil de segurança bem documentado na prática clínica: é conhecido inibidor potente de CYP2C9 e CYP3A4 (risco de interações com varfarina, tacrolimus, fenitoína, entre outros), hepatotoxicidade dose-dependente é uma reação adversa documentada (PMID: 1548414), e é contraindicado na gestação em doses altas (categoria D). Dados completos devem ser obtidos diretamente da bula aprovada.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A ceratoconjuntivite epitelial punctata tem etiologia predominantemente viral ou inflamatória não fúngica, tornando o mecanismo antifúngico do Fluconazole farmacologicamente incompatível com esta indicação. A ausência total de evidências clínicas e de literatura impede qualquer avanço além da previsão computacional.

**Para prosseguir, é necessário:**
- Verificar manualmente o registro ANVISA do Fluconazole no portal oficial (dados automatizados provavelmente incompletos)
- Obter dados de MOA completos via DrugBank API (DB00196)
- Obter advertências e contraindicações da bula ANVISA aprovada
- Revisar a hipótese de indicação: dentro deste Evidence Pack, a indicação **pneumocistose (rank 7, L3)** apresenta a base de evidências mais robusta, com **7 ensaios clínicos** (incluindo 2 Phase 3 concluídos com Fluconazole) e **20 publicações**, sendo um candidato mais promissor para análise aprofundada
- Para a indicação de rank 1, considerar descarte ou reclassificação no pipeline após confirmação da fraqueza mecanística
---

