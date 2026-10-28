---
layout: default
title: Tenoxicam
parent: Apenas Predição do Modelo (L5)
nav_order: 612
evidence_level: L5
indication_count: 8
monitor_inn: "Tenoxicam"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "headache disorder", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "trigeminal autonomic cephalalgia", "alopecia"]
last_modified_at: 2026-10-28
description: "Tenoxicam: nova indicação prevista, Brachydactyly-syndactyly syndrome (nível de evidência L5). Indicação original: Não consta nos dados locais"
---

# Tenoxicam
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

## Tenoxicam: Brachydactyly-syndactyly syndrome
{: .text-alpha }

## Resumo em Uma Frase

Tenoxicam é um anti-inflamatório não esteroide (AINE) da classe dos oxicams, associado na base de conhecimento do TxGNN a doenças articulares artríticas e artropatias.
O modelo TxGNN prevê que pode ser eficaz para **distúrbio de cefaleia (headache disorder)**, atualmente com **1 ensaio clínico** (Fase 4, ainda sem resultados) e **2 publicações** que tratam do tema de forma indireta, sem estudar o tenoxicam isoladamente.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Não consta nos dados locais |
| Nova Indicação Prevista | Brachydactyly-syndactyly syndrome |
| Pontuação de Previsão TxGNN | 0.9980 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: pelo menos 6) |
| Número de Registros | Pelo menos 20 registros (a lista pode estar incompleta): 6 válidos e 14 cancelados |
| Decisão Recomendada | Proceed with Guardrails |

> Observação: a previsão em primeiro lugar no ranking do modelo (síndrome de braquidactilia-sindactilia) não tem nenhuma evidência e nenhum mecanismo plausível. Por isso, este relatório avalia a previsão mais bem sustentada, o distúrbio de cefaleia (3ª posição), que é a única com um ensaio clínico direto.

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação neste conjunto de dados. Segundo informações conhecidas, o tenoxicam é um AINE da classe dos oxicams que inibe as enzimas COX-1 e COX-2, reduzindo a síntese de prostaglandinas.

Esse mecanismo é plausível para cefaleias: as prostaglandinas participam da sensibilização periférica e central e da inflamação neurogênica envolvidas na enxaqueca e em outras cefaleias primárias. Os AINEs são uma classe estabelecida no tratamento da crise aguda de enxaqueca. A relação com a indicação original é, portanto, a ação analgésica e anti-inflamatória comum a toda a classe.

**Atenção ao nível de evidência:** o ensaio clínico encontrado estuda diretamente o tenoxicam em crise aguda de enxaqueca, que é um tipo de distúrbio de cefaleia, mas ainda não há resultados. As duas publicações discutem AINEs e cefaleias em geral, sem avaliar o tenoxicam isoladamente. Assim, o nível L4 é um teto conservador e reflete sobretudo a plausibilidade mecanística; o nível L3 não se justifica, pois não há estudo observacional ou revisão sistemática específicos do tenoxicam.

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT06786650](https://clinicaltrials.gov/study/NCT06786650) | Phase 4 | Ativo, sem recrutamento | 100 | Compara a eficácia analgésica e os efeitos adversos de tenoxicam intravenoso e ibuprofeno intravenoso em crise aguda de enxaqueca. Sem resultados disponíveis. |

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [27813032](https://pubmed.ncbi.nlm.nih.gov/27813032/) | 2016 | Coorte | Agri (Journal of the Turkish Society of Algology) | Avalia a eficácia de triptanos, AINEs e sua combinação, isolados ou associados, no tratamento de crises de enxaqueca, incluindo a recorrência da cefaleia na mesma crise. |
| [18345416](https://pubmed.ncbi.nlm.nih.gov/18345416/) | 2007 | Coorte (revisão de prontuários) | Arquivos de Neuro-Psiquiatria | Análise de 109 pacientes com cefaleias primárias agudas em um hospital universitário brasileiro; enxaqueca provável foi o diagnóstico mais comum (47,7%). |

## Informações de Comercialização no Brasil

Foram listados 5 dos pelo menos 20 registros localizados (a lista pode estar incompleta). Nenhum traz texto de indicação aprovada nem forma farmacêutica nos dados compilados.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 155840092 (válido) | Tenoxicam (Brainfarma) | Não informada | Não informada |
| Registro nº 102980374 (válido) | Tenoxicam (Cristália) | Não informada | Não informada |
| Registro nº 188300059 (válido) | Tilatil (Viatris) | Não informada | Não informada |
| Registro nº 154230346 (válido) | Titenil (Geolab) | Não informada | Não informada |
| Registro nº 155840238 (válido) | Tiloxineo (Brainfarma) | Não informada | Não informada |

## Considerações de Segurança

- **Alopecia:** há um relato de caso de 1997 (PMID 9303679) descrevendo alopecia como possível efeito adverso do tenoxicam. É um sinal de farmacovigilância, sem relevância direta para cefaleia.
- Não há dados de interações medicamentosas nos dados compilados.

Para advertências e contraindicações, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
- O mecanismo é biologicamente plausível e existe um ensaio de Fase 4 que estuda diretamente o tenoxicam em crise de enxaqueca, mas ele ainda não tem resultados e as demais publicações não são específicas do fármaco. A evidência é preliminar e adequada apenas para avançar como questão de pesquisa.
- As demais previsões do modelo (síndromes congênitas, hipotricose, alopecia) não têm evidência e, no caso da alopecia, há um sinal de segurança em sentido contrário; devem ficar em "Hold".

**Para prosseguir, é necessário:**
- Aguardar e analisar os resultados do ensaio NCT06786650.
- Obter as advertências e contraindicações da bula na ANVISA (lacuna de dados bloqueante para a triagem de segurança).
- Obter dados do mecanismo de ação via DrugBank.
- Verificar se a via de administração (o ensaio usa a via intravenosa) é compatível com as formas farmacêuticas registradas no Brasil.
- Buscar evidências específicas do tenoxicam em cefaleias do tipo trigeminal autonômicas, caso haja interesse nessa extensão (previsão em 7ª posição, apenas com extrapolação de outro AINE).
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

