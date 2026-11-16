---
layout: default
title: Atezolizumabe
parent: Apenas Predição do Modelo (L5)
nav_order: 85
evidence_level: L5
indication_count: 6
drugbank_id: DB11595
monitor_inn: "Atezolizumab"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-11-16
description: "Atezolizumabe: nova indicação prevista, Uterine ligament adenocarcinoma (nível de evidência L5). Indicação original: Não consta nos dados locais"
---

# Atezolizumabe
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **6** 
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

## Atezolizumabe: Uterine ligament adenocarcinoma
{: .text-alpha }

## Resumo em Uma Frase

Atezolizumabe é um anticorpo monoclonal que bloqueia o PD-L1, usado em oncologia e com registro ativo no Brasil.
O modelo TxGNN prevê que ele pode ser eficaz para **Carcinoma urotelial da uretra prostática (prostatic urethra urothelial carcinoma)**.
Essa previsão conta hoje com **1 ensaio clínico** de fase inicial, que não é específico para esta doença, e **nenhuma publicação** diretamente relacionada.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Uterine ligament adenocarcinoma |
| Pontuação de Previsão TxGNN | 0.9993 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação compilados para este relatório. Atezolizumabe é um anticorpo anti-PD-L1. Esse tipo de fármaco impede que o tumor use a via PD-L1/PD-1 para "desligar" os linfócitos T. Com isso, o sistema imune pode voltar a atacar as células tumorais.

O carcinoma urotelial da uretra prostática tem a mesma histologia urotelial dos tumores de bexiga e do trato urinário superior. Esses tumores compartilham a biologia da via PD-L1/PD-1, o que torna a plausibilidade biológica alta. Por isso, a pontuação elevada do modelo é coerente com o mecanismo.

Essa plausibilidade, porém, é uma inferência. Nenhum estudo compilado testou o atezolizumabe especificamente nesta localização. O único ensaio identificado é um estudo de fase 1b com várias neoplasias, no qual o atezolizumabe é usado em combinação com outro fármaco.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Fase 1 | Ativo, sem recrutamento | 914 | Estudo de fase 1b, aberto e multicêntrico, de escalonamento de dose. Avalia cabozantinibe isolado ou combinado com atezolizumabe em tumores sólidos avançados ou metastáticos, incluindo coortes de carcinoma urotelial (bexiga, pelve renal, ureter e uretra). Mede segurança, tolerabilidade, eficácia preliminar e farmacocinética. Conclusão prevista para setembro de 2027. |

Este estudo usa uma combinação de fármacos, então a contribuição isolada do atezolizumabe não pode ser separada. Ele também é de fase inicial e não é específico da uretra prostática.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Detentor | Situação |
|---------|------|------|-----------|
| Registro 101000665 | TECENTRIQ | Produtos Roche Químicos e Farmacêuticos S.A. | Válido |

## Citotoxicidade

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Imunoterapia (anticorpo anti-PD-L1) |
| Risco de Mielossupressão | Consulte as advertências e precauções na bula |
| Classificação de Emetogenicidade | Consulte as advertências e precauções na bula |
| Itens de Monitoramento | Consulte as advertências e precauções na bula |
| Proteção no Manuseio | Consulte as advertências e precauções na bula |

## Considerações de Segurança

Consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- O único ensaio é de fase 1b, em combinação e com várias neoplasias. Por isso, o nível de evidência é L5.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), pois os dados de segurança locais estão ausentes e isso bloqueia a triagem de segurança.
- Complementar os dados do mecanismo de ação a partir de uma fonte como o DrugBank.
- Buscar estudos clínicos ou séries de casos que incluam especificamente tumores uroteliais da uretra prostática tratados com atezolizumabe.
- Obter os resultados de eficácia da coorte urotelial do estudo NCT03170960 quando forem divulgados, para avaliar o sinal nesta localização.

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “No entanto, os detalhes do registro (número, nome comercial, forma farmacêutica e indicação aprovada) **não estão disponíveis** no Evidence ” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “os detalhes do registro regulatório estão vazios” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “(ANVISA/TFDA)” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

