"""證據包收錯品項的排除規則（2026-11-25 第五輪，用戶決定；規則與依據在 config/bundle_record_exclusions.json）。

早期的子字串收集器把名稱含本藥字串的別的藥收進來（citalopram←escitalopram、iron←dipirona…）。規則：證據包名在規則的
bundles 裡，紀錄成分欄（「,」「+」「;」分段；空白時用品名）有一段符合 family、卻沒有一段符合 keep → 排除。
scripts/exclude_mismatched_records.py、scripts/add_current_registrations.py 與 collectors/brfda.py 共用。
"""
from __future__ import annotations

import json
import re
import unicodedata
from functools import lru_cache
from pathlib import Path

CONF = Path(__file__).resolve().parents[3] / "config" / "bundle_record_exclusions.json"


def _norm(s) -> str:
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", s).strip()


def bundle_key(name) -> str:
    return re.sub(r"[^a-z0-9]+", "_", _norm(name)).strip("_")


@lru_cache(maxsize=None)
def rules() -> dict:
    """證據包名 → [規則]"""
    out = {}
    if not CONF.exists():
        return out
    for r in json.loads(CONF.read_text(encoding="utf-8")).get("rules") or []:
        for b in r["bundles"]:
            out.setdefault(bundle_key(b), []).append(r)
    return out


def components(rec) -> list:
    ing = rec.get("active_ingredient") or rec.get("ingredients") or rec.get("PRINCIPIO_ATIVO") or ""
    cs = [_norm(c) for c in re.split(r"[,+;]", str(ing)) if c.strip()]
    if not cs:  # 成分欄空白：用品名
        name = rec.get("product_name") or rec.get("brand_name_zh") or rec.get("NOME_PRODUTO") or ""
        cs = [_norm(name)] if str(name).strip() else []
    return cs


def match(bundle, rec):
    """這筆紀錄依規則該排除就回傳規則，否則 None"""
    comps = components(rec)
    for r in rules().get(bundle_key(bundle), ()):
        fam, keep = re.compile(r["family"]), re.compile(r["keep"])
        if any(fam.search(c) for c in comps) and not any(keep.search(c) for c in comps):
            return r
    return None


def query_terms(bundle):
    """規則指定改照依成分重建收的成分名（沒有就 None）"""
    for r in rules().get(bundle_key(bundle), ()):
        if r.get("query_terms"):
            return list(r["query_terms"])
    return None
