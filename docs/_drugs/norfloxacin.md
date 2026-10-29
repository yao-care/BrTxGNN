---
layout: default
title: Norfloxacin
parent: Apenas Predição do Modelo (L5)
nav_order: 480
evidence_level: L5
indication_count: 10
monitor_inn: "Norfloxacin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "punctate epithelial keratoconjunctivitis", "premalignant hematological system disease", "diffuse scleroderma", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
last_modified_at: 2026-10-29
description: "Norfloxacin: nova indicação prevista, Síndrome de hiperviscosidade policlonal (nível de evidência L5). Indicação original: Infecções bacterianas (infecção urinária, febre tifoide, disenteria…"
---

# Norfloxacin
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

## Norfloxacino: Das infecções bacterianas à síndrome de hiperviscosidade policlonal
{: .text-alpha }

## Resumo em Uma Frase

Norfloxacino é um antibiótico da classe das fluoroquinolonas, originalmente usado em infecções bacterianas como infecção urinária, disenteria e febre tifoide.
O modelo TxGNN prevê que pode ser eficaz para **síndrome de hiperviscosidade policlonal (polyclonal hyperviscosity syndrome)**, mas **não há nenhum ensaio clínico nem publicação** que apoie esta previsão. A pontuação alta vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, e não evidência biológica.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções bacterianas (infecção urinária, febre tifoide, disenteria, entre outras), conforme relações registradas no grafo de conhecimento; os registros locais não trazem texto de indicação |
| Nova Indicação Prevista | Síndrome de hiperviscosidade policlonal |
| Pontuação de Previsão TxGNN | 0,9970 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: pelo menos 1) |
| Número de Registros | Pelo menos 20 registros de medicamentos de ingrediente único (a lista pode estar incompleta) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação compilados para este relatório. Segundo informações conhecidas, o norfloxacino é uma fluoroquinolona que inibe a DNA girase e a topoisomerase IV bacterianas, e sua atividade antibacteriana é a base de seu uso em infecções urinárias e gastrointestinais.

Não foi identificada relação mecanística plausível com a síndrome de hiperviscosidade policlonal, que envolve produção excessiva de imunoglobulinas e aumento da viscosidade sérica. O norfloxacino não tem efeito conhecido sobre esses processos. A pontuação alta vem do modelo TxGNN (deep learning) e pode refletir semelhanças que o modelo aprendeu entre doenças relacionadas, e não evidência biológica.

Outras previsões do mesmo modelo, com pontuações igualmente altas, também carecem de suporte: hiperamilasemia, analbuminemia congênita e incompatibilidade de grupo sanguíneo. A única hipótese biologicamente plausível entre as dez primeiras é a peste septicêmica (bactéria Gram-negativa sensível a fluoroquinolonas), embora o norfloxacino tenha baixa exposição sistêmica e existam alternativas estabelecidas.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

## Evidências da Literatura

Atualmente não há literatura relacionada com a síndrome de hiperviscosidade policlonal.

## Informações de Comercialização no Brasil

Dos registros listados (lista possivelmente parcial), 2 estão válidos e 18 cancelados. Abaixo, os registros válidos e alguns cancelados. Os registros não trazem forma farmacêutica nem texto de indicação aprovada.

| Número de Registro | Nome Comercial | Situação | Fabricante |
|---------|------|------|-----------|
| Registro nº 109170100 | Norfloxacino | Válido | Medquímica Indústria Farmacêutica Ltda. |
| Registro nº 104810106 | Norfloxacino | Válido | 1Farma Indústria Farmacêutica Ltda. |
| Registro nº 155840328 | Neofloxin | Cancelado | Brainfarma |
| Registro nº 172870202 | Neofloxin | Cancelado | Hypera S.A. |
| Registro nº 100890225 | Uroseptal | Cancelado | Merck S/A |

## Considerações de Segurança

- **Contraindicações e condições de risco (relações registradas no grafo de conhecimento, não texto de bula)**: síndrome do QT longo (inclusive familiar) e torsades de pointes; insuficiência hepática, cirrose e doença hepática; doença renal; epilepsia; transtornos psiquiátricos (ansiedade, psicose, transtorno esquizoafetivo); tendinite e periartrite; neuropatia periférica; rabdomiólise; diabetes mellitus e cetoacidose diabética; trombocitopenia; anemia; deficiência de potássio.
- **Interações Medicamentosas** (100 interações encontradas; principais exemplos):
  - Gravidade maior: hidrocortisona, dexametasona, betametasona, triamcinolona (corticosteroides, com risco de tendinopatia), bupropiona, clorpropamida.
  - Gravidade moderada: antidiabéticos (acarbose, metformina, pioglitazona, alogliptina, canagliflozina, albiglutida), famotidina, loperamida, ácido acetilsalicílico, balsalazida, bisacodil, sais de cálcio e citrato de potássio.
- Para advertências e contraindicações formais, consulte a bula, pois o texto aprovado pela ANVISA não estava disponível.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- Não há ensaios clínicos nem literatura para a síndrome de hiperviscosidade policlonal, não existe mecanismo plausível e o perfil de segurança (restrições em várias condições) é desfavorável. A previsão parece ser um artefato do modelo (nível L5).

**Para prosseguir, é necessário:**
- Obter e analisar a bula aprovada pela ANVISA (advertências e contraindicações), lacuna que bloqueia a triagem de segurança.
- Obter dados do mecanismo de ação a partir do DrugBank.
- Identificar qualquer hipótese biológica ou estudo direto sobre a doença prevista antes de reconsiderar.
- Se houver interesse em reposicionamento, priorizar a peste septicêmica como pergunta de pesquisa, comparando com fluoroquinolonas de maior exposição sistêmica, pois as evidências disponíveis são apenas pré-clínicas e não específicas para o norfloxacino.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

