from abc import abstractmethod


class AvaliacaoInterface:

    @abstractmethod
    def select(self):
        raise NotImplementedError

    @abstractmethod
    def inserir(self, id: int, disciplina_fk: int, aluno_fk: int, nota: float):
        raise NotImplementedError

    @abstractmethod
    def pesquisar(self, id: int) -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    def editar(self, id: int, disciplina_fk: int, aluno_fk: int, nota: float):
        raise NotImplementedError

    @abstractmethod
    def remover(self, id: int):
        raise NotImplementedError
