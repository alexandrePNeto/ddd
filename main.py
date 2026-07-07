# APP
from application.reservar_livro import reservar_livro
from application.realizar_emprestimo import realizar_emprestimo

# Factories
from domain.livro.factory import LivroFactory
from domain.usuario.factory import UsuarioFactory

# VO's
from domain.emprestimo.value_object.periodo_emprestimo import (
    PeriodoEmprestimo
)

# Services
from domain.services.disponibilidade_livro_service import DisponibilidadeLivroService

# Repositórios implementados
from infrastructure.persistence.memory.livro_repository import LivroRepositoryMemory
from infrastructure.persistence.memory.usuario_repository import UsuarioRepositoryMemory
from infrastructure.persistence.memory.reserva_repository import ReservaRepositoryMemory
from infrastructure.persistence.memory.emprestimo_repository import EmprestimoRepositoryMemory

# ================================================================================================== #

# Repositories
livro_repository = LivroRepositoryMemory()
usuario_repository = UsuarioRepositoryMemory()
reserva_repository = ReservaRepositoryMemory()
emprestimo_repository = EmprestimoRepositoryMemory()

# Services
disponibilidade_service = DisponibilidadeLivroService(
    emprestimo_repository=emprestimo_repository,
    reserva_repository=reserva_repository
)

# ================================================================================================== #

# Criação das entidades, como se a gente mandasse um payload de json tanto faz

livro = LivroFactory.criar(
    titulo="Clean Architecture",
    autor="Robert C. Martin"
)

usuario1 = UsuarioFactory.criar(
    nome="Alexandre"
)

usuario2 = UsuarioFactory.criar(
    nome="Maria"
)


livro_repository.salvar(livro)
usuario_repository.salvar(usuario1)
usuario_repository.salvar(usuario2)

# ================================================================================================== #

# Emprétimos

emprestimo = realizar_emprestimo(
    livro_id=livro.id,
    usuario_id=usuario1.id,
    periodo=PeriodoEmprestimo.criar(15),
    livro_repository=livro_repository,
    usuario_repository=usuario_repository,
    emprestimo_repository=emprestimo_repository
)


print(emprestimo.id)
print(emprestimo.status)

# Reserva

reserva = reservar_livro(
    livro_id=livro.id,
    usuario_id=usuario2.id,
    livro_repository=livro_repository,
    usuario_repository=usuario_repository,
    reserva_repository=reserva_repository,
    disponibilidade_service=disponibilidade_service
)


print(reserva.id)
print(reserva.status)