from domain.livro.livro import Livro
from domain.reserva.reserva import Reserva

from domain.reserva.repository.reserva_repository import ReservaRepository


class FilaReservaService:

    def __init__(
        self,
        reserva_repository: ReservaRepository
    ):
        self._reserva_repository = reserva_repository

    def atender_proxima_reserva(
        self,
        livro: Livro
    ) -> Reserva | None:

        if not livro.esta_disponivel():
            return None

        reservas: list[Reserva] | None = self._reserva_repository.buscar_reservas_pendentes_por_livro(livro)

        if not reservas:
            return None

        proxima_reserva: Reserva = reservas[0]

        proxima_reserva.atender()

        return proxima_reserva
