from domain.reserva.value_object.status_reserva import StatusReserva

class Reserva:

    def __init__(self, id, usuario, livro, data_reserva, status):
        self.id = id
        self.usuario = usuario
        self.livro = livro
        self.data_reserva = data_reserva
        self.status: StatusReserva = status

    def criar(self) -> "Reserva":
        pass

    def atender(self):
        pass

    def cancelar(self):
        pass

    def esta_pendente(self):
        pass