import socket

import Pyro5.socketutil, Pyro5.api

# Utils
hostname = socket.gethostname()
my_ip = Pyro5.socketutil.get_ip_address(hostname, workaround127 = True, version = 4)
port = 9090
print(f"Hostname = {hostname}, IP = {my_ip}, Port = {port}")

classe = "AvaliacaoController"

uri = f"PYRO:{classe}@{my_ip}:{port}"

try:
    avaliacao_control = Pyro5.api.Proxy(uri)
except Exception as e:
    raise e

def select():
    # print("Getting data from server, table: avaliacaos")

    avaliacoes = avaliacao_control.select()
    if avaliacoes:
        # print("SQL executed successfully.")
        return avaliacoes
    else:
        print("ERROR: An error ocurred check the server for details")

def inserir(id: int, disciplina_fk: int, aluno_fk: int, nota: float):

    if avaliacao_control.inserir(id, disciplina_fk, aluno_fk, nota):
        print("SQL executed successfully.")
    else:
        print("ERROR: An error ocurred check the server for details")

def pesquisar(id: int):
    avaliacoes = avaliacao_control.pesquisar(id)
    if avaliacoes:
        print(avaliacoes)
        return avaliacoes
    else:
        print("Did not find that key")

def editar(id: int, disciplina_fk: int, aluno_fk: int, nota: float):
    if avaliacao_control.editar(id, disciplina_fk, aluno_fk, nota):
        print("SQL executed successfully.")
    else:
        print("ERROR: An error ocurred check the server for details")

def remover(id: int, disciplina_fk: int, aluno_fk: int, nota: float):
    if avaliacao_control.remover(id):
        print("SQL executed successfully.")
    else:
        print("Did not find that key")

if __name__ == "__main__":

   print(select())