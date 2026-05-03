---
layout: default
title: Abemaciclibe
parent: 僅模型預測 (L5)
nav_order: 13
evidence_level: L5
indication_count: 0
---

# Abemaciclibe
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

# Abemaciclib: Do Câncer de Mama a Nova Indicação — Predição TxGNN Pendente

## Resumo

Abemaciclib (ABEMACICLIBE) é um inibidor seletivo de CDK4/6, originalmente aprovado para o tratamento do câncer de mama hormônio-receptor positivo e HER2-negativo (HR+/HER2-). O modelo TxGNN **ainda não gerou previsões de reposicionamento** para este fármaco neste ciclo de análise, pois dados essenciais — DrugBank ID e mecanismo de ação — estão pendentes de coleta. O presente relatório documenta o estado atual da evidência e define os próximos passos obrigatórios antes de prosseguir.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Câncer de mama HR+/HER2- |
| Nova Indicação Prevista | ⏳ Pendente — predição TxGNN não disponível |
| Pontuação de Previsão TxGNN | ⏳ Pendente |
| Nível de Evidência | ⏳ Pendente |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 1 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão É Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis no Evidence Pack. Segundo informações conhecidas, abemaciclib pertence à classe dos inibidores de CDK4/6 (quinases dependentes de ciclina 4 e 6), enzimas que regulam a transição G1→S do ciclo celular. Sua eficácia no câncer de mama HR+/HER2- foi comprovada em estudos de fase III (MONARCH-2, MONARCH-3), e mecanisticamente pode ser aplicável a outros tumores com hiperativação do eixo ciclina D–CDK4/6–Rb — incluindo tumores hematológicos, glioblastoma e alguns carcinomas de pulmão.

A ausência do DrugBank ID impede o mapeamento correto no grafo de conhecimento do TxGNN, bloqueando a geração de predições. Uma vez resolvida essa lacuna, espera-se que o modelo identifique indicações candidatas com base nas relações moleculares entre CDK4/6, vias de sinalização e doenças representadas no grafo.

---

## Informações de Comercialização no Brasil

O Evidence Pack confirma **1 registro ativo** com status **Comercializado**, porém os detalhes do registro não foram recuperados na consulta atual à base de dados. Recomenda-se consulta direta à ANVISA para obter:

| Campo | Status |
|-------|--------|
| Número de registro | Não recuperado |
| Nome comercial | Não recuperado |
| Forma farmacêutica | Não recuperada |
| Indicação aprovada | Não recuperada |

> 💡 **Ação imediata**: Busca manual em [consultas.anvisa.gov.br](https://consultas.anvisa.gov.br) com o termo "ABEMACICLIBE" para obter o registro completo.

---

## Citotoxicidade

Abemaciclib é um antineoplásico da classe das terapias-alvo moleculares.

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia-alvo (Inibidor seletivo de CDK4/6) |
| Risco de Mielossupressão | Médio — neutropenia é evento adverso frequente na classe CDK4/6 |
| Classificação de Emetogenicidade | Baixa a média (oral) |
| Itens de Monitoramento | Hemograma completo (CBC), função hepática (ALT/AST), função renal, sinais de infecção |
| Proteção no Manuseio | Necessário seguir regulamentos de manuseio de citotóxicos orais |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> ⚠️ **Dados de segurança TFDA/ANVISA não foram recuperados neste ciclo** (DG001 — Bloqueante). A análise de advertências e contraindicações está pendente de download e análise do PDF da bula.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
O Evidence Pack de ABEMACICLIBE está incompleto em itens críticos — ausência de predições TxGNN, DrugBank ID não mapeado e dados de segurança não recuperados — o que impede qualquer avaliação formal de reposicionamento neste momento.

**Para prosseguir, é necessário:**

- [ ] **[Bloqueante]** Baixar e analisar o PDF da bula no portal ANVISA para obter advertências, contraindicações e precauções (DG001)
- [ ] **[Alta prioridade]** Consultar DrugBank API para obter o DrugBank ID e dados de MOA completos (DG002)
- [ ] Preencher os detalhes do registro ANVISA (número, nome comercial, forma farmacêutica, indicação aprovada)
- [ ] Re-executar o pipeline TxGNN após resolver DG001 e DG002, para gerar predições de reposicionamento
- [ ] Após obtenção das predições, atualizar este relatório com a tabela de ensaios clínicos, literatura e nível de evidência
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

