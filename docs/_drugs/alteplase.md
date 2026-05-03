---
layout: default
title: Alteplase
parent: 僅模型預測 (L5)
nav_order: 41
evidence_level: L5
indication_count: 9
---

# Alteplase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Alteplase: Da Terapia Trombolítica ao Infarto do Miocárdio Posterolateral

## Resumo em Uma Frase

Alteplase é um ativador do plasminogênio tecidual recombinante (rt-PA), amplamente utilizado no tratamento do AVC isquêmico agudo, STEMI e embolia pulmonar maciça. O modelo TxGNN prevê que pode ser eficaz para **Infarto do Miocárdio Posterolateral (posterolateral myocardial infarction)**, com **0 ensaios clínicos específicos** e **3 publicações** apoiando esta direção. Em uma análise de 9 indicações candidatas (pacote multi-indicação), o **infarto septal** (rank 3) apresenta o nível de evidência mais robusto (L1), sustentado por ensaios clínicos Phase 3 e 13 publicações.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | AVC isquêmico agudo; STEMI; Embolia Pulmonar Maciça |
| Nova Indicação Prevista (Rank 1) | Infarto do Miocárdio Posterolateral |
| Pontuação de Previsão TxGNN | 99,79% |
| Nível de Evidência | L3 (Rank 1) · L1 disponível no Rank 3 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 1 |
| Decisão Recomendada | Proceed with Guardrails (Rank 3 — Infarto Septal) |

---

## Resumo das 9 Indicações Previstas

| Rank | Indicação | Score TxGNN | Evidência | Ensaios | Publicações | Decisão |
|------|-----------|-------------|-----------|---------|-------------|---------|
| 1 | Infarto posterolateral | 99,79% | L3 | 0 | 3 | Research Question |
| 2 | Infarto postero-inferior | 99,79% | L4 | 0 | 1 | Research Question |
| **3** | **Infarto septal** | **99,77%** | **L1** | **1** | **13** | **Proceed with Guardrails** |
| 4 | Deficiência de heparina cofator 2 | 99,72% | L4 | 0 | 20 | Hold |
| 5 | Anomalia congênita da coronária | 99,64% | L3 | 4 | 5 | Research Question |
| 6 | Excesso do fator V c/ trombose espontânea | 99,56% | L5 | 0 | 0 | Hold |
| 7 | Deficiência de antitrombina tipo 2 | 99,56% | L5 | 0 | 0 | Hold |
| **8** | **Trombofilia** | **99,43%** | **L2** | **9** | **20** | **Proceed with Guardrails** |
| 9 | Estenose coronária | 99,14% | L2 | 7 | 20 | Research Question |

---

## Por que Esta Previsão é Razoável?

Alteplase é uma serina protease recombinante que converte o plasminogênio em plasmina com alta seletividade para a fibrina, dissolvendo coágulos de fibrina nos sítios de trombose ativa. Ao contrário dos fibrinolíticos de primeira geração (ex.: estreptoquinase), alteplase possui preferência cinética pela fibrina associada ao coágulo e meia-vida plasmática curta (~5 minutos), o que confere um perfil de ação localizado. Por ter estrutura idêntica ao tPA endógeno produzido pelo endotélio vascular, o mecanismo de ação é fisiologicamente integrado ao sistema fibrinolítico natural.

O infarto do miocárdio posterolateral ocorre tipicamente pela oclusão trombótica da artéria coronária direita (ACD) em seu segmento distal ou da artéria circunflexa esquerda (ACE), com isquemia das paredes posterior e lateral do ventrículo esquerdo. Este substrato fisiopatológico — oclusão trombótica coronária aguda causando necrose miocárdica — é mecanisticamente idêntico ao do STEMI para o qual alteplase já possui aprovação regulatória consolidada; a distinção é essencialmente anatômica (localização da oclusão) e diagnóstica (derivações V7–V9), e não mecanística. A plausibilidade da previsão TxGNN é, portanto, muito alta.

A escassez de ensaios clínicos específicos para esta subclassificação anatômica reflete, principalmente, a tradição de estudos em STEMI como categoria global, e não uma ausência de eficácia. O TAMI-1 (Phase 3 RCT, PMID 2521226) — avaliado no contexto do infarto septal (rank 3) — analisou diretamente alteplase em diferentes territórios coronários, incluindo dados estratificados por artéria responsável (LAD, LCX e ACD), fornecendo uma base de evidências transferível para os subtipos anatômicos posterolateral e posteroinferior.

