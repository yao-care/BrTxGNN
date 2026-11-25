#!/usr/bin/env python3
"""依原收集規則補收 ANVISA 現行清單有、證據包沒收的本藥登記號（2026-11-25 第五輪，用戶決定；比照 DkTxGNN 第四輪、HkTxGNN）。

證據包有兩種收法，各照各的規則補（不放寬）：
1. 10-31 依成分重建的證據包（tfda.query_terms，母目錄 .claude/br_rebuild_by_ingredient_20261031.py）：
   PRINCIPIO_ATIVO 依「,」「+」「;」分段、去掉開頭鹽類「xxato／xxeto／xxito／xxido de」後，本藥成分名（query_terms）以整詞出現就算；
   不設筆數上限、各種狀態都收（同一號多列任一列 Ativo 即 Ativo）。現行清單有、證據包沒有的號全部補進 records，total_matches＝紀錄數。
2. 原收集器 collectors/brfda.py 的證據包（license_id 格式）：drug_mapping.csv 依 DrugBank ID 對照、只收非註銷（Ativo）、
   records 最多 20 筆（單方在前）、total_matches＝符合的張數。drug_mapping.csv 是 2026-03 清單做的，之後新註冊的號不在裡面：
   現行清單裡不在 2026-03 清單（data/raw/anvisa_medicamentos.csv）、也不在 drug_mapping 的 Ativo 號，用本站同一支
   map_fda_drugs_to_drugbank（src/brtxgnn/mapping/drugbank_mapper.py）對 DrugBank ID，跟證據包的 drugbank_ids 相交就補；
   records 未滿 20 筆補進 records，滿了只記在 tfda.records_not_stored 並算進 total_matches。
兩種都：證據包已有（records、records_not_stored、excluded_records）的號不補；config/bundle_record_exclusions.json 判定收錯的不補；
每筆記 source（清單與規則）、added（補收日）。只加不刪、可重複執行（第二次跑 0 筆）。
與其他程式的關係：每週 license-refresh.yml 在 merge_duplicate_bundles.py、exclude_mismatched_records.py 之後、license_refresh 前以 --download 跑；
母目錄 br_rebuild_by_ingredient 重建（會整批換掉 records）之後要再跑一次（第 1 類補收的號重建本身就會收進去）。
用法（repo 根目錄，先還原 data/）：python3 scripts/add_current_registrations.py (--download | --csv 現行清單.csv) [--dry-run] [--report 檔.tsv]
"""
import csv
import io
import json
import re
import sys
import time
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from brtxgnn.regulatory import record_exclusions as RX  # noqa: E402

URL = "https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv"
CAP = 20
MIN_ROWS = 20000


# —— 依成分重建的比對規則（同母目錄 .claude/br_rebuild_by_ingredient_20261031.py 的 norm／parts／core／has）——
def norm(x):
    x = unicodedata.normalize("NFKD", str(x or "")).encode("ascii", "ignore").decode().lower()
    return " ".join(x.split())


def core(c):
    return re.sub(r"^\w+(ato|eto|ito|ido) de ", "", c)


def parts(pa):
    return [core(norm(p)) for p in re.split(r"[,+;]", pa or "") if norm(p)]


def has(comp, term):
    return re.search(r"(^|[\s(])" + re.escape(term) + r"($|[\s(),-])", comp) is not None


def load_csv_bytes(raw):
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("latin-1")
    return list(csv.DictReader(io.StringIO(text), delimiter=";"))


def fetch():
    import requests
    for attempt in range(4):
        try:
            r = requests.get(URL, timeout=300)
            r.raise_for_status()
            return r.content
        except Exception:
            if attempt == 3:
                raise
            time.sleep(15 * (attempt + 1))


def rid(r):
    return str(r.get("registration_number") or r.get("license_id") or "").strip()


def ncomp(pa):
    return len([p for p in re.split(r"[,+;]", pa or "") if p.strip()])


