---
layout: default
title: Acyclovir
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
---

# Acyclovir
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

# Acyclovir: Das Infecções Herpéticas à Ceratoconjuntivite Epitelial Punctata

## Resumo em Uma Frase

Acyclovir é um antiviral nucleosídeo amplamente utilizado no tratamento de infecções por herpes simplex (HSV-1 e HSV-2) e varicella-zoster (VZV), incluindo ceratite herpética, herpes genital e herpes-zóster.
O modelo TxGNN prevê que pode ser eficaz para **Ceratoconjuntivite Epitelial Punctata (Punctate Epithelial Keratoconjunctivitis)**,
atualmente com **0 ensaios clínicos** e **2 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções por HSV e VZV (herpes labial, herpes genital, herpes-zóster, ceratite herpética) |
| Nova Indicação Prevista | Ceratoconjuntivite Epitelial Punctata (Punctate Epithelial Keratoconjunctivitis) |
| Pontuação de Previsão TxGNN | 99,67% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | Não registrado (dados regulatórios não disponíveis) |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Acyclovir é um análogo nucleosídeo acíclico da guanosina com atividade antiviral seletiva contra membros da família Herpesviridae. Após fosforilação inicial pela timidina quinase (TK) codificada pelo vírus — enzima presente em HSV e VZV, mas ausente em adenovírus, HPV e outros vírus — o fármaco inibe competitivamente a DNA polimerase viral, bloqueando a replicação do DNA. Este mecanismo de ativação TK-dependente confere alta especificidade ao fármaco.

A ceratoconjuntivite epitelial punctata (PEK, punctate epithelial keratitis) é uma alteração inespecífica da superfície corneana caracterizada por múltiplos focos de erosão epitelial. No contexto de infecção por HSV, a PEK surge frequentemente como manifestação precoce ou sinal de progressão da ceratite herpética — indicação na qual o Acyclovir possui eficácia globalmente reconhecida. Esta sobreposição clínica e fisiopatológica entre infecção herpética e PEK fornece a base mecanística indireta para a previsão do TxGNN.

É fundamental, contudo, considerar que PEK não é patognomônica de infecção por HSV: pode ser causada por adenovírus (sem atividade do Acyclovir), microsporidia (parasita intracelular, para o qual o Acyclovir é ineficaz), toxicidade medicamentosa ou síndrome do olho seco. Nenhum dos 2 artigos identificados testa o Acyclovir diretamente para PEK como entidade nosológica primária, e a previsão do modelo pode refletir co-ocorrência epidemiológica no grafo de conhecimento, e não uma relação terapêutica causal estabelecida.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/) | 1995 | Retrospective Case Series | American Journal of Ophthalmology | Dois pacientes com AIDS desenvolveram lipidose corneana com alterações de superfície ocular sugestivas de toxicidade por fármacos utilizados em infecções oportunistas; o Acyclovir não foi testado diretamente para PEK |
| [21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/) | 2011 | Case Series | Indian Journal of Pathology & Microbiology | Série de casos de ceratoconjuntivite por microsporidia em coorte do leste indiano; etiologia parasitária sem relação com terapia antiviral nucleosídea |

---

## Informações de Comercialização no Brasil

Nenhum registro ativo foi identificado na base de dados regulatória brasileira até a data de corte deste relatório (04/04/2026). Recomenda-se consulta direta à ANVISA para confirmação, pois a ausência de registros pode refletir uma limitação na coleta de dados deste Evidence Pack.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A pontuação TxGNN de 99,67% provavelmente reflete co-ocorrência epidemiológica entre infecções herpéticas e PEK no grafo de conhecimento, e não evidência clínica direta de eficácia do Acyclovir nesta indicação específica. Não há ensaios clínicos registrados, e os 2 artigos identificados não testam diretamente o fármaco para ceratoconjuntivite epitelial punctata como entidade diagnóstica independente — um dos artigos descreve uma etiologia (microsporidia) para a qual o Acyclovir é farmacologicamente ineficaz.

**Para prosseguir, é necessário:**
- Confirmar registros do Acyclovir na ANVISA via consulta direta ao portal regulatório brasileiro
- Obter dados formais do mecanismo de ação (MOA) via DrugBank para análise de compatibilidade mecanística
- Delimitar a subpopulação elegível: PEK de etiologia herpética confirmada (HSV/VZV) representa uma extensão de indicação já estabelecida, não um reposicionamento genuíno
- Conduzir revisão bibliográfica aprofundada sobre Acyclovir em uveíte viral e ceratite herpética com componente epitelial punctata
- Priorizar avaliação das indicações deste mesmo Evidence Pack com melhor suporte clínico disponível:
  - **Verruga Comum (Common Wart)** — Rank 2, Nível L2, 6 ensaios clínicos incluindo Phase 2/3 RCT (NCT06261684, 92 pacientes) e múltiplos RCTs de 2025, recomendação **Proceed with Guardrails**
  - **Doença da Região Orbital (Disease of Orbital Region)** — Rank 9, Nível L3, com ensaio direto de Acyclovir oral em uveíte viral (NCT03389191) e histórico clínico em ceratite herpética, recomendação **Proceed with Guardrails**
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

