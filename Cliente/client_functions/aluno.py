import socket

import Pyro5.socketutil, Pyro5.api

# Utils
hostname = socket.gethostname()
my_ip = Pyro5.socketutil.get_ip_address(hostname, workaround127 = True, version = 4)
port = 9090
print(f"Hostname = {hostname}, IP = {my_ip}, Port = {port}")

classe = "AlunoController"

uri = f"PYRO:{classe}@{my_ip}:{port}"

try:
    aluno_control = Pyro5.api.Proxy(uri)
except Exception as e:
    raise e

def select():
    # print("Getting data from server, table: alunos")

    alunos = aluno_control.select()
    if alunos:
        # print("SQL executed successfully.")
        return alunos
    else:
        print("ERROR: An error ocurred check the server for details")

def inserir(matricula: int, nome: str, idade: int, periodo: int):

    if aluno_control.inserir(matricula, nome, idade, periodo):
        print("SQL executed successfully.")
    else:
        print("ERROR: An error ocurred check the server for details")

def pesquisar(matricula: int):
    alunos = aluno_control.pesquisar(matricula)
    if alunos:
        print(alunos)
        return alunos
    else:
        print("Did not find that key")

def editar(matricula: int, nome: str, idade: int, periodo: int):
    if aluno_control.editar(matricula, nome, idade, periodo):
        print("SQL executed successfully.")
    else:
        print("ERROR: An error ocurred check the server for details")

def remover(matricula: int, nome: str, idade: int, periodo: int):
    if aluno_control.remover(matricula):
        print("SQL executed successfully.")
    else:
        print("Did not find that key")

if __name__ == "__main__":

   print(select())