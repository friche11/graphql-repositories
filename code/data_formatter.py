import csv
import os
from datetime import datetime
from tabulate import tabulate

OUTPUT_DIR = "../outputs"
OUTPUT_FILE = f"{OUTPUT_DIR}/repositorios_formatados.csv"

def safe_get(dictionary, keys, default="N/A"):
    """ Obtém um valor aninhado de um dicionário de forma segura. """
    for key in keys:
        if dictionary is None:
            return default
        dictionary = dictionary.get(key)
    return dictionary if dictionary is not None else default

def process_repositories(repos):
    processed_repos = []
    now = datetime.utcnow()

    for repo in repos:
        try:
            created_at_str = safe_get(repo, ["createdAt"])
            updated_at_str = safe_get(repo, ["updatedAt"])

            # Convertendo datas apenas se forem válidas
            created_at = datetime.strptime(created_at_str, "%Y-%m-%dT%H:%M:%SZ") if created_at_str != "N/A" else None
            updated_at = datetime.strptime(updated_at_str, "%Y-%m-%dT%H:%M:%SZ") if updated_at_str != "N/A" else None

            age_days = (now - created_at).days if created_at else "N/A"
            time_since_last_update = (now - updated_at).days if updated_at else "N/A"

            # Tratamento para issues
            total_issues = safe_get(repo, ["totalIssues", "totalCount"], 0)
            closed_issues = safe_get(repo, ["closedIssues", "totalCount"], 0)
            issue_ratio = int(round((closed_issues / total_issues) * 100)) if total_issues > 0 else ""

            processed_repos.append({
                "name": safe_get(repo, ["name"]),
                "age_days": age_days,
                "pull_requests": safe_get(repo, ["pullRequests", "totalCount"], 0),
                "releases": safe_get(repo, ["releases", "totalCount"], 0),
                "time_since_last_update": time_since_last_update,
                "primary_language": safe_get(repo, ["primaryLanguage", "name"]),
                "issue_ratio": issue_ratio,
            })

        except Exception as e:
            print(f"Erro inesperado ao processar repositório '{safe_get(repo, ['name'])}': {e}")

    return processed_repos

def save_to_csv(repositories):
    """Salva os dados processados em um arquivo CSV formatado corretamente."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Nome", "Idade (dias)", "PRs", "Releases", "Última Atualização (dias)", "Linguagem", "Fechamento de Issues (%)"])
        
        formatted_data = []
        for repo in repositories:
            row = [
                repo["name"],
                repo["age_days"],
                repo["pull_requests"],
                repo["releases"],
                repo["time_since_last_update"],
                repo["primary_language"],
                repo["issue_ratio"]
            ]
            writer.writerow(row)
            formatted_data.append(row)
    
    print_formatted_output(formatted_data)

def print_formatted_output(formatted_data=None):
    """Exibe os dados no terminal de maneira formatada."""
    if formatted_data is None:
        formatted_data = []
    
    print("\n Repositórios Populares Formatados \n")
    print(tabulate(
        formatted_data, 
        headers=["Nome", "Idade (dias)", "PRs", "Releases", "Última Atualização (dias)", "Linguagem", "Fechamento de Issues (%)"], 
        tablefmt="fancy_grid", 
        numalign="right"
    ))
    print(f"\n Arquivo CSV formatado salvo em: {OUTPUT_FILE}")
