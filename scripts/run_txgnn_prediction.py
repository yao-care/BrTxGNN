#!/usr/bin/env python3
"""TxGNN 深度學習預測腳本

使用 TxGNN 預訓練模型進行藥物-疾病關係預測。
需要在 conda txgnn 環境中執行。

使用方法:
    # 啟動 conda 環境
    source ~/miniforge3/etc/profile.d/conda.sh
    source ~/miniforge3/bin/activate txgnn

    # 執行預測
    python scripts/run_txgnn_prediction.py

    # 或指定參數
    python scripts/run_txgnn_prediction.py --device cpu --min-score 0.5
"""

import sys
from pathlib import Path

# 將 src 加入 Python 路徑
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from brtxgnn.predict.txgnn_model import main

if __name__ == "__main__":
    main()
