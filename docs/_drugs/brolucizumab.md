---
layout: default
title: Brolucizumab
parent: Apenas Predição do Modelo (L5)
nav_order: 155
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-13
description: "Brolucizumab: nova indicação prevista, Transtorno mitocondrial da fosforilação oxidativa por anomalias do DN… (nível de evidência L5). Indicação original: Outros medicamentos com ação no aparelho vis…"
---

# Brolucizumab
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **4** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Relatório de avaliação farmacêutica

</div>

# Brolucizumabe: De medicamento de ação no aparelho visual para transtorno mitocondrial da fosforilação oxidativa

## Resumo em Uma Frase

Brolucizumabe (VSIQQ) é um fragmento de anticorpo de cadeia única anti-VEGF-A, registrado na ANVISA na categoria "outros medicamentos com ação no aparelho visual".
O modelo TxGNN prevê que pode ser eficaz para **transtorno mitocondrial da fosforilação oxidativa por anomalias do DNA nuclear (mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção: trata-se apenas de uma previsão do modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Outros medicamentos com ação no aparelho visual |
| Nova Indicação Prevista | Transtorno mitocondrial da fosforilação oxidativa por anomalias do DNA nuclear |
| Pontuação de Previsão TxGNN | 99,67% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Somente registro cancelado |
| Número de Registros | 1 |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, o brolucizumabe é um fragmento de anticorpo de cadeia única (scFv) que inibe o VEGF-A, aprovado para uso intraocular (injeção intravítrea).

**Não foi estabelecida uma ligação mecanística plausível.** Os transtornos mitocondriais da fosforilação oxidativa não são conhecidos por serem dirigidos pelo VEGF-A, e um biológico administrado por via intravítrea dificilmente alcançaria a disfunção mitocondrial sistêmica. A pontuação alta (99,67%) reflete uma associação baseada em grafo de conhecimento, sem respaldo em estudos reais. Além disso, os riscos de inflamação intraocular e vasculite retiniana associados ao fármaco acrescentam uma preocupação de segurança.

### Outras indicações previstas (todas com nível L5, sem ensaios nem literatura)

| Posição | Indicação prevista | Pontuação TxGNN | Comentário |
|------|------|------|------|
| 2 | Varizes esofágicas com sangramento | 99,12% | A angiogênese esplâncnica mediada por VEGF contribui para a hipertensão portal, mas a racionalidade é apenas indireta e especulativa. A inibição sistêmica do VEGF pode agravar sangramentos e prejudicar a cicatrização, o que é preocupante em hemorragia varicosa ativa. |
| 3 | Varizes esofágicas sem sangramento | 99,12% | Mesma racionalidade especulativa. O tratamento padrão (betabloqueadores não seletivos, ligadura endoscópica) tem base de evidências muito superior. |
| 4 | Insuficiência pancreática exócrina | 99,07% | Nenhuma ligação mecanística crível: resulta da perda da função acinar e é tratada com reposição enzimática; o VEGF-A não tem papel conhecido na restauração da secreção. |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 100681185 (cancelado) | VSIQQ | Não informada | Outros medicamentos com ação no aparelho visual |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (PrimeKG, não derivadas da bula)**: uveíte, doença da íris, doença do corpo ciliar, panuveíte, doenças infecciosas oculares e conjuntivite.
- **Riscos de classe e do fármaco**: inflamação intraocular e vasculite retiniana (já mencionadas acima). A inibição sistêmica do VEGF pode aumentar o risco hemorrágico e prejudicar a cicatrização, o que é relevante sobretudo nas indicações de varizes esofágicas.

Para as demais informações de segurança, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Todas as indicações previstas têm apenas previsão do modelo (L5), sem ensaios clínicos nem literatura, e sem ligação mecanística plausível. Além disso, o único registro no Brasil está cancelado e a via de administração (intravítrea) é incompatível com doenças sistêmicas.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), etapa que bloqueia a triagem de segurança
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank)
- Demonstrar uma ligação mecanística plausível e evidências pré-clínicas para a indicação prevista
- Avaliar a compatibilidade de via de administração e a exposição sistêmica necessária, com análise de risco hemorrágico e vascular
- Esclarecer o motivo do cancelamento do registro e a situação comercial atual no Brasil
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

