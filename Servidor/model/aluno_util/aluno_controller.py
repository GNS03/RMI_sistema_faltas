from Servidor.model import Aluno  # , clear_screen
from Servidor.model.aluno_util.aluno_interface import AlunoInterface
from Servidor.model.sql_connect.sql import sql_execute


class AlunoController(AlunoInterface):

    def __init__(self):
        pass

    def select(self):
        op = "Select"

        sql_str = "SELECT * FROM aluno"  # no params needed

        alunos = sql_execute(op, sql_str, fetch = True)

        return alunos

    def inserir(self, matricula: int, nome: str, idade: int, periodo: int) -> bool | list[dict]:
        op = "Insert"

        aluno = Aluno(matricula, nome, idade, periodo)

        params = {
            "matricula": aluno.matricula,
            "nome":      aluno.nome,
            "idade":     aluno.idade,
            "periodo":   aluno.periodo,
            }

        sql_str = (
            "INSERT INTO aluno (matricula, nome, idade, periodo) VALUES (%(matricula)s, %(nome)s, %(idade)s, "
            "%(periodo)s)"
        )

        return sql_execute(op, sql_str, params, fetch = False)

    # Nao e serializavel, ent tem q usar dict
    def pesquisar(self, matricula: int) -> None | list[dict]:
        op = "Search"

        # TODO: pesquisar por nome?

        params = {"matricula": matricula}

        sql_str = "SELECT matricula, nome, idade, periodo FROM aluno WHERE matricula = %(matricula)s"
        alunos = sql_execute(op, sql_str, params, fetch = True)

        return alunos

    def editar(
            self, matricula: int, nome: str = None, idade: int = None, periodo: int = None,
            ) -> bool | list[dict]:
        op = "Edit"

        novo = {
            "matricula": matricula,
            "nome":      nome,
            "idade":     idade,
            "periodo":   periodo,
            }

        # Pega os valores atuais do aluno
        print(f"Pegando valores da matricula: {matricula}")
        aluno = self.pesquisar(matricula)[0]

        # Se os valores passados para a funcao forem diferentes de None, substitui o valor atual
        for key, value in aluno.items():
            if novo.get(key) is not None:
                aluno[key] = novo.get(key)

        params = aluno

        sql_str = (
            "UPDATE aluno SET nome = %(nome)s, idade = %(idade)s, periodo = %(periodo)s "
            "WHERE "
            "matricula "
            "= %(matricula)s"
        )

        return sql_execute(op, sql_str, params, fetch = False)

    def remover(self, matricula: int, nome: str = None, idade: int = None, periodo: int = None) -> bool | list[dict]:
        op = "Delete"

        aluno = Aluno(matricula)

        params = {"matricula": aluno.matricula}

        sql_str = "DELETE FROM aluno WHERE matricula = %(matricula)s"

        return sql_execute(op, sql_str, params, fetch = False)


if __name__ == "__main__":
    aluno_controller = AlunoController()
    print(aluno_controller.select())
