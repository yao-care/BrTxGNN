#!/usr/bin/env python3
"""處理巴西 ANVISA 藥品資料

從 ANVISA 開放資料下載藥品註冊資料並轉換為 JSON 格式。

使用方法:
    uv run python scripts/process_fda_data.py

資料來源:
    https://dados.anvisa.gov.br/dados/DADOS_ABERTOS_MEDICAMENTOS.csv

產生檔案:
    data/raw/br_fda_drugs.json
"""

import json
import warnings
from pathlib import Path

import pandas as pd
import requests
import urllib3
import yaml

# Suppress SSL warnings for ANVISA server (has certificate issues)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def load_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def download_anvisa_data(output_path: Path) -> Path:
    """從 ANVISA 下載藥品資料

    Args:
        output_path: CSV 輸出路徑

    Returns:
        下載的檔案路徑
    """
    config = load_config()
    url = config["data_source"]["url"]

    print(f"正在從 ANVISA 下載資料...")
    print(f"URL: {url}")

    # ANVISA server has SSL certificate issues, so we need to skip verification
    response = requests.get(url, timeout=180, verify=False)
    response.raise_for_status()

    # 確保輸出目錄存在
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "wb") as f:
        f.write(response.content)

    print(f"下載完成: {output_path}")
    print(f"檔案大小: {output_path.stat().st_size / 1024 / 1024:.1f} MB")

    return output_path


def process_anvisa_csv(csv_path: Path, output_path: Path) -> Path:
    """處理 ANVISA CSV 並轉換為 JSON

    Args:
        csv_path: CSV 檔案路徑
        output_path: JSON 輸出路徑

    Returns:
        輸出檔案路徑
    """
    config = load_config()
    encoding = config["data_source"].get("encoding", "latin-1")
    delimiter = config["data_source"].get("delimiter", ";")

    print(f"讀取 CSV 檔案: {csv_path}")

    # 讀取 CSV (ANVISA 使用 Latin-1 編碼和分號分隔)
    df = pd.read_csv(
        csv_path,
        encoding=encoding,
        delimiter=delimiter,
        dtype=str,  # 全部作為字串讀取，避免類型問題
        on_bad_lines="skip",  # 跳過格式錯誤的行
    )

    print(f"原始資料筆數: {len(df)}")

    # 過濾僅保留藥品 (MEDICAMENTO)
    filters = config.get("filters", {})
    product_type_filter = filters.get("product_type")
    if product_type_filter and "TIPO_PRODUTO" in df.columns:
        df = df[df["TIPO_PRODUTO"] == product_type_filter]
        print(f"過濾後資料筆數 (僅 {product_type_filter}): {len(df)}")

    # 清理資料
    df = df.fillna("")

    # 轉換為 JSON 格式
    data = df.to_dict(orient="records")

    # 確保輸出目錄存在
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # 儲存 JSON
    print(f"儲存至: {output_path}")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"完成！共 {len(data)} 筆藥品資料")

    # 顯示統計
    print_statistics(df, config)

    return output_path


def print_statistics(df: pd.DataFrame, config: dict):
    """印出資料統計"""
    fm = config["field_mapping"]
    status_field = fm["status"]
    ingredients_field = fm["ingredients"]
    category_field = fm["category"]

    print("\n" + "=" * 50)
    print("資料統計")
    print("=" * 50)

    # 狀態統計
    if status_field in df.columns:
        print(f"\n註冊狀態分布:")
        status_counts = df[status_field].value_counts()
        for status, count in status_counts.items():
            print(f"  {status}: {count:,}")

    # 有活性成分的比例
    if ingredients_field in df.columns:
        with_ingredients = (df[ingredients_field] != "").sum()
        print(f"\n有活性成分: {with_ingredients:,} ({with_ingredients/len(df)*100:.1f}%)")

    # 監管類別統計
    if category_field in df.columns:
        print(f"\n監管類別分布:")
        category_counts = df[category_field].value_counts().head(10)
        for category, count in category_counts.items():
            if category:
                print(f"  {category}: {count:,}")


def main():
    print("=" * 60)
    print("處理巴西 ANVISA 藥品資料")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    raw_dir = base_dir / "data" / "raw"
    csv_path = raw_dir / "anvisa_medicamentos.csv"
    output_path = raw_dir / "br_fda_drugs.json"

    # 確保 raw 目錄存在
    raw_dir.mkdir(parents=True, exist_ok=True)

    # 下載資料（如果不存在）
    if not csv_path.exists():
        download_anvisa_data(csv_path)
    else:
        print(f"使用已存在的 CSV 檔案: {csv_path}")

    # 處理 CSV
    process_anvisa_csv(csv_path, output_path)

    print()
    print("下一步: 準備詞彙表資料")
    print("  uv run python scripts/prepare_external_data.py")


if __name__ == "__main__":
    main()
