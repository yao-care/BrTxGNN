"""Testes para o script process_fda_data.py (processamento de dados ANVISA)"""

import json
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

import pandas as pd
import pytest

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from process_fda_data import load_config, process_anvisa_csv, download_anvisa_data


class TestLoadConfig:
    """Testes para a função load_config"""

    def test_loads_yaml_config(self):
        """Deve carregar o arquivo de configuração YAML"""
        config = load_config()
        assert isinstance(config, dict)

    def test_has_required_keys(self):
        """Deve conter as chaves necessárias"""
        config = load_config()
        assert "country_code" in config
        assert "field_mapping" in config
        assert "data_source" in config

    def test_country_code_is_br(self):
        """O código do país deve ser BR"""
        config = load_config()
        assert config["country_code"] == "BR"

    def test_data_source_has_url(self):
        """A fonte de dados deve ter URL"""
        config = load_config()
        assert "url" in config["data_source"]
        assert "anvisa" in config["data_source"]["url"].lower()


class TestProcessAnvisaCsv:
    """Testes para a função process_anvisa_csv"""

    def test_processes_csv_to_json(self, tmp_path):
        """Deve processar CSV e gerar JSON"""
        # Criar dados de teste em CSV
        csv_path = tmp_path / "test.csv"
        output_path = tmp_path / "output.json"

        csv_content = (
            "TIPO_PRODUTO;NOME_PRODUTO;NUMERO_REGISTRO_PRODUTO;PRINCIPIO_ATIVO;SITUACAO_REGISTRO;CATEGORIA_REGULATORIA\n"
            "MEDICAMENTO;ASPIRINA;100001;ÁCIDO ACETILSALICÍLICO;Ativo;Genérico\n"
            "MEDICAMENTO;PARACETAMOL;100002;PARACETAMOL;Ativo;Similar\n"
        )
        csv_path.write_text(csv_content, encoding="latin-1")

        result = process_anvisa_csv(csv_path, output_path)

        assert result == output_path
        assert output_path.exists()

        with open(output_path, encoding="utf-8") as f:
            data = json.load(f)

        assert len(data) == 2
        assert data[0]["NOME_PRODUTO"] == "ASPIRINA"

    def test_filters_medicamento_only(self, tmp_path):
        """Deve filtrar apenas medicamentos (TIPO_PRODUTO=MEDICAMENTO)"""
        csv_path = tmp_path / "test.csv"
        output_path = tmp_path / "output.json"

        csv_content = (
            "TIPO_PRODUTO;NOME_PRODUTO;NUMERO_REGISTRO_PRODUTO\n"
            "MEDICAMENTO;ASPIRINA;100001\n"
            "COSMÉTICO;SHAMPOO;100002\n"
            "MEDICAMENTO;IBUPROFENO;100003\n"
        )
        csv_path.write_text(csv_content, encoding="latin-1")

        process_anvisa_csv(csv_path, output_path)

        with open(output_path, encoding="utf-8") as f:
            data = json.load(f)

        # Deve conter apenas 2 medicamentos, não o cosmético
        assert len(data) == 2
        names = [d["NOME_PRODUTO"] for d in data]
        assert "SHAMPOO" not in names

    def test_creates_output_directory(self, tmp_path):
        """Deve criar o diretório de saída automaticamente"""
        csv_path = tmp_path / "test.csv"
        output_path = tmp_path / "subdir" / "nested" / "output.json"

        csv_content = "TIPO_PRODUTO;NOME_PRODUTO\nMEDICAMENTO;TESTE\n"
        csv_path.write_text(csv_content, encoding="latin-1")

        process_anvisa_csv(csv_path, output_path)

        assert output_path.exists()
        assert output_path.parent.exists()

    def test_handles_special_characters(self, tmp_path):
        """Deve lidar corretamente com caracteres especiais em português"""
        csv_path = tmp_path / "test.csv"
        output_path = tmp_path / "output.json"

        csv_content = (
            "TIPO_PRODUTO;NOME_PRODUTO;PRINCIPIO_ATIVO\n"
            "MEDICAMENTO;ÁCIDO FÓLICO;ÁCIDO FÓLICO\n"
            "MEDICAMENTO;PARACETAMOL;PARACETAMOL + CAFEÍNA\n"
        )
        csv_path.write_text(csv_content, encoding="latin-1")

        process_anvisa_csv(csv_path, output_path)

        with open(output_path, encoding="utf-8") as f:
            data = json.load(f)

        assert "ÁCIDO" in data[0]["NOME_PRODUTO"]


class TestDownloadAnvisaData:
    """Testes para a função download_anvisa_data"""

    @patch("process_fda_data.requests.get")
    def test_downloads_from_anvisa(self, mock_get, tmp_path):
        """Deve baixar dados da URL da ANVISA"""
        output_path = tmp_path / "test.csv"

        mock_response = MagicMock()
        mock_response.content = b"TIPO_PRODUTO;NOME\nMEDICAMENTO;TEST\n"
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        result = download_anvisa_data(output_path)

        assert result == output_path
        assert output_path.exists()
        mock_get.assert_called_once()
        # Verifica que a chamada usou verify=False (devido ao problema de certificado SSL)
        call_args = mock_get.call_args
        assert call_args.kwargs.get("verify") is False

    @patch("process_fda_data.requests.get")
    def test_creates_parent_directory(self, mock_get, tmp_path):
        """Deve criar o diretório pai automaticamente"""
        output_path = tmp_path / "subdir" / "test.csv"

        mock_response = MagicMock()
        mock_response.content = b"test data"
        mock_response.raise_for_status = MagicMock()
        mock_get.return_value = mock_response

        download_anvisa_data(output_path)

        assert output_path.parent.exists()


class TestAnvisaDataExistence:
    """Testes para verificar se os dados da ANVISA existem"""

    @pytest.fixture
    def raw_dir(self):
        """Obtém o caminho do diretório data/raw"""
        return Path(__file__).parent.parent / "data" / "raw"

    def test_anvisa_json_or_csv_exists(self, raw_dir):
        """Verifica se os dados da ANVISA já existem (JSON ou CSV)

        Se este teste falhar, execute primeiro o script de processamento:
        1. Execute: uv run python scripts/process_fda_data.py
        2. O script irá baixar automaticamente os dados da ANVISA
        """
        json_exists = (raw_dir / "br_fda_drugs.json").exists()
        csv_exists = (raw_dir / "anvisa_medicamentos.csv").exists()

        if not json_exists and not csv_exists:
            pytest.skip(
                "Dados da ANVISA ainda não foram baixados. Execute:\n"
                "uv run python scripts/process_fda_data.py"
            )

        assert json_exists or csv_exists

    def test_json_has_records(self, raw_dir):
        """Verifica se o JSON contém registros"""
        json_path = raw_dir / "br_fda_drugs.json"

        if not json_path.exists():
            pytest.skip("Arquivo br_fda_drugs.json não encontrado")

        with open(json_path, encoding="utf-8") as f:
            data = json.load(f)

        # ANVISA deve ter mais de 40.000 medicamentos
        assert len(data) > 40000, f"Esperado >40000 registros, encontrado {len(data)}"
