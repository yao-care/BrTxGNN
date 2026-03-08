"""ANVISA 藥品資料載入與過濾

載入巴西 ANVISA 藥品註冊資料。
"""

import json
from pathlib import Path
from typing import Optional

import pandas as pd
import yaml


def load_config() -> dict:
    """載入欄位映射設定

    Returns:
        設定字典
    """
    config_path = Path(__file__).parent.parent.parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_fda_drugs(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入巴西 ANVISA 藥品資料

    Args:
        filepath: JSON 檔案路徑，預設為 data/raw/br_fda_drugs.json

    Returns:
        包含所有藥品的 DataFrame

    Raises:
        FileNotFoundError: 找不到 ANVISA 資料檔案時，提供下載指引
    """
    if filepath is None:
        # loader.py -> data -> txgnn -> src -> BrTxGNN
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "raw" / "br_fda_drugs.json"

    if not filepath.exists():
        raise FileNotFoundError(
            f"找不到 ANVISA 藥品資料: {filepath}\n"
            f"請先執行以下步驟：\n"
            f"1. 執行: uv run python scripts/process_fda_data.py\n"
            f"   (腳本會自動從 ANVISA 下載資料)"
        )

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    return df


def filter_active_drugs(df: pd.DataFrame) -> pd.DataFrame:
    """過濾有效藥品（排除已註銷）

    Args:
        df: 原始藥品 DataFrame

    Returns:
        僅包含有效藥品的 DataFrame
    """
    config = load_config()
    status_field = config["field_mapping"]["status"]
    ingredients_field = config["field_mapping"]["ingredients"]
    active_statuses = config.get("active_statuses", ["Ativo"])

    # 過濾有效狀態的藥品
    active = df[df[status_field].isin(active_statuses)].copy()

    # 過濾有主成分的藥品（TxGNN 需要）
    active = active[active[ingredients_field].notna() & (active[ingredients_field] != "")]

    # 重設索引
    active = active.reset_index(drop=True)

    return active


def get_drug_summary(df: pd.DataFrame) -> dict:
    """取得藥品資料摘要統計

    Args:
        df: 藥品 DataFrame

    Returns:
        摘要統計字典
    """
    config = load_config()
    fm = config["field_mapping"]

    ingredients_field = fm["ingredients"]
    indication_field = fm["indication"]
    category_field = fm["category"]

    result = {
        "total_count": len(df),
        "with_ingredient": df[ingredients_field].notna().sum() if ingredients_field in df.columns else 0,
        "with_indication": df[indication_field].notna().sum() if indication_field and indication_field in df.columns else 0,
        "unique_ingredients": df[ingredients_field].nunique() if ingredients_field in df.columns else 0,
    }

    # 監管類別統計
    if category_field and category_field in df.columns:
        result["regulatory_categories"] = df[category_field].value_counts().to_dict()

    return result
