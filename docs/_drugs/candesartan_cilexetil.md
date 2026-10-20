---
layout: default
title: Candesartan Cilexetil
parent: Apenas Predição do Modelo (L5)
nav_order: 185
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
description: "Candesartan Cilexetil: nova indicação prevista, Hipertensão renovascular maligna (malignant renovascular hypertension) (nível de evidência L5). Indicação original: Anti-hipertensivos simples"
monitor_inn: "candesartan cilexetil"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
---

# Candesartan Cilexetil
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **5** 
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

# Candesartana cilexetila: De anti-hipertensivo para hipertensão renovascular maligna

## Resumo em Uma Frase

Candesartana cilexetila é um bloqueador do receptor de angiotensina II do tipo 1 (BRA), originalmente registrado na ANVISA como anti-hipertensivo.
O modelo TxGNN prevê que pode ser eficaz para **hipertensão renovascular maligna (malignant renovascular hypertension)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando diretamente esta direção; trata-se de uma previsão computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Anti-hipertensivos simples |
| Nova Indicação Prevista | Hipertensão renovascular maligna (malignant renovascular hypertension) |
| Pontuação de Previsão TxGNN | 99,68% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Somente registros cancelados |
| Número de Registros | 17 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a candesartana cilexetila é um pró-fármaco da classe dos BRAs: bloqueia o receptor AT1 da angiotensina II, reduzindo vasoconstrição e pressão arterial. Sua eficácia como anti-hipertensivo é reconhecida.

A hipertensão renovascular maligna é impulsionada pela ativação do sistema renina-angiotensina, o que torna o racional mecanístico plausível e coerente com o uso original do fármaco. Porém, a pontuação do TxGNN (0,997) é apenas uma previsão computacional.

Há uma preocupação importante de segurança: na estenose bilateral da artéria renal ou em rim único, os BRAs podem precipitar lesão renal aguda. A própria base de conhecimento do modelo registra "obstrução da artéria renal" entre as contraindicações. Assim, a indicação prevista exige cautela especial.

### Outras indicações previstas (todas em nível L5, recomendação Hold)

| Posição | Indicação prevista | Pontuação TxGNN | Observação |
|------|------|------|------|
| 2 | Doença renal hipertensiva maligna | 99,68% | Sobrepõe-se amplamente ao uso anti-hipertensivo original; pouca novidade |
| 3 | Hipertensão pulmonar de mecanismo multifatorial incerto | 99,67% | Racional teórico (remodelamento vascular pulmonar); risco de hipotensão sistêmica |
| 4 | Hipertensão pulmonar por doença pulmonar e/ou hipóxia | 99,67% | Duas publicações indiretas (ver abaixo) |
| 5 | Síndrome de Braddock | 99,56% | Sem vínculo mecanístico claro; pode refletir apenas conectividade do grafo |

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Não há literatura para a indicação principal (hipertensão renovascular maligna). Para a 4ª indicação prevista (hipertensão pulmonar por doença pulmonar/hipóxia), foram recuperados dois artigos, ambos indiretos:

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [31396238](https://pubmed.ncbi.nlm.nih.gov/31396238/) | 2019 | Pré-clínico (camundongo) | Frontiers in Immunology | Candesartana cilexetila, com ação anti-inflamatória, melhorou desfechos neurológicos em modelo murino de hipóxia neonatal; outra área de doença |
| [21423692](https://pubmed.ncbi.nlm.nih.gov/21423692/) | 2011 | Pré-clínico (fórmula herbal) | Evidence-based Complementary and Alternative Medicine | Hachimijiogan (fórmula Kampo) reduziu disfunção renal em ratos com rim remanescente, com envolvimento de HIF-1α, comparado a um BRA; não avalia candesartana em hipertensão pulmonar |

## Informações de Comercialização no Brasil

Todos os 17 registros encontram-se cancelados; não há registro válido atualmente. Principais registros (5 de 17):

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 102351089 | Candesartana cilexetila | Não informada | Anti-hipertensivos simples |
| Registro nº 189770010 | Atacand | Não informada | Anti-hipertensivos simples |
| Registro nº 105831048 | Vecande | Não informada | Anti-hipertensivos simples |
| Registro nº 100330197 | Venzer | Não informada | Anti-hipertensivos simples |
| Registro nº 189770011 | Atacand HCT | Não informada | Anti-hipertensivos |

Os demais registros incluem associações com hidroclorotiazida (por exemplo, Venzer HCT, Vecande HCT, Procordis HCTZ, Angiotensil HCT).

## Considerações de Segurança

- **Contraindicações (base de conhecimento do TxGNN, não extraídas da bula)**: pancreatite, doença hepática, doença da vesícula biliar, lúpus eritematoso sistêmico (inclusive pediátrico), deficiência de potássio, diabetes mellitus, cetoacidose diabética, hiperuricemia, distúrbios hipotensivos, hiperparatireoidismo, osteíte fibrosa, coma hepático, encefalopatia hepática, icterícia neonatal, anúria, gota, hipercalcemia, nefrocalcinose, distúrbios do metabolismo do fósforo, **obstrução da artéria renal** e comprometimento da função renal. Parte desses itens provavelmente se refere aos produtos associados à hidroclorotiazida, e não à candesartana isolada.
- **Interações medicamentosas**: nenhuma interação foi encontrada na consulta realizada.

Para advertências e contraindicações oficiais, consulte a bula.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Todas as indicações previstas estão em nível L5, sem ensaios clínicos nem literatura direta. Além disso, a indicação principal sobrepõe-se ao uso anti-hipertensivo original e envolve risco renal relevante (estenose da artéria renal), e todos os registros no Brasil estão cancelados.

**Para prosseguir, é necessário:**
- Obter e analisar a bula na ANVISA (advertências e contraindicações), pois a triagem de segurança está bloqueada sem esses dados
- Complementar os dados de mecanismo de ação (por exemplo, via DrugBank)
- Realizar busca sistemática de ensaios clínicos e literatura específicos de candesartana em hipertensão renovascular maligna
- Avaliar o risco de lesão renal aguda em estenose bilateral da artéria renal ou rim único
- Esclarecer a situação regulatória atual no Brasil (todos os registros cancelados) e a viabilidade de novo registro
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

