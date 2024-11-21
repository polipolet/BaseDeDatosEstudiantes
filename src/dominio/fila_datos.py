from src.dominio.excepcionesDominio import ClaveInexistenteException
from src.utils.string_builder import StringBuilder

class FilaDatos:
    """
    # Clase que representa una fila de datos dentro de una Tabla. Cada
    # fila de datos es un conjunto de claves-valor, cuya clave representa el nombre
    # de una columna, y el valor será el contenido de esa columna para la fila
    # dada
    """
    ##@var claves_valor
    #Mapa de parejas [nombre de clave, valor de la clave] para la fila de datos

    ##@brief
    # Constructor sin argumentos. Crea un nuevo mapa claves_valor vacío.
    #
    def __init__(self):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("FilaDatos::__init__(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Añade un par [nombre de clave,valor] al mapa claves_valor
    #
    # @param nombre_clave Nombre de la clave (columna de la Tabla donde se añadirá)
    # @param valor Valor que tendrá la columna para la fila dada (valor mapeado con
    # nombre nombre_clave en la fila
    #
    def put(self,nombre_clave,valor):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("FilaDatos::put(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Retorna el valor mapeado con el nombre_clave en la fila de datos si
    # existe una clave con ese nombre. Returna None en caso contrario.
    #
    # @param nombre_clave Nombre de la clave (columna de la Tabla para la fila en cuestión)
    # @return Valor de la columna para la fila dada si existe una clave con el
    # nombre igual al argumento (valor mapeado con nombre_clave en la fila); devuelve None en caso contrario
    #
    def get(self,nombre_clave):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("FilaDatos::get(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Comprueba si la fila es válida para dicho esquema.
    # Una fila NO será válida:
    #  - Si el número de columnas de la fila NO COÍNCIDE con el número de campos del esquema, O
    #  - Si el número de columnas de la fila  COÍNCIDE con el número de campos del esquema Y hay alguna clave
    #  en la fila pasada cuyo nombre no está definido como clave dentro del ESQUEMA pasado como argumento
    #
    # Si no se cumple ninguna de las dos condiciones anteriores, la fila SERÁ VÁLIDA
    #
    # Si la fila NO es válida, lanza una excepción ClaveInexistenteException creada pasándole a su
    #constructor el nombre de la clave en la que se ha detectado el problema.
    #
    # Si la fila es válida para el esquema pasado como argumento, el método
    # acaba sin problemas (NO DEVUELVE NADA).
    #
    # @param esquema el Esquema sobre el que validar la fila.
    # @exception ClaveInexistenteException si la fila de datos NO ES VÁLIDA
    #
    def valida(self,esquema):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("FilaDatos::valida(...) NO SE HA IMPLEMENTADO")

    ##@brief
    #Genera un string con una representación textual de un objeto FilaDatos.
    #**MUY IMPORTANTE:** \n
    # - ESTE MÉTODO SE DA HECHO.\n
    # - EL CORRECTOR AUTOMÁTICO UTILIZA LOS STRINGS GENERADOS POR ESTE MÉTODO.\n
    # - POR TANTO, NO DEBÉIS MODIFICARLO.\n
    # - SI LO HACÉIS EL CORRECTOR AUTOMÁTICO NO FUNCIONARÁ CORRECTAMENTE.\n
    #
    def __str__(self):
        result = "FilaDatos["
        i = 0
        for item in self.claves_valor.items():
            if i != 0:
                result +=','
            result +=item[0]+":"+item[1]
            i+=1
        result +="]"
        return result

    ##@brief
    # Crea una nueva fila de datos vacía.
    # **MUY IMPORTANTE:** \n
    # - ESTE MÉTODO SE DA HECHO.\n
    # - EL CORRECTOR AUTOMÁTICO UTILIZA LOS STRINGS GENERADOS POR ESTE MÉTODO.\n
    # - POR TANTO, NO DEBÉIS MODIFICARLO.\n
    # - SI LO HACÉIS EL CORRECTOR AUTOMÁTICO NO FUNCIONARÁ CORRECTAMENTE.\n
    #
    @staticmethod
    def crea_fila_vacia():
        return FilaDatos()

    ##@brief
    #Compara los contenidos de esta fila de datos con otra y presenta información en caso de que no
    #sean los mismos, identificando en qué lugar se ha detectado la primera desigualdad
    #**MUY IMPORTANTE:** \n
    # - ESTE MÉTODO SE DA HECHO.\n
    # - EL CORRECTOR AUTOMÁTICO UTILIZA LOS STRINGS GENERADOS POR ESTE MÉTODO.\n
    # - POR TANTO, NO DEBÉIS MODIFICARLO.\n
    # - SI LO HACÉIS EL CORRECTOR AUTOMÁTICO NO FUNCIONARÁ CORRECTAMENTE.\n
    #
    def compara_fila(self,otra,tabs,mensaje,num):
        ob_name = "Fila(" + str(num) +")\n"
        indentado = tabs + "  "
        if len(self.claves_valor)!=len(otra.claves_valor):
            mensaje.append(tabs).append(ob_name)\
            .append(indentado).append("Razón: el número de filas de esta es ").append(str(len(self.claves_valor)))\
                .append("; el número de filas de la otra es ").append(str(len(otra.claves_valor))).append("\n")
            return False
        for clave in self.claves_valor:
            valor_esta = self.claves_valor.get(clave)
            valor_otra = otra.claves_valor.get(clave)
            if valor_esta!=valor_otra:
                mensaje.append(tabs).append(ob_name) \
                    .append(indentado).append("Razón: el valor en esta para la clave ").append(clave).append(" es ")\
                    .append(valor_esta).append("; el el valor en la otra para dicha clave es ")\
                    .append(valor_otra).append("\n")
                return False
        return True


class ComparadorFilas:
    """
    Una clase que implementa que compara dos objetos FilaDatos.
    Esta clase se utilizará como clase auxiliar para ordenar las filas
    de una tabla según los valores de una clave dada, tanto en orden ascendente como descendente.
    """
    ##@var clave_a_comparar
    # String: nombre de la clave de la tabla con la que se llevará a cabo la comparación.
    #
    clave_a_comparar = None

    ##@brief
    #Método de clase (estático) que signa al atributo clave_a_comparar el valor pasado como argumento
    #
    #@param clave_a_comparar string con el valor a asignar al atributo clave_a_comparar
    #
    def set_clave(clave_a_comparar):
        ComparadorFilas.clave_a_comparar = clave_a_comparar

    ##@brief
    #Método de clase (estático) que compara 2 filas.
    #Este método compara los valores mapeados con las clave cuyo nombre coíncide con el
    #atributo clave_a_comparar
    #
    #@param una_fila una de las filas a comparar
    #@param otra_fila la otra fila a comparar
    #@return
    # - <0 si una de las filas tiene la clave por la que comparar y otra no.
    # - 0 si ninguna de ellas tiene la clave por la que comparar.
    # - >0 si ambas tienen la clave por la que comparar y el valor mapeado con
    #      la clave en una_fila es MAYOR que el valor mapeado con la clave en otra_fila.
    # - 0 si ambas tienen la clave por la que comparar y el valor mapeado con
    #      la clave en una_fila es IGUAL que el valor mapeado con la clave en otra_fila.
    # - <0 si ambas tienen la clave por la que comparar y el valor mapeado con
    #      la clave en una_fila es MENOR que el valor mapeado con la clave en otra_fila.
    def compare(una_fila,otra_fila):
        una_fila_str = una_fila.get(ComparadorFilas.clave_a_comparar)
        otra_fila_str = otra_fila.get(ComparadorFilas.clave_a_comparar)
        una_fila_has_key = una_fila_str != None
        otra_fila_has_key = otra_fila_str != None
        if not una_fila_has_key and otra_fila_has_key:
            return -1
        if una_fila_has_key and not otra_fila_has_key:
            return -1
        if not una_fila_has_key and not otra_fila_has_key:
            return 0
        #Las dos filas tienen la clave
        try:
            una_fila_numero = float(una_fila_str)
            otra_fila_numero = float(otra_fila_str)
            return una_fila_numero - otra_fila_numero
        except:
            return (una_fila_str > otra_fila_str) - (una_fila_str < otra_fila_str)
