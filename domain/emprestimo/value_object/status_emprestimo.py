from enum import Enum

from domain.exception import DomainException

class StatusEmprestimo(Enum):
    ABERTO: str = "ABERTO"
    ATRASADO: str = "ATRASADO"
    FINALIZADO: str = "FINALIZADO"

    @classmethod
    def atualizar(cls, status_atual: "StatusEmprestimo", novo_status: "StatusEmprestimo") -> "StatusEmprestimo":
        if status_atual == cls.FINALIZADO:
            raise DomainException("Não é possível alterar o status de um empréstimo finalizado.")

        if status_atual == cls.ATRASADO and novo_status == cls.ABERTO:
            raise DomainException("Não é possível alterar o status de um empréstimo atrasado para aberto.")

        return novo_status
