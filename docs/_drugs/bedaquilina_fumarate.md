---
layout: default
title: Bedaquilina Fumarate
parent: Apenas Predição do Modelo (L5)
nav_order: 110
evidence_level: L5
indication_count: 4
drugbank_id: DB08903
monitor_inn: "Bedaquiline"
predicted_indications: ["vulvovaginal candidiasis", "fascioliasis", "urea cycle disorder", "esophageal candidiasis"]
last_modified_at: 2026-11-24
description: "Bedaquilina Fumarate: nova indicação prevista, candidíase vulvovaginal (vulvovaginal candidiasis) (nível de evidência L5). Indicação original: OUTROS MEDICAMENTOS USADOS NO TRATAMENTO DA TUBERCULOSE"
---

# Bedaquilina Fumarate
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

## Bedaquilina Fumarate: candidíase vulvovaginal (vulvovaginal candidiasis)
{: .text-alpha }

## Resumo em Uma Frase

Bedaquilina fumarato é um medicamento antimicobacteriano, registrado no Brasil como SIRTURO e utilizado no tratamento da tuberculose.
O modelo TxGNN prevê que pode ser eficaz para **candidíase vulvovaginal (vulvovaginal candidiasis)**, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | OUTROS MEDICAMENTOS USADOS NO TRATAMENTO DA TUBERCULOSE |
| Nova Indicação Prevista | candidíase vulvovaginal (vulvovaginal candidiasis) |
| Pontuação de Previsão TxGNN | 0.9988 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo as seções “Mechanism of Action” e “Microbiology” da bula aprovada pela FDA dos EUA (Prescribing Information) para Bedaquilina Fumarate (tradução não oficial): “A bedaquilina é um fármaco antimicobacteriano da classe das diarilquinolinas. […] SIRTURO é um fármaco antimicobacteriano da classe das diarilquinolinas que inibe a ATP (adenosina 5'-trifosfato) sintase micobacteriana, ligando-se à subunidade c da enzima, que é essencial para a geração de energia em M. tuberculosis.” Texto original em inglês: "Bedaquiline is a diarylquinoline antimycobacterial drug. […] SIRTURO is a diarylquinoline antimycobacterial drug that inhibits mycobacterial ATP (adenosine 5'- triphosphate) synthase, by binding to subunit c of the enzyme that is essential for the generation of energy in M. tuberculosis." ([DailyMed: Sirturo (bedaquiline fumarate) prescribing information, Janssen Products, LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1534c9ae-4948-4cf4-9f66-222a99db6d0e), versão de 2025-10-17; acessado em 2026-11-19). Sabe-se, pela análise disponível, que a bedaquilina inibe a ATP sintase micobacteriana (subunidade c do domínio F0), alvo específico de micobactérias.

Não há vínculo estabelecido entre esse mecanismo e a biologia de *Candida*. A ATP sintase fúngica difere estruturalmente da micobacteriana, de modo que qualquer atividade antifúngica seria especulativa. A pontuação elevada do TxGNN é apenas uma previsão computacional, sem estudos que a sustentem.

Além disso, já existem opções antifúngicas eficazes e bem estabelecidas (azóis). Como a bedaquilina traz advertências de prolongamento do intervalo QT e hepatotoxicidade, a relação risco-benefício para esse reposicionamento é pouco favorável.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

<!-- licenses:begin -->

| Registro | Produto | Situação |
|------|------|------|
| 112363422 | SIRTURO | Ativo |

<!-- licenses:end -->

## Considerações de Segurança

Consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão para candidíase vulvovaginal baseia-se apenas na pontuação do modelo, sem ensaios clínicos nem publicações, e não há plausibilidade mecanística clara. Existem tratamentos eficazes disponíveis, o que reduz a necessidade de priorizar este reposicionamento.

**Para prosseguir, é necessário:**
- Testes de sensibilidade antifúngica in vitro contra espécies de *Candida*, como etapa mínima inicial
- Dados detalhados do mecanismo de ação (MOA) a partir de fonte especializada
- Bula da ANVISA com advertências e contraindicações, para triagem de segurança (incluindo QT e hepatotoxicidade)
- Avaliação da compatibilidade de vias de administração, já que o uso sistêmico da bedaquilina pode não ser adequado para uma infecção localizada

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Ausência de registro regulatório** O fármaco não possui registros ativos na base regulatória consultada (total de registros: 0)” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido (revisado em 2026-11-12; versão anterior guardada no registro)) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “(TFDA/ANVISA/EMA)” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Sirturo (bedaquiline fumarate) prescribing information, Janssen Products, LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1534c9ae-4948-4cf4-9f66-222a99db6d0e) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

