from abc import abstractmethod

from domain.repository import Repository

from domain.usuario.usuario import Usuario


class UsuarioRepository(Repository[Usuario]):

    @abstractmethod
    def buscar_por_nome(self, nome: str) -> Usuario | None:
        pass