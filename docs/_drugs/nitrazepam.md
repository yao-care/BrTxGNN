---
layout: default
title: Nitrazepam
parent: 僅模型預測 (L5)
nav_order: 360
evidence_level: L5
indication_count: 3
---

# Nitrazepam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Using `txgnn-pipeline` to confirm context. Now generating the report from the Evidence Pack.

---

# Nitrazepam: De hipnótico benzodiazepínico ao distúrbio de início e manutenção do sono

## Resumo em Uma Frase

Nitrazepam é um benzodiazepínico clássico, amplamente reconhecido por sua ação hipnótico-sedativa no sistema nervoso central via modulação do receptor GABA-A.
O modelo TxGNN prevê que pode ser eficaz para o **Distúrbio de Início e Manutenção do Sono (sleep disorder, initiating and maintaining sleep)**,
atualmente com **0 ensaios clínicos registrados** e **20 publicações** apoiando esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Dados regulatórios individuais não disponíveis no dataset atual (hipnótico benzodiazepínico) |
| Nova Indicação Prevista | Distúrbio de Início e Manutenção do Sono (sleep disorder, initiating and maintaining sleep) |
| Pontuação de Previsão TxGNN | 99,89% |
| Nível de Evidência | L1 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 20 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Nitrazepam é um benzodiazepínico da classe das 1,4-benzodiazepinas que atua como modulador alostérico positivo do receptor GABA-A no sítio das benzodiazepinas. Esse mecanismo potencia a neurotransmissão inibitória mediada pelo GABA, produzindo sedação central e resultando em encurtamento da latência do sono e melhora da manutenção do sono ao longo da noite — com redução dos despertares noturnos.

A relação entre o mecanismo de ação e a indicação prevista é direta e farmacologicamente coerente: a potenciação gabaérgica atua exatamente sobre os substratos neurais responsáveis pelo distúrbio de início e manutenção do sono. Estudos clínicos comparativos históricos demonstraram eficácia de Nitrazepam 5 mg em populações geriátricas hospitalizadas, com qualidade e quantidade de sono comparáveis a outros hipnóticos benzodiazepínicos como triazolam e brotizolam, o que sustenta a coerência da previsão do modelo.

A elevada pontuação TxGNN (99,89%) reflete essa correspondência mecanística direta — o modelo captura a associação entre modulação GABA-A e melhora do sono como um caminho farmacológico de alta confiança. A literatura disponível abrange desde estudos farmacocinéticos e ensaios controlados randomizados históricos até revisões sistemáticas recentes sobre o papel dos benzodiazepínicos no manejo da insônia.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [6135296](https://pubmed.ncbi.nlm.nih.gov/6135296/) | 1983 | RCT (duplo-cego cruzado) | Acta Psychiatrica Scandinavica | Nitrazepam 5 mg vs. triazolam 0,25 mg em 26 pacientes geriátricos internados; qualidade e quantidade de sono similares entre os dois hipnóticos sem diferenças significativas em testes psicomotores |
| [4892037](https://pubmed.ncbi.nlm.nih.gov/4892037/) | 1969 | Estudo Clínico | British Medical Journal | Nitrazepam em sobredosagem aguda (até 80 comprimidos) sem efeitos graves além de sonolência; ensaio duplo-cego em enfermaria médica geral confirmando eficácia hipnótica equivalente ao butobarbital |
| [32724021](https://pubmed.ncbi.nlm.nih.gov/32724021/) | 2020 | Revisão de ECR | The Medical Letter on Drugs and Therapeutics | Avaliação do lemborexanto (Dayvigo) para insônia com referências comparativas a benzodiazepínicos hipnóticos, incluindo Nitrazepam, como padrão de classe |
| [7037262](https://pubmed.ncbi.nlm.nih.gov/7037262/) | 1981 | Estudo Farmacocinético | Clinical Pharmacokinetics | Caracterização da farmacocinética clínica de Nitrazepam; dados de absorção, distribuição e eliminação relevantes para racionalização de dose e intervalo de administração |
| [1125532](https://pubmed.ncbi.nlm.nih.gov/1125532/) | 1975 | Série de Casos / Segurança | British Journal of Psychiatry | Relato de dependência a Nitrazepam (Mogadon); alerta para potencial de abuso com uso prolongado como hipnótico |
| [19450355](https://pubmed.ncbi.nlm.nih.gov/19450355/) | 2007 | Revisão | BMJ Clinical Evidence | Insônia em idosos: prevalência de até 40% em adultos; fatores de risco (estresse, ronco diurno, hiperexcitação) e opções de tratamento farmacológico e não farmacológico |
| [238826](https://pubmed.ncbi.nlm.nih.gov/238826/) | 1975 | Revisão | Drugs | Fisiologia e patologia do sono; ciclos NREM/REM e critérios para avaliação de eficácia de hipnóticos, incluindo benzodiazepínicos |
| [7725291](https://pubmed.ncbi.nlm.nih.gov/7725291/) | 1995 | Revisão | Tidsskrift for den Norske Laegeforening | Classificação, diagnóstico e tratamento da insônia; necessidade de consenso diagnóstico universal e discussão de hipnóticos disponíveis |
| [39231170](https://pubmed.ncbi.nlm.nih.gov/39231170/) | 2024 | Estudo Observacional | PLoS ONE | Padrões de consumo e fatores associados à prescrição inapropriada de benzodiazepínicos na atenção primária; risco de dependência, tolerância e declínio cognitivo, especialmente em idosos |
| [20467592](https://pubmed.ncbi.nlm.nih.gov/20467592/) | 2010 | Revisão | Drugs of Today | Antagonistas 5-HT2A no tratamento da insônia; benzodiazepínicos (incluindo Nitrazepam) como comparadores de referência para eficácia em indução e manutenção do sono |

---

## Informações de Comercialização no Brasil

Os dados individuais de cada registro (número de registro, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis no conjunto de dados extraído. O sistema confirma **20 registros ativos** de Nitrazepam na base regulatória brasileira com situação **Comercializado**.

> Para consultar os registros individuais, acesse o portal da ANVISA: [consultas.anvisa.gov.br](https://consultas.anvisa.gov.br)

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

> Nota: As advertências e contraindicações formais da bula ANVISA não foram recuperadas neste ciclo de coleta (item DG001 — Bloqueante). Recomenda-se download e parsing do PDF da bula antes de qualquer avaliação de segurança aprofundada.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
O mecanismo de ação de Nitrazepam (modulação GABA-A via sítio benzodiazepínico) possui correspondência direta e farmacologicamente estabelecida com o distúrbio de início e manutenção do sono, sustentada por ensaios clínicos controlados históricos e extensa literatura comparativa com outros hipnóticos. No entanto, o risco conhecido de dependência, o perfil de segurança em populações vulneráveis (idosos) e a ausência dos dados regulatórios detalhados da bula exigem salvaguardas explícitas antes de qualquer expansão de uso.

**Para prosseguir, é necessário:**
- Recuperar e analisar as bulas aprovadas pela ANVISA para extrair indicações aprovadas, advertências formais e contraindicações (item DG001 — Bloqueante)
- Completar o perfil de mecanismo de ação via DrugBank API (item DG002 — Alta prioridade)
- Avaliar formalmente o risco de dependência e síndrome de abstinência para populações de uso prolongado e idosos
- Verificar conformidade com a regulamentação de psicotrópicos da ANVISA (Portaria SVS/MS nº 344/1998 — Lista C1 ou B1)
- Definir plano de monitoramento farmacológico (frequência, parâmetros clínicos) para uso no contexto de reposicionamento
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

