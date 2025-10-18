from abc import abstractmethod


class AlunoInterface:

    @abstractmethod
    def select(self):
        raise NotImplementedError

    @abstractmethod
    def inserir(self, matricula: int, nome: str, idade: int, periodo: int):
        raise NotImplementedError

    @abstractmethod
    def pesquisar(self, matricula: int) -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    def editar(self, matricula: int, nome: str, idade: int, periodo: int):
        raise NotImplementedError

    @abstractmethod
    def remover(self, matricula: int):
        raise NotImplementedError
