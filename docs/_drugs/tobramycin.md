---
layout: default
title: Tobramycin
parent: 僅模型預測 (L5)
nav_order: 486
evidence_level: L5
indication_count: 10
---

# Tobramycin
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

Using the `txgnn-pipeline` skill to guide report generation. Now producing the full Markdown report based on the Evidence Pack.

---

# Tobramycin: De infecções bacterianas por Gram-negativos à ceratite de exposição

## Resumo em Uma Frase

Tobramycin é um antibiótico aminoglicosídeo com ampla história de uso no tratamento de infecções graves por bactérias Gram-negativas, especialmente *Pseudomonas aeruginosa* em contextos clínicos como fibrose cística e infecções oculares bacterianas.
O modelo TxGNN prevê que pode ser eficaz para **Ceratite de Exposição (Exposure Keratitis)**,
atualmente com **2 ensaios clínicos** (ambos de baixa relevância direta) e **7 publicações** apoiando essa direção — a maioria constituída por relatos de caso e estudos in vitro.

---

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Infecções bacterianas graves por bacilos Gram-negativos (especialmente *P. aeruginosa*) |
| Nova Indicação Prevista | Ceratite de Exposição (Exposure Keratitis) |
| Pontuação de Previsão TxGNN | 99,93% |
| Nível de Evidência | L4 |
| Situação no Mercado Brasileiro | ✗ Não comercializado |
| Número de Registros | 0 |
| Decisão Recomendada | Hold |

---

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação no Evidence Pack. Segundo informações conhecidas, tobramycin é um antibiótico aminoglicosídeo que atua ligando-se irreversivelmente à subunidade 30S do ribossomo bacteriano, inibindo a síntese proteica e exercendo atividade bactericida de amplo espectro contra bacilos Gram-negativos — com especial eficácia contra *Pseudomonas aeruginosa* e *Staphylococcus aureus*.

A ceratite de exposição ocorre quando o fechamento incompleto das pálpebras expõe a superfície corneana à dessecação crônica, elevando significativamente o risco de infecção bacteriana secundária. Os principais agentes infecciosos nesse contexto — *P. aeruginosa* e *S. aureus* — são justamente os patógenos-alvo para os quais tobramycin demonstra maior atividade antibacteriana. Formulações oftálmicas de tobramycin já são amplamente utilizadas na prática clínica para ceratite bacteriana e conjuntivite bacteriana, o que fundamenta mecanisticamente a extensão de seu uso a infecções secundárias na ceratite de exposição.

No entanto, há uma limitação crítica de segurança que não pode ser ignorada: o estudo in vitro de Lass et al. (PMID 2707046, 1989) demonstrou que tobramycin, assim como outros aminoglicosídeos, apresenta potencial toxicidade sobre células epiteliais corneanas. Em córneas já comprometidas pela exposição crônica, essa toxicidade epitelial adicional pode agravar o dano tecidual preexistente. Qualquer avanço nessa indicação deve, portanto, partir de uma cuidadosa avaliação da relação risco-benefício em modelos de córnea comprometida.

---

## Evidências de Ensaios Clínicos

