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
        self.usuario: Usuario = None
        self.multa: Multa | None = None
        self.status: StatusEmprestimo = None
        self.periodo: PeriodoEmprestimo | None = None

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
