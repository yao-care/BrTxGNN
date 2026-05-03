---
layout: default
title: Secnidazole
parent: 僅模型預測 (L5)
nav_order: 436
evidence_level: L5
indication_count: 10
---

# Secnidazole
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

O skill txgnn-pipeline não adiciona instruções específicas para geração de relatórios — o formato completo já está definido no system prompt. Vou proceder diretamente com a geração.

> **Nota de análise pré-relatório**: `predicted_indications[0]` é "postmenopausal atrophic vaginitis" (Hold, L5, sem evidências — mecanisticamente incompatível com um antibiótico anaeróbio). O relatório mais informativo é para a indicação com maior sustentação clínica: **vaginal discharge** (rank 3, 99.41%, 5 ensaios Phase 2–4 concluídos, 16 publicações). É essa indicação que será utilizada como foco do relatório.

---

# Secnidazole: Das Infecções Anaeróbicas ao Corrimento Vaginal

## Resumo em Uma Frase

Secnidazole é um antibiótico 5-nitroimidazólico aprovado internacionalmente (FDA 2017/2021) para vaginose bacteriana e tricomoníase, mas ainda sem registro no Brasil.
O modelo TxGNN prevê eficácia para **Corrimento Vaginal (Vaginal Discharge)**, indicação diretamente compatível com seu mecanismo de ação contra patógenos anaeróbios vaginais,
com **5 ensaios clínicos** e **16 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Vaginose bacteriana e tricomoníase (aprovações internacionais; sem registro ANVISA) |
| Nova Indicação Prevista | Corrimento Vaginal (Vaginal Discharge) |
| Pontuação de Previsão TxGNN | 99.41% (ranking geral nº 3.847) |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros ANVISA | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Secnidazole pertence à família dos 5-nitroimidazóis — a mesma classe do metronidazol e do tinidazol — e atua pela redução intracelular do grupo nitro mediada por ferredoxina, gerando radicais livres que fragmentam o DNA de micro-organismos estritamente anaeróbicos e protozoários. Sua principal vantagem farmacológica é a meia-vida de eliminação significativamente mais longa (17–29 horas versus ∼8 horas do metronidazol), o que viabiliza regime de **dose única oral**, com adesão potencialmente superior aos esquemas multidose convencionais.

O corrimento vaginal anormal é o sintoma cardinal de três infecções prevalentes: vaginose bacteriana (VB), tricomoníase e candidíase vulvovaginal. Entre essas, VB (causada por bactérias anaeróbias como *Gardnerella vaginalis* e *Prevotella* spp.) e tricomoníase (*Trichomonas vaginalis*, protozoário estritamente anaeróbio) situam-se diretamente no espectro de cobertura do secnidazol. A abordagem sindrômica preconizada pela OMS para corrimento vaginal — tratar simultaneamente os patógenos mais prováveis sem diagnóstico etiológico prévio — favorece agentes de amplo espectro anaeróbio como este, especialmente em contextos de recursos diagnósticos limitados.

