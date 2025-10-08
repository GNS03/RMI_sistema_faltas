import mysql.connector

class SQLConnection:

    def __init__(self, host: str = "localhost", user: str = "root", password: str = "root"):
        self.host = host
        self.user = user
        self.password = password
        self.db = self.connect()


    def connect(self):
        try:
            db = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )

            if db:
                print("Database connected succesfully")

            return db
        except Exception as e:
            print(e)

    def disconnect(self):
        self.db.close()
        print("Database connection closed")