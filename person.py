# https://youtu.be/qLdShpqS-Ok

import psycopg2 as db
import csv


class Config:
    def __init__(self):
        self.config = {
            "postgres": {
                "user": "postgres",
                "password": "postgres5689",
                "host": "127.0.0.1",
                "port": "5432",
                "database": "pydb"
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
class Person(Connection):
    def __init__(self):
        Connection.__init__(self)

    def insert(self, *args):
        try:
            sql = "INSERT INTO person (name) VALUES (%s)"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print("Erro de inserção", e)

    # importa de um CSV (precisa import csv)
    def insert_csv(self, filename):
        try:
            data = csv.DictReader(open(filename, encoding="utf-8"))
            for row in data:
                self.insert(row["name"])
            print("Registro inserido")
        except Exception as e:
            print("Erro ao inserir", e)

    def delete(self, id):
        try:
            sql_s = f"SELECT * FROM person WHERE id = {id}"
            if not self.query(sql_s):
                return "Registro não encontrado para deletar"
            sql_d = f"DELETE FROM person WHERE id = {id}"
            self.execute(sql_d)
            self.commit()
            return "Registro deletado"
        except Exception as e:
            print("Erro ao deletar", e)

    def update(self, id, *args):
        try:
            sql = f"UPDATE person SET name = %s WHERE id = {id}"
            self.execute(sql, args)
            self.commit()
            print("Registro atualizado ")
        except Exception as e:
            print("Erro ao atualizar", e)

    def search(self, *args, type_s="name"):
        sql = "SELECT * FROM person WHERE name LIKE %s"
        if type_s == "id":
            sql = "SELECT * FROM person WHERE id = %s"
        data = self.query(sql, args)
        if data:
            return data
        return "registro não encontrado"


if __name__ == '__main__':
    person = Person()
    # person.insert("Banana")
    print(person.query("SELECT * FROM person"))
    # person.insert_csv("data.csv")
    # print(person.delete(4))
    # person.update(1, "Willian C. Canio")
    print(person.search(1, type_s="id"))
    # x = input("pesquisar por: ")
    # x = f"%{x}%"
    # print(person.search(x))
    # print(person.search("Willian"))
    # print(person.search("%Will%"))
