---
layout: default
title: Ibuprofen
parent: Apenas Predição do Modelo (L5)
nav_order: 358
evidence_level: L5
indication_count: 7
monitor_inn: "Ibuprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
last_modified_at: 2026-11-20
description: "Ibuprofen: nova indicação prevista, displasia acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) (nível de evidência L5). Indicação original: Não consta nos dados loc…"
---

# Ibuprofen
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **7** 
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

## Ibuprofeno: inibidor não seletivo da ciclo-oxigenase (COX) → displasia acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type)
{: .text-alpha }

## Resumo em Uma Frase

Ibuprofeno é um anti-inflamatório não esteroidal (AINE) amplamente utilizado.
O modelo TxGNN prevê que pode ser eficaz para **displasia acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. Trata-se apenas de uma previsão do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | displasia acromesomélica tipo Hunter-Thompson (acromesomelic dysplasia, Hunter-Thompson type) |
| Pontuação de Previsão TxGNN | 0,9974 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 101 de 218) |
| Número de Registros | 218 (ativos: 101) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Ibuprofen (tradução não oficial): “O ibuprofeno tem propriedades analgésicas, anti-inflamatórias e antipiréticas. O mecanismo de ação de CALDOLOR, assim como o de outros AINEs, não é completamente compreendido, mas envolve a inibição da ciclo-oxigenase (COX-1 e COX-2).” Texto original em inglês: "Ibuprofen has analgesic, anti-inflammatory, and antipyretic properties. The mechanism of action of CALDOLOR, like that of other NSAIDs, is not completely understood but involves inhibition of cyclooxygenase (COX-1 and COX-2)." ([DailyMed: Caldolor (ibuprofen) prescribing information, Cumberland Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1eaa7790-f1a1-4f51-b10a-cbbaf033f684), versão de 2026-01-29; acessado em 2026-11-19). Sabe-se, de forma geral, que o ibuprofeno atua inibindo a COX-1 e a COX-2, reduzindo a síntese de prostaglandinas, com efeito analgésico e anti-inflamatório.

Já a displasia acromesomélica tipo Hunter-Thompson é uma displasia esquelética rara, causada por variantes de perda de função no gene CDMP1/GDF5, que participa da sinalização de BMP. Não há vínculo mecanístico estabelecido entre essa via e a inibição da COX. Uma ação anti-inflamatória não seria capaz de corrigir um defeito genético do desenvolvimento.

A pontuação alta (0,9974) provavelmente reflete a proximidade do doença com termos musculoesqueléticos e articulares nos dados de treinamento do modelo, e não uma justificativa biológica. A previsão deve ser tratada com cautela.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

Os dados de registro são parciais, e a lista detalhada de registros não está disponível neste relatório.

<!-- review:begin br-lic-20261106-ibuprofen-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Segundo os dados compilados, o ibuprofeno consta como comercializado no Brasil, com 13 registros válidos e 7 cancelados. Os dados de registro são parciais, e a lista detalhada de registros não está disponível neste relatório.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 218 registros para este medicamento, 101 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-ibuprofen-1 -->

## Considerações de Segurança

- **Contraindicações registradas nos dados de segurança (não extraídas da bula)**: hipertensão, insuficiência hepática, doença renal, doença hepática, úlcera péptica, doença inflamatória intestinal, trombocitopenia, distúrbios da coagulação sanguínea, acidente vascular cerebral e infarto do miocárdio, entre outras condições (por exemplo, epilepsia, DPOC, lúpus eritematoso sistêmico, diabetes mellitus, hipotireoidismo e hiperplasia prostática benigna).
- **Interações Medicamentosas** (100 interações identificadas; exemplos):
  - **Maior gravidade**: ácido acetilsalicílico.
  - **Moderada**: corticosteroides (betametasona, budesonida, dexametasona, hidrocortisona), sulfonilureias (acetoexamida, clorpropamida, glimepirida, glipizida, glibenclamida), aprepitanto, balsalazida, exenatida, fenfluramina, dexfenfluramina, canamicina e levofloxacino.
  - **Menor**: famotidina, ranitidina e cimetidina.

As advertências e contraindicações da bula aprovada pela ANVISA não estavam disponíveis; consulte a bula para informações de segurança completas.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem publicações para esta doença, e não existe vínculo mecanístico plausível entre a inibição da COX e a via GDF5/BMP. A previsão baseia-se apenas no modelo (L5).

**Para prosseguir, é necessário:**
- Dados detalhados do mecanismo de ação (MOA) e uma hipótese biológica que justifique a aplicação nesta doença
- Estudos pré-clínicos que demonstrem algum efeito sobre a patologia da doença
- Obtenção e análise da bula da ANVISA (advertências e contraindicações) para a triagem de segurança
- Avaliação de que o uso se limitaria, no máximo, ao alívio sintomático da dor, o que não configura reposicionamento

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Segundo os dados compilados, o ibuprofeno consta como comercializado no Brasil, com 13 registros válidos e 7 cancelados” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Caldolor (ibuprofen) prescribing information, Cumberland Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1eaa7790-f1a1-4f51-b10a-cbbaf033f684) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

