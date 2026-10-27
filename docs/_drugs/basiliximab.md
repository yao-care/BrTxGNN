---
layout: default
title: Basiliximab
parent: Apenas Predição do Modelo (L5)
nav_order: 107
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Basiliximab: nova indicação prevista, Mieloma de Plasmócitos (Plasma Cell Myeloma) (nível de evidência L5). Indicação original: Não disponível nos registros da ANVISA compilados"
monitor_inn: "Basiliximab"
predicted_indications: ["plasma cell myeloma", "bronchitis", "indolent plasma cell myeloma", "hemoglobinopathy", "gastric carcinoma", "diffuse gastric adenocarcinoma", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "hemolytic anemia due to glucophosphate isomerase deficiency", "Jeune syndrome situs inversus"]
---

# Basiliximab
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relatório de avaliação farmacêutica

</div>

## Basiliximabe: Da imunossupressão em transplantes ao mieloma múltiplo (plasmocitoma)
{: .text-alpha }

## Resumo em Uma Frase

O basiliximabe é um anticorpo monoclonal que bloqueia o receptor de interleucina-2 (anti-CD25). Segundo os dados compilados, não há indicação original registrada no Brasil, mas o fármaco é conhecido pelo uso em imunossupressão de transplantes.
O modelo TxGNN prevê que pode ser útil para **Mieloma de Plasmócitos (Plasma Cell Myeloma)**, atualmente com **3 ensaios clínicos** e **4 publicações** relacionados. O benefício observado é de apoio (prevenção da doença do enxerto contra o hospedeiro, DECH), e não de ação antimieloma direta.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível nos registros da ANVISA compilados |
| Nova Indicação Prevista | Mieloma de Plasmócitos (Plasma Cell Myeloma) |
| Pontuação de Previsão TxGNN | 95,61% |
| Nível de Evidência | L2 (segundo a classificação dos dados compilados; ver ressalva abaixo) |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

*Ressalva sobre o nível de evidência:* o único estudo de Fase 2 é pequeno (17 participantes) e sem desenho comparativo confirmado. Pelas regras estritas (1 RCT de Fase 2/3 concluído), a evidência seria mais próxima de L3–L4. Por isso, a decisão é conservadora.

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos registros compilados. Segundo informações conhecidas, o basiliximabe é um anticorpo monoclonal quimérico anti-CD25 (cadeia alfa do receptor de IL-2). Ele bloqueia a ativação e a proliferação de linfócitos T ativados e atua sobre células T reguladoras (Tregs).

A relação com o mieloma não é antitumoral direta. No mieloma, o fármaco foi estudado em dois contextos: (1) depleção in vivo de células T ativadas para prevenir a DECH após transplante alogênico não mieloablativo; e (2) redução de Tregs ao redor do transplante autólogo de células-tronco, na tentativa de melhorar a resposta imune contra o mieloma, já que as Tregs se reconstituem rapidamente após o transplante e inibem essa resposta.

Portanto, a previsão é plausível como **terapia de suporte e imunomodulação** em pacientes com mieloma submetidos a transplante, mas não como tratamento direto da doença.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00975975](https://clinicaltrials.gov/study/NCT00975975) | Phase 2 | Concluído | 17 | Basiliximabe + ciclosporina para prevenir DECH após transplante alogênico não mieloablativo em câncer do sangue; estudo pequeno |
| [NCT00594308](https://clinicaltrials.gov/study/NCT00594308) | NA | Encerrado | 10 | Compara basiliximabe + ciclosporina com ciclosporina isolada na prevenção de DECH; encerrado precocemente, valor limitado |
| [NCT01526096](https://clinicaltrials.gov/study/NCT01526096) | Phase 1 | Concluído | 30 | Piloto de depleção de Tregs em pacientes com mieloma submetidos a transplante autólogo; avalia viabilidade e segurança |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [31940591](https://pubmed.ncbi.nlm.nih.gov/31940591/) | 2020 | Ensaio de Fase 1 | Journal for Immunotherapy of Cancer | Estudo piloto de depleção de Tregs em transplante autólogo no mieloma, motivado pela disfunção imune após melfalano em altas doses |
| [12476283](https://pubmed.ncbi.nlm.nih.gov/12476283/) | 2002 | Coorte | Bone Marrow Transplantation | Basiliximabe foi bem tolerado e eficaz em 17 pacientes com DECH aguda refratária a esteroides após transplante alogênico (incluindo mieloma múltiplo) |
| [42379467](https://pubmed.ncbi.nlm.nih.gov/42379467/) | 2026 | Revisão/Série de casos | American Journal of Kidney Diseases | Transplante renal após terapia CAR-T no mieloma múltiplo, com novas oportunidades em pacientes selecionados |
| [28320553](https://pubmed.ncbi.nlm.nih.gov/28320553/) | 2017 | Relato de casos | American Journal of Kidney Diseases | Quatro pacientes com mieloma submetidos a transplante renal após resposta ao tratamento |

---

## Considerações de Segurança

- **Interações Medicamentosas:** foram identificadas 69 interações, das quais as de maior gravidade (nível Maior) incluem:
  - Adalimumabe
  - Baricitinibe
  - Certolizumabe pegol
  - Vacina BCG (cepa Tice, vivo)

  Há ainda interações de nível Moderado com outros imunossupressores e biológicos (por exemplo, alentuzumabe, anacinra, azatioprina, canaquinumabe e roflumilaste) e com diversas vacinas. As interações com sais de zinco são de nível Menor. De modo geral, o uso concomitante com outros imunossupressores aumenta o risco de infecção, e vacinas vivas devem ser evitadas.

Para advertências e contraindicações, consulte a bula.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Os ensaios existentes são pequenos (10 a 30 participantes), de Fase 1/2 ou encerrados precocemente, e avaliam o uso de suporte (prevenção de DECH e modulação de Tregs), não a eficácia antimieloma. O fármaco não está comercializado no Brasil e não há dados de bula para avaliar a segurança.

**Para prosseguir, é necessário:**
- Obter a bula e os dados de advertências e contraindicações na ANVISA (lacuna bloqueante para a triagem de segurança)
- Obter dados detalhados do mecanismo de ação (por exemplo, via DrugBank)
- Definir a indicação original e a situação regulatória do fármaco no Brasil
- Ensaios randomizados maiores que mostrem benefício clínico em pacientes com mieloma (DECH, recaída, sobrevida)
- Avaliar o risco de infecção e a segurança da imunossupressão em populações com mieloma

**Observação sobre outras indicações previstas:** as demais previsões têm evidência fraca ou inexistente. Hemoglobinopatia (talassemia maior) tem suporte indireto, com um estudo de Fase 4 de 205 participantes sobre prevenção de DECH em transplante, mas o benefício é sobre a complicação do transplante, não sobre a doença de base. As previsões para bronquite e carcinoma gástrico não têm base mecanística plausível, e a imunossupressão poderia ser inadequada ou até prejudicial nesses casos.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

