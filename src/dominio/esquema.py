
from src.dominio.excepcionesDominio import ClaveYaExisteException
from src.utils.string_builder import StringBuilder

class Esquema:
    """
    Clase Esquema.
    Indica la estructura de una Tabla, es decir: qué claves tiene ésta y, para cada clave, si es única o no.
    """
    ##@var campos
    #mapa. La clave de cada entrada del mapa es el nombre de una Clave de la base de datos;
    #el valor de cada entrada entrada del mapa es el objeto Clave en cuestión.

    ##@brief
    # Constructor. Instancia un nuevo esquema vacío (sin claves)
    #
    def __init__(self):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Esquema::__init__(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Retorna True si el esquema contiene una clave cuyo nombre
    # coincide con el argumento nombre
    #
    # @param nombre nombre de la clave a buscar
    # @return True si el esquema contiene una clave cuyo nombre
    # coincide con el argumento nombre. False en caso
    # contrario
    #
    def contiene_clave(self,nombre_clave):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Esquema::contiene_clave(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Añade una clave al esquema
    #
    # - Si el esquema contiene una clave con ese nombre, lanza la excepción ClaveYaExisteException
    # - Si no es así, añade la clave al mapa (mapea la clave con su nombre)
    #
    # @param clave clave a añadir al esquema
    # @exception ClaveYaExisteException en caso de que ya exista una clave con ese nombre en el esquema
    #
    def add_clave(self,clave):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Esquema::add_clave(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Crea, construye y retorna una nueva lista con las claves del esquema
    #
    # @return la nueva lista con las claves del esquema
    #
    def get_lista_de_claves(self):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Esquema::get_lista_de_claves(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Devuelve el número de campos del esquema
    # @return
    #
    def get_num_campos(self):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Esquema::get_num_campos(...) NO SE HA IMPLEMENTADO")

    ##@brief
    #Genera un string con una representación textual de los contenidos del Esquema.
    #**MUY IMPORTANTE:** \n
    # - ESTE MÉTODO SE DA HECHO.\n
    # - EL CORRECTOR AUTOMÁTICO UTILIZA LOS STRINGS GENERADOS POR ESTE MÉTODO.\n
    # - POR TANTO, NO DEBÉIS MODIFICARLO.\n
    # - SI LO HACÉIS EL CORRECTOR AUTOMÁTICO NO FUNCIONARÁ CORRECTAMENTE.\n
    #
    def __str__(self):
        result = "Esquema["
        i = 0
        for item in self.campos.items():
            if i!=0:
                result +=','
            result +=str(item[1])
            i += 1
        result += "]"
        return result

    ##@brief
    # Crea un nuevo esquema vacío.
    # **MUY IMPORTANTE:** \n
    # - ESTE MÉTODO SE DA HECHO.\n
    # - EL CORRECTOR AUTOMÁTICO UTILIZA LOS STRINGS GENERADOS POR ESTE MÉTODO.\n
    # - POR TANTO, NO DEBÉIS MODIFICARLO.\n
    # - SI LO HACÉIS EL CORRECTOR AUTOMÁTICO NO FUNCIONARÁ CORRECTAMENTE.\n
    #
    @staticmethod
    def crea_esquema_vacio():
        return Esquema()
    ##@brief
    #Compara los contenidos de este esquema con otro y presenta información en caso de que no
    #sean los mismos, identificando en qué lugar se ha detectado la primera desigualdad
    #**MUY IMPORTANTE:** \n
    # - ESTE MÉTODO SE DA HECHO.\n
    # - EL CORRECTOR AUTOMÁTICO UTILIZA LOS STRINGS GENERADOS POR ESTE MÉTODO.\n
    # - POR TANTO, NO DEBÉIS MODIFICARLO.\n
    # - SI LO HACÉIS EL CORRECTOR AUTOMÁTICO NO FUNCIONARÁ CORRECTAMENTE.\n
    #
    def compara_esquema(self,otra,tabs,mensaje):
        ob_name = "Esquema\n"
        indentado = tabs + "  "
        if len(self.campos)!=len(otra.campos):
            mensaje.append(tabs).append(ob_name)\
            .append(indentado).append("Razón: el número de campos de esta es ").append(str(len(self.campos)))\
                .append("; el número de campos de la otra es ").append(str(len(otra.campos))).append("\n")
            return False
        report = StringBuilder()
        for clave in self.campos:
            valor_esta = self.campos.get(clave)
            valor_otra = otra.campos.get(clave)
            if not valor_esta.compara_clave(valor_otra,indentado,report):
                mensaje.append(tabs).append(ob_name).append(report.to_string())
                return False
        return True
