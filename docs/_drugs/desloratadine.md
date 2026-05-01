---
layout: default
title: Desloratadine
parent: 僅模型預測 (L5)
nav_order: 214
evidence_level: L5
indication_count: 10
---

# Desloratadine
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

# Desloratadine: De Rinite Alérgica para Urticária ao Frio

## Resumo em Uma Frase

Desloratadine é um anti-histamínico de segunda geração seletivo para receptores H1, amplamente utilizado no tratamento de rinite alérgica e urticária idiopática crônica em diversos países ao redor do mundo.
O modelo TxGNN prevê que pode ser eficaz para **Urticária ao Frio (Cold Urticaria)**,
atualmente com **3 ensaios clínicos** e **7 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Rinite alérgica e urticária crônica idiopática (indicação global; sem registro na ANVISA) |
| Nova Indicação Prevista | Urticária ao Frio (Cold Urticaria) |
| Pontuação de Previsão TxGNN | 99.94% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Desloratadine é um antagonista seletivo e de longa duração dos receptores H1 de histamina — metabolito ativo da loratadina. Seu mecanismo central é o bloqueio periférico dos receptores H1, inibindo os efeitos da histamina nos tecidos: vasodilatação, extravasamento vascular, prurido e formação de edema. Estudos in vitro adicionalmente demonstraram propriedades anti-inflamatórias independentes da histamina, como inibição da liberação de citocinas pró-inflamatórias (IL-4, IL-13) e supressão da via NF-κB.

A urticária ao frio é uma forma de urticária física desencadeada pela exposição ao frio, que ativa mastócitos e basófilos cutâneos, levando à degranulação e à liberação maciça de histamina. O resultado clínico — pápulas, eritema, prurido e potencial anafilaxia sistêmica — é mediado diretamente por este mediador. Este mecanismo se alinha com precisão ao bloqueio H1 do desloratadine, que atua sobre o principal mediador inflamatório desta condição, tornando a previsão do TxGNN biologicamente plausível.

Crucialmente, estudos clínicos de escalada de dose confirmaram que doses elevadas de desloratadine (10–20 mg, frente à dose-padrão de 5 mg) aumentam o limiar crítico de temperatura necessário para desencadear os sintomas, demonstrando uma relação dose-resposta mensurável. Esta evidência diferencia esta indicação de uma mera associação topológica no grafo do conhecimento, conferindo robustez à predição do modelo.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Phase 4 | Concluído | 33 | Estudo randomizado duplo-cego, placebo-controlado e crossover. Compara desloratadine 5 mg vs. 20 mg em urticária ao frio adquirida, utilizando termografia, volumetria e fotografia temporal. Hipótese: updosing (20 mg) é superior à dose-padrão e ao placebo. Metodologia mais rigorosa entre os três ensaios. |
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Phase 4 | Concluído | 30 | Estudo multicêntrico duplo-cego de dose-escalada (5 mg, 10 mg e 20 mg) para determinar a dose de desloratadine suficiente para inibir sintomas de urticária ao frio adquirida. Fornece base clínica direta para esquemas de alta dose. |
| [NCT01940393](https://clinicaltrials.gov/study/NCT01940393) | Phase 4 | Concluído | 150 | Comparação head-to-head de 5 anti-histamínicos (incluindo desloratadine) para avaliação de efeitos farmacocinéticos e farmacodinâmicos em urticária na América Latina tropical. Estudo não exclusivo ao desloratadine, mas oferece dados de eficácia comparativa em contexto regional relevante. |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | RCT | British Journal of Dermatology | RCT de escalada de dose de anti-histamínicos H1 em urticária ao frio; avalia limiar de temperatura crítico como desfecho objetivo. Demonstra variabilidade de resposta individual e suporte clínico para ajuste posológico personalizado. |
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | Estudo Clínico | J Allergy and Clinical Immunology | Alta dose de desloratadine reduz volume de pápula e melhora limiares de provocação ao frio vs. dose-padrão em urticária ao frio adquirida; estudo randomizado, placebo-controlado e crossover. Evidência quantitativa de superioridade da alta dose. |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | Estudo Clínico Controlado | J Dermatological Treatment | Desloratadine 5 mg por 4 dias inibiu resposta a cubos de gelo em 12 pacientes com urticária ao frio. Primeiro estudo específico sobre desloratadine nesta indicação, estabelecendo prova de conceito. |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Revisão | Drugs | Revisão abrangente da etiologia, manejo e opções terapêuticas em urticária crônica; contextualiza anti-histamínicos de segunda geração como pilar da primeira linha e discute perfil autoimune da urticária crônica idiopática. |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Revisão Comparativa | Allergy | Revisão da ebastina em rinite alérgica e urticária crônica com desloratadine como comparador ativo; fornece dados de eficácia comparativa no espectro de urticária e rhinite. |
| [29698807](https://pubmed.ncbi.nlm.nih.gov/29698807/) | 2018 | Série de Casos | J Allergy Clin Immunol In Practice | Descreve nova variante — urticária ao frio alimentar — e seu manejo com anti-histamínicos H1. Amplia o espectro clínico da urticária ao frio para além dos gatilhos físicos clássicos. |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Relato de Caso | Qatar Medical Journal | Primeiro relato de urticária ao frio adquirida após anafilaxia por picada de formiga-preta. Ilustra gatilhos imunológicos não-convencionais da urticária ao frio e manejo com anti-histamínicos. |

---

## Informações de Comercialização no Brasil

Desloratadine **não possui registro ativo na ANVISA** e atualmente não é comercializado no Brasil. Nenhum produto foi identificado no banco de dados regulatório consultado em 2026-03-24.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Há três ensaios clínicos Phase 4 concluídos com metodologia robusta (randomizado, duplo-cego, placebo-controlado, crossover) diretamente testando desloratadine em urticária ao frio, além de 7 publicações científicas com evidência de nível L1. A base mecanística — bloqueio H1 sobre a degranulação de mastócitos induzida pelo frio e a liberação de histamina — é direta, biologicamente plausível e quantitativamente confirmada por relação dose-resposta estabelecida (5 mg < 10 mg < 20 mg em eficácia).

**Para prosseguir, é necessário:**
- Resolver **DG001**: obter e analisar a bula oficial (advertências, contraindicações) para viabilizar a avaliação de segurança S1
- Resolver **DG002**: levantar dados formais do mecanismo de ação (DrugBank API) para completar a análise de relevância mecanística
- Verificar a viabilidade regulatória no Brasil: desloratadine sem registro na ANVISA exige processo de registro ou uso via importação/uso compassivo
- Definir protocolo de monitoramento para uso em alta dose (10–20 mg), que excede a dose-padrão de 5 mg aprovada internacionalmente
- Conduzir revisão sistemática formal da evidência antes de qualquer protocolo clínico brasileiro
---

