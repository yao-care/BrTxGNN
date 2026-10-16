---
layout: default
title: Salbutamol
parent: Apenas Predição do Modelo (L5)
nav_order: 577
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Salbutamol: nova indicação prevista, Conjuntivite Papilar (Papillary Conjunctivitis) (nível de evidência L5). Indicação original: Asma"
monitor_inn: "Salbutamol"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "pharyngitis", "bronchitis", "acute laryngopharyngitis", "anaphylaxis", "common cold", "atopic conjunctivitis", "anorectal stricture", "obstructive lung disease"]
---

# Salbutamol
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relatório de avaliação farmacêutica

</div>

# Salbutamol: Da asma à conjuntivite papilar

## Resumo em Uma Frase

Salbutamol é um agonista beta-2 adrenérgico, originalmente usado no tratamento da asma e de doenças brônquicas.
O modelo TxGNN prevê que pode ser eficaz para **Conjuntivite Papilar (Papillary Conjunctivitis)**, mas, para essa indicação, **não há nenhum ensaio clínico nem publicação** que sustente a previsão: trata-se apenas de uma previsão do modelo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Asma; doença brônquica (conforme o grafo de conhecimento do TxGNN, pois não há registros no Brasil) |
| Nova Indicação Prevista | Conjuntivite Papilar (Papillary Conjunctivitis) |
| Pontuação de Previsão TxGNN | 99,996% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

> **Observação:** a indicação de maior prioridade segundo o modelo é a conjuntivite papilar, mas dentre as dez indicações previstas, a que tem evidências mais robustas é a **doença pulmonar obstrutiva** (nível L1), que se sobrepõe ao uso original do fármaco. Ambas são detalhadas abaixo.

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, o salbutamol é um agonista beta-2 adrenérgico de curta ação, que relaxa a musculatura lisa das vias aéreas. Sua eficácia na asma está bem estabelecida.

Para a conjuntivite papilar, a ligação é apenas especulativa: a ativação de receptores beta-2 poderia reduzir a liberação de mediadores por mastócitos e a vasodilatação ocular. Não há dados clínicos que sustentem essa hipótese nos dados compilados. Em outra indicação prevista, a conjuntivite atópica, existem estudos pré-clínicos em cobaias (salbutamol tópico suprimiu a conjuntivite alérgica imediata) e sobre a atividade anti-inflamatória conjuntival de agonistas beta-2, o que torna a ideia biologicamente plausível, mas ainda sem estudos em humanos.

Portanto, a previsão do TxGNN para conjuntivite papilar deve ser tratada como uma hipótese a investigar, e não como evidência de eficácia.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para conjuntivite papilar.