def rebuilt_record(x, date, terms):
    return {"registration_number": x["NUMERO_REGISTRO_PRODUTO"].strip(), "product_name": x["NOME_PRODUTO"], "active_ingredient": x["PRINCIPIO_ATIVO"],
            "therapeutic_class": x["CLASSE_TERAPEUTICA"], "regulatory_category": x["CATEGORIA_REGULATORIA"], "product_type": x["TIPO_PRODUTO"],
            "company": x["EMPRESA_DETENTORA_REGISTRO"], "registration_status": x["SITUACAO_REGISTRO"], "process_number": x["NUMERO_PROCESSO"],
            "expiration_date": x["DATA_VENCIMENTO_REGISTRO"], "finalization_date": x["DATA_FINALIZACAO_PROCESSO"],
            "kind": "combo" if ncomp(x["PRINCIPIO_ATIVO"]) > 1 else "single",
            "source": f"ANVISA DADOS_ABERTOS_MEDICAMENTOS {date}（依成分，query_terms {', '.join(terms)}）", "added": time.strftime("%Y-%m-%d")}


def collector_record(x, date, dbs):
    pa = x["PRINCIPIO_ATIVO"]
    return {"license_id": x["NUMERO_REGISTRO_PRODUTO"].strip(), "brand_name_zh": x["NOME_PRODUTO"], "brand_name_en": pa, "ingredients": pa,
            "indication": x["CLASSE_TERAPEUTICA"], "dosage_form": "", "manufacturer": "", "license_holder": "", "approval_date": "", "expiry_date": "",
            "status": x["SITUACAO_REGISTRO"],
            "source": f"ANVISA DADOS_ABERTOS_MEDICAMENTOS {date}（新註冊，map_fda_drugs_to_drugbank → {', '.join(sorted(dbs))}）", "added": time.strftime("%Y-%m-%d")}


