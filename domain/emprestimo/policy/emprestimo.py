class EmprestimoPolicy:

    @classmethod
    def limite_emprestimos(cls) -> int:
        return 1

    @classmethod
    def prazo_dias(cls) -> int:
        return 15

    @classmethod
    def renovacoes_permitidas(cls) -> int:
        return 1