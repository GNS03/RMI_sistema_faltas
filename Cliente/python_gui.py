import socket
import sys

import Pyro5.socketutil
from PyQt6.QtWidgets import QApplication

from Cliente.GUI.app import MyApp

if __name__ == "__main__":

    print("Starting...")

    print("Searching for pyro server...")

    # Utils
    hostname = socket.gethostname()
    my_ip = Pyro5.socketutil.get_ip_address(hostname, workaround127=True, version=4)
    port = 9090

    # classe = "..." # TODO: Add depending on which table is selected in view(1)
    #
    # uri = f"PYRO:{classe}@{my_ip}:{port}"
    #
    # try:
    #     control = Pyro5.api.Proxy(uri)
    # except Exception as e:
    #     raise e

    print(f"Found pyro server at: Hostname = {hostname}, IP = {my_ip}, Port = {port}")

    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())