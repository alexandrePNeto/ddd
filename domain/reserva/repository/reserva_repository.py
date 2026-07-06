from abc import abstractmethod

from domain.livro.livro import Livro
from domain.reserva.reserva import Reserva

from domain.repository import Repository


class ReservaRepository(Repository[Reserva]):

    @abstractmethod
    def buscar_reservas_pendentes_por_livro(
        self,
        livro: Livro
    ) -> list[Reserva]:
        pass