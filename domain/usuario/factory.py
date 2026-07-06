from uuid import (
    UUID,
    uuid4
)

from domain.usuario.usuario import Usuario
from domain.usuario.value_object.status_usuario import StatusUsuario


class UsuarioFactory:

    @classmethod
    def criar(
        cls,
        nome: str
    ) -> Usuario:

        return Usuario.criar(
            id=cls._gerar_id(),
            nome=nome,
            status=StatusUsuario.ATIVO
        )

    @classmethod
    def _gerar_id(cls) -> UUID:
        return uuid4()