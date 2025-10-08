from abc import abstractmethod

from Cliente.model import Aluno


class AlunoInterface:

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
