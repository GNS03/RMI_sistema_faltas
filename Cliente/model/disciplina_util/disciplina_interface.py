from abc import abstractmethod


class DisciplinaInterface:

    @abstractmethod
    def select(self):
        raise NotImplementedError

    @abstractmethod
    def inserir(self, id: int, nome: str, horas: int):
        raise NotImplementedError

    @abstractmethod
    def pesquisar(self, id: int) -> list[dict]:
        raise NotImplementedError

    @abstractmethod
    def editar(self, id: int, nome: str, horas: int):
        raise NotImplementedError

    @abstractmethod
    def remover(self, id: int):
        raise NotImplementedError
