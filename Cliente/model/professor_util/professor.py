class Professor:

    def __init__(self, id: int = 0, nome: str = ""):

        self.id = id
        self.nome = nome

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
        }
