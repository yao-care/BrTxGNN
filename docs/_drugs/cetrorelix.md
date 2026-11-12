---
layout: default
title: Cetrorelix
parent: Apenas Predição do Modelo (L5)
nav_order: 217
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Cetrorelix: nova indicação prevista, Hipertricose (hypertrichosis) (nível de evidência L5). Indicação original: Hormônios da hipófise"
monitor_inn: "cetrorelix"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "persistent fetal circulation syndrome", "familial isolated trichomegaly", "familial male-limited precocious puberty", "aromatase excess syndrome", "centra precocious puberty 1"]
---

# Cetrorelix
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

## Cetrorelix: Dos hormônios da hipófise à hipertricose (hypertrichosis)
{: .text-alpha }

## Resumo em Uma Frase

Cetrorelix (comercializado como CETROTIDE) é um antagonista do receptor de GnRH, registrado na ANVISA na categoria "hormônios da hipófise" e usado para inibir picos prematuros de LH em mulheres submetidas à estimulação ovariana controlada em tratamentos de fertilidade.
O modelo TxGNN prevê que pode ser eficaz para **Hipertricose (hypertrichosis)**, mas há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. Trata-se apenas de uma previsão computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Hormônios da hipófise |
| Nova Indicação Prevista | Hipertricose (hypertrichosis) |
| Pontuação de Previsão TxGNN | 0,9998 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 1 de 2) |
| Número de Registros | 2 (ativos: 1) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Segundo informações conhecidas, cetrorelix é um antagonista do receptor GnRH1 (gene GNRHR), um peptídeo que bloqueia a ação do GnRH na hipófise e suprime a liberação de LH e FSH, reduzindo os androgênios gonadais a jusante.

A relação com a hipertricose é fraca. A supressão de androgênios poderia, em teoria, afetar o crescimento de pelos, mas a hipertricose (principalmente as formas congênitas) geralmente não é dirigida por androgênios. A pontuação muito alta do TxGNN (0.9998) vem do modelo TxGNN (deep learning) e pode refletir similaridades que o modelo aprendeu entre doenças relacionadas, não evidência biológica; não há respaldo clínico ou bibliográfico.

### Outras previsões avaliadas

As demais previsões entre as 10 primeiras também carecem de evidências (todas L5, sem ensaios ou publicações):

| Doença prevista | Pontuação TxGNN | Avaliação mecanística |
|------|------|------|
| Hipertricose universal congênita tipo Ambras | 0,9997 | Distúrbio congênito ligado à regulação de TRPS1, não hormonal; a pontuação do modelo TxGNN (deep learning) pode refletir similaridades aprendidas entre doenças relacionadas, não evidência biológica |
| Síndrome malformativa com componente dentário/periodontal | 0,9997 | Sem conexão mecanística plausível |
| Síndrome com malformação de Dandy-Walker | 0,9996 | Defeito estrutural do desenvolvimento, não corrigível por antagonista de GnRH |
| Anormalidade genética isolada da haste capilar | 0,9996 | Defeitos estruturais/de queratina, não mediados por hormônios |
| Síndrome da circulação fetal persistente | 0,9967 | Sem papel conhecido do eixo GnRH; inaplicável a neonatos |
| Tricomegalia isolada familiar | 0,9963 | Traço genético, independente de gonadotrofinas |
| Puberdade precoce familiar limitada ao sexo masculino | 0,9955 | Domínio biológico relacionado, mas mecanismo incompatível (mutação ativadora de LHCGR, independente de LH) |
| Síndrome de excesso de aromatase | 0,9953 | Defeito primário na síntese periférica de estrogênio; inibidores de aromatase são a classe adequada |
| Puberdade precoce central 1 | 0,9929 | Candidata biologicamente mais plausível, mas agonistas de GnRH são o padrão de cuidado |

---

## Informações de Comercialização no Brasil

| Registro | Produto | Empresa detentora | Situação |
|------|------|------|------|
| 100890369 | CETROTIDE | MERCK S/A | Ativo |
| 111240220 | CETROTIDE | SERONO PRODUTOS FARMACÊUTICOS LTDA | Cancelado |

---

## Considerações de Segurança

- **Interações Medicamentosas**: a consulta foi concluída e retornou apenas uma entrada de farmacologia, sem classificação de gravidade: a interação com o alvo, o receptor GnRH1 (GNRHR). Não há interações medicamentosas clinicamente classificadas nos dados compilados.

Para advertências e contraindicações, consulte a bula.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura para nenhuma das indicações previstas. Para a hipertricose, o mecanismo é fraco e a pontuação elevada do TxGNN (deep learning) pode refletir similaridades que o modelo aprendeu entre doenças relacionadas, não evidência biológica.
- A puberdade precoce central é a hipótese biologicamente mais coerente e pode ser tratada como pergunta de pesquisa, mas os agonistas de GnRH já são o padrão de cuidado.

<!-- review:begin br-lic-20261106-cetrorelix-1 -->

> **Correção de verificação (2026-11-06)**: Texto original: “Para a hipertricose, o mecanismo é fraco e a pontuação elevada do TxGNN (deep learning) pode refletir similaridades que o modelo aprendeu entre doenças relacionadas, não evidência biológica. / O registro único no Brasil está cancelado, o que limita a viabilidade prática.” Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro (dados abertos de medicamentos da ANVISA, em 2026-11-06). Nos dados (dados abertos de medicamentos da ANVISA) constam 2 registros para este medicamento, 1 válidos; os números atualizados estão no resumo rápido e nas informações de comercialização. Fonte: [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv).

<!-- review:end br-lic-20261106-cetrorelix-1 -->

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois essa lacuna impede a triagem de segurança.
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank).
- Realizar revisão sistemática da literatura e busca em registros de ensaios, priorizando a puberdade precoce central.
- Verificar a situação regulatória atual do produto no Brasil e a compatibilidade de vias de administração e formas farmacêuticas.

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “O registro único no Brasil está cancelado, o que limita a viabilidade prática” | Corrigido | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

