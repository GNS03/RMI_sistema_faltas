import socket
import sys

import dotenv
from PyQt6.QtWidgets import QApplication

from GUI.app import MyApp


def get_server_ip():
    default_ip = dotenv.get_key(".env", "IP")  # IP fixo do servidor
    op = input(f"Digite o IP do servidor ou Enter para usar {default_ip}: ")

    return op or default_ip


dotenv.set_key(".env", "IP", get_server_ip())

if __name__ == "__main__":

    print("Starting...")

    print("Searching for pyro server...")

    # Utils
    hostname = socket.gethostname()
    my_ip = dotenv.get_key(".env", "IP")
    port = 9090

    # print(f"Ip found: {my_ip}")
    # op = input("Type a new Ip to change it or press enter to continue...\n")

    print(f"Found pyro server at: Hostname = {hostname}, IP = {my_ip}, Port = {port}")

    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
