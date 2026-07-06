from enum import Enum

from domain.exception import DomainException

class StatusReserva(Enum):
    PENDENTE: str = "PENDENTE"
    ATENDIDA: str = "ATENDIDA"
    CANCELADA: str = "CANCELADA"

    @classmethod
    def atualizar(cls, status: "StatusReserva", novo: "StatusReserva") -> "StatusReserva":
        if status not in (
            cls.ATENDIDA,
            cls.CANCELADA
        ):
            return novo

        if novo == cls.PENDENTE:
            raise DomainException(f"Uma reserva em {status.name} não pode ser alterada para {novo.value}")

        return novo
