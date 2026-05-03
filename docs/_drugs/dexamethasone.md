---
layout: default
title: Dexamethasone
parent: 僅模型預測 (L5)
nav_order: 216
evidence_level: L5
indication_count: 10
---

# Dexamethasone
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

---

# Dexamethasona: Da Imunossupressão Sistêmica à Alopecia Areata

## Resumo em Uma Frase

Dexamethasona é um corticosteroide sintético de alta potência, amplamente utilizado no tratamento de condições inflamatórias, autoimunes e como suporte em protocolos oncológicos.
O modelo TxGNN prevê que pode ser eficaz para **Alopecia Areata (Alopecia Areata)**, uma forma autoimune de perda de cabelo,
atualmente com **nenhum ensaio clínico dedicado registrado**, mas com **20 publicações** — incluindo 1 ensaio clínico randomizado, 1 revisão sistemática com meta-análise em rede e múltiplas coortes prospectivas — apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Glicocorticoide sistêmico — imunossupressão, inflamação, suporte oncológico (dados regulatórios não disponíveis no sistema) |
| Nova Indicação Prevista | Alopecia Areata (Alopecia Areata) |
| Pontuação de Previsão TxGNN | 99,99% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | Não registrado (sem dados no sistema ANVISA) |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

A dexamethasona é um glicocorticoide sintético que se liga ao receptor de glucocorticoide (GR) intracelular, desencadeando supressão potente da resposta imune: inibe a produção de citocinas pró-inflamatórias (IL-2, IFN-γ), bloqueia a ativação e proliferação de células T e reduz a expressão de moléculas de adesão. Este mecanismo é a base de seu uso consolidado em múltiplas condições autoimunes e inflamatórias.

A alopecia areata é uma doença autoimune em que células T CD8+ atacam os folículos pilosos, destruindo a "imunoprivilégio" local e desencadeando a queda de cabelo. A conexão mecanística com a dexamethasona é, portanto, direta: ao bloquear a ativação das células T CD8+ e suprimir as citocinas inflamatórias responsáveis pelo dano folicular, o fármaco pode interromper o processo patológico. O regime denominado "mini-pulse" — tipicamente 5 mg oral em dois dias consecutivos por semana, ou pulso intravenoso mensal — foi desenvolvido especificamente para equilibrar eficácia imunossupressora com menor risco de supressão do eixo hipotálamo-hipófise-adrenal (HPA), tornando-se um regime de segunda linha estabelecido em dermatologia.

A analogia entre a indicação original (imunossupressão sistêmica) e a nova indicação (AA de etiologia autoimune) é direta e bem fundamentada mecanisticamente, o que explica tanto a alta pontuação do modelo TxGNN (99,99%) quanto a existência de literatura clínica substancial em múltiplos desenhos de estudo apoiando este uso.

---

## Evidências de Ensaios Clínicos

