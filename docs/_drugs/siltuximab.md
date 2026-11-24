---
layout: default
title: Siltuximab
parent: Apenas Predição do Modelo (L5)
nav_order: 585
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
description: "Siltuximab: nova indicação prevista, Mastocitoma extracutâneo (extracutaneous mastocytoma) (nível de evidência L5). Indicação original: Imunossupressor"
monitor_inn: "siltuximab"
predicted_indications: ["extracutaneous mastocytoma", "hepatic infarction", "hepatic veno-occlusive disease", "peliosis hepatis", "Kaposi's sarcoma (disease)", "autosomal recessive familial Mediterranean fever", "aggressive systemic mastocytosis", "autosomal dominant familial periodic fever"]
---

# Siltuximab
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **8** 
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

## Siltuximabe: De imunossupressor a mastocitoma extracutâneo
{: .text-alpha }

## Resumo em Uma Frase

Siltuximabe (nome comercial SYLVANT) é um anticorpo monoclonal que bloqueia a interleucina-6 (IL-6) e foi registrado na ANVISA com a indicação genérica de "imunossupressor".
O modelo TxGNN prevê que pode ser eficaz para **mastocitoma extracutâneo (extracutaneous mastocytoma)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção específica; a previsão se baseia apenas na pontuação do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Imunossupressor |
| Nova Indicação Prevista | Mastocitoma extracutâneo (extracutaneous mastocytoma) |
| Pontuação de Previsão TxGNN | 0,9964 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 3) |
| Número de Registros | 3 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Siltuximab (tradução não oficial): “Siltuximabe liga-se à IL-6 humana e impede a ligação da IL-6 aos receptores de IL-6 tanto solúveis quanto ligados à membrana. Foi demonstrado que a IL-6 está envolvida em diversos processos fisiológicos normais, como a indução da secreção de imunoglobulinas.” Texto original em inglês: "Siltuximab binds human IL-6 and prevents the binding of IL-6 to both soluble and membrane-bound IL-6 receptors. IL-6 has been shown to be involved in diverse normal physiologic processes such as induction of immunoglobulin secretion." ([DailyMed: Sylvant (siltuximab) prescribing information, Recordati Rare Diseases, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8d663642-f52e-49c0-a023-2da083fdfc0b), versão de 2024-08-27; acessado em 2026-11-19). Segundo informações conhecidas, siltuximabe é um anticorpo monoclonal anti-IL-6, e a IL-6 é uma citocina central em processos inflamatórios e linfoproliferativos.

A IL-6 tem sido associada à proliferação e à sobrevivência de mastócitos, o que cria um vínculo teórico entre o bloqueio dessa via e o mastocitoma extracutâneo. A relação com a indicação original ("imunossupressor") é de natureza ampla: ambas envolvem modulação da resposta imunológica e inflamatória.

Ainda assim, esse vínculo é apenas plausível e não comprovado. Não há ensaios clínicos nem literatura para esta condição rara, e a previsão se apoia somente na pontuação do TxGNN. Outras indicações previstas, como o sarcoma de Kaposi (com uma revisão indireta sobre a doença de Castleman), têm um racional mecanístico comparativamente mais concreto, embora ainda sem evidência direta.

## Considerações sobre Outras Indicações Previstas

| Indicação prevista | Pontuação TxGNN | Nível | Recomendação |
|------|------|------|------|
| Mastocitoma extracutâneo | 0,9964 | L5 | Hold |
| Infarto hepático | 0,9944 | L5 | Hold |
| Doença veno-oclusiva hepática | 0,9940 | L5 | Hold |
| Peliose hepática | 0,9929 | L5 | Hold |
| Sarcoma de Kaposi | 0,9928 | L4 | Questão de pesquisa |
| Febre mediterrânea familiar autossômica recessiva | 0,9922 | L5 | Hold |
| Mastocitose sistêmica agressiva | 0,9916 | L5 | Hold |
| Febre periódica familiar autossômica dominante | 0,9905 | L5 | Hold |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Para a indicação principal (mastocitoma extracutâneo), atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 171260007 | SYLVANT | RECORDATI RARE DISEASES COMÉRCIO DE MEDICAMENTOS L | Ativo |
| 112363411 | SYLVANT | JANSSEN-CILAG FARMACÊUTICA LTDA | Cancelado |
| 151890004 | SYLVANT | COLLECT IMPORTAÇÃO E COMÉRCIO LTDA | Cancelado |

<!-- licenses:end -->

## Considerações de Segurança

- **Interações Medicamentosas**: foram identificadas 139 interações no total. Exemplos de destaque:
  - **Maior gravidade**: deferiprona.
  - **Moderada**: sinvastatina, apixabana, varfarina, rivaroxabana, dicumarol, lidocaína, hidrocodona, teofilina, aminofilina, oxtrifilina, roflumilaste, tacrolimo, fentanila, nifedipino e toxoide tetânico.
  - **Menor**: sais de zinco (sulfato, acetato, gluconato e cloreto).

  Muitas das interações moderadas envolvem substratos de enzimas do citocromo P450, cuja expressão pode ser normalizada quando a IL-6 é bloqueada, alterando as concentrações desses fármacos. Esse ponto deve ser confirmado na bula.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão para mastocitoma extracutâneo tem pontuação alta no modelo, mas nenhuma evidência clínica ou da literatura (nível L5).

<!-- review:begin br-lic-20261106-siltuximab-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “A previsão para mastocitoma extracutâneo tem pontuação alta no modelo, mas nenhuma evidência clínica ou da literatura (nível L5). Além disso, o único registro na ANVISA está cancelado e faltam dados de segurança da bula.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Os números atualizados de registros estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-siltuximab-2 -->

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança
- Complementar os dados do mecanismo de ação a partir do DrugBank
- Fazer busca sistemática de ensaios clínicos e literatura sobre IL-6 e mastocitoma/mastocitose
- Esclarecer a situação regulatória e a viabilidade de acesso ao produto no Brasil
- Avaliar prioritariamente o sarcoma de Kaposi (L4) como alternativa com racional mecanístico mais sólido, associado à doença de Castleman multicêntrica relacionada ao KSHV

<!-- review:begin br-lic-20261031-siltuximab-1 -->

> **Correção de verificação (2026-10-31)**: Texto original: “Esclarecer a situação regulatória (registro cancelado) e a viabilidade de acesso ao produto no Brasil” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-10-31). Os números atualizados de registros estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261031-siltuximab-1 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-10-31 | Removido: “(registro cancelado)” | Corrigido (revisado em 2026-11-24; versão anterior guardada no registro) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “Além disso, o único registro na ANVISA está cancelado e faltam dados de segurança da bula” | Corrigido (revisado em 2026-11-24; versão anterior guardada no registro) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Sylvant (siltuximab) prescribing information, Recordati Rare Diseases, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8d663642-f52e-49c0-a023-2da083fdfc0b) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

