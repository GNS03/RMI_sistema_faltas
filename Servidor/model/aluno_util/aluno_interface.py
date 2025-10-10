from abc import abstractmethod

from Servidor.model import Aluno


class AlunoInterface:

    @abstractmethod
    def inserir(self, matricula: int, nome: str, idade: int, periodo: int):
        raise NotImplementedError

    @abstractmethod
    def pesquisar(self, matricula: int) -> Aluno:
        raise NotImplementedError

    @abstractmethod
    def editar(self, matricula: int, nome: str, idade: int, periodo: int):
        raise NotImplementedError

    @abstractmethod
    def remover(self, matricula: int):
        raise NotImplementedError
