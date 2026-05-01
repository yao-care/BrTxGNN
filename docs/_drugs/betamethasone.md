---
layout: default
title: Betamethasone
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 10
---

# Betamethasone
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

# Betamethasone: Das Condições Inflamatórias à Alopecia Areata

## Resumo em Uma Frase

Betamethasone é um glicocorticoide sintético de alta potência, amplamente utilizado no manejo de condições inflamatórias, alérgicas e autoimunes diversas.
O modelo TxGNN prevê que pode ser eficaz especificamente para **Alopecia Areata (alopecia areata)**,
atualmente com **7 ensaios clínicos** e **20 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não disponível no sistema (sem registro ANVISA) |
| Nova Indicação Prevista | Alopecia Areata |
| Pontuação de Previsão TxGNN | 99,97% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros ANVISA | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Betamethasone é um glicocorticoide sintético que atua predominantemente através do receptor de glicocorticoide (GR). Ao se ligar ao GR, suprime a transcrição de citocinas pró-inflamatórias (como IL-1, IL-6 e TNF-α), inibe a ativação da via JAK-STAT — central no processo inflamatório mediado por IFN-γ — e reduz a proliferação e migração de linfócitos T ativados. Embora os detalhes completos do mecanismo de ação não estejam disponíveis no sistema, o perfil farmacológico classe é bem estabelecido na literatura científica.

A alopecia areata é uma doença autoimune em que linfócitos T CD8+ invadem o bulbo piloso e destroem o "privilégio imunológico" do folículo capilar — mecanismo diretamente endereçável pela ação do betamethasone. O fármaco suprime a infiltração perifolicular de células T CD8+ (principal executor do ataque autoimune impulsionado por IFN-γ), reduz a ativação da via JAK-STAT e pode restaurar o microambiente imunossupressor necessário para a sobrevivência do folículo capilar. Dessa forma, existe uma correspondência mecanística direta entre o perfil farmacodinâmico do betamethasone e a fisiopatologia central da alopecia areata.

