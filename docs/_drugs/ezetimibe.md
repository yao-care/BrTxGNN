---
layout: default
title: Ezetimibe
parent: 僅模型預測 (L5)
nav_order: 248
evidence_level: L5
indication_count: 4
---

# Ezetimibe
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

# Ezetimibe: Da Hipercolesterolemia à Hiperlipoproteinemia

## Resumo em Uma Frase

Ezetimibe é um inibidor seletivo da absorção intestinal de colesterol, estabelecido globalmente para o tratamento de hipercolesterolemia e dislipidemias, amplamente utilizado em combinação com estatinas.
O modelo TxGNN prevê que pode ser eficaz para **Hiperlipoproteinemia (Hyperlipoproteinemia)**, com suporte de **múltiplos ensaios clínicos de Fase 3** e **19 publicações** indexadas — consolidando uma indicação com forte base científica internacional que, no entanto, ainda não possui registro ativo no Brasil.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hipercolesterolemia / dislipidemia (uso global estabelecido, sem registro brasileiro) |
| Nova Indicação Prevista | Hiperlipoproteinemia (Hyperlipoproteinemia) |
| Pontuação de Previsão TxGNN | 99,63% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Ezetimibe atua mediante inibição seletiva da proteína NPC1L1 (Niemann-Pick C1-Like 1), localizada na borda em escova do enterócito intestinal. Ao bloquear esta proteína transportadora, o fármaco impede a absorção de colesterol exógeno (dietético e biliar) e de fitoesteróis, reduzindo o aporte de colesterol ao fígado. Como resposta compensatória, o fígado upregula os receptores de LDL, aumentando a captação de LDL-C circulante e reduzindo seus níveis séricos em média 15–25%. Este mecanismo é complementar ao das estatinas — que inibem a síntese hepática de colesterol via HMG-CoA redutase —, razão pela qual a combinação é padrão em diretrizes internacionais.

A hiperlipoproteinemia compreende um espectro de distúrbios do metabolismo das lipoproteínas, incluindo hipercolesterolemia primária (tipo IIa), hiperlipidemia mista (tipo IIb) e formas genéticas como a hipercolesterolemia familiar. O mecanismo de ação do ezetimibe é diretamente aplicável a todo este espectro: ao reduzir o influxo intestinal de colesterol, o fármaco diminui a disponibilidade de substrato para a montagem de lipoproteínas aterogênicas, independentemente da causa primária da dislipidemia — seja ela dietética, genética ou secundária a outras condições.

