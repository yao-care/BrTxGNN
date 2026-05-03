---
layout: default
title: Aminophylline
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 10
---

# Aminophylline
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

# Aminophylline: Do broncoespasmo à enxaqueca

## Resumo em Uma Frase

Aminophylline é a sal etilenodiamina da teofilina, amplamente utilizada como broncodilatador no tratamento de broncoespasmo, asma brônquica e apneia da prematuridade.
O modelo TxGNN prevê que pode ser eficaz para **Transtorno de Enxaqueca (Migraine Disorder)**,
atualmente com **0 ensaios clínicos** e **6 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Broncoespasmo / Asma brônquica (indicação reconhecida internacionalmente; sem registro no Brasil) |
| Nova Indicação Prevista | Transtorno de Enxaqueca (Migraine Disorder) |
| Pontuação de Previsão TxGNN | 99,88% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Aminophylline atua por dois mecanismos principais: inibição da fosfodiesterase (PDE), que eleva os níveis intracelulares de AMPc, e antagonismo não seletivo dos receptores de adenosina (A1, A2A, A2B e A3). Embora os dados formais de mecanismo de ação (MOA) não estejam disponíveis neste pacote de evidências, o perfil farmacológico geral do fármaco é amplamente documentado na literatura médica.

A base mecanística para o reposicionamento em enxaqueca converge no papel da adenosina como mediador central da crise: a ativação do receptor A2A cerebral promove dilatação seletiva das artérias piais e ativa neurônios nociceptivos trigeminais, resultando na dor característica da enxaqueca. A revisão de Phillips et al. (PMID 38059379, 2023) sintetiza evidências observacionais de que aminophylline, ao bloquear estes receptores, proporciona alívio terapêutico significativo em dores, incluindo a cefaleia pós-dural — uma condição com fisiopatologia sobreponível à enxaqueca.

O caso relatado por Elsadany et al. (PMID 34308528, 2022) oferece uma prova de conceito reversa especialmente convincente: a administração de regadenoson (agonista seletivo A2A utilizado em imagem miocárdica de estresse) desencadeou um episódio de enxaqueca hemiplégica, cujos efeitos foram revertidos com metiilxantinas como aminophylline. Este relato inverso confirma experimentalmente que a sinalização via A2A é capaz de precipitar enxaqueca, e que o seu bloqueio — mecanismo exato de aminophylline — pode ter efeito terapêutico.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [38059379](https://pubmed.ncbi.nlm.nih.gov/38059379/) | 2023 | Review / Clinical Study | Pain Management | Propõe que a enxaqueca é mediada por adenosina em contexto de metabolismo energético cerebral comprometido; aminophylline, como antagonista adenosinérgico, demonstrou forte alívio terapêutico em cefaleia pós-dural e em série observacional de casos de enxaqueca |
| [34308528](https://pubmed.ncbi.nlm.nih.gov/34308528/) | 2022 | Case Report | Journal of Nuclear Cardiology | Regadenoson (agonista A2A) induziu episódio de enxaqueca hemiplégica durante MPI; aminophylline e cafeína foram utilizados para reversão — prova de conceito direta do papel antagonista A2A no tratamento da enxaqueca |
| [7728647](https://pubmed.ncbi.nlm.nih.gov/7728647/) | 1995 | Case Report | Canadian Journal of Cardiology | Síndrome X atribuída a efeito excessivo de adenosina descrita como "enxaqueca miocárdica sem isquemia"; dipiridamol (indutor de adenosina endógena) provocou dor torácica intensa e alterações eletrocardiográficas sem evidência de isquemia focal |
| [219563](https://pubmed.ncbi.nlm.nih.gov/219563/) | 1979 | In Vitro Study | Stroke | Adenosina e compostos adenínicos (AMP, AMPc, ADP, ATP) dilataram seletivamente artérias piais cerebrais felinas e humanas in vitro, sem efeito em artérias extracranianas; autores sugerem envolvimento na fisiopatologia da enxaqueca |

---

## Informações de Comercialização no Brasil

Aminophylline não possui registro ativo na ANVISA e não está comercializado no mercado brasileiro. Não há licenças vigentes na base de dados regulatória consultada.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A hipótese de reposicionamento em enxaqueca apresenta plausibilidade mecanística sólida (antagonismo adenosinérgico via A2A), sustentada por evidências indiretas de nível L4 — revisão clínica observacional e casos documentados. No entanto, a ausência total de ensaios clínicos controlados e o fato de aminophylline não estar registrado no Brasil impedem progressão imediata. Vale destacar que, dentre todas as indicações previstas neste pacote de evidências, **hipertensão pulmonar (rank 7)** apresenta o perfil de evidência mais maduro (L3, 1 ensaio Fase 1 concluído com ambrisentan — NCT01530464), podendo ser considerada candidata prioritária para desenvolvimento paralelo.

**Para prosseguir com enxaqueca, é necessário:**
- Conduzir ensaio clínico Fase 2 com desfecho primário de alívio de crise aguda de enxaqueca
- Obter dados completos de MOA via DrugBank API (DG002)
- Levantar advertências, contraindicações e perfil de interações medicamentosas a partir da bula oficial (DG001)
- Avaliar viabilidade de registro do produto na ANVISA previamente à condução de estudos clínicos no Brasil
- Definir via de administração adequada para o contexto de enxaqueca (oral vs. intravenoso)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

