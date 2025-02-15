from datetime import datetime

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
            issue_ratio = f"{(closed_issues / total_issues) * 100:.2f}%" if total_issues > 0 else "N/A"

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
