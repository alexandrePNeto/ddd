class DomainException(Exception):
    """Exceção base para erros de domínio."""

    def __init__(self, message: str):
        super().__init__(f"Exceção de domínio: {message}")
