from src.dominio.criterios.criterio import  Criterio


class CriterioIgual(Criterio):
    """
    # Clase que implementa el criterio "igual", en el que que el
    # el valor mapeado con nombre_clave en una cierta fila, ha de tener un valor
    # IGUAL al del atributo valor_a_comparar.
    """
    ##@brief
    #ConstructorEl métodoi invoca al constructor de la superclase con los dos argumentos.
    #
    #@param nombre_clave el nombre de la clave sobre la que se aplicará el criterio
    #@param valor_a_comparar valor del atributo valor_a_comparar. El método se_cumple(fila) comparará el valor mapeado
    # con la clave nombre_clave en la fila pasada como argumento, con dicho atributo (valor_a_comparar) para determinar si se cumple el criterio o no
    #
    def __init__(self,nombre_clave,valor_a_comparar):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("CriterioIgual::__init__(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Retorna True si el valor mapeado con la clave nombre_clave en
    # la fila pasada como argumento, es
    # IGUAL al del atributo valor_a_comparar de este objeto.
    #
    # @param fila Fila sobre la cual comprobar si se cumple el criterio
    # @return True si el criterio se cumple. False en caso contrario
    #
    def se_cumple(self,fila):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("CriterioIgual::se_cumple(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Genera un string con una representación textual de los contenidos de la base
    # de datos.
    # **MUY IMPORTANTE:** \n
    # - ESTE MÉTODO SE DA HECHO.\n
    # - NO DEBÉIS MODIFICARLO.\n
    #
    def __str__(self):
        return f"CriterioIgual<{self.nombre_clave},{self.valor_a_comparar}>"