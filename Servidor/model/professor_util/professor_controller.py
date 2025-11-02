from .. import Professor
from ..professor_util.professor_interface import ProfessorInterface
from ..sql_connect import sql_execute


class ProfessorController(ProfessorInterface):

    def __init__(self):
        pass

    def select(self):
        op = "Select"

        sql_str = "SELECT * FROM professor"  # no params needed

        professores = sql_execute(op, sql_str, fetch=True)

        return professores

    def inserir(self, id: int, nome: str):
        op = "Insert"

        professor = Professor(id, nome)

        params = {
            "id": professor.id,
            "nome": professor.nome,
        }

        sql_str = "INSERT INTO professor (id, nome) VALUES (%(id)s, %(nome)s)"

        return sql_execute(op, sql_str, params, fetch=False)

    def pesquisar(self, id: int) -> list[dict]:
        op = "Search"

        params = {"id": id}

        sql_str = "SELECT id, nome FROM professor WHERE id = %(id)s"
        professores = sql_execute(op, sql_str, params, fetch=True)

        return professores

    def editar(self, id: int, nome: str):
        op = "Edit"

        novo = {
            "id": id,
            "nome": nome,
        }

        # Pega os valores atuais da professor
        print(f"Pegando valores da id: {id}")
        professor = self.pesquisar(id)[0]

        # Se os valores passados para a funcao forem diferentes de None, substitui o valor atual
        for key, value in professor.items():
            if novo.get(key) is not None:
                professor[key] = novo.get(key)

        params = professor

        sql_str = "UPDATE professor SET nome = %(nome)s WHERE id = %(id)s"

        return sql_execute(op, sql_str, params, fetch=False)

    def remover(self, id: int):
        op = "Delete"

        params = {"id": id}

        sql_str = "DELETE FROM professor WHERE id = %(id)s"

        return sql_execute(op, sql_str, params, fetch=False)


if __name__ == "__main__":
    prof_controller = ProfessorController()
    print(prof_controller.select())
