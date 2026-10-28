---
layout: default
title: Glimepiride
parent: Apenas Predição do Modelo (L5)
nav_order: 344
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Glimepiride: nova indicação prevista, Síndrome do membro rígido focal (focal stiff limb syndrome) (nível de evidência L5). Indicação original: Antidiabéticos"
monitor_inn: "GLIMEPIRIDE"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Glimepiride
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

## Glimepirida: De antidiabético a síndrome do membro rígido focal
{: .text-alpha }

## Resumo em Uma Frase

Glimepirida é um antidiabético da classe das sulfonilureias, registrado no Brasil na categoria "antidiabéticos".
O modelo TxGNN prevê que pode ser eficaz para **síndrome do membro rígido focal (focal stiff limb syndrome)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção; trata-se de uma previsão puramente computacional.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | Antidiabéticos |
| Nova Indicação Prevista | Síndrome do membro rígido focal (focal stiff limb syndrome) |
| Pontuação de Previsão TxGNN | 0,9975 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: 13 de 13) |
| Número de Registros | 13 (ativos: 13) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório. Segundo informações conhecidas, a glimepirida é uma sulfonilureia que bloqueia os canais de potássio sensíveis ao ATP (K-ATP) das células beta pancreáticas, estimulando a secreção de insulina. Sua eficácia no diabetes é estabelecida.

A relação com a nova indicação é fraca. A síndrome do membro rígido focal pertence ao espectro da síndrome da pessoa rígida, que envolve autoimunidade (frequentemente anti-GAD65) e comprometimento da inibição GABAérgica. O bloqueio de canais K-ATP não atua sobre esse processo. A pontuação do modelo TxGNN (deep learning) pode refletir similaridades aprendidas entre doenças relacionadas, não evidência biológica, e provavelmente decorre da associação com o diabetes autoimune com anticorpos anti-GAD, um fator de confusão e não uma justificativa terapêutica.

**Não há vínculo mecanístico claro.** A pontuação alta (0,9975) vem do modelo TxGNN (deep learning) e pode refletir similaridades aprendidas entre doenças relacionadas, não evidência biológica.

Outras previsões do modelo seguem a mesma lógica (síndrome da pessoa rígida clássica, opsismodisplasia, síndrome de disfunção responsiva à tiamina, lipodistrofias localizadas e agenesia pancreática). Em geral, refletem a proximidade com o diabetes ou a resistência à insulina, e nenhuma delas tem evidência clínica. Na agenesia pancreática, a glimepirida deveria ser ineficaz, pois depende de tecido pancreático funcional.

## Informações de Comercialização no Brasil

Dos 13 registros encontrados, 13 estão válidos. Os 5 principais:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro nº 155370007 | Glimepirida | Não informada | Antidiabéticos |
| Registro nº 154230236 | Glimepirida | Não informada | Antidiabéticos |
| Registro nº 100431143 | Glimepirida | Não informada | Antidiabéticos |
| Registro nº 103900130 | Glimepil | Não informada | Antidiabéticos |
| Registro nº 102351379 | Glimepirida + cloridrato de metformina | Não informada | Antidiabéticos |

## Considerações de Segurança

- **Contraindicações (grafo de conhecimento, não texto de bula)**: o grafo de conhecimento associa o fármaco a contraindicações em doença renal, doença hepática, doença da vesícula biliar, insuficiência cardíaca congestiva, hipopituitarismo e deficiências hormonais hipofisárias (incluindo deficiência de hormônio do crescimento, síndrome de Sheehan e hipogonadismo hipogonadotrófico/síndrome de Kallmann), doença do timo, osteoporose (incluindo pós-menopausa) e doenças infecciosas.
- **Interações Medicamentosas**: foram identificadas 100 interações; entre as listadas, a maioria é de gravidade moderada. Exemplos:
  - Anti-histamínicos H2: famotidina, ranitidina
  - Beta-agonistas e simpaticomiméticos: formoterol, salbutamol, epinefrina, fenilefrina, pseudoefedrina
  - Outros: acebutolol, acetazolamida, acitretina, cetorolaco, ibuprofeno, etinilestradiol, hidrocortisona, albiglutida, nitazoxanida, hidroclorotiazida, etanol
  - Interações menores: hidrocortisona tópica, alclometasona tópica
- Para advertências e contraindicações da bula, consulte a bula, pois não estavam disponíveis nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão vem do modelo TxGNN (deep learning) (nível L5), sem ensaios clínicos nem literatura de suporte, e sem vínculo mecanístico plausível. O medicamento está comercializado no Brasil (13 dos 13 registros são válidos).

**Para prosseguir, é necessário:**
- Evidência clínica ou pré-clínica que sustente o uso em síndrome do membro rígido focal (hoje inexistente)
- Dados detalhados do mecanismo de ação e análise da relação com a autoimunidade anti-GAD
- Advertências e contraindicações da bula na ANVISA, necessárias para a triagem de segurança
- Esclarecimento da situação regulatória (registros cancelados) e da compatibilidade de vias de administração
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

