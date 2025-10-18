class Disciplina:

    def __init__(self, id: int = 0, nome: str = "", horas: int = 0):

        self.id = id
        self.nome = nome
        self.horas = horas

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "horas": self.horas,
        }
