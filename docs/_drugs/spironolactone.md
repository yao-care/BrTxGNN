---
layout: default
title: Spironolactone
parent: 僅模型預測 (L5)
nav_order: 450
evidence_level: L5
indication_count: 2
---

# Spironolactone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

Usando a skill `txgnn-pipeline` como referência para o contexto do pipeline — e seguindo o prompt de avaliação v5, vou agora produzir o relatório com base no Evidence Pack fornecido.

---

# Spironolactone: Do Tratamento da Hipertensão e Edema à Hipotricose Simples do Couro Cabeludo

## Resumo em Uma Frase

Spironolactone é um antagonista da aldosterona (diurético poupador de potássio) amplamente utilizado no tratamento da hipertensão arterial, edema e hiperaldosteronismo primário, com propriedades anti-androgênicas adicionais que motivam uso off-label em condições hormonais. O modelo TxGNN prevê que pode ser eficaz para a **Hipotricose Simples do Couro Cabeludo (Hypotrichosis Simplex of the Scalp)**, porém atualmente **não há ensaios clínicos nem publicações** específicas apoiando esta direção — a evidência se restringe à previsão computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hipertensão arterial, edema, hiperaldosteronismo primário |
| Nova Indicação Prevista | Hipotricose Simples do Couro Cabeludo (Hypotrichosis Simplex of the Scalp) |
| Pontuação de Previsão TxGNN | 99,26% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Os dados de mecanismo de ação (MOA) ainda não foram obtidos via DrugBank API (DG002 — pendente). Com base em conhecimento farmacológico estabelecido, Spironolactone é um antagonista competitivo da aldosterona que atua nos receptores mineralocorticoides do túbulo distal renal, promovendo natriurese e retenção de potássio. De forma secundária, bloqueia receptores androgênicos periféricos e inibe parcialmente a 5-alfa-redutase, reduzindo os efeitos da testosterona e da di-hidrotestosterona (DHT) nos tecidos-alvo — mecanismo pelo qual é utilizado off-label em acne hormonal e alopecia androgenética feminina.

A aparente conexão com condições capilares deriva exatamente desta ação anti-androgênica: em patologias dependentes de andrógenos (ex.: alopecia androgenética), o fármaco demonstra efeito sobre o ciclo folicular. O modelo TxGNN provavelmente identificou o padrão fenotípico compartilhado de "escassez capilar no couro cabeludo" como elo de similaridade entre as indicações, gerando a previsão.

**Contudo, a Hipotricose Simples do Couro Cabeludo é uma condição monogênica** — causada por mutações de perda de função nos genes *LPAR6* e *LIPH*, que codificam proteínas da via do ácido lisofosfatídico essenciais para a integridade estrutural da haste capilar e do folículo. Sua fisiopatologia é **completamente independente do eixo aldosterona-andrógeno**. Nenhum mecanismo conhecido de Spironolactone atua sobre defeitos de desenvolvimento folicular de origem genética. A análise do pipeline classifica internamente esta ligação mecanística como **fraca — extrapolação fenotípica de alto risco de falso positivo**.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

Atualmente não há literatura relacionada.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A pontuação elevada do TxGNN (99,26%) reflete provavelmente transferência fenotípica por similaridade de padrão capilar, sem correspondência mecanística real — a Hipotricose Simples do Couro Cabeludo é uma doença genética estrutural, não responsiva ao bloqueio androgênico ou mineralocorticoide que Spironolactone provê. A ausência total de ensaios clínicos e literatura específica confirma que esta previsão não evoluiu além do estágio computacional.

**Para prosseguir, é necessário:**
- Obter o MOA completo via DrugBank API (pendência DG002) para formalizar a análise mecanística
- Consultar especialista em genética dermatológica para avaliação da plausibilidade biológica desta indicação específica
- Caso o interesse clínico seja em perda capilar androgênica, redirecionar a avaliação para **alopecia androgenética** — indicação com base mecanística robusta e literatura existente para Spironolactone
- Registrar este candidato como baixa prioridade de desenvolvimento, mantendo monitoramento passivo da literatura
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

