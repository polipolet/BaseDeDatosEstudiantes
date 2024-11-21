from abc import ABC

class Criterio(ABC):
    """
    Clase abstracta superclase de los criterios concretos.
     - Es una clase abstracta.  Los criterios de búsqueda se implementarán como subclases
     - El método se_cumple(fila) es abstracto y se debe implementar en las subclases
    """

    ##@var nombre_clave
    # string: nombre de la clave con el que está mapeado el valor cuyo cumplimiento con el criterio se desea evaluar
    #
    ##@var valor_a_comparar
    # string: valor con el que se compara el valor de la fila pasada como argumento, mapeado con la clave cuyo nombre es  nombre_clave
    #

    ##@brief
    # Constructor.
    #Asigna al atributo nombre_clave el valor pasado en el argumento nombre_clave.
    #Asigna al atributo valor_a_comparar el valor pasado en el argumento valor_a_comparar.
    #
    #@param nombre_clave el nombre de la clave sobre la que se aplicará el criterio
    #@param valor_a_comparar valor del atributo valor_a_comparar. El método se_cumple(fila) comparará el valor mapeado
    # con la clave nombre_clave con dicho atributo o con el valor numérico por él representado (depende de la subclase)
    # para determinar si se cumple el criterio o no
    #
    def __init__(self,nombre_clave,valor_a_comparar):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Criterio::__init__(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Retorna True si el criterio se cumple para la
    # fila pasada como argumento, es decir, si la fila tiene una pareja
    # [nombre de clave, valor de clave] cuya clave (nombre de clave) es el mismo que
    # el atributo nombre_clave y cuyo valor (valor de clave)
    # cumple las condiciones especificadas en el método (a implementar por las subclases)
    # respecto al atributo valor_a_comparar.
    #
    # <p>En caso de que la fila pasada como argumento no contenga ninguna pareja con la clave
    # buscada, devuelve False si el atributo valor_a_comprobar es
    # distinto de None y devuelve True si el atributo valor_a_comprobar es
    # None.</p>
    #
    # @param fila objeto FilaDatos a comprobar si cumple con el criterio
    #
    # @return True si:
    #  - la fila pasada tiene una pareja con la clave buscada que cumple el criterio,
    #  - la fila pasada NO tiene una pareja con la clave buscada que cumple el criterio y el atributo valor_a_comprobar es None
    # @return False si:
    #  - la fila pasada tiene una pareja con la clave buscada que NO cumple el criterio,
    #  - la fila pasada NO tiene una pareja con la clave buscada que cumple el criterio y el atributo valor_a_comprobar NO es None
    #
    def se_cumple(self,fila):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Criterio::se_cumple(...) NO SE HA IMPLEMENTADO")
