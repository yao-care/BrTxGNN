#!/usr/bin/env python3
"""證據包收錯品項移出（2026-11-25 第五輪，用戶決定；照 CHTxGNN 第三輪）：依 config/bundle_record_exclusions.json，
把 data/bundles/*/drug_bundle.json 裡早期子字串收集器收錯的紀錄（citalopram 收到 escitalopram 等）從 tfda.records 移到
tfda.excluded_records（附 excluded＝第一次排除日、excluded_reason、excluded_basis），不刪資料。
規則有 query_terms 的證據包：tfda.query_terms 寫成規則的成分名（10-31 依成分重建的寫法），total_matches 改成留下的紀錄數
（原值是子字串命中列數、含收錯的，存 total_matches_before_exclusion）；之後 scripts/add_current_registrations.py 依現行清單、
照依成分重建的整詞比對規則補齊。沒有 query_terms 的規則：total_matches 扣掉移出的筆數。
只移不刪、可重複執行（已移出的不再扣）。每週 license-refresh.yml 在 license_refresh 前先跑；改完要重算證據包 local_regulatory、事實層與快照。
用法（repo 根目錄，先還原 data/）：python3 scripts/exclude_mismatched_records.py [--dry-run]
"""
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from brtxgnn.regulatory import record_exclusions as RX  # noqa: E402


def _rid(r):
    return str(r.get("registration_number") or r.get("license_id") or "").strip()


def run(dry=False):
    today = time.strftime("%Y-%m-%d")
    moved, touched = 0, []
    for f in sorted((ROOT / "data" / "bundles").glob("*/drug_bundle.json")):
        name = f.parent.name
        if RX.bundle_key(name) not in RX.rules():
            continue
        b = json.loads(f.read_text(encoding="utf-8"))
        t = b.get("tfda") or {}
        keep, out = [], []
        for r in t.get("records") or []:
            rule = RX.match(name, r)
            if rule:
                out.append(dict(r, excluded=today, excluded_reason=rule["reason"], excluded_basis=rule["basis"]))
            else:
                keep.append(r)
        qt = RX.query_terms(name)
        set_qt = bool(qt) and t.get("query_terms") != qt
        if not out and not set_qt:
            continue
        for r in out:
            print(f"  {name}: 移出 {_rid(r) or '（無登記號）'} {str(r.get('product_name') or r.get('brand_name_zh'))[:45]}（{str(r.get('active_ingredient') or r.get('ingredients') or '')[:60]}）")
        moved += len(out)
        touched.append(name)
        if dry:
            continue
        t["records"] = keep
        if out:
            t["excluded_records"] = (t.get("excluded_records") or []) + out
        if set_qt:
            t.setdefault("total_matches_before_exclusion", t.get("total_matches"))
            t["query_terms"] = qt
            t["query_terms_source"] = "config/bundle_record_exclusions.json（2026-11-25，依成分重建規則）"
            t["total_matches"] = len(keep)
        elif out:
            t["total_matches"] = max(len(keep), int(t.get("total_matches") or 0) - len(out))
        t["found"] = bool(keep)
        b["tfda"] = t
        f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"證據包收錯品項：移出 {moved} 筆（{len(touched)} 個證據包）{'（試跑，沒寫檔）' if dry else ''}")
    return touched


if __name__ == "__main__":
    run(dry="--dry-run" in sys.argv[1:])
