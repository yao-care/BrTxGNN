"""本站查核機制的在地設定（2026-11-12 建；核心流程比照 TwTxGNN、UsTxGNN，程式在同目錄與 scripts/）。

頁面上的查核框、查核紀錄表、說明文字用本站語言（葡萄牙文）；依據是 ANVISA 藥品開放資料（DADOS_ABERTOS_MEDICAMENTOS）。
改這裡的字樣後跑 python3 scripts/apply_drug_reviews.py 重套，gate（scripts/check_seo_docs.py）會檢查。
COMMITS／REGEN_COMMITS：2026-10-31～11-06 正文的許可證刪改提交與期間內 AI 重產報告的提交（scripts/reviews_from_edits.py --git 用）。
"""
import json as _json

C = _json.loads(r"""{
 "SITE": "BrTxGNN",
 "ID_PREFIX": "br",
 "SNAPSHOT": "br_licenses.json.gz",
 "HEADER_LABEL": "Nível de evidência",
 "OVERVIEW_LABELS": [
  "Nível de Evidência",
  "Nível de evidência"
 ],
 "WITHDRAWN_RE": "Retirad[oa]",
 "DESC_LEVEL_RE": "nível de evidência (L[1-5]|N/A)",
 "DESC_LEVEL_FMT": "nível de evidência {lv}",
 "NA_DESC": "apenas usos conhecidos",
 "HEADER_RULE_NOTE": "2026-11-12 實測：有 Quick Overview 等級的 518 頁，頁首全部等於第一個等級（整格取最高會有 7 頁不同）",
 "MARKET_RE": "Comercializa|[Mm]ercado",
 "ID_RE": "\\b\\d{9,13}\\b",
 "PROSE_ID_RE": null,
 "ORIGINAL_LABELS": [
  "Indicação Original",
  "Indicação original"
 ],
 "ORIGINAL_NONE_RE": "^\\s*(não consta|não disponível|nenhuma|n/a|–|-)",
 "ORIGINAL_SPLIT_RE": "[;,/()]+|\\be\\b|\\bou\\b",
 "ORIGINAL_NOTE": "2026-11-12：證據包的許可證紀錄來自 ANVISA 藥品開放資料；可比對頁數以程式輸出為準",
 "COMMITS": [
  "0fb4c25c",
  "32888d31",
  "bb4dc9a4",
  "d2611a2b",
  "f9e637d4"
 ],
 "REGEN_COMMITS": [
  "2ef4e02c",
  "6f5ad6da",
  "c6a1f929",
  "d711d02f",
  "d28ed23b",
  "1ffc8841",
  "a8d73679",
  "d0e7071d"
 ],
 "SOURCES": [
  {
   "title": "ANVISA – Dados abertos de medicamentos",
   "url": "https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv"
  }
 ],
 "PROGRAM_LINE_RE": "^A tabela mostra até \\d+ registros \\(os ativos primeiro\\)",
 "CLASSIFY": [
  [
   "tw",
   "Taiwan|TFDA|台灣|臺灣"
  ],
  [
   "combo",
   "princípio ativo único|isolad[oa]|em associação|associaç|combinaç|monofármaco"
  ],
  [
   "cancel",
   "cancelad|caducad|vencid|revogad|inativ|sem registro (?:válido|ativo|vigente)|não (?:está |há )?(?:comercializ|registrad|válid|vigente)|nenhum registro|não (?:possui|tem|há|foram encontrados) (?:nenhum )?registros?|sem registros?\\b|ausência de registro"
  ],
  [
   "count",
   "\\b\\d+\\b[^.;]{0,40}(?:registro|produto|apresenta|licen)|(?:registro|apresenta|licen)[^.;]{0,30}\\b\\d+\\b|\\b(?:todos|todas|ambos)\\b[^.;]{0,30}(?:registro|válid|vigente)|\\bvigentes?\\b|\\bválidos?\\b"
  ],
  [
   "product",
   "\\b(?:como|na forma de|forma farmac|comprimid|cápsul|injetáve|pomada|comercializ)"
  ]
 ],
 "T": {
  "label": {
   "correct": "Correção de verificação",
   "annotate": "Nota de verificação",
   "rereview": "Revisão pendente",
   "rereview_result": "Resultado da revisão"
  },
  "action": {
   "correct": "Corrigido",
   "annotate": "Nota acrescentada",
   "rereview": "Marcado para revisão",
   "section": "Seção com fontes acrescentada",
   "rereview_result": "Revisão concluída",
   "header_level": "Nível de evidência do cabeçalho recalculado a partir do resumo rápido",
   "description_level": "Nível de evidência da descrição alinhado ao cabeçalho"
  },
  "verdict": {
   "maintain": "Mantido",
   "downgrade": "Rebaixado",
   "upgrade": "Elevado",
   "withdraw": "Retirado"
  },
  "log_head": "## Registro de verificação",
  "disclaimer_re": "Aviso de isenção de responsabilidade",
  "log_cols": [
   "Data da verificação",
   "Item",
   "Ação",
   "Fonte"
  ],
  "level_same": "nível de evidência {o} inalterado",
  "level_change": "nível de evidência {o} → {n}",
  "orig": "Texto original: “{x}”",
  "table_updated": "Os itens “{labels}” desta página foram atualizados conforme o resultado da revisão; os valores originais estão no registro abaixo.",
  "decision": "Recomendação de decisão: {x}",
  "source": "Fonte",
  "rereviewed": "Marcado para revisão → revisado (ver o resultado da revisão)",
  "hdr": "Nível de evidência do cabeçalho recalculado a partir do resumo rápido ({o} → {n})",
  "hdr_withdraw": "Previsão principal retirada na revisão; nível de evidência do cabeçalho recalculado ({o} → {n})",
  "now_listed": ", agora listado em “{x}”",
  "rr": "Revisão: {v}, {c}",
  "tu": "; {l}: “{a}” → “{b}”",
  "desc": "Descrição da página: “{a}” alterado para “{b}” (acompanha o cabeçalho; restante do texto inalterado, original guardado no registro)",
  "revised": " (revisado em {d}; versão anterior guardada no registro)",
  "superseded": "Substituído pela tabela de registros gerada por programa (antes: {a})",
  "regen": "Não aparece mais após a regeneração do relatório ({d}: {n}; antes: {a})",
  "program": "Não aparece mais após uma correção do programa ({d}: {n}; antes: {a})",
  "withdrawn": "Verificação retirada ({d}: {n}; antes: {a})",
  "intro": "Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos; as previsões do modelo, os níveis de evidência e as conclusões não foram reescritos.",
  "intro_header": "Abaixo está o registro de verificação desta página; o nível de evidência do cabeçalho acompanha o resumo rápido. As previsões do modelo, a tabela resumo e as conclusões não foram reescritas.",
  "intro_rr": "Abaixo está o registro de verificação desta página: afirmações conferidas com os dados oficiais de registro (dados abertos de medicamentos da ANVISA). As correções se limitam a fatos básicos e o texto da previsão não foi reescrito; níveis de evidência e decisões só mudaram por um resultado de revisão (rebaixamento, elevação ou retirada), com os valores originais abaixo.",
  "figures": "Nos dados (dados abertos de medicamentos da ANVISA) constam {total} registros para este medicamento, {valid} válidos; os números atualizados estão no resumo rápido e nas informações de comercialização.",
  "data_as_of": "dados abertos de medicamentos da ANVISA, em {date}",
  "notes": {
   "rewrite": "Corrigido: a afirmação não correspondia aos dados de registro ({d}) e foi substituída pelo texto atual.",
   "tw": "Removido: texto residual do modelo taiwanês (TFDA), que não se aplica a esta página.",
   "combo": "Removido: a indicação de produtos de princípio ativo único ou em associação não correspondia aos dados de registro ({d}).",
   "cancel": "Removido: a afirmação de que os registros estariam cancelados, vencidos ou inválidos não correspondia aos dados de registro ({d}).",
   "count": "Removido: o número ou a situação dos registros informado não correspondia aos dados de registro ({d}).",
   "product": "Removido: a descrição dos produtos não correspondia aos dados de registro ({d}).",
   "generic": "Removido: a afirmação contradizia os dados de registro ({d})."
  },
  "notes_with_figures": [
   "cancel",
   "count",
   "product",
   "generic"
  ],
  "summary": "Removido: “{x}”",
  "regen_note": "o relatório foi regenerado em novembro de 2026 e não contém mais esta afirmação"
 }
}""")
