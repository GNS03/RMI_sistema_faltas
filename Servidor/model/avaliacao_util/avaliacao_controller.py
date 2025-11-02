from .. import Avaliacao
from ..avaliacao_util.avaliacao_interface import AvaliacaoInterface
from ..sql_connect import sql_execute


class AvaliacaoController(AvaliacaoInterface):

    def __init__(self):
        pass

    def select(self):
        op = "Select"

        sql_str = "SELECT * FROM avaliacao"  # no params needed

        avaliacoes = sql_execute(op, sql_str, fetch=True)

        return avaliacoes

    def inserir(self, id: int, disciplina_fk: int, aluno_fk: int, nota: float):
        op = "Insert"

        avaliacao = Avaliacao(id, disciplina_fk, aluno_fk, nota)

        params = {
            "id": avaliacao.id,
            "disciplina_fk": avaliacao.disciplina_fk,
            "aluno_fk": avaliacao.aluno_fk,
            "nota": avaliacao.nota,
        }

        sql_str = (
            "INSERT INTO avaliacao (id, disciplina_fk, aluno_fk, nota) VALUES (%(id)s, %(disciplina_fk)s, "
            "%(aluno_fk)s, %(nota)s)"
        )

        return sql_execute(op, sql_str, params, fetch=False)

    def pesquisar(self, id: int) -> list[dict]:
        op = "Search"

        params = {"id": id}

        sql_str = (
            "SELECT id, disciplina_fk, aluno_fk, nota FROM avaliacao WHERE id = %(id)s"
        )
        avaliacoes = sql_execute(op, sql_str, params, fetch=True)

        return avaliacoes

    def editar(self, id: int, disciplina_fk: int, aluno_fk: int, nota: float):
        op = "Edit"

        novo = {
            "id": id,
            "disciplina_fk": disciplina_fk,
            "aluno_fk": aluno_fk,
            "nota": nota,
        }

        # Pega os valores atuais da avaliacao
        print(f"Pegando valores da id: {id}")
        avaliacao = self.pesquisar(id)[0]

        # Se os valores passados para a funcao forem diferentes de None, substitui o valor atual
        for key, value in avaliacao.items():
            if novo.get(key) is not None:
                avaliacao[key] = novo.get(key)

        params = avaliacao

        sql_str = (
            "UPDATE avaliacao SET disciplina_fk = %(disciplina_fk)s, aluno_fk = %(aluno_fk)s, nota = %(nota)s "
            "WHERE id = %(id)s"
        )

        return sql_execute(op, sql_str, params, fetch=False)

    def remover(self, id: int):
        op = "Delete"

        params = {"id": id}

        sql_str = "DELETE FROM avaliacao WHERE id = %(id)s"

        return sql_execute(op, sql_str, params, fetch=False)


if __name__ == "__main__":
    av_controller = AvaliacaoController()
    print(av_controller.select())