> ⚠️ **Nota sobre relevância:** Os ensaios clínicos recuperados pelo sistema utilizaram dexamethasona predominantemente como medicação adjuvante (pré-medicação, antiemético, manejo de edema) em protocolos oncológicos — não como tratamento primário para alopecia areata. Não foi identificado nenhum ensaio clínico registrado no ClinicalTrials.gov com dexamethasona como intervenção principal para AA. A literatura clínica (seção abaixo) constitui a fonte de evidências direta mais relevante.

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT04343560](https://clinicaltrials.gov/study/NCT04343560) | N/A | Concluído | 380 | Estudo observacional sobre efeitos do metabolismo anormal de esteroides na densidade e qualidade óssea, remodelação e composição corporal em pacientes com secreção autônoma de cortisol (MACS); fornece dados de segurança a longo prazo de corticosteroides |
| [NCT02685826](https://clinicaltrials.gov/study/NCT02685826) | Phase 1/2 | Concluído | 56 | Durvalumab + Lenalidomida ± Dexametasona em mieloma múltiplo recém-diagnosticado; dexametasona como componente do regime imunomodulador, não como principal agente |
| [NCT02288078](https://clinicaltrials.gov/study/NCT02288078) | Phase 2 | Desconhecido | 74 | Avaliação prospectiva e randomizada de dexametasona oral profilática para fadiga e mal-estar por Regorafenibe em câncer colorretal metastático; demonstra efeito anti-fadiga do corticoide |
| [NCT01866449](https://clinicaltrials.gov/study/NCT01866449) | Phase 2 | Concluído | 24 | Cabazitaxel em glioblastoma refratário a Temozolomida; dexametasona utilizada para manejo de edema cerebral, demonstrando papel anti-inflamatório do SNC |
| [NCT01126736](https://clinicaltrials.gov/study/NCT01126736) | Phase 1/2 | Concluído | 98 | Eribulina + Pemetrexede em CPNPC estágio IIIB/IV; dexametasona como pré-medicação obrigatória para Pemetrexede |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | RCT | Dermatologic Therapy | ECR em 30 crianças com AA grave comparando mini-pulse de dexametasona oral vs. DPCP (difenicilopropenona); ambas as modalidades apresentaram eficácia, com dexametasona demonstrando respostas rápidas |
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | Systematic Review / Network Meta-analysis | Archives of Dermatological Research | Revisão sistemática e meta-análise em rede conforme PRISMA comparando corticosteroides sistêmicos, inibidores de JAK e imunoterapia de contato em AA grave (SALT ≥ 50%); corticosteroides sistêmicos com perfil de eficácia comparável |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | Prospective Cohort | Journal of Clinical Medicine | Coorte prospectiva de vida real avaliando eficácia e segurança do mini-pulse oral de corticosteroides para AA; identificou fatores clínicos preditivos de boa resposta |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | Case Series | Journal of Dermatological Treatment | Remissão durável de AA grave com mini-pulse de dexametasona oral em pacientes inelegíveis ou sem acesso a inibidores de JAK; revisão focada de alternativas ao JAKi |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | Retrospective Cohort | Dermatologic Therapy | Estudo multicêntrico de mini-pulse oral de dexametasona para AA moderada a grave em subtipos extensos (totalis, universalis, multifocal), em contexto europeu com acesso limitado a JAKi |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Clinical Review | Pediatric Dermatology | Revisão da literatura sobre pulsoterapia com corticosteroides em crianças com AA; avalia esquemas de dosagem, vias de administração e perfil de efeitos adversos em faixa etária pediátrica |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | Observational Study | Dermatologic Therapy | 73 pacientes pediátricos com AA grave (>30% do couro cabeludo); pulsos IV mensais de dexametasona por 1 ou 3 dias; 67% de boa resposta (>50% de recrescimento), com seguimento estruturado |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | Longitudinal Cohort | Dermatologic Therapy | Seguimento de longo prazo (mediana de 96 meses) de 65 crianças com AA afetando >30% do couro cabeludo tratadas com pulso oral de dexametasona; dados sobre manutenção da resposta e recidiva |
| [16707886](https://pubmed.ncbi.nlm.nih.gov/16707886/) | 2006 | Comparative Study | Dermatology (Basel) | Comparação de três modalidades de corticosteroides sistêmicos em AA extensiva; análise de eficácia, taxa de recidiva e efeitos colaterais entre as diferentes estratégias posológicas |
| [10535249](https://pubmed.ncbi.nlm.nih.gov/10535249/) | 1999 | Observational Study | Journal of Dermatology | 30 pacientes com AA extensiva (média de 4,2 anos de evolução) tratados com pulso oral de dexametasona 5 mg em 2 dias consecutivos por semana; avaliação de recrescimento de cabelo terminal após mínimo de 12 semanas |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Existe base mecanística sólida (imunossupressão GR-mediada direcionada ao mecanismo central da AA) e literatura clínica consistente — incluindo um ECR pediátrico, revisão sistemática com meta-análise em rede e múltiplas coortes prospectivas e longitudinais — que suporta o uso do regime mini-pulse de dexametasona para alopecia areata moderada a grave. O nível de evidência L2 e a ausência de ensaios clínicos dedicados registrados justificam avançar com cautela estruturada.

**Para prosseguir, é necessário:**
- **Verificar registros ANVISA:** O sistema não identificou registros ativos de dexametasona no Brasil, o que é inconsistente com o perfil clínico do fármaco; uma consulta direta à base de dados da ANVISA é prioritária
- **Obter dados completos de segurança:** Advertências, contraindicações e interações medicamentosas da bula brasileira aprovada
- **Definir protocolo de monitoramento:** Para o regime mini-pulse, estabelecer parâmetros de vigilância de glicemia, pressão arterial, densidade mineral óssea e supressão do eixo HPA
- **Mapear posologia e cobertura regulatória:** Confirmar se o esquema mini-pulse (5 mg oral 2x/semana) está coberto pelas indicações aprovadas existentes ou requer uso off-label estruturado
- **Análise comparativa com inibidores de JAK:** Baricitinibe e ritlecitinibe receberam aprovações recentes para AA; definir o posicionamento terapêutico relativo da dexamethasona (custo, acesso, populações específicas como gestantes ou pacientes imunossuprimidos)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

