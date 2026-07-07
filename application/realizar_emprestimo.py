from uuid import UUID

from domain.exception import DomainException

from domain.livro.repository.livro_repository import LivroRepository
from domain.usuario.repository.usuario_repository import UsuarioRepository
from domain.emprestimo.repository.emprestimo_repository import EmprestimoRepository

from domain.emprestimo.factory import EmprestimoFactory
from domain.emprestimo.value_object.periodo_emprestimo import PeriodoEmprestimo


def realizar_emprestimo(
    livro_id: UUID,
    usuario_id: UUID,
    periodo: PeriodoEmprestimo,
    livro_repository: LivroRepository,
    usuario_repository: UsuarioRepository,
    emprestimo_repository: EmprestimoRepository
):

    livro = livro_repository.buscar(livro_id)

    if livro is None:
        raise DomainException("Livro não encontrado.")

    usuario = usuario_repository.buscar(usuario_id)

    if usuario is None:
        raise DomainException("Usuário não encontrado.")

    emprestimo = EmprestimoFactory.criar(
        livro=livro,
        usuario=usuario,
        periodo=periodo
    )

    livro.emprestar()

    usuario.emprestimos.append(emprestimo)

    emprestimo_repository.salvar(emprestimo)
    livro_repository.atualizar(livro)
    usuario_repository.atualizar(usuario)

    return emprestimo