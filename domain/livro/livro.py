from uuid import UUID

from domain.exception import DomainException

from domain.livro.value_object.status_livro import StatusLivro


class Livro:

    def __init__(self):
        self.id: UUID = None
        self.titulo: str = None
        self.autor: str = None
        self.status: StatusLivro = None

    @classmethod
    def criar(
        cls,
        id: UUID,
        titulo: str,
        autor: str,
        status: StatusLivro
    ) -> "Livro":

        if not id or not isinstance(id, UUID):
            raise DomainException("ID inválido para o livro.")

        if not titulo or not titulo.strip():
            raise DomainException("Título do livro é obrigatório.")

        if not autor or not autor.strip():
            raise DomainException("Autor do livro é obrigatório.")

        if not status or not isinstance(status, StatusLivro):
            raise DomainException("Status do livro é inválido.")

        livro = cls()

        livro.id = id
        livro.titulo = titulo.strip()
        livro.autor = autor.strip()
        livro.status = status

        return livro

    def emprestar(self) -> None:
        self.status = self.status.atualizar(
            self.status,
            StatusLivro.EMPRESTADO
        )

    def devolver(self) -> None:
        self.status = self.status.atualizar(
            self.status,
            StatusLivro.DISPONIVEL
        )

    def reservar(self) -> None:
        self.status = self.status.atualizar(
            self.status,
            StatusLivro.RESERVADO
        )

    def esta_disponivel(self) -> bool:
        return self.status == StatusLivro.DISPONIVEL