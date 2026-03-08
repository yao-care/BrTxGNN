#!/usr/bin/env python3
"""Pipeline de validação para fluxo de reposicionamento de medicamentos BrTxGNN.

Este script valida a integridade dos dados ao longo do pipeline:
1. DrugBundle -> Evidence Pack: Garante 100% de fidelidade dos dados
2. Evidence Pack -> Notes: Garante que os marcadores de status estão corretos

Uso:
    # Validar medicamento único
    uv run python scripts/validate_data_pipeline.py --drug minoxidil

    # Validar todos os medicamentos
    uv run python scripts/validate_data_pipeline.py --all

    # Validar etapa específica
    uv run python scripts/validate_data_pipeline.py --drug aspirin --stage bundle-to-ep
"""

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class ValidationResult:
    """Resultado de uma verificação de validação."""

    stage: str
    drug: str
    passed: bool
    errors: list[str]
    warnings: list[str]


def get_data_dir() -> Path:
    """Obter o diretório de dados."""
    return Path(__file__).parent.parent / "data"


def validate_bundle_to_evidence_pack(drug_name: str) -> ValidationResult:
    """Validar que o Evidence Pack reflete corretamente os dados do Bundle.

    Verificações:
    - Contagem de indicações corresponde
    - Contagem de ensaios clínicos por indicação corresponde
    - Contagem de literatura por indicação corresponde
    - query_log tem entradas para itens do collection_log

    Args:
        drug_name: Nome do medicamento a validar

    Returns:
        ValidationResult com achados
    """
    errors = []
    warnings = []
    data_dir = get_data_dir()

    # Carregar bundle
    bundle_path = data_dir / "bundles" / drug_name / "drug_bundle.json"
    if not bundle_path.exists():
        return ValidationResult(
            stage="bundle-to-ep",
            drug=drug_name,
            passed=False,
            errors=[f"Bundle não encontrado: {bundle_path}"],
            warnings=[],
        )

    with open(bundle_path) as f:
        bundle = json.load(f)

    # Carregar evidence pack
    ep_dir = data_dir / "evidence_packs" / drug_name
    ep_files = list(ep_dir.glob("*_drug_evidence_pack.json"))
    if not ep_files:
        return ValidationResult(
            stage="bundle-to-ep",
            drug=drug_name,
            passed=False,
            errors=[f"Evidence Pack não encontrado em: {ep_dir}"],
            warnings=[],
        )

    ep_path = ep_files[0]
    with open(ep_path) as f:
        ep = json.load(f)

    # Verificar contagem de indicações
    bundle_indications = bundle.get("drug", {}).get("predicted_indications", [])
    ep_indications = ep.get("predicted_indications", [])

    if len(bundle_indications) != len(ep_indications):
        errors.append(
            f"Contagem de indicações não corresponde: Bundle={len(bundle_indications)}, EP={len(ep_indications)}"
        )

    # Verificar contagem de evidências de cada indicação
    for i, (b_ind, e_ind) in enumerate(zip(bundle_indications, ep_indications)):
        disease = b_ind.get("disease_name", f"indication_{i}")

        # Ensaios clínicos
        b_trials = [
            t for t in b_ind.get("clinical_trials", [])
            if isinstance(t, dict) and not t.get("error")
        ]
        e_trials = e_ind.get("evidence", {}).get("clinical_trials", [])

        if len(b_trials) != len(e_trials):
            errors.append(
                f"{disease}: contagem de ensaios não corresponde (Bundle={len(b_trials)}, EP={len(e_trials)})"
            )

        # Literatura
        b_lit = [
            a for a in b_ind.get("pubmed_articles", [])
            if isinstance(a, dict) and not a.get("error")
        ]
        e_lit = e_ind.get("evidence", {}).get("literature", [])

        if len(b_lit) != len(e_lit):
            errors.append(
                f"{disease}: contagem de literatura não corresponde (Bundle={len(b_lit)}, EP={len(e_lit)})"
            )

    # Verificar query_log
    collection_log = bundle.get("collection_log", [])
    query_log = ep.get("query_log", [])

    if collection_log and not query_log:
        errors.append("query_log está vazio mas collection_log tem entradas")

    if len(collection_log) != len(query_log):
        warnings.append(
            f"Contagem de log não corresponde: collection_log={len(collection_log)}, query_log={len(query_log)}"
        )

    return ValidationResult(
        stage="bundle-to-ep",
        drug=drug_name,
        passed=len(errors) == 0,
        errors=errors,
        warnings=warnings,
    )


