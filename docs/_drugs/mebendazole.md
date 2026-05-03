---
layout: default
title: Mebendazole
parent: 僅模型預測 (L5)
nav_order: 338
evidence_level: L5
indication_count: 10
---

# Mebendazole
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

Com base no Evidence Pack fornecido, o fármaco principal do relatório é Mebendazole, cuja indicação de topo prevista pelo TxGNN é acne — uma previsão com evidência L5. Vou gerar o relatório completo seguindo o formato especificado.

---

# Mebendazole: De helmintíases a acne

## Resumo em Uma Frase

Mebendazole é um anti-helmíntico da classe benzimidazol, utilizado no tratamento de infecções por parasitas intestinais — como oxiúros, áscaris, ancilóstomos e tricocéfalos. O modelo TxGNN prevê que pode ser eficaz para **acne (disease)**, porém atualmente há **0 ensaios clínicos** e apenas **1 publicação** tangencialmente relacionada apoiando esta direção, situando esta previsão no nível de evidência mínimo (L5).

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Anti-helmíntico (infecções por vermes parasitários intestinais) |
| Nova Indicação Prevista | Acne (*Acne vulgaris*) |
| Pontuação de Previsão TxGNN | 99,20% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros ANVISA | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Mebendazole é um benzimidazol cujo mecanismo de ação consiste na inibição seletiva da polimerização da **β-tubulina** em parasitas eucariotos. Ao bloquear a formação do fuso mitótico, impede a divisão celular dos helmintos e, secundariamente, bloqueia a captação de glicose pelos vermes — levando à sua morte por depleção energética. Este mecanismo é altamente seletivo para tubulinas de organismos eucariotos inferiores (nematódeos, cestódeos e alguns protozoários), apresentando afinidade consideravelmente menor pela tubulina humana.

A acne (*Acne vulgaris*) é uma doença inflamatória crônica da unidade pilossebácea, cuja fisiopatologia envolve hiperqueratinização folicular, hiperprodução de sebo, colonização por *Cutibacterium acnes* (bactéria gram-positiva anaeróbia) e resposta inflamatória cutânea mediada por citocinas. Não existe nenhuma conexão mecanística conhecida entre a inibição de β-tubulina de parasitas e qualquer um desses processos — seja a proliferação bacteriana, a produção de sebo pelos sebácitos, ou o recrutamento de neutrófilos e macrófagos ao folículo.

A pontuação elevada do TxGNN (99,20%) provavelmente reflete conexões indiretas no grafo de conhecimento entre nós genéricos de "doenças de pele" e o fármaco, sem representar uma relação farmacológica real. De acordo com a análise de racionalidade mecanística do próprio Evidence Pack, esta previsão é classificada como **ruído de modelo** — não constitui uma oportunidade de reposicionamento clinicamente viável.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [7072899](https://pubmed.ncbi.nlm.nih.gov/7072899/) | 1982 | Case Report | Am J Trop Med Hyg | Primeiro relato de esparganose proliferativa humana no hemisfério sul. O paciente apresentava lesões cutâneas nodulares e papulares **com aparência semelhante à acne** — a menção é puramente descritiva da morfologia, sem qualquer relação com tratamento de acne por Mebendazole. |

> ⚠️ **Nota de relevância:** A única publicação encontrada descreve lesões com *aspecto morfológico* de acne em contexto de infecção parasitária grave. Não testa, não sugere e não apoia o uso de Mebendazole para acne.

---

## Informações de Comercialização no Brasil

Mebendazole **não possui registro na ANVISA**. O medicamento não está comercializado no mercado brasileiro. Não há histórico de licenças ativas ou inativas para esta substância ativa no banco de dados regulatório consultado.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Não existe base mecanística plausível para o uso de Mebendazole em acne, e a única evidência identificada é um relato de caso de 1982 com relevância apenas descritiva de morfologia cutânea. A previsão TxGNN aparenta ser ruído resultante de conexões inespecíficas no grafo de conhecimento entre nós de doenças dermatológicas e o fármaco.

**Para prosseguir, é necessário:**
- Identificar qualquer hipótese mecanística minimamente viável (por exemplo: atividade anti-inflamatória documentada, efeito sobre microbioma cutâneo, ou atividade sobre *C. acnes*) antes de qualquer investigação adicional
- Se o interesse de reposicionamento em Mebendazole persistir, redirecionar a avaliação para as indicações com evidência real identificadas neste Evidence Pack: **echinococcose por *E. granulosus*** (rank 3, L3, 7 publicações) e **echinococcose alveolar** (rank 5, L3, 1 ensaio clínico + 20 publicações) — ambas com recomendação *Proceed with Guardrails* e conexão mecanística estabelecida via inibição de β-tubulina do parasita
- Antes de qualquer avanço regulatório no Brasil, iniciar processo de registro na ANVISA, dado que o fármaco não possui comercialização no país
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

