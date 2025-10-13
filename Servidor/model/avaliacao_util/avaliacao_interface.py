from abc import abstractmethod


class AvaliacaoInterface:

    @abstractmethod
    def inserir(self, id: int, disciplina_k: int, aluno_k: int):
        raise NotImplementedError

    @abstractmethod
    def pesquisar(self, id: int) -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    def editar(self, id: int, disciplina_k: int, aluno_k: int):
        raise NotImplementedError

    @abstractmethod
    def remover(self, id: int):
        raise NotImplementedError
