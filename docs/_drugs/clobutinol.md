---
layout: default
title: Clobutinol
parent: Apenas Predição do Modelo (L5)
nav_order: 232
evidence_level: L5
indication_count: 10
monitor_inn: "Clobutinol"
predicted_indications: ["typhoid fever", "mucocutaneous leishmaniasis", "leishmaniasis, diffuse cutaneous", "diffuse scleroderma", "pneumonia", "trigonitis", "bronchiolitis obliterans with obstructive pulmonary disease", "paratyphoid fever", "cystitis", "combined immunodeficiency due to DOCK8 deficiency"]
last_modified_at: 2026-11-20
description: "Clobutinol: nova indicação prevista, febre tifoide (typhoid fever) (nível de evidência L5). No Brasil, registros na ANVISA: 18 (ativos: 2)"
---

# Clobutinol
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

## Clobutinol: antitussígeno de ação central → febre tifoide (typhoid fever)
{: .text-alpha }

## Resumo em Uma Frase

Clobutinol é um antitussígeno de ação central, retirado do mercado europeu em 2007 por causa do prolongamento do intervalo QT.
O modelo TxGNN prevê que pode ser eficaz para **febre tifoide (typhoid fever)**, mas **não há ensaios clínicos nem publicações** nos dados compilados para este relatório que apoiem essa direção.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | febre tifoide (typhoid fever) |
| Pontuação de Previsão TxGNN | 0,9998 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 2 de 18) |
| Número de Registros | 18 (ativos: 2) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo o ChEMBL (EMBL-EBI), o mecanismo de ação registrado para Clobutinol é (tradução não oficial): “Desconhecido”. Texto original em inglês: "Unknown" ([ChEMBL CHEMBL1474889 (clobutinol): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1474889), CC BY-SA 3.0; acessado em 2026-11-19). Sabe-se que ele atua centralmente para suprimir a tosse, um efeito apenas sintomático.

Não foi identificado nenhum vínculo mecanístico com a febre tifoide: o fármaco não tem atividade antibacteriana conhecida contra a *Salmonella* Typhi. A previsão decorre exclusivamente de cálculo computacional, e a similaridade com a indicação original ainda não foi avaliada. Portanto, a razoabilidade biológica da previsão não está sustentada pelos dados atuais.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

Os dados locais indicam 2 registros válidos e 18 cancelados. Esta lista pode estar incompleta, pois os registros são parciais, e nenhum registro detalhado está disponível para listagem neste relatório.

## Considerações de Segurança

- **Contraindicações (relação de risco registrada): síndrome do QT longo** (long QT syndrome). O clobutinol é conhecido por prolongar o intervalo QT e bloquear o canal hERG, motivo de sua retirada do mercado em 2007.
- **Interações medicamentosas**: nenhuma interação foi encontrada na consulta realizada.

Para as demais informações de segurança, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão é puramente computacional (nível de evidência L5), sem ensaios clínicos, literatura ou mecanismo plausível, e o perfil de risco cardíaco (prolongamento do QT) é uma barreira importante.

**Para prosseguir, é necessário:**
- Obter e analisar a bula da ANVISA (advertências e contraindicações), lacuna bloqueante para a triagem de segurança.
- Obter dados de mecanismo de ação a partir do DrugBank.
- Realizar estudos pré-clínicos que demonstrem atividade contra *Salmonella* Typhi.
- Avaliar o risco cardíaco (QT/hERG) frente a qualquer uso em doença infecciosa.

<!-- review:begin log -->

## Registro de verificação

Abaixo, o registro de verificação desta página. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial); as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte (revisado em 2026-11-20; versão anterior guardada no registro) | [ChEMBL CHEMBL1474889 (clobutinol): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1474889) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

