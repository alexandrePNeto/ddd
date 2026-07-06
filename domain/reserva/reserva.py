from uuid import UUID
from datetime import datetime

from domain.usuario.usuario import Usuario
from domain.livro.livro import Livro

from domain.exception import DomainException

from domain.reserva.value_object.status_reserva import StatusReserva


class Reserva:

    def __init__(self, id, usuario, livro, data_reserva, status):
        self.id: UUID = id
        self.livro: Livro = livro
        self.usuario: Usuario = usuario
        self.status: StatusReserva = status
        self.data_reserva : datetime= data_reserva

    @classmethod
    def criar(
        cls,
        id: UUID,
        livro: Livro,
        usuario: Usuario,
        status: StatusReserva
    ) -> "Reserva":

        if not id or not isinstance(id, UUID):
            raise DomainException("ID inválido para a reserva.")

        if not livro or not isinstance(livro, Livro):
            raise DomainException("Livro inválido para a reserva.")

        if not usuario or not isinstance(usuario, Usuario):
            raise DomainException("Usuário inválido para a reserva.")

        if not status or not isinstance(status, StatusReserva):
            raise DomainException("Status da reserva é inválido.")

        reserva = cls()

        reserva.id = id
        reserva.livro = livro
        reserva.usuario = usuario
        reserva.status = status

        return reserva

    def atender(self) -> None:
        if self.status == StatusReserva.ATENDIDA:
            raise DomainException("A reserva já foi atendida.")

        if self.status == StatusReserva.CANCELADA:
            raise DomainException("Uma reserva cancelada não pode ser atendida.")

        self.status = self.status.atualizar(
            self.status,
            StatusReserva.ATENDIDA
        )

    def cancelar(self) -> None:
        if self.status == StatusReserva.CANCELADA:
            raise DomainException("A reserva já foi cancelada.")

        if self.status == StatusReserva.ATENDIDA:
            raise DomainException("Uma reserva atendida não pode ser cancelada.")

        self.status = self.status.atualizar(
            self.status,
            StatusReserva.CANCELADA
        )

    def esta_pendente(self) -> bool:
        return self.status == StatusReserva.PENDENTE

    def esta_atendida(self) -> bool:
        return self.status == StatusReserva.ATENDIDA

    def esta_cancelada(self) -> bool:
        return self.status == StatusReserva.CANCELADA