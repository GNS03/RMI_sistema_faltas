import socket

import Pyro5.api
import Pyro5.socketutil
import dotenv


# Utils
hostname = socket.gethostname()
my_ip = dotenv.dotenv_values(".env").get("IP")
port = 9090
print(f"Hostname = {hostname}, IP = {my_ip}, Port = {port}")

classe = "ProfessorController"

uri = f"PYRO:{classe}@{my_ip}:{port}"

try:
    professor_control = Pyro5.api.Proxy(uri)
except Exception as e:
    raise e


def select():
    # print("Getting data from server, table: professores")

    professores = professor_control.select()
    if professores:
        # print("SQL executed successfully.")
        return professores
    else:
        print("ERROR: An error ocurred check the server for details")


def inserir(id: int, nome: str):

    if professor_control.inserir(id, nome):
        print("SQL executed successfully.")
    else:
        print("ERROR: An error ocurred check the server for details")


def pesquisar(id: int):
    professores = professor_control.pesquisar(id)
    if professores:
        print(professores)
        return professores
    else:
        print("Did not find that key")


def editar(id: int, nome: str):
    if professor_control.editar(id, nome):
        print("SQL executed successfully.")
    else:
        print("ERROR: An error ocurred check the server for details")


def remover(id: int, nome: str):
    if professor_control.remover(id):
        print("SQL executed successfully.")
    else:
        print("Did not find that key")


if __name__ == "__main__":

    print(select())
