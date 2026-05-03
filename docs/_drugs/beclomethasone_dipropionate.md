---
layout: default
title: Beclomethasone Dipropionate
parent: 僅模型預測 (L5)
nav_order: 99
evidence_level: L5
indication_count: 1
---

# Beclomethasone Dipropionate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Beclometasona Dipropionato: Da asma e rinite alérgica ao eczema atópico

## Resumo em Uma Frase

Beclometasona Dipropionato (BDP) é um glicocorticoide sintético amplamente utilizado no tratamento de asma brônquica e rinite alérgica, principalmente por via inalatória e intranasal. O modelo TxGNN prevê que pode ser eficaz para **Eczema Atópico (Atopic Eczema)**, contando atualmente com **0 ensaios clínicos registrados** e **18 publicações** apoiando esta direção — incluindo um ensaio clínico randomizado controlado com resultado positivo.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Asma brônquica e rinite alérgica (uso inalatório/intranasal) |
| Nova Indicação Prevista | Eczema Atópico (Atopic Eczema) |
| Pontuação de Previsão TxGNN | 99,41% |
| Nível de Evidência | L2 |
| Situação no Mercado Brasileiro | Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Proceed with Guardrails |

---

## Por que Esta Previsão é Razoável?

O BDP é um glicocorticoide sintético de alta potência. Seu mecanismo de ação central consiste na ligação ao receptor intracelular de glicocorticoides (GR-α), que suprime o fator de transcrição NF-κB e reduz a expressão de citocinas pró-inflamatórias do eixo Th2 — incluindo IL-4, IL-13, IL-31 e TSLP. Em paralelo, inibe a degranulação de mastócitos e a infiltração tecidual de eosinófilos. Esses efeitos correspondem diretamente aos alvos patológicos do eczema atópico, que é uma doença inflamatória crônica da pele mediada exatamente pelo mesmo eixo Th2.

O eczema atópico e as indicações originais do BDP (asma, rinite alérgica) pertencem ao mesmo espectro de doenças atópicas IgE-mediadas, compartilhando inflamação Th2, ativação de mastócitos e infiltração eosinofílica como denominadores comuns. Não por acaso, os corticosteroides tópicos já são reconhecidos como tratamento de primeira linha para o eczema como classe farmacológica — e a previsão do TxGNN identifica o BDP especificamente dentro dessa classe, com excelente plausibilidade biológica.

A literatura publicada reforça esse raciocínio de forma concreta: um RCT duplo-cego controlado por placebo de 1984 (PMID 6434024) demonstrou melhora significativa com BDP oral e nasal em crianças com eczema atópico grave; estudos clínicos subsequentes utilizaram BDP oral e tópico em dermatite atópica refratária na infância; e estudos comparativos em modelos animais posicionam o BDP como referência de eficácia anti-inflamatória local nessa indicação.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [6434024](https://pubmed.ncbi.nlm.nih.gov/6434024/) | 1984 | RCT | British Medical Journal | RCT duplo-cego cruzado em 26 crianças com eczema atópico grave: BDP oral + nasal por 4 semanas produziu melhora significativa vs. placebo; cortisol urinário levemente reduzido |
| [1476023](https://pubmed.ncbi.nlm.nih.gov/1476023/) | 1992 | Série de Casos Clínicos | Acta Derm Venereol Suppl | BDP oral controlou dermatite atópica grave em 10/14 crianças (dose média 1.000 µg/dia); monitoramento de crescimento linear e função adrenal durante o tratamento |
| [30911861](https://pubmed.ncbi.nlm.nih.gov/30911861/) | 2019 | Estudo de Formulação | AAPS PharmSciTech | Desenvolvimento de micelas mistas de BDP para entrega dérmica em modelo animal de dermatite subcrônica; demonstra viabilidade de formulação tópica otimizada |
| [14522624](https://pubmed.ncbi.nlm.nih.gov/14522624/) | 2003 | Estudo Clínico Intervencionista | J Dermatol Treat | Terapia de curativo úmido oclusivo com corticoide em 8 crianças com eczema atópico; avaliação de efeitos no crescimento e turnover ósseo ao longo de 2 semanas |
| [19874229](https://pubmed.ncbi.nlm.nih.gov/19874229/) | 2009 | Estudo Experimental | Immunopharmacol Immunotoxicol | Comparação entre mometasona e BDP em modelo murino de dermatite atópica; MF apresentou maior potência anti-inflamatória local com menores efeitos sistêmicos que BDP |
| [9463794](https://pubmed.ncbi.nlm.nih.gov/9463794/) | 1998 | Revisão | Drugs | Revisão de mometasona (análogo sintético do BDP); BDP utilizado como comparador ativo em ensaios de dermatite atópica, consolidando a classe na indicação |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Revisão | Neuroimmunomodulation | Corticosteroides intranasais (incluindo BDP) podem causar supressão do eixo HPA em pacientes com rinite + asma + dermatite atópica em tratamento combinado |
| [11488426](https://pubmed.ncbi.nlm.nih.gov/11488426/) | 2001 | Revisão | Jpn J Pharmacol | Revisão abrangente sobre fármacos para doenças alérgicas; BDP citado como referência entre os glicocorticoides para asma e doenças atópicas relacionadas |
| [14616123](https://pubmed.ncbi.nlm.nih.gov/14616123/) | 2003 | Revisão | Allergy | Investigação de alergia a corticosteroides em pacientes asmáticos; BDP identificado como potencial alérgeno de contato em formulações tópicas — relevante para monitoramento de segurança |
| [37023229](https://pubmed.ncbi.nlm.nih.gov/37023229/) | 2023 | Computacional / Grafo de Conhecimento | J Chem Inf Model | Estudo de reposicionamento por grafos de conhecimento (DrugRep-KG); valida metodologicamente abordagens de KG para identificação de novas indicações, como a realizada pelo TxGNN |

---

## Informações de Comercialização no Brasil

Não foram encontrados registros de Beclometasona Dipropionato na base regulatória consultada (0 registros ativos).

---

## Considerações de Segurança

Consulte a bula para informações de segurança.

---

## Conclusão e Próximos Passos

**Decisão: Proceed with Guardrails**

**Justificativa:**
Existe um RCT publicado com resultado positivo e múltiplos estudos clínicos que demonstram eficácia do BDP em eczema atópico, com mecanismo de ação diretamente alinhado à fisiopatologia da doença. A pontuação TxGNN de 99,41% é consistente com esse suporte de literatura. Contudo, a ausência de ensaios clínicos registrados contemporâneos, a falta de registro regulatório no Brasil e a ausência de dados formais de segurança da bula impõem a necessidade de salvaguardas antes de qualquer avanço.

**Para prosseguir, é necessário:**
- Confirmar situação regulatória na ANVISA — verificar se há registros ativos não capturados na base consultada (ex.: Clenil, Becotide, Qvar)
- Obter dados completos de segurança da bula (advertências, contraindicações, interações), preferencialmente via ANVISA ou FDA
- Definir a via de administração e formulação adequadas para eczema atópico (tópica, oral ou combinada) com as respectivas faixas de dose
- Protocolo de monitoramento do eixo hipotálamo-hipófise-adrenal (HPA), especialmente em uso pediátrico ou prolongado
- Consideração de novos ensaios clínicos prospectivos com formulações tópicas modernas de BDP para validação da indicação em populações brasileiras
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

