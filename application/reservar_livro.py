from uuid import UUID

from domain.exception import DomainException

from domain.livro.repository.livro_repository import LivroRepository
from domain.usuario.repository.usuario_repository import UsuarioRepository
from domain.reserva.repository.reserva_repository import ReservaRepository

from domain.reserva.factory import ReservaFactory

from domain.services.disponibilidade_livro_service import DisponibilidadeLivroService


def reservar_livro(
    livro_id: UUID,
    usuario_id: UUID,
    livro_repository: LivroRepository,
    usuario_repository: UsuarioRepository,
    reserva_repository: ReservaRepository,
    disponibilidade_service: DisponibilidadeLivroService
):

    livro = livro_repository.buscar(livro_id)

    if livro is None:
        raise DomainException("Livro não encontrado.")

    usuario = usuario_repository.buscar(usuario_id)

    if usuario is None:
        raise DomainException("Usuário não encontrado.")

    reserva = ReservaFactory.criar(
        livro=livro,
        usuario=usuario,
        disponibilidade_service=disponibilidade_service
    )

    livro.reservar()

    reserva_repository.salvar(reserva)
    livro_repository.atualizar(livro)

    return reserva