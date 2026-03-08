#!/usr/bin/env python3
"""
Gerar lista de palavras-chave para monitoramento de notícias

Extrai de dados existentes:
- Nomes de medicamentos (DrugBank + nomes comerciais da ANVISA)
- Classes terapêuticas (português)
- Indicações previstas (inglês)

Saída: data/news/keywords.json
"""

import json
import re
from datetime import datetime
from pathlib import Path

# Diretório raiz do projeto
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
DOCS_DATA_DIR = PROJECT_ROOT / "docs" / "data"


def load_json(path: Path) -> dict | list:
    """Carregar arquivo JSON"""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_portuguese_terms(text: str) -> list[str]:
    """Extrair termos individuais do texto em português (separados por vírgula, ponto e vírgula, etc.)"""
    if not text:
        return []
    # Separadores: vírgula, ponto e vírgula, ponto, E
    terms = re.split(r"[,;.]+|\s+[eE]\s+", text)
    # Limpar espaços e filtrar strings vazias
    return [t.strip() for t in terms if t.strip() and len(t.strip()) >= 2]


def get_brand_names_from_anvisa(anvisa_data: list, drug_name: str) -> list[str]:
    """Encontrar nomes comerciais do medicamento nos dados da ANVISA"""
    brand_names = set()
    drug_name_lower = drug_name.lower()

    for item in anvisa_data:
        # Verificar se o princípio ativo corresponde
        ingredient = item.get("PRINCIPIO_ATIVO") or ""
        if drug_name_lower in ingredient.lower():
            product_name = item.get("NOME_PRODUTO", "")
            status = item.get("SITUACAO_REGISTRO", "")
            if product_name and status == "Ativo":
                # Extrair nome comercial (geralmente antes de números ou parênteses)
                match = re.match(r"^([A-Za-zÀ-ÿ\s]+)", product_name)
                if match:
                    brand = match.group(1).strip()
                    if len(brand) >= 3:
                        brand_names.add(brand)

    return list(brand_names)[:5]  # Máximo de 5 nomes comerciais


def load_synonyms(path: Path) -> dict:
    """Carregar tabela de sinônimos em português"""
    if not path.exists():
        return {"indication_synonyms": {}, "drug_synonyms": {}}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# Padrões de palavras-chave genéricas
GENERIC_KEYWORD_PATTERNS = {
    "_generic_cancer": [
        "cancer", "carcinoma", "tumor", "tumour", "neoplasm", "malignant",
        "leukemia", "lymphoma", "melanoma", "sarcoma", "myeloma"
    ],
    "_cardiovascular": [
        "cardiovascular", "atherosclerosis", "arteriosclerosis",
        "coronary", "vascular disease"
    ],
    "_heart_disease": [
        "heart disease", "heart failure", "cardiac", "myocardial",
        "arrhythmia", "angina", "cardiomyopathy"
    ],
    "stroke": ["stroke", "ischemic stroke", "cerebrovascular"],
    "herpes zoster": ["herpes", "zoster", "varicella"],
    "dementia": ["dementia", "alzheimer", "cognitive impairment"],
    "pancreatic cancer": ["pancreatic cancer", "pancreatic carcinoma", "pancreatic neoplasm"],
    "menopause": ["menopause", "postmenopaus", "estrogen-receptor", "hormone-resistant"],
}


