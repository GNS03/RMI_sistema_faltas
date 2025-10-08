from Cliente.model import Aluno
from Cliente.model.aluno_util.aluno_interface import AlunoInterface


class AlunoController(AlunoInterface):

    def __init__(self):
        raise NotImplemented

    def inserir(self, aluno: Aluno):
        pass

    def pesquisar(self, matricula: int) -> Aluno:
        pass

    def editar(self, aluno: Aluno):
        pass

    def remover(self, matricula: int):
        pass




