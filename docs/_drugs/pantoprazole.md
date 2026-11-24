---
layout: default
title: Pantoprazole
parent: Apenas Predição do Modelo (L5)
nav_order: 509
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "PANTOPRAZOLE"
predicted_indications: ["duodenal obstruction"]
description: "Pantoprazole: nova indicação prevista, Duodenal obstruction (nível de evidência L5). Indicação original: ANTIULCEROSOS"
---

# Pantoprazole
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **1** 
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

## Pantoprazole: Duodenal obstruction
{: .text-alpha }

## Resumo em Uma Frase

Pantoprazol é um inibidor da bomba de prótons, registrado na ANVISA como antiulceroso e antiácido.
O modelo TxGNN prevê que pode ser eficaz para **doença ulcerosa péptica ativa (Active Peptic Ulcer Disease)**,
atualmente com **1 ensaio clínico** e **20 publicações** apoiando esta direção. Trata-se, na prática, de uma indicação já estabelecida para a classe, e não de um reposicionamento propriamente dito.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | ANTIULCEROSOS; ANTIACIDOS E ANTIULCEROSOS SIMPLES; ANTIACIDOS E ANTIULCEROSOS |
| Nova Indicação Prevista | Duodenal obstruction |
| Pontuação de Previsão TxGNN | 0.9921 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 48 de 103) |
| Número de Registros | 103 (ativos: 48) |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

Segundo a seção “Mechanism of Action” da bula aprovada pela FDA dos EUA (Prescribing Information) para Pantoprazole (tradução não oficial): “O pantoprazol é um IBP que suprime a etapa final da produção de ácido gástrico ligando-se covalentemente ao sistema enzimático (H +, K + )-ATPase na superfície secretora da célula parietal gástrica. Esse efeito leva à inibição da secreção de ácido gástrico tanto basal quanto estimulada, independentemente do estímulo.” Texto original em inglês: "Pantoprazole is a PPI that suppresses the final step in gastric acid production by covalently binding to the (H +, K + )-ATPase enzyme system at the secretory surface of the gastric parietal cell. This effect leads to inhibition of both basal and stimulated gastric acid secretion irrespective of the stimulus." ([DailyMed: Protonix I.V. (pantoprazole sodium) prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3cde88e6-28f2-4cbe-8c3f-770b05cc0e1b), versão de 2026-11-06; acessado em 2026-11-19). Pelo conhecimento da classe e pela literatura compilada, o pantoprazol inibe de forma irreversível a H+/K+ ATPase (bomba de prótons) das células parietais gástricas. Isso reduz a secreção de ácido e permite a cicatrização da úlcera.

