import socket

import Pyro5.api
import Pyro5.errors
import Pyro5.socketutil

from model import Aluno

if __name__ == "__main__":

    # Utils
    hostname = socket.gethostname()
    my_ip = Pyro5.socketutil.get_ip_address(hostname, workaround127=True)
    port = 9090
    print(f"Hostname = {hostname}, IP = {my_ip}, Port = {port}")

    # nameserver = Pyro5.api.locate_ns(host=my_ip, port=9090)
    # print("Nameserver found")

    classe = "Aluno"

    uri = f"PYRO:{classe}@{my_ip}:{port}"

    aluno = Pyro5.api.Proxy(uri)

    aluno.hello()
