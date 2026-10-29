---
layout: default
title: Cefoxitin
parent: Apenas Predição do Modelo (L5)
nav_order: 209
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-29
description: "Cefoxitin: nova indicação prevista, Otite média infecciosa (infectious otitis media) (nível de evidência L5). Indicação original: Cefalosporinas"
monitor_inn: "cefoxitin"
predicted_indications: ["infectious otitis media", "urinary tract infection (disease)", "chronic otitis media", "suppurative otitis media", "middle ear disease", "Ureaplasma urethritis", "toxocariasis", "otosalpingitis", "non-suppurative otitis media"]
---

# Cefoxitin
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **9** 
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

## Cefoxitina: Das cefalosporinas à otite média infecciosa
{: .text-alpha }

## Resumo em Uma Frase

Cefoxitina é um antibiótico da classe das cefamicinas (cefalosporinas), registrado na ANVISA sob a categoria "CEFALOSPORINAS".
O modelo TxGNN prevê que pode ser eficaz para **otite média infecciosa (infectious otitis media)**, mas, até o momento, **não há ensaios clínicos** e apenas **1 publicação** (uma revisão sobre MRSA, que não sustenta a eficácia) está associada a esta previsão.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Cefalosporinas (texto de indicação registrado na ANVISA) |
| Nova Indicação Prevista | Otite média infecciosa (infectious otitis media) |
| Pontuação de Previsão TxGNN | 0,9930 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 3 de 4) |
| Número de Registros | 4 (ativos: 3) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no conjunto de dados compilado. Segundo informações conhecidas, a cefoxitina é uma cefamicina beta-lactâmica que inibe a síntese da parede celular bacteriana, com atividade contra bactérias Gram-negativas e anaeróbias, incluindo o grupo *Bacteroides fragilis*.

A relação com a nova indicação é plausível no plano conceitual: a otite média é frequentemente de origem bacteriana, e um antibiótico de amplo espectro poderia, em tese, ser aplicável.

Há, porém, uma ressalva importante. A única publicação associada é uma revisão sobre MRSA (*Staphylococcus aureus* resistente à meticilina). O MRSA é intrinsecamente resistente à cefoxitina (a própria cefoxitina é usada como marcador para detectar MRSA), portanto este artigo não sustenta eficácia. A pontuação alta do modelo é uma previsão sem respaldo clínico.

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para a otite média infecciosa.

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [33061472](https://pubmed.ncbi.nlm.nih.gov/33061472/) | 2020 | Revisão | Infection and Drug Resistance | Revisão sobre epidemiologia, virulência e resistência do MRSA, que cita a otite média entre as infecções que causa; não avalia a cefoxitina como tratamento |

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 116370123 | CEFOXITINA SÓDICA | Não informada | CEFALOSPORINAS |
| Registro nº 155620007 | KEFOX | Não informada | CEFALOSPORINAS |
| Registro nº 116370188 | CEFTON | Não informada | CEFALOSPORINAS |
| Registro nº 100410203 | CEFOXITINA SÓDICA | Não informada | CEFALOSPORINAS |

O medicamento é comercializado no Brasil, com 4 registros válidos de 4.

## Considerações de Segurança

- **Contraindicações (previstas no grafo de conhecimento, não extraídas da bula)**: doença renal, piureter, colite por *Clostridium difficile*, enterocolite necrosante perinatal e colite.
- **Interações Medicamentosas**: foram identificadas 35 interações. As de nível moderado incluem:
  - aminoglicosídeos (canamicina, neomicina, estreptomicina);
  - picossulfato de sódio;
  - dicumarol (anticoagulante).

  Há também uma interação de nível leve (heparina) e várias de nível não classificado (por exemplo, vancomicina, metronidazol, omeprazol, dexametasona e morfina).

Consulte a bula para as advertências e contraindicações oficiais, que não estavam disponíveis nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão para otite média infecciosa tem pontuação alta, mas é apenas teórica (L5): não há ensaios clínicos, a única publicação não sustenta a eficácia e o MRSA é resistente à cefoxitina. No Brasil, o medicamento é comercializado, com 4 registros válidos de 4.

**Para prosseguir, é necessário:**
- Estudos clínicos ou dados de suscetibilidade dos patógenos típicos da otite média (por exemplo, *S. pneumoniae*, *H. influenzae*, *M. catarrhalis*) à cefoxitina.
- Dados do mecanismo de ação a partir do DrugBank.
- Bula da ANVISA com advertências e contraindicações, para a triagem de segurança.
- Avaliação da viabilidade regulatória e comercial, dado que não há registro vigente no Brasil.

**Observações sobre outras indicações previstas** (como contexto, sem alterar a decisão acima):
- **Infecção do trato urinário**: nível L3, com um ensaio de fase 4 (NCT02474706, cefoxitina vs. imipenem/cilastatina em ITU por *E. coli* produtora de ESBL) encerrado precocemente com apenas 6 participantes, sem dados de eficácia utilizáveis. Há estudos históricos (1978-1979) e um modelo murino favorável. Classificada como questão de pesquisa, e não como novo reposicionamento.
- **Uretrite gonocócica**: nível L2, com diversos estudos clínicos históricos (1979-1983) mostrando cura com dose única. Trata-se de um uso já conhecido, hoje preterido em favor da ceftriaxona.
- **Uretrite por Ureaplasma e toxocaríase**: sem respaldo mecanístico, pois o *Ureaplasma* não possui parede celular e a toxocaríase é uma parasitose; provavelmente artefatos do modelo.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

