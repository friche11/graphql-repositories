# Relatório Final 

## Introdução

Neste estudo, analisamos os 1.000 repositórios mais populares do GitHub, considerando o número de estrelas como critério de popularidade. O objetivo é analisar as principais características desses repositórios, como idade, contribuição externa, regularidade de releases e atualizações, popularidade das linguagens de programação utilizadas e taxa de issues fechadas. A partir dos dados coletados, apresentamos uma sumarização dos valores medianos e discutimos os resultados em relação às nossas hipóteses iniciais.

## Hipóteses inicias

#### RQ 01. Sistemas populares são maduros/antigos?
  _É provável que sistemas populares são maduros, pois projetos antigos têm mais tempo para ganhar popularidade e contribuidores._
  
#### RQ 02. Sistemas populares recebem muita contribuição externa?
  _Acreditamos que sistemas populares recebem muita contribuição externa, ou seja, um grande número de pull requests aceitas._
  
#### RQ 03. Sistemas populares lançam releases com frequência?
  _Supomos que esses sistemas lançam releases com bastante frequência._
  
#### RQ 04. Sistemas populares são atualizados com frequência?
  _Supomos que os sistemas populares sejam atualizados regularmente._
  
#### RQ 05. Sistemas populares são escritos nas linguagens mais populares?
  _Esperamos que sejam escritos nas linguagens mais populares._
  
#### RQ 06. Sistemas populares possuem um alto percentual de issues fechadas?
  _Acreditamos que esses sistemas possuem um alto percentual de issues fechadas._

#### RQ 07 Sistemas escritos em linguagens mais populares recebem mais contribuição externa, lançam mais releases e são atualizados com mais frequência? 
  _Esperamos que sistemas escritos em linguagens mais populares recebam mais contribuidores, lancem mais releases e sejam atualizados com mais frequência._

## Metodologia

Para responder às questões de pesquisa, coletamos dados de 1.000 repositórios com maior número de estrelas no GitHub utilizando GraphQL. As informações foram obtidas por meio da query.gql utilizando a API do GitHub e analisadas de acordo com os seguintes dados:
  - Nome do repositório (_name_),
  - Idade do repositório pela data de criação (_createdAt_),
  - Total de pull requests aceitas (_pullRequests(_states:_ _MERGED_)_),
  - Total de releases (_releases_),
  - Data da última atualização (_updatedAt_),
  - Linguagem primária (_primaryLanguage_),
  - Total de issues fechadas (_closedIssues: issues(states: CLOSED)_),
  - Total de issues (_totalIssues_),
  - Data do último commit na branch principal (_defaultBranchRef.target.committedDate_).

Paginação: Para obter os dados dos 1.000 repositórios, implementamos um mecanismo de paginação. A cada requisição, buscamos um lote de 20 repositórios e utilizamos o cursor _endCursor_ para continuar a busca na próxima página até atingir o limite de 1.000 repositórios.

### Processamento dos Dados

- Para cada repositório retornado pela API, calculamos as seguintes métricas: Idade do Repositório, Tempo desde a Última Atualização, Tempo desde o Último Commit, Proporção de Issues Fechadas.

### Armazenamento dos Dados

- Os dados processados foram armazenados em um arquivo CSV (repositorios_formatados.csv) para análise.
  
### Análise de dados

- Após a coleta e armazenamento dos dados, realizamos a análise das métricas para responder às questões de pesquisa. Utilizamos fórmulas da planilha para achar valores medianos para fornecer uma visão central das características dos repositórios analisados. Além disso, realizamos uma contagem por linguagem de programação para entender a distribuição das linguagens utilizadas nos repositórios populares.