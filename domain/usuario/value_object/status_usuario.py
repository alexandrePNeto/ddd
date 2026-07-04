from enum import Enum

from domain.exception import DomainException


class StatusUsuario(Enum):
    ATIVO: str = "ATIVO"
    BLOQUEADO: str = "BLOQUEADO"
    COM_PENDENCIA: str = "COM_PENDENCIA"

    @classmethod
    def atualizar(cls, atual: "StatusUsuario", novo: "StatusUsuario") -> "StatusUsuario":

        if atual == novo:
            raise DomainException("O usuário já possui este status.")

        if atual == cls.BLOQUEADO and novo == cls.COM_PENDENCIA:
            raise DomainException("Usuário bloqueado não pode voltar para pendente.")

        return novo