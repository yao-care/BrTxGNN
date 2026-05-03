---
layout: default
title: Zinc Sulfate
parent: 僅模型預測 (L5)
nav_order: 514
evidence_level: L5
indication_count: 4
---

# Zinc Sulfate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Sulfato de Zinco: Do suplemento de zinco à faringite

## Resumo em Uma Frase

Sulfato de zinco é um composto inorgânico de zinco reconhecido pelo uso como suplemento nutricional e agente tópico para deficiência de zinco, sem registro formal no Brasil até a data desta análise.
O modelo TxGNN prevê que pode ser eficaz para **Faringite (Pharyngitis)**,
atualmente com **4 ensaios clínicos** e **3 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Sem registro de indicação aprovada no Brasil |
| Nova Indicação Prevista | Faringite (Pharyngitis) |
| Pontuação de Previsão TxGNN | 99.85% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação formal do sulfato de zinco no repositório DrugBank consultado. Com base no conhecimento disponível, o sulfato de zinco é um sal inorgânico que libera íons zinco (Zn²⁺) — mineral essencial envolvido em centenas de reações enzimáticas e no funcionamento do sistema imunológico. Seu histórico de uso inclui suplementação de zinco em deficiências nutricionais, tratamento de acne em algumas formulações e uso oftalmológico como adstringente.

A ligação mecanística com a faringite é biologicamente plausível: os íons zinco demonstraram capacidade de **interferir na ligação do rinovírus ao receptor ICAM-1**, inibindo a replicação viral nas células da mucosa faríngea. Além disso, o zinco exerce efeito anti-inflamatório direto, modulando a resposta imune local e reduzindo a produção de citocinas pró-inflamatórias. Quando administrado em forma de pastilha (*lozenge*), o sulfato de zinco mantém concentrações locais elevadas em contato direto com a mucosa da garganta, potencializando esses efeitos.

É importante, contudo, distinguir entre a **formulação local (pastilhas de zinco)** e a **administração sistêmica (sulfato de zinco oral/IV)**. A grande maioria das evidências disponíveis para faringite e dor de garganta refere-se a formas de contato local. A eficácia sistêmica para infecções faríngeas não está suficientemente estabelecida e exige investigação específica por via de administração.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02405832](https://clinicaltrials.gov/study/NCT02405832) | NA | Concluído | 87 | Ensaio duplo-cego, placebo-controlado avaliando o efeito de pastilhas de zinco administradas antes da cirurgia na incidência de síndrome de dor de garganta pós-operatória em pacientes com intubação endotraqueal — alta relevância para faringite |
| [NCT04370782](https://clinicaltrials.gov/study/NCT04370782) | Phase 4 | Concluído | 18 | Avaliação de hidroxicloroquina + zinco com azitromicina ou doxiciclina para COVID-19 ambulatorial; relevância para faringite é indireta, e o tamanho amostral (n=18) é insuficiente para conclusões isoladas sobre o zinco |
| [NCT04446104](https://clinicaltrials.gov/study/NCT04446104) | Phase 3 | Concluído | 4.257 | Grande ensaio profilático em trabalhadores migrantes de alto risco para COVID-19 (n=4.257); suporta o potencial antiviral do zinco em infecções respiratórias, incluindo sintomas de faringite, mas não avalia faringite como desfecho primário |
| [NCT04621461](https://clinicaltrials.gov/study/NCT04621461) | Phase 4 | Concluído | 3 | Ensaio duplo-cego placebo-controlado para COVID-19 ambulatorial com zinco; n=3 torna impossível qualquer conclusão estatística |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [38693477](https://pubmed.ncbi.nlm.nih.gov/38693477/) | 2024 | RCT | BMC Anesthesiology | Comparação de gargarejos pré-operatórios com zinco, magnésio e budesonida para redução da incidência e gravidade de dor de garganta pós-operatória em pacientes com intubação endotraqueal; suporte direto ao uso do zinco em patologia faríngea |
| [23720981](https://pubmed.ncbi.nlm.nih.gov/23720981/) | 2013 | RCT | J Med Assoc Thailand | Ensaio duplo-cego placebo-controlado de suplementação com sulfato de zinco para alívio de mucosite oral e faringite induzidas por radioterapia em pacientes com câncer de cabeça e pescoço; uso direto do sulfato de zinco na faringite |
| [20123362](https://pubmed.ncbi.nlm.nih.gov/20123362/) | 2010 | Case Report | Oral Surg Oral Med Oral Pathol | Relato de caso sobre disgeusia pós-amigdalectomia de longa duração e seu tratamento; levanta o papel da deficiência de zinco em complicações de procedimentos faríngeos — evidência indireta e de baixo nível |

---

## Situação no Mercado Brasileiro

O sulfato de zinco **não possui registro ativo na ANVISA** até a data de corte desta análise (2026-05-03). Nenhuma licença de comercialização foi identificada, o que significa que eventual uso clínico no Brasil dependeria de importação por excepcionalidade ou de um processo formal de registro.

---

## Considerações de Segurança

Não há dados de advertências, contraindicações ou interações medicamentosas disponíveis no Evidence Pack consultado para este fármaco.

> Consulte a bula e fontes regulatórias oficiais (ANVISA, DrugBank, TFDA) para informações completas de segurança antes de qualquer uso clínico ou pesquisa.

**Alerta adicional — Indicação de Doença de Cavidade Nasal (Rank 2):**
A literatura disponível para o uso nasal de zinco revela um sinal de segurança importante: a instilação intranasal de sulfato de zinco foi associada a **anosmia periférica permanente** em modelos animais e documentada em eventos adversos humanos (caso Zicam). Este risco deve ser considerado ao avaliar qualquer formulação de zinco para uso em vias aéreas superiores.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Existem dois ensaios clínicos randomizados controlados (RCTs — PMID 38693477 e 23720981) e um ensaio clínico prospectivo duplo-cego (NCT02405832) que fornecem suporte direto ao uso do zinco em condições faríngeas, incluindo avaliação direta do sulfato de zinco para faringite radioinduzida. A plausibilidade mecanística (atividade antiviral e anti-inflamatória local) é sólida, especialmente para formulações de contato direto com a mucosa. O nível de evidência L2 justifica avançar com cautela, porém são necessárias condições específicas para prosseguimento seguro.

**Para prosseguir, é necessário:**
- Confirmar o mecanismo de ação formal (MOA) via consulta ao DrugBank API — dado atualmente ausente
- Obter a bula oficial (TFDA/ANVISA ou equivalente) para mapeamento completo de advertências, contraindicações e interações — dado atualmente bloqueante (DG001)
- Definir **via de administração e forma farmacêutica-alvo**: a evidência favorece formulações de contato local (pastilhas, gargarejos), não sulfato de zinco sistêmico
- Planejar ensaio clínico prospectivo de Phase 2 especificamente para faringite aguda infecciosa com formulação local de zinco, dado que os estudos existentes avaliam modelos cirúrgicos ou de radioterapia
- Verificar compatibilidade regulatória para registro no Brasil antes de qualquer desenvolvimento comercial
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

