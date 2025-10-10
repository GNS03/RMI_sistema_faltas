import mysql.connector
from mysql.connector import MySQLConnection, errorcode

def sql_execute(op: str, sql_command: str, params: dict, fetch: bool = False) -> bool | list[dict]:

    # Conectar com o banco de dados
    cnx = SQLConnection()
    cursor = cnx.mysql_db.cursor()

    # Usa o cursor para mandar comandos, nao e bom usar f-strings
    try:
        cursor.execute(sql_command, params)
        # clear_screen.clear_console()

        print(f"Operation: {op}")

        # Se for pesquisa, devolve o resultado como uma lista de alunos
        if fetch:
            rows = cursor.fetchall()
            alunos: list[dict] = []
            for (matricula, nome, idade, periodo) in rows:
                print(f"Found: {matricula}, {nome}, {idade}, {periodo}")
                aluno = {"matricula": matricula, "nome": nome, "idade": idade, "periodo": periodo}
                alunos.append(aluno)
            return alunos

        # Se nao for pesquisa salva as mudancas com o commit, retorna True
        else:
            cnx.mysql_db.commit()
            print("SQL executed successfully.")
            return True

    # Se falhar retorna False e imprime o erro no servidor
    except mysql.connector.Error as err:
        print(f"Failed executing SQL command: {err}")
        return False
    finally:
        cursor.close()
        cnx.disconnect()

class SQLConnection:

    def __init__(self, host: str = "127.0.0.1", user: str = "root", password: str = "root", database: str = "Escola"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.mysql_db = self.connect()


    def connect(self) -> MySQLConnection:
        try:
            db = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database = self.database
            )

            if db:
                # print("Database connected succesfully")
                pass

            return db

        except mysql.connector.Error as err:

            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")

            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")

            else:
                print(err)

    def disconnect(self):
        self.mysql_db.close()
        # print("Database connection closed")