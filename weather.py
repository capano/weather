# Weather API Python - by Capano Wagner - 2021

import requests
from flask import Flask
import psycopg2 as db
import json

#----------------------------------------------------
#   CONNECTION
#----------------------------------------------------
# Dados para conectar na API openweather + Endereço do servidor da API weather DEVEM ESTAR EM ARQUIVO


class Connect:
    host = "192.168.100.15"
    port = "9000"
    debug = "False"
    url = "https://api.openweathermap.org/data/2.5/forecast"
    appid = "2d92472a453a1eebe622a647e2e4f882"

#----------------------------------------------------
#   CONFIG
#----------------------------------------------------


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

#----------------------------------------------------
#   CONNECTION
#----------------------------------------------------


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

    #----------------------------------------------------
    #   INSERT
    #----------------------------------------------------

    def insert(self, *args):
        try:
            sql = "INSERT INTO weather (cidade,info) VALUES (%s,%s)"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print("Erro de inserção", e)

    #----------------------------------------------------
    #   SEARCH
    #----------------------------------------------------

    def search(self, *args, type_s="name"):
        sql = 'SELECT count(cidade) from weather WHERE cidade = %s '
        data = self.query(sql, args)
        data_cnz = data[0]
        data_cnt = data_cnz[0]
        data_qtd = int(data_cnt)

        # q_06 query OK - =5 + ELEMENTOS REMOVIDOS
        sql = "SELECT json_agg(json_build_object('db_id', id , " \
              "'created_at',cast(cast(extract(epoch from created_at)" \
              " as int) as text),'list',info -> 'list' )) FROM weather WHERE cidade = %s"

        # print(sql)                                        # TESTE
        data = self.query(sql, args)
        data_cnz = data[0]                                  # TESTE
        # data = data_cnz                                   # TESTE
        data_cny = data_cnz[0]                              # TESTE
        data = data_cny                                     # TESTE

        if data_qtd < 1:
            data = json.loads('{"cod": "404", "message": "sem registros para esta cidade"}')

        if data:
            output = json.dumps(data)                       # dump data
            return data

        return "registro não encontrado"


w = Weather()
# Consulta
app = Flask(__name__)


@app.route("/weather/<i_consulta>")
def ok(i_consulta):

    #----------------------------------------------------
    #   CONSULTA
    #----------------------------------------------------
    i_error = 0
    i_key_func = i_consulta.rsplit("&")
    if len(i_key_func) > 1:
        i_key_cidade = i_key_func[1].rsplit("=")
        i_cidade = i_key_cidade[1]
        i_cidade = i_cidade.capitalize()
        i_funcao = i_key_func[0]
        i_funcao = i_funcao.casefold()

        if i_key_cidade[0] != "cidade":
            i_error = 445                                   #erro na chave de pesquisa de cidade

    else:
        i_error = 443                                       #não especificado chave cidade

    if i_error == 0:

        #----------------------------------------------------
        #   PREVISAO
        #----------------------------------------------------
        if i_funcao == "previsao":
            i_request = Connect.url
            i_request += "?q="+i_cidade
            i_request += '&units=metric'
            i_request += "&appid="+Connect.appid
            request = requests.get(i_request)
            return_data = request.json()                    # dict Py
            i_code = return_data["cod"]
            return_code = json.dumps(return_data, indent=4)  # transforma em JSON
            outfile = json.dumps(return_data)               # JSON plano

            # Print test area -------------                 # TEST AREA
            if 1 == 2:
                i_s1 = '======================================= '
                print(i_s1+'i_request\n'+i_request)
                print(i_s1+'request\n')
                print(request)
                print(i_s1+'return_data\n')
                print(return_data)
                print(i_s1 + 'i_code\n' + i_code)
                print(i_s1 + 'return_code\n' + return_code)
                print(i_s1 + 'outfile\n' + outfile)
                print(outfile)
                print(type(outfile))
                print(i_s1 + 'outfile\n')
            # ----------------------------------------------------

            if i_code == "200":
                w.insert(i_cidade, outfile)
                return outfile

            else:
                i_error = int(i_code)

        #----------------------------------------------------
        #   PESQUISA
        #----------------------------------------------------
        elif i_funcao == "pesquisa":
            ret_query = w.search(i_cidade)
            outfile = json.dumps(ret_query)                  # funcionava normal
            return outfile

        else:
            i_error = 442                           # não especificado chave de pesquisa valida

    #----------------------------------------------------
    #   NENSAGEM DE ERRO
    #----------------------------------------------------
    # mensagens de erro
    if i_error > 0:
        return '{"cod": ' + str(i_error) + ', "message": "Invalid API key. ' \
                  'Please see https://github.com/capano/weather for more info."}'


app.run(host=Connect.host, port=Connect.port, debug=Connect.debug)
