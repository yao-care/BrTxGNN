---
layout: default
title: Miconazole
parent: 僅模型預測 (L5)
nav_order: 350
evidence_level: L5
indication_count: 10
---

# Miconazole
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

O skill confirma o contexto do projeto. Vou agora gerar o relatório seguindo o formato especificado no prompt do sistema.

---

# Miconazole: Das infecções fúngicas à acne

## Resumo em Uma Frase

Miconazole é um antifúngico imidazólico com mais de 30 anos de uso clínico no tratamento de infecções fúngicas superficiais e cutâneas, incluindo candidíase, dermatomicoses e micoses mucosas.
O modelo TxGNN prevê que pode ser eficaz para **Acne (acne disease)**,
atualmente com **1 ensaio clínico** e **4 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções fúngicas superficiais e cutâneas (candidíase, dermatomicoses, micoses mucosas) |
| Nova Indicação Prevista | Acne (acne disease) |
| Pontuação de Previsão TxGNN | 99,54% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis no Evidence Pack. Segundo informações conhecidas na literatura, miconazole é um antifúngico imidazólico que se distingue dos demais azóis por possuir **dois mecanismos de ação simultâneos**: (1) inibição da enzima CYP51 (lanosterol 14α-desmetilase), bloqueando a síntese de ergosterol e comprometendo a integridade da membrana celular fúngica — mecanismo compartilhado com outros azóis; e (2) inibição de peroxidases, levando ao acúmulo intracelular de peróxidos tóxicos que resultam em morte celular. Essa dupla ação confere ao miconazole um perfil antimicrobiano mais amplo, que inclui atividade contra bactérias Gram-positivas.

A hipótese de reposicionamento para a acne vulgaris fundamenta-se nessa atividade antibacteriana ampliada. *Propionibacterium acnes* (atualmente *Cutibacterium acnes*) é o principal agente bacteriano envolvido na inflamação folicular da acne, e estudos *in vitro* demonstraram que imidazóis possuem atividade inibitória contra essa bactéria. Paralelamente, leveduras do gênero *Malassezia* colonizam o folículo piloso e estão associadas ao agravamento de formas específicas de acne — criando um segundo eixo de plausibilidade biológica, já que o miconazole é reconhecidamente ativo contra este fungo.

É importante destacar, porém, que a acne vulgaris clássica difere fisiopatologicamente da foliculite por *Malassezia* (frequentemente confundida com acne), e que os mecanismos predominantes da acne — hipersecreção sebácea, hiperqueratinização e resposta inflamatória — não são diretamente modulados pela inibição de CYP51. A previsão do modelo TxGNN é biologicamente plausível, mas representa uma **hipótese de pesquisa** que exige validação clínica direta com miconazole como agente isolado.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspenso | 80 | Estudo comparativo da combinação beclometasona 0,025% + gentamicina 0,1% + clotrimazol 1% em pacientes com dermatose infectada com lesões bilaterais simétricas. O agente principal é clotrimazol (não miconazole), e o desenho em combinação não permite isolar a contribuição de cada componente. A suspensão impede conclusões definitivas. |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Estudo clínico (split-face) | Skin Res Technol | Avaliação bioinstrumental da acne catamenial (hormonal) em mulheres jovens, explorando abordagens de tratamento adjuvante; relevante para contextualizar subtipos de acne que podem ter componente microbiológico. |
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Review | Expert Opin Pharmacother | Revisão narrativa sobre os efeitos multifacetados do nitrato de miconazole em dermatoses, destacando propriedades além do espectro antifúngico clássico — incluindo atividade antibacteriana e modulação do microbioma cutâneo. |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Ensaio terapêutico clínico | Clin Exp Dermatol | 62 pacientes com foliculite por *Pityrosporum* frequentemente diagnosticados erroneamente como acne vulgaris; responderam ao tratamento antifúngico. Sublinha a importância clínica de distinguir as condições e o papel de *Malassezia* em lesões acneiformes. |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In vitro | Biol Pharm Bull | Imidazóis azólicos demonstraram atividade inibitória *in vitro* contra *P. acnes*, o principal agente bacteriano da acne vulgaris; resultado relevante no contexto crescente de resistência aos antibióticos convencionais (tetraciclinas, macrolídeos). |

---

## Informações de Comercialização no Brasil

Miconazole **não possui registro ativo na ANVISA**. Não há licenças vigentes para este fármaco no Brasil (total: 0 registros). Não é possível listar produtos comerciais ou indicações aprovadas.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
As evidências disponíveis para o uso de miconazole na acne vulgaris resumem-se a um ensaio clínico suspenso com outro fármaco da mesma classe (clotrimazol) e quatro publicações que estabelecem plausibilidade mecanicista, mas não comprovam eficácia clínica direta do miconazole isolado na acne. O nível de evidência L3 reflete estudos observacionais e revisões, insuficientes para sustentar uma decisão de avanço. Soma-se a isso a ausência completa de registro da substância no Brasil, o que representa barreira regulatória significativa.

**Para prosseguir, é necessário:**
- Ensaio clínico randomizado e controlado testando miconazole tópico versus placebo em pacientes com acne vulgaris confirmada
- Protocolo que distinga claramente acne vulgaris de foliculite por *Malassezia* na seleção de participantes
- Dados de MOA detalhados confirmando atividade antibacteriana clinicamente relevante contra *C. acnes* em concentrações topicamente atingíveis
- Avaliação de tolerabilidade e perfil de segurança do miconazole em pele acneica (potencial de irritação, resistência cruzada)
- Análise do caminho regulatório junto à ANVISA para eventual submissão de nova indicação, caso estudos clínicos confirmem eficácia
---