def validate_evidence_pack_status(drug_name: str) -> ValidationResult:
    """Validar que o query_log do Evidence Pack tem valores de status corretos.

    Verificações:
    - Cada entrada do query_log tem result_status
    - result_status é um de: success, error, not_found
    - result_count está presente para status success

    Args:
        drug_name: Nome do medicamento a validar

    Returns:
        ValidationResult com achados
    """
    errors = []
    warnings = []
    data_dir = get_data_dir()

    # Carregar evidence pack
    ep_dir = data_dir / "evidence_packs" / drug_name
    ep_files = list(ep_dir.glob("*_drug_evidence_pack.json"))
    if not ep_files:
        return ValidationResult(
            stage="ep-status",
            drug=drug_name,
            passed=False,
            errors=[f"Evidence Pack não encontrado em: {ep_dir}"],
            warnings=[],
        )

    ep_path = ep_files[0]
    with open(ep_path) as f:
        ep = json.load(f)

    query_log = ep.get("query_log", [])

    if not query_log:
        warnings.append("query_log está vazio")

    valid_statuses = {"success", "error", "not_found"}

    for entry in query_log:
        source = entry.get("source", "desconhecido")
        status = entry.get("result_status")

        if not status:
            errors.append(f"{source}: falta result_status")
            continue

        if status not in valid_statuses:
            errors.append(f"{source}: status inválido '{status}' (esperado: {valid_statuses})")

        if status == "success" and "result_count" not in entry:
            warnings.append(f"{source}: status success mas sem result_count")

    return ValidationResult(
        stage="ep-status",
        drug=drug_name,
        passed=len(errors) == 0,
        errors=errors,
        warnings=warnings,
    )


def validate_notes_exist(drug_name: str) -> ValidationResult:
    """Validar que os arquivos Notes existem e não estão vazios.

    Args:
        drug_name: Nome do medicamento a validar

    Returns:
        ValidationResult com achados
    """
    errors = []
    warnings = []
    data_dir = get_data_dir()

    notes_dir = data_dir / "notes" / drug_name

    if not notes_dir.exists():
        return ValidationResult(
            stage="notes-exist",
            drug=drug_name,
            passed=False,
            errors=[f"Diretório de notas não encontrado: {notes_dir}"],
            warnings=[],
        )

    pharmacist_notes = notes_dir / "drug_pharmacist_notes.md"
    sponsor_notes = notes_dir / "drug_sponsor_notes.md"

    for notes_path, name in [
        (pharmacist_notes, "Notas do Farmacêutico"),
        (sponsor_notes, "Notas do Patrocinador"),
    ]:
        if not notes_path.exists():
            errors.append(f"{name} não encontrado: {notes_path}")
        elif notes_path.stat().st_size < 100:
            errors.append(f"{name} é muito pequeno ({notes_path.stat().st_size} bytes)")
        elif notes_path.stat().st_size < 1000:
            warnings.append(f"{name} é incomumente pequeno ({notes_path.stat().st_size} bytes)")

    return ValidationResult(
        stage="notes-exist",
        drug=drug_name,
        passed=len(errors) == 0,
        errors=errors,
        warnings=warnings,
    )


