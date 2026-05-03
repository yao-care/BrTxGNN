---
layout: default
title: Cyclosporine
parent: 僅模型預測 (L5)
nav_order: 205
evidence_level: L5
indication_count: 10
---

# Cyclosporine
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

# Ciclosporina: Da prevenção de rejeição de transplante à doença granulomatosa crônica

## Resumo em Uma Frase

Ciclosporina é um imunossupressor clássico amplamente utilizado na prevenção de rejeição em transplantes de órgãos sólidos e como profilaxia da doença do enxerto contra hospedeiro (GvHD) após transplante de células-tronco hematopoéticas (HSCT).
O modelo TxGNN prevê que pode ser eficaz para a **Doença Granulomatosa Crônica — forma autossômica recessiva (Granulomatous Disease, Chronic, Autosomal Recessive)**,
atualmente com **1 ensaio clínico** e **1 publicação** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Prevenção de rejeição em transplantes de órgãos; profilaxia de GvHD pós-HSCT |
| Nova Indicação Prevista | Doença Granulomatosa Crônica — forma autossômica recessiva (Granulomatous Disease, Chronic, Autosomal Recessive) |
| Pontuação de Previsão TxGNN | 99.68% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

O Evidence Pack não contém dados estruturados de mecanismo de ação para este candidato. Com base nas informações disponíveis no pacote, a ciclosporina atua inibindo a ativação de células T — bloqueando a via da calcineurina e, consequentemente, a produção de IL-2 —, o que sustenta sua ampla aplicação como imunossupressor em contextos de transplante.

A Doença Granulomatosa Crônica (DGC) é causada por defeito genético na enzima NADPH oxidase dos fagócitos, resultando em incapacidade de destruir patógenos intracelulares, inflamação granulomatosa crônica e infecções recorrentes graves. A hipótese de reposicionamento da ciclosporina baseia-se na sua capacidade de modular a resposta inflamatória mediada por células T que contribui para a formação excessiva de granulomas, característica desta doença.

Contudo, há um risco relevante de **confusão de indicação**: as evidências clínicas disponíveis não avaliam a ciclosporina como tratamento direto da DGC, mas sim como componente da profilaxia de GvHD no contexto de HSCT realizado *para tratar* a DGC. Nesse cenário, o benefício clínico observado reflete primariamente o efeito do transplante em si, e não da ciclosporina como agente terapêutico autônomo para a doença.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01917708](https://clinicaltrials.gov/study/NCT01917708) | Phase 1 | Concluído | 10 | Estudo de braço único avaliando a tolerabilidade de abatacept combinado com ciclosporina e mofetila de micofenolato como profilaxia de GvHD em crianças e adolescentes submetidos a HSCT de doador não aparentado para doenças não malignas graves (incluindo DGC). A ciclosporina atuou como componente padrão da combinação imunossupressora, não como agente investigacional primário. |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [22078471](https://pubmed.ncbi.nlm.nih.gov/22078471/) | 2012 | Retrospective Cohort | J Allergy Clin Immunol | HSCT de doador aparentado compatível (MRD) apresenta alta sobrevida na DGC; o estudo também avalia a segurança e eficácia do HSCT de doador não aparentado nessa população. A ciclosporina integrava o regime de imunossupressão, sem avaliação isolada do seu efeito sobre a DGC. |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A ciclosporina está presente em protocolos de HSCT para DGC, mas exclusivamente como profilaxia de GvHD — não existe evidência que a sustente como tratamento primário e independente da doença granulomatosa crônica. O único ensaio clínico identificado avalia o abatacept como intervenção principal, com a ciclosporina em papel secundário (relevância grau B). A evidência é indireta, o risco de confusão de indicação é alto e o fármaco não está registrado no Brasil.

**Para prosseguir, é necessário:**
- Identificar estudos que avaliem ciclosporina como tratamento direto da DGC (inflamação granulomatosa, não como profilaxia pós-HSCT)
- Obter dados completos de mecanismo de ação (MOA) e perfil de segurança via DrugBank API e bula oficial
- Consultar especialistas em imunodeficiências primárias para validação da hipótese mecanística
- Avaliar a viabilidade regulatória de um registro junto à ANVISA caso as evidências sejam fortalecidas
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

