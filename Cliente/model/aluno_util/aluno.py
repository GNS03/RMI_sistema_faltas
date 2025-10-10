class Aluno:

    def __init__(self, matricula: int = 0, nome: str = "", idade: int = 0, periodo: int = 0, disciplinas_matriculadas=None):

        if disciplinas_matriculadas is None:
            disciplinas_matriculadas = []

        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.periodo = periodo
        self.disciplinas_matriculadas: list[int] = disciplinas_matriculadas

    def hello(self):
        print(f"Hello {self.nome}")