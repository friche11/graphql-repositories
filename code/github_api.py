import http.client
import json
import os
from dotenv import load_dotenv 

load_dotenv()

def load_query():
    with open("query.gql", "r") as file:
        return file.read()

QUERY = load_query()
TOKEN = os.getenv("GITHUB_TOKEN")

GITHUB_API_URL = "api.github.com"

def fetch_github_data():
    if not TOKEN:
        raise ValueError("GITHUB_TOKEN não está definido. Configure a variável de ambiente.")

    conn = http.client.HTTPSConnection(GITHUB_API_URL)

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": "Python-Request"
    }

    repos = []
    after_cursor = None  # Cursor para paginação

    while len(repos) < 100:
        variables = {"after": after_cursor}
        request_body = json.dumps({"query": QUERY, "variables": variables})
        
        conn.request("POST", "/graphql", body=request_body, headers=headers)
        response = conn.getresponse()
        data = json.loads(response.read().decode("utf-8"))

        if "errors" in data:
            print("Erro ao requisitar API do GitHub:", data["errors"])
            print(f"\nTente diminuir a quantidade de repositórios a serem consultados em uma única requisição.")
            break

        search_results = data.get("data", {}).get("search", {})

        new_repos = [edge["node"] for edge in search_results.get("edges", [])]
        if not new_repos:
            print("Nenhum novo repositório encontrado, encerrando paginação.")
            break

        repos.extend(new_repos)

        # Atualiza paginação
        has_next_page = search_results.get("pageInfo", {}).get("hasNextPage", False)
        after_cursor = search_results.get("pageInfo", {}).get("endCursor")

        print(f"Obtidos {len(new_repos)} novos repositórios. Total: {len(repos)}\n")

        if not has_next_page or len(repos) >= 100:
            break

    conn.close()
    return repos[:100] 
