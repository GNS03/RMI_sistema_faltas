from Servidor.model import Avaliacao
from Servidor.model.avaliacao_util.avaliacao_interface import AvaliacaoInterface
from Servidor.model.sql_connect import sql_execute


class AvaliacaoController(AvaliacaoInterface):

    def __init__(self):
        pass

    def inserir(self, id: int, disciplina_k: int, aluno_k: int):
        op = "Insert"

        avaliacao = Avaliacao(id, disciplina_k, aluno_k)

        params = {
            "id": avaliacao.id,
            "disciplina_k": avaliacao.disciplina_k,
            "aluno_k": avaliacao.aluno_k,
        }

        sql_str = "INSERT INTO avaliacao (id, disciplina_k, aluno_k) VALUES (%(id)s, %(disciplina_k)s, %(aluno_k)s)"
        sql_execute(op, sql_str, params, fetch=False)

        return True

    def pesquisar(self, id: int) -> list[dict]:
        op = "Search"

        params = {"id": id}

        sql_str = "SELECT id, disciplina_k, aluno_k FROM avaliacao WHERE id = %(id)s"
        avaliacoes = sql_execute(op, sql_str, params, fetch=True)

        return avaliacoes

    def editar(self, id: int, disciplina_k: int, aluno_k: int):
        op = "Edit"

        novo = {
            "id": id,
            "disciplina_k": disciplina_k,
            "aluno_k": aluno_k,
        }

        # Pega os valores atuais da avaliacao
        print(f"Pegando valores da id: {id}")
        avaliacao = self.pesquisar(id)[0]

        # Se os valores passados para a funcao forem diferentes de None, substitui o valor atual
        for key, value in avaliacao.items():
            if novo.get(key) is not None:
                avaliacao[key] = novo.get(key)

        params = avaliacao

        sql_str = "UPDATE avaliacao SET disciplina_k = %(disciplina_k)s, aluno_k = %(aluno_k)s WHERE id = %(id)s"
        sql_execute(op, sql_str, params, fetch=False)

        return True

    def remover(self, id: int):
        op = "Delete"

        avaliacao = Avaliacao(id)

        params = {"id": avaliacao.id}

        sql_str = "DELETE FROM avaliacao WHERE id = %(id)s"
        sql_execute(op, sql_str, params, fetch=False)

        return True
