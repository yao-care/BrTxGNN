---
layout: default
title: Irbesartan
parent: 僅模型預測 (L5)
nav_order: 286
evidence_level: L5
indication_count: 4
---

# Irbesartan
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

Using the `txgnn-pipeline` skill to orient the work, and now generating the report based on the Evidence Pack. The top predicted indication (`predicted_indications[0]`) is **malignant renovascular hypertension** — I'll focus the report on this indication, noting the absence of clinical trials and literature, and applying the mechanistic rationale from the JSON.

---

# Irbesartan: Da Hipertensão Arterial à Hipertensão Renovascular Maligna

## Resumo em Uma Frase

Irbesartan é um bloqueador do receptor de angiotensina II (BRA/ARB), amplamente utilizado no tratamento da hipertensão arterial e da nefropatia diabética em pacientes com diabetes tipo 2.
O modelo TxGNN prevê que pode ser eficaz para a **Hipertensão Renovascular Maligna (Malignant Renovascular Hypertension)**, com pontuação de predição de 99,31% — porém, atualmente **não há ensaios clínicos nem publicações** específicas apoiando esta indicação.
A plausibilidade é sustentada exclusivamente por raciocínio mecanístico, o que exige cautela antes de qualquer avanço clínico.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Hipertensão arterial / Nefropatia diabética |
| Nova Indicação Prevista | Hipertensão Renovascular Maligna (Malignant Renovascular Hypertension) |
| Pontuação de Previsão TxGNN | 99,31% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados formais sobre o mecanismo de ação disponíveis neste Evidence Pack. Com base em informações amplamente consolidadas na literatura médica, Irbesartan é um antagonista seletivo do receptor AT₁ da angiotensina II, pertencente à classe dos BRA (Bloqueadores do Receptor de Angiotensina). Sua eficácia no controle da pressão arterial e na proteção renal em nefropatia diabética — demonstrada no estudo pivotal IDNT (*Irbesartan Diabetic Nephropathy Trial*) — está amplamente comprovada.

A hipertensão renovascular maligna tem como mecanismo central a estenose da artéria renal, que desencadeia ativação excessiva do sistema RAAS (renina-angiotensina-aldosterona), com elevação pronunciada de renina e angiotensina II circulante. Ao bloquear o receptor AT₁ — o alvo final deste eixo fisiopatológico —, o Irbesartan interrompe diretamente a cascata que sustenta a hipertensão nesta condição, tornando a previsão do TxGNN mecanisticamente coerente e altamente plausível.

Contudo, existe uma ressalva clínica crítica: a hipertensão renovascular maligna é uma emergência com elevada urgência terapêutica. O uso de ARBs neste contexto pode precipitar insuficiência renal aguda grave, especialmente em casos de estenose bilateral das artérias renais ou rim solitário — situação que pode coexistir justamente com este diagnóstico. Este risco de segurança representa o principal obstáculo para progressão direta ao uso clínico sem avaliação estruturada prévia.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Informações de Comercialização no Brasil

Irbesartan possui **20 registros ativos** junto à ANVISA e está comercializado no Brasil. Os dados detalhados de cada registro (número, nome comercial, forma farmacêutica e indicação aprovada) não foram carregados neste Evidence Pack — consulte diretamente o [portal da ANVISA](https://consultas.anvisa.gov.br/) para informações completas.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> ⚠️ **Nota clínica relevante**: A partir do mecanismo de ação do Irbesartan, destaca-se o risco de insuficiência renal aguda em pacientes com estenose bilateral das artérias renais ou rim solitário — cenário que pode coexistir exatamente com o quadro de hipertensão renovascular maligna. Esta sobreposição requer avaliação nefrológica criteriosa antes de qualquer uso nesta indicação.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A conexão mecanística entre o Irbesartan e a hipertensão renovascular maligna é biologicamente coerente — ambas as condições envolvem ativação excessiva do RAAS, e o receptor AT₁ é o alvo central da patologia. No entanto, a ausência total de ensaios clínicos e publicações específicas, combinada ao risco real de insuficiência renal aguda neste contexto clínico de urgência, impede a progressão sem dados adicionais de segurança e eficácia.

**Para prosseguir, é necessário:**
- Obter dados formais de mecanismo de ação (MOA) via DrugBank API
- Baixar e analisar a bula do Irbesartan (ANVISA) para mapeamento completo de advertências e contraindicações — especialmente em contextos de estenose renovascular
- Conduzir revisão sistemática da literatura sobre o uso de ARBs em emergências hipertensivas de origem renovascular
- Avaliar a viabilidade de um estudo observacional piloto em centro especializado de nefrologia e hipertensão
- Verificar se a indicação já coberta pela aprovação atual de hipertensão arterial engloba subtipos renovasculares, o que poderia simplificar o caminho regulatório
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

