---
layout: default
title: Potassium Sulfate
parent: 僅模型預測 (L5)
nav_order: 409
evidence_level: L5
indication_count: 10
---

# Potassium Sulfate
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

Usando o skill `txgnn-pipeline` para verificar contexto do projeto — o skill confirma que este é trabalho de relatório para BrTxGNN. Vou agora gerar o relatório completo com base no Evidence Pack.

---

# Sulfato de Potássio: De composto mineral eletrolítico para Distúrbio Hipertensivo

## Resumo em Uma Frase

Sulfato de Potássio (K₂SO₄) é um composto mineral inorgânico sem indicação farmacêutica formal registrada no Brasil, encontrado principalmente como componente em soluções de preparo intestinal e produtos agrícolas. O modelo TxGNN prevê que pode ser eficaz para **Distúrbio Hipertensivo (Hypertensive Disorder)**, com base no mecanismo de fornecimento de íons K⁺ e sua ação vasodilatadora. Atualmente, há **1 ensaio clínico com relevância indireta** e **nenhuma publicação diretamente relacionada** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Sem indicação farmacêutica formal registrada |
| Nova Indicação Prevista | Distúrbio Hipertensivo (Hypertensive Disorder) |
| Pontuação de Previsão TxGNN | 98,79% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Não há dados formais de mecanismo de ação (MOA) disponíveis para o Sulfato de Potássio (K₂SO₄) enquanto agente farmacêutico. Trata-se de um sal inorgânico cuja principal propriedade biológica relevante é o fornecimento de íons potássio (K⁺) ao organismo — o mesmo princípio ativo de outros sais de potássio, especialmente o cloreto de potássio (KCl), amplamente estudado em contexto cardiovascular.

A base mecanística da previsão reside no papel do K⁺ na regulação da pressão arterial: o potássio promove a natriurese renal (favorece a excreção urinária de sódio), hiperpolariza a membrana do músculo liso vascular promovendo vasodilatação direta, e pode suprimir a atividade do sistema renina-angiotensina-aldosterona (RAAS). Revisões sistemáticas sobre suplementação de potássio (com KCl) demonstram redução modesta mas consistente da pressão arterial em populações hipertensas. O estudo NCT01429246, conduzido no Tibet com 282 participantes hipertensos, avaliou um substituto salino à base de KCl e confirmou redução de pressão arterial sistólica, representando a evidência indireta mais robusta identificada para a classe.

Contudo, é fundamental ressaltar que **toda evidência clínica disponível utiliza KCl — não K₂SO₄**. O ânion acompanhante (SO₄²⁻ vs. Cl⁻) pode influenciar significativamente a biodisponibilidade oral, a tolerabilidade gastrointestinal e os efeitos renais. Não existe nenhum ensaio clínico randomizado testando diretamente K₂SO₄ como agente anti-hipertensivo, tornando esta previsão uma extrapolação de classe com plausibilidade mecanística, mas sem evidência clínica direta.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT01429246](https://clinicaltrials.gov/study/NCT01429246) | N/A | Concluído | 282 | ECR cego simples no Tibet: substituto salino (KCl) vs. NaCl em hipertensos (PAS ≥ 140 mmHg) a 4.300 m de altitude. Mecanismo K⁺ análogo ao K₂SO₄, mas composto diferente. Melhor evidência indireta disponível (Grau B). |
| [NCT00811954](https://clinicaltrials.gov/study/NCT00811954) | Phase 3 | Concluído | 1.814 | Estudo ARDENT comparando regimes antirretrovirais (atazanavir, raltegravir, darunavir + TDF/FTC) em HIV não tratados; hipertensão como comorbidade dos participantes. Sem relação com K₂SO₄ (Grau C). |
| [NCT06111885](https://clinicaltrials.gov/study/NCT06111885) | Phase 2 | Recrutando | 99 | Cruzamento duplo-cego comparando diuréticos tiazídicos (indapamida, clortalidona vs. hidroclorotiazida) para prevenção de cálculos renais; hipocalemia figura como contexto adverso. Sem relação com K₂SO₄ (Grau C). |
| [NCT03975790](https://clinicaltrials.gov/study/NCT03975790) | N/A | Concluído | 479 | Estudo de coorte retrospectivo de tofacitinib + metotrexato em artrite reumatoide; hipertensão como comorbidade. Sem relação com K₂SO₄ (Grau C). |

> **Observação:** Nenhum dos ensaios testou diretamente K₂SO₄ como agente terapêutico anti-hipertensivo. Três dos quatro ensaios são classificados como Grau C (sem relação com o composto). O NCT01429246 é o único com relevância indireta (Grau B) por compartilhar o mecanismo K⁺.

---

## Evidências da Literatura

Atualmente não há literatura diretamente relacionada ao uso de Sulfato de Potássio para distúrbio hipertensivo. A única publicação identificada na busca (PMID 25917854, *Journal of Prosthetic Dentistry*, 2015) aborda procedimentos odontológicos de afastamento gengival — sem qualquer relação com hipertensão ou uso sistêmico de K₂SO₄. Nenhuma publicação clínica ou pré-clínica investigando K₂SO₄ para indicação cardiovascular foi identificada.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do modelo TxGNN possui plausibilidade mecanística via suplementação de K⁺, porém toda evidência clínica relevante foi gerada com KCl, não com K₂SO₄. A diferença no ânion acompanhante representa uma lacuna crítica que impede a extrapolação direta. Adicionalmente, o composto não possui qualquer registro ou comercialização no Brasil, e os dados de segurança para uso farmacêutico sistêmico oral são inexistentes no pacote atual.

**Para prosseguir, é necessário:**
- Estudo de biodisponibilidade e farmacocinética comparando K₂SO₄ vs. KCl em administração oral
- Ensaio clínico piloto (Phase 1/2) avaliando o efeito de K₂SO₄ oral sobre a pressão arterial em adultos hipertensos
- Levantamento completo do perfil de segurança: tolerabilidade gastrointestinal, efeito renal e risco de hipercalemia
- Preenchimento da lacuna de MOA via consulta ao DrugBank e literatura farmacológica especializada (lacuna DG002)
- Avaliação de viabilidade regulatória para registro como medicamento junto à ANVISA antes de qualquer estudo clínico no Brasil
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

