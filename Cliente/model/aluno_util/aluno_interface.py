from abc import abstractmethod

from .. import Aluno


class AlunoInterface:

    @abstractmethod
    def select(self):
        raise NotImplementedError

    @abstractmethod
    def inserir(self, aluno: Aluno):
        raise NotImplementedError

    @abstractmethod
    def pesquisar(self, matricula: int) -> Aluno:
        raise NotImplementedError

    @abstractmethod
    def editar(self, aluno: Aluno):
        raise NotImplementedError

    @abstractmethod
    def remover(self, matricula: int):
        raise NotImplementedError
