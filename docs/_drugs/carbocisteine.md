---
layout: default
title: Carbocisteine
parent: Apenas Predição do Modelo (L5)
nav_order: 194
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Carbocisteine: nova indicação prevista, Gota (Gout) (nível de evidência L5). Indicação original: Expectorantes"
monitor_inn: "Carbocisteine"
predicted_indications: ["gout", "appendicitis", "congestive heart failure", "acute pulmonary heart disease", "epiglottitis", "peritonitis", "laryngitis", "Lesch-Nyhan syndrome", "gastrointestinal allergy"]
---

# Carbocisteine
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

# Carbocisteína: De expectorante mucolítico a gota (previsão do modelo)

## Resumo em Uma Frase

Carbocisteína é um mucolítico/expectorante, originalmente usado para facilitar a eliminação de secreções das vias respiratórias.
O modelo TxGNN prevê que pode ser eficaz para **Gota (Gout)**, com a maior pontuação entre as previsões, mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção. Trata-se apenas de uma previsão computacional.

Observação importante: a segunda previsão, **Bronquite (Bronchitis)**, é a única com respaldo na literatura (1 RCT de 1985, 1 metanálise de 2024 e estudos pré-clínicos). Ela corresponde, em grande parte, à indicação original e não a um reposicionamento verdadeiro. Ela é apresentada adiante como alternativa de maior interesse prático.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Expectorantes |
| Nova Indicação Prevista | Gota (Gout) |
| Pontuação de Previsão TxGNN | 99,67% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Somente registros cancelados |
| Número de Registros | 14 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a carbocisteína é um mucolítico com atividade mucorreguladora e antioxidante, usado para reduzir a viscosidade do muco respiratório.

Para a **gota**, não há nenhum elo mecanístico identificável. Nada nos dados conecta a carbocisteína ao metabolismo do urato ou à inflamação gotosa. A pontuação alta (99,67%) reflete apenas associações do grafo de conhecimento, e deve ser interpretada com cautela.

Em contraste, para a **bronquite** (2º lugar, 98,77%), a plausibilidade é forte: a carbocisteína regula a viscosidade do muco, melhora o transporte mucociliar (modelo de bronquite induzida por SO₂ em ratos) e elimina espécies reativas de oxigênio in vitro. Ainda assim, isso é essencialmente a reconfirmação da indicação original.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para a gota.

## Evidências da Literatura

Atualmente não há literatura relacionada à gota.

Para referência, a literatura disponível para a previsão de **bronquite** (2º lugar):

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [3907681](https://pubmed.ncbi.nlm.nih.gov/3907681/) | 1985 | RCT | Br J Clin Pract | Estudo duplo-cego, controlado por placebo, de carbocisteína oral a longo prazo em bronquite crônica (sem resumo disponível) |
| [39413571](https://pubmed.ncbi.nlm.nih.gov/39413571/) | 2024 | Revisão sistemática | Respir Investig | Metanálise sobre eficácia e segurança de mucolíticos em DPOC estável |
| [18832259](https://pubmed.ncbi.nlm.nih.gov/18832259/) | 2008 | Revisão | Drug Ther Bull | Compara a erdosteína com carbocisteína e mecisteína, usadas por mais tempo para prevenir exacerbações de DPOC |
| [8500784](https://pubmed.ncbi.nlm.nih.gov/8500784/) | 1993 | Estudo animal | Fundam Clin Pharmacol | Carbocisteína melhorou o transporte mucociliar em ratos com bronquite por SO₂ |
| [1487227](https://pubmed.ncbi.nlm.nih.gov/1487227/) | 1992 | Estudo animal | Fundam Clin Pharmacol | Efeito sobre parâmetros ventilatórios em ratos com bronquite por SO₂ |
| [19144049](https://pubmed.ncbi.nlm.nih.gov/19144049/) | 2009 | In vitro | Respirology | Carbocisteína elimina espécies reativas de oxigênio |
| [3518737](https://pubmed.ncbi.nlm.nih.gov/3518737/) | 1986 | In vitro | Biol Chem Hoppe-Seyler | Efeito sobre enzimas proteolíticas e oxidação do inibidor de α1-proteinase |
| [23291681](https://pubmed.ncbi.nlm.nih.gov/23291681/) | 2013 | Relato de caso | Intern Med | Pneumonia induzida por L-carbocisteína em paciente com síndrome CATCH22 |

## Informações de Comercialização no Brasil

Todos os 14 registros estão cancelados; não há produto comercializado atualmente. Principais registros:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 118190009 | Mucolab | — | Expectorantes |
| Registro 125680034 | Carbocisteína | — | Expectorantes balsâmicos e mucolítico |
| Registro 143810037 | Carbocin | — | Expectorantes |
| Registro 138410034 | Mucobronq | — | Expectorantes balsâmicos e mucolítico |
| Registro 103700180 | Fluitoss | — | Expectorantes simples |

## Considerações de Segurança

- **Contraindicação (grafo de conhecimento, não texto de bula)**: doença ulcerosa péptica ativa.
- **Evento adverso descrito na literatura**: relato de caso de pneumonia induzida por L-carbocisteína (paciente com síndrome CATCH22), com teste de estimulação linfocitária positivo.
- **Interações medicamentosas**: nenhuma interação encontrada na consulta realizada.

Consulte a bula para as demais informações de segurança.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Para a gota, não há ensaios, literatura nem mecanismo plausível (nível L5). A pontuação alta do modelo é um provável artefato do grafo, possivelmente por associação com doenças do metabolismo de purinas.
- A única previsão com respaldo real é a bronquite (L3, "Proceed with Guardrails"), mas ela é basicamente a indicação original. Além disso, não há registro ativo no Brasil.

**Para prosseguir, é necessário:**
- Obter dados do mecanismo de ação (consulta à API do DrugBank).
- Baixar e analisar as bulas na ANVISA para advertências e contraindicações (lacuna bloqueante para a triagem de segurança).
- Para a gota: gerar evidência pré-clínica de um elo com o metabolismo do urato ou a inflamação gotosa antes de qualquer avanço.
- Para a bronquite: verificar fase e tamanhos de efeito dos estudos (apenas títulos e resumos parciais estavam disponíveis) e esclarecer o motivo do cancelamento dos registros.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

