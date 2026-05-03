---
layout: default
title: Centella Asiatica
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 10
---

# Centella Asiatica
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

O skill é sobre gestão de pipeline de treinamento e deploy — não se aplica à geração de relatório. Prossigo diretamente com o relatório conforme as instruções do prompt.

---

# Centella asiatica: Da cicatrização de feridas à insônia

## Resumo em Uma Frase

Centella asiatica (Gotu Kola / Erva-tigre) é uma planta medicinal com longa tradição de uso na medicina Ayurvédica e asiática, principalmente para cicatrização de feridas, condições de pele e melhora da microcirculação, com 16 registros ativos no Brasil. O modelo TxGNN prevê que pode ser eficaz para **insônia (Insomnia Disease)**, com pontuação de predição de **99,94%**, atualmente apoiado por **2 ensaios clínicos** e **1 publicação** nesta direção. A evidência disponível, contudo, é ainda de caráter pré-clínico (modelo animal com peixe-zebra) e os ensaios clínicos identificados não foram desenhados especificamente para insônia com Centella asiatica isolada.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Cicatrização de feridas, condições de pele e suporte microcirculatório (uso tradicional e aprovado) |
| Nova Indicação Prevista | Insônia (Insomnia Disease) |
| Pontuação de Previsão TxGNN | 99,94% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 16 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste pacote de evidências. Com base no conhecimento farmacológico estabelecido na literatura, Centella asiatica contém compostos triterpênicos principais — asiaticoside, madecassoside, ácido asiático e ácido madecássico — responsáveis por ações anti-inflamatórias, antioxidantes, neuroprotetoras e de modulação da síntese de colágeno. Esses mecanismos justificam o uso aprovado na cicatrização de feridas, úlceras varicosas, e condições inflamatórias da pele.

A hipótese mecanística para insônia apoia-se em duas vias principais identificadas em estudos pré-clínicos: (1) modulação positiva do receptor GABA-A — mecanismo análogo ao das benzodiazepinas — que promoveria sedação e facilitação da manutenção do sono; e (2) inibição do eixo HPA (hipotálamo-hipófise-adrenal), reduzindo os níveis de cortisol noturno que frequentemente comprometem o início e a qualidade do sono. Adicionalmente, o estudo em larvas de peixe-zebra (PMID 38812527) demonstrou que o extrato etanólico de C. asiatica inibiu a sinalização de orexina e as vias MAPK/ERK e p38, moléculas centrais do sistema de alerta circadiano.

No entanto, essas hipóteses mecanísticas carecem inteiramente de validação em estudos humanos. A evidência mais robusta disponível para insônia provém de um modelo pré-clínico com larvas de peixe-zebra, e os dois ensaios clínicos identificados não foram desenhados especificamente para avaliar o efeito de Centella asiatica isolada sobre o sono em pacientes com insônia. A alta pontuação do TxGNN (99,94%) reflete provavelmente a sobreposição de mecanismos neurológicos detectada na rede de conhecimento — especialmente a proximidade com transtornos de ansiedade, para os quais a evidência clínica é consideravelmente mais sólida (L3).

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|-----------------|------|--------|---------------|--------------------|
| [NCT07274371](https://clinicaltrials.gov/study/NCT07274371) | NA | Em andamento (sem novas inscrições) | 30 | Massagem nos pés com óleo de Brahmi–Gotu Kola em mulheres perimenopáusicas (40–55 anos); sono é desfecho secundário; intervenção tópica e em formulação combinada — não permite isolar contribuição de C. asiatica |
| [NCT04872946](https://clinicaltrials.gov/study/NCT04872946) | NA | Concluído | 74 | Suplementação oral + tópica para saúde da pele e bem-estar; insônia não é desfecho principal ou secundário; relevância para insônia é mínima — provavelmente falso-positivo por correspondência de palavras-chave |

> **Nota:** Nenhum ensaio foi desenhado especificamente para tratar insônia com Centella asiatica isolada em dose padronizada. Ambos receberam grau de relevância **C** pelos avaliadores do pipeline.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [38812527](https://pubmed.ncbi.nlm.nih.gov/38812527/) | 2024 | Modelo Animal (larvas de peixe-zebra) | F1000Research | Extrato etanólico de C. asiatica reduziu comportamento de insônia em modelo de larvas de peixe-zebra; mecanismo envolve inibição de orexina, ERK1/2, Akt e p38-MAPK — sinalizadores-chave do sistema de alerta circadiano |

---

## Informações de Comercialização no Brasil

Centella asiatica possui **16 registros ativos** na ANVISA, confirmando ampla disponibilidade no mercado brasileiro. Os detalhes individuais de cada registro (número de registro, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis nos dados processados neste relatório. Recomenda-se consulta direta ao [portal de consulta de medicamentos da ANVISA](https://consultas.anvisa.gov.br/) para obter a listagem completa e as bulas correspondentes.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A evidência atual para o uso de Centella asiatica em insônia é de nível **L4** — restrita a um estudo pré-clínico com larvas de peixe-zebra e dois ensaios clínicos de relevância periférica (grau C) não desenhados para esta indicação. Embora o mecanismo hipotético (modulação GABA-A e supressão do eixo HPA) seja biologicamente plausível e internamente coerente, nenhum estudo clínico controlado avaliou diretamente o efeito de Centella asiatica sobre insônia em humanos.

**Para prosseguir, é necessário:**
- Ensaio clínico randomizado e controlado (Phase 2) desenhado especificamente para insônia, com Centella asiatica oral em extrato padronizado e dose definida
- Caracterização do mecanismo de ação em humanos — especialmente modulação do receptor GABA-A (polissonografia + marcadores de cortisol noturno)
- Obtenção dos dados de segurança completos (advertências, contraindicações, interações medicamentosas) diretamente das bulas registradas na ANVISA
- Estudo de farmacocinética oral para estabelecer biodisponibilidade dos triterpenos (asiaticoside, madecassoside) e correlacioná-la com efeito sedativo em humanos
- Avaliação prioritária das indicações com evidência mais robusta: **ansiedade** (rank 2, L3) e **transtorno de ansiedade** (rank 6, L3) apresentam um ensaio Phase 2 concluído (NCT03482063, n=141), um estudo clínico não randomizado em GAD (PMID 20677602), e múltiplas revisões sistemáticas — constituindo base mais sólida para desenvolvimento clínico imediato
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

