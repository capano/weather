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

        
          
