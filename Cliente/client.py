import socket

import Pyro5.api
import Pyro5.errors
import Pyro5.socketutil

from model import Aluno


def menu():

    opcao = input(
    """
    1 - Alunos
    2 - Disciplinas
    3 - Avaliacoes
    4 - Frequencia
    0 - Sair
    """
    )

    match(opcao):
        case 1:
            classe = "AlunoController"

            uri = f"PYRO:{classe}@{my_ip}:{port}"

            aluno_control = Pyro5.api.Proxy(uri)

            opcao = input(
            """
            1 - Inserir
            2 - Editar
            3 - Pesquisar
            4 - Deletar
            0 - Sair
            """
            )

            match(opcao):
                case 1:
                    matricula = int(input("Matricula: "))
                    nome = input("Nome: ")
                    idade = int(input("Idade: "))
                    periodo = int(input("Periodo: "))

                    if aluno_control.inserir(matricula, nome, idade, periodo):
                        print("SQL executed successfully.")
                    else:
                        print("An error ocurred check the server for details")
                case 2:
                    matricula = int(input("Matricula: "))

                    alunos = aluno_control.pesquisar(matricula)
                    if alunos:
                        print(alunos)
                    else:
                        print("Did not find that key")
                case 3:
                    print("Aperte enter para nao modificar o campo")
                    matricula = int(input("Matricula: "))
                    nome = input("Nome: ")
                    idade = int(input("Idade: "))
                    periodo = int(input("Periodo: "))

                    if aluno_control.editar(matricula, nome, idade, periodo):
                        print("SQL executed successfully.")
                    else:
                        print("An error ocurred check the server for details")
                case 4:
                    matricula = int(input("Matricula: "))

                    alunos = aluno_control.remover(matricula)
                    if alunos:
                        print(alunos)
                    else:
                        print("Did not find that key")
                case 0:
                    raise NotImplementedError

        case 2:
            raise NotImplementedError
        case 3:
            raise NotImplementedError
        case 4:
            raise NotImplementedError
        case 0:
            raise NotImplementedError


if __name__ == "__main__":

    # Utils
    hostname = socket.gethostname()
    my_ip = Pyro5.socketutil.get_ip_address(hostname, workaround127=True)
    port = 9090
    print(f"Hostname = {hostname}, IP = {my_ip}, Port = {port}")

    # nameserver = Pyro5.api.locate_ns(host=my_ip, port=9090)
    # print("Nameserver found")

    classe = "AlunoController"

    uri = f"PYRO:{classe}@{my_ip}:{port}"

    aluno_control = Pyro5.api.Proxy(uri)

    # if aluno_control.inserir(3, "Eduardo", 24, 4):
    #     print("SQL executed successfully.")
    # else:
    #     print("An error ocurred check the server for details")

    # alunos = aluno_control.pesquisar(2)
    # print(alunos)

    # aluno_control.editar(1, "Fer")

    # aluno_control.remover(2)