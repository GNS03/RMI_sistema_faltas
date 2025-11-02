This project uses the Remote Method Invocation(RMI) protocol to communicate between the Client, the Server and the Database (MySQL).

To run this project you'll need Python 3.11 or higher installed, and a MySQL server running.

Start by clone this repository to your local drive with:

`git clone https://github.com/GNS03/RMI_sistema_faltas.git`

Run the MySQL query (.sql file) in your MySQL server, it should create a new database called "escola" (Make sure MySQL user and password are "root")

Now, install the python libraries with PiP:

`python3 pip install -r requirements.txt`

With everything installed run `server.py` first and then set the ip that appears in .env, run `python_gui.py`

