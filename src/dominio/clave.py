from src.utils.string_builder import StringBuilder

class Clave:
    """
    Clase Clave.
    Define los atributos y los métodos para gestionar una clave
    """
    ## @var nombre
    #  string con el nombre de la clave
    ## @var unica
    #  booleano que indica si la clave es única o no

    ##@brief Constructor de clave.
    #
    #@param nombre nombre de la clave
    #@param unica booleano que indica si es una clave unica (True) o no (False)
    #
    def __init__(self,nombre,es_unica):
        self.nombre = nombre
        self.unica = es_unica
        #hola

    ##@brief Retorna el nombre de la clave
    #
    #@return Nombre de la clave
    def get_nombre(self):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Clave::get_nombre(...) NO SE HA IMPLEMENTADO")

    ##@brief Retorna si la clave es única o no
    #
    #@return True si la clave es única; False en caso contrario
    def is_unica(self):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Clave::is_unica(...) NO SE HA IMPLEMENTADO")


    ##@brief
    #Genera un string con una representación textual de los contenidos de la clave.
    #**MUY IMPORTANTE:** \n
    # - ESTE MÉTODO SE DA HECHO.\n
    # - EL CORRECTOR AUTOMÁTICO UTILIZA LOS STRINGS GENERADOS POR ESTE MÉTODO.\n
    # - POR TANTO, NO DEBÉIS MODIFICARLO.\n
    # - SI LO HACÉIS EL CORRECTOR AUTOMÁTICO NO FUNCIONARÁ CORRECTAMENTE.\n
    #
    def __str__(self):
        return f'Clave({self.nombre};{self.unica})'

    ##@brief Método fábrica: crea una clave NO única con
    #el nombre pasado como argumento: el atributo unica se
    #pone a False
    #**MUY IMPORTANTE:** \n
    # - ESTE MÉTODO SE DA HECHO.\n
    # - EL CORRECTOR AUTOMÁTICO UTILIZA LOS STRINGS GENERADOS POR ESTE MÉTODO.\n
    # - POR TANTO, NO DEBÉIS MODIFICARLO.\n
    # - SI LO HACÉIS EL CORRECTOR AUTOMÁTICO NO FUNCIONARÁ CORRECTAMENTE.\n
    #
    #@param nombre nombre de la clave
    #
    @staticmethod
    def create_with_name_only(nombre):
        return Clave(nombre,False)

    ##@brief
    # Crea una nueva clave vacía.
    # **MUY IMPORTANTE:** \n
    # - ESTE MÉTODO SE DA HECHO.\n
    # - EL CORRECTOR AUTOMÁTICO UTILIZA LOS STRINGS GENERADOS POR ESTE MÉTODO.\n
    # - POR TANTO, NO DEBÉIS MODIFICARLO.\n
    # - SI LO HACÉIS EL CORRECTOR AUTOMÁTICO NO FUNCIONARÁ CORRECTAMENTE.\n
    #
    @staticmethod
    def crea_clave_vacia():
        return Clave(None,None)

    ##@brief
    #Compara los contenidos de esta clave con otra y presenta información en caso de que no
    #sean los mismos, identificando en qué lugar se ha detectado la primera desigualdad
    #**MUY IMPORTANTE:** \n
    # - ESTE MÉTODO SE DA HECHO.\n
    # - EL CORRECTOR AUTOMÁTICO UTILIZA LOS STRINGS GENERADOS POR ESTE MÉTODO.\n
    # - POR TANTO, NO DEBÉIS MODIFICARLO.\n
    # - SI LO HACÉIS EL CORRECTOR AUTOMÁTICO NO FUNCIONARÁ CORRECTAMENTE.\n
    #
    def compara_clave(self,otra,tabs,mensaje):
        ob_name = "Clave[" + self.nombre +"," + str(self.unica) +"]\n"
        indentado = tabs + "  "
        if otra is None:
            mensaje.append(tabs).append(ob_name)\
            .append(indentado).append("Razón: nombre de esta es ").append(self.nombre)\
                .append("; pero no se ha podido encontrar en la otra ninguna clave con ese nombre ").append("\n")
            return False

        if(self.nombre!=otra.nombre):
            mensaje.append(tabs).append(ob_name)\
            .append(indentado).append("Razón: nombre de esta es ").append(self.nombre)\
                .append("; nombre de la otra es ").append(otra.nombre).append("\n")
            return False
        if(self.unica!=otra.unica):
            mensaje.append(tabs).append(ob_name)\
            .append(indentado).append("Razón: unica del campo ").append(self.nombre).append(" en esta es ").append(str(self.unica))\
                .append("; unica del campo ").append(otra.nombre).append(" en la otra es ").append(str(otra.unica)).append("\n")
            return False
        return True