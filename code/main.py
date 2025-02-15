from github_api import fetch_github_data
from data_formatter import process_repositories

if __name__ == "__main__":
    print(f"Buscando dados do GitHub...\n")
    try:
        raw_data = fetch_github_data()

        processed_data = process_repositories(raw_data)

        contador = 0  # Inicializa o contador de repositórios 
        
        for repo in processed_data[:100]:  # Mostra no console apenas a quantidade de repositórios informada
            contador += 1
            print(f"Repositório: {repo['name']}")
            print(f"Idade: {repo['age_days']} dias")
            print(f"PRs: {repo['pull_requests']}")
            print(f"Releases: {repo['releases']}")
            print(f"Última atualização: {repo['time_since_last_update']} dias")
            print(f"Linguagem: {repo['primary_language']}")
            print(f"Fechamento de Issues: {repo['issue_ratio']}")
            print("-" * 50)

        print(f"\nTotal de repositórios consultados: {len(raw_data)}")
        print(f"Total de repositórios exibidos: {contador}")

    except Exception as e:
        print(f"Houve um erro ao conectar com a API do Github.")
