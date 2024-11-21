from src.dominio.esquema import Esquema
from src.dominio.clave import Clave
from src.dominio.tabla import Tabla
from src.dominio.fila_datos import FilaDatos
from src.dominio.excepcionesDominio import ClaveYaExisteException, TablaInexistenteException
from src.dominio.excepcionesDominio import ValorClaveUnicaException, ClaveInexistenteException
from src.dominio.criterios.criterio_igual import CriterioIgual
from src.dominio.criterios.criterio_contiene import CriterioContiene
from src.dominio.criterios.criterio_mayor_que import CriterioMayorQue
from src.dominio.criterios.criterio_menor_que import CriterioMenorQue
from src.utils.string_builder import StringBuilder

class Controlador:
    """
    Controlador de la base de datos, que guardará las diferentes tablas y
    facilitará la comunicación entre la {@link edu.upc.etsetb.poo.basededatos.iu.InterfazUsuario} y los
    demás elementos de la base de datos.

    IMPORTANTE: SE OS ENTREGA EL SIGUIENTE CÓDIGO, QUE NO TENÉIS QUE
    MODIFICAR:
    - LAS DEFINICIONES DE LOS ATRIBUTOS PÚBLICOS FINALES Y ESTÁTICOS
      (CONSTANTES) QUE DEFINEN CARACTERES ESPECIALES UTILIZADOS EN LOS COMANDOS QUE
      CONLLEVEN BÚSQUEDA EN UNA TABLA
    - LOS COMANDOS
    - ANCHO DE COLUMNA-
    """
    ##@var SIMB_CLAVE_UNICA
    #String que, durante la definición del esquema de una tabla (comando
    #'crea') delante del nombre de una clave indica que ésta es clave única
    #
    SIMB_CLAVE_UNICA = '*'
    ## @var SIMB_IGUAL
    # String que, durante la definición de un criterio de
    # búsqueda/eliminación, especifica que es un criterio del tipo
    # CriterioIgual
    SIMB_IGUAL = "="
    ## @var SIMB_CONTIENE
    # String que, durante la definición de un criterio de
    # búsqueda/eliminación, especifica que es un criterio del tipo
    # CriterioContiene
    SIMB_CONTIENE = "#"
    ## @var SIMB_MAYOR_QUE
    # String que, durante la definición de un criterio de
    # búsqueda/eliminación, especifica que es un criterio del tipo
    # CriterioMayorQue
    SIMB_MAYOR_QUE = ">"
    ## @var SIMB_MENOR_QUE
    # String que, durante la definición de un criterio de
    # búsqueda/eliminación, especifica que es un criterio del tipo
    # CriterioMenorQue
    SIMB_MENOR_QUE = "<"

    ## @var ANCHO_COLUMNA
    # Ancho de columna para presentación de tablas fijado en 15 posiciones
    ANCHO_COLUMNA = 15

    ## @var CMD_CREA_TABLA
    # String usado en el comando que crea una tabla
    CMD_CREA_TABLA = "crea"
    ## @var CMD_BUSCA
    # String usado en el comando que crea una tabla
    CMD_BUSCA = "busca"
    ## @var CMD_AÑADE
    # String usado en el comando que busca filas en una tabla
    CMD_AÑADE = "añade"
    ## @var CMD_ELIMINA
    # String usado en el comando que elimina filas de una tabla
    CMD_ELIMINA = "elimina"
    ## @var CMD_AYUDA
    # String usado en el comando que muestra ayuda
    CMD_AYUDA = "ayuda"
    ## @var CMD_SALIR
    # String usado en el comando que acaba la ejecución
    CMD_SALIR = "salir"
    ## @var CMD_EXPORTA
    # String usado en el comando que exporta la base de datos
    CMD_EXPORTA = "exporta"
    ## @var CMD_ORDENA
    # String usado en el comando que ordena una tabla
    CMD_ORDENA = "ordena"

    ##@var tablas
    #Atributo: mapa con las tablas de la base de datos. En cada entrada la clave es el nombre de una de las tablas;
    #el valor es el objetos Tabla que tiene ese nombre.
    #
    ##@var exportador
    #Atributo: objeto de clase Exportador
    #
    ##@var iu
    #Atributo: objeto de clase InterfazUsuario
    #

    ##@brief
    # Constructor del Controlador. Realiza las siguientes tareas:
    # - Crea el mapa de tablas
    # - Asigna al atributo 'exportador' el argumento,
    # - Asigna al atributo 'iu' el valor None
    # @param exportador el objeto de clase Exportador
    #
    def __init__(self, exportador):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Controlador::__init__(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Asigna valor a atributo iu
    #
    # @param iu el nuevo valor de atributo iu
    def set_iu(self, iu):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Controlador::set_iu(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Gestiona el comando 'crea', que se encarga de crear una tabla nueva con
    # un esquema dado.
    #
    # Crea una tabla dado un nombre y un esquema, y la guarda en el sistema.
    # Si ya existe una tabla con dicho nombre, no la creará y ordenará al interfaz
    # de usuario que presente un mensaje de error por pantalla.
    # Hará lo mismo si el formato del comando es erróneo (el número de palabras es menor que
    # 3).
    #
    # Formato:
    #    <code>alumnos crea nombre apellidos *dni año_nacimiento</code></p>
    #
    # Se debe considerar que las claves precedidas por el carácter
    # '*' son claves únicas (es decir, no puede haber dos o más valores iguales para
    # esa clave en diferentes filas de la tabla)
    #
    # Si el usuario no introduce al menos una clave para la tabla, el sistema
    # debe invocar al método InterfazUsuario::println() pasándole como argumento
    # el string "Error en formato del comando."
    #
     # Para facilitar la tarea, asumiremos que las claves del esquema son
    # cadenas alfanuméricas sin espacios en blanco
    #
    # @param palabras Lista con las palabras pertenecientes a un comando, por
    # ejemplo: ["canciones", "crea", "artista", "título",
    #                 "duración" ]
    #
    def crear_tabla(self, palabras):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Controlador::crear_tabla(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Gestiona el comando 'añadir' para la tabla especificada por el usuario,
    # añadiendo todos los pares clave-valor dentro de objeto de clase FilaDatos.
    #
    # Si hay un error de formato en el comando (el número de palabras es menor
    # que 3), O la tabla NO existe O  ha ocurrido algún otro problema a la hora
    # de anyadir los datos, se invocará al método InterfazUsuario.println()
    # pasándole como argumento un string que informe del problema.
    #
    # Formato:
    #   nombreTabla anyadir clave1=valor1 ... claveN=valorN
    #
    # Si el conjunto de pares clave-valor no es válido el sistema muestra el
    # mensaje "<code>"Error añadiendo datos".
    #
    # Para facilitar la tarea, asumiremos que los pares clave-valor son cadenas
    # alfanuméricas sin espacios en blanco.
    #
    # @param palabras Lista con las diferentes palabras que el usuario ha
    # introducido en la línea de comandos, que conforman la orden completa, por
    # ejemplo: ["coches", "anyadir", "matricula=1234GGD","marca=Seat", "modelo=Ibiza", "año=2009"]
    #
    def anyadir(self, palabras):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Controlador::anyadir(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Dado un array perteneciente a las palabras que acompañan a las órdenes
    # 'busca' o 'elimina', interpreta el tipo de criterio que acompañarían a
    # éstas (que coincidiría con el contenido de <code>palabras[2]
    #
    # Si el número de palabras es menor a 3, debe devolver None.
    #
    # El comando debe considerar el operador de criterio que el usuario
    # especifique.
    #
    # Para facilitar la tarea, asumiremos que los criterios de búsqueda son
    # cadenas alfanuméricas sin espacios en blanco
    #
    # @param palabras Lista con las palabras pertenecientes a un comando, por
    # ejemplo: ["peliculas", "busca", "título#Padrino"]
    # @return Una instancia de una de las subclases de Criterio correspondiente a la
    # interpretación de palabras[2].
    #
    def interpreta_criterio(palabras):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Controlador::interpreta_criterio(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Retorna una lista con los nombres de las claves de una tabla dada
    #
    # @param nombreTabla Nombre de la tabla
    # @return Una nueva lista con las getCabeceras, o <code>null</code> si la tabla
    # no existe
    #
    def get_cabeceras(self, nombre_tabla):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Controlador::get_cabeceras(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Gestiona el comando 'busca': para la tabla especificada por el usuario,
    # presenta por pantalla los detalles todas las filas que cumplan con el
    # criterio definido en el comando, invocando al método
    # InterfazUsuario::presentaResultados(cabeceras_tabla,filas).</p>
    #
    # Formato y ejemplos:
    #  - "nombreTabla busca" O
    #  - "nombretabla busca criterio=valorBuscado" (en este ejemplo el valor de criterio debe a
    # ser igual a valorBuscado ó <code>nombreTabla busca criterio#valorBuscado</code> (el
    # valor de criterio debe contener a valorBuscado) O
    #  - "nombreTabla busca criterio>valorBuscado" (en este ejemplo el valor del criterio
    # debe ser mayor que valorBuscado)  O
    #  - "nombreTabla busca criterio<valorBuscado" (en este ejemplo el valor del criterio
    # debe ser menor que valorBuscado
    #
    # Si el usuario no introduce criterio, se mostrarán todas las filas de la
    # tabla.
    #
    # <p>
    # Debe usarse el método auxiliar Controlador::interpretaCriterio(palabras)
    #
    # Para facilitar la tarea, asumiremos que los criterios son cadenas
    # alfanuméricas sin espacios en blanco</p>
    #
    # Si el usuario introduce un nombre de tabla que no existe, se invocará al método
    # InterfazUsuario::println() con el siguiente string como argumento: "Tabla errónea"
    #
    # Las tablas se mostrarán con columnas de ancho fijo
    #  mostrando una cabecera y las diferentes filas.
    # Si el contenido de una columna no cabe en {@link #ANCHO_COLUMNA}, ésta se
    # cortará. Podéis usar el método
    # InterfazUsuari::anchoFijo(String, int)
    #
    # Las tablas se mostrarán invocando al método
    #InterfazUsuario::presentaResultados(cabeceras_tabla,filas)
    #
    # Ejemplo:
    #  "canciones busca título#Bulería".
    #
    ## Artista          |Título           |Duración
    ## ---------------- | --------------- | -------
    ## |David Bisbal    |Bulería          |2:33
    ## |Camarón de la I |Bulerías inédit  |3:15
    ## |Pericón de Cádi |Papas Aliñá (Bu  |1:44
    #
    #
    # @param palabras Una lista con las diferentes palabras que el usuario ha
    # introducido en la línea de comandos, que conforman la orden completa, por
    # ejemplo: ["alumnos", "busca", "apellido=Pérez"]
    #
    # @return lista de filas de datos que cumplen el criterio o lista vacía
    # si se intenta buscar en una tabla que NO existe
    #
    def buscar(self, palabras):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Controlador::buscar(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Gestiona el comando 'elimina'. Para la tabla especificada por el usuario,
    # ELIMINA de la tabla todas las filas que cumplan con el criterio.
    #
    # Elimina las filas de la tabla cuyo nombre está en
    # palabras[0] que cumplan el criterio especificado. Una vez
    # eliminadas ordenará al interfaz de usuario presentar un mensaje que
    # indique el número de filas eliminadas.
    # Si la tabla no existe, debe invocar al método InterfazUsuario::println()
    # pasándoloe como argumento un string que lo indique.
    # Si el comando tiene un error de formato (un criterio erróneo) debe invocar
    # al método InterfazUsuario::println() pasándoloe como argumento un string que lo indique.
    #
    # Formato y ejemplo: "nombreTabla elimina clave#valor""
    #
    # Si el usuario no introduce criterio, o éste es erróneo, debe invocar al método InterfazUsuario::println()
    # pasándole como argumento el string "Error en formato del comando"."
    #
    # Puede usarse el método auxiliar Controlador::interpretaCriterio(palabras)
    #
    # Para facilitar la tarea, asumiremos que los criterios son cadenas
    # alfanuméricas sin espacios en blanco</p>
    #
    # @param palabras Una lista con las diferentes palabras que el usuario ha
    # introducido en la línea de comandos, que conforman la orden completa, por
    # ejemplo: ["alumnos", "elimina", "apellido=garcia"]
    #
    # @return la lista de filas eliminadas si se ha eliminado alguna fila. Una
    # lista vacía si hay un error en el formato del comando o si el comando
    # contiene el nombre de una tabla que no existe
    #
    def eliminar(self, palabras):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Controlador::eliminar(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Ordena la tabla cuyo nombre coincide con palabras[0] según la clave cuyo nombre
    # coincide con palabras[2]></p>
    #
    # Por defecto se ordena en orden ascendente, pero si se pasa la palabra 'desc' dentro de
    # palabras[3], se ordenan en orden descendente.
    #
    # Si la tabla cuyo nombre se pasa en el array de Strings no existe, debe
    # invocar al método InterfazUsuario::println() con el argumento "Error. Tabla inexistente".
    #
    # Si la tabla cuyo nombre se pasa en el array de Strings existe pero en
    # ella no existe la columna cuyo nombre se pasa en el array de Strings, debe
    # invocar al método InterfazUsuario::println() con el argumento "Error. Columna inexistente".
    #
    # @param palabras Lista con las palabras pertenecientes a un comando, por
    # ejemplos:
    # ["peliculas", "ordena", "título"]
    # ["peliculas", "ordena", "año", "desc"]
    #
    def ordenar(self, palabras):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Controlador::ordenar(...) NO SE HA IMPLEMENTADO")

    ##@brief
    # Gestiona el comando 'exporta': invoca al método de Exportador que exporta la base de datos a
    # un archivo
    # @param pathName Nombre del archivo en el que se guardará el archivo de exportación
    #
    def exporta(self, path_name):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Controlador::exporta(...) NO SE HA IMPLEMENTADO")

    ##@brief
    #Genera un string con una representación textual de los contenidos de la base
    #de datos.
    #**MUY IMPORTANTE:** \n
    # - ESTE MÉTODO SE DA HECHO.\n
    # - EL CORRECTOR AUTOMÁTICO UTILIZA LOS STRINGS GENERADOS POR ESTE MÉTODO.\n
    # - POR TANTO, NO DEBÉIS MODIFICARLO.\n
    # - SI LO HACÉIS EL CORRECTOR AUTOMÁTICO NO FUNCIONARÁ CORRECTAMENTE.\n
    #
    def __str__(self):
        result = "BaseDeDatos<"
        i = 0
        for item in self.tablas.items():
            if i != 0:
                result += ','
            result += str(item[1])
            i += 1
        result += '>'
        return result

    ##@brief
    #Compara los contenidos de este controlador con otro y presenta información en caso de que no
    #sean los mismos, identificando en qué lugar se ha detectado la primera desigualdad
    #**MUY IMPORTANTE:** \n
    # - ESTE MÉTODO SE DA HECHO.\n
    # - EL CORRECTOR AUTOMÁTICO UTILIZA LOS STRINGS GENERADOS POR ESTE MÉTODO.\n
    # - POR TANTO, NO DEBÉIS MODIFICARLO.\n
    # - SI LO HACÉIS EL CORRECTOR AUTOMÁTICO NO FUNCIONARÁ CORRECTAMENTE.\n
    #
    def compara(self,otro,tabs,mensaje):
        ob_name = "Controlador" + "\n"
        indentado = tabs + "  "
        report = StringBuilder()
        if len(self.tablas)!=len(otro.tablas):
            mensaje.append(tabs).append(ob_name)\
            .append(indentado).append("Razón: el número de tablas de este es ").append(str(len(self.tablas)))\
                .append("; el número de tablas del otro es ").append(str(len(otro.tablas))).append("\n")
            return False
        for nombre_tabla in self.tablas.keys():
            tabla_este = self.tablas.get(nombre_tabla)
            tabla_otro = otro.tablas.get(nombre_tabla)
            if tabla_otro==None:
                mensaje.append(tabs).append(ob_name) \
                    .append(indentado).append("Razón: este controlador tiene una tabla de nombre ").append(nombre_tabla) \
                    .append("; el otro controlador NO lo tiene ").append("\n")
                return False
            if not tabla_este.compara_tabla(tabla_otro,indentado,report):
                mensaje.append(tabs).append(ob_name).append(report.to_string())
                return False;
        return True

    ##@brief
    # Crea un nuevo controlador vacío.
    # **MUY IMPORTANTE:** \n
    # - ESTE MÉTODO SE DA HECHO.\n
    # - EL CORRECTOR AUTOMÁTICO UTILIZA LOS STRINGS GENERADOS POR ESTE MÉTODO.\n
    # - POR TANTO, NO DEBÉIS MODIFICARLO.\n
    # - SI LO HACÉIS EL CORRECTOR AUTOMÁTICO NO FUNCIONARÁ CORRECTAMENTE.\n
    #
    def crea_controlador_vacio():
        return Controlador(None)
