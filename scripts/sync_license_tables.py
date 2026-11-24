#!/usr/bin/env python3
"""藥物頁「## Informações de Comercialização no Brasil」段落的許可證表一律由程式依證據包產生（2026-11-24，用戶決定）。

為什麼：每週許可證排程（母目錄 license_refresh_20261029.py）只改程式管得到的格子；AI 寫的自由格式許可證表
（「Número de Registro | Nome Comercial | Forma Farmacêutica | Indicação Aprovada」等）的列、狀態與張數跟著 ANVISA 資料過期，
checker 擋頁、要人處理。10-31 母目錄 br_rebuild_by_ingredient_20261031.py --tables 一次性重建過一批表（沒有標記、之後不再同步），
本支把那套表格寫法變成每次都跑的程式：
- 段落裡的第一張表（AI 表、known_use_pages 的表、10-31 重建的表都算）換成程式表，前後加
  「<!-- licenses:begin -->」「<!-- licenses:end -->」標記；已有標記就換掉標記之間的內容。
- 表頭「| Registro | Produto | Empresa detentora | Situação |」（10-31 重建表的寫法；證據包是原收集器格式、沒有持有人欄的，三欄不放持有人）；最多 30 列、Ativo 在前、再依登記號；
  狀態用 ANVISA 原文 Ativo，其他（Inativo）寫本站既有用語 Cancelado（.claude/license_labels/BrTxGNN.json）。
- 登記號超過 30 個：表下一句「A tabela mostra até 30 registros (os ativos primeiro), de N registros nos dados. …」；
  證據包只收了一部分（total_matches 大於紀錄數）：另一句「Os dados contêm apenas parte dos registros; a lista pode estar incompleta.」。
- 證據包沒有任何紀錄：表換成一句 NONE_LINE。段落裡沒有表、也沒有標記的頁不新增（同 10-31 重建）。
- 段落裡、程式區塊外跟程式句相同的行（MORE、PARTIAL_NOTE，以前重排時重複插入的）一併拿掉。
資料來源兩種：bundle（data/bundles 的 tfda.records；每週排程 adapter 的 sync_tables、手動）與 snapshot
（snapshots/br_licenses.json.gz 的 rows／total／partial；scripts/apply_drug_reviews.py 結尾、scripts/build_license_snapshot.py 結尾，不需要 data/）。
gate（src/brtxgnn/regulatory/licenses.py 的 program_block_problems）擋「程式區塊≠快照重算結果」。
用法（repo 根目錄）：python3 scripts/sync_license_tables.py [--from-snapshot] [--dry-run] [頁 ...]
"""
import gzip
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC = "## Informações de Comercialização no Brasil"
HEAD = ["| Registro | Produto | Empresa detentora | Situação |", "|------|------|------|------|"]
HEAD3 = ["| Registro | Produto | Situação |", "|------|------|------|"]  # 證據包沒有持有人資料（原收集器格式）時
CAP = 30
MORE = ("A tabela mostra até 30 registros (os ativos primeiro), de {m} registros nos dados. "
        "A lista completa está na consulta de medicamentos da ANVISA (https://consultas.anvisa.gov.br/#/medicamentos/).")
MORE_RX = re.compile(r"^A tabela mostra até \d+ registros \(os ativos primeiro\)")
PART_NOTE = "Os dados contêm apenas parte dos registros; a lista pode estar incompleta."
NONE_LINE = "Não há registros deste medicamento nos dados abertos de medicamentos da ANVISA usados neste relatório."
BEGIN, END = "<!-- licenses:begin -->", "<!-- licenses:end -->"
# 每週排程 3b 自我檢查用（license_adapter.PAGE_NOTE）：程式區塊裡表格列以外的行
NOTE_RX = r"^(A tabela mostra até \d+ registros \(os ativos primeiro\).*|" + re.escape(PART_NOTE) + "|" + re.escape(NONE_LINE) + r"|<!-- licenses:(begin|end) -->)$"
SNAP = ROOT / "snapshots" / "br_licenses.json.gz"


def _cell(x, n):
    t = re.sub(r"\s+", " ", str(x or "").replace("|", "/")).strip()
    return t[:n]


def _rid(r):
    return str(r.get("registration_number") or r.get("license_id") or "").strip()


def _active(r):
    return (r.get("registration_status") if "registration_number" in r else r.get("status")) == "Ativo"