def build_indication_index(drugs_data: dict, search_index: dict, synonyms: dict) -> dict:
    """Construir índice de indicações, registrando quais medicamentos estão associados a cada indicação"""
    indication_map = {}
    indication_synonyms = synonyms.get("indication_synonyms", {})

    # Primeiro adicionar todas as entradas de sinônimos (incluindo palavras-chave genéricas como _generic_cancer)
    for en_name, pt_list in indication_synonyms.items():
        key = en_name.lower()
        if key not in indication_map:
            indication_map[key] = {
                "name": en_name.lstrip("_"),  # Remover prefixo sublinhado
                "keywords_en": [en_name] if not en_name.startswith("_") else [],
                "keywords_pt": pt_list.copy(),
                "related_drugs": []
            }
            # Criar índice para cada sinônimo em português também
            for pt in pt_list:
                pt_key = pt.lower()
                if pt_key not in indication_map:
                    indication_map[pt_key] = {
                        "name": pt,
                        "keywords_en": [en_name] if not en_name.startswith("_") else [],
                        "keywords_pt": [pt],
                        "related_drugs": []
                    }

    for drug in search_index.get("drugs", []):
        drug_slug = drug.get("slug", "")

        # Processar indicações previstas
        for ind in drug.get("indications", []):
            ind_name = ind.get("name", "").lower()
            if ind_name:
                if ind_name not in indication_map:
                    # Procurar sinônimos
                    pt_synonyms = indication_synonyms.get(ind.get("name", ""), [])
                    indication_map[ind_name] = {
                        "name": ind.get("name", ""),
                        "keywords_en": [ind.get("name", "")],
                        "keywords_pt": pt_synonyms.copy(),
                        "related_drugs": []
                    }
                # Criar índice independente para sinônimos em português
                for pt in indication_synonyms.get(ind.get("name", ""), []):
                    pt_key = pt.lower()
                    if pt_key not in indication_map:
                        indication_map[pt_key] = {
                            "name": pt,
                            "keywords_en": [ind.get("name", "")],
                            "keywords_pt": [pt],
                            "related_drugs": []
                        }
                    if drug_slug not in indication_map[pt_key]["related_drugs"]:
                        indication_map[pt_key]["related_drugs"].append(drug_slug)

                if drug_slug not in indication_map[ind_name]["related_drugs"]:
                    indication_map[ind_name]["related_drugs"].append(drug_slug)

    # Adicionar palavras-chave em português das classes terapêuticas do drugs.json
    for drug_info in drugs_data.get("drugs", []):
        original = drug_info.get("original_indication", "")
        drug_slug = drug_info.get("slug", "")

        # Extrair termos em português
        pt_terms = extract_portuguese_terms(original)

        # Criar mapeamento para cada termo de indicação em português
        for term in pt_terms:
            term_key = term.lower()
            if term_key not in indication_map:
                indication_map[term_key] = {
                    "name": term,
                    "keywords_en": [],
                    "keywords_pt": [term],
                    "related_drugs": []
                }
            else:
                if term not in indication_map[term_key]["keywords_pt"]:
                    indication_map[term_key]["keywords_pt"].append(term)

            if drug_slug not in indication_map[term_key]["related_drugs"]:
                indication_map[term_key]["related_drugs"].append(drug_slug)

    # Conectar palavras-chave genéricas aos medicamentos com indicações relacionadas
    for generic_key, patterns in GENERIC_KEYWORD_PATTERNS.items():
        generic_key_lower = generic_key.lower()
        if generic_key_lower not in indication_map:
            continue

        # Encontrar todos os medicamentos que correspondem aos padrões
        for drug in search_index.get("drugs", []):
            drug_slug = drug.get("slug", "")
            for ind in drug.get("indications", []):
                ind_name = ind.get("name", "").lower()
                # Verificar se corresponde a algum padrão
                for pattern in patterns:
                    if pattern.lower() in ind_name:
                        if drug_slug not in indication_map[generic_key_lower]["related_drugs"]:
                            indication_map[generic_key_lower]["related_drugs"].append(drug_slug)
                        break

        # Atualizar também as entradas de sinônimos em português
        pt_list = indication_synonyms.get(generic_key, [])
        for pt in pt_list:
            pt_key = pt.lower()
            if pt_key in indication_map:
                for drug_slug in indication_map[generic_key_lower]["related_drugs"]:
                    if drug_slug not in indication_map[pt_key]["related_drugs"]:
                        indication_map[pt_key]["related_drugs"].append(drug_slug)

    return indication_map


