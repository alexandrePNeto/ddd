from domain.emprestimo.value_object.multa import Multa

class MultaPolicy:

    VALOR_POR_DIA = 2.50

    def calcular_multa(self, dias_atraso):

        if dias_atraso <= 0:
            return Multa.criar(0, "Empréstimo não está atrasado.")

        return Multa.criar(
            valor=dias_atraso * self.VALOR_POR_DIA,
            motivo=f"Empréstimo está atrasado a {dias_atraso} dia{'' if dias_atraso == 1 else 's'}."
        )