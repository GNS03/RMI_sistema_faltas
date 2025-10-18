class Avaliacao:
    def __init__(self, id: int, disciplina_fk: int, aluno_fk: int, nota: float):

        self.id = id
        self.disciplina_fk = disciplina_fk
        self.aluno_fk = aluno_fk
        self.nota = nota

    def to_dict(self):
        return {
            "id": self.id,
            "disciplina_fk": self.disciplina_fk,
            "aluno_fk": self.aluno_fk,
            "nota": self.nota
        }
