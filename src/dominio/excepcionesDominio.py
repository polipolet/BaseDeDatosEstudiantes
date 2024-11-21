
class BaseDatosException(Exception):
    def __init__(self,mssg):
        super().__init__(mssg)

class ClaveYaExisteException(BaseDatosException):
    def __init__(self,mssg):
        super().__init__(mssg)

class ClaveInexistenteException(BaseDatosException):
    def __init__(self,nombre_clave):
        super().__init__("")
        self.nombre_clave = nombre_clave

    def get_nombre_clave(self):
        return self.nombre_clave

class TablaInexistenteException(BaseDatosException):
    def __init__(self,nombre_tabla):
        super().__init__("")
        self.nombre_tabla = nombre_tabla

    def get_nombre_tabla(self):
        return self.nombre_tabla

class ValorClaveUnicaException(BaseDatosException):
    def __init__(self,nombre_clave,valor_duplicado):
        super().__init__("")
        self.nombre_clave = nombre_clave
        self.valor_duplicado = valor_duplicado

    def get_nombre_clave(self):
        return self.nombre_clave

    def get_valor_duplicado(self):
        return self.valor_duplicado

class MetodoNoImplementadoException(Exception):
    def __init__(self,mssg):
        super().__init__(mssg)