def main():
    print("Carregando arquivos de dados...")

    # Verificar se os arquivos necessários existem
    search_index_path = DOCS_DATA_DIR / "search-index.json"
    drugs_data_path = DOCS_DATA_DIR / "drugs.json"
    anvisa_data_path = DATA_DIR / "raw" / "br_fda_drugs.json"
    synonyms_path = DATA_DIR / "news" / "synonyms.json"

    # Se os arquivos de dados processados não existirem, criar estrutura básica
    if not search_index_path.exists() or not drugs_data_path.exists():
        print("  AVISO: Arquivos de dados processados não encontrados.")
        print("  Execute primeiro as previsões do modelo para gerar os dados.")
        print("  Por enquanto, criando keywords.json básico apenas com dados da ANVISA...")

        # Carregar apenas dados da ANVISA
        if anvisa_data_path.exists():
            anvisa_data = load_json(anvisa_data_path)
            print(f"  - br_fda_drugs.json: {len(anvisa_data)} registros ANVISA")
        else:
            print(f"  ERRO: Arquivo ANVISA não encontrado em {anvisa_data_path}")
            print("  Execute: uv run python scripts/process_fda_data.py")
            return

        # Carregar sinônimos
        synonyms = load_synonyms(synonyms_path)
        print(f"  - synonyms.json: {len(synonyms.get('indication_synonyms', {}))} sinônimos de indicações")

        # Criar keywords básico a partir da ANVISA
        drugs_keywords = []
        therapeutic_classes = set()

        for drug in anvisa_data[:1000]:  # Limitar para processamento inicial
            ingredient = drug.get("PRINCIPIO_ATIVO", "")
            product_name = drug.get("NOME_PRODUTO", "")
            therapeutic_class = drug.get("CLASSE_TERAPEUTICA", "")

            if ingredient and drug.get("SITUACAO_REGISTRO") == "Ativo":
                slug = ingredient.lower().replace(" ", "-").replace("/", "-")

                # Coletar classes terapêuticas
                if therapeutic_class:
                    therapeutic_classes.add(therapeutic_class)

                drugs_keywords.append({
                    "slug": slug,
                    "name": ingredient,
                    "keywords": {
                        "en": [ingredient.lower()],
                        "pt": [product_name] if product_name else []
                    },
                    "therapeutic_class": therapeutic_class
                })

        # Criar índice de indicações a partir das classes terapêuticas
        indications_keywords = []
        for tc in therapeutic_classes:
            if tc:
                indications_keywords.append({
                    "name": tc,
                    "keywords": {
                        "en": [],
                        "pt": [tc]
                    },
                    "related_drugs": []
                })

        output = {
            "generated": datetime.now().strftime("%Y-%m-%d"),
            "drug_count": len(drugs_keywords),
            "indication_count": len(indications_keywords),
            "drugs": drugs_keywords[:200],  # Limitar saída inicial
            "indications": indications_keywords
        }

        output_path = DATA_DIR / "news" / "keywords.json"
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)

        print(f"\nSaída: {output_path}")
        print(f"  - Palavras-chave de medicamentos: {len(drugs_keywords[:200])}")
        print(f"  - Palavras-chave de indicações: {len(indications_keywords)}")
        return

    # Fluxo normal com todos os dados
    search_index = load_json(search_index_path)
    drugs_data = load_json(drugs_data_path)
    anvisa_data = load_json(anvisa_data_path)
    synonyms = load_synonyms(synonyms_path)

    print(f"  - search-index.json: {search_index.get('drug_count', 0)} medicamentos")
    print(f"  - drugs.json: {drugs_data.get('total_count', 0)} medicamentos")
    print(f"  - br_fda_drugs.json: {len(anvisa_data)} registros ANVISA")
    print(f"  - synonyms.json: {len(synonyms.get('indication_synonyms', {}))} sinônimos de indicações")

    # Construir lista de palavras-chave de medicamentos
    drugs_keywords = []

    for drug in search_index.get("drugs", []):
        drug_name = drug.get("name", "")
        drug_slug = drug.get("slug", "")

        # Palavras-chave em inglês
        keywords_en = [drug_name.lower()]

        # Adicionar nomes de marca (do search-index)
        for brand in drug.get("brands", []):
            if brand.lower() not in keywords_en:
                keywords_en.append(brand.lower())

        # Nomes comerciais em português (dos dados da ANVISA)
        keywords_pt = get_brand_names_from_anvisa(anvisa_data, drug_name)

        drugs_keywords.append({
            "slug": drug_slug,
            "name": drug_name,
            "keywords": {
                "en": keywords_en,
                "pt": keywords_pt
            },
            "url": f"/drugs/{drug_slug}/"
        })

    print(f"\nProcessando palavras-chave de medicamentos: {len(drugs_keywords)} medicamentos")

    # Construir lista de palavras-chave de indicações
    indication_map = build_indication_index(drugs_data, search_index, synonyms)

    # Converter para formato de lista (manter apenas palavras-chave com medicamentos relacionados)
    indications_keywords = []
    for key, data in indication_map.items():
        # Manter apenas indicações com medicamentos associados
        if data["related_drugs"]:
            indications_keywords.append({
                "name": data["name"],
                "keywords": {
                    "en": data["keywords_en"],
                    "pt": data["keywords_pt"]
                },
                "related_drugs": data["related_drugs"]
            })

    print(f"Processando palavras-chave de indicações: {len(indications_keywords)} indicações")

    # Saída
    output = {
        "generated": datetime.now().strftime("%Y-%m-%d"),
        "drug_count": len(drugs_keywords),
        "indication_count": len(indications_keywords),
        "drugs": drugs_keywords,
        "indications": indications_keywords
    }

    output_path = DATA_DIR / "news" / "keywords.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nSaída: {output_path}")
    print(f"  - Palavras-chave de medicamentos: {len(drugs_keywords)}")
    print(f"  - Palavras-chave de indicações: {len(indications_keywords)}")


if __name__ == "__main__":
    main()
