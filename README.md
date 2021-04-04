# Weather Python API

Weather é uma simples API desenvolvida em Python para acessar dados de previsão de tempo para 5 dias por cidade. Cada consulta que retorne dados válidos os grava em histórico para consulta .

The latest version can always be found at http://github.com/capano/weather

## Requisitos Mínimos

* PostgreSQL v9.6, 10, 11, 12 ou 13 
* Python v2.6 - v2.7 ou v3.7

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

        
          
