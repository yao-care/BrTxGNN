#!/usr/bin/env python3
"""生成 FHIR R4 資源

從預測結果生成 FHIR 格式的資源檔案。

使用方法:
    uv run python scripts/generate_fhir_resources.py

前置條件:
    已執行 run_kg_prediction.py

產生檔案:
    docs/fhir/metadata
    docs/fhir/MedicationKnowledge/*.json
    docs/fhir/ClinicalUseDefinition/*.json
"""

import json
from pathlib import Path
from datetime import datetime

import pandas as pd


# 巴西 BrTxGNN 設定
BASE_URL = "https://brtxgnn.yao.care"

JURISDICTION = {
    "coding": [{
        "system": "urn:iso:std:iso:3166",
        "code": "BR",
        "display": "Brazil"
    }]
}


def generate_capability_statement() -> dict:
    """生成 CapabilityStatement (metadata)"""
    return {
        "resourceType": "CapabilityStatement",
        "id": "brtxgnn-fhir-server",
        "url": f"{BASE_URL}/fhir/metadata",
        "version": "1.0.0",
        "name": "BrTxGNNFHIRServer",
        "title": "BrTxGNN FHIR Server - Reposicionamento de Medicamentos no Brasil",
        "status": "active",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "publisher": "BrTxGNN Project",
        "description": "Sistema de predição de reposicionamento de medicamentos da ANVISA - API FHIR",
        "kind": "instance",
        "fhirVersion": "4.0.1",
        "format": ["json"],
        "rest": [{
            "mode": "server",
            "resource": [
                {
                    "type": "MedicationKnowledge",
                    "interaction": [{"code": "read"}, {"code": "search-type"}],
                    "searchParam": [
                        {"name": "code", "type": "token"},
                        {"name": "status", "type": "token"}
                    ]
                },
                {
                    "type": "ClinicalUseDefinition",
                    "interaction": [{"code": "read"}, {"code": "search-type"}],
                    "searchParam": [
                        {"name": "type", "type": "token"},
                        {"name": "subject", "type": "reference"}
                    ]
                }
            ]
        }]
    }


def generate_medication_knowledge(drug_id: str, drug_name: str, evidence_level: str = "L5") -> dict:
    """生成 MedicationKnowledge 資源"""
    slug = drug_id.lower().replace(" ", "-").replace("/", "-")
    return {
        "resourceType": "MedicationKnowledge",
        "id": slug,
        "meta": {
            "profile": [f"{BASE_URL}/fhir/StructureDefinition/BrTxGNNMedicationKnowledge"]
        },
        "status": "active",
        "code": {
            "coding": [{
                "system": "https://go.drugbank.com/drugs/",
                "code": drug_id,
                "display": drug_name
            }]
        },
        "intendedJurisdiction": [JURISDICTION],
        "extension": [{
            "url": f"{BASE_URL}/fhir/StructureDefinition/evidence-level",
            "valueCode": evidence_level
        }]
    }


def generate_clinical_use_definition(
    drug_id: str,
    drug_name: str,
    indication: str,
    score: float,
    evidence_level: str = "L5"
) -> dict:
    """生成 ClinicalUseDefinition 資源"""
    drug_slug = drug_id.lower().replace(" ", "-").replace("/", "-")
    indication_slug = indication.lower().replace(" ", "-").replace("/", "-")[:50]
    resource_id = f"{drug_slug}-{indication_slug}"

    return {
        "resourceType": "ClinicalUseDefinition",
        "id": resource_id,
        "meta": {
            "profile": [f"{BASE_URL}/fhir/StructureDefinition/BrTxGNNClinicalUseDefinition"]
        },
        "type": "indication",
        "subject": [{"reference": f"MedicationKnowledge/{drug_slug}"}],
        "indication": {
            "diseaseSymptomProcedure": {
                "concept": {"text": indication}
            }
        },
        "extension": [
            {
                "url": f"{BASE_URL}/fhir/StructureDefinition/evidence-level",
                "valueCode": evidence_level
            },
            {
                "url": f"{BASE_URL}/fhir/StructureDefinition/txgnn-score",
                "valueDecimal": round(score, 4)
            },
            {
                "url": f"{BASE_URL}/fhir/StructureDefinition/prediction-source",
                "valueString": "TxGNN Knowledge Graph"
            }
        ]
    }


