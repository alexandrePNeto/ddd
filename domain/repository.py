from abc import ABC, abstractmethod
from uuid import UUID


class Repository[T](ABC):

    @abstractmethod
    def salvar(self, entidade: T) -> None:
        pass

    @abstractmethod
    def buscar(self, id: UUID) -> T | None:
        pass

    @abstractmethod
    def atualizar(self, entidade: T) -> None:
        pass

    @abstractmethod
    def deletar(self, entidade: T) -> None:
        pass