def main(argv):
    dry = "--dry-run" in argv
    if "--csv" in argv:
        p = Path(argv[argv.index("--csv") + 1])
        raw, date = p.read_bytes(), time.strftime("%Y-%m-%d", time.gmtime(p.stat().st_mtime))
    elif "--download" in argv:
        raw, date = fetch(), time.strftime("%Y-%m-%d")
    else:
        sys.exit("要給 --download 或 --csv 現行清單.csv")
    report = Path(argv[argv.index("--report") + 1]) if "--report" in argv else None
    cur = load_csv_bytes(raw)
    if len(cur) < MIN_ROWS or "PRINCIPIO_ATIVO" not in (cur[0] if cur else {}):
        sys.exit(f"現行清單只有 {len(cur)} 列或缺 PRINCIPIO_ATIVO 欄，不補收")
    byreg = {}
    for x in cur:  # 同號多列：任一列 Ativo 即 Ativo
        k = (x.get("NUMERO_REGISTRO_PRODUTO") or "").strip()
        if k and (k not in byreg or (x.get("SITUACAO_REGISTRO") == "Ativo" and byreg[k].get("SITUACAO_REGISTRO") != "Ativo")):
            byreg[k] = x
    by_word = {}
    for k, x in byreg.items():
        pa = x.get("PRINCIPIO_ATIVO") or ""
        for w in {w for c in parts(pa) + [norm(q) for q in re.split(r"[,+;]", pa)] for w in re.findall(r"[\w-]+", c)}:
            by_word.setdefault(w, []).append(k)
    base_f = ROOT / "data/raw/anvisa_medicamentos.csv"
    if not base_f.exists():
        sys.exit("缺 data/raw/anvisa_medicamentos.csv（2026-03 清單），不補收")
    base = {(x.get("NUMERO_REGISTRO_PRODUTO") or "").strip() for x in load_csv_bytes(base_f.read_bytes())}
    dm = {r["license_id"].strip() for r in csv.DictReader(open(ROOT / "data/processed/drug_mapping.csv", encoding="utf-8"))}
    # 第 2 類候選：新註冊（不在 2026-03 清單、不在 drug_mapping）、Ativo 的號 → 本站 mapper 對 DrugBank ID
    fresh = [k for k, x in byreg.items() if k not in base and k not in dm and x.get("SITUACAO_REGISTRO") == "Ativo" and (x.get("PRINCIPIO_ATIVO") or "").strip()]
    fresh_db = {}
    if fresh:
        import pandas as pd
        from brtxgnn.mapping.drugbank_mapper import map_fda_drugs_to_drugbank
        mp = map_fda_drugs_to_drugbank(pd.DataFrame([byreg[k] for k in fresh]))
        for _, r in mp.iterrows():
            if r["mapping_success"] and r["drugbank_id"]:
                fresh_db.setdefault(str(r["license_id"]).strip(), set()).add(str(r["drugbank_id"]))
    rows_out, nb, nrec, nns = [], 0, 0, 0
    for f in sorted((ROOT / "data/bundles").glob("*/drug_bundle.json")):
        name = f.parent.name
        b = json.loads(f.read_text(encoding="utf-8"))
        t = b.get("tfda") or {}
        recs = t.get("records") or []
        have = {rid(r) for r in recs} | {rid(r) for r in t.get("excluded_records") or []} | {str(x).strip() for x in t.get("records_not_stored") or []}
        terms = t.get("query_terms")
        add, ns = [], []
        if terms:
            ks = {k for tm in terms for w in tm.split() for k in by_word.get(w, [])}
            for k in sorted(ks):
                if k in have:
                    continue
                x = byreg[k]
                pa = x.get("PRINCIPIO_ATIVO") or ""
                if not any(has(p, tm) for p in parts(pa) + [norm(q) for q in re.split(r"[,+;]", pa) if norm(q)] for tm in terms):
                    continue
                rec = rebuilt_record(x, date, terms)
                if RX.match(name, rec):
                    continue
                add.append(rec)
        elif recs and "license_id" in recs[0] or (not recs and t.get("drugbank_ids")):
            dbs = set(t.get("drugbank_ids") or []) | ({b["drug"]["drugbank_id"]} if (b.get("drug") or {}).get("drugbank_id") else set())
            for k in sorted(fresh_db):
                if k in have or not (fresh_db[k] & dbs):
                    continue
                rec = collector_record(byreg[k], date, fresh_db[k] & dbs)
                if RX.match(name, rec):
                    continue
                add.append(rec)
        if not add:
            continue
        if terms:
            new_recs = sorted(recs + add, key=lambda r: ((r.get("registration_status") or r.get("status")) != "Ativo", rid(r)))
            total = len(new_recs) + len(t.get("records_not_stored") or [])
        else:
            room = max(0, CAP - len(recs))
            add = sorted(add, key=lambda r: ncomp(r["ingredients"]))  # 原收集器：單方在前
            ns = [r["license_id"] for r in add[room:]]
            add = add[:room]
            new_recs = recs + add
            total = int(t.get("total_matches") or len(recs)) + len(add) + len(ns)
        nb += 1
        nrec += len(add)
        nns += len(ns)
        for r in add:
            rows_out.append((name, "records", rid(r), r.get("product_name") or r.get("brand_name_zh"), r.get("active_ingredient") or r.get("ingredients"), r.get("registration_status") or r.get("status"), "new" if rid(r) not in base else "in-2026-03"))
        for k in ns:
            x = byreg[k]
            rows_out.append((name, "not_stored", k, x["NOME_PRODUTO"], x["PRINCIPIO_ATIVO"], x["SITUACAO_REGISTRO"], "new"))
        print(f"{name}\t{'依成分' if terms else '原收集器'}\t+{len(add)}{f'（另 {len(ns)} 筆只算張數）' if ns else ''}\t{len(recs)} → {len(new_recs)} 筆；total_matches {t.get('total_matches')} → {total}")
        if dry:
            continue
        t["records"] = new_recs
        if ns:
            t["records_not_stored"] = (t.get("records_not_stored") or []) + ns
        t["total_matches"] = total
        t["found"] = True
        b["tfda"] = t
        f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if report:
        with open(report, "w", encoding="utf-8") as fh:
            fh.write("bundle\twhere\tregistro\tproduto\tprincipio_ativo\tsituacao\tbase\n")
            for r in rows_out:
                fh.write("\t".join(str(c or "") for c in r) + "\n")
    print(f"補收：{nb} 個證據包、存進 records {nrec} 筆、只算張數 {nns} 筆（現行清單 {date}，{len(byreg)} 個登記號；新註冊候選 {len(fresh)}，對到 DrugBank {len(fresh_db)}）{'（試跑，沒寫檔）' if dry else ''}")
    return nb


if __name__ == "__main__":
    main(sys.argv[1:])
