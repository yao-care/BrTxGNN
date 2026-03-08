#!/usr/bin/env python3
"""
Utilitários da API do GitHub para scripts de verificação de evidências do BrTxGNN.
Fornece funções de deduplicação e gerenciamento de issues.
"""

import os
import re
import requests
from typing import Optional, List

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPO = os.environ.get("GITHUB_REPOSITORY", "yao-care/BrTxGNN")


def get_headers() -> dict:
    """Obter headers da API do GitHub."""
    return {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }


def issue_exists(title: str, state: str = "all") -> bool:
    """
    Verificar se uma issue com o título dado já existe.

    Args:
        title: O título exato da issue a buscar
        state: "open", "closed", ou "all" (padrão: "all")

    Returns:
        True se uma issue com este título existe, False caso contrário
    """
    if not GITHUB_TOKEN:
        print(f"[DRY RUN] Verificaria issue existente: {title}")
        return False

    url = f"https://api.github.com/repos/{GITHUB_REPO}/issues"

    params = {
        "state": state,
        "labels": "auto-detected",
        "per_page": 100
    }

    try:
        response = requests.get(url, headers=get_headers(), params=params, timeout=30)
        response.raise_for_status()
        issues = response.json()

        # Verificar correspondência exata do título
        for issue in issues:
            if issue.get("title") == title:
                print(f"  → Issue já existe: #{issue['number']} - {title}")
                return True

        return False

    except requests.RequestException as e:
        print(f"Aviso: Não foi possível verificar issues existentes: {e}")
        return False


def find_existing_issues_by_label(drug_name: str, label: str, state: str = "open") -> List[dict]:
    """
    Encontrar issues existentes para um medicamento específico com um rótulo dado.

    Args:
        drug_name: O nome do medicamento a buscar
        label: O rótulo para filtrar (ex: "pubmed", "clinicaltrials", "anvisa")
        state: "open", "closed", ou "all" (padrão: "open")

    Returns:
        Lista de issues correspondentes (ordenadas por número, mais recentes primeiro)
    """
    if not GITHUB_TOKEN:
        print(f"[DRY RUN] Buscaria issues {label}: {drug_name}")
        return []

    url = f"https://api.github.com/repos/{GITHUB_REPO}/issues"
    params = {
        "state": state,
        "labels": label,
        "per_page": 100
    }

    try:
        response = requests.get(url, headers=get_headers(), params=params, timeout=30)
        response.raise_for_status()
        issues = response.json()

        # Filtrar issues que correspondem ao padrão do nome do medicamento
        matching = []
        drug_name_lower = drug_name.lower()
        for issue in issues:
            title = issue.get("title", "")
            match = re.search(r'：(.+?)\s*\(', title)
            if match:
                issue_drug = match.group(1).strip().lower()
                if issue_drug == drug_name_lower:
                    matching.append({
                        "number": issue["number"],
                        "title": issue["title"],
                        "url": issue["html_url"]
                    })

        # Ordenar por número da issue (mais recente primeiro)
        matching.sort(key=lambda x: x["number"], reverse=True)
        return matching

    except requests.RequestException as e:
        print(f"Aviso: Não foi possível buscar issues existentes: {e}")
        return []


def close_issue(issue_number: int, comment: str = None) -> bool:
    """
    Fechar uma issue do GitHub com um comentário opcional.

    Args:
        issue_number: O número da issue a fechar
        comment: Comentário opcional a adicionar antes de fechar

    Returns:
        True se bem sucedido, False caso contrário
    """
    if not GITHUB_TOKEN:
        print(f"[DRY RUN] Fecharia issue #{issue_number}")
        return True

    try:
        # Adicionar comentário se fornecido
        if comment:
            comment_url = f"https://api.github.com/repos/{GITHUB_REPO}/issues/{issue_number}/comments"
            requests.post(comment_url, headers=get_headers(), json={"body": comment}, timeout=30)

        # Fechar a issue
        url = f"https://api.github.com/repos/{GITHUB_REPO}/issues/{issue_number}"
        response = requests.patch(url, headers=get_headers(), json={"state": "closed"}, timeout=30)
        response.raise_for_status()
        print(f"  → Issue #{issue_number} fechada")
        return True

    except requests.RequestException as e:
        print(f"Erro ao fechar issue #{issue_number}: {e}")
        return False


def close_older_issues_by_label(drug_name: str, label: str, issue_type: str) -> int:
    """
    Fechar issues mais antigas de um medicamento com um rótulo específico, mantendo apenas a mais recente.

    Args:
        drug_name: O nome do medicamento a processar
        label: O rótulo para filtrar (ex: "pubmed", "clinicaltrials")
        issue_type: Descrição legível para o comentário (ex: "literatura", "ensaios clínicos")

    Returns:
        Número de issues fechadas
    """
    existing = find_existing_issues_by_label(drug_name, label, state="open")

    if len(existing) <= 1:
        return 0

    # Manter a primeira (mais recente), fechar o resto
    closed_count = 0
    for issue in existing[1:]:
        comment = f"🤖 Fechamento automático: há uma issue mais recente #{existing[0]['number']} rastreando {issue_type} deste medicamento."
        if close_issue(issue["number"], comment):
            closed_count += 1

    return closed_count


def close_older_pubmed_issues(drug_name: str) -> int:
    """Fechar issues mais antigas do PubMed para um medicamento."""
    return close_older_issues_by_label(drug_name, "pubmed", "nova literatura")


def close_older_clinicaltrials_issues(drug_name: str) -> int:
    """Fechar issues mais antigas de ClinicalTrials para um medicamento."""
    return close_older_issues_by_label(drug_name, "clinicaltrials", "novos ensaios clínicos")


def close_older_anvisa_issues(drug_name: str) -> int:
    """Fechar issues mais antigas da ANVISA para um medicamento."""
    return close_older_issues_by_label(drug_name, "anvisa", "alterações de registro")


def create_issue(title: str, body: str, labels: list) -> Optional[str]:
    """
    Criar uma issue no GitHub com verificação de deduplicação.

    Args:
        title: Título da issue
        body: Corpo da issue (markdown)
        labels: Lista de nomes de rótulos

    Returns:
        URL da issue se criada, None se ignorada ou falhou
    """
    if not GITHUB_TOKEN:
        print(f"[DRY RUN] Criaria issue: {title}")
        return None

    # Verificar se a issue já existe
    if issue_exists(title):
        print(f"  → Ignorando issue duplicada: {title}")
        return None

    url = f"https://api.github.com/repos/{GITHUB_REPO}/issues"
    payload = {
        "title": title,
        "body": body,
        "labels": labels
    }

    try:
        response = requests.post(url, headers=get_headers(), json=payload, timeout=30)
        response.raise_for_status()
        issue_url = response.json().get("html_url")
        print(f"  → Issue criada: {issue_url}")
        return issue_url

    except requests.RequestException as e:
        print(f"Erro ao criar issue: {e}")
        return None
