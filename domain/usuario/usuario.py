from domain.usuario.value_object.status_usuario import StatusUsuario


class Usuario:

    def __init__(self):
        self.id = None
        self.nome = None
        self.status = None
        self.emprestimos = None

    def criar(self) -> "Usuario":
        pass

    def bloquear(self):
        pass

    def desbloquear(self):
        pass

    def possui_pendencias(self):
        pass

    def pode_realizar_emprestimo(self):
        pass