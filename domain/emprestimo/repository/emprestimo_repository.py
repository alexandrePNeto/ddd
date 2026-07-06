from abc import abstractmethod

from domain.livro.livro import Livro
from domain.emprestimo.emprestimo import Emprestimo

from domain.repository import Repository


class EmprestimoRepository(Repository[Emprestimo]):

    @abstractmethod
    def buscar_emprestimos_ativos_por_livro(
        self,
        livro: Livro
    ) -> list[Emprestimo]:
        pass