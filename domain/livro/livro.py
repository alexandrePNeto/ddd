from domain.livro.value_object.status_livro import StatusLivro


class Livro:

    def __init__(self, id, titulo, autor, status):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.status = status

    def criar(self) -> "Livro":
        pass

    def emprestar(self):
        pass

    def devolver(self):
        pass

    def reservar(self):
        pass

    def esta_disponivel(self):
        pass