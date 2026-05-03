---
layout: default
title: Potassium Acetate
parent: 僅模型預測 (L5)
nav_order: 404
evidence_level: L5
indication_count: 1
---

# Potassium Acetate
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

Usando `txgnn-pipeline` para contextualizar o projeto, e aplicando o template de relatório definido no prompt do sistema. Vou agora analisar o Evidence Pack e gerar o relatório completo.

---

# Acetato de Potássio: Do suplemento eletrolítico à acidose tubular renal

## Resumo em Uma Frase

O Acetato de Potássio (Potassium Acetate, DB14498) é um sal de potássio reconhecido clinicamente como suplemento eletrolítico intravenoso, sem registros ativos na ANVISA.
O modelo TxGNN prevê potencial eficácia para **Acidose Tubular Renal (Renal Tubular Acidosis)**,
com **0 ensaios clínicos** e **9 publicações** relacionadas — porém a literatura identificada descreve predominantemente contextos de risco de segurança no subtipo hiperkalêmico (Tipo IV), criando uma contradição importante com o alto escore de previsão.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|----------|
| Indicação Original | Não registrada no Brasil (uso clínico reconhecido: suplemento de potássio / componente de soluções eletrolíticas IV) |
| Nova Indicação Prevista | Acidose Tubular Renal (Renal Tubular Acidosis) |
| Pontuação de Previsão TxGNN | 99,90% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação formal disponíveis no banco de dados consultado. Com base no conhecimento clínico estabelecido, o Acetato de Potássio é composto por dois íons com papéis fisiopatológicos relevantes na acidose tubular renal (RTA): o **íon acetato (CH₃COO⁻)** e o **íon potássio (K⁺)**.

O acetato é rapidamente metabolizado pelo fígado e tecidos periféricos em **bicarbonato (HCO₃⁻)**, exercendo efeito alcalinizante sistêmico. Esse mecanismo é biologicamente plausível como terapia corretora na **RTA Tipo I (distal)** e **Tipo II (proximal)**, onde há perda de bicarbonato e acidose metabólica hiperclorêmica com ânion gap normal. O potássio suplementar, por sua vez, pode corrigir a hipocalemia frequentemente associada a esses subtipos, restaurando o gradiente eletroquímico necessário para a secreção tubular de H⁺.

Contudo, existe uma **ressalva crítica de segurança** que não pode ser ignorada: na **RTA Tipo IV (hiperkalêmica)**, a administração de potássio adicional está **formalmente contraindicada**, pois pode agravar a hipercalemia e representar risco imediato de vida. A maior parte da literatura recuperada descreve exatamente esse contexto de risco — não evidências de eficácia do acetato de potássio como terapia. Essa contradição com o escore TxGNN de 99,90% exige esclarecimento prioritário sobre qual subtipo de RTA seria o alvo terapêutico antes de qualquer avanço no desenvolvimento.

---

## Evidências de Ensaios Clínicos

