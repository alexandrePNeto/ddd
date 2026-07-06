from abc import abstractmethod

from domain.repository import Repository

from domain.livro.livro import Livro

class LivroRepository(Repository[Livro]):

    @abstractmethod
    def buscar_por_titulo(self, titulo: str) -> list[Livro]:
        pass