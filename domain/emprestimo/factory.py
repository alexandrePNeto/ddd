from uuid import (
    uuid4,
    UUID
)

# Value Objects
from domain.emprestimo.value_object.periodo_emprestimo import PeriodoEmprestimo
from domain.emprestimo.value_object.status_emprestimo import StatusEmprestimo

# Exceptions
from domain.exception import DomainException

# Aggregates
from domain.livro.livro import Livro
from domain.usuario.usuario import Usuario
from domain.emprestimo.emprestimo import Emprestimo

# Policies
from domain.emprestimo.specification.pode_realizar_emprestimo import PodeRealizarEmprestimoSpecification


class EmprestimoFactory:

    @classmethod
    def criar(
        cls,
        livro: Livro,
        usuario: Usuario,
        periodo: PeriodoEmprestimo
    ) -> "Emprestimo":

        emprestimo: Emprestimo = Emprestimo.criar(
            id=cls._gerar_id(),
            livro=livro,
            usuario=usuario,
            periodo=periodo,
            status=StatusEmprestimo.ABERTO
        )

        if not PodeRealizarEmprestimoSpecification.satisfaz(emprestimo):
            raise DomainException("Não é possível realizar o empréstimo.")

        return emprestimo

    @classmethod
    def _gerar_id(cls) -> UUID:
        return uuid4()
