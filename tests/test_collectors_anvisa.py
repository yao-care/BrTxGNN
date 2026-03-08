"""Tests for ANVISA collector."""

import json
import pytest
from pathlib import Path

from brtxgnn.collectors.anvisa import ANVISACollector


@pytest.fixture
def sample_anvisa_data():
    """Sample ANVISA drug records."""
    return [
        {
            "TIPO_PRODUTO": "MEDICAMENTO",
            "NOME_PRODUTO": "WARFARINA SÓDICA",
            "DATA_FINALIZACAO_PROCESSO": "01/01/2020",
            "CATEGORIA_REGULATORIA": "Genérico",
            "NUMERO_REGISTRO_PRODUTO": "100000001",
            "DATA_VENCIMENTO_REGISTRO": "01/2025",
            "NUMERO_PROCESSO": "25351000000001",
            "CLASSE_TERAPEUTICA": "ANTICOAGULANTES",
            "EMPRESA_DETENTORA_REGISTRO": "12345678000100 - LABORATÓRIO TESTE LTDA",
            "SITUACAO_REGISTRO": "Ativo",
            "PRINCIPIO_ATIVO": "VARFARINA SÓDICA",
        },
        {
            "TIPO_PRODUTO": "MEDICAMENTO",
            "NOME_PRODUTO": "ÁCIDO ACETILSALICÍLICO",
            "DATA_FINALIZACAO_PROCESSO": "01/01/2019",
            "CATEGORIA_REGULATORIA": "Similar",
            "NUMERO_REGISTRO_PRODUTO": "100000002",
            "DATA_VENCIMENTO_REGISTRO": "01/2024",
            "NUMERO_PROCESSO": "25351000000002",
            "CLASSE_TERAPEUTICA": "ANALGESICOS E ANTIPIRETICOS",
            "EMPRESA_DETENTORA_REGISTRO": "98765432000100 - OUTRO LABORATÓRIO LTDA",
            "SITUACAO_REGISTRO": "Ativo",
            "PRINCIPIO_ATIVO": "ÁCIDO ACETILSALICÍLICO",
        },
        {
            "TIPO_PRODUTO": "MEDICAMENTO",
            "NOME_PRODUTO": "WARFARINA MARCA B",
            "DATA_FINALIZACAO_PROCESSO": "01/01/2021",
            "CATEGORIA_REGULATORIA": "Novo",
            "NUMERO_REGISTRO_PRODUTO": "100000003",
            "DATA_VENCIMENTO_REGISTRO": "01/2026",
            "NUMERO_PROCESSO": "25351000000003",
            "CLASSE_TERAPEUTICA": "ANTICOAGULANTES",
            "EMPRESA_DETENTORA_REGISTRO": "11111111000100 - TERCEIRO LABORATÓRIO LTDA",
            "SITUACAO_REGISTRO": "Inativo",
            "PRINCIPIO_ATIVO": "VARFARINA SÓDICA",
        },
    ]


@pytest.fixture
def anvisa_data_file(tmp_path, sample_anvisa_data):
    """Create temporary ANVISA data file."""
    data_file = tmp_path / "br_fda_drugs.json"
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(sample_anvisa_data, f, ensure_ascii=False)
    return data_file


