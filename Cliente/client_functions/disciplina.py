import socket

import Pyro5.api
import Pyro5.socketutil
import dotenv


# Utils
hostname = socket.gethostname()
my_ip = dotenv.dotenv_values(".env").get("IP")
port = 9090
print(f"Hostname = {hostname}, IP = {my_ip}, Port = {port}")

classe = "DisciplinaController"

uri = f"PYRO:{classe}@{my_ip}:{port}"

try:
    disciplina_control = Pyro5.api.Proxy(uri)
except Exception as e:
    raise e


def select():
    # print("Getting data from server, table: disciplinas")

    disciplinas = disciplina_control.select()
    if disciplinas:
        # print("SQL executed successfully.")
        return disciplinas
    else:
        print("ERROR: An error ocurred check the server for details")


def inserir(id: int, nome: str, horas: int):

    if disciplina_control.inserir(id, nome, horas):
        print("SQL executed successfully.")
    else:
        print("ERROR: An error ocurred check the server for details")


def pesquisar(id: int):
    disciplinas = disciplina_control.pesquisar(id)
    if disciplinas:
        print(disciplinas)
        return disciplinas
    else:
        print("Did not find that key")


def editar(id: int, nome: str, horas: int):
    if disciplina_control.editar(id, nome, horas):
        print("SQL executed successfully.")
    else:
        print("ERROR: An error ocurred check the server for details")


def remover(id: int, nome: str, horas: int):
    if disciplina_control.remover(id):
        print("SQL executed successfully.")
    else:
        print("Did not find that key")


if __name__ == "__main__":

    print(select())
