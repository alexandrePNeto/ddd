from uuid import (
    SafeUUID,
    UUID
)

# Value Objects
from domain.emprestimo.value_object.periodo_emprestimo import PeriodoEmprestimo
from domain.emprestimo.value_object.status_emprestimo import StatusEmprestimo
from domain.emprestimo.value_object.multa import Multa

# Exceptions
from domain.exception import DomainException

# Aggregates
from domain.livro.livro import Livro
from domain.usuario.usuario import Usuario

# Policies
from domain.emprestimo.policy.multa import MultaPolicy


class Emprestimo:

    def __init__(self):
        self.id: int = None
        self.livro: Livro = None
        self.multa: Multa  = None
        self.usuario: Usuario = None
        self.status: StatusEmprestimo = None
        self.periodo: PeriodoEmprestimo = None

    @classmethod
    def criar(
        cls,
        id: UUID,
        livro: Livro,
        usuario: Usuario,
        status: StatusEmprestimo,
        periodo: PeriodoEmprestimo
    ) -> "Emprestimo":
        if not id or not isinstance(id, UUID) or id.is_safe != SafeUUID.safe:
            raise DomainException("ID é inválido para processeguir")

        if not livro or not isinstance(livro, Livro):
            raise DomainException("Livro deve ser válido para iniciar um empréstimo")

        if not usuario or not isinstance(usuario, Usuario):
            raise DomainException("Usuario deve ser válido para iniciar um empréstimo")

        if not status or not isinstance(status, StatusEmprestimo):
            raise DomainException("Status de emprestimo deve ser válido para iniciar um empréstimo")

        if not periodo or not isinstance(periodo, PeriodoEmprestimo):
            raise DomainException("Periodo de emprestimo deve ser válido para iniciar um empréstimo")

        emprestimo: "Emprestimo" = cls()

        emprestimo.livro = livro
        emprestimo.usuario = usuario
        emprestimo.status = status
        emprestimo.periodo = periodo
        emprestimo.multa = Multa.criar(0, "")

        return emprestimo

    def atualizar_status(self) -> None:
        if self.status == StatusEmprestimo.FINALIZADO:
            return

        if self.esta_atrasado():
            self.atrasar_emprestimo()

    def finalizar(self) -> None:
        if self.status == StatusEmprestimo.FINALIZADO:
            raise DomainException("Empréstimo já está finalizado.")

        if self.esta_atrasado():
            self.atrasar_emprestimo()
            return

        self.status = self.status.atualizar(self.status, StatusEmprestimo.FINALIZADO)

    def atrasar_emprestimo(self) -> None:
        self.status = self.status.atualizar(self.status, StatusEmprestimo.ATRASADO)
        self.multa = MultaPolicy.calcular_multa(self.periodo.dias_de_atraso())

    def esta_atrasado(self) -> bool:
        if self.status == StatusEmprestimo.FINALIZADO:
            return False

        if not self.periodo.esta_atrasado():
            return False

        return True

    def esta_finalizado(self) -> bool:
        return self.status == StatusEmprestimo.FINALIZADO
