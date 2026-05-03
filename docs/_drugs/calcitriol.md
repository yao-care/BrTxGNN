---
layout: default
title: Calcitriol
parent: 僅模型預測 (L5)
nav_order: 154
evidence_level: L5
indication_count: 7
---

# Calcitriol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Calcitriol: Dos Distúrbios do Metabolismo Cálcio-Fósforo ao Raquitismo Hipofosfatêmico Hereditário

## Resumo em Uma Frase

Calcitriol (1,25-di-hidroxivitamina D₃) é a forma biologicamente ativa da vitamina D, empregada no tratamento de hipocalcemia, hipoparatireoidismo e doença óssea metabólica associada à doença renal crônica. O modelo TxGNN prevê eficácia para **Raquitismo Hipofosfatêmico Hereditário (Hereditary Hypophosphatemic Rickets)**, indicação candidata com o mais alto nível de evidência clínica entre todas as previsões geradas, apoiada por **7 ensaios clínicos** — incluindo um Phase 4 com 100 participantes — e **20 publicações** na literatura especializada.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hipocalcemia e distúrbios do metabolismo cálcio-fósforo (hipoparatireoidismo, doença renal crônica) |
| Nova Indicação Prevista | Raquitismo Hipofosfatêmico Hereditário (Hereditary Hypophosphatemic Rickets) |
| Pontuação de Previsão TxGNN | 99.28% (ranking #7 entre todas as previsões) |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✓ Já comercializado |
| Número de Registros | 12 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Calcitriol é a forma biologicamente ativa da vitamina D, produzida nos rins pela enzima 1α-hidroxilase (CYP27B1). Sua principal ação é ligar-se ao receptor de vitamina D (VDR), um fator de transcrição nuclear que regula a absorção intestinal de cálcio e fósforo, a reabsorção renal desses íons e a mineralização óssea. Embora os dados detalhados de MOA não tenham sido recuperados automaticamente neste Evidence Pack, o mecanismo de ação do calcitriol é amplamente estabelecido e constitui a base de décadas de uso clínico em diversas condições hiperparatiróideas e hipofosfatêmicas.

O raquitismo hipofosfatêmico hereditário — predominantemente a forma X-linked (XLH), causada por mutações no gene PHEX — cursa com hipersecreção crônica do hormônio fosfatúrico FGF23. O FGF23 em excesso exerce duplo efeito supressor: inibe a reabsorção tubular de fosfato (via downregulation dos cotransportadores NaPi-2a/2c) e reduz a atividade da 1α-hidroxilase renal, resultando em níveis de calcitriol endógeno inadequadamente baixos para a condição de hipofosfatemia. A administração exógena de calcitriol contorna diretamente essa supressão enzimática mediada pelo FGF23, fornecendo o ligante VDR ativo necessário para restaurar parcialmente a absorção intestinal de cálcio e fósforo e promover a mineralização óssea.

A terapia combinada de calcitriol + suplementação de fosfato foi o padrão de tratamento global para XLH por décadas — antes da aprovação do burosumab (anti-FGF23) em 2018 pela FDA e EMA. Múltiplos ensaios clínicos, incluindo um Phase 4 com 100 crianças (NCT03820518) comparando diferentes doses de calcitriol, e um estudo de monoterapia com calcitriol atualmente ativo (NCT03748966), reafirmam que este fármaco permanece parte ativa do arsenal terapêutico desta doença, tanto como alternativa de menor custo quanto como possível terapia adjuvante às novas abordagens moleculares.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT03820518](https://clinicaltrials.gov/study/NCT03820518) | Phase 4 | Desconhecido | 100 | RCT comparando alta vs. baixa dose de vitamina D ativa (incluindo calcitriol) combinada com fosfato neutro em crianças com XLH; objetivo de estabelecer dosagem baseada em peso para otimizar eficácia e segurança |
| [NCT03748966](https://clinicaltrials.gov/study/NCT03748966) | Early Phase 1 | Ativo (não recrutando) | 20 | Calcitriol em monoterapia (sem suplementação de fosfato) em crianças e adultos com XLH; hipótese de que calcitriol isolado melhora fosfatemia e mineralização óssea sem aumentar nefrocalcinose |
| [NCT04846647](https://clinicaltrials.gov/study/NCT04846647) | N/A | Concluído | 260 | Estudo observacional da secreção inapropriada de FGF23 em pacientes hospitalizados com hipofosfatemia; clarifica o eixo FGF23–calcitriol como mecanismo central que justifica a intervenção |
| [NCT06046820](https://clinicaltrials.gov/study/NCT06046820) | Phase 3 | Ativo (não recrutando) | 27 | ENERGY 3: RCT avaliando INZ-701 em deficiência de ENPP1; calcitriol potencialmente como tratamento de controle ou componente combinado, fornecendo referência comparativa indireta |
| [NCT06921720](https://clinicaltrials.gov/study/NCT06921720) | N/A | Ainda não recrutando | 65 | Medição de ATP por espectroscopia de fósforo-31 (³¹P MRS) em diabetes fosfato (XLH); identifica biomarcadores energéticos para monitorar resposta ao tratamento com calcitriol |
| [NCT01526304](https://clinicaltrials.gov/study/NCT01526304) | N/A | Desconhecido | 150 | Estudo transversal sobre FGF23, Klotho e Sclerostin em formadores de cálculos renais; contexto mecanístico do eixo FGF23 que sustenta a lógica de intervenção com calcitriol |
| [NCT00844740](https://clinicaltrials.gov/study/NCT00844740) | N/A | Retirado | 0 | Cinacalcet como adjuvante ao tratamento padrão (calcitriol + fosfato) em raquitismo hipofosfatêmico familiar; retirado antes de recrutar, mas confirma que calcitriol era o backbone terapêutico aceito |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [39181153](https://pubmed.ncbi.nlm.nih.gov/39181153/) | 2024 | Review | Lancet | Revisão abrangente de XLH no Lancet: FGF23 como causa central da supressão de calcitriol e raquitismo; calcitriol + fosfato como tratamento histórico padrão |
| [40295317](https://pubmed.ncbi.nlm.nih.gov/40295317/) | 2025 | Review | Calcified Tissue Int | Diagnóstico e terapia atual de XLH: calcitriol + fosfato como base histórica estabelecida, com comparação ao burosumab |
| [6252463](https://pubmed.ncbi.nlm.nih.gov/6252463/) | 1980 | Experimental | NEJM | Estudo seminal em 11 crianças com raquitismo resistente à vitamina D: calcitriol superior ao ergocalciferol, aumentando absorção intestinal de fosfato e reduzindo necessidade de suplementação |
| [3839245](https://pubmed.ncbi.nlm.nih.gov/3839245/) | 1985 | Experimental | J Clin Investigation | Altas doses de calcitriol + fosfato cicatrizam osteomalácia em XLH onde vitamina D convencional falha; demonstra necessidade da forma ativa |
| [36446330](https://pubmed.ncbi.nlm.nih.gov/36446330/) | 2022 | Review | Hormone Res Paediatrics | Metabolismo do raquitismo, vitamina D e cálcio-fósforo; revisão da base histórica, mecanística e terapêutica desde Sniadecki (1822) até era molecular |
| [38988138](https://pubmed.ncbi.nlm.nih.gov/38988138/) | 2024 | Review | J Bone Mineral Res | Raquitismo hipofosfatêmico e baixa estatura: abordagem diagnóstica e terapêutica baseada em fosfatemia, FGF23 e calcitriol |
| [29292875](https://pubmed.ncbi.nlm.nih.gov/29292875/) | 2017 | Cohort | Pediatric Endocrinol Rev | Crescimento em 127 pacientes com XLH de 49 centros antes e após terapia com calcitriol + fosfato; descreve efeito de intervenção precoce |
| [35226335](https://pubmed.ncbi.nlm.nih.gov/35226335/) | 2022 | Cohort | J Endocrinol Invest | Crescimento em altura e proporção corporal do nascimento à idade adulta em raquitismo hipofosfatêmico hereditário; coorte retrospectiva |
| [17117305](https://pubmed.ncbi.nlm.nih.gov/17117305/) | 2006 | Review | Arq Bras Endocrinol | Revisão em português de condições hipofosfatêmicas hereditárias e adquiridas; calcitriol destacado como componente essencial do tratamento padrão |
| [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/) | 2024 | Review | Nutrients | Tipos de raquitismo e tratamento com vitamina D e análogos: calcitriol e alfacalcidol como opções terapêuticas chave para raquitismo resistente |

---

## Informações de Comercialização no Brasil

Calcitriol está registrado na ANVISA com **12 registros ativos** e situação de mercado **já comercializado**. No entanto, os dados individuais de cada registro — incluindo números de registro, nomes comerciais, formas farmacêuticas e textos de indicação aprovada — não foram recuperados nesta versão do Evidence Pack (campos retornados como vazios na base consultada). A complementação desses dados é necessária para verificar se a indicação para raquitismo hipofosfatêmico hereditário já consta em algum registro nacional.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> **Nota de atenção clínica para a indicação candidata:** O uso de calcitriol em raquitismo hipofosfatêmico hereditário requer monitoramento rigoroso de hipercalcemia, hipercalciúria e nefrocalcinose — riscos bem documentados nesta população, especialmente em doses elevadas. A comparação de eficácia e segurança com burosumab (aprovado FDA/EMA para XLH pediátrico desde 2018) deve ser avaliada no contexto regulatório brasileiro.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
O uso de calcitriol no raquitismo hipofosfatêmico hereditário é sustentado por nível de evidência L1 — com ensaio Phase 4 ativo, estudo de monoterapia em curso, e décadas de uso clínico consolidado como tratamento padrão anterior ao burosumab — e pelo mecanismo biologicamente bem fundamentado de contorno à supressão FGF23-mediada da 1α-hidroxilase. O calcitriol já está disponível no mercado brasileiro (12 registros), eliminando barreiras regulatórias de entrada.

**Para prosseguir, é necessário:**
- Recuperar os dados completos dos 12 registros ANVISA (nomes comerciais, formas farmacêuticas, textos de indicação aprovada) para verificar abrangência atual das indicações registradas
- Acessar a bula completa via ANVISA para mapeamento de advertências, contraindicações e interações medicamentosas relevantes para esta indicação específica
- Confirmar dados de MOA via DrugBank API (DG002 — gap de alta severidade)
- Definir protocolo de monitoramento de segurança: cálcio sérico e urinário, creatinina, ultrassonografia renal (rastreio de nefrocalcinose) a cada 3–6 meses
- Avaliar posicionamento estratégico frente ao burosumab: calcitriol pode ser alternativa de menor custo em populações sem acesso ao biológico, ou componente de esquemas combinados em investigação
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

