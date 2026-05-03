---
layout: default
title: Avibactam
parent: 僅模型預測 (L5)
nav_order: 84
evidence_level: L5
indication_count: 10
---

# Avibactam
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

# Avibactam: De infecções bacterianas por Gram-negativos resistentes para pneumonia estreptocócica

## Resumo em Uma Frase

Avibactam é um inibidor de β-lactamase de nova geração, utilizado em combinação com antibióticos β-lactâmicos (como ceftazidima) para o tratamento de infecções bacterianas graves causadas por micro-organismos Gram-negativos multirresistentes, sendo comercializado no Brasil com 3 registros ativos na ANVISA.
O modelo TxGNN prevê que pode ser eficaz para **Pneumonia Estreptocócica (Streptococcal Pneumonia)**, porém atualmente sem **ensaios clínicos** nem **publicações científicas** apoiando diretamente esta direção.
A análise mecanística do próprio Evidence Pack aponta que esta previsão é **provavelmente um falso positivo**, dado que o *Streptococcus pneumoniae* é uma bactéria Gram-positiva e não expressa as β-lactamases-alvo do Avibactam.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções por bactérias Gram-negativas resistentes (terapia combinada com β-lactâmico) |
| Nova Indicação Prevista | Pneumonia Estreptocócica (Streptococcal Pneumonia) |
| Pontuação de Previsão TxGNN | 99,70% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 3 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Os dados detalhados de mecanismo de ação (MOA) não estão disponíveis nesta versão do Evidence Pack. Com base no conhecimento farmacológico estabelecido, o Avibactam é um inibidor de β-lactamase não-β-lactâmico (derivado diazabiciclooct-2-eno) que atua por ligação covalente **reversível** às enzimas β-lactamase das classes A (incluindo KPC e ESBL), C (AmpC) e parcialmente D (OXA). Ao inativar essas enzimas, o Avibactam restaura a atividade do antibiótico parceiro contra bactérias Gram-negativas que seriam de outra forma resistentes — não possuindo, por si só, atividade antibacteriana intrínseca relevante.

A relação mecanística entre a indicação conhecida e a **pneumonia estreptocócica** é biologicamente incompatível. O *Streptococcus pneumoniae* é uma bactéria **Gram-positiva** e não expressa as β-lactamases das classes A, C ou D que são os alvos do Avibactam. A resistência do pneumococo aos β-lactâmicos ocorre principalmente por alteração nas proteínas de ligação à penicilina (PBPs), mecanismo completamente distinto — sobre o qual o Avibactam não tem qualquer ação.

A alta pontuação do TxGNN (99,70%) reflete, muito provavelmente, adjacência ampla no grafo de conhecimento entre os nós de "infecção bacteriana" e "pneumonia", e não uma aplicabilidade mecanística real. O próprio Evidence Pack classifica explicitamente esta previsão como **provável falso positivo**, observando que o alto score pode ser artefato da sobreposição semântica do contexto "infecção respiratória" no grafo de treinamento.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Avibactam em pneumonia estreptocócica.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para Avibactam em pneumonia estreptocócica.

---

## Informações de Comercialização no Brasil

O Avibactam possui **3 registros** na ANVISA com status de comercializado. Os detalhes individuais dos registros (números de registro, nomes comerciais, formas farmacêuticas e textos de indicação aprovada) não estavam disponíveis nesta versão do Evidence Pack. Recomenda-se consulta direta ao portal da ANVISA — Consulta de Medicamentos — para acesso às informações completas dos registros.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN para pneumonia estreptocócica não possui suporte mecanístico (o Avibactam atua exclusivamente sobre β-lactamases de bactérias Gram-negativas, enquanto o *S. pneumoniae* é Gram-positivo e utiliza mecanismo de resistência distinto), não existem ensaios clínicos nem publicações direcionadas a esta indicação, e a análise interna do Evidence Pack classifica o resultado como provável falso positivo de grafo de conhecimento.

**Para prosseguir, é necessário:**
- Confirmar o mecanismo de ação completo via consulta à API do DrugBank (lacuna de dados de grau "High" identificada — DG002)
- Recuperar os dados completos dos 3 registros ANVISA, incluindo indicações aprovadas e nomes comerciais, por meio de download e análise das bulas em PDF (lacuna de dados de grau "Blocking" — DG001)
- Avaliar indicações de maior plausibilidade biológica identificadas no mesmo Evidence Pack: a previsão de rank 7 (*infecção por S. aureus*) apresenta nível de evidência L4 com 2 ensaios clínicos e até 20 publicações relacionadas e base mecanística parcial via ceftarolina-avibactam; e a previsão de rank 3/8 (tuberculose ureteral/renal) possui fundamento teórico por inibição da BlaC de *M. tuberculosis*, merecendo análise dedicada antes de descarte
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