Obstrução duodenal (pontuação de 0,9921) não tem vínculo mecanístico crível. A pontuação vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, não evidência biológica.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Concluído | 323 | Ensaio multicêntrico, randomizado, duplo-cego e com controle ativo, comparando terapia tripla de 7 dias com ilaprazol versus pantoprazol na erradicação de *H. pylori* em pacientes com úlcera gástrica e/ou duodenal |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [38384180](https://pubmed.ncbi.nlm.nih.gov/38384180/) | 2024 | RCT | Gut and Liver | Estudo randomizado com controle ativo sobre o tegoprazan em úlceras artificiais induzidas por ressecção endoscópica |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | Revisão sistemática/meta-análise | Am J Gastroenterol | Compara bloqueadores ácidos competitivos de potássio (P-CAB) e IBPs na cicatrização de esofagite grau C/D |
| [10638560](https://pubmed.ncbi.nlm.nih.gov/10638560/) | 2000 | Estudo comparativo | Am J Gastroenterol | Pantoprazol versus ranitidina no tratamento da úlcera duodenal, em estudo multicêntrico no Brasil |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | Estudo comparativo | Hepato-gastroenterology | Compara lansoprazol e pantoprazol na úlcera duodenal ativa e na erradicação de *H. pylori* |
| [8930575](https://pubmed.ncbi.nlm.nih.gov/8930575/) | 1996 | Revisão | Eur J Gastroenterol Hepatol | Descreve o mecanismo do pantoprazol: acúmulo no compartimento ácido da célula parietal e ativação por ácido antes de agir na bomba de prótons |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Revisão | Clin Drug Investig | Pantoprazol liga-se de forma irreversível à bomba de prótons, com duração de ação relativamente longa |
| [15989651](https://pubmed.ncbi.nlm.nih.gov/15989651/) | 1997 | Revisão | Expert Opin Investig Drugs | Em comparação com os antagonistas H2, o pantoprazol alivia a dor mais rápido e cicatriza mais depressa as úlceras |
| [11060758](https://pubmed.ncbi.nlm.nih.gov/11060758/) | 2000 | Revisão | Expert Opin Investig Drugs | Atualização sobre abordagens terapêuticas em úlceras gástricas e duodenais |
| [21534455](https://pubmed.ncbi.nlm.nih.gov/21534455/) | 2011 | Revisão | Med Arh | IBPs no manejo da doença do refluxo gastroesofágico |
| [16961157](https://pubmed.ncbi.nlm.nih.gov/16961157/) | 2006 | Revisão | Int J Clin Pharmacol Ther | Impacto do polimorfismo de CYP2C19 na ação dos IBPs |

---

## Informações de Comercialização no Brasil

O medicamento está comercializado no Brasil. Abaixo, os 5 primeiros:

<!-- review:begin br-lic-20261106-pantoprazole-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Todos os 20 registros encontrados estão válidos; o medicamento está comercializado no Brasil.” Removido: o número ou a situação dos registros informado não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 103 registros para este medicamento, 48 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-pantoprazole-1 -->

<!-- licenses:begin -->

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 100430026 | PANTOPRAZOL | EUROFARMA LABORATORIOS S.A. | Ativo |
| 100430634 | PANTOCAL | EUROFARMA LABORATORIOS S.A. | Ativo |
| 100431213 | PANTOCAL | EUROFARMA LABORATORIOS S.A. | Ativo |
| 100431438 | PANTOPRAZOL SÓDICO SESQUI-HIDRATADO | EUROFARMA LABORATORIOS S.A. | Ativo |
| 100431440 | GÁZIA | EUROFARMA LABORATORIOS S.A. | Ativo |
| 100470307 | PANTOPAZ | SANDOZ DO BRASIL INDÚSTRIA FARMACÊUTICA LTDA | Ativo |
| 100470456 | PANTOPRAZOL | SANDOZ DO BRASIL INDÚSTRIA FARMACÊUTICA LTDA | Ativo |
| 100681129 | PANTOPRAZOL | NOVARTIS BIOCIENCIAS S.A | Ativo |
| 101180622 | INILOK | APSEN FARMACEUTICA S/A | Ativo |
| 101460064 | ZIPROL | LABORATÓRIOS BALDACCI LTDA | Ativo |
| 102350156 | PANTOPRAZOL SÓDICO | EMS S/A | Ativo |
| 102351266 | NIVUX | EMS S/A | Ativo |
| 102351289 | PANTOPRAZOL MAGNÉSICO DI-HIDRATADO | EMS S/A | Ativo |
| 102351296 | RESTITUE | EMS S/A | Ativo |
| 102980519 | PTZOL | CRISTÁLIA PRODUTOS QUÍMICOS FARMACÊUTICOS LTDA. | Ativo |
| 102980542 | PANTOPRAZOL SÓDICO SESQUI-HIDRATADO | CRISTÁLIA PRODUTOS QUÍMICOS FARMACÊUTICOS LTDA. | Ativo |
| 103700756 | TOLZA | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 103700774 | PANTOPRAZOL SÓDICO SESQUI-HIDRATADO | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 103700778 | TOLZA IV | LABORATÓRIO TEUTO BRASILEIRO S/A | Ativo |
| 104971564 | PANGASTRI | UNIÃO QUÍMICA FARMACÊUTICA NACIONAL S/A | Ativo |
| 105730011 | PANTOMIX | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Ativo |
| 105730031 | DISPETIC | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Ativo |
| 105730462 | ADIPEPT | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Ativo |
| 105730503 | DIVENA | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Ativo |
| 105730550 | PANTOPRAZOL SÓDICO | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Ativo |
| 105730554 | PANTOPRAZOL MAGNÉSICO DIIDRATADO | ACHÉ LABORATÓRIOS FARMACÊUTICOS S.A | Ativo |
| 105830897 | PANTOPRAZOL SÓDICO SESQUI-HIDRATADO | GERMED FARMACEUTICA LTDA | Ativo |
| 105830983 | NIDUE | GERMED FARMACEUTICA LTDA | Ativo |
| 105831007 | PANTOPRAZOL MAGNÉSICO | GERMED FARMACEUTICA LTDA | Ativo |
| 106390182 | PANTOZOL | TAKEDA PHARMA LTDA. | Ativo |

A tabela mostra até 30 registros (os ativos primeiro), de 103 registros nos dados. A lista completa está na consulta de medicamentos da ANVISA (https://consultas.anvisa.gov.br/#/medicamentos/).

<!-- licenses:end -->

---

## Considerações de Segurança

- **Contraindicações no grafo de conhecimento (não extraídas de bula)**: osteoporose, osteoporose pós-menopausa, fratura óssea e anemia perniciosa.
- **Interações medicamentosas**: foram identificadas 100 interações no total (amostra de 20 exibida nos dados compilados). Principais, de gravidade **maior**:
  - Acalabrutinibe
  - Atazanavir

  Interações **moderadas** incluem hidroclorotiazida, alpelisibe, anfotericina B, amicacina, anfetamina, fenofibrato, apalutamida, armodafinila, atorvastatina, bosutinibe e bumetanida. Interações **menores** incluem ácido acetilsalicílico, axitinibe, bortezomibe, brivaracetam e cianocobalamina.

As advertências e contraindicações da bula da ANVISA não estavam disponíveis; consulte a bula para essas informações.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
- Há ensaio de Phase 3 concluído e vários ensaios comparativos de pantoprazol na úlcera duodenal, o que sustenta o nível L1. Porém, trata-se de uma indicação já estabelecida da classe, sem novidade terapêutica.

<!-- review:begin br-lic-20261106-pantoprazole-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Porém, trata-se de uma indicação já estabelecida da classe, sem novidade terapêutica, e há 20 registros válidos no Brasil, com o medicamento comercializado.” Removido: o número ou a situação dos registros informado não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 103 registros para este medicamento, 48 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-pantoprazole-2 -->

**Para prosseguir, é necessário:**
- Obter a bula da ANVISA (advertências e contraindicações), que é uma lacuna bloqueante para a triagem de segurança.
- Confirmar o mecanismo de ação em fonte primária (DrugBank).
- Avaliar o risco em pacientes com osteoporose, risco de fratura ou deficiência de vitamina B12, e revisar as interações de maior gravidade (atazanavir, acalabrutinibe).
- Confirmar a população exata do ensaio NCT02084420, cujo título não deixa claro se se trata de úlcera péptica ativa.

<!-- review:begin br-lic-20261106-pantoprazole-3 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Confirmar o mecanismo de ação em fonte primária (DrugBank). / Verificar a situação regulatória atual: os 20 registros estão cancelados, então é preciso confirmar se há outro registro vigente ou se seria necessário um novo registro.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 103 registros para este medicamento, 48 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-pantoprazole-3 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos. A frase que dizia não haver dados sobre o mecanismo de ação foi substituída por um trecho da bula oficial citada (com tradução não oficial).

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “Todos os 20 registros encontrados estão válidos; o” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “e há 20 registros válidos no Brasil, com o medicamento comercializado” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “Verificar a situação regulatória atual: os 20 registros estão cancelados, então é preciso confirmar se há outro registro vigente ou se seria” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-19 | Frase “não há dados sobre o mecanismo de ação” substituída por trecho da bula dos EUA | Frase sobre a falta de dados do mecanismo de ação substituída por um trecho com fonte | [DailyMed: Protonix I.V. (pantoprazole sodium) prescribing information, Cardinal Health 107, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3cde88e6-28f2-4cbe-8c3f-770b05cc0e1b) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

