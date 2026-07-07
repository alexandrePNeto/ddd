from uuid import UUID

from domain.usuario.usuario import Usuario
from domain.usuario.repository.usuario_repository import UsuarioRepository


class UsuarioRepositoryMemory(UsuarioRepository):

    def __init__(self):
        self._usuarios: dict[UUID, Usuario] = {}

    def salvar(self, usuario: Usuario) -> None:
        self._usuarios[usuario.id] = usuario

    def buscar(self, id: UUID) -> Usuario | None:
        return self._usuarios.get(id)

    def atualizar(self, usuario: Usuario) -> None:
        self._usuarios[usuario.id] = usuario

    def deletar(self, usuario: Usuario) -> None:
        self._usuarios.pop(usuario.id, None)
