from abc import ABC, abstractmethod

from domain.emprestimo.emprestimo import Emprestimo


class EmprestimoRepository(ABC):
    @abstractmethod
    def salvar(self, emprestimo: Emprestimo) -> None:
        pass


    @abstractmethod
    def buscar(self, emprestimo: Emprestimo) -> Emprestimo | None:
        pass


    @abstractmethod
    def atualizar(self, emprestimo: Emprestimo) -> None:
        pass


    @abstractmethod
    def deletar(self, emprestimo: Emprestimo) -> None:
        pass
