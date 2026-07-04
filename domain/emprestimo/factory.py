from uuid import uuid4

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
        if not livro or not isinstance(livro, Livro):
            raise DomainException("Livro inválido para empréstimo.")

        if not usuario or not isinstance(usuario, Usuario):
            raise DomainException("Usuário inválido para empréstimo.")

        if not periodo or not isinstance(periodo, PeriodoEmprestimo):
            raise DomainException("Período de empréstimo inválido.")

        emprestimo: Emprestimo = Emprestimo()

        emprestimo.id = cls._gerar_id()
        emprestimo.livro = livro
        emprestimo.usuario = usuario
        emprestimo.periodo = periodo
        emprestimo.status = StatusEmprestimo.ABERTO
        emprestimo.multa = None

        if not PodeRealizarEmprestimoSpecification.satisfaz(emprestimo):
            raise DomainException("Não é possível realizar o empréstimo.")

        return emprestimo

    @classmethod
    def _gerar_id(cls) -> str:
        return str(uuid4())
