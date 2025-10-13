class Avaliacao:
    def __init__(self, id: int, disciplina_k: int, aluno_k: int):

        self.id = id
        self.disciplina_k = disciplina_k
        self.aluno_k = aluno_k

    def to_dict(self):
        return {
            "id": self.id,
            "disciplina_k": self.disciplina_k,
            "aluno_k": self.aluno_k,
        }
