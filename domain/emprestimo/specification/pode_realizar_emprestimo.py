from domain.emprestimo.emprestimo import Emprestimo

from domain.emprestimo.value_object.status_emprestimo import StatusEmprestimo

from domain.emprestimo.policy.emprestimo import EmprestimoPolicy

from domain.exception import DomainException

class PodeRealizarEmprestimoSpecification:

    @classmethod
    def satisfaz(cls, emprestimo: Emprestimo) -> bool:
        if not emprestimo or not isinstance(emprestimo, Emprestimo):
            raise DomainException("Empréstimo inválido.")

        if emprestimo.status != StatusEmprestimo.ABERTO:
            return False

        if not emprestimo.usuario.pode_realizar_emprestimo():
            return False

        if len(emprestimo.usuario.emprestimos) > EmprestimoPolicy.limite_emprestimos():
            return False

        if not emprestimo.livro.esta_disponivel():
            return False

        if emprestimo.periodo.esta_atrasado():
            return False

        return True
