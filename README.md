# Weather Python API (v0.91 05-abr-2021)

Weather é uma simples API desenvolvida em Python para acessar dados de previsão de tempo de 5 dias para a cidade escolhida. Cada consulta que retorne dados válidos irá grava-los em um histórico para posterior consulta .
Estes dados serão armazenados em uma tabela no PostgreSQL.

The latest version can always be found at http://github.com/capano/weather

## Requisitos Mínimos

* PostgreSQL v9.6, 10, 11, 12 ou 13 
* Python v2.6 - v2.7 ou v3.7

## Considerações sobre o Projeto

### Escolha do Framework

Dois Frameworks se destacam para uso em Python, o Django que é o mais utilizado e o Flask, que é considerado um micro-framework.
A escolha recaiu sobre o Flask devido a facilidade em importar suas funcionalidades e se encaixar no escopo do projeto que é a simplicidade e tamanho reduzido.
Além disso o Flask é satisfatório para desenvolvimento de APIs em Back-end.

## Instalação e uso

### Arquivos e dependências

O arquivo principal e que armazena todo o código da API é o weather.py
Basta executar no python, cuidando antes para ter as bibliotecas necessárias. 
Voce vai precisar de:

* Requests
* Flask
* psycopg2 
* json.

### Configurações

Edite os dados da classe Connect para um IP e porta que o servidor Web Python deverá usar.
Depois insira os dados PostgreSQL na classe Config.
Sim estes dados não deveriam está no código, mas essa ainda não é a versão de produção, ok ? Então podemos agregar uma classe que pesque todos os dados em um lugar seguro depois.

Connect:
* host : IP da maquina onde o servidor WEB do projeto deve rodar. 
* port : Número da porta que a API usará para receber e enviar as requisições e dados. Cerifique que o Firewall esteja configurado para não a bloquear
* debug: False
* url e appid : endereço e key para a API Weather consultar outra API que fornecerá os dados meteorológicos.

Postgres
* user : nome de usuário do SGBD PostgreSQL
* password : senha para conectar ao banco de dados
* host : IP do PostgreSQL
* port : porta do Postgres. Por default é a 5432
* database : Nome do DB aberto para criar a tabela weather


### Criando tabelas

Voce deve criar um DB no Postgres, conforme indicado na classe Config. Depois use o Script weather.sql para criar a tabela.

### Primeiros testes

Quando rodar o programa ele fara listen da porta e IP configurado, de posse desses dados, pode testar de um destes modos:

* Se voce tiver outro computador numa rede interna que possua Pyton, poderá rodar o programa weatherunit.py nele. 
O programa faz o papel de navegador e pede para digitar a Key. Digite a chave 'previsao&cidade=blumenau' e enter.
Se tudo estiver ok, um grande código JSON irá rolar pela tela e ela vai voltar para o ponto inicial pedindo uma Key de novo.

* Um navegador como o Chrome também pode ser utilizado para o teste inicial, basta digitar algo como o seguinte: 
http://192.168.100.15:9000/weather/previsao&cidade=blumenau , sendo que IP e a porta devem ser iguais ao que voce configurou.
Se tudo estiver ok, um enorme código JSON devera aparecer. Bom, talvez apareça uma mensagem de erro caso a cidade digitada não exista no banco de dados ou esteja grafada de modo diferente.


### Como usar

Para fazer uma consulta é necessário colocar o temo 'previsao' (sem caracteres especiais), logo depois da ultima barra de endereço.
A seguir digite a cidade logo após o segmento '&cidade=' , como aí acima. 
Algumas cidades podem estar no idioma de origem, e com caracteres especiais ou espaços, como 'São Paulo' ou a potencialmente incrível cidade de 'Ayn Ḩalāqīm'.
Uma lista de todas cidades disponiveis para consulta da previsão do tempo no momento da elaboração deste programa, está em http://bulk.openweathermap.org/sample/city.list.json.gz .

Cada consulta feita nesta API é armazenada no banco de dados e o histórico fica disponível para consulta.
para fazê-lo basta trocar a chave "previsao" por "pesquisa" como nesse exemplo http://192.168.100.15:9000/weather/pesquisa&cidade=assis .
como na consulta da previsão, é necessário especificar a cidade a ser pesquisada.
Caso não exista um histórico da cidade digitada, retornará um erro 404 dizendo que não há registros para a cidade, como na figura abaixo.

![alt text](https://github.com/capano/weather/blob/main/Figura_01.png)

Os principais erros foram tratados e já devolvem mensagem para o consumidor da API. Mas alguns podem quebrar o sistema e devolver erro no terminal, fazendo a aplicação terminar.

O arquivo que a API devolve para o consumo está no formato JSON. Foi utilizada a ferramenta da http://jsonviewer.stack.hu/ para checar a compatibilidade. Alguns detalhes de formatação da parte de pesquisa ainda estão sendo corrigidos. Abaixo um print da ferramenta exibindo uma parte do JSON de  previsão devolvido pela API:


![alt text](https://github.com/capano/weather/blob/main/Figura_02.png)

## Considerações

Alguma localização ainda falta na API, nem todos termos estão em nosso idioma, mas as unidades já estão no sistema métrico e Celsius.
Para interpretar alguns dados como condições de clima, há uma tabela de referência disponível em https://openweathermap.org/weather-conditions

## Códigos de erro

### O que pode dar errado na API Weather ?

Os erros mais comuns retornam mensagens e são tratados internamente pela API.
Alguns dos códigos de erro retornados pela API estão explicados abaixo. Veja o exemplo :


```
{"cod": 401, "message": "Invalid API key. Please see https://github.com/capano/weather for more info."}
```

 - **401** : a chave de consulta foi digitada incorretamente 
 - **404** : sem registro para a cidade digitada ou cidade digitada incorretamente
 - **441** : não foi especifidado uma chave válida para o uso da API
 - **442** : a especificação da cidade está incorreta
 

#

Copyright 2021 W.Capano	

        
          
