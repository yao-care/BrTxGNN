---
layout: default
title: Neratinib
parent: Apenas Predição do Modelo (L5)
nav_order: 468
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Neratinib: nova indicação prevista, Câncer de mama positivo para receptor de progesterona (progesterone-r… (nível de evidência L5). Indicação original: Agentes antineoplásicos"
---

# Neratinib
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **4** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Relatório de avaliação farmacêutica

</div>

## Neratinibe: De agente antineoplásico a câncer de mama positivo para receptor de progesterona
{: .text-alpha }

## Resumo em Uma Frase

Neratinibe (NERLYNX) é um inibidor de tirosina quinase originalmente classificado como agente antineoplásico no registro da ANVISA.
O modelo TxGNN prevê que pode ser eficaz para **câncer de mama positivo para receptor de progesterona (progesterone-receptor positive breast cancer)**,
atualmente com **2 ensaios clínicos** (um recrutando e um retirado) e **12 publicações** apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Agentes antineoplásicos |
| Nova Indicação Prevista | Câncer de mama positivo para receptor de progesterona (progesterone-receptor positive breast cancer) |
| Pontuação de Previsão TxGNN | 99,68% |
| Nível de Evidência | L1 (com ressalvas: o ensaio de Fase 3 ExteNET é em câncer de mama HER2-positivo, não em todo câncer RP-positivo) |
| Situação no Mercado Brasileiro | Apenas registros cancelados |
| Número de Registros | 1 |
| Decisão Recomendada | Proceed with Guardrails |

> Observação: o modelo previu outras indicações de mama com pontuações semelhantes (RP-negativo, 99,67%; luminal A ou B, 99,67%; subtipo "normal-like", 99,68%). Este relatório foca na indicação de maior ordem com evidências clínicas diretas, a de RP-positivo. Os demais subtipos são comentados na conclusão.

## Por que Esta Previsão é Razoável?

Neratinibe é um inibidor de tirosina quinase irreversível pan-HER, que atua sobre EGFR (HER1), HER2 e HER4. Ao bloquear esses receptores, interrompe as vias de sinalização a jusante PI3K/AKT e MAPK, que sustentam o crescimento tumoral. Não há dados detalhados de mecanismo de ação no registro estruturado do fármaco; a descrição acima baseia-se na literatura compilada para este relatório.

A indicação original (antineoplásico) e a nova indicação (câncer de mama RP-positivo) são ambas oncológicas. Nos tumores com receptores hormonais positivos e HER2 positivo, há comunicação cruzada entre a sinalização de HER2 e a do receptor de estrogênio, que contribui para a resistência à terapia endócrina. Inibir HER2 pode, portanto, restaurar a sensibilidade ao tratamento hormonal.

Atenção: isto é, na prática, uma indicação oncológica já existente, e não um reposicionamento genuíno. A evidência vale para doença HER2-positiva e não para qualquer câncer RP-positivo. O subgrupo HR-positivo foi o que mais se beneficiou no ExteNET.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Phase 2 | Recrutando | 30 | Neratinibe + inibidor de aromatase + trastuzumabe por 24 semanas antes da cirurgia em câncer de mama inicial ER+/HER2+; resultados ainda não disponíveis |
| [NCT04901299](https://clinicaltrials.gov/study/NCT04901299) | Phase 2 | Retirado | 0 | Fulvestranto + neratinibe em câncer de mama metastático HR+/HER2- previamente tratado; retirado sem inclusão de participantes, sem evidência gerada |

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | RCT (Fase 3) | Lancet Oncol | ExteNET: 12 meses de neratinibe após terapia adjuvante com trastuzumabe em câncer de mama inicial HER2-positivo |
| [27406346](https://pubmed.ncbi.nlm.nih.gov/27406346/) | 2016 | RCT (Fase 2 adaptativo) | N Engl J Med | I-SPY 2: neratinibe neoadjuvante associado à quimioterapia padrão em câncer de mama de alto risco |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Diretriz | J Clin Oncol | Atualização da diretriz ASCO para terapia sistêmica do câncer de mama avançado HER2-positivo |
| [29784737](https://pubmed.ncbi.nlm.nih.gov/29784737/) | 2018 | Diretriz | J Natl Compr Canc Netw | Atualização das diretrizes NCCN para câncer de mama, incluindo duração estendida da terapia endócrina |
| [39153126](https://pubmed.ncbi.nlm.nih.gov/39153126/) | 2024 | Coorte | Breast Cancer Res Treat | Padrões de uso e tolerância do neratinibe adjuvante em HR+/HER2+; efeitos gastrointestinais frequentemente levam à descontinuação |
| [41499317](https://pubmed.ncbi.nlm.nih.gov/41499317/) | 2026 | Coorte | Oncology | Tendências de prescrição do neratinibe adjuvante na prática atual, após o ExteNET (anterior ao uso de pertuzumabe e T-DM1) |
| [32139271](https://pubmed.ncbi.nlm.nih.gov/32139271/) | 2020 | Revisão | Clin Breast Cancer | Discussão de especialistas sobre avanços clínicos no câncer de mama HER2-positivo |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Revisão | Future Oncol | Tendências no tratamento de HR+/HER2+; combinação hormonal + anti-HER2 pode controlar a doença a longo prazo |
| [41886605](https://pubmed.ncbi.nlm.nih.gov/41886605/) | 2026 | Pré-clínico | Cancer Res | BRD8/EP400 como módulo de cromatina mediador da resposta anti-HER2 em HR+/HER2+ |
| [35251981](https://pubmed.ncbi.nlm.nih.gov/35251981/) | 2022 | Relato de caso | Front Oncol | Piotinibe + vinorelbina metronômica em câncer de mama HER2+ com doença leptomeníngea |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 139000004 (cancelado) | NERLYNX | Não informada | Agentes antineoplásicos |

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia alvo (inibidor de tirosina quinase pan-HER) |
| Risco de Mielossupressão | Consulte as advertências e precauções na bula |
| Classificação de Emetogenicidade | Consulte as advertências e precauções na bula |
| Itens de Monitoramento | Função hepática, além de acompanhamento clínico de diarreia e hidratação/eletrólitos |
| Proteção no Manuseio | Consulte as advertências e precauções na bula |

## Considerações de Segurança

- **Interações Medicamentosas**: foram registradas 181 interações. Entre as principais, de gravidade **maior**: famotidina, ranitidina, cimetidina, omeprazol, esomeprazol, lansoprazol, dexlansoprazol, rabeprazol (redutores de acidez gástrica), aprepitanto, dexametasona, claritromicina e clotrimazol. De gravidade **moderada**: loperamida, óxido de magnésio, hidróxido de alumínio, carbonato de cálcio, empagliflozina e naldemedina. De gravidade **menor**: naloxegol e fidaxomicina.
- **Eventos adversos relevantes (literatura)**: efeitos gastrointestinais significativos, principalmente diarreia, são frequentes e muitas vezes levam à interrupção do tratamento. Recomenda-se profilaxia da diarreia.

Para as demais informações de segurança (advertências e contraindicações), consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
- O ExteNET (Fase 3 randomizado) e as diretrizes NCCN/ASCO sustentam o uso do neratinibe em câncer de mama HER2-positivo, com maior benefício no subgrupo HR-positivo. Porém, a evidência não se estende ao câncer RP-positivo em geral, e os ensaios diretamente ligados são pequenos, em andamento ou retirados.

**Para prosseguir, é necessário:**
- Restringir o uso a doença HER2-positiva (ou HER2-mutada, com base nos dados do SUMMIT) e confirmar o status de HER2.
- Obter a bula da ANVISA (advertências e contraindicações), pois esses dados estão ausentes e bloqueiam a triagem de segurança.
- Esclarecer a situação regulatória: o único registro no Brasil está cancelado, e é preciso reconciliá-la com a região de uso pretendida.
- Implementar profilaxia da diarreia e revisar as interações (CYP3A4/gp-P e agentes redutores de acidez gástrica, sobretudo inibidores de bomba de prótons e antagonistas H2).
- Obter dados do mecanismo de ação a partir do DrugBank.
- Acompanhar os resultados do NCT04886531.

**Observações sobre as demais previsões:**
- **RP-negativo** (99,67%): evidência indireta (ensaios em HR-positivo); mesmas ressalvas de uso restrito a HER2-positivo.
- **Luminal A ou B** (99,67%): sem ensaios registrados; evidência de Fase 2 (SUMMIT, plasmaMATCH) apenas em doença selecionada por biomarcador (HER2-mutada). Classificada como questão de pesquisa.
- **Subtipo "normal-like"** (99,68%): apenas previsão do modelo (L5), sem ensaios nem literatura, e com justificativa mecanística fraca por ser tipicamente HER2-baixo ou negativo. Decisão: Hold.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

