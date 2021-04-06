# Weather Python API

Weather é uma simples API desenvolvida em Python para acessar dados de previsão de tempo para 5 dias por cidade. Cada consulta que retorne dados válidos os grava em histórico para consulta .

The latest version can always be found at http://github.com/capano/weather

## Requisitos Mínimos

* PostgreSQL v9.6, 10, 11, 12 ou 13 
* Python v2.6 - v2.7 ou v3.7

## Considerações sobre o Projeto

### Escolha do Framework

Dois Frameworks se destacam para uso em Python, o Django que é o mais utilizado e o Flask, que é considerado um micro-framework.
A escolha recaiu sobre o Flask devido a facilidade em importar suas funcionalidades e se encaixar na **** do projeto que é a simplicidade e tamanho reduzido.
Além disso o Flask é satisfatório para desenvolvimento de APIs em Back-end.

## Instalação e uso

### Arquivos e dependências

O arquivo principal a ser usado é o weather.py
Basta executar no python, cuidando antes para ter as bibliotecas necessárias. 
Voce vai precisar da Requests, Flask, psycopg2 e json.

### Configurações

Edite os dados da classe Connect para um IP e porta que o servidor Web Python deverá usar.
Depois insira os dados PostgreSQL na classe Config.
Sim estes dados não deveriam está no código, mas essa ainda não é a versão de produção, ok ? Então podemos agregar uma classe que pesque todos os dados em um lugar seguro depois.

### Criando tabelas

Voce deve criar um DB no Postgres, conforme indicado na classe Config. Depois use o Script weather.sql para criar a tabela.

### Primeiros testes

Quando rodar o programa ele fara listen da porta e IP configurado
Se voce tiver outro computador numa rede interna que possua Pyton, poderá rodar o programa



## Códigos de erro

### O que pode dar de errado com o Weather ?
Os códigos de erro retornados pela API estão listados abaixo. Veja o exemplo :


```
{"cod": 401, "message": "Invalid API key. Please see https://github.com/capano/weather for more info."}
```


 - **441** : não foi especifidado uma chave válida para o uso da API
 - **442** : a especificação da cidade está incorreta

#

Copyright 2021 W.Capano	

        
          
