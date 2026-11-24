---
layout: default
title: Ibuprofen
parent: Apenas Predição do Modelo (L5)
nav_order: 358
evidence_level: L5
indication_count: 7
monitor_inn: "Ibuprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
last_modified_at: 2026-11-24
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

<!-- licenses:begin -->

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 100431469 | IBUPROFENO + PARACETAMOL | EUROFARMA LABORATORIOS S.A. | Ativo |
| 100431516 | DUALGI | EUROFARMA LABORATORIOS S.A. | Ativo |
| 100431560 | IBUPROFENO | EUROFARMA LABORATORIOS S.A. | Ativo |
| 100840148 | SPIDUFEN | ZAMBON LABORATÓRIOS FARMACÊUTICOS LTDA. | Ativo |
| 100849959 | SPIDUFEN LIMÃO COLA | ZAMBON LABORATÓRIOS FARMACÊUTICOS LTDA. | Ativo |
| 100849960 | SPIDUFEN ORO | ZAMBON LABORATÓRIOS FARMACÊUTICOS LTDA. | Ativo |
| 100849961 | ARGYFEN | ZAMBON LABORATÓRIOS FARMACÊUTICOS LTDA. | Ativo |
| 100850149 | PROINFLAC | LABORATORIOS B. BRAUN S/A | Ativo |
| 101750021 | CAPSFEN | CATALENT BRASIL LTDA. | Ativo |
| 102350961 | IBULIV | EMS S/A | Ativo |
| 102351435 | IBULIV | EMS S/A | Ativo |
| 103700076 | IBUPRIL | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 103700539 | IBUPROFENO | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 103700757 | IBUPROFENO | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 103700762 | IBUPRIL CAPS | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 103920065 | ALGY-FLANDERIL | VITAMEDIC INDUSTRIA FARMACEUTICA LTDA | Ativo |
| 103920201 | IBUPROFENO | VITAMEDIC INDUSTRIA FARMACEUTICA LTDA | Ativo |
| 103920205 | ALGY GOTAS | VITAMEDIC INDUSTRIA FARMACEUTICA LTDA | Ativo |
| 103920219 | IBUPROFENO | VITAMEDIC INDUSTRIA FARMACEUTICA LTDA | Ativo |
| 103920220 | ALGY-FLANDERIL CAPS | VITAMEDIC INDUSTRIA FARMACEUTICA LTDA | Ativo |
| 103920222 | IBUPROFENO | VITAMEDIC INDUSTRIA FARMACEUTICA LTDA | Ativo |
| 104810074 | VANTIL | 1FARMA INDUSTRIA FARMACEUTICA LTDA | Ativo |
| 104810152 | IBUPROFENO | 1FARMA INDUSTRIA FARMACEUTICA LTDA | Ativo |
| 104971570 | IBUPROFENO | UNIÃO QUÍMICA FARMACÊUTICA NACIONAL S/A | Ativo |
| 104971574 | ALIZ | UNIÃO QUÍMICA FARMACÊUTICA NACIONAL S/A | Ativo |
| 105350220 | IBUPROFENO | LABORATÓRIO GLOBO SA | Ativo |
| 105350230 | IBUPROFENO | LABORATÓRIO GLOBO SA | Ativo |
| 105350231 | IBUGLOBO | LABORATÓRIO GLOBO SA | Ativo |
| 105730370 | DORALIV | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Ativo |
| 105730579 | IBUPROFENO | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Ativo |

A tabela mostra até 30 registros (os ativos primeiro), de 218 registros nos dados. A lista completa está na consulta de medicamentos da ANVISA (https://consultas.anvisa.gov.br/#/medicamentos/).

<!-- licenses:end -->

<!-- review:begin br-lic-20261106-ibuprofen-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Segundo os dados compilados, o ibuprofeno consta como comercializado no Brasil, com 13 registros válidos e 7 cancelados. Os dados de registro são parciais, e a lista detalhada de registros não está disponível neste relatório.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Os números atualizados de registros estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-ibuprofen-1 -->

<!-- review:begin br-lic-20261124c-ibuprofen-1 -->

> **Correção de verificação (2026-11-24)**: Texto original: “Os dados de registro são parciais, e a lista detalhada de registros não está disponível neste relatório.” Removido: a frase dizia que a lista de registros seria parcial ou não estaria disponível; os dados abertos de medicamentos da ANVISA usados nesta página trazem todos os registros do medicamento, que estão na tabela desta seção gerada por programa (os números atualizados estão no resumo rápido e na tabela). Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261124c-ibuprofen-1 -->

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
| 2026-11-06 | Removido: “Segundo os dados compilados, o ibuprofeno consta como comercializado no Brasil, com 13 registros válidos e 7 cancelados” | Corrigido (revisado em 2026-11-24; versão anterior guardada no registro) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Caldolor (ibuprofen) prescribing information, Cumberland Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1eaa7790-f1a1-4f51-b10a-cbbaf033f684) |
| 2026-11-24 | Removido: “Os dados de registro são parciais, e a lista detalhada de registros não está disponível neste relatório.” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

