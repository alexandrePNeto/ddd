from datetime import datetime, timedelta

from domain.exception import DomainException

class PeriodoEmprestimo:
    def __init__(self):
        self.data_inicio: datetime | None = None
        self.data_fim: datetime | None = None

    @classmethod
    def criar(cls, data_inicio: datetime, data_fim: datetime) -> "PeriodoEmprestimo":
        if data_fim <= data_inicio:
            raise DomainException("A data de fim deve ser posterior à data de início.")

        periodo: "PeriodoEmprestimo" = cls()
        periodo.data_inicio = data_inicio
        periodo.data_fim = data_fim

        return periodo


    def calcular_duracao(self) -> timedelta:
        return self.data_fim - self.data_inicio


    def dias_de_atraso(self) -> int:
        if not self.esta_atrasado():
            return 0

        return (datetime.now() - self.data_fim).days

    def esta_atrasado(self) -> bool:
        return datetime.now() > self.data_fim