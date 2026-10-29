"""BR（ANVISA 開放資料）許可證下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv（; 分隔、latin-1，免金鑰；2026-10-30 實測 TLS 憑證可正常驗證）。
欄位：NUMERO_REGISTRO_PRODUTO、SITUACAO_REGISTRO（Ativo／Inativo）。同一登記號多列時，任一列 Ativo 即 Ativo。
證據包紀錄有兩種格式：license_id＋status，或 registration_number＋registration_status；兩種都更新對應的狀態欄。
新檔沒有的登記號保留原狀態。
"""
import csv
import io
import time

import requests

RAW_FILE = "raw/anvisa_situacao.json"
URL = "https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv"


def fetch():
    for attempt in range(4):
        try:
            r = requests.get(URL, timeout=300)
            r.raise_for_status()
            break
        except Exception:
            if attempt == 3:
                raise
            time.sleep(15 * (attempt + 1))
    raw = r.content
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("latin-1")
    rows = csv.DictReader(io.StringIO(text), delimiter=";")
    if "NUMERO_REGISTRO_PRODUTO" not in (rows.fieldnames or []) or "SITUACAO_REGISTRO" not in (rows.fieldnames or []):
        raise RuntimeError(f"欄位改變：{rows.fieldnames}")
    out = {}
    for x in rows:
        k = (x.get("NUMERO_REGISTRO_PRODUTO") or "").strip()
        s = (x.get("SITUACAO_REGISTRO") or "").strip()
        if k and s:
            out[k] = "Ativo" if s == "Ativo" or out.get(k) == "Ativo" else s
    return [{"registro": k, "situacao": v} for k, v in out.items()]


def validate(new, old):
    p = []
    if len(new) < 20000:
        p.append(f"只解析出 {len(new)} 個登記號（ANVISA 通常 >30,000），疑似格式改變")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    return {r["registro"]: r["situacao"] for r in new}


def record_id(rec):
    return str(rec.get("license_id") or rec.get("registration_number") or "").strip()


def update(rec, new):
    key = "registration_status" if "registration_status" in rec and "status" not in rec else "status"
    if rec.get(key) == new:
        return False
    rec[key] = new
    return True