def table_rows(recs):
    """證據包紀錄 → 表格列（全部，依 Ativo 在前、登記號排序；同號多筆任一 Ativo 即 Ativo）"""
    by = {}
    for r in recs or []:
        k = _rid(r)
        if not k:
            continue
        if k in by and (_active(by[k]) or not _active(r)):
            continue
        by[k] = r
    out = []
    items = sorted(by.items(), key=lambda kv: (not _active(kv[1]), kv[0]))
    has_comp = any(r.get("company") or r.get("license_holder") or r.get("manufacturer") for _, r in items)
    for k, r in items:
        prod = r.get("product_name") if "registration_number" in r else r.get("brand_name_zh")
        st = "Ativo" if _active(r) else "Cancelado"
        if has_comp:
            comp = re.sub(r"^[0-9]+ - ", "", str(r.get("company") or r.get("license_holder") or r.get("manufacturer") or "")).strip() or "—"
            out.append(f"| {k} | {_cell(prod, 60)} | {_cell(comp, 50)} | {st} |")
        else:  # 原收集器格式的證據包沒有持有人欄：不放整欄「—」，改三欄表（HEAD3）
            out.append(f"| {k} | {_cell(prod, 60)} | {st} |")
    return out


def rows_of(tf):
    """快照用：(前 CAP 列, 總數, partial)"""
    recs = tf.get("records") or []
    rows = table_rows(recs)
    return rows[:CAP], len(rows), int(tf.get("total_matches") or 0) > len(recs)


def program_block(rows, total, partial):
    if not rows:
        return [NONE_LINE]
    out = (HEAD if rows[0].count("|") == 5 else HEAD3) + rows[:CAP]
    notes = ([MORE.format(m=total)] if total > CAP else []) + ([PART_NOTE] if partial else [])
    return out + ([""] + notes if notes else [])


def _section(lines):
    if SEC not in lines:
        return None, None
    a = lines.index(SEC) + 1
    return a, next((k for k in range(a, len(lines)) if lines[k].startswith("## ")), len(lines))


def process(text, rows, total, partial):
    """回傳新頁面；段落沒有表也沒有標記時回傳原文"""
    lines = text.split("\n")
    a, b = _section(lines)
    if a is None:
        return text
    blk = [BEGIN, ""] + program_block(rows, total, partial) + ["", END]
    if BEGIN in lines[a:b] and END in lines[a:b]:
        x, y = lines.index(BEGIN, a), lines.index(END, a)
    else:
        tb = [k for k in range(a, b) if lines[k].startswith("|")]
        if not tb:
            return text
        x = y = tb[0]
        while y + 1 < b and lines[y + 1].startswith("|"):
            y += 1
    head = lines[:x]
    while head and not head[-1].strip():
        head.pop()
    rest = lines[y + 1:b]
    rest = [l for l in rest if not (MORE_RX.match(l.strip()) or l.strip() in (PART_NOTE, NONE_LINE))]
    while rest and not rest[0].strip():
        rest.pop(0)
    out = head + [""] + blk + [""] + rest
    if b < len(lines) and out[-1].strip():
        out.append("")
    out += lines[b:]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))


def _snap():
    return json.loads(gzip.open(SNAP).read().decode("utf-8")).get("drugs", {}) if SNAP.exists() else {}


def _bundle(stem):
    for key in (stem, stem.replace("-", "_"), stem.replace("_", "-")):
        f = ROOT / "data/bundles" / key / "drug_bundle.json"
        if f.exists():
            return json.loads(f.read_text(encoding="utf-8")).get("tfda") or {}
    return None


def run(only=None, from_snapshot=False, dry=False):
    snap = _snap() if from_snapshot else None
    changed = []
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only and page.stem not in only and page.name not in only:
            continue
        raw = page.read_bytes().decode("utf-8")
        if "layout: id_redirect" in raw[:3000] or 'http-equiv="refresh"' in raw[:3000]:
            continue
        if from_snapshot:
            e = snap.get(page.stem)
            if not e or "rows" not in e:
                continue
            rows, total, partial = e["rows"], e["total"], e["partial"]
        else:
            tf = _bundle(page.stem)
            if tf is None:
                continue
            rows, total, partial = rows_of(tf)
        crlf = "\r\n" in raw[:500]
        t0 = raw.replace("\r\n", "\n")
        new = process(t0, rows, total, partial)
        if new != t0:
            changed.append(page.stem)
            if not dry:
                page.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    return changed


if __name__ == "__main__":
    a = sys.argv[1:]
    ch = run({x for x in a if not x.startswith("--")} or None, "--from-snapshot" in a, "--dry-run" in a)
    print(f"許可證表（程式區塊）：改 {len(ch)} 頁" + ("（dry-run）" if "--dry-run" in a else ""))