---

## Evidências de Ensaios Clínicos — Infarto Posterolateral (Rank 1)

Atualmente não há ensaios clínicos relacionados especificamente ao infarto do miocárdio posterolateral com alteplase registrados.

---

## Evidências da Literatura — Infarto Posterolateral (Rank 1)

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [9502627](https://pubmed.ncbi.nlm.nih.gov/9502627/) | 1998 | Observacional | J Am Coll Cardiol | Elevação do ST nas derivações posteriores (V7–V9) durante IAM inferior identifica infarto posterior concomitante; pacientes com infarto posterior têm maior benefício potencial com trombólise |
| [21351226](https://pubmed.ncbi.nlm.nih.gov/21351226/) | 2011 | Relato de Caso | Catheter Cardiovasc Interv | IAM posterolateral por oclusão ostial do tronco coronário esquerdo (FE 30%): PCI com mini-crush DES facilitada por reteplase intracoronária; manejo trombolítico adjunto em caso de alto risco hemodinâmico |
| [8480981](https://pubmed.ncbi.nlm.nih.gov/8480981/) | 1993 | Relato de Caso | Ann Cardiol Angeiol | Fibrinólise tardia com tPA em IAM posterolateral complicada por embolismo cerebral; revisão dos riscos de embolização sistêmica por trombos intraventriculares durante terapia fibrinolítica |

---

## Indicação com Maior Evidência: Infarto Septal (Rank 3)

O infarto septal apresenta o maior nível de evidência do pacote multi-indicação (L1), com o TAMI-1 como principal estudo de referência. A seguir, os principais ensaios e publicações.

### Evidências de Ensaios Clínicos — Infarto Septal

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT03377465](https://clinicaltrials.gov/study/NCT03377465) | N/A | Concluído | 100 | Preditores biomarcadores e ecocardiográficos de AVC isquêmico em pacientes com doença coronária; contexto clínico com alteplase como terapia de referência — relevância indireta como dado de background |

### Evidências da Literatura — Infarto Septal

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [2521226](https://pubmed.ncbi.nlm.nih.gov/2521226/) | 1989 | Phase 3 RCT | J Am Coll Cardiol | **TAMI-1**: alteplase 150mg IV em 386 pacientes com IAM; análise estratificada por artéria responsável — LAD 77%, LCX 68%, ACD 68% de patência aos 90 min; base direta para eficácia em IAM septal (território LAD proximal) |
| [8763515](https://pubmed.ncbi.nlm.nih.gov/8763515/) | 1996 | RCT | Rev Port Cardiol | Fibrinólise tardia (>6h) com alteplase em IAM: melhora significativa dos parâmetros de função ventricular esquerda — mecanismo de proteção miocárdica relevante para IAM septal |
| [1907087](https://pubmed.ncbi.nlm.nih.gov/1907087/) | 1991 | RCT | Am Heart J | TAMI 1–3 e 5: cirurgia de bypass em 303/1387 pacientes após terapia trombolítica com alteplase; evidência da cadeia terapêutica completa (fibrinólise → PCI → CABG) em IAM |
| [9014973](https://pubmed.ncbi.nlm.nih.gov/9014973/) | 1997 | Cohort Retrospectivo | J Am Coll Cardiol | **GUSTO**: impacto da revascularização cirúrgica na sobrevida pós-IAM tratado com tPA; dados de desfechos de longo prazo após fibrinólise sistêmica |
| [40281444](https://pubmed.ncbi.nlm.nih.gov/40281444/) | 2025 | Cohort Study | BMC Cardiovasc Disord | SCA (STEMI/NSTEMI/AI) no Butão: fibrinólise como estratégia primária em contexto com PCI limitado; resultados clínicos de curto prazo que apoiam o papel da fibrinólise onde PCI não está disponível |
| [37754803](https://pubmed.ncbi.nlm.nih.gov/37754803/) | 2023 | Relato de Caso | J Cardiovasc Dev Dis | EP maciça simulando IAM antero-septal com supradesnivelamento de ST em V1–V2; tratada com trombectomia e trombólise dirigida por cateter — diagnóstico diferencial crítico para a indicação |
| [18183355](https://pubmed.ncbi.nlm.nih.gov/18183355/) | 2009 | Relato de Caso | J Thromb Thrombolysis | EP maciça mimetizando IAM septal tratada com tenecteplase; salienta a necessidade de confirmação diagnóstica antes do uso de fibrinolítico em ST-elevação septal |
| [8638875](https://pubmed.ncbi.nlm.nih.gov/8638875/) | 1996 | Relato de Caso | Angiology | CIV pós-infarto em paciente trombolisado com coronárias normais; sobrevida de longo prazo — complicação estrutural rara pós-fibrinólise em IAM septal |
| [10983682](https://pubmed.ncbi.nlm.nih.gov/10983682/) | 2000 | Série de Casos | Scand Cardiovasc J | Fechamento transcateter de CIV pós-infarto (n=2) com Amplatzer — manejo de complicação estrutural pós-IAM septal após falha cirúrgica |
| [1934382](https://pubmed.ncbi.nlm.nih.gov/1934382/) | 1991 | RCT | Circulation | Ácido tranexâmico + desmopressina em cirurgia cardíaca: relação com liberação de tPA endotelial — dados mecanísticos sobre o sistema fibrinolítico em contexto cardiovascular cirúrgico |

---

## Informações de Comercialização no Brasil

Os dados detalhados do registro ANVISA (número de registro, nome comercial, forma farmacêutica e texto completo da indicação aprovada) não estão disponíveis no pacote de evidências atual. Alteplase encontra-se em situação ativa de comercialização no Brasil com 1 registro ativo.

> Para informações completas do registro, consulte o **DATAVISA/ANVISA**: https://consultas.anvisa.gov.br/

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails** *(Rank 3 — Infarto Septal)* · **Research Question** *(Rank 1 — Infarto Posterolateral)*

**Justificativa:**

- O **infarto septal** (rank 3) é sustentado por evidência **L1**: o TAMI-1 (Phase 3 RCT, n=386) avaliou diretamente alteplase por localização de IAM, com 77% de patência coronária em território LAD (responsável pelo infarto septal) aos 90 minutos. A cadeia de evidências (TAMI-1 → RCTs de função ventricular → GUSTO) é coerente e o mecanismo é idêntico ao STEMI aprovado. Esta é a indicação candidata mais madura do pacote.
- O **infarto posterolateral** (rank 1) é mecanisticamente altamente plausível, mas a evidência disponível (3 publicações: 1 observacional, 2 relatos de caso) configura nível L3, insuficiente para mudança de protocolo sem investigação prospectiva adicional.
- A **trombofilia** (rank 8, L2) apresenta dois ensaios de nível A: NCT00251771 (RCT concluído, n=209, CDT vs. anticoagulação em DVT iliofemoral — contexto de alta prevalência de trombofilia) e NCT05540834 (Phase 2, VET-guiado para tPA individualizado). Também recomendada como "Proceed with Guardrails" em serviços com protocolo CDT estabelecido.

**Para prosseguir, é necessário:**

- **[Prioritário — Blocking]** Resolver DG001: Obter advertências e contraindicações completas da bula ANVISA — sem este dado, a avaliação de segurança S1 não pode ser concluída
- **[Alta Prioridade]** Resolver DG002: Confirmar mecanismo de ação detalhado via DrugBank para análise de relevância mecanística completa
- Confirmar número de registro ANVISA, nome comercial e forma farmacêutica disponível no Brasil
- Para o **infarto septal**: mapear os critérios de elegibilidade do TAMI-1 em relação aos protocolos brasileiros atuais de STEMI (tempo porta-balão, disponibilidade de PCI); definir cenários em que fibrinólise é alternativa (ex.: ausência de laboratório de hemodinâmica 24h)
- Para o **infarto posterolateral**: desenhar estudo observacional prospectivo estratificado por localização anatômica com derivações V7–V9, focando em desfechos de reperfusão
- Para a **trombofilia**: avaliar aplicabilidade do protocolo CDT do NCT00251771 em serviços brasileiros de referência em trombose venosa, com avaliação de risco hemorrágico individualizado
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

