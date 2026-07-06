from domain.livro.livro import Livro

from domain.reserva.repository.reserva_repository import ReservaRepository
from domain.emprestimo.repository.emprestimo_repository import EmprestimoRepository

class DisponibilidadeLivroService:

    def __init__(
        self,
        emprestimo_repository: EmprestimoRepository,
        reserva_repository: ReservaRepository
    ):
        self._emprestimo_repository = emprestimo_repository
        self._reserva_repository = reserva_repository

    def pode_ser_emprestado(self, livro: Livro) -> bool:

        if not livro.esta_disponivel():
            return False

        if self._emprestimo_repository.buscar_emprestimos_ativos_por_livro(livro):
            return False

        if self._reserva_repository.buscar_reservas_pendentes_por_livro(livro):
            return False

        return True
