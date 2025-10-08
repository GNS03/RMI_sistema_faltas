from Servidor.model import Disciplina


class Aluno:

    def __init__(self, matricula: int = 0, nome: str = "", idade: int = 0, disciplinas_matriculadas: list[Disciplina] = []):

        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.disciplinas_matriculadas: list[Disciplina] = disciplinas_matriculadas

    def hello(self):
        print("Hello")