---
layout: default
title: Dexchlorpheniramine
parent: 僅模型預測 (L5)
nav_order: 217
evidence_level: L5
indication_count: 2
---

# Dexchlorpheniramine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

Com base no Evidence Pack fornecido, segue o relatório de avaliação de reposicionamento:

---

# Dexchlorpheniramine: De antihistamínico H1 de 1ª geração para urticária alérgica

## Resumo em Uma Frase

Dexchlorpheniramine é o enantiômero ativo (dextroisômero R) da clorfeniramina, um antihistamínico H1 de primeira geração classicamente utilizado no manejo de condições alérgicas, porém sem registro ativo na ANVISA.
O modelo TxGNN prevê que pode ser eficaz para **Urticária Alérgica (Allergic Urticaria)**, atualmente com **0 ensaios clínicos registrados** e **6 publicações** apoiando esta direção.
A pontuação TxGNN de 99,89% e o alinhamento mecanístico direto fundamentam a recomendação de **Proceed with Guardrails**.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Antihistamínico H1 de 1ª geração (sem registro formal no Brasil) |
| Nova Indicação Prevista | Urticária Alérgica (Allergic Urticaria) |
| Pontuação de Previsão TxGNN | 99,89% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Dexchlorpheniramine é o isômero dextrógiro da clorfeniramina, pertencente à classe dos antihistamínicos H1 de primeira geração. Embora os dados formais de MOA estejam pendentes de complementação via DrugBank (lacuna DG002), o mecanismo farmacológico da classe é amplamente estabelecido: a molécula atua como antagonista competitivo do receptor H1, bloqueando a ligação da histamina liberada por mastócitos e basófilos após sensibilização alérgena — inibindo assim vasodilatação, aumento da permeabilidade vascular e estímulo nociceptivo responsáveis pelo prurido.

A urticária alérgica tem como eixo fisiopatológico central exatamente esses eventos. A exposição ao alérgeno desencadeia desgranulação de mastócitos dérmicos, com liberação de histamina que ativa receptores H1 em células endoteliais e fibras nervosas sensoriais, resultando em pápulas eritematosas pruriginosas e eritema circundante. O bloqueio desse receptor pelo dexchlorpheniramine ataca diretamente os mediadores responsáveis pela lesão clínica característica da doença.

Complementarmente, literatura de base mecanística (PMID 2523357) documenta que antihistamínicos desta classe exercem efeitos anti-inflamatórios multimodais — inibição da quimiotaxia de eosinófilos e da ativação plaquetária dependente de IgE — que conferem suporte além do simples antagonismo H1. O estudo farmacológico controlado conduzido no Brasil (PMID 29723372) avaliou diretamente a potência de supressão de pápula e eritema do dexchlorpheniramine frente a outros antihistamínicos disponíveis no mercado brasileiro, reforçando a relevância local da molécula.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados (ClinicalTrials.gov e ICTRP consultados em 26/03/2026).

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [39265704](https://pubmed.ncbi.nlm.nih.gov/39265704/) | 2024 | Estudo Clínico Comparativo (Fase I RCT) | Eur J Pharm Sci | Comparação entre bilastina oral, dexchlorpheniramine parenteral e nova formulação parenteral de bilastina na supressão de pápula e eritema induzidos por histamina; dexchlorpheniramine utilizado como comparador ativo de referência padrão |
| [29723372](https://pubmed.ncbi.nlm.nih.gov/29723372/) | 2018 | Estudo Farmacodinâmico Controlado | An Bras Dermatol | Avaliação comparativa da potência dos principais antihistamínicos H1 comercializados no Brasil; dexchlorpheniramine demonstrou supressão significativa da resposta ao teste de histamina cutânea |
| [39803](https://pubmed.ncbi.nlm.nih.gov/39803/) | 1979 | Estudo Clínico Inicial | Dermatologica | Caso de urticária de contato por calor adquirida em mulher jovem; documenta resposta ao tratamento antihistamínico e parâmetros imunológicos envolvidos na urticária física |
| [2523357](https://pubmed.ncbi.nlm.nih.gov/2523357/) | 1989 | Estudo Mecanístico In Vitro | Int Arch Allergy | Documentação de mecanismos anti-inflamatórios adicionais de antihistamínicos H1 — inibição de quimiotaxia eosinofílica e ativação plaquetária IgE-dependente; relevante para a compreensão das ações de classe do dexchlorpheniramine |
| [28601540](https://pubmed.ncbi.nlm.nih.gov/28601540/) | 2017 | Relato de Caso | Am J Med | Fibrilação atrial em anafilaxia; uso de dexchlorpheniramine no manejo de reação alérgica grave com complicação cardiovascular, ilustrando aplicação clínica em contexto agudo |
| [26179134](https://pubmed.ncbi.nlm.nih.gov/26179134/) | 2015 | Relato de Caso | Contact Dermatitis | Angioedema palpebral e dermatite de contato alérgica por cerumenolítico; dexchlorpheniramine empregado no manejo de reação alérgica com componente urticariforme |

---

## Considerações de Segurança

Consulte a bula para informações de segurança. *(Dados de advertências, contraindicações e interações medicamentosas não disponíveis nesta versão do Evidence Pack — lacunas DG001 e DG002 pendentes de resolução via bula ANVISA/TFDA e DrugBank API.)*

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
O alinhamento entre o mecanismo de antagonismo H1 do dexchlorpheniramine e a fisiopatologia central da urticária alérgica é direto e bem fundamentado farmacologicamente; estudos farmacodinâmicos controlados — incluindo um conduzido no próprio Brasil — demonstram eficácia quantificável na supressão da resposta histamínica cutânea. O principal obstáculo é a ausência de registro na ANVISA e de dados formais de segurança neste pacote de evidências.

**Para prosseguir, é necessário:**
- Resolver lacuna DG001: obter bula ANVISA/TFDA para levantamento completo de advertências e contraindicações (severidade **Blocking**)
- Resolver lacuna DG002: confirmar MOA formal via DrugBank API (severidade **High**)
- Investigar se existem registros ANVISA de produtos **combinados** contendo dexchlorpheniramine (e.g., formulações antitussígenas ou antigripais) que possam viabilizar uso off-label em urticária
- Conduzir revisão sistemática comparando dexchlorpheniramine (1ª geração, perfil sedativo) com antihistamínicos de 2ª geração nas diretrizes brasileiras de urticária (SBD/SBAI), avaliando se o perfil de segurança justifica posicionamento em sub-populações específicas
- Avaliar viabilidade de estudo clínico controlado no Brasil caso a estratégia regulatória prossiga, com desfecho primário em escore de atividade de urticária (UAS7)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