Para contexto, outras indicações previstas têm ensaios registrados, como:

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02177253](https://clinicaltrials.gov/study/NCT02177253) | Phase 3 | Concluído | 1118 | Combinação ipratrópio/salbutamol (Respimat) vs. Combivent em DPOC, por 12 semanas (obstrução pulmonar) |
| [NCT05653024](https://clinicaltrials.gov/study/NCT05653024) | Phase 3 | Encerrado | 24 | Salbutamol inalado vs. placebo para dor abdominal em reações alérgicas alimentares (anafilaxia); encerrado precocemente, sem poder estatístico |
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | N/A | Desconhecido | 600 | Epinefrina vs. albuterol (salbutamol) em bronquiolite |
| [NCT00696540](https://clinicaltrials.gov/study/NCT00696540) | Phase 2 | Desconhecido | 74 | Salbutamol diluído em solução salina hipertônica vs. normal em bronquiolite |
| [NCT06665711](https://clinicaltrials.gov/study/NCT06665711) | N/A | Ainda não recrutando | 100 | Salina hipertônica 3% vs. salbutamol em crianças com bronquiolite |
| [NCT00677729](https://clinicaltrials.gov/study/NCT00677729) | Phase 2 | Concluído | 81 | Salina hipertônica inalada em bronquiolite infantil (salbutamol provavelmente como co-intervenção) |

---

## Evidências da Literatura

Atualmente não há literatura relacionada a conjuntivite papilar.

Para contexto, literatura de outras indicações previstas:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [24937099](https://pubmed.ncbi.nlm.nih.gov/24937099/) | 2014 | Revisão sistemática (Cochrane) | Cochrane Database Syst Rev | Broncodilatadores em bronquiolite: benefício clínico pouco expressivo |
| [33893229](https://pubmed.ncbi.nlm.nih.gov/33893229/) | 2021 | Metanálise em rede | Pediatrics | Eficácia comparativa de intervenções em bronquiolite aguda |
| [26859020](https://pubmed.ncbi.nlm.nih.gov/26859020/) | 2014 | RCT | East Afr Med J | Mel, salbutamol e placebo para tosse em crianças com resfriado comum |
| [35383741](https://pubmed.ncbi.nlm.nih.gov/35383741/) | 2022 | RCT | Mymensingh Med J | Salina hipertônica 3% vs. salina normal e salbutamol em bronquiolite aguda |
| [34366098](https://pubmed.ncbi.nlm.nih.gov/34366098/) | 2021 | Relato/Revisão | J Allergy Clin Immunol Pract | Uso de salbutamol na anafilaxia gastrointestinal |
| [3666475](https://pubmed.ncbi.nlm.nih.gov/3666475/) | 1987 | Pré-clínico (cobaia) | Graefes Arch Clin Exp Ophthalmol | Salbutamol tópico suprimiu a conjuntivite alérgica imediata (inibição de 98% com 0,1%) |
| [2906082](https://pubmed.ncbi.nlm.nih.gov/2906082/) | 1985 | Pré-clínico | J Ocul Pharmacol | Atividade anti-inflamatória tópica de agonistas beta-2 na conjuntiva |
| [1729064](https://pubmed.ncbi.nlm.nih.gov/1729064/) | 1992 | RCT cruzado | Chest | Teofilina e salbutamol melhoram a função pulmonar em DPOC irreversível |

---

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento** (não correspondem ao texto da bula): hipertensão, síndrome do QT longo, epilepsia, deficiência de potássio, diabetes mellitus e cetoacidose diabética, hiperplasia prostática benigna, hipertensão ocular, glaucoma de ângulo fechado, acidose metabólica, parada cardíaca súbita, doença do sistema de condução cardíaca, hipertireoidismo/doença de Graves/tireotoxicose, obstrução do colo vesical, isquemia miocárdica e doença arterial coronariana.
- **Interações medicamentosas** (100 interações identificadas; principais exemplos):
  - Moderadas: acarbose, isometepteno, famotidina, epinefrina, albiglutida, acetoexamida, alogliptina, bisacodil, canagliflozina, óleo de rícino, clorpropamida, cisaprida, claritromicina, dapagliflozina, dietilpropiona.
  - Leves: hidrocortisona, beclometasona, betametasona, budesonida, dexametasona.
- **Sinais de segurança na literatura:** relato de anafilaxia ao próprio salbutamol (PMID 18447148) e metanálise sobre uso materno de medicamentos e malformações anorretais (PMID 29747656).

Para advertências e contraindicações oficiais, consulte a bula.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Para a conjuntivite papilar, a previsão do TxGNN é alta (99,996%), mas não há ensaios nem literatura: evidência L5, somente previsão do modelo.
- O produto não está comercializado no Brasil (0 registros), e os dados de bula e de mecanismo de ação estão ausentes.

**Outras indicações previstas (para priorização):**
- **Doença pulmonar obstrutiva (L1, Proceed with Guardrails):** há Phase 3 concluído (NCT02177253, n=1118), mas testa uma combinação e se sobrepõe ao uso original, sendo quase uma indicação já estabelecida, não um reposicionamento genuíno.
- **Anafilaxia, resfriado comum (L3) e bronquite (L2):** classificadas como questões de pesquisa; as evidências são limitadas ou, na bronquiolite, em grande parte negativas.
- **Conjuntivite atópica (L4):** apenas dados pré-clínicos.
- **Faringite, cavidade nasal, laringofaringite aguda e estenose anorretal (L5):** sem mecanismo plausível; provavelmente artefatos do modelo.

**Para prosseguir, é necessário:**
- Obter a bula da ANVISA com advertências e contraindicações (lacuna bloqueante para a triagem de segurança).
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank).
- Esclarecer o status regulatório do salbutamol no Brasil (sem registros ativos) e a via de administração necessária (por exemplo, oftálmica tópica), pois a compatibilidade de via ainda não foi avaliada.
- Realizar estudos pré-clínicos e, se promissores, ensaios exploratórios em conjuntivite alérgica/papilar antes de qualquer avanço.
- Definir se o objetivo é reposicionamento real ou uso já estabelecido (DPOC).
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