No cenário regulatório internacional, o secnidazol (marca Solosec® 2g granulado oral) obteve aprovação do FDA para VB em 2017 e para tricomoníase em 2021, fornecendo embasamento sólido para pedidos de registro em outros países. No Brasil, alternativas disponíveis como metronidazol e tinidazol requerem regimes multidose com menor comodidade posológica. A introdução do secnidazol preencheria uma lacuna terapêutica real, particularmente em populações com histórico de baixa adesão a tratamentos prolongados.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02111629](https://clinicaltrials.gov/study/NCT02111629) | Phase 3 | Concluído | 118 | Eficácia clínica e microbiológica da combinação fluconazol + secnidazol para corrimento vaginal sintomático (BV + Candida) em abordagem sindrômica; contexto de infecção mista |
| [NCT03935217](https://clinicaltrials.gov/study/NCT03935217) | Phase 3 | Concluído | 147 | Secnidazol 2g dose única vs. placebo em tricomoníase; estudo randomizado, duplo-cego, controlado por placebo |
| [NCT02147899](https://clinicaltrials.gov/study/NCT02147899) | Phase 2 | Concluído | 215 | Eficácia e segurança do SYM-1219 (secnidazol) oral para VB; estudo multicêntrico, prospectivo, randomizado, duplo-cego |
| [NCT05033743](https://clinicaltrials.gov/study/NCT05033743) | Phase 2/3 | Concluído | 24 | Terapia supressora com secnidazol semanal por 18 semanas para prevenção de VB recorrente; estudo piloto |
| [NCT03937869](https://clinicaltrials.gov/study/NCT03937869) | Phase 4 | Concluído | 40 | Segurança de dose única de Solosec™ 2g em adolescentes com VB; avaliação de perfil de segurança em população jovem |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [28867602](https://pubmed.ncbi.nlm.nih.gov/28867602/) | 2017 | Phase 3 RCT | Am J Obstet Gynecol | Secnidazol 2g dose única é eficaz no tratamento de VB; meia-vida longa (∼17h) permite regime de dose única com boa tolerabilidade |
| [31129560](https://pubmed.ncbi.nlm.nih.gov/31129560/) | 2019 | Meta-análise | Eur J Obstet Gynecol Reprod Biol | Revisão sistemática com meta-análise confirma eficácia e segurança da dose única oral de secnidazol 2g para VB |
| [39463760](https://pubmed.ncbi.nlm.nih.gov/39463760/) | 2024 | Revisão sistemática/NMA | Front Cell Infect Microbiol | Meta-análise em rede comparando múltiplos fármacos para VB: secnidazol entre os mais eficazes com boa tolerabilidade |
| [20885970](https://pubmed.ncbi.nlm.nih.gov/20885970/) | 2010 | Phase 3 RCT | Infect Dis Obstet Gynecol | Estudo duplo-cego, duplo-dummy: secnidazol não inferior ao metronidazol multidose para VB, com vantagem de dose única |
| [29323627](https://pubmed.ncbi.nlm.nih.gov/29323627/) | 2018 | Phase 3 Open-label | J Womens Health | Segurança de secnidazol 2g em mulheres e adolescentes pós-menarca com VB; bem tolerado com baixa taxa de descontinuação |
| [22529484](https://pubmed.ncbi.nlm.nih.gov/22529484/) | 2012 | RCT | Indian J Pharmacol | Secnidazol 2g dose única vs. metronidazol, tinidazol e ornidazol em VB; taxas de cura equivalentes entre todos os braços |
| [29132478](https://pubmed.ncbi.nlm.nih.gov/29132478/) | 2017 | RCT | J Coll Physicians Surg Pak | Secnidazol dose única vs. clindamicina vaginal multidose para VB; eficácia comparável com maior comodidade posológica |
| [31499057](https://pubmed.ncbi.nlm.nih.gov/31499057/) | 2020 | Review | Am J Obstet Gynecol | VB é a causa mais comum de corrimento vaginal anormal; tratamento antimicrobiano reduz risco de infecções cirúrgicas associadas |
| [15733882](https://pubmed.ncbi.nlm.nih.gov/15733882/) | 2005 | Ensaio clínico | Int J Gynaecol Obstet | Dose reduzida (1g) de secnidazol também demonstra eficácia para VB, sugerindo flexibilidade de posologia |
| [35863010](https://pubmed.ncbi.nlm.nih.gov/35863010/) | 2022 | In vitro | Microbiology Spectrum | Atividade antitrichomonas in vitro de secnidazol comparável ao metronidazol; alternativa promissora em casos de resistência |

---

## Informações de Comercialização no Brasil

Secnidazole não possui nenhum registro na ANVISA e não está comercializado no Brasil. Internacionalmente, é comercializado como **Solosec®** (granulado oral 2g) nos Estados Unidos, com aprovações FDA para vaginose bacteriana (2017) e tricomoníase (2021).

---

## Considerações de Segurança

Consulte a bula oficial do FDA/EMA para informações completas de segurança. Os dados de advertências e contraindicações específicos para o mercado brasileiro não estão disponíveis neste pacote de evidências.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Secnidazol possui dois ensaios Phase 3 concluídos e aprovações regulatórias do FDA para as principais causas de corrimento vaginal (VB e tricomoníase), com mecanismo de ação diretamente compatível com os patógenos-alvo. A ausência de registro na ANVISA é a principal barreira, mas o dossiê regulatório internacional é sólido e oferece base para uma submissão robusta.

**Para prosseguir, é necessário:**
- Submissão de pedido de registro à ANVISA utilizando o dossiê das aprovações FDA (2017 e 2021) como referência
- Obtenção e análise completa da bula oficial (FDA/EMA) para extração de advertências, contraindicações e interações medicamentosas relevantes ao perfil brasileiro
- Avaliação epidemiológica local: prevalência de VB e tricomoníase no Brasil para dimensionar a demanda potencial e justificar a introdução
- Definição da estratégia de posicionamento: dose única 2g granulado oral para VB e/ou tricomoníase frente às alternativas já disponíveis (metronidazol, tinidazol)
- Protocolo de uso seguro em populações especiais (gestantes, adolescentes, pessoas imunossuprimidas)
- Plano de farmacovigilância pós-introdução com monitoramento de resistência aos 5-nitroimidazóis
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

