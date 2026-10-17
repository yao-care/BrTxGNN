---
layout: default
title: Famotidine
parent: Evidência Moderada (L3-L4)
nav_order: 311
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-13
description: "Famotidine: nova indicação prevista, Refluxo duodenogástrico (Duodenogastric Reflux) (nível de evidência L4). Indicação original: Antiácidos e antiulcerosos"
monitor_inn: "Famotidine"
predicted_indications: ["duodenal obstruction", "active peptic ulcer disease", "gastrojejunal ulcer", "peptic ulcer perforation", "abnormality of glucagon secretion", "multiple endocrine neoplasia", "acne (disease)"]
---

# Famotidine
{: .fs-9 }

Nível de evidência: **L4** | Indicações previstas: **10** 
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

# Famotidina: De antiácido e antiulceroso para refluxo duodenogástrico

## Resumo em Uma Frase

A famotidina é um antagonista dos receptores H2 da histamina, originalmente usado como antiácido e antiulceroso.
O modelo TxGNN prevê que ela pode ser eficaz para **refluxo duodenogástrico (duodenogastric reflux)**.
Até o momento, essa direção é apoiada por **0 ensaios clínicos** e **2 publicações**, ambas de baixo nível de evidência.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antiácidos e antiulcerosos |
| Nova Indicação Prevista | Refluxo duodenogástrico (Duodenogastric Reflux) |
| Pontuação de Previsão TxGNN | 99,99% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Somente registros cancelados |
| Número de Registros | 2 (ambos cancelados) |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a famotidina é um antagonista dos receptores H2 que reduz a secreção de ácido gástrico. Sua eficácia como antiácido e antiulceroso é estabelecida, e mecanisticamente ela pode ser aplicável ao refluxo duodenogástrico.

A relação entre a indicação original e a nova é plausível, mas **indireta**. Ao reduzir a acidez, a famotidina pode diminuir a carga ácida e a lesão da mucosa em condições de refluxo. No refluxo duodenogástrico, porém, o problema central é o retorno de conteúdo duodenal (como a bile) ao estômago, e a famotidina não atua sobre esse componente.

As duas publicações encontradas são pequenas ou de baixo nível. Não há ensaios clínicos registrados. A pontuação alta do modelo, portanto, reflete sobretudo a proximidade na rede de conhecimento, e não evidência clínica direta.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [12532466](https://pubmed.ncbi.nlm.nih.gov/12532466/) | 2003 | Estudo clínico (pacientes críticos) | World J Gastroenterol | Investigou o efeito da famotidina sobre o refluxo gastroesofágico e o duodeno-gastro-esofágico em pacientes graves, além dos possíveis mecanismos e fatores associados. O resumo disponível não traz os resultados. |
| [16259441](https://pubmed.ncbi.nlm.nih.gov/16259441/) | 2004 | Relato clínico/revisão (em russo) | Eksp Klin Gastroenterol | Avaliou famotidina 20 mg, duas vezes ao dia, em estágios iniciais da doença do refluxo gastroduodenal (graus 0 e 1 da escala de Savary-Miller), com base em avaliação clínica e endoscópica. O resumo disponível não traz os resultados. |

---

## Informações de Comercialização no Brasil

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 105730144 (cancelado) | FAMOX | Não informada | Antiácidos e antiulcerosos |
| Registro nº 105730052 (cancelado) | FAMOX | Não informada | Não informada |

Os dois registros encontrados estão cancelados, portanto não há produto de famotidina com registro válido neste conjunto de dados.

---

## Considerações de Segurança

- **Contraindicações sugeridas pelo grafo de conhecimento** (relações fármaco-doença do TxGNN/PrimeKG, não texto de bula): doença renal e função renal comprometida, nefrolitíase, nefrocalcinose, doença hepática, doença da vesícula biliar, sarcoidose, hiperparatireoidismo, hipercalcemia, doença do metabolismo do fósforo, doenças diarreicas, constipação, lesões ósseas metastáticas líticas, câncer e neoplasias gástricas (incluindo adenocarcinoma difuso e linite plástica). Estas são associações do modelo e devem ser confirmadas na bula.
- **Interações medicamentosas**: foram identificadas 100 interações; as primeiras 20 listadas são, em sua maioria, de gravidade moderada. Entre elas:
  - Moderadas: abiraterona, acalabrutinibe, tramadol, abarelix, acetohexamida, adenosina, salbutamol, alfuzosina, aminofilina, amiodarona, amissulprida, amitriptilina, amoxapina, anagrelida, apalutamida, apomorfina, arformoterol e aripiprazol.
  - Leves: ácido alendrônico e hidróxido de alumínio.

Para advertências e contraindicações oficiais, consulte a bula.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
- A ligação mecanística é plausível, mas indireta, pois a famotidina não atua sobre o refluxo de bile ou conteúdo duodenal. A evidência se limita a duas publicações pequenas ou de baixo nível, sem ensaios registrados.
- Todos os registros brasileiros estão cancelados, e a segurança não pôde ser avaliada a partir da bula.

**Para prosseguir, é necessário:**
- Obter a bula na ANVISA, com advertências e contraindicações oficiais, para a triagem de segurança.
- Obter dados do mecanismo de ação (por exemplo, no DrugBank) para analisar a ligação mecanística.
- Avaliar os resultados completos dos dois estudos e buscar ensaios controlados em refluxo duodenogástrico.
- Verificar a disponibilidade regulatória no Brasil, já que não há registro válido.
- Confirmar a relevância clínica frente a alternativas, como os inibidores da bomba de prótons, e a necessidade de agentes que atuem sobre o conteúdo biliar.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

