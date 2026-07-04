from domain.emprestimo.emprestimo import Emprestimo

from domain.emprestimo.value_object.status_emprestimo import StatusEmprestimo

class PodeRealizarEmprestimoSpecification:

    LIMITE_EMPRESTIMOS: int = 1

    @classmethod
    def pode_realizar_emprestimo(cls, emprestimo: Emprestimo) -> bool:
        if not emprestimo or not isinstance(emprestimo, Emprestimo):
            raise ValueError("Empréstimo inválido.")

        if emprestimo.status != StatusEmprestimo.ABERTO:
            return False

        if emprestimo.usuario.status.BLOQUEADO:
            return False

        if emprestimo.usuario.status.COM_PENDENCIA:
            return False

        if len(emprestimo.usuario.emprestimo) >= cls.LIMITE_EMPRESTIMOS:
            return False

        if not emprestimo.livro.status.ESTA_DISPONIVEL:
            return False

        return True
