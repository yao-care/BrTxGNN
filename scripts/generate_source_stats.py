#!/usr/bin/env python3
"""/sources/ 頁 TxGNN、ANVISA、DrugBank 表的數字（BrTxGNN，2026-11-05）：從 data/ 算出來，寫進
docs/_data/source_stats.json，頁面用 Liquid 讀（site.data.source_stats.display.*，pt-BR 千分位），不在頁面寫死。

算法（只數檔案，不做推估）：
    txgnn_diseases           data/external/disease_vocab.csv 的列數（TxGNN 知識圖譜的疾病節點）
    txgnn_drug_disease_edges data/external/drug_disease_relations.csv 的列數（kg.csv 的藥物–疾病 indication、contraindication 邊）
    txgnn_drugbank_drugs     data/external/drugbank_vocab.csv 的列數（知識圖譜裡有 DrugBank ID 的藥物）
    anvisa_records           data/raw/br_fda_drugs.json 的筆數（scripts/process_fda_data.py 從 ANVISA
                             DADOS_ABERTOS_MEDICAMENTOS.csv 轉出，一列一筆）
    anvisa_active            同檔中 SITUACAO_REGISTRO＝Ativo 的筆數

data/ 不進 git（成果放本 repo 的 Release；還原見 scripts/restore_data.sh）。prepare_external_data.py 跑完會自動呼叫本腳本；
也可單獨跑：uv run python scripts/generate_source_stats.py [--release data-YYYYMMDD-HHMMSS]
check_seo_docs.py 第 13 項用 problems() 檢查 /sources/ 這幾列沒有寫死數字。
"""
import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "docs" / "_data" / "source_stats.json"
PAGE = ROOT / "docs" / "sources.md"
# /sources/ 表格裡由本檔供應數字的列（第一欄的標籤）
ROWS = ("**Doenças no grafo**", "**Relações**", "**Registros**", "**Entidades**")


def pt_br(n: int) -> str:
    return f"{n:,}".replace(",", ".")


def rows(path: Path) -> int:
    with open(path, encoding="utf-8", newline="") as f:
        return sum(1 for _ in csv.DictReader(f))


def build() -> dict:
    ext = DATA / "external"
    with open(ext / "drug_disease_relations.csv", encoding="utf-8", newline="") as f:
        rel = Counter(r["relation"] for r in csv.DictReader(f))
    anvisa = json.loads((DATA / "raw" / "br_fda_drugs.json").read_text(encoding="utf-8"))
    v = {
        "txgnn_diseases": rows(ext / "disease_vocab.csv"),
        "txgnn_drug_disease_edges": sum(rel.values()),
        "txgnn_drugbank_drugs": rows(ext / "drugbank_vocab.csv"),
        "anvisa_records": len(anvisa),
        "anvisa_active": sum(1 for d in anvisa if d.get("SITUACAO_REGISTRO") == "Ativo"),
    }
    if not all(v.values()):
        raise SystemExit(f"有來源檔是空的，不寫檔：{v}")
    return {**v, "edges_by_relation": dict(sorted(rel.items())), "display": {k: pt_br(n) for k, n in v.items()}}


def problems() -> list:
    """/sources/ 的 ROWS 列必須用 Liquid 讀 source_stats，不能寫死數字；資料檔要有頁面用到的欄位。"""
    out = []
    if not OUT.exists():
        return ["docs/_data/source_stats.json 不存在（還原 Release 的 data/ 後跑 scripts/generate_source_stats.py）"]
    disp = json.loads(OUT.read_text(encoding="utf-8")).get("display", {})
    text = PAGE.read_text(encoding="utf-8")
    for label in ROWS:
        line = next((ln for ln in text.splitlines() if ln.startswith(f"| {label} |")), None)
        if line is None:
            out.append(f"docs/sources.md：找不到「{label}」列（改了表格就要一起改 scripts/generate_source_stats.py 的 ROWS）")
            continue
        cell = re.sub(r"\{\{.*?\}\}", "", line.split("|", 2)[2])
        if re.search(r"\d", cell):
            out.append(f"docs/sources.md「{label}」列寫死了數字，改用 {{{{ site.data.source_stats.display.* }}}}")
        for key in re.findall(r"site\.data\.source_stats\.display\.(\w+)", line):
            if key not in disp:
                out.append(f"docs/sources.md「{label}」列用到 source_stats 沒有的欄位 {key}")
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--release", help="還原的 data/ 來自哪個 Release（寫進 _source；不給就沿用檔裡原本的值）")
    a = ap.parse_args(argv)
    old = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    release = a.release or old.get("release", "")
    data = {
        "_source": "Calculado a partir de data/ (Release " + (release or "?") + ") por scripts/generate_source_stats.py; não editar. "
                   "Algoritmo no cabeçalho do script.",
        "release": release,
        **build(),
    }
    text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if old != data:
        OUT.write_text(text, encoding="utf-8")
        print(f"更新 {OUT.relative_to(ROOT)}：{data['display']}")
    else:
        print(f"{OUT.relative_to(ROOT)} 不變：{data['display']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