class TestANVISACollector:
    """Tests for ANVISACollector class."""

    def test_source_name(self, anvisa_data_file):
        """Should have correct source name."""
        collector = ANVISACollector(data_path=anvisa_data_file)
        assert collector.source_name == "anvisa"

    def test_search_by_product_name(self, anvisa_data_file):
        """Should find drugs by product name."""
        collector = ANVISACollector(data_path=anvisa_data_file)
        result = collector.search("warfarina")

        assert result.success is True
        assert result.data["found"] is True
        assert len(result.data["records"]) == 2  # Two warfarin products

    def test_search_by_ingredient(self, anvisa_data_file):
        """Should find drugs by active ingredient."""
        collector = ANVISACollector(data_path=anvisa_data_file)
        result = collector.search("ACETILSALICÍLICO")

        assert result.success is True
        assert result.data["found"] is True
        assert len(result.data["records"]) == 1

    def test_search_case_insensitive(self, anvisa_data_file):
        """Should search case insensitively."""
        collector = ANVISACollector(data_path=anvisa_data_file)

        # Lowercase
        result1 = collector.search("warfarina")
        # Uppercase
        result2 = collector.search("WARFARINA")
        # Mixed case
        result3 = collector.search("Warfarina")

        assert result1.data["found"] == result2.data["found"] == result3.data["found"]
        assert (
            len(result1.data["records"])
            == len(result2.data["records"])
            == len(result3.data["records"])
        )

    def test_search_not_found(self, anvisa_data_file):
        """Should return found=False for unknown drug."""
        collector = ANVISACollector(data_path=anvisa_data_file)
        result = collector.search("unknown_drug_xyz")

        assert result.success is True
        assert result.data["found"] is False
        assert result.data["records"] == []

    def test_search_with_therapeutic_class_filter(self, anvisa_data_file):
        """Should filter by therapeutic class."""
        collector = ANVISACollector(data_path=anvisa_data_file)
        result = collector.search("warfarina", disease="ANTICOAGULANTES")

        assert result.success is True
        assert result.data["found"] is True
        assert len(result.data["records"]) == 2
        assert "ANTICOAGULANTES" in result.data["records"][0]["therapeutic_class"]

    def test_search_filter_no_match_returns_all(self, anvisa_data_file):
        """Should return all drug matches if filter has no matches."""
        collector = ANVISACollector(data_path=anvisa_data_file)
        result = collector.search("warfarina", disease="CLASSE INEXISTENTE")

        assert result.success is True
        assert result.data["found"] is True
        assert len(result.data["records"]) == 2  # Returns all warfarin matches

    def test_record_fields(self, anvisa_data_file):
        """Should return properly formatted records."""
        collector = ANVISACollector(data_path=anvisa_data_file)
        result = collector.search("acetilsalicílico")

        record = result.data["records"][0]
        assert "registration_number" in record
        assert "product_name" in record
        assert "active_ingredient" in record
        assert "therapeutic_class" in record
        assert "regulatory_category" in record
        assert "product_type" in record
        assert "company" in record
        assert "registration_status" in record
        assert "process_number" in record
        assert "expiration_date" in record
        assert "finalization_date" in record

    def test_record_values(self, anvisa_data_file):
        """Should extract correct field values."""
        collector = ANVISACollector(data_path=anvisa_data_file)
        result = collector.search("acetilsalicílico")

        record = result.data["records"][0]
        assert record["registration_number"] == "100000002"
        assert record["product_name"] == "ÁCIDO ACETILSALICÍLICO"
        assert record["active_ingredient"] == "ÁCIDO ACETILSALICÍLICO"
        assert record["therapeutic_class"] == "ANALGESICOS E ANTIPIRETICOS"

    def test_total_matches_count(self, anvisa_data_file):
        """Should include total matches count."""
        collector = ANVISACollector(data_path=anvisa_data_file)
        result = collector.search("warfarina")

        assert result.data["total_matches"] == 2

    def test_summary_info(self, anvisa_data_file):
        """Should include summary information."""
        collector = ANVISACollector(data_path=anvisa_data_file)
        result = collector.search("warfarina")

        assert "summary" in result.data
        summary = result.data["summary"]
        assert "therapeutic_class" in summary
        assert "regulatory_category" in summary
        assert "active_status_count" in summary
        assert "inactive_status_count" in summary
        assert summary["active_status_count"] == 1
        assert summary["inactive_status_count"] == 1

    def test_limits_records_to_20(self, tmp_path):
        """Should limit records to 20."""
        # Create data with more than 20 records
        data = [
            {
                "TIPO_PRODUTO": "MEDICAMENTO",
                "NOME_PRODUTO": f"TESTE MEDICAMENTO {i}",
                "NUMERO_REGISTRO_PRODUTO": f"{100000000 + i}",
                "PRINCIPIO_ATIVO": "INGREDIENTE TESTE",
                "CLASSE_TERAPEUTICA": "CLASSE TESTE",
                "SITUACAO_REGISTRO": "Ativo",
            }
            for i in range(30)
        ]
        data_file = tmp_path / "many_drugs.json"
        with open(data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

        collector = ANVISACollector(data_path=data_file)
        result = collector.search("TESTE")

        assert len(result.data["records"]) == 20
        assert result.data["total_matches"] == 30

    def test_get_by_registration_number(self, anvisa_data_file):
        """Should get record by registration number."""
        collector = ANVISACollector(data_path=anvisa_data_file)
        record = collector.get_by_registration_number("100000002")

        assert record is not None
        assert record["NOME_PRODUTO"] == "ÁCIDO ACETILSALICÍLICO"

    def test_get_by_registration_number_not_found(self, anvisa_data_file):
        """Should return None for unknown registration number."""
        collector = ANVISACollector(data_path=anvisa_data_file)
        record = collector.get_by_registration_number("999999999")

        assert record is None

    def test_get_active_drugs(self, anvisa_data_file):
        """Should get only active drugs."""
        collector = ANVISACollector(data_path=anvisa_data_file)
        active_drugs = collector.get_active_drugs()

        assert len(active_drugs) == 2
        for drug in active_drugs:
            assert drug["SITUACAO_REGISTRO"] == "Ativo"

    def test_get_by_therapeutic_class(self, anvisa_data_file):
        """Should get drugs by therapeutic class."""
        collector = ANVISACollector(data_path=anvisa_data_file)
        anticoagulants = collector.get_by_therapeutic_class("ANTICOAGULANTES")

        assert len(anticoagulants) == 2
        for drug in anticoagulants:
            assert "ANTICOAGULANTES" in drug["CLASSE_TERAPEUTICA"]

    def test_get_statistics(self, anvisa_data_file):
        """Should return statistics."""
        collector = ANVISACollector(data_path=anvisa_data_file)
        stats = collector.get_statistics()

        assert stats["total"] == 3
        assert "by_status" in stats
        assert "by_category" in stats
        assert "by_therapeutic_class" in stats
        assert stats["by_status"]["Ativo"] == 2
        assert stats["by_status"]["Inativo"] == 1

    def test_caching(self, anvisa_data_file):
        """Should cache loaded data."""
        collector = ANVISACollector(data_path=anvisa_data_file)

        # First search loads data
        collector.search("warfarina")
        assert collector._data is not None

        # Second search uses cached data
        cached_data = collector._data
        collector.search("acetilsalicílico")
        assert collector._data is cached_data

    def test_missing_data_file(self, tmp_path):
        """Should handle missing data file gracefully."""
        collector = ANVISACollector(data_path=tmp_path / "nonexistent.json")
        result = collector.search("warfarina")

        assert result.success is True
        assert result.data["found"] is False
        assert result.data["records"] == []

    def test_query_in_result(self, anvisa_data_file):
        """Should include query in result."""
        collector = ANVISACollector(data_path=anvisa_data_file)
        result = collector.search("warfarina", disease="anticoagulantes")

        assert result.query == {"drug": "warfarina", "disease": "anticoagulantes"}

    def test_search_by_therapeutic_class(self, anvisa_data_file):
        """Should find drugs by therapeutic class."""
        collector = ANVISACollector(data_path=anvisa_data_file)
        result = collector.search("ANTICOAGULANTES")

        assert result.success is True
        assert result.data["found"] is True

    def test_handles_empty_fields(self, tmp_path):
        """Should handle records with empty fields."""
        data = [
            {
                "TIPO_PRODUTO": "MEDICAMENTO",
                "NOME_PRODUTO": "Test Drug",
                "NUMERO_REGISTRO_PRODUTO": "TEST001",
                "PRINCIPIO_ATIVO": "",
                "CLASSE_TERAPEUTICA": "",
                "SITUACAO_REGISTRO": "Ativo",
            }
        ]
        data_file = tmp_path / "sparse.json"
        with open(data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

        collector = ANVISACollector(data_path=data_file)
        result = collector.search("Test Drug")

        assert result.success is True
        assert result.data["found"] is True

    def test_default_data_path(self):
        """Should use default data path."""
        collector = ANVISACollector()
        expected_suffix = Path("data") / "raw" / "br_fda_drugs.json"
        assert collector.data_path.parts[-3:] == expected_suffix.parts

    def test_handles_json_error(self, tmp_path):
        """Should handle invalid JSON file."""
        data_file = tmp_path / "invalid.json"
        with open(data_file, "w") as f:
            f.write("invalid json content")

        collector = ANVISACollector(data_path=data_file)
        result = collector.search("test")

        assert result.success is False
        assert result.data["found"] is False
        assert result.error_message is not None
