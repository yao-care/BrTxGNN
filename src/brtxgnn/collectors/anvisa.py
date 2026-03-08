"""ANVISA collector - fetches Brazil ANVISA drug data."""

import json
from pathlib import Path
from typing import Any

from .base import BaseCollector, CollectorResult


class ANVISACollector(BaseCollector):
    """Collector for Brazil ANVISA drug data.

    Reads from local br_fda_drugs.json file that was processed
    from the ANVISA open data.
    """

    source_name = "anvisa"

    def __init__(self, data_path: str | Path | None = None):
        """Initialize the collector.

        Args:
            data_path: Path to br_fda_drugs.json file.
                      Defaults to data/raw/br_fda_drugs.json
        """
        if data_path is None:
            self.data_path = (
                Path(__file__).parent.parent.parent.parent
                / "data"
                / "raw"
                / "br_fda_drugs.json"
            )
        else:
            self.data_path = Path(data_path)

        self._data: list[dict] | None = None

    def _load_data(self) -> list[dict]:
        """Load ANVISA data from JSON file."""
        if self._data is not None:
            return self._data

        if not self.data_path.exists():
            self._data = []
            return self._data

        with open(self.data_path, "r", encoding="utf-8") as f:
            self._data = json.load(f)

        return self._data

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        """Search for ANVISA records matching a drug name.

        Args:
            drug: Drug name (INN, brand name, or active ingredient)
            disease: Therapeutic class (used for filtering if provided)

        Returns:
            CollectorResult with ANVISA data
        """
        query = {"drug": drug, "disease": disease}

        try:
            data = self._load_data()

            # Search for matching records
            matches = self._find_matches(drug, data)

            # If disease/therapeutic class is provided, further filter
            if disease and matches:
                matches = self._filter_by_therapeutic_class(matches, disease)

            # Format the result
            result = self._format_result(matches)

            return self._make_result(
                query=query,
                data=result,
                success=True,
            )

        except Exception as e:
            return self._make_result(
                query=query,
                data={"found": False, "records": []},
                success=False,
                error_message=str(e),
            )

    def _find_matches(self, drug: str, data: list[dict]) -> list[dict]:
        """Find records matching the drug name.

        Args:
            drug: Drug name to search for
            data: List of ANVISA records

        Returns:
            List of matching records
        """
        drug_lower = drug.lower()
        matches = []

        for record in data:
            # Check various name fields
            fields_to_check = [
                record.get("NOME_PRODUTO", ""),
                record.get("PRINCIPIO_ATIVO", ""),
                record.get("CLASSE_TERAPEUTICA", ""),
            ]

            for field in fields_to_check:
                if field and drug_lower in field.lower():
                    matches.append(record)
                    break

        return matches

    def _filter_by_therapeutic_class(
        self, records: list[dict], therapeutic_class: str
    ) -> list[dict]:
        """Filter records by therapeutic class.

        Args:
            records: List of ANVISA records
            therapeutic_class: Therapeutic class to filter by

        Returns:
            Filtered list of records
        """
        class_lower = therapeutic_class.lower()
        filtered = []

        for record in records:
            classe = record.get("CLASSE_TERAPEUTICA", "").lower()
            if class_lower in classe:
                filtered.append(record)

        # If no matches with class filter, return original
        return filtered if filtered else records

    def _format_result(self, records: list[dict]) -> dict:
        """Format the result for the bundle.

        Args:
            records: List of matching ANVISA records

        Returns:
            Formatted result dictionary
        """
        if not records:
            return {"found": False, "records": []}

        formatted_records = []
        for record in records[:20]:  # Limit to 20 records
            formatted = {
                "registration_number": record.get("NUMERO_REGISTRO_PRODUTO", ""),
                "product_name": record.get("NOME_PRODUTO", ""),
                "active_ingredient": record.get("PRINCIPIO_ATIVO", ""),
                "therapeutic_class": record.get("CLASSE_TERAPEUTICA", ""),
                "regulatory_category": record.get("CATEGORIA_REGULATORIA", ""),
                "product_type": record.get("TIPO_PRODUTO", ""),
                "company": record.get("EMPRESA_DETENTORA_REGISTRO", ""),
                "registration_status": record.get("SITUACAO_REGISTRO", ""),
                "process_number": record.get("NUMERO_PROCESSO", ""),
                "expiration_date": record.get("DATA_VENCIMENTO_REGISTRO", ""),
                "finalization_date": record.get("DATA_FINALIZACAO_PROCESSO", ""),
            }
            formatted_records.append(formatted)

        # Create summary from first record
        first_record = records[0]
        summary = {
            "therapeutic_class": first_record.get("CLASSE_TERAPEUTICA", ""),
            "regulatory_category": first_record.get("CATEGORIA_REGULATORIA", ""),
            "active_status_count": sum(
                1 for r in records if r.get("SITUACAO_REGISTRO") == "Ativo"
            ),
            "inactive_status_count": sum(
                1 for r in records if r.get("SITUACAO_REGISTRO") == "Inativo"
            ),
        }

        return {
            "found": True,
            "records": formatted_records,
            "total_matches": len(records),
            "summary": summary,
        }

    def get_by_registration_number(self, registration_number: str) -> dict | None:
        """Get a specific record by registration number.

        Args:
            registration_number: ANVISA registration number

        Returns:
            Record dictionary or None if not found
        """
        data = self._load_data()

        for record in data:
            if record.get("NUMERO_REGISTRO_PRODUTO") == registration_number:
                return record

        return None

    def get_active_drugs(self) -> list[dict]:
        """Get all active drugs.

        Returns:
            List of active drug records
        """
        data = self._load_data()
        return [r for r in data if r.get("SITUACAO_REGISTRO") == "Ativo"]

    def get_by_therapeutic_class(self, therapeutic_class: str) -> list[dict]:
        """Get all drugs in a therapeutic class.

        Args:
            therapeutic_class: Therapeutic class name

        Returns:
            List of matching records
        """
        data = self._load_data()
        class_lower = therapeutic_class.lower()
        return [
            r for r in data
            if class_lower in r.get("CLASSE_TERAPEUTICA", "").lower()
        ]

    def get_statistics(self) -> dict:
        """Get statistics about the ANVISA data.

        Returns:
            Dictionary with statistics
        """
        data = self._load_data()

        if not data:
            return {"total": 0}

        status_counts = {}
        category_counts = {}
        class_counts = {}

        for record in data:
            # Status counts
            status = record.get("SITUACAO_REGISTRO", "Unknown")
            status_counts[status] = status_counts.get(status, 0) + 1

            # Category counts
            category = record.get("CATEGORIA_REGULATORIA", "Unknown")
            if category:
                category_counts[category] = category_counts.get(category, 0) + 1

            # Therapeutic class counts
            classe = record.get("CLASSE_TERAPEUTICA", "")
            if classe:
                class_counts[classe] = class_counts.get(classe, 0) + 1

        return {
            "total": len(data),
            "by_status": status_counts,
            "by_category": dict(
                sorted(category_counts.items(), key=lambda x: -x[1])[:20]
            ),
            "by_therapeutic_class": dict(
                sorted(class_counts.items(), key=lambda x: -x[1])[:20]
            ),
        }
