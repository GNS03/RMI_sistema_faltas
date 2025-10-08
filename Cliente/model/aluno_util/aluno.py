class Aluno:

    def __init__(self, matricula: int = 0, nome: str = "", idade: int = 0):

        self.matricula = matricula
        self.nome = nome
        self.idade = idade

    def hello(self):
        print("Hello")