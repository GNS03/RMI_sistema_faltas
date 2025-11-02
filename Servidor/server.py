# Fix for python being dumb
import socket

import Pyro5.api
import Pyro5.socketutil

from model.aluno_util.aluno_controller import AlunoController
from model.avaliacao_util.avaliacao_controller import AvaliacaoController
from model.disciplina_util.disciplina_controller import DisciplinaController
from model.professor_util.professor_controller import ProfessorController


# import sys
# import os
#
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def get_local_ip():
    try:
        # cria um socket UDP “para fora” (não envia dados de fato)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Google DNS só para descobrir a interface
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


if __name__ == "__main__":

    # Utils
    hostname = socket.gethostname()
    my_ip = Pyro5.socketutil.get_ip_address(hostname, workaround127=True, version=4)

    # Start SQL connection
    # sql = SQLConnection()
    # sql.connect()

    # # Run NameServer
    # try:
    #     nameserverUri, nameserverDaemon, broadcastServer = Pyro5.nameserver.start_ns(my_ip, 9090)
    #     assert broadcastServer is not None, "expect a broadcast server to be created"
    #     print (f"Nameserver running at: {nameserverUri}")
    # except Exception as e:
    #     print(e)
    #     exit(1)

    # Expose classes to Pyro5
    aluno_exp = Pyro5.api.expose(AlunoController)
    avaliacao_exp = Pyro5.api.expose(AvaliacaoController)
    disciplina_exp = Pyro5.api.expose(DisciplinaController)
    professor_exp = Pyro5.api.expose(ProfessorController)

    # Starting RMI server

    Pyro5.api.serve(
        {
            aluno_exp: "AlunoController",
            avaliacao_exp: "AvaliacaoController",
            disciplina_exp: "DisciplinaController",
            professor_exp: "ProfessorController",
        },
        host=get_local_ip(),
        port=9090,
        use_ns=False,
    )

    # with Pyro5.api.Daemon(my_ip) as daemon:
    #
    #     # Register exposed classes
    #     uri = daemon.register(aluno_exp)
    #     nameserverDaemon.nameserver.register("aluno", uri)
    #     print(f"Wrapped class registered, uri: {uri}")
    #
    #     print("Waiting for requests...")
    #     daemon.requestLoop()

    # clean up
    # nameserverDaemon.close()
    # broadcastServer.close()
    print("done")
