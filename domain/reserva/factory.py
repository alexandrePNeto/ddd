from uuid import (
    UUID,
    uuid4
)

from domain.livro.livro import Livro
from domain.usuario.usuario import Usuario

from domain.exception import DomainException

from domain.reserva.reserva import Reserva
from domain.reserva.value_object.status_reserva import StatusReserva

from domain.services.disponibilidade_livro_service import DisponibilidadeLivroService

class ReservaFactory:

    @classmethod
    def criar(
        cls,
        livro: Livro,
        usuario: Usuario,
        disponibilidade_service: DisponibilidadeLivroService
    ) -> Reserva:

        if disponibilidade_service.pode_ser_emprestado(livro):
            raise DomainException("O livro está disponível para empréstimo e não precisa ser reservado.")

        if usuario.possui_pendencias():
            raise DomainException("Um usuário com pendência não pode realizar uma reserva.")

        return Reserva.criar(
            id=cls._gerar_id(),
            livro=livro,
            usuario=usuario,
            status=StatusReserva.PENDENTE
        )

    @classmethod
    def _gerar_id(cls) -> UUID:
        return uuid4()