A previsão do TxGNN é altamente consistente com décadas de evidências clínicas globais. Ezetimibe está aprovado em mais de 70 países sob marcas como Zetia® e, em combinação com sinvastatina, Vytorin®. O escore de 99,63% reflete a robustez da conexão mecanística e epidemiológica no grafo de conhecimento. A ausência de registro no Brasil não reflete falta de evidências, mas sim uma lacuna regulatória que representa a principal barreira para progressão.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT00704444](https://clinicaltrials.gov/study/NCT00704444) | Pós-comercialização | Concluído | 11.332 | Investigação pós-aprovação do Japão (Zetia® 10mg): avalia segurança e eficácia de ezetimibe em monoterapia e combinação para hiperlipoproteinemia na prática clínica real ao longo de 12 semanas |
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Fase 3 | Concluído | 611 | RCT avaliando Ezetimibe/Sinvastatina + Fenofibrate em hiperlipidemia mista (colesterol e triglicerídeos elevados); demonstra eficácia do ezetimibe na melhora do perfil lipídico completo |
| [NCT00704535](https://clinicaltrials.gov/study/NCT00704535) | Pós-comercialização | Concluído | 4.105 | Vigilância pós-comercialização nas Filipinas: avalia segurança, tolerabilidade e eficácia do ezetimibe em monoterapia ou combinação com estatina em pacientes com hipercolesterolemia |
| [NCT00092560](https://clinicaltrials.gov/study/NCT00092560) | Fase 3 | Concluído | 587 | RCT comparando fenofibrate + ezetimibe vs. componentes isolados em hiperlipidemia mista; avalia redução de LDL-C e triglicerídeos em combinação terapêutica |
| [NCT00268697](https://clinicaltrials.gov/study/NCT00268697) | Fase 3 | Concluído | 1.267 | Lapaquistat 100mg ± ezetimibe 10mg vs. ezetimibe 10mg em dislipidemia primária; demonstra ezetimibe como comparador ativo de referência em ensaios de novos agentes hipolipemiantes |
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Fase 3 | Concluído | 1.220 | RCT duplo-cego de Ezetimibe/Sinvastatina + Niacina (liberação prolongada) em hiperlipidemia tipo IIa e IIb; avalia eficácia e segurança da terapia combinada em múltiplos alvos lipídicos |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Fase 3 | Concluído | 720 | ENHANCE Trial: ezetimibe + sinvastatina em alta dose vs. sinvastatina isolada em hipercolesterolemia familiar heterozigótica; avalia progressão aterosclerótica carotídea |
| [NCT04929249](https://clinicaltrials.gov/study/NCT04929249) | Fase 3 | Concluído | 450 | VICTORION-INITIATE: estratégia "inclisiran first" vs. tratamento usual (incluindo ezetimibe) em ASCVD com LDL-C elevado; ezetimibe posicionado como padrão de cuidado no braço controle |
| [NCT00704535](https://clinicaltrials.gov/study/NCT00704535) | Pós-comercialização | Concluído | 4.105 | Vigilância pós-comercialização nas Filipinas: avalia segurança, tolerabilidade e eficácia do ezetimibe em monoterapia ou combinação com estatina em pacientes com hipercolesterolemia |
| [NCT00652431](https://clinicaltrials.gov/study/NCT00652431) | Fase 1 | Concluído | 18 | Estudo cruzado de interação farmacocinética bidirecional entre Vytorin® (Ezetimibe+Sinvastatina) e Niaspan® (Niacina de liberação prolongada); fornece dados de segurança de combinação terapêutica |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | Phase 3 RCT | Lancet | TANDEM: combinação obicetrapib + ezetimibe em dose fixa reduziu significativamente LDL-C em HeFH e ASCVD; comprova o papel central do ezetimibe como componente em terapias combinadas de nova geração |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | Phase 3 RCT | JAMA | Enlicitide (inibidor oral de PCSK9) em HeFH; ezetimibe como terapia de base estabelecida, demonstrando sua posição consolidada na escada terapêutica da hiperlipoproteinemia |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | Guideline / Epidemiologia | European Heart Journal | Consenso da Sociedade Europeia de Aterosclerose: FH subdiagnosticada e subtratada; ezetimibe recomendado como terapia de segunda linha após estatinas para controle de LDL-C em hiperlipoproteinemia familiar |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Review | Cardiology Clinics | Revisão abrangente de FH: ezetimibe listado como tratamento estabelecido capaz de reduzir LDL-C e prevenir eventos cardiovasculares em pacientes com hiperlipoproteinemia familiar e não familiar |
| [34480646](https://pubmed.ncbi.nlm.nih.gov/34480646/) | 2021 | Review | Current Cardiology Reports | Revisão global de FH: ezetimibe como opção terapêutica-chave em combinação com estatinas; discute estratégias para atingir metas de LDL-C em diferentes subtipos de hiperlipoproteinemia |
| [38599725](https://pubmed.ncbi.nlm.nih.gov/38599725/) | 2024 | Review | Indian Heart Journal | Revisão de FH em população indiana; ezetimibe recomendado para tratamento combinado e rastreamento precoce; relevante para populações asiáticas com perfil lipídico distinto |
| [29219151](https://pubmed.ncbi.nlm.nih.gov/29219151/) | 2017 | Review | Nature Reviews Disease Primers | Primer sobre FH: ezetimibe discutido como terapia complementar que reduz LDL por via independente dos receptores de LDL, mecanisticamente relevante para toda a gama de hiperlipoproteinemias |
| [37762244](https://pubmed.ncbi.nlm.nih.gov/37762244/) | 2023 | Review | Int J Mol Sci | Hiperlipidemia pós-prandial: patofisiologia e tratamentos; ezetimibe abordado como agente para redução da absorção intestinal de colesterol e melhora do perfil lipídico pós-prandial |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Review | Molecular Medicine Reports | Revisão de fármacos atuais para hiperlipidemia; ezetimibe posicionado como tratamento de segunda linha estabelecido com mecanismo complementar às estatinas no contexto global das dislipidemias |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Review | J Cardiovascular Pharmacology & Therapeutics | Revisão abrangente de inibidores de PCSK9; ezetimibe descrito como padrão de cuidado para pacientes intolerantes a estatinas ou sem controle adequado de LDL-C em hiperlipoproteinemia |

---

## Informações de Comercialização no Brasil

O Ezetimibe **não possui nenhum registro ativo na ANVISA** (Agência Nacional de Vigilância Sanitária). A consulta ao banco de dados regulatório brasileiro retornou zero registros de comercialização.

> **Nota regulatória:** Internacionalmente, ezetimibe é comercializado sob diversas marcas — incluindo Zetia® (monoterapia 10mg) e Vytorin®/Ezetrol® (combinação com sinvastatina) — com aprovações ativas nos EUA (FDA), Europa (EMA), Japão (PMDA) e Filipinas, entre outros. A ausência completa de registro no Brasil representa uma lacuna regulatória relevante, dado o alto impacto das dislipidemias na morbimortalidade cardiovascular da população brasileira.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Ezetimibe possui nível de evidência L1 consolidado para hiperlipoproteinemia, com múltiplos ensaios clínicos de Fase 3 concluídos, diretrizes internacionais favoráveis e décadas de uso seguro. A principal barreira ao avanço no Brasil é inteiramente regulatória — a ausência de registro na ANVISA —, e não científica, o que torna a progressão viável mediante estratégia regulatória adequada.

**Para prosseguir, é necessário:**
- Iniciar processo de registro regulatório junto à ANVISA com dossiê completo de eficácia, segurança e qualidade (referenciado em aprovações internacionais como FDA e EMA)
- Obter e revisar a bula completa com advertências, contraindicações e interações medicamentosas para o mercado brasileiro
- Completar a análise de MOA com dados do DrugBank (lacuna identificada como DG002 no Evidence Pack)
- Obter advertências e contraindicações oficiais da bula brasileira ou internacional (lacuna DG001)
- Definir estratégia de entrada no mercado: produto isolado (Ezetimibe 10mg) e/ou combinação em dose fixa (Ezetimibe/Sinvastatina ou Ezetimibe/Rosuvastatina), conforme necessidades do mercado local
- Avaliar viabilidade de acesso via SUS, considerando custo-efetividade frente às estatinas genéricas disponíveis no Brasil
---

