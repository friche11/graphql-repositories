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

## Resultados Obtidos

#### RQ 01. Sistemas populares são maduros/antigos?
  - Métrica: Idade do repositório
  - Mediana: 8.28 anos (3024 dias)
  - Os dados indicam que os sistemas populares têm, no geral, mais de 8 anos, confirmando nossa hipótese de que esses sistemas são maduros.

#### RQ 02. Sistemas populares recebem muita contribuição externa?
  - Métrica: Total de pull requests aceitas
  - Mediana: 629 pull requests
  - A mediana de 629 pull requests aceitas sugere que os sistemas populares recebem uma boa quantidade de contribuições externas.

#### RQ 03. Sistemas populares lançam releases com frequência?
  - Métrica: Total de releases
  - Mediana: 33 releases
  - Com uma mediana de 33 releases, comprovamos que os sistemas populares frequentemente lançam novas versões.

#### RQ 04. Sistemas populares são atualizados com frequência?
  - Métrica: Tempo até a última atualização
  - Mediana: 0 dias
  - A mediana de 0 dias indica que os sistemas populares são atualizados praticamente diariamente. Até analisamos melhor e encontramos poucos repositórios que tinha apenas 1 ou mais dias sem atualizações. Isso indica que sistemas populares são atualizados com frequência. 

#### RQ 05. Sistemas populares são escritos nas linguagens mais populares?
  - Métrica: Linguagem primária de cada repositório
  - Contagem por Linguagem:
    - Python: 172
    - JavaScript: 143
    - TypeScript: 146
    - Go: 73
    - Java: 52
    - C++: 51
    - Rust: 41
    - ... (entre outras)
      
  - Os dados mostram que os sistemas populares são frequentemente escritos em linguagens mais populares e conhecidas.

![image](https://github.com/user-attachments/assets/338d0880-189f-4ed0-ba62-3abc258c332b)
  
#### RQ 06. Sistemas populares possuem um alto percentual de issues fechadas?
  - Métrica: Proporção de issues fechadas
  - Mediana: 86
  - A proporção de 86% de issues fechadas confirma que os sistemas populares mantêm um alto percentual de resolução de problemas.

#### Logo abaixo mostramos em um gráfico as métricas por valores medianos que respondem o RQ 01, RQ 02, RQ 03, RQ 04 e RQ 06.
![image](https://github.com/user-attachments/assets/e5989313-9673-4403-94cb-51c70a552827)

#### RQ 07. Sistemas escritos em linguagens mais populares recebem mais contribuição externa, lançam mais releases e são atualizados com mais frequência?

Para fazer essa análise comparamos as 3 linguagens mais populares (Python, JavaScript e TypeScript) com o restante.

#### Considerando contribuições externas:
  - A mediana do número de PRs é um pouco maior para as linguagens populares (789) do que para as outras (681).

#### Considerando número de releases:
  - A mediana do número de releases é maior para as linguagens populares (50) do que para outras linguagens (39).

#### Considerando o tempo desde a última atualização:
  - A mediana de dias desde a última atualização é 0 para ambos os grupos, indicando que a maioria dos repositórios analisados é atualizada com frequência.

Sistemas escritos nas três linguagens mais populares recebem mais contribuição externa (PRs aceitos) e lançam mais releases com mais frequência. No entanto, a frequência de atualização não mostra uma diferença significativa, pois a mediana de dias desde a última atualização é zero para ambos os grupos, indicando que a maioria dos sistemas analisados é atualizada regularmente.

![image](https://github.com/user-attachments/assets/dd0a6bbe-8dce-4284-b61c-78bae3b09b2f)

## Conclusão

Nossa análise mostrou que os repositórios mais populares do GitHub são, em sua maioria, antigos, bem mantidos e com muitos colaboradores. Com a mediana da idade de mais de 8 anos, esses projetos recebem muitas contribuições externas, são atualizados frequentemente e lançam novas versões de forma regular.

As linguagens mais populares, como Python, JavaScript e TypeScript, tendem a atrair mais contribuições e releases. Além disso, a alta taxa de fechamento de issues (86%) indica que esses projetos possuem uma manutenção ativa e eficiente.

No fim, o que torna um sistema popular não é apenas a tecnologia usada, mas também o forte engajamento da comunidade e a consistência na evolução do projeto.
