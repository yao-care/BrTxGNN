---
noindex: true
sitemap: false
layout: default
title: Acalabrutinibe Monohydrate Maleate
parent: Apenas Predição do Modelo (L5)
nav_order: 15
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Acalabrutinibe Monohydrate Maleate
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **0** 
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

## Acalabrutinibe: Avaliação de Reposicionamento — Previsões TxGNN Não Disponíveis
{: .text-alpha }

## Resumo em Uma Frase

Acalabrutinibe maleato mono-hidratado é um inibidor seletivo da tirosina quinase de Bruton (BTK), reconhecido internacionalmente como antineoplásico para neoplasias de células B, como linfoma de células do manto e leucemia linfocítica crônica (LLC). O modelo TxGNN **não gerou previsões de reposicionamento** para este fármaco na presente análise, provavelmente em razão da ausência de DrugBank ID no registro de entrada da pipeline. Não foram recuperados ensaios clínicos nem publicações relevantes para análise de reposicionamento neste pacote de evidências.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Sem registro disponível no sistema regulatório brasileiro |
| Nova Indicação Prevista | Sem previsão disponível |
| Pontuação de Previsão TxGNN | Indisponível |
| Nível de Evidência | L5 (somente entrada no modelo, sem estudos recuperados) |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 1) |
| Número de Registros | 1 (ativos: 1) |
| Decisão Recomendada | Hold |

---

## Citotoxicidade

> **Nota:** Acalabrutinibe pertence à classe dos inibidores de BTK, categoria de terapia-alvo antineoplásica de uso exclusivamente oncológico.

| Item | Conteúdo |
|------|------|
| Classificação de Citotoxicidade | Terapia alvo — Inibidor de BTK (Bruton's Tyrosine Kinase) |
| Risco de Mielossupressão | Baixo a Médio (inferior à quimioterapia citotóxica convencional; neutropenia pode ocorrer) |
| Classificação de Emetogenicidade | Baixa |
| Itens de Monitoramento | Hemograma completo com diferencial, função hepática, monitoramento cardíaco (fibrilação atrial) |
| Proteção no Manuseio | Seguir protocolos institucionais para manuseio de antineoplásicos orais |

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A causa mais provável é a ausência de DrugBank ID no registro de entrada, impedindo o mapeamento do fármaco ao grafo de conhecimento.

<!-- review:begin br-lic-20261106-acalabrutinibe_monohydrate_maleate-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “O fármaco não possui registro regulatório no Brasil e o modelo TxGNN não gerou previsões de reposicionamento, tornando a análise de evidências inviável no momento. A causa mais provável é a ausência de DrugBank ID no registro de entrada, impedindo o mapeamento do fármaco ao grafo de conhecimento.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 1 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-acalabrutinibe_monohydrate_maleate-1 -->

**Para prosseguir, é necessário:**
- **Corrigir o mapeamento DrugBank:** identificar e inserir o DrugBank ID correto de acalabrutinibe para re-executar a pipeline TxGNN e obter previsões de reposicionamento
- **Coletar MOA e categorias via DrugBank API:** lacuna classificada como Alta Severidade no Evidence Pack (DG002)
- **Recuperar dados regulatórios internacionais:** consultar FDA (NDA 210259) e EMA para caracterizar as indicações aprovadas globalmente e subsidiar a análise de indicação original
- **Avaliar acesso no Brasil:** verificar viabilidade de importação autorizada pela ANVISA ou inclusão em programa de acesso expandido/uso compassivo

<!-- review:begin br-lic-20261106-acalabrutinibe_monohydrate_maleate-2 -->

> **Correção de verificação (2026-11-06)**: Texto original: “**Recuperar dados regulatórios internacionais:** consultar FDA (NDA 210259) e EMA para caracterizar as indicações aprovadas globalmente e subsidiar a análise de indicação original / **Baixar e analisar bula de referência:** obter advertências, contraindicações e perfil de segurança completo de fontes internacionais, como medida paliativa à ausência de registro nacional (DG001)” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 1 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-acalabrutinibe_monohydrate_maleate-2 -->

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “O fármaco não possui registro regulatório no Brasil e o modelo TxGNN não gerou previsões de reposicionamento, tornando a análise de evidênci” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |
| 2026-11-06 | Removido: “**Baixar e analisar bula de referência:** obter advertências, contraindicações e perfil de segurança completo de fontes internacionais, como” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

