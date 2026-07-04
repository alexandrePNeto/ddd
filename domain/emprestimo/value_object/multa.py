from domain.emprestimo.emprestimo import Emprestimo
from domain.emprestimo.value_object.periodo_emprestimo import PeriodoEmprestimo

class Multa:
    def __init__(self):
        self.valor: float = 0.0
        self.motivo: str = ""

    @classmethod
    def criar(cls, valor: float, motivo: str) -> "Multa":
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("O valor da multa deve ser um número não negativo.")

        if not isinstance(motivo, str):
            raise ValueError("O motivo da multa deve ser uma string.")

        multa = cls()
        multa.valor = valor
        multa.motivo = motivo

        return multa