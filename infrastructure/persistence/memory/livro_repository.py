from uuid import UUID

from domain.livro.livro import Livro
from domain.livro.repository.livro_repository import LivroRepository


class LivroRepositoryMemory(LivroRepository):

    def __init__(self):
        self._livros: dict[UUID, Livro] = {}

    def salvar(self, livro: Livro) -> None:
        self._livros[livro.id] = livro

    def buscar(self, id: UUID) -> Livro | None:
        return self._livros.get(id)

    def atualizar(self, livro: Livro) -> None:
        self._livros[livro.id] = livro

    def deletar(self, livro: Livro) -> None:
        self._livros.pop(livro.id, None)
