---
layout: default
title: Albuterol Sulfate
parent: Apenas Predição do Modelo (L5)
nav_order: 36
evidence_level: L5
indication_count: 8
drugbank_id: DB01001
monitor_inn: "Salbutamol"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "anaphylaxis", "common cold", "atopic conjunctivitis", "anorectal stricture"]
last_modified_at: 2026-11-16
description: "Albuterol Sulfate: nova indicação prevista, Conjuntivite papilar (papillary conjunctivitis) (nível de evidência L5). Indicação original: BRONCODILATADORES"
---

# Albuterol Sulfate
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **8** 
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

## Albuterol Sulfate: Conjuntivite papilar (papillary conjunctivitis)
{: .text-alpha }

## Resumo em Uma Frase

O sulfato de albuterol (salbutamol) é um broncodilatador de uso inalatório, registrado no Brasil na categoria de broncodilatadores.
O modelo TxGNN prevê que pode ser eficaz para **Conjuntivite papilar (papillary conjunctivitis)**, mas **não há nenhum ensaio clínico nem publicação** que apoie diretamente esta previsão nos dados compilados para este relatório.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | BRONCODILATADORES; ANTIASMATICOS |
| Nova Indicação Prevista | Conjuntivite papilar (papillary conjunctivitis) |
| Pontuação de Previsão TxGNN | 1.0000 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 14 de 15) |
| Número de Registros | 15 (ativos: 14) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados. Sabe-se que o albuterol pertence à classe dos agonistas beta-2 adrenérgicos, que relaxam a musculatura lisa brônquica.

Existe uma possível linha de raciocínio: agonistas beta-2 têm atividade anti-alérgica pré-clínica em tecido conjuntival, como a estabilização de mastócitos e a redução da permeabilidade vascular. Esses achados foram descritos para a conjuntivite atópica, e não para a conjuntivite papilar.

Esse raciocínio é frágil. A conjuntivite papilar costuma ser causada por lentes de contato ou por estímulo mecânico, e não apenas por mecanismo alérgico mediado por mastócitos. Por isso, a previsão do modelo não encontra respaldo mecanístico claro nem estudos reais. A pontuação do modelo é muito alta (0,9999643, aqui exibida como 1,0000 com quatro casas), mas ela não substitui evidência clínica.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada.

## Informações de Comercialização no Brasil

Há registros válidos de produtos de componente único no Brasil, e um registro cancelado. Principais registros:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 135310035 | AERO-IFAL | Não informada | Broncodilatadores |
| Registro 113430134 | SULFATO DE SALBUTAMOL | Não informada | Broncodilatadores |
| Registro 154230066 | SULFATO DE SALBUTAMOL | Não informada | Broncodilatadores |
| Registro 105710026 | NEUTOSS | Não informada | Broncodilatadores |
| Registro 101070226 | AEROLIN | Não informada | Broncodilatadores |

## Considerações de Segurança

Consulte a bula para informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão principal não tem ensaios clínicos nem publicações que a sustentem, e o mecanismo proposto é pouco plausível para uma condição frequentemente causada por lentes de contato ou fatores mecânicos. O nível de evidência é L5.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação do fármaco.
- Revisão sistemática da literatura sobre agonistas beta-2 tópicos oculares em conjuntivites, incluindo a conjuntivite papilar.
- Estudos pré-clínicos específicos nesta condição, antes de qualquer ensaio clínico.
- Avaliação da via de administração, já que a forma inalatória não é compatível com uso ocular.
- Dados de advertências, contraindicações e interações da bula aprovada pela ANVISA.

<!-- review:begin log -->

## Registro de verificação

Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.

| Data da verificação | Item | Ação | Fonte |
|------|------|------|------|
| 2026-11-06 | Removido: “A busca na ANVISA com o termo "ALBUTEROL SULFATE" retornou **0 registros**, o que indica uma provável divergência de nomenclatura: no Brasil” | Não aparece mais após a regeneração do relatório (2026-11-16: o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação; antes: Corrigido) | [ANVISA – Dados abertos de medicamentos](https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv) |

<!-- review:end log -->

## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

