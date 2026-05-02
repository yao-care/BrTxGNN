---
layout: default
title: Relebactam
parent: 僅模型預測 (L5)
nav_order: 426
evidence_level: L5
indication_count: 10
---

# Relebactam
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

Usando `txgnn-pipeline` para orientar o formato do relatório. Procedendo agora com a análise do Evidence Pack e geração do relatório.

---

# Relebactam: De infecções bacterianas gram-negativas à síndrome de hiperviscosidade policlonal

## Resumo em Uma Frase

Relebactam é um inibidor de β-lactamase utilizado em combinação com imipenem-cilastatina (Recarbrio) para o tratamento de infecções bacterianas graves por gram-negativos resistentes.
O modelo TxGNN prevê que pode ser eficaz para a **Síndrome de Hiperviscosidade Policlonal (Polyclonal Hyperviscosity Syndrome)**, com pontuação de 99,22% — no entanto, atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção, e a análise mecanística indica **ausência de base biológica plausível**.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Informação não disponível nos dados regulatórios cadastrados |
| Nova Indicação Prevista | Síndrome de Hiperviscosidade Policlonal (Polyclonal Hyperviscosity Syndrome) |
| Pontuação de Previsão TxGNN | 99,22% |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 1 |
| Decisão Recomendada | **Hold** |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação disponíveis neste Evidence Pack. Segundo informações farmacológicas conhecidas, Relebactam é um inibidor de β-lactamase do Grupo 2 (Classe A/C), desenvolvido para ser co-administrado com imipenem-cilastatina. Seu mecanismo consiste em se ligar irreversivelmente a β-lactamases bacterianas — especialmente KPC (*Klebsiella pneumoniae* carbapenemase) e outras enzimas do tipo AmpC — impedindo que bactérias resistentes inativem o antibiótico carbapenêmico. Relebactam não possui ação conhecida sobre células humanas, proteínas plasmáticas ou qualquer via imunológica.

A **Síndrome de Hiperviscosidade Policlonal** é uma condição em que a produção excessiva de imunoglobulinas policlonais eleva a viscosidade sérica, causando sintomas neurológicos, visuais e hemorrágicos. Sua gestão é direcionada ao tratamento da doença de base (tipicamente inflamatória ou autoimune) e, em casos agudos, à plasmaférese para remoção das proteínas em excesso. A fisiopatologia é inteiramente centrada em mecanismos imunológicos e de coagulação humanos.

Não existe ligação mecanística identificada entre a inibição de β-lactamases bacterianas e a modulação da síntese, degradação ou viscosidade das imunoglobulinas humanas. A alta pontuação TxGNN (99,22%) reflete correlações estruturais no grafo de conhecimento — possivelmente por associações indiretas entre infecção, inflamação e hiperviscosidade — mas **não representa uma oportunidade biológica válida de reposicionamento neste momento**. A previsão do modelo deve ser interpretada como sinal exploratório, não como indicação clínica.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados para Relebactam e Síndrome de Hiperviscosidade Policlonal.

---

## Evidências da Literatura

Atualmente não há literatura relacionada para Relebactam e Síndrome de Hiperviscosidade Policlonal.

---

## Informações de Comercialização no Brasil

O registro ANVISA consta como ativo (`total_licenses: 1`), porém os detalhes do cadastro (número de registro, nome comercial, forma farmacêutica e indicação aprovada) não foram populados nesta versão do Evidence Pack. Os dados regulatórios completos devem ser obtidos diretamente no portal ANVISA para esta entrada.

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|--------------------|----------------|--------------------|--------------------|
| Pendente de preenchimento | Pendente | Pendente | Pendente |

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Apesar da pontuação TxGNN elevada (99,22%), não existe base biológica plausível que conecte a inibição de β-lactamases bacterianas ao tratamento da Síndrome de Hiperviscosidade Policlonal — condição de natureza imunológica e hematológica. Não há nenhum ensaio clínico ou publicação científica apoiando esta hipótese, configurando nível de evidência L5 (apenas previsão de modelo). O mesmo padrão se repete em todas as 10 indicações previstas para este fármaco neste relatório, sugerindo que o modelo TxGNN pode estar capturando associações espúrias via nós intermediários no grafo de conhecimento (ex.: infecção → inflamação → alterações hematológicas).

**Para prosseguir, é necessário:**
- Preencher os dados regulatórios ANVISA (número de registro, nome comercial, indicação aprovada, forma farmacêutica)
- Obter e analisar o mecanismo de ação formal via DrugBank API (DG002)
- Obter advertências e contraindicações do produto via bula PDF da ANVISA (DG001)
- Investigar se alguma das 10 indicações previstas possui ao menos uma hipótese mecanística indireta (ex.: septicemic plague — única com mínima plausibilidade biológica anotada no Evidence Pack) antes de descartar completamente o conjunto de previsões
- Considerar revisão dos parâmetros de treinamento do TxGNN para fármacos da classe β-lactamase inhibitor, dado o padrão sistemático de previsões sem suporte mecanístico
---

