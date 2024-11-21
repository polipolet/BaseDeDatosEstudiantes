from src.dominio.excepcionesDominio import BaseDatosException

class CorrectorException(BaseDatosException):
    def __init__(self,mssg):
        super().__init__(mssg)
