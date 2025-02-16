
# Repositórios Populares com GraphQL

## Descrição
Este projeto utiliza Python para buscar dados sobre repositórios populares no GitHub através de consultas GraphQL. O script retorna informações como nome do repositório, data de criação, última atualização, linguagem principal, número de pull requests, issues e releases.

## Requisitos
- Python 3.8 ou superior instalado.
- Um token de acesso pessoal do GitHub para realizar consultas à API GraphQL.

## Instruções de Execução
1. Clone o repositório para sua máquina:
   ```bash
   git clone <URL-do-repositorio>
   ```
2. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script principal:
   ```bash
   python code/main.py
   ```

## Saída
Os resultados formatados serão salvos na pasta `outputs` em um arquivo CSV chamado `repositorios_formatados.csv`.
