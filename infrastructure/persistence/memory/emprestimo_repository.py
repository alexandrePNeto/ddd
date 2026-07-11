from uuid import UUID

from domain.livro.livro import Livro
from domain.emprestimo.emprestimo import Emprestimo
from domain.emprestimo.repository.emprestimo_repository import EmprestimoRepository

class EmprestimoRepositoryMemory(EmprestimoRepository):

    def __init__(self):
        self._emprestimos: dict[UUID, Emprestimo] = {}

    def salvar(self, emprestimo: Emprestimo):
        self._emprestimos[emprestimo.id] = emprestimo

    def buscar(self, id: UUID):
        return self._emprestimos.get(id)

    def atualizar(self, emprestimo: Emprestimo):
        self._emprestimos[emprestimo.id] = emprestimo

    def deletar(self, emprestimo: Emprestimo):
        self._emprestimos.pop(emprestimo.id, None)

    def buscar_emprestimos_ativos_por_livro(self, livro: Livro):
      return [
        emprestimo
        for emprestimo in self._emprestimos.values()
        if emprestimo.livro.id == livro.id and emprestimo.esta_ativo()
    ]
