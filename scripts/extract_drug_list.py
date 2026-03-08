#!/usr/bin/env python3
"""
Extrair lista de medicamentos para verificação de evidências.

Gera um arquivo JSON com a lista de medicamentos para os scripts de verificação
de evidências (check_clinicaltrials.py, check_pubmed.py, etc.).
"""

import json
from datetime import date
from pathlib import Path

# Caminhos
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
BUNDLES_DIR = PROJECT_ROOT / "data" / "bundles"
SEARCH_INDEX_FILE = PROJECT_ROOT / "docs" / "data" / "search-index.json"
OUTPUT_FILE = SCRIPT_DIR / "drug_list.json"


def extract_from_bundles() -> list:
    """Extrair lista de medicamentos dos bundles."""
    drugs = []

    if not BUNDLES_DIR.exists():
        print(f"Diretório de bundles não encontrado: {BUNDLES_DIR}")
        return drugs

    for drug_dir in BUNDLES_DIR.iterdir():
        if not drug_dir.is_dir():
            continue

        bundle_file = drug_dir / "drug_bundle.json"
        if not bundle_file.exists():
            continue

        try:
            with open(bundle_file, "r", encoding="utf-8") as f:
                bundle = json.load(f)

            drug_data = bundle.get("drug", {})
            drug_name = drug_data.get("inn", drug_dir.name.replace("_", " ").title())

            drugs.append({
                "name": drug_name,
                "slug": drug_dir.name
            })
        except Exception as e:
            print(f"Erro ao carregar {bundle_file}: {e}")

    return drugs


def extract_from_search_index() -> list:
    """Extrair lista de medicamentos do índice de pesquisa."""
    drugs = []

    if not SEARCH_INDEX_FILE.exists():
        print(f"Índice de pesquisa não encontrado: {SEARCH_INDEX_FILE}")
        return drugs

    try:
        with open(SEARCH_INDEX_FILE, "r", encoding="utf-8") as f:
            index = json.load(f)

        for drug in index.get("drugs", []):
            drugs.append({
                "name": drug.get("name", ""),
                "slug": drug.get("slug", "")
            })
    except Exception as e:
        print(f"Erro ao carregar índice de pesquisa: {e}")

    return drugs


def main():
    print("=" * 60)
    print("Extraindo Lista de Medicamentos")
    print("=" * 60)

    # Tentar extrair dos bundles primeiro
    drugs = extract_from_bundles()

    if not drugs:
        # Se não houver bundles, tentar o índice de pesquisa
        print("Nenhum bundle encontrado, tentando índice de pesquisa...")
        drugs = extract_from_search_index()

    if not drugs:
        print("Nenhum medicamento encontrado.")
        print("\nPara gerar a lista de medicamentos, primeiro execute as previsões:")
        print("  uv run python scripts/run_kg_prediction.py")
        return

    # Remover duplicatas e ordenar
    seen = set()
    unique_drugs = []
    for drug in drugs:
        if drug["name"] not in seen:
            seen.add(drug["name"])
            unique_drugs.append(drug)

    unique_drugs.sort(key=lambda x: x["name"])

    # Criar saída
    output = {
        "generated": date.today().isoformat(),
        "count": len(unique_drugs),
        "drugs": unique_drugs
    }

    # Salvar
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"Extraídos {len(unique_drugs)} medicamentos")
    print(f"Saída: {OUTPUT_FILE}")

    # Mostrar amostra
    print("\nAmostra de medicamentos:")
    for drug in unique_drugs[:10]:
        print(f"  - {drug['name']}")
    if len(unique_drugs) > 10:
        print(f"  ... e mais {len(unique_drugs) - 10} medicamentos")


if __name__ == "__main__":
    main()
