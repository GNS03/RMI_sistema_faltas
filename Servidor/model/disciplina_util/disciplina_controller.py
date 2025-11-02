from .. import Disciplina
from ..disciplina_util.disciplina_interface import DisciplinaInterface
from ..sql_connect import sql_execute


class DisciplinaController(DisciplinaInterface):

    def __init__(self):
        pass

    def select(self):
        op = "Select"

        sql_str = "SELECT * FROM disciplina"  # no params needed

        disciplinas = sql_execute(op, sql_str, fetch=True)

        return disciplinas

    def inserir(self, id: int, nome: str, horas: int):
        op = "Insert"

        disciplina = Disciplina(id, nome, horas)

        params = {
            "id": disciplina.id,
            "nome": disciplina.nome,
            "horas": disciplina.horas,
        }

        sql_str = "INSERT INTO disciplina (id, nome, horas) VALUES (%(id)s, %(nome)s, %(horas)s)"

        return sql_execute(op, sql_str, params, fetch=False)

    def pesquisar(self, id: int) -> list[dict]:
        op = "Search"

        params = {"id": id}

        sql_str = "SELECT id, nome, horas FROM disciplina WHERE id = %(id)s"
        disciplinas = sql_execute(op, sql_str, params, fetch=True)

        return disciplinas

    def editar(self, id: int, nome: str, horas: int):
        op = "Edit"

        novo = {
            "id": id,
            "nome": nome,
            "horas": horas,
        }

        # Pega os valores atuais da disciplina
        print(f"Pegando valores da id: {id}")
        disciplina = self.pesquisar(id)[0]

        # Se os valores passados para a funcao forem diferentes de None, substitui o valor atual
        for key, value in disciplina.items():
            if novo.get(key) is not None:
                disciplina[key] = novo.get(key)

        params = disciplina

        sql_str = (
            "UPDATE disciplina SET nome = %(nome)s, horas = %(horas)s WHERE id = %(id)s"
        )

        return sql_execute(op, sql_str, params, fetch=False)

    def remover(self, id: int):
        op = "Delete"

        params = {"id": id}

        sql_str = "DELETE FROM disciplina WHERE id = %(id)s"

        return sql_execute(op, sql_str, params, fetch=False)


if __name__ == "__main__":
    disc_controller = DisciplinaController()
    print(disc_controller.select())
