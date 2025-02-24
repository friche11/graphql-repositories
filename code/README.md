# Análise de Características de Repositórios Populares no GitHub

## 1. Introdução

Este relatório apresenta uma análise preliminar dos 1.000 repositórios com maior número de estrelas no GitHub. O objetivo é investigar diversos aspectos desses repositórios, tais como maturidade, contribuição externa, frequência de releases e atualizações, linguagem predominante e a eficácia na resolução de issues.

## 2. Hipóteses Informais

- **RQ01: Sistemas populares são maduros/antigos?**  
  *Hipótese:* Repositórios populares tendem a ser mais antigos, pois tiveram mais tempo para ganhar visibilidade e acumular estrelas.

- **RQ02: Sistemas populares recebem muita contribuição externa?**  
  *Hipótese:* É esperado que esses repositórios apresentem um volume significativo de pull requests de colaboradores externos, indicando uma comunidade ativa.

- **RQ03: Sistemas populares lançam releases com frequência?**  
  *Hipótese:* A frequência de releases pode ser alta, refletindo um desenvolvimento contínuo e a implementação regular de novas funcionalidades ou correções.

- **RQ04: Sistemas populares são atualizados com frequência?**  
  *Hipótese:* A manutenção ativa é comum nesses repositórios, sendo esperado que apresentem atualizações recentes e recorrentes.

- **RQ05: Sistemas populares são escritos nas linguagens mais populares?**  
  *Hipótese:* Acredita-se que a maioria desses repositórios utiliza linguagens amplamente adotadas no mercado, como JavaScript, Python, Java, entre outras.

- **RQ06: Sistemas populares possuem um alto percentual de issues fechadas?**  
  *Hipótese:* Um alto índice de issues fechadas pode indicar uma gestão eficiente do projeto e uma boa resposta às demandas da comunidade.

- **RQ07 (Bônus): Sistemas escritos em linguagens mais populares recebem mais contribuição externa, lançam mais releases e são atualizados com mais frequência?**  
  *Hipótese:* Repositórios desenvolvidos em linguagens populares podem atrair um número maior de colaboradores, refletido em métricas superiores de pull requests, releases e atualizações.

## 3. Metodologia

- **Coleta de Dados:**  
  Utilização da API GraphQL do GitHub para buscar informações dos 1.000 repositórios mais estrelados.

- **Processamento dos Dados:**
  - Cálculo da idade dos repositórios (em dias) a partir da data de criação.
  - Determinação do tempo decorrido desde a última atualização.
  - Contagem de pull requests aceitas, releases e issues fechadas.
  - Extração da linguagem principal de cada repositório.

- **Análise:**  
  A análise será realizada utilizando medidas descritivas (mediana para dados numéricos e contagens para dados categóricos) e, futuramente, uma comparação dos dados de acordo com a linguagem utilizada.

## 4. Resultados Preliminares



## 5. Discussão



## 6. Conclusão


