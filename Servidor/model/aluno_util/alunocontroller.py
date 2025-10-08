from Servidor.model import Aluno
from Servidor.model.aluno_util.aluno_interface import AlunoInterface


class AlunoController(AlunoInterface):

    def __init__(self):
        raise NotImplemented

    def inserir(self, aluno: Aluno):
        sql_command = f"insert into aluno(matricula, nome, idade)"

    def pesquisar(self, matricula: int) -> Aluno:
        pass

    def editar(self, aluno: Aluno):
        pass

    def remover(self, matricula: int):
        pass




