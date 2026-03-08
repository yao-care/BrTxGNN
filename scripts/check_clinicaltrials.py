#!/usr/bin/env python3
"""
Verificar ClinicalTrials.gov para novos ensaios clínicos relacionados à nossa lista de medicamentos.
Cria Issues no GitHub quando novos ensaios são encontrados.
"""

import json
import os
import time
from datetime import datetime, timedelta
from pathlib import Path

import requests

from github_utils import create_issue, issue_exists, close_older_clinicaltrials_issues

# Configuração
API_BASE = "https://clinicaltrials.gov/api/v2/studies"
CACHE_FILE = Path(__file__).parent.parent / "data" / "cache" / "clinicaltrials_cache.json"
DRUG_LIST_FILE = Path(__file__).parent / "drug_list.json"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPO = os.environ.get("GITHUB_REPOSITORY", "yao-care/BrTxGNN")
RATE_LIMIT_DELAY = 0.5  # segundos entre chamadas da API


def load_cache() -> dict:
    """Carregar o cache de IDs de ensaios já vistos."""
    if CACHE_FILE.exists():
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"last_check": None, "seen_trials": {}}


def save_cache(cache: dict):
    """Salvar o cache."""
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    cache["last_check"] = datetime.now().isoformat()
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)


def load_drug_list() -> list:
    """Carregar a lista de medicamentos."""
    if not DRUG_LIST_FILE.exists():
        print(f"Arquivo de lista de medicamentos não encontrado: {DRUG_LIST_FILE}")
        print("Execute extract_drug_list.py primeiro para gerar a lista.")
        return []

    with open(DRUG_LIST_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("drugs", [])


def search_trials(drug_name: str, days_back: int = 7) -> list:
    """Buscar ensaios atualizados nos últimos N dias."""
    min_date = (datetime.now() - timedelta(days=days_back)).strftime("%Y-%m-%d")

    params = {
        "query.term": drug_name,
        "filter.advanced": f"AREA[LastUpdatePostDate]RANGE[{min_date},MAX]",
        "pageSize": 50,
        "fields": "NCTId,BriefTitle,OverallStatus,Phase,EnrollmentCount,Condition,LastUpdatePostDate"
    }

    try:
        response = requests.get(API_BASE, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data.get("studies", [])
    except requests.RequestException as e:
        print(f"Erro ao buscar ensaios para {drug_name}: {e}")
        return []


def create_github_issue(drug_name: str, new_trials: list):
    """Criar uma Issue no GitHub para novos ensaios encontrados."""
    title = f"🔬 Novos Ensaios Clínicos: {drug_name} ({len(new_trials)} registros)"

    if not GITHUB_TOKEN:
        print(f"[DRY RUN] Criaria issue para {drug_name} com {len(new_trials)} novos ensaios")
        for trial in new_trials[:3]:  # Mostrar primeiros 3
            nct_id = trial.get("protocolSection", {}).get("identificationModule", {}).get("nctId", "Desconhecido")
            brief_title = trial.get("protocolSection", {}).get("identificationModule", {}).get("briefTitle", "Desconhecido")
            print(f"  - {nct_id}: {brief_title[:60]}...")
        return

    # Fechar issues mais antigas deste medicamento antes de criar uma nova
    closed_count = close_older_clinicaltrials_issues(drug_name)
    if closed_count > 0:
        print(f"  → Fechadas {closed_count} issue(s) mais antigas para {drug_name}")

    # Formatar detalhes dos ensaios
    trial_details = []
    for trial in new_trials:
        protocol = trial.get("protocolSection", {})
        id_module = protocol.get("identificationModule", {})
        status_module = protocol.get("statusModule", {})
        design_module = protocol.get("designModule", {})

        nct_id = id_module.get("nctId", "Desconhecido")
        brief_title = id_module.get("briefTitle", "Desconhecido")
        status = status_module.get("overallStatus", "Desconhecido")
        phase = ", ".join(design_module.get("phases", ["Desconhecido"]))
        enrollment = design_module.get("enrollmentInfo", {}).get("count", "Desconhecido")

        trial_details.append(
            f"### {nct_id}\n"
            f"- **Título**: {brief_title}\n"
            f"- **Status**: {status}\n"
            f"- **Fase**: {phase}\n"
            f"- **Participantes**: {enrollment}\n"
            f"- **Link**: https://clinicaltrials.gov/study/{nct_id}\n"
        )

    body = f"""## 🔬 Detecção Automática de Novos Ensaios Clínicos

Esta Issue foi criada automaticamente pelo GitHub Actions.

### Nome do Medicamento
{drug_name}

### Fonte de Dados
ClinicalTrials.gov

### Tipo de Evidência
Novos ensaios clínicos

### Informações Detalhadas
Encontrados **{len(new_trials)}** ensaios clínicos novos ou atualizados:

{"".join(trial_details)}

### Ações Sugeridas
- [ ] Revisar conteúdo dos ensaios clínicos
- [ ] Avaliar se é necessário atualizar o nível de evidência do relatório do medicamento
- [ ] Adicionar informações dos ensaios clínicos ao relatório

---
*Tempo de detecção automática: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC*
"""

    # Criar a issue com verificação de deduplicação
    labels = ["auto-detected", "needs-review", "clinicaltrials"]
    create_issue(title, body, labels)


def main():
    print("=" * 60)
    print("Verificador de Evidências ClinicalTrials.gov")
    print(f"Iniciado em: {datetime.now().isoformat()}")
    print("=" * 60)

    # Carregar dados
    cache = load_cache()
    drugs = load_drug_list()

    if not drugs:
        print("Nenhum medicamento encontrado. Saindo.")
        return

    print(f"Carregados {len(drugs)} medicamentos da lista")
    print(f"Última verificação: {cache.get('last_check', 'Nunca')}")

    # Verificar cada medicamento
    new_findings = []
    seen_trials = cache.get("seen_trials", {})

    for i, drug in enumerate(drugs):
        drug_name = drug["name"]
        print(f"\n[{i+1}/{len(drugs)}] Verificando: {drug_name}")

        trials = search_trials(drug_name, days_back=7)
        time.sleep(RATE_LIMIT_DELAY)  # Limitação de taxa

        if not trials:
            continue

        # Filtrar para ensaios realmente novos
        drug_seen = seen_trials.get(drug_name, [])
        is_initial_discovery = not drug_seen  # Primeira vez verificando este medicamento
        new_trials = []

        for trial in trials:
            nct_id = trial.get("protocolSection", {}).get("identificationModule", {}).get("nctId")
            if nct_id and nct_id not in drug_seen:
                new_trials.append(trial)
                drug_seen.append(nct_id)

        if new_trials:
            # Pular criação de issue para descoberta inicial (primeira vez vendo este medicamento)
            if is_initial_discovery:
                print(f"  Descoberta inicial: {len(new_trials)} ensaios (nenhuma issue criada, linha de base estabelecida)")
            # Pular se apenas 1 ensaio - muito ruidoso, aguardar mais evidências
            elif len(new_trials) < 2:
                print(f"  Apenas {len(new_trials)} ensaio encontrado - abaixo do limite, ignorando issue")
            else:
                print(f"  Encontrados {len(new_trials)} novos ensaios!")
                new_findings.append({
                    "drug": drug_name,
                    "trials": new_trials
                })

        # Atualizar ensaios vistos
        seen_trials[drug_name] = drug_seen

    # Atualizar cache
    cache["seen_trials"] = seen_trials
    save_cache(cache)

    # Criar issues para novos achados
    print("\n" + "=" * 60)
    print("Criando Issues para Novos Achados")
    print("=" * 60)

    if new_findings:
        for finding in new_findings:
            create_github_issue(finding["drug"], finding["trials"])
    else:
        print("Nenhum novo ensaio encontrado.")

    print(f"\nConcluído em: {datetime.now().isoformat()}")


if __name__ == "__main__":
    main()
