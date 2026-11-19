"""同一 DrugBank ID 的重複公開頁「合併後轉址」：把被轉址頁的許可證併進保留頁的證據包（2026-11-19，用戶決定）。

背景：公開藥物頁 arginine／arginine_aspartate／arginine_glutamate（DB00125）、levometionina／methionine（DB00134）預測相同，
但各頁證據包收的登記號不同（arginine 是 10-31 依成分 arginina 重建的 73 個；arginine_aspartate 等是原收集器依
data/processed/drug_mapping.csv 的 DrugBank ID 收的，最多 20 筆），所以 11-19 第一輪轉址時沒轉。用戶決定合併：
被轉址頁改轉址，它的登記號併進保留頁的證據包。

收錄規則（照本站原規則，不放寬）：保留頁證據包原有的登記號＋被轉址頁證據包的登記號＋drug_mapping.csv 裡對到同一個
DrugBank ID 的登記號（原收集器 collectors/brfda.py 的規則；methionine 證據包因 20 筆上限少收的 100419935 AMINOVEN 由這條補回）。
新加的紀錄照依成分重建的格式（registration_number、product_name…，母目錄 .claude/br_rebuild_by_ingredient_20261031.py），
欄位取 data/raw/anvisa_medicamentos.csv（同號多列任一列 Ativo 即 Ativo），狀態取 data/raw/anvisa_situacao.json（每週排程的現行狀態），
另記 source、merged_from（被轉址頁證據包名／drug_mapping）、added。total_matches＝紀錄數。
只加不刪、可重複執行；依成分重建（會整批換掉 records）或重新收集證據包之後要再跑一次。每週排程（license-refresh.yml）在 license_refresh 前先跑。
2026-11-19 同日補：l-arginina → arginine、l-metionina／dl-metionina → levometionina（見 MERGES 下的說明）。
用法（repo 根目錄）：python3 scripts/merge_duplicate_bundles.py [--dry-run]
"""
import csv
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
ADDED = "2026-11-19"
SOURCE = "ANVISA DADOS_ABERTOS_MEDICAMENTOS（同一 DrugBank ID 合併，2026-11-19）"

# 保留頁證據包 → (DrugBank ID, 被轉址頁證據包)
MERGES = {
    "arginine": ("DB00125", ["arginine_aspartate", "arginine_glutamate", "l-arginina"]),
    "levometionina": ("DB00134", ["methionine", "l-metionina", "dl-metionina"]),
}
# l-arginina、l-metionina、dl-metionina（2026-11-19 補，用戶決定「補進來」）：沒有藥物頁的證據包，10-31 依成分重建時以
# 「l-arginina」等寫法收的登記號；保留頁依整詞 arginina／levometionina 重建，認不到 l- / dl- 前綴寫法，所以少收。
# drug_mapping.csv 把 L-ARGININA 對到 DB00125、L-METIONINA 與 DL-METIONINA（外消旋體，本站對照如此）對到 DB00134，
# 跟保留頁同一個 DrugBank ID；只收這 3 個證據包（不放寬一般成分比對）。這 3 個證據包本身不刪。


def rid(r):
    return str(r.get("registration_number") or r.get("license_id") or "").strip()


def load_bundle(name):
    f = DATA / "bundles" / name / "drug_bundle.json"
    return f, json.loads(f.read_text(encoding="utf-8"))


def anvisa_rows():
    raw = (DATA / "raw/anvisa_medicamentos.csv").read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("latin-1")
    by = {}
    for x in csv.DictReader(io.StringIO(text), delimiter=";"):
        k = (x.get("NUMERO_REGISTRO_PRODUTO") or "").strip()
        if k and (k not in by or (x.get("SITUACAO_REGISTRO") == "Ativo" and by[k].get("SITUACAO_REGISTRO") != "Ativo")):
            by[k] = x
    return by


def record_from_row(x, status, merged_from):
    ps = [p for p in re.split(r"[,+;]", x.get("PRINCIPIO_ATIVO") or "") if p.strip()]
    return {"registration_number": x["NUMERO_REGISTRO_PRODUTO"].strip(), "product_name": x["NOME_PRODUTO"],
            "active_ingredient": x["PRINCIPIO_ATIVO"], "therapeutic_class": x["CLASSE_TERAPEUTICA"],
            "regulatory_category": x["CATEGORIA_REGULATORIA"], "product_type": x["TIPO_PRODUTO"],
            "company": x["EMPRESA_DETENTORA_REGISTRO"], "registration_status": status or x["SITUACAO_REGISTRO"],
            "process_number": x["NUMERO_PROCESSO"], "expiration_date": x["DATA_VENCIMENTO_REGISTRO"],
            "finalization_date": x["DATA_FINALIZACAO_PROCESSO"], "kind": "combo" if len(ps) > 1 else "single",
            "source": SOURCE, "merged_from": merged_from, "added": ADDED}


def record_from_old(r, status, merged_from):
    """ANVISA 全量裡沒有這個號（不應發生）：照被轉址頁證據包的舊格式紀錄轉"""
    ing = r.get("ingredients") or r.get("active_ingredient") or ""
    return {"registration_number": rid(r), "product_name": r.get("brand_name_zh") or r.get("product_name") or "",
            "active_ingredient": ing, "therapeutic_class": r.get("indication") or "", "company": r.get("license_holder") or "",
            "registration_status": status or r.get("status") or r.get("registration_status") or "",
            "kind": "combo" if len([p for p in re.split(r"[,+;]", ing) if p.strip()]) > 1 else "single",
            "source": SOURCE, "merged_from": merged_from, "added": ADDED}


def main(argv):
    dry = "--dry-run" in argv
    rows = anvisa_rows()
    sit = {x["registro"]: x["situacao"] for x in json.loads((DATA / "raw/anvisa_situacao.json").read_text(encoding="utf-8"))}
    dmap = {}
    for x in csv.DictReader(open(DATA / "processed/drug_mapping.csv", encoding="utf-8")):
        if x.get("drugbank_id"):
            dmap.setdefault(x["drugbank_id"], set()).add(x["license_id"].strip())
    for keep, (dbid, drops) in MERGES.items():
        f, b = load_bundle(keep)
        t = b.setdefault("tfda", {})
        recs = t.get("records") or []
        have = {rid(r) for r in recs}
        want = {}  # 號 → (來源, 舊紀錄)
        for d in drops:
            for r in (load_bundle(d)[1].get("tfda") or {}).get("records") or []:
                want.setdefault(rid(r), [[], r])[0].append(d)
        for k in sorted(dmap.get(dbid, ())):
            want.setdefault(k, [[], None])[0].append(f"drug_mapping.csv {dbid}")
        add = []
        for k, (src, old) in sorted(want.items()):
            if not k or k in have:
                continue
            add.append(record_from_row(rows[k], sit.get(k), src) if k in rows else record_from_old(old or {"registration_number": k}, sit.get(k), src))
        before = len(recs)
        if add:
            recs = sorted(recs + add, key=lambda r: (r.get("registration_status") != "Ativo", rid(r)))
            t.update({"records": recs, "found": True})
        ch = bool(add) or t.get("total_matches") != len(recs)
        t["total_matches"] = len(recs)
        act = sum(1 for r in recs if (r.get("registration_status") or r.get("status")) == "Ativo")
        print(f"{keep}\t{before} → {len(recs)} 個登記號（Ativo {act}）\t補 {len(add)}：{','.join(rid(r) for r in add)}")
        if ch and not dry:
            f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1:])
