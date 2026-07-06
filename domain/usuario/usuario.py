from uuid import UUID

from domain.exception import DomainException

from domain.usuario.value_object.status_usuario import StatusUsuario


class Usuario:

    def __init__(self):
        self.id: str | None = None
        self.nome: str | None = None
        self.status: StatusUsuario | None = None
        self.emprestimos: list = []

    @classmethod
    def criar(
        cls,
        id: UUID,
        nome: str,
        status: StatusUsuario
    ) -> "Usuario":

        if not id or not isinstance(id, UUID):
            raise DomainException("ID inválido para o usuário.")

        if not nome or not nome.strip():
            raise DomainException("Nome do usuário é obrigatório.")

        if not status or not isinstance(status, StatusUsuario):
            raise DomainException("Status do usuário é inválido.")

        usuario = cls()

        usuario.id = id
        usuario.nome = nome.strip()
        usuario.status = status
        usuario.emprestimos = []

        return usuario

    def bloquear(self) -> None:
        if self.status == StatusUsuario.BLOQUEADO:
            raise DomainException("O usuário já está bloqueado.")

        self.status = self.status.atualizar(
            self.status,
            StatusUsuario.BLOQUEADO
        )

    def desbloquear(self) -> None:
        if self.status != StatusUsuario.BLOQUEADO:
            raise DomainException("O usuário não está bloqueado.")

        self.status = self.status.atualizar(
            self.status,
            StatusUsuario.ATIVO
        )

    def marcar_com_pendencia(self) -> None:
        if self.status == StatusUsuario.BLOQUEADO:
            raise DomainException(
                "Usuário bloqueado não pode voltar para pendência."
            )

        self.status = self.status.atualizar(
            self.status,
            StatusUsuario.COM_PENDENCIA
        )

    def remover_pendencia(self) -> None:
        if self.status != StatusUsuario.COM_PENDENCIA:
            raise DomainException("O usuário não possui pendências.")

        self.status = self.status.atualizar(
            self.status,
            StatusUsuario.ATIVO
        )

    def possui_pendencias(self) -> bool:
        return self.status == StatusUsuario.COM_PENDENCIA

    def esta_bloqueado(self) -> bool:
        return self.status == StatusUsuario.BLOQUEADO

    def pode_realizar_emprestimo(self) -> bool:
        return self.status == StatusUsuario.ATIVO

    def adicionar_emprestimo(self, emprestimo) -> None:
        self.emprestimos.append(emprestimo)

    def remover_emprestimo(self, emprestimo) -> None:
        self.emprestimos.remove(emprestimo)