Atualmente não há ensaios clínicos relacionados registrados (ClinicalTrials.gov e ICTRP consultados em 26/03/2026).

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|-----------|-------------------|
| [33771116](https://pubmed.ncbi.nlm.nih.gov/33771116/) | 2021 | RCT | BMC Nephrology | NaCl 0,9% vs. Plasma-Lyte em artroplastia de quadril: salina isotônica induziu acidose hiperclorêmica e alteração em biomarcadores de lesão tubular renal; Plasma-Lyte (contém acetato) mostrou menor impacto renal |
| [6758113](https://pubmed.ncbi.nlm.nih.gov/6758113/) | 1982 | Review | Schweiz. Med. Wochenschr. | Revisão do hipoaldosteronismo hiporeninêmico e diagnóstico diferencial de hipercalemia; discute mecanismos de acidose e deficiência na secreção tubular de K⁺ e H⁺ |
| [637641](https://pubmed.ncbi.nlm.nih.gov/637641/) | 1978 | Cohort / Case Series | Arch. Internal Medicine | Série familiar com hipercalemia persistente, hipertensão e acidose metabólica hiperclorêmica com função renal normal; sugere defeito tubular primário no manejo do potássio |
| [3398981](https://pubmed.ncbi.nlm.nih.gov/3398981/) | 1988 | Cohort / Fisiológico | Nephron | Hipercalemia e acidose por hipoaldosteronismo; fludrocortisona corrigiu ambas ao aumentar excreção urinária de K⁺ e ácido net, apontando o déficit mineralocorticoide como mecanismo central |
| [37224266](https://pubmed.ncbi.nlm.nih.gov/37224266/) | 2023 | Case Report | Veterinary Medicine and Science | RTA distal transitória com diabetes insípido nefrogênico após anestesia geral em cão; hipocalemia e acidose metabólica hiperclorêmica com ânion gap normal |
| [4015282](https://pubmed.ncbi.nlm.nih.gov/4015282/) | 1985 | Case Report | Arch. Internal Medicine | RTA distal hiperkalêmica combinada com deficiência seletiva de aldosterona em nefropatia por chumbo; fludrocortisona não corrigiu a acidose nem restaurou a excreção de K⁺ |
| [2973296](https://pubmed.ncbi.nlm.nih.gov/2973296/) | 1988 | Case Report | Arch. Mal. Cœur Vaisseaux | Hipertensão com hipercalemia e acidose tubular proximal com função renal normal; suspeita de Síndrome de Gordon / pseudo-hipoaldosteronismo tipo II |
| [34442051](https://pubmed.ncbi.nlm.nih.gov/34442051/) | 2021 | Case Report | Journal of Clinical Medicine | Hipercalcemia induzida por patiromer (resina cálcio-potássio): quadro inusitado de alcalose metabólica e hipocalemia em DRC estágio 4, ilustrando sensibilidade do equilíbrio ácido-base a trocas iônicas |
| [239022](https://pubmed.ncbi.nlm.nih.gov/239022/) | 1975 | Animal Study | J. Clinical Investigation | Expansão de volume em ratos com deficiência de KCl induzida por furosemida: correção parcial da alcalose metabólica e redução de citrato urinário e metabolismo renal de amônia |

---

## Informações de Comercialização no Brasil

O Acetato de Potássio não possui nenhum registro ativo na ANVISA. Nenhum produto com este princípio ativo foi localizado na base de dados regulatória brasileira consultada em 26/03/2026.

---

## Considerações de Segurança

Com base nos dados mecanísticos disponíveis na análise de reposicionamento, destaca-se o seguinte sinal crítico:

- **Contraindicação no subtipo hiperkalêmico (RTA Tipo IV):** A administração de potássio adicional em pacientes com RTA Tipo IV pode agravar hipercalemia com risco de arritmia e morte. A maioria das publicações identificadas descreve justamente esse contexto de risco. Este ponto deve ser esclarecido **antes de qualquer avanço** no desenvolvimento clínico.

Para informações formais de segurança (advertências em bula, contraindicações registradas, interações medicamentosas), consulte o DrugBank (DB14498), UpToDate ou fontes regulatórias como FDA/ANVISA.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
Embora o mecanismo alcalinizante do acetato e a suplementação de potássio sejam biologicamente plausíveis para RTA Tipo I e Tipo II, a literatura identificada foca predominantemente em contextos de RTA hiperkalêmica (Tipo IV) — exatamente o subtipo onde o Acetato de Potássio está **contraindicado**. Com zero ensaios clínicos, evidências apenas de nível L4 e uma contradição de segurança não resolvida, não é possível avançar para a próxima etapa de avaliação no momento.

**Para prosseguir, é necessário:**
- **Definir o subtipo-alvo de RTA** (Tipo I hipocalêmico ou Tipo II) antes de qualquer análise subsequente — este é o bloqueio crítico
- **Obter dados completos de MOA** via DrugBank API (DG002) para fundamentar a análise mecanística formal
- **Verificar a situação regulatória na ANVISA** e identificar formulações disponíveis no mercado brasileiro (ex.: uso em nutrição parenteral ou soluções IV)
- **Realizar busca ampliada de literatura** especificamente em RTA Tipo I/II com alcalinizantes à base de acetato (não restrita ao acetato de potássio como monocomponente)
- **Consultar especialista em nefrologia** para validar a plausibilidade clínica da proposta de reposicionamento antes de reavaliar o nível de evidência
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

