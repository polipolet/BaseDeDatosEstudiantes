from src.dominio.criterios.criterio import  Criterio


class CriterioMayorQue(Criterio):
    """
    Para valores que pueden convertirse a números ,
    esta clase los compara y comprueba que el valor buscado en una fila dada es mayor al valor númerido del atributo valor_a_comparar,
    que se guarda en el atributo valor_numerico_a_comparar
    """
    ##@var valor_numerico_a_comparar
    #float: valor numérico del atributo valor_a_comparar, obtenido mediante la aplicación de la función float a
    #dicho atributo, según la expresión:
    # self.valor_numerico_a_comparar = float(self.valor_numerico)
    #

    ##@brief
    #Constructor. El método:
    # - Invoca al constructor de la superclase con los dos argumentos.
    # - Asigna al atributo valor_numerico_a_comparar el valor numérico representado en el atributo valor_a_comparar
    #usando la expresión mostrada en la descripción del atributo valor_numerico_a_comparar
    #
    #El argumento valor_a_comparar DEBE ser la representación textual de un número
    #
    #@param nombre_clave el nombre de la clave sobre la que se aplicará el criterio
    #@param valor_a_comparar valor del atributo valor_a_comparar. El método se_cumple(fila) comparará el valor mapeado
    # con la clave nombre_clave en la fila pasada como argumento, con el valor numérico de dicho atributo (el calculado valor_numerico_a_comparar)
    # para determinar si se cumple el criterio o no
    #
    def __init__(self,nombre_clave,valor_a_comparar):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("CriterioMayorQue::__init__(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Convierte a número el valor la  propiedad de la fila pasada como argumento, cuyo nombre
    # es igual al atributo nombre_clave de este objeto CriterioMayor. Esta conversión se realiza usando la función float(...) tal y como se indica en
    # la documentación del constructor
    #
    # Acto seguido compara el valor numérico obtenido en el paso anterior con el atributo valor_numerico_a_comparar.
    # Devuelve True si el valor obtenido es ESTRICTAMENTE MAYOR que dicho atributo. Devuelve False en caso contrario.
    #
    #Si el valor de la propiedad de la fila pasada como argumento NO puede convertirse a un número, devuelve False.
    #
    # Tened en cuenta que en tal caso, la invocación a la función float(...) puede lanzarnos una excepción, que
    # debe capturarse en el método para, como parte del procesado de la captura, retornar False.
    #
    # @param f Fila sobre la cual comprobar si se cumple el criterio
    # @return True si el criterio se cumple. False en caso contrario
    #
    def se_cumple(self,fila):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("CriterioMayorQue::se_cumple(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Genera un string con una representación textual de los contenidos de la base
    # de datos.
    # **MUY IMPORTANTE:** \n
    # - ESTE MÉTODO SE DA HECHO.\n
    # - NO DEBÉIS MODIFICARLO.\n
    #
    def __str__(self):
        return f"CriterioMayorQue<{self.nombre_clave},{self.valor_a_comparar},{self.valor_numerico_a_comparar}>"