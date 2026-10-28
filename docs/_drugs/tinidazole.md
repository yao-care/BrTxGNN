---
layout: default
title: Tinidazole
parent: Apenas Predição do Modelo (L5)
nav_order: 639
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "Tinidazole"
predicted_indications: ["postmenopausal atrophic vaginitis", "ulceration of vulva", "vulvar neoplasm", "breast fibrocystic disease", "AIDS", "apocrine adenosis of breast", "blunt duct adenosis of breast", "congenital human immunodeficiency virus", "AIDS related complex", "benign mammary dysplasia"]
description: "Tinidazole: nova indicação prevista, Vaginite atrófica pós-menopausa (postmenopausal atrophic vaginitis) (nível de evidência L5). Indicação original: AMEBICIDAS, GIARDICIDAS E TRICOMONICIDAS"
---

# Tinidazole
{: .fs-9 }

Nível de evidência: **L5** | Indicações previstas: **10** 
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

## Tinidazole: Vaginite atrófica pós-menopausa (postmenopausal atrophic vaginitis)
{: .text-alpha }

## Resumo em Uma Frase

Tinidazol é um nitroimidazólico originalmente registrado no Brasil para amebíases, giardíases e tricomoníase, além de associações tópicas ginecológicas antiinfecciosas e antimicóticas.
O modelo TxGNN prevê que pode ser eficaz para **vaginite atrófica pós-menopausa (postmenopausal atrophic vaginitis)**,
mas atualmente há **0 ensaios clínicos** e **0 publicações** apoiando esta direção específica: trata-se de uma previsão puramente baseada no modelo.

## Visão Geral Rápida

| Item | Conteúdo |
|------|------|
| Indicação Original | AMEBICIDAS, GIARDICIDAS E TRICOMONICIDAS; ANTINFECCIOSOS TOPICOS-ASSOCIACOES MEDICAMENTOSAS; PRODS GINECOLOGICOS ANTINFECC TOPICOS ASSOC MEDICAMENTOSAS; PRODUTOS GINECOLOGICOS ANTIINFECCIOSOS TOPICOS ASSOCIACAO MEDICAMENTOSA; ANTIMICOTICO; ANTIMICOTICOS PARA USO TOPICO |
| Nova Indicação Prevista | Vaginite atrófica pós-menopausa (postmenopausal atrophic vaginitis) |
| Pontuação de Previsão TxGNN | 0.9993 |
| Nível de Evidência | L5 |
| Situação no Mercado Brasileiro | Comercializado (registros ativos: pelo menos 20) |
| Número de Registros | 20 (todos cancelados) |
| Decisão Recomendada | Hold |

## Por que Esta Previsão é Razoável?

Atualmente, não há dados detalhados sobre o mecanismo de ação. Segundo informações conhecidas, o tinidazol é um antimicrobiano da classe dos 5-nitroimidazólicos, com atividade contra protozoários e bactérias anaeróbias. Sua eficácia em tricomoníase, giardíase e amebíase está estabelecida, e ele foi comercializado no Brasil em associações vaginais tópicas (por exemplo, com nitrato de miconazol e tioconazol).

A previsão do modelo provavelmente decorre da proximidade na rede de conhecimento entre o tinidazol e produtos ginecológicos antiinfecciosos tópicos. A vaginite atrófica, porém, é causada principalmente pela deficiência de estrogênio, e não por infecção. Por isso, a plausibilidade biológica de um mecanismo antimicrobiano é fraca.

Em resumo, o escore alto (0,9993) deve ser interpretado com cautela: vem do modelo TxGNN (deep learning) e pode refletir semelhanças aprendidas pelo modelo entre doenças relacionadas, não evidência biológica ou clínica.

## Informações de Comercialização no Brasil

Há 20 registros válidos. Principais exemplos:

| Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada |
|---------|------|------|-----------|
| Registro 105830520 | Tinidazol | — | Amebicidas, giardicidas e tricomonicidas |
| Registro 188710005 | Amplogin | — | Antiinfecciosos tópicos – associações medicamentosas |
| Registro 154230115 | Tinidazol + nitrato de miconazol | — | Produtos ginecológicos antiinfecciosos tópicos, associações medicamentosas |
| Registro 178170806 | Amplium G | — | Produtos ginecológicos antiinfecciosos tópicos, associações medicamentosas |
| Registro 102980426 | Tindamas | — | Antimicótico |

## Considerações de Segurança

- **Contraindicações segundo o grafo de conhecimento (não extraídas da bula)**: epilepsia, neutropenia, agranulocitose, doença do sistema nervoso periférico e neuropatia periférica.
- **Interações medicamentosas**: foram identificadas 100 interações, e as 20 listadas são todas de nível moderado. Entre as principais estão etanol, paclitaxel, cabazitaxel, capecitabina, bortezomibe, amiodarona, atorvastatina, etinilestradiol, estradiol, levodopa, barbitúricos (amobarbital, butalbital), apalutamida, adalimumabe e trastuzumabe entansina.

Consulte a bula para as advertências e contraindicações formais, pois essas informações não estavam disponíveis nos dados compilados.

## Conclusão e Próximos Passos

**Decisão: Hold**

**Justificativa:**
A previsão para vaginite atrófica pós-menopausa não tem nenhum ensaio clínico ou publicação de apoio (L5), e o mecanismo antimicrobiano é biologicamente pouco plausível para uma condição causada por deficiência estrogênica.

**Para prosseguir, é necessário:**
- Dados do mecanismo de ação do tinidazol.
- Bula da ANVISA com advertências e contraindicações, para a triagem de segurança.
- Justificativa biológica para uso em vaginite atrófica (por exemplo, papel de infecção secundária) e estudos pré-clínicos ou exploratórios.
- Avaliação de compatibilidade de via de administração e forma farmacêutica, hoje pendente.
- Esclarecimento do status regulatório, já que não há registro válido no Brasil.

### Observação sobre as demais previsões

Nenhuma das outras previsões de maior pontuação tem respaldo suficiente (todas recomendadas como Hold):

- **Úlcera de vulva (0.9987)**, **neoplasia vulvar (0.9986)** e **doenças benignas da mama** (doença fibrocística, adenose de ducto obtuso, adenose apócrina, displasia mamária benigna; 99,2% a 0.9975): L5, sem evidências e sem mecanismo plausível. Para a úlcera vulvar, existe apenas um relato de caso em que a úlcera era causada por *Trichomonas vaginalis* e se resolveu com tinidazol oral, o que corresponde ao uso já aprovado.
- **AIDS (0.9969)**: nível L4. A literatura recuperada trata de coinfecções parasitárias (amebíase, giardíase, tricomoníase), e não da infecção pelo HIV. O único ensaio (NCT03412071, fase NA, situação desconhecida, 125 participantes) é um estudo piloto de intervenção focada no microbioma para reduzir a suscetibilidade ao HIV em homens ugandenses. O papel do tinidazol nele não está claro e não há resultados de eficácia.
- **Complexo relacionado à AIDS e HIV congênito (0,9939)**: L5, sem mecanismo anti-HIV; o escore vem do modelo TxGNN (deep learning) e pode refletir semelhanças aprendidas entre doenças relacionadas, não evidência biológica.
## Aviso de isenção de responsabilidade

Este conteúdo é apenas para fins de pesquisa e não constitui aconselhamento médico.
É necessária validação clínica antes de qualquer aplicação clínica.

---

