---
layout: default
title: Amoxicillin
parent: Apenas Predição do Modelo (L5)
nav_order: 62
evidence_level: L5
indication_count: 10
---

# Amoxicillin
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

# Amoxicilina: Da penicilina de amplo espectro à síndrome de hiperviscosidade policlonal

## Resumo em Uma Frase

Amoxicilina é um antibiótico da classe das penicilinas de amplo espectro, originalmente usado no tratamento de infecções bacterianas sistêmicas.
O modelo TxGNN prevê que pode ser eficaz para **síndrome de hiperviscosidade policlonal (polyclonal hyperviscosity syndrome)**, mas **não há nenhum ensaio clínico nem publicação** apoiando esta direção. A previsão é puramente computacional.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Penicilina de amplo espectro |
| Nova Indicação Prevista | Síndrome de hiperviscosidade policlonal (polyclonal hyperviscosity syndrome) |
| Pontuação de Previsão TxGNN | 99,63% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✗ Apenas registros cancelados |
| Número de Registros | 20 (todos cancelados) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, a amoxicilina é um antibiótico beta-lactâmico da classe das penicilinas, cuja eficácia em infecções bacterianas está estabelecida, e age sobre a síntese da parede celular bacteriana.

Para a síndrome de hiperviscosidade policlonal, **não se identifica um vínculo mecanístico plausível**. Essa condição decorre do excesso de imunoglobulinas policlonais, e a amoxicilina não tem atividade conhecida sobre esse processo. A pontuação elevada parece ser um artefato da predição baseada em grafos, sem respaldo clínico ou na literatura.

Outras previsões do modelo também apresentam o mesmo problema. Entre as 10 principais, a maioria (hiperamilasemia, analbuminemia congênita, doenças hematológicas pré-malignas, gamopatia monoclonal, entre outras) não tem mecanismo plausível. As duas exceções com plausibilidade biológica, **peste septicêmica** e **epiglotite**, são infecções bacterianas, mas apoiadas apenas por evidências indiretas (estudos in vitro, modelos animais, revisões e relatos de caso). A epiglotite, em especial, está dentro do uso já existente da classe antibacteriana, não sendo um reposicionamento propriamente dito.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para a síndrome de hiperviscosidade policlonal.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para a síndrome de hiperviscosidade policlonal.

---

## Informações de Comercialização no Brasil

Todos os 20 registros estão **cancelados**; não há registro válido atualmente. Principais registros (5 de 20):

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 170420029 | Amoxicilina | Não informada | Penicilina de amplo espectro |
| Registro nº 167730477 | Polimoxil | Não informada | Penicilina de amplo espectro |
| Registro nº 155840102 | Amoxicilina | Não informada | Penicilina de amplo espectro |
| Registro nº 105730548 | Amoxicilina tri-hidratada | Não informada | Antibióticos sistêmicos simples |
| Registro nº 125680375 | Apluc | Não informada | Penicilina de amplo espectro |

---

## Considerações de Segurança

- **Contraindicações descritas no grafo de conhecimento (não extraídas de bula)**: síndrome do QT longo, torsades de pointes, insuficiência e doenças hepáticas, colestase, porfirias, doença renal, doenças da vesícula biliar, osteoporose, fratura óssea, colite por *Clostridium difficile*, enterocolite necrosante perinatal, miastenia gravis, taquicardia ventricular, mononucleose infecciosa e infecção crônica pelo vírus Epstein-Barr. Esses itens vêm de relações do grafo de conhecimento e devem ser confirmados na bula.
- **Interações medicamentosas** (100 registradas; principais):
  - **Maior gravidade**: metotrexato; vacina viva contra cólera (*Vibrio cholerae* CVD 103-HgR).
  - **Moderada**: doxiciclina, minociclina, demeclociclina, etinilestradiol, estradiol, anisindiona, dicumarol, balsalazida, entecavir, micofenolato de mofetila, probióticos (*Lactobacillus acidophilus*, *Bifidobacterium longum infantis*) e índio-111 oxiquinolina.
  - **Menor**: alopurinol, amilorida, azitromicina, claritromicina, eritromicina.
- **Sinal de segurança na literatura**: relato de anemia hemolítica não imune induzida por amoxicilina em criança com deficiência de glicose-6-fosfato isomerase (PMID 20516363).

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A previsão tem pontuação alta (99,63%), mas não há ensaios, literatura nem vínculo mecanístico plausível (nível L5). Além disso, todos os registros brasileiros estão cancelados.

**Para prosseguir, é necessário:**
- Obter dados do mecanismo de ação (DrugBank) e analisar qualquer vínculo com a hiperviscosidade policlonal.
- Baixar e analisar a bula na ANVISA para advertências e contraindicações (lacuna bloqueante para a triagem de segurança).
- Confirmar a situação regulatória atual no Brasil, já que não há registro válido.
- Considerar priorizar outras previsões com racional biológico, como epiglotite e peste septicêmica, que ainda exigem estudos clínicos diretos.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

