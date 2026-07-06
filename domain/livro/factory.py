from uuid import (
    UUID,
    uuid4
)

from domain.livro.livro import Livro
from domain.livro.value_object.status_livro import StatusLivro


class LivroFactory:

    @classmethod
    def criar(
        cls,
        titulo: str,
        autor: str
    ) -> Livro:

        return Livro.criar(
            id=cls._gerar_id(),
            titulo=titulo,
            autor=autor,
            status=StatusLivro.DISPONIVEL
        )

    @classmethod
    def _gerar_id(cls) -> UUID:
        return uuid4()