def validate_drug(drug_name: str, stages: list[str] | None = None) -> list[ValidationResult]:
    """Executar todas as verificações de validação para um único medicamento.

    Args:
        drug_name: Nome do medicamento a validar
        stages: Lista opcional de etapas a validar. Se None, valida todas as etapas.

    Returns:
        Lista de ValidationResults
    """
    all_stages = {
        "bundle-to-ep": validate_bundle_to_evidence_pack,
        "ep-status": validate_evidence_pack_status,
        "notes-exist": validate_notes_exist,
    }

    if stages is None:
        stages = list(all_stages.keys())

    results = []
    for stage in stages:
        if stage in all_stages:
            result = all_stages[stage](drug_name)
            results.append(result)

    return results


def validate_all_drugs(stages: list[str] | None = None) -> dict[str, list[ValidationResult]]:
    """Validar todos os medicamentos no diretório de dados.

    Args:
        stages: Lista opcional de etapas a validar

    Returns:
        Dict mapeando nome do medicamento para lista de ValidationResults
    """
    data_dir = get_data_dir()
    results = {}

    # Encontrar todos os medicamentos (de bundles, evidence_packs ou notes)
    drugs = set()

    bundles_dir = data_dir / "bundles"
    if bundles_dir.exists():
        for d in bundles_dir.iterdir():
            if d.is_dir():
                drugs.add(d.name)

    ep_dir = data_dir / "evidence_packs"
    if ep_dir.exists():
        for d in ep_dir.iterdir():
            if d.is_dir():
                drugs.add(d.name)

    notes_dir = data_dir / "notes"
    if notes_dir.exists():
        for d in notes_dir.iterdir():
            if d.is_dir():
                drugs.add(d.name)

    for drug in sorted(drugs):
        results[drug] = validate_drug(drug, stages)

    return results


def print_result(result: ValidationResult, verbose: bool = False) -> None:
    """Imprimir um resultado de validação."""
    status = "✅ PASSOU" if result.passed else "❌ FALHOU"
    print(f"  [{result.stage}] {status}")

    if result.errors:
        for error in result.errors:
            print(f"    ❌ {error}")

    if verbose and result.warnings:
        for warning in result.warnings:
            print(f"    ⚠️  {warning}")


def main():
    parser = argparse.ArgumentParser(
        description="Validar integridade do pipeline de dados BrTxGNN"
    )
    parser.add_argument(
        "--drug",
        type=str,
        help="Nome do medicamento a validar",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Validar todos os medicamentos",
    )
    parser.add_argument(
        "--stage",
        type=str,
        choices=["bundle-to-ep", "ep-status", "notes-exist"],
        help="Validar apenas etapa específica",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Mostrar avisos além de erros",
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Mostrar apenas resumo",
    )

    args = parser.parse_args()

    if not args.drug and not args.all:
        parser.error("Por favor especifique --drug ou --all")

    stages = [args.stage] if args.stage else None

    if args.drug:
        print(f"\n{'=' * 60}")
        print(f"Validando: {args.drug}")
        print(f"{'=' * 60}")

        results = validate_drug(args.drug, stages)

        all_passed = True
        for result in results:
            print_result(result, args.verbose)
            if not result.passed:
                all_passed = False

        sys.exit(0 if all_passed else 1)

    elif args.all:
        print(f"\n{'=' * 60}")
        print("Validando todos os medicamentos")
        print(f"{'=' * 60}")

        all_results = validate_all_drugs(stages)

        total_passed = 0
        total_failed = 0
        failed_drugs = []

        for drug, results in all_results.items():
            drug_passed = all(r.passed for r in results)

            if args.summary:
                status = "✅" if drug_passed else "❌"
                print(f"  {status} {drug}")
            else:
                print(f"\n{drug}:")
                for result in results:
                    print_result(result, args.verbose)

            if drug_passed:
                total_passed += 1
            else:
                total_failed += 1
                failed_drugs.append(drug)

        print(f"\n{'=' * 60}")
        print(f"Resumo: {total_passed} passaram, {total_failed} falharam")

        if failed_drugs:
            print(f"\nMedicamentos que falharam: {', '.join(failed_drugs)}")

        sys.exit(0 if total_failed == 0 else 1)


if __name__ == "__main__":
    main()
