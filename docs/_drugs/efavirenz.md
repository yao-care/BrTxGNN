---
layout: default
title: Efavirenz
parent: 僅模型預測 (L5)
nav_order: 233
evidence_level: L5
indication_count: 3
---

# Efavirenz
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Efavirenz: Do HIV-1 humano à Síndrome de Imunodeficiência Adquirida Felina

## Resumo em Uma Frase

Efavirenz é um inibidor não nucleosídeo da transcriptase reversa (NNRTI), originalmente utilizado no tratamento da infecção pelo HIV-1 em combinação com outros antirretrovirais.
O modelo TxGNN prevê que pode ser eficaz para a **Síndrome de Imunodeficiência Adquirida Felina (Feline Acquired Immunodeficiency Syndrome / FIV)**, atualmente com **0 ensaios clínicos relevantes** e **1 publicação** apoiando diretamente esta direção.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecção pelo HIV-1 (antirretroviral da classe NNRTI) |
| Nova Indicação Prevista | Síndrome de Imunodeficiência Adquirida Felina (feline acquired immunodeficiency syndrome) |
| Pontuação de Previsão TxGNN | 99.80% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✓ Comercializado |
| Número de Registros | 8 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Efavirenz atua bloqueando alostericamente a transcriptase reversa (TR) do HIV-1, ligando-se ao sítio NNIBP (Non-Nucleoside Inhibitor Binding Pocket) e inibindo a replicação viral. O FIV (Feline Immunodeficiency Virus) é também um lentivírus e, como o HIV-1, depende de uma TR para replicação — o que justifica a hipótese de classe que o TxGNN explorou.

No entanto, existe uma diferença estrutural crítica que não pode ser ignorada: os resíduos-chave do NNIBP no HIV-1 (como Y181, Y188 e K103) apresentam variações significativas na TR do FIV. Essa divergência nos aminoácidos de ancoragem do sítio de ligação é conhecida por reduzir — ou mesmo abolir — a afinidade de NNRTIs de primeira e segunda geração pela TR de outros lentivírus não humanos. O único estudo da literatura identificado (PMID 38031646, 2023) foi concebido precisamente para comparar bioquímica e estruturalmente o comportamento de Efavirenz, Nevirapina e Rilpivirina contra TR de FIV e HIV-1. Seus resultados provavelmente revelam **atividade inferior** do Efavirenz contra a TR do FIV — um sinal mecanístico negativo que deve orientar qualquer decisão de avanço.

Em síntese: a previsão do modelo é biologicamente plausível em termos de parentesco viral, mas as evidências estruturais disponíveis levantam dúvida substancial sobre eficácia real do Efavirenz nesta indicação. A indicação ranking 2 (infecção por SIV em modelo RT-SHIV) possui suporte empírico muito mais sólido, porém refere-se a um modelo animal baseado em TR quimérica de HIV-1 — não ao vírus felino.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relevantes registrados para Efavirenz em Síndrome de Imunodeficiência Adquirida Felina.

> **Nota de qualidade dos dados:** Dois registros foram recuperados pelo coletor (NCT00951015 e NCT01263015), porém ambos investigam **Dolutegravir** (inibidor de integrase) em **HIV-1 humano** — sem qualquer relação com Efavirenz ou FIV. Ambos foram classificados como grau C (erros de associação do coletor) e excluídos da análise de evidências.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | Bioquímica / Biologia Estrutural (in vitro + computacional) | Journal of Veterinary Science | Comparação bioquímica e estrutural de NNRTIs de 1ª e 2ª geração (Nevirapina, Efavirenz e Rilpivirina) contra TR do FIV e do HIV; investiga o potencial terapêutico para tratamento de gatos infectados por FIV |

---

## Informações de Comercialização no Brasil

Efavirenz possui **8 registros** ativos no Brasil com situação **comercializado**. Os dados detalhados dos registros individuais (número de registro, nome comercial, forma farmacêutica e indicação aprovada) não estão disponíveis neste Evidence Pack e deverão ser consultados diretamente no portal da ANVISA.

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão do TxGNN baseia-se em plausibilidade de classe viral (lentivírus compartilham TR), mas a evidência disponível é de nível L4 (apenas 1 estudo pré-clínico estrutural), não há ensaios clínicos relevantes, e o único trabalho identificado sugere que diferenças nos resíduos do NNIBP da TR do FIV podem comprometer a atividade do Efavirenz — configurando um **sinal mecanístico negativo**, não positivo.

**Para prosseguir, é necessário:**
- Obter e analisar os resultados completos de PMID 38031646 para confirmar se Efavirenz apresenta atividade inibidora mensurável contra a TR do FIV e qual é a magnitude da diferença
- Realizar ensaios enzimáticos in vitro (IC₅₀ de Efavirenz contra TR purificada de FIV vs. HIV-1) para quantificar a perda de afinidade
- Avaliar se NNRTIs de geração mais recente (ex.: Rilpivirina, Doravirina) com perfil estrutural distinto apresentam melhor adequação ao NNIBP do FIV
- Complementar os dados regulatórios (bula ANVISA) para MOA, advertências e contraindicações
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

