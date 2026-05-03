---
layout: default
title: Basiliximab
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 10
---

# Basiliximab
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

# Basiliximab: Da prevenção de rejeição em transplante ao mieloma de plasmócitos

## Resumo em Uma Frase

Basiliximab é um anticorpo monoclonal quimérico antagonista do receptor de interleucina-2 (IL-2Rα/CD25), originalmente utilizado para a prevenção de rejeição aguda em transplante renal.
O modelo TxGNN prevê que pode ser eficaz para **Mieloma de Plasmócitos (Plasma Cell Myeloma)**,
atualmente com **3 ensaios clínicos** e **3 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Prevenção de rejeição aguda em transplante renal |
| Nova Indicação Prevista | Mieloma de Plasmócitos (Plasma Cell Myeloma) |
| Pontuação de Previsão TxGNN | 95,61% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 2 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis na base consultada. Segundo informações amplamente estabelecidas na literatura científica, Basiliximab é um anticorpo monoclonal quimérico (IgG1κ) que bloqueia especificamente o receptor de IL-2 (CD25/IL-2Rα) na superfície de linfócitos T ativados, inibindo a proliferação celular mediada por IL-2. Originalmente aprovado como imunossupressor para prevenir rejeição aguda no transplante renal, seu mecanismo central atua na supressão da resposta imune adaptativa contra o enxerto.

A conexão com o mieloma de plasmócitos emerge de um raciocínio imunológico: o CD25 é altamente expresso nas células T regulatórias (Tregs). No contexto do transplante autólogo de células-tronco (ASCT) para mieloma múltiplo, as Tregs se reconstituem rapidamente após o procedimento e suprimem respostas imunes antitumorais, favorecendo a progressão da doença. Ao deplecionar Tregs via bloqueio de CD25, o Basiliximab pode potencializar o efeito enxerto-versus-mieloma, reforçando a vigilância imune contra células neoplásicas residuais no período pós-ASCT.

Esta hipótese é diretamente suportada por um ensaio clínico de Fase 1 já concluído (NCT01526096), que investigou especificamente a segurança e viabilidade desta estratégia em 30 pacientes com mieloma múltiplo submetidos ao ASCT, além de um estudo piloto prospectivo publicado no *Journal for Immunotherapy of Cancer* em 2020, consolidando a plausibilidade biológica da abordagem.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01526096](https://clinicaltrials.gov/study/NCT01526096) | Phase 1 | Concluído | 30 | Avaliação da segurança e viabilidade da deplecção de Tregs com Basiliximab em pacientes com mieloma múltiplo submetidos ao transplante autólogo de células-tronco (ASCT); estudo piloto diretamente relacionado à indicação prevista |
| [NCT00975975](https://clinicaltrials.gov/study/NCT00975975) | Phase 2 | Concluído | 17 | Basiliximab combinado com ciclosporina para prevenção de GVHD em transplante alogênico não-mieloablativo para cânceres hematológicos; mecanismo de deplecção de células T ativadas aplicável ao contexto do mieloma |
| [NCT00594308](https://clinicaltrials.gov/study/NCT00594308) | N/A | Encerrado prematuramente | 10 | Comparação de Basiliximab + ciclosporina versus ciclosporina isolada na prevenção de GVHD; ensaio interrompido precocemente, evidência limitada e motivo do encerramento não documentado |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [31940591](https://pubmed.ncbi.nlm.nih.gov/31940591/) | 2020 | Prospective Pilot Study | Journal for Immunotherapy of Cancer | Deplecção de Tregs com Basiliximab em ASCT para mieloma múltiplo demonstrou viabilidade e segurança; sugere que a rápida reconstituição de Tregs pós-ASCT contribui para progressão da doença via supressão imune |
| [12476283](https://pubmed.ncbi.nlm.nih.gov/12476283/) | 2002 | Retrospective Cohort | Bone Marrow Transplantation | Basiliximab foi bem tolerado e eficaz no tratamento de GVHD agudo refratário a corticoides após transplante alogênico em 17 pacientes, incluindo casos de mieloma múltiplo; apoia o perfil de tolerabilidade no contexto hematológico |
| [28320553](https://pubmed.ncbi.nlm.nih.gov/28320553/) | 2017 | Case Report | American Journal of Kidney Diseases | Relato de 4 casos de transplante renal em pacientes com mieloma múltiplo em remissão; relevância indireta ao demonstrar que pacientes com MM controlado podem ser submetidos a procedimentos transplante sob imunossupressão com Basiliximab |

---

## Informações de Comercialização no Brasil

O Basiliximab possui **2 registros ativos** junto à ANVISA com status **comercializado**. Os detalhes individuais de cada registro (número ANVISA, nome comercial, forma farmacêutica e texto de indicação aprovada) não estavam disponíveis nesta versão do Evidence Pack e devem ser consultados diretamente no portal da ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Existe hipótese mecanística biologicamente plausível — depleção de Tregs via bloqueio de CD25 para potencializar o efeito antitumoral pós-ASCT — com suporte direto de um ensaio de Fase 1 concluído em mieloma múltiplo e de um estudo piloto prospectivo publicado em periódico especializado de alto impacto. O nível de evidência L3 justifica investigação clínica avançada, mas é insuficiente para recomendação de uso clínico rotineiro.

**Para prosseguir, é necessário:**
- Obter dados completos de segurança (advertências e contraindicações) a partir da bula registrada na ANVISA
- Confirmar indicações aprovadas e nomes comerciais dos 2 registros brasileiros via portal ANVISA
- Identificar ou iniciar ensaio de Fase 2 randomizado e controlado para deplecção de Tregs com Basiliximab em mieloma múltiplo pós-ASCT
- Avaliar interações medicamentosas com os regimes de condicionamento do ASCT (ex.: melfalan em altas doses)
- Comparar o perfil de risco-benefício frente a alternativas imunoterápicas disponíveis no contexto pós-ASCT (ex.: pembrolizumabe, elotuzumabe, daratumumabe)
- Mapear populações específicas de alto risco (ex.: MM de alto risco citogenético) onde a estratégia imunológica possa oferecer maior benefício diferencial
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