| Número do Ensaio | Fase | Status | Participantes | Principais Achados |
|---------|------|------|------|---------|
| [NCT05313828](https://clinicaltrials.gov/study/NCT05313828) | N/A | Desconhecido | 40 | Comparação de modalidades de tratamento para úlcera corneana dendriforme por herpes simplex (HSK); tobramycin não é a intervenção principal; objeto do estudo é ceratite viral, não de exposição |
| [NCT06200727](https://clinicaltrials.gov/study/NCT06200727) | N/A | Desconhecido | 170 | Uso de membrana de PRF (fibrina rica em plaquetas) em quatro condições oftálmicas (buraco macular, pterígio, úlcera corneana e glaucoma); tobramycin não é intervenção específica do estudo |

> ⚠️ Ambos os ensaios possuem relevância baixa para a indicação prevista (grau C). Atualmente não há ensaios clínicos registrados avaliando especificamente tobramycin em ceratite de exposição.

---

## Evidências da Literatura

| PMID | Ano | Tipo | Periódico | Principais Achados |
|------|-----|------|------|---------|
| [2707046](https://pubmed.ncbi.nlm.nih.gov/2707046/) | 1989 | Estudo In Vitro | Current Eye Research | Avaliação da citotoxicidade de quatro aminoglicosídeos (neomicina, gentamicina, **tobramycin**, amicacina) em cultura primária de células epiteliais corneanas de coelho; demonstrou toxicidade epitelial dose e tempo-dependente — relevante para segurança em córneas já comprometidas |
| [34987857](https://pubmed.ncbi.nlm.nih.gov/34987857/) | 2021 | Relato de Caso | Oxford Medical Case Reports | Ceratite bacteriana por *Shewanella algae* multirresistente em paciente acamado em estado vegetativo incapaz de fechar os olhos (contexto de ceratite de exposição); perfil de sensibilidade incluiu tobramycin |
| [17228760](https://pubmed.ncbi.nlm.nih.gov/17228760/) | 2006 | Estudo In Vitro (MIC/PAE) | Nippon Ganka Gakkai Zasshi | Determinação de CIM e efeito pós-antibiótico de colírios antibióticos, incluindo tobramycin, frente a isolados de ceratite infecciosa no Japão; apoio à eficácia microbiológica |
| [12861116](https://pubmed.ncbi.nlm.nih.gov/12861116/) | 2003 | Relato de Caso | Eye & Contact Lens | Ceratite bilateral por MRSA após ceratectomia fotorrefrativa; discussão de cobertura antibacteriana incluindo tobramycin no manejo de ceratite bacteriana pós-cirúrgica |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Relato de Caso | Ophthalmology | Primeiro relato de ceratite associada a lentes de contato por *Bacillus cereus*; contextualiza o espectro de agentes causadores de ceratite bacteriana tratável com aminoglicosídeos |
| [14574976](https://pubmed.ncbi.nlm.nih.gov/14574976/) | 2003 | Relato de Caso | Eye Science | Dellen corneana paracentral como sinal raro de oftalmopatia de Graves — conexão indireta com ceratite de exposição via exoftalmia (fechamento palpebral incompleto por proptose) |
| [33847093](https://pubmed.ncbi.nlm.nih.gov/33847093/) | 2021 | Série de Casos (Animal) | Polish Journal of Veterinary Sciences | Toxoplasmose ocular felina tratada com protocolo incluindo tobramycin; relevância periférica ao modelo de doença |

---

## Considerações de Segurança

Consulte a bula para informações de segurança completas.

> **Alerta de segurança específico para esta indicação:** O estudo PMID 2707046 (Lass et al., 1989) documentou citotoxicidade de tobramycin sobre o epitélio corneano in vitro de forma dose e tempo-dependente. Em pacientes com ceratite de exposição — nos quais o epitélio corneano já se encontra cronicamente comprometido pela dessecação — a aplicação de tobramycin tópico pode potencialmente agravar o dano epitelial. Essa limitação deve ser considerada central em qualquer desenho de estudo futuro para esta indicação.

---

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
As evidências disponíveis para tobramycin em ceratite de exposição são predominantemente pré-clínicas e indiretas (nível L4), sem nenhum ensaio clínico dedicado e sem publicações de alta qualidade (RCT ou revisão sistemática) diretamente endereçando esta indicação. Adicionalmente, a preocupação com toxicidade epitelial corneana documentada in vitro (PMID 2707046) representa um sinal de segurança que deve ser esclarecido antes de qualquer avanço clínico. Somado ao fato de tobramycin não estar registrado no Brasil, o contexto atual não suporta progressão para uso clínico nesta indicação sem investigação adicional robusta.

**Para prosseguir, é necessário:**
- Realização de estudos em modelos de córnea comprometida (ex vivo ou animal) para determinar concentrações tópicas seguras de tobramycin em epitélio danificado
- Registro de ensaio clínico Phase 2 avaliando tobramycin oftálmico como profilaxia de infecção secundária em ceratite de exposição confirmada
- Obtenção de dados completos de MOA via DrugBank API (ID: DB00684)
- Avaliação de viabilidade regulatória junto à ANVISA para registro no Brasil
- Revisão sistemática de aminoglicosídeos tópicos em doenças da superfície ocular para contextualizar o perfil de segurança comparativo
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

