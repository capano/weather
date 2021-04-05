# text


import requests
# from flask import Flask, request, jsonify, json
from flask import Flask
import psycopg2 as db
import json


# Dados para conectar na API openweather + Endereço do servidor da API weather
class Connect:
    host = "192.168.100.15"
    port = "9000"
    debug = "False"
    url = "https://api.openweathermap.org/data/2.5/forecast"
    appid = "2d92472a453a1eebe622a647e2e4f882"


class Config:
    def __init__(self):
        self.config = {
            "postgres": {
                "user": "postgres",
                "password": "postgres5689",
                "host": "127.0.0.1",
                "port": "5432",
                "database": "postgres"
            }
        }


class Connection(Config):
    def __init__(self):
        Config.__init__(self)
        try:
            self.conn = db.connect(**self.config["postgres"])
            self.cur = self.conn.cursor()
        except Exception as e:
            print("Erro de conexão", e)
            exit(24)

    def __enter__(self):
        return self

    # fecha conexão
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self.conn

    @property
    def cursor(self):
        return self.cur

    def commit(self):
        self.connection.commit()

    # return em registros
    def fetchall(self):
        return self.cursor.fetchall()

    # execute no SQL
    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    # Query no SQL
    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()


# manipular o banco
class Weather(Connection):
    def __init__(self):
        Connection.__init__(self)

    def insert(self, *args):
        try:
            sql = "INSERT INTO weather (cidade,info) VALUES (%s, %s)"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print("Erro de inserção", e)

    def search(self, *args, type_s="name"):
        # sql = "SELECT id,cidade,cast(cast(extract(epoch from created_at) as int) as text) as created_at FROM weather WHERE cidade = %s"
        sql = "SELECT json_agg(json_build_object('data_a',id,'data_b',cidade))  from weather WHERE cidade = %s"
        if type_s == "id":
            sql = "SELECT * FROM weather WHERE id = %s"
        data = self.query(sql, args)
        if data:
            return data
        return "registro não encontrado"


w=Weather()
# Consulta
app = Flask(__name__)


@app.route("/weather/<i_consulta>")
def ok(i_consulta):
    print(i_consulta)                               # teste
    print(Connect.host)                                # teste
    i_error = 0
    i_key_func = i_consulta.rsplit("&")
    print(i_key_func)                                     # teste
    if len(i_key_func) > 1:
        i_key_cidade = i_key_func[1].rsplit("=")
        i_cidade = i_key_cidade[1]
        i_cidade = i_cidade.capitalize()
        print(i_key_cidade)                                # teste
        if i_key_cidade[0] != "cidade":
            i_error = 445                               #erro na chave de pesquisa de cidade

    else:
        i_error = 443                                   #não especificado chave cidade

    if i_error == 0:
        if i_key_func[0] == "previsao":
            i_request = Connect.url
            i_request += "?q="+i_cidade
            i_request += '&units=metric'
            i_request += "&appid="+Connect.appid
            # print(i_request)
            # request = requests.get('https://api.openweathermap.org/data/2.5/forecast?q=London&units=metric&appid=2d92472a453a1eebe622a647e2e4f882')
            request = requests.get(i_request)
            return_data = request.json()                    # dict Py
            i_code = return_data["cod"]
            return_code = json.dumps(return_data, indent=4)  # transforma em JSON
            # outfile = open("sample.json", "w")
            # json.dump(return_data, outfile)
            outfile = json.dumps(return_data)               # JSON plano
            print(outfile)
            print(i_code)
            if i_code == "200":
                w.insert(i_cidade,outfile)
                return outfile
                # return return_data
            else:
                i_error = int(i_code)


        elif i_key_func[0] == "pesquisa":
            i_query = w.search(i_cidade)
            print(i_query)
            print(json.dumps(i_query, indent=4))
            # return '{ "PESQUISA": "Lily Bush", "items": {"product": "Diaper","qty": 24}}'
            return json.dumps(i_query, indent=4)

        else:
            i_error = 442                           # não especificado chave de pesquisa valida

    # -----------------------------------------------------
    # mensagens de erro
    if i_error > 0:
        return '{"cod": ' + str(i_error) + ', "message": "Invalid API key. Please see https://github.com/capano/weather for more info."}'


app.run(host=Connect.host, port=Connect.port, debug=Connect.debug)
