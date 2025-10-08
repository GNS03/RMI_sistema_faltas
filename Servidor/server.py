# Fix for python being dumb
import socket
# import sys
# import os


#
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import Pyro5.api
import Pyro5.socketutil
import Pyro5.nameserver

from Servidor.model.sql_connect.sql import SQLConnection
from model import *

if __name__ == "__main__":

    # Utils
    hostname = socket.gethostname()
    my_ip = Pyro5.socketutil.get_ip_address(hostname, workaround127=True)

    # Start SQL connection
    sql = SQLConnection()
    sql.connect()

    # # Run NameServer
    # try:
    #     nameserverUri, nameserverDaemon, broadcastServer = Pyro5.nameserver.start_ns(my_ip, 9090)
    #     assert broadcastServer is not None, "expect a broadcast server to be created"
    #     print (f"Nameserver running at: {nameserverUri}")
    # except Exception as e:
    #     print(e)
    #     exit(1)

    # Expose classes to Pyro5
    aluno_exp = Pyro5.api.expose(Aluno)
    avaliacao_exp = Pyro5.api.expose(Avaliacao)
    disciplina_exp = Pyro5.api.expose(Disciplina)
    frequencia_exp = Pyro5.api.expose(Frequencia)

    # Starting RMI server

    Pyro5.api.serve({
        aluno_exp:  "Aluno",
        avaliacao_exp: "Avaliacao",
        disciplina_exp: "Disciplina",
        frequencia_exp: "Frequencia"
    }, host=my_ip, port=9090, use_ns=False)


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
    nameserverDaemon.close()
    broadcastServer.close()
    print("done")