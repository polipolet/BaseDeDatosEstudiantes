from src.dominio.excepcionesDominio import ValorClaveUnicaException
from src.dominio.fila_datos import ComparadorFilas
from functools import cmp_to_key
from src.utils.string_builder import StringBuilder

class Tabla:
    """
    Clase cuyos objetos guardan y gestionan la información de una tabla: su nombre, un objeto Esquema y
    una lista de objetos FilaDatos.
    """

    ##@var nombre
    # string: nombre de la tabla
    #
    ##@var esquema
    # Esquema: objeto Esquema que indica la estructura de la tabla, es decir, qué columnas
    # tiene y si los valores de estas columnas deben ser únicos o no
    #
    ##@var filas
    # lista de objetos FilaDatos: los datos en cuestión. Cada objeto FilaDatos indica una entrada en la
    # tabla.
    #

    ##@brief
    # Constructor. Instancia la clase Tabla:
    # - Asigna al atributo nombre el valor pasado en el argumento nombre
    # - Asigna al atributo esquema el valor del argumento esquema
    # - Crea una lista vacía de filas
    #
    # @param nombre el nombre de la tabla
    # @param esquema el esquema de la tabla
    #
    def __init__(self,nombre,esquema):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Tabla::__init__(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Añade una fila de datos a la tabla.
    # Lanza una excepción si no se ha
    # podido añadir dicha fila. Eso sucede en uno de estos casos:
    # - La clave única ha sido violada: se ha insertado un dato en una
    # columna marcada como clave única, y ya existía en la tabla
    # una fila con ese mismo valor mapeado a esa clave.
    #  - La fila no es válida conforme al esquema de la tabla.
    #
    #Nota: recordad que en FilaDatos existe el método FilaDatos::valida()
    #
    # @param fila_datos Fila de datos a insertar
    # @exception ValorClaveUnicaException Si se ha violado la clave única
    # @exception ClaveInexistenteException Si en la fila se define una clave no
    # existente en el esquema
    #
    def anyade(self,fila_datos):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Tabla::anyade(...) NO SE HA IMPLEMENTADO")


    ##@brief
    # Devuelve una lista con todas las filas de la tabla. Debe ser
    # UNA COPIA de la lista, no la lista original.
    #
    # @return Devuelve una lista con todas las {@link FilaDatos} de la tabla.
    #
    def busca_todo(self):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Tabla::busca_todo(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Devuelve una lista con todas las filas de la tabla que
    # cumplen el criterio pasado por argumento.
    #
    # Si el argumento es None, deberá devolver el mismo resultado
    # que el método Tabla::busca_todo()</p>
    #
    # @param criterio Criterio que deben cumplir las filas devueltas.
    # @return una lista con todas las listas de la tabla que cumplen
    # el criterio pasado por argumento.
    #
    def busca(self,criterio):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Tabla::busca(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # ELIMINA DE LA TABLA todas las filas que cumplen el criterio
    # pasado por parámetro y DEVUELVE UNA LISTA CON LAS FILAS ELIMINADAS.</p>
    #
    # Si el criterio es None, no eliminará nada y devuelve una
    # lista vacía.
    #
    # @param criterio Criterio que deben cumplir las filas eliminadas.
    #
    # @return una lista con todas las filas eliminadas de la tabla
    # o una lista vacía si no ha eliminado ninguna.
    #
    def elimina(self,criterio):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Tabla::elimina(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Retorna el esquema de la tabla
    #
    # @return el esquema de la tabla
    #
    def get_esquema(self):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Tabla::get_esquema(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Retorna una lista con los nombres de las claves de la tabla tal y como
    # aparecen en su esquema
    #
    # @return Una lista con los nombres de las claves de la tabla
    #
    def get_cabeceras(self):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Tabla::get_cabeceras(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Ordena la lista de filas según una columna (identificada por columna_a_ordenar) dada, en orden ascendente o
    # descendente
    #
    #**MUY IMPORTANTE:** \n
    # - ESTE MÉTODO SE DA HECHO.\n
    # - EL CORRECTOR AUTOMÁTICO UTILIZA LOS STRINGS GENERADOS POR ESTE MÉTODO.\n
    # - POR TANTO, NO DEBÉIS MODIFICARLO.\n
    # - SI LO HACÉIS EL CORRECTOR AUTOMÁTICO NO FUNCIONARÁ CORRECTAMENTE.\n
    #
    #
    # @param columnaAOrdenar La columna por la cual se debe ordenar la tabla
    # @param reverse Si es True se ordena en orden descendente. Si es False se ordena en orden ascendente.
    #
    def ordena(self,columna_a_ordenar,reverse):
        ComparadorFilas.set_clave(columna_a_ordenar)
        self.filas.sort(key =cmp_to_key(ComparadorFilas.compare),reverse=not reverse)

    ##@brief
    # Método de clase (estático) sin argumentos. Instancia la clase Tabla:
    # - Asigna al atributo nombre el valor None
    # - Asigna al atributo esquema el valor None
    #
    #**MUY IMPORTANTE:** \n
    # - ESTE MÉTODO SE DA HECHO.\n
    # - EL CORRECTOR AUTOMÁTICO UTILIZA LOS STRINGS GENERADOS POR ESTE MÉTODO.\n
    # - POR TANTO, NO DEBÉIS MODIFICARLO.\n
    # - SI LO HACÉIS EL CORRECTOR AUTOMÁTICO NO FUNCIONARÁ CORRECTAMENTE.\n
    #
    @staticmethod
    def crear_sin_argumentos():
        return Tabla(None,None)

    ##@brief
    #Genera un string con una representación textual de un objeto Tabla.
    #**MUY IMPORTANTE:** \n
    # - ESTE MÉTODO SE DA HECHO.\n
    # - EL CORRECTOR AUTOMÁTICO UTILIZA LOS STRINGS GENERADOS POR ESTE MÉTODO.\n
    # - POR TANTO, NO DEBÉIS MODIFICARLO.\n
    # - SI LO HACÉIS EL CORRECTOR AUTOMÁTICO NO FUNCIONARÁ CORRECTAMENTE.\n
    #
    def __str__(self):
        result = "Tabla<"
        if len(self.nombre)!=0:
            result += f"\'{self.nombre}\'"
            if self.esquema is not None:
                result += f",{self.esquema}"
        if len(self.filas) != 0:
            result += ","
        i = 0
        for fila in self.filas:
            if i!=0:
                result += ','
            result += str(fila)
            i += 1
        result += '>'
        return result


    ##@brief
    #Compara los contenidos de esta tabla con otra y presenta información en caso de que no
    #sean los mismos, identificando en qué lugar se ha detectado la primera desigualdad
    #**MUY IMPORTANTE:** \n
    # - ESTE MÉTODO SE DA HECHO.\n
    # - EL CORRECTOR AUTOMÁTICO UTILIZA LOS STRINGS GENERADOS POR ESTE MÉTODO.\n
    # - POR TANTO, NO DEBÉIS MODIFICARLO.\n
    # - SI LO HACÉIS EL CORRECTOR AUTOMÁTICO NO FUNCIONARÁ CORRECTAMENTE.\n
    #
    def compara_tabla(self,otra,tabs,mensaje):
        ob_name = "Tabla[" + self.nombre +"]\n"
        indentado = tabs + "  "
        report = StringBuilder()
        if self.nombre!=otra.nombre:
            mensaje.append(tabs).append(ob_name)\
            .append(indentado).append("Razón: nombre de esta es ").append(self.nombre)\
                .append("; nombre de la otra es ").append(otra.nombre).append("\n")
            return False
        if not self.esquema.compara_esquema(otra.esquema,indentado,report):
            mensaje.append(tabs).append(ob_name).append(report.to_string())
            return False;
        num_filas = len(self.filas)
        if num_filas!=len(otra.filas):
            mensaje.append(tabs).append(ob_name)\
            .append(indentado).append("Razón: el número de filas de esta es ").append(str(len(self.filas)))\
                .append("; el número de filas de la otra es ").append(str(len(otra.filas))).append("\n")
            return False
        for i in range(0,num_filas):
            if not self.filas[i].compara_fila(otra.filas[i],indentado,report,i):
                mensaje.append(tabs).append(ob_name).append(report.to_string())
                return False;
        return True
