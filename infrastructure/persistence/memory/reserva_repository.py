from uuid import UUID

from domain.reserva.reserva import Reserva
from domain.reserva.repository.reserva_repository import ReservaRepository

class ReservaRepositoryMemory(ReservaRepository):

    def __init__(self):
        self._reservas: dict[UUID, Reserva] = {}

    def salvar(self, reserva: Reserva):
        self._reservas[reserva.id] = reserva

    def buscar(self, id: UUID):
        return self._reservas.get(id)

    def atualizar(self, reserva: Reserva):
        self._reservas[reserva.id] = reserva

    def deletar(self, reserva: Reserva):
        self._reservas.pop(reserva.id, None)
