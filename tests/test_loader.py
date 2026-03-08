"""Testes para o módulo de carregamento de dados ANVISA"""

import pytest
from pathlib import Path

from brtxgnn.data.loader import load_fda_drugs, filter_active_drugs, get_drug_summary


class TestLoadFdaDrugs:
    """Testes para a função load_fda_drugs"""

    def test_load_returns_dataframe(self):
        """Deve retornar um DataFrame"""
        df = load_fda_drugs()
        assert hasattr(df, "columns")
        assert len(df) > 0

    def test_load_has_required_columns(self):
        """Deve conter as colunas obrigatórias do ANVISA"""
        df = load_fda_drugs()
        required_columns = [
            "NUMERO_REGISTRO_PRODUTO",
            "NOME_PRODUTO",
            "PRINCIPIO_ATIVO",
            "CLASSE_TERAPEUTICA",
            "SITUACAO_REGISTRO",
        ]
        for col in required_columns:
            assert col in df.columns, f"Coluna faltando: {col}"

    def test_load_total_count(self):
        """Deve conter aproximadamente 40.000+ medicamentos"""
        df = load_fda_drugs()
        assert len(df) > 40000, f"Esperado >40000 registros, encontrado {len(df)}"


class TestFilterActiveDrugs:
    """Testes para a função filter_active_drugs"""

    def test_filter_removes_inactive(self):
        """Deve filtrar medicamentos inativos"""
        df = load_fda_drugs()
        active = filter_active_drugs(df)

        # Verifica que não há medicamentos inativos
        assert (active["SITUACAO_REGISTRO"] == "Ativo").all()

    def test_filter_removes_empty_ingredients(self):
        """Deve filtrar medicamentos sem princípio ativo"""
        df = load_fda_drugs()
        active = filter_active_drugs(df)

        # Verifica que todos têm princípio ativo
        assert active["PRINCIPIO_ATIVO"].notna().all()
        assert (active["PRINCIPIO_ATIVO"] != "").all()

    def test_filter_count_reasonable(self):
        """O número de medicamentos ativos deve ser razoável (~10.000+)"""
        df = load_fda_drugs()
        active = filter_active_drugs(df)

        # ANVISA tem aproximadamente 10.000 medicamentos ativos com princípio ativo
        assert len(active) > 8000
        assert len(active) < 30000


class TestGetDrugSummary:
    """Testes para a função get_drug_summary"""

    def test_summary_has_keys(self):
        """O resumo deve conter as chaves necessárias"""
        df = load_fda_drugs()
        active = filter_active_drugs(df)
        summary = get_drug_summary(active)

        assert "total_count" in summary
        assert "with_ingredient" in summary
        assert "unique_ingredients" in summary

    def test_summary_values_reasonable(self):
        """Os valores do resumo devem ser razoáveis"""
        df = load_fda_drugs()
        active = filter_active_drugs(df)
        summary = get_drug_summary(active)

        # Todos os medicamentos ativos devem ter princípio ativo
        assert summary["with_ingredient"] == summary["total_count"]
        # Deve haver ingredientes únicos
        assert summary["unique_ingredients"] > 1000