def main():
    print("=" * 60)
    print("BrTxGNN - 生成 FHIR R4 資源")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    fhir_dir = base_dir / "docs" / "fhir"

    # 建立目錄
    (fhir_dir / "MedicationKnowledge").mkdir(parents=True, exist_ok=True)
    (fhir_dir / "ClinicalUseDefinition").mkdir(parents=True, exist_ok=True)
    (fhir_dir / "Bundle").mkdir(parents=True, exist_ok=True)

    # 1. 生成 CapabilityStatement
    print("1. 生成 CapabilityStatement...")
    metadata = generate_capability_statement()
    with open(fhir_dir / "metadata", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    print(f"   已儲存: {fhir_dir / 'metadata'}")

    # 2. 載入預測結果
    print()
    print("2. 載入預測結果...")
    candidates_path = base_dir / "data" / "processed" / "repurposing_candidates.csv"

    if not candidates_path.exists():
        print(f"   找不到預測結果: {candidates_path}")
        print("   請先執行 run_kg_prediction.py")
        print()
        print("   已生成基本 FHIR metadata")
        return

    candidates = pd.read_csv(candidates_path)
    print(f"   載入 {len(candidates)} 筆預測")

    # 3. 生成 MedicationKnowledge
    print()
    print("3. 生成 MedicationKnowledge 資源...")

    # 取得唯一藥物 ID
    drug_col = "drugbank_id" if "drugbank_id" in candidates.columns else candidates.columns[0]
    drugs = candidates[drug_col].dropna().unique()

    med_count = 0
    for drug_id in drugs:
        drug_name = str(drug_id)
        # 嘗試取得更友善的藥物名稱
        drug_rows = candidates[candidates[drug_col] == drug_id]
        if "drug_ingredient" in drug_rows.columns:
            drug_name = drug_rows["drug_ingredient"].iloc[0] or drug_id

        evidence_level = "L5"  # 預設為模型預測
        resource = generate_medication_knowledge(str(drug_id), str(drug_name), evidence_level)

        slug = str(drug_id).lower().replace(" ", "-").replace("/", "-")
        filepath = fhir_dir / "MedicationKnowledge" / f"{slug}.json"
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(resource, f, indent=2, ensure_ascii=False)
        med_count += 1

    print(f"   生成 {med_count} 個 MedicationKnowledge 資源")

    # 4. 生成 ClinicalUseDefinition
    print()
    print("4. 生成 ClinicalUseDefinition 資源...")

    indication_col = "potential_indication" if "potential_indication" in candidates.columns else "disease_name"
    score_col = "score" if "score" in candidates.columns else None

    cud_count = 0
    for _, row in candidates.iterrows():
        drug_id = row.get(drug_col, "")
        indication = row.get(indication_col, "")
        score = row.get(score_col, 0.5) if score_col else 0.5

        if pd.isna(drug_id) or pd.isna(indication):
            continue

        drug_name = str(drug_id)
        evidence_level = "L5"

        resource = generate_clinical_use_definition(
            str(drug_id),
            drug_name,
            str(indication),
            float(score) if not pd.isna(score) else 0.5,
            evidence_level
        )

        drug_slug = str(drug_id).lower().replace(" ", "-").replace("/", "-")
        indication_slug = str(indication).lower().replace(" ", "-").replace("/", "-")[:50]
        filename = f"{drug_slug}-{indication_slug}.json"

        filepath = fhir_dir / "ClinicalUseDefinition" / filename
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(resource, f, indent=2, ensure_ascii=False)
        cud_count += 1

    print(f"   生成 {cud_count} 個 ClinicalUseDefinition 資源")

    print()
    print("=" * 60)
    print("完成！")
    print(f"FHIR 資源已儲存至: {fhir_dir}")
    print()
    print("資源統計:")
    print(f"  - CapabilityStatement: 1")
    print(f"  - MedicationKnowledge: {med_count}")
    print(f"  - ClinicalUseDefinition: {cud_count}")


if __name__ == "__main__":
    main()
