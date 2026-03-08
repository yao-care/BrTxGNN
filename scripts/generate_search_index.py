#!/usr/bin/env python3
"""
Gerar índice de pesquisa unificado para funcionalidade de busca de medicamentos.

Este script cria um arquivo JSON de índice que suporta:
1. Busca por nome de medicamento (DrugBank + nomes comerciais ANVISA)
2. Busca por indicação/doença
3. Busca bidirecional (medicamento → indicações, indicação → medicamentos)
"""

import json
import re
from pathlib import Path
from collections import defaultdict
from datetime import date

# Caminhos
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
BUNDLES_DIR = PROJECT_ROOT / "data" / "bundles"
OUTPUT_FILE = PROJECT_ROOT / "docs" / "data" / "search-index.json"


def calculate_evidence_level(indication: dict) -> str:
    """Calcular nível de evidência com base em ensaios clínicos e artigos."""
    trials = indication.get("clinical_trials", [])
    articles = indication.get("pubmed_articles", [])

    phase3_4_count = 0
    phase2_count = 0
    phase1_count = 0

    for trial in trials:
        phase = trial.get("phase", "").upper()
        if "PHASE3" in phase or "PHASE4" in phase or "PHASE 3" in phase or "PHASE 4" in phase:
            phase3_4_count += 1
        elif "PHASE2" in phase or "PHASE 2" in phase:
            phase2_count += 1
        elif "PHASE1" in phase or "PHASE 1" in phase:
            phase1_count += 1

    total_articles = len(articles)

    if phase3_4_count >= 2:
        return "L1"
    elif phase3_4_count >= 1 or phase2_count >= 2:
        return "L2"
    elif phase2_count >= 1 or phase1_count >= 1 or len(trials) >= 1:
        return "L3"
    elif total_articles >= 1:
        return "L4"
    else:
        return "L5"


def extract_brand_names(bundle: dict) -> list:
    """Extrair nomes comerciais dos dados da ANVISA."""
    brand_names = set()

    anvisa = bundle.get("anvisa", {})
    records = anvisa.get("records", [])

    for record in records:
        name = record.get("product_name", "")
        if name:
            # Extrair nome principal (antes de números ou dosagens)
            match = re.match(r"^([A-Za-zÀ-ÿ\s]+)", name)
            if match:
                brand = match.group(1).strip()
                if brand and len(brand) >= 3:
                    brand_names.add(brand)

    return list(brand_names)[:5]  # Limitar a 5 nomes comerciais


def get_original_indication(bundle: dict) -> str:
    """Obter indicação original do bundle."""
    drug = bundle.get("drug", {})
    original = drug.get("original_indications", [])
    if original:
        return original[0][:50] + "..." if len(original[0]) > 50 else original[0]
    return ""


def load_all_bundles() -> list:
    """Carregar todos os bundles de medicamentos."""
    bundles = []

    if not BUNDLES_DIR.exists():
        print(f"Diretório de bundles não encontrado: {BUNDLES_DIR}")
        return bundles

    for drug_dir in BUNDLES_DIR.iterdir():
        if not drug_dir.is_dir():
            continue

        bundle_file = drug_dir / "drug_bundle.json"
        if not bundle_file.exists():
            continue

        try:
            with open(bundle_file, "r", encoding="utf-8") as f:
                bundle = json.load(f)
                bundle["_slug"] = drug_dir.name
                bundles.append(bundle)
        except Exception as e:
            print(f"Erro ao carregar {bundle_file}: {e}")

    return bundles


def build_search_index(bundles: list) -> dict:
    """Construir o índice de pesquisa a partir de todos os bundles."""
    drugs = []
    indication_map = defaultdict(list)  # indicação -> lista de medicamentos

    level_order = {"L1": 1, "L2": 2, "L3": 3, "L4": 4, "L5": 5}

    for bundle in bundles:
        drug_data = bundle.get("drug", {})
        slug = bundle.get("_slug", "")
        name = drug_data.get("inn", slug.replace("_", " ").title())

        # Obter nomes comerciais
        brand_names = extract_brand_names(bundle)

        # Obter indicação original
        original_indication = get_original_indication(bundle)

        # Obter indicações previstas
        predicted = drug_data.get("predicted_indications", [])
        indications = []
        best_level = "L5"

        for ind in predicted:
            ind_name = ind.get("disease_name", "")
            score = ind.get("txgnn_score", 0)
            level = calculate_evidence_level(ind)

            indications.append({
                "name": ind_name,
                "score": round(score * 100, 2),
                "level": level
            })

            # Rastrear melhor nível de evidência
            if level_order.get(level, 5) < level_order.get(best_level, 5):
                best_level = level

            # Adicionar ao mapa de indicações para busca reversa
            indication_map[ind_name].append({
                "name": name,
                "slug": slug,
                "score": round(score * 100, 2),
                "level": level,
                "original": original_indication
            })

        drugs.append({
            "name": name,
            "slug": slug,
            "brands": brand_names,
            "original": original_indication,
            "level": best_level,
            "indications": indications
        })

    # Construir índice de indicações
    indications = []
    for ind_name, ind_drugs in indication_map.items():
        # Ordenar medicamentos por nível de evidência, depois por score
        sorted_drugs = sorted(
            ind_drugs,
            key=lambda x: (level_order.get(x["level"], 5), -x["score"])
        )

        best_level = sorted_drugs[0]["level"] if sorted_drugs else "L5"

        indications.append({
            "name": ind_name,
            "count": len(sorted_drugs),
            "level": best_level,
            "drugs": sorted_drugs
        })

    # Ordenar indicações por contagem de medicamentos (decrescente)
    indications.sort(key=lambda x: -x["count"])

    return {
        "generated": date.today().isoformat(),
        "drug_count": len(drugs),
        "indication_count": len(indications),
        "drugs": drugs,
        "indications": indications
    }


def main():
    print("=" * 60)
    print("Gerando Índice de Pesquisa")
    print("=" * 60)

    # Carregar todos os bundles
    bundles = load_all_bundles()
    print(f"Carregados {len(bundles)} bundles de medicamentos")

    # Construir índice de pesquisa
    index = build_search_index(bundles)
    print(f"Índice construído com {index['drug_count']} medicamentos e {index['indication_count']} indicações")

    # Garantir que o diretório de saída existe
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Escrever saída
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    print(f"Saída gravada em: {OUTPUT_FILE}")

    # Mostrar dados de exemplo
    if index["drugs"]:
        print("\nMedicamentos de exemplo:")
        for drug in index["drugs"][:3]:
            print(f"  - {drug['name']} ({drug['level']}): {len(drug['indications'])} indicações")
            if drug['brands']:
                print(f"    Marcas: {', '.join(drug['brands'])}")

    if index["indications"]:
        print("\nIndicações de exemplo:")
        for ind in index["indications"][:3]:
            print(f"  - {ind['name']} ({ind['level']}): {ind['count']} medicamentos")


if __name__ == "__main__":
    main()
