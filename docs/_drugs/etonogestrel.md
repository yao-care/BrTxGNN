---
layout: default
title: Etonogestrel
parent: 僅模型預測 (L5)
nav_order: 244
evidence_level: L5
indication_count: 10
---

# Etonogestrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Etonogestrel: Da contracepção à amenorreia

## Resumo em Uma Frase

Etonogestrel é um progestagênio sintético de terceira geração, utilizado em implantes contraceptivos subdérmicos (Nexplanon/Implanon) para prevenção de gravidez.
O modelo TxGNN prevê potencial eficácia para **Amenorreia (Amenorrhea)**, com **1 ensaio clínico** de fase 3 concluído e **1 publicação** relevante apoiando essa direção.
Importante ressaltar: a amenorreia é um efeito colateral bem documentado do implante — a hipótese de reposicionamento mais plausível seria o uso *terapêutico intencional* desse efeito em condições como endometriose ou sangramento uterino anormal.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Contracepção (dados detalhados de registro ANVISA pendentes) |
| Nova Indicação Prevista | Amenorreia (Amenorrhea) |
| Pontuação de Previsão TxGNN | 99.84% |
| Nível de Evidência | L3 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 8 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Etonogestrel atua suprimindo o eixo hipotálamo-hipófise-ovário (HPO), inibindo o pico de LH e bloqueando a ovulação. Secundariamente, induz atrofia endometrial e altera o muco cervical. Esses mecanismos fazem parte do conhecimento farmacológico estabelecido da classe dos progestagênios — os dados detalhados de MOA do DrugBank (DB00294) ainda estão pendentes de consulta formal.

A amenorreia ocorre em aproximadamente 20–30% das usuárias do implante de etonogestrel após um ano de uso, resultado direto da supressão do ciclo menstrual e atrofia endometrial. Essa característica tem relevância clínica real em condições onde a supressão menstrual é desejada: endometriose, menorragia, sangramento uterino disfuncional e dismenorreia severa. A previsão do TxGNN captura essa sobreposição farmacológica de forma razoável.

No entanto, é fundamental esclarecer a direção da hipótese de reposicionamento: etonogestrel *causa* amenorreia (efeito colateral documentado), mas não existe evidência de que ele *trate* amenorreia patológica (ex.: amenorreia hipotalâmica, síndrome de Asherman). A hipótese clinicamente coerente seria "uso deliberado do implante para indução terapêutica de amenorreia em populações específicas", o que representa uma indicação expandida, não um reposicionamento clássico. Essa distinção precisa ser formalizada antes de qualquer avanço.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|------------------|------|--------|---------------|--------------------|
| [NCT04626596](https://clinicaltrials.gov/study/NCT04626596) | Phase 3 | Concluído | 498 | Avalia eficácia e segurança do implante de etonogestrel em uso estendido (4.º e 5.º anos pós-inserção) em mulheres ≤35 anos. Amenorreia é resultado secundário documentado — o ensaio fornece dados populacionais robustos sobre incidência de amenorreia, mas o endpoint primário é eficácia contraceptiva, não tratamento de amenorreia como doença. |

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | RCT | Contraception | Ensaio randomizado multicêntrico (n=200, China) comparando Implanon (bastão único) vs. Norplant (6 cápsulas) por 2–4 anos. Nenhuma gravidez registrada em ambos os grupos. Avalia padrões de sangramento e amenorreia como desfechos secundários, documentando diferenças entre os dois implantes progestagênicos. |

> **Nota sobre qualidade dos dados**: Uma segunda publicação presente na base de dados para esta indicação (PMID [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/), 2021) refere-se a um ensaio clínico sobre COVID-19 com o composto BIO101, sem qualquer relação com etonogestrel ou amenorreia. Esse registro foi excluído por ausência de relevância — sua inclusão indica ruído no processo de recuperação de evidências para este candidato.

---

## Informações de Comercialização no Brasil

O sistema ANVISA registra **8 licenças ativas** para Etonogestrel no Brasil. Os detalhes individuais (número de registro, nome comercial, forma farmacêutica e texto da indicação aprovada) não estão disponíveis no Evidence Pack atual — todos os campos de dados regulatórios estão pendentes de complementação. Recomenda-se consulta direta à base de dados ANVISA para obtenção dessas informações.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN tem plausibilidade mecanística, pois a amenorreia induzida por etonogestrel é um fenômeno farmacológico bem documentado. Contudo, a hipótese de reposicionamento ainda não está claramente definida — é necessário distinguir entre "tratar amenorreia patológica" e "usar amenorreia induzida como recurso terapêutico para outras condições". Além disso, a ausência de dados de segurança da ANVISA (gap classificado como *Blocking*) impede a progressão para avaliação clínica formal.

**Para prosseguir, é necessário:**
- Formalizar a hipótese de reposicionamento: definir a população-alvo (ex.: pacientes com endometriose ou menorragia) e o endpoint clínico específico (ex.: redução de sangramento, controle da dor)
- Obter dados completos de advertências e contraindicações via download e análise da bula ANVISA (PDF)
- Complementar os dados de registro ANVISA: número de licença, nome comercial, forma farmacêutica e indicação aprovada para cada um dos 8 registros
- Confirmar o mecanismo de ação detalhado via consulta à API DrugBank (DB00294)
- Realizar busca bibliográfica direcionada para uso intencional do implante de etonogestrel como supressor menstrual terapêutico (ex.: endometriose, menorragia, dismenorreia)
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

