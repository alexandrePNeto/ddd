from enum import Enum

from domain.exception import DomainException


class StatusLivro(Enum):
    DISPONIVEL: str = "DISPONIVEL"
    EMPRESTADO: str = "EMPRESTADO"
    RESERVADO: str = "RESERVADO"

    @classmethod
    def atualizar(cls, atual: "StatusLivro", novo: "StatusLivro") -> "StatusLivro":

        if atual == novo:
            raise DomainException("O livro já possui este status.")

        if atual == cls.EMPRESTADO and novo == cls.RESERVADO:
            raise DomainException(
                "Um livro emprestado não pode ser reservado diretamente."
            )

        return novo
