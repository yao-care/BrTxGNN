---
layout: default
title: Prednisolone Acetate
parent: 僅模型預測 (L5)
nav_order: 413
evidence_level: L5
indication_count: 10
---

# Prednisolone Acetate
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

Using `txgnn-pipeline` to understand project conventions — confirmed this is a multi-indication evidence pack for BrTxGNN. Now generating the report from the provided Evidence Pack.

---

# Prednisolone Acetate: Da Inflamação Ocular à Conjuntivite Parasitária

## Resumo em Uma Frase

Prednisolone acetate é um corticosteroide tópico oftálmico amplamente reconhecido no tratamento de inflamações oculares de diversas etiologias, sem registro regulatório ativo no banco de dados consultado.
O modelo TxGNN prevê que pode ser eficaz para **Conjuntivite Parasitária (Parasitic Conjunctivitis)**,
atualmente com **0 ensaios clínicos** e **1 publicação** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Sem registro ativo no banco de dados regulatório consultado |
| Nova Indicação Prevista | Conjuntivite Parasitária (Parasitic Conjunctivitis) |
| Pontuação de Previsão TxGNN | 99.74% |
| Nível de Evidência | L4 |
| Situação no Mercado | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no banco de dados consultado. Conforme informações amplamente estabelecidas na literatura médica, prednisolone acetate é um glicocorticoide sintético que age por ligação ao receptor nuclear de glicocorticoide (GR), suprimindo a transcrição de citocinas pró-inflamatórias (IL-1β, IL-6, TNF-α), inibindo a fosfolipase A2 e bloqueando a via NF-κB. Em formulação tópica oftálmica (suspensão 1%), atua localmente na conjuntiva e no segmento anterior com absorção sistêmica mínima, sendo esta a base do seu perfil de segurança favorável em uso ocular.

A conjuntivite parasitária — como a causada por *Dirofilaria repens*, nematódeo zoonótico em expansão geográfica — desencadeia uma resposta inflamatória local intensa mediada por eosinófilos, linfócitos e mastócitos, com edema periorbitário, hiperemia e desconforto ocular significativos. Nesse contexto, o corticosteroide tópico pode atuar como agente adjuvante para controlar a reação inflamatória do hospedeiro após remoção cirúrgica do parasita, sendo o mecanismo anti-inflamatório biologicamente plausível.

É essencial destacar, porém, que o tratamento definitivo da conjuntivite parasitária é a extração mecânica ou cirúrgica do parasita, associada à terapia antiparasitária sistêmica. O uso de corticosteroides nessa condição é considerado auxiliar e deve ser feito com cautela: a imunossupressão local pode mascarar sinais de infecção ativa ou facilitar a progressão parasitária antes do tratamento definitivo. Esta previsão reflete, portanto, um potencial de uso adjuvante mecanisticamente plausível, e não uma indicação primária estabelecida.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [26846596](https://pubmed.ncbi.nlm.nih.gov/26846596/) | 2016 | Case Report/Review | *Eye (London, England)* | Relato de zoonose ocular emergente por *Dirofilaria repens*, descrevendo manifestações clínicas de conjuntivite parasitária e abordagem de manejo; contextualiza o papel adjuvante dos corticosteroides no controle da resposta inflamatória local |

---

## Informações de Comercialização

Prednisolone acetate não possui registros ativos no banco de dados regulatório consultado. Nenhum produto com este princípio ativo foi encontrado.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> **Nota clínica relevante:** Embora os dados formais de segurança não estejam disponíveis neste Evidence Pack, corticosteroides tópicos oftálmicos como classe apresentam riscos conhecidos de aumento da pressão intraocular (glaucoma corticosteroide-induzido), formação de catarata subcapsular posterior e susceptibilidade aumentada a infecções oculares com uso prolongado. Em conjuntivite parasitária especificamente, o uso deve ser restrito ao período pós-remoção do parasita, dado o risco de agravamento da infecção ativa por imunossupressão.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A evidência para prednisolone acetate em conjuntivite parasitária restringe-se a um único relato de caso/revisão (nível L4), sem ensaios clínicos registrados, e as preocupações de segurança específicas para uso em infecções ativas impõem cautela adicional que não sustenta progressão clínica imediata para esta indicação.

**Para prosseguir, é necessário:**
- Obter dados completos de MOA junto ao DrugBank (DG002) e advertências/contraindicações da bula regulatória (DG001)
- Verificar histórico de registros internacionais (FDA, EMA) para compreender o espectro de indicações já aprovadas para prednisolone acetate oftálmico
- Conduzir revisão sistemática de literatura sobre uso de corticosteroides tópicos em conjuntivite por *Dirofilaria* e demais parasitas oculares
- **Priorizar avaliação das indicações com maior suporte de evidência neste perfil do fármaco:**
  - **Conjuntivite Vernal** (rank 9, L3 — Proceed with Guardrails): 1 ensaio clínico + 19 publicações, incluindo comparativo com prednisolone acetate 1% (PMID 24055903) e estudos de coorte prospectivos
  - **Conjuntivite Papilar** (rank 5, L3 — Proceed with Guardrails): 2 ensaios clínicos + 6 publicações, com evidência de classe via loteprednol etabonate (NCT01437982, Phase 4 concluído)
- Investigar razão da ausência de registro regulatório, dado que prednisolone acetate oftálmico é amplamente aprovado em outros mercados
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

