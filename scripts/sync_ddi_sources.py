#!/usr/bin/env python3
"""DDInter／Guide to PHARMACOLOGY（GtoPdb）的筆數與版本：.github/ddi-versions.json 的 site_data
→ docs/_data/ddi_sources.json（BrTxGNN，2026-11-05）。

頁面（docs/sources.md 的「Interações medicamentosas」段等）用 Liquid 讀 site.data.ddi_sources，
數字用 display 裡的 pt-BR 千分位字串（222.383），不要手寫。site_data 是本站 Release 資料檔實算的值，
重算方式見 site_data.note；改了 site_data 就跑這支重寫資料檔。check_seo_docs.py 第 12 項呼叫 problems()。

用法：python3 scripts/sync_ddi_sources.py          # 重寫 docs/_data/ddi_sources.json
      python3 scripts/sync_ddi_sources.py --check  # 只檢查，不一致就非零
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSIONS = ROOT / ".github" / "ddi-versions.json"
OUT = ROOT / "docs" / "_data" / "ddi_sources.json"
# 本站 site_data 有的欄位（Br 沒有 DFI／DDSI／DHI 資料）
KEYS = ("ddinter_rows", "ddinter_unique_pairs", "ddinter_drug_names",
        "gtopdb_version", "gtopdb_drug_target_records", "gtopdb_release")
# 檢查手寫數字時略過的目錄（藥物頁、新聞、FHIR 等是產線產生的，不在這裡管）
SKIP = {"_site", "_drugs", "_news", "fhir", "data", "vendor", "node_modules", ".jekyll-cache", ".sass-cache"}
CTX = re.compile(r"DDInter(?!act)|GtoPdb|PHARMACOLOGY")


def pt_br(n: int) -> str:
    return f"{n:,}".replace(",", ".")


def build() -> dict:
    sd = json.loads(VERSIONS.read_text(encoding="utf-8")).get("site_data", {})
    missing = [k for k in KEYS if k not in sd]
    if missing:
        raise SystemExit(f".github/ddi-versions.json 的 site_data 缺 {missing}")
    data = {"_note": "Gerado por scripts/sync_ddi_sources.py a partir de site_data em .github/ddi-versions.json; não editar."}
    data.update({k: sd[k] for k in KEYS})
    data["display"] = {k: pt_br(sd[k]) for k in KEYS if isinstance(sd[k], int)}
    return data


def text(data: dict) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def problems() -> list:
    data = build()
    out = []
    if not OUT.exists() or OUT.read_text(encoding="utf-8") != text(data):
        out.append("docs/_data/ddi_sources.json 與 .github/ddi-versions.json 的 site_data 不一致（跑 scripts/sync_ddi_sources.py）")
    # 頁面正文提到 DDInter／GtoPdb 的行（含後 3 行，涵蓋表格下一列）不得手寫 site_data 的數字（pt-BR 或英文千分位都算）與 GtoPdb 版本
    vals = set()
    for k, v in data.items():
        if isinstance(v, int):
            vals |= {pt_br(v), f"{v:,}", str(v)}
    vals.add(data["gtopdb_version"])
    rx = re.compile(r"(?<![\d.,])(" + "|".join(re.escape(v) for v in sorted(vals, key=len, reverse=True)) + r")(?![\d.,]?\d)")
    docs = ROOT / "docs"
    for f in sorted(docs.rglob("*")):
        if f.suffix not in (".md", ".html") or not f.is_file() or SKIP & set(f.relative_to(docs).parts[:-1]):
            continue
        lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
        body = 0
        if lines and lines[0].strip() == "---":
            body = next((i + 1 for i in range(1, len(lines)) if lines[i].strip() == "---"), 0)
        bad = set()
        for i in range(body, len(lines)):
            if CTX.search(lines[i]):
                for j in range(i, min(i + 4, len(lines))):
                    bad |= {(j + 1, m.group(1)) for m in rx.finditer(lines[j])}
        out += [f"docs/{f.relative_to(docs)}:{n} 手寫了 {v}（改用 site.data.ddi_sources 的 Liquid）" for n, v in sorted(bad)]
    return out


def main() -> int:
    if "--check" in sys.argv[1:]:
        p = problems()
        for e in p:
            print("✗", e)
        return 1 if p else 0
    OUT.write_text(text(build()), encoding="utf-8")
    print(f"✓ {OUT.relative_to(ROOT)}")
    p = problems()
    for e in p:
        print("✗", e)
    return 1 if p else 0


if __name__ == "__main__":
    raise SystemExit(main())