Diferentes rotas de administração são suportadas pelas evidências clínicas: o esquema **oral mini-pulse semanal** (3 mg/semana) representa uma alternativa ao uso sistêmico contínuo com menor risco de supressão do eixo HPA; formulações **tópicas** (betamethasone valerato 0,1%) são utilizadas como primeira linha para formas localizadas; e a via **intralesional** demonstra resultados promissores. A convergência entre mecanismo de ação, fisiopatologia e corpus de evidências clínicas sustenta fortemente esta previsão do TxGNN.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT06786689](https://clinicaltrials.gov/study/NCT06786689) | Phase 2 | Concluído | 60 | Comparação direta de betamethasone oral mini-pulse (BOMP) versus azatioprina semanal em AA moderada a grave; ensaio mais relevante para a indicação avaliada |
| [NCT05803070](https://clinicaltrials.gov/study/NCT05803070) | N/A | Desconhecido | 59 | Avaliação de eficácia e segurança de cetirizina tópica 1% versus betamethasone valerato tópico 0,1% no tratamento de AA localizada |
| [NCT03535233](https://clinicaltrials.gov/study/NCT03535233) | Phase 4 | Concluído | 40 | Ensaio randomizado controlado comparando minoxidil 5% tópico + corticosteroide potente versus triancinolona intralesional em AA |
| [NCT02350023](https://clinicaltrials.gov/study/NCT02350023) | Phase 4 | Concluído | 50 | Estudo comparativo de betamethasone tópico versus latanoprost tópico em AA localizada; betamethasone como braço ativo de referência |
| [NCT06087796](https://clinicaltrials.gov/study/NCT06087796) | Phase 1 | Desconhecido | 60 | Pentoxifilina 2% gel e metformina 10% gel tópicos versus betamethasone valerato 0,1% creme em AA em placas; betamethasone como controle padrão |
| [NCT04207931](https://clinicaltrials.gov/study/NCT04207931) | Phase 4 | Em recrutamento | 250 | Estudo multicêntrico prospectivo de resultados em CCCA com diferentes grupos de tratamento; betamethasone como opção terapêutica (relevância indireta) |
| [NCT01111981](https://clinicaltrials.gov/study/NCT01111981) | Phase 4 | Desconhecido | 30 | Segurança e eficácia de clobetasol propionato 0,05% em CCCA; evidência de classe para corticosteroide de alta potência (relevância indireta) |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Network Meta-Analysis | Cochrane Database Syst Rev | Meta-análise em rede abrangente sobre tratamentos para AA; avalia imunossupressores, estimulantes do crescimento capilar e imunoterapia de contato |
| [40519428](https://pubmed.ncbi.nlm.nih.gov/40519428/) | 2025 | RCT/Clinical Trial | Cureus | Avaliação prospectiva de eficácia, segurança e perfil de resposta do betamethasone oral mini-pulse em AA moderada a grave |
| [34400956](https://pubmed.ncbi.nlm.nih.gov/34400956/) | 2021 | RCT | Iranian J Pharm Res | Ensaio randomizado duplo-cego placebo-controlado comparando betamethasone oral pulse (3 mg/semana), metotrexato (15 mg/semana) e combinação em AA grave (n=36) |
| [40510104](https://pubmed.ncbi.nlm.nih.gov/40510104/) | 2025 | RCT | Cureus | Ensaio randomizado paralelo não-cegado (n=60) comparando ciclosporina oral 3 mg/kg/dia versus betamethasone mini-pulse em AA |
| [39393548](https://pubmed.ncbi.nlm.nih.gov/39393548/) | 2025 | RCT | J Am Acad Dermatol | Betamethasone composto via microneedle transdérmico em AA: alternativa menos dolorosa à injeção intralesional convencional |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Systematic Review | Dermatol Pract Concept | Revisão sistemática sobre eficácia, taxas de recidiva, efeitos adversos e fatores prognósticos do corticosteroide pulse therapy em AA |
| [38623137](https://pubmed.ncbi.nlm.nih.gov/38623137/) | 2024 | Comparative Study | Cureus | Comparação direta de betamethasone dipropionato tópico versus minoxidil tópico em pacientes com AA |
| [36257912](https://pubmed.ncbi.nlm.nih.gov/36257912/) | 2022 | Comparative Study | Dermatol Ther | Ensaio randomizado cegado com múltiplos grupos (n=108) avaliando latanoprost vs minoxidil, betamethasone e combinações em AA |
| [36114868](https://pubmed.ncbi.nlm.nih.gov/36114868/) | 2023 | RCT | Arch Dermatol Res | Laser CO₂ fracionado isolado versus combinado com betamethasone valerato creme no tratamento de AA (n=30) |
| [32594786](https://pubmed.ncbi.nlm.nih.gov/32594786/) | 2022 | RCT | J Dermatol Treat | Betamethasone intralesional versus triancinolona acetonida em AA localizada: ensaio randomizado controlado intra-paciente |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Múltiplos ensaios clínicos (incluindo um Phase 2 concluído com comparador ativo e uma meta-análise Cochrane) sustentam o uso de betamethasone — em formulações oral mini-pulse, tópica e intralesional — no tratamento da alopecia areata, com correspondência mecanística direta entre a ação imunossupressora do fármaco e a fisiopatologia autoimune perifolicular da doença.

**Para prosseguir, é necessário:**
- Obtenção de dados completos de mecanismo de ação via DrugBank API (item DG002 em aberto)
- Consulta e análise da bula de referência para levantamento de advertências, contraindicações e interações medicamentosas relevantes (item DG001 bloqueante)
- Definição da via de administração preferencial (tópica, intralesional ou oral mini-pulse) conforme gravidade e extensão da AA no perfil de pacientes-alvo
- Avaliação do perfil de segurança específico para uso prolongado: risco de supressão do eixo HPA, efeitos cutâneos locais com uso tópico prolongado e impacto em populações especiais (pediátrica, gestantes)
- Verificação de viabilidade regulatória no Brasil: possibilidade de registro ANVISA ou uso via importação excepcional, dado que o fármaco não consta na base regulatória brasileira consultada

---

> **Aviso**: Este relatório é gerado pelo sistema TxGNN para fins de pesquisa e não constitui recomendação médica. Todos os candidatos a reposicionamento requerem validação clínica antes de qualquer aplicação terapêutica.
---

