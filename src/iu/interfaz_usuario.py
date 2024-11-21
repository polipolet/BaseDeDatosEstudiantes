from src.casosdeuso.controlador import Controlador
from src.iu.entrada_datos import EntradaDatos

class InterfazUsuario:

    last_println_con_arg = ""
    last_print_con_arg = ""
    corrigiendo = False;

    def __init__(self,controlador,exportador):
        self.controlador = controlador

    def procesa_comando(self):
        print("COMANDO>",end="")
        cmd = EntradaDatos.palabras()
        if len(cmd)>0:
            if Controlador.CMD_AYUDA==cmd[0]:
                self.ayuda()
            elif Controlador.CMD_EXPORTA==cmd[0]:
                    self.controlador.exporta(cmd[1])
            elif len(cmd)>1:
                if cmd[1]==Controlador.CMD_CREA_TABLA:
                    self.controlador.crear_tabla(cmd)
                elif cmd[1]==Controlador.CMD_BUSCA:
                    self.controlador.buscar(cmd)
                elif cmd[1]==Controlador.CMD_AÑADE:
                    self.controlador.anyadir(cmd)
                elif cmd[1]==Controlador.CMD_ELIMINA:
                    self.controlador.eliminar(cmd)
                elif cmd[1]==Controlador.CMD_ORDENA:
                    self.controlador.ordenar(cmd)
                else:
                    print("Error! Comando no reconocido")
                    print("Escribe ",Controlador.CMD_AYUDA," para conocer la lista de comandos.")
        else:
            print("Final de entrada de datos")
            return True
        return False

    def ayuda(self):
        print("Lista de comandos:");
        print("\n",Controlador.CMD_AYUDA," : esta ayuda");
        print("\n",Controlador.CMD_SALIR," : salir del programa");
        print("\n<nombreTabla> ",Controlador.CMD_CREA_TABLA," [ <clave> ]");
        print("\t- Crea una nueva tabla llamada <nombretabla>, cuyo esquema está descrito por una sucesión de <clave>");
        print("\t  Ejemplo: coches crea matricula marca modelo año");

        print("\n<nombreTabla> ",Controlador.CMD_AÑADE," [ <clave>=<valor> ó *<clave>=<valor>]");
        print("\t- Añade una nueva fila a la tabla <nombretabla>, descrita por una sucesión de pares <clave>=<valor>");
        print("\t  Las claves cuyo nombre tiene delante asterisco '*' son claves únicas");
        print("\t  Ejemplo: coches añade matricula=12345XD marca=Seat modelo=Ibiza año=2000");

        print("\n<nombreTabla> ",Controlador.CMD_BUSCA);
        print("\t- Muestra TODOS los datos de la tabla");

        print("\n<nombreTabla> ",Controlador.CMD_BUSCA," <clave>=<valor> ó <clave>#<valor>");
        print("\t- Busca filas según UN criterio especificado por una clave y un valor.");
        print("\t  El operador '=' indica que el valor debe ser IGUAL al valor de la columna identificada por <clave>");
        print("\t  El operador '=' indica que el valor debe estar CONTENIDO al valor de la columna identificada por <clave>");
        print("\t  Ejemplo: coches busca matricula#123 --> devolverá todos los coches cuya matrícula contenga la sucesión de números '123'");
        print("\t           coches busca marca=Seat --> devolverá todos los coches cuya marca sea exactamente igual a Seat");

        print("\n<nombreTabla> ",Controlador.CMD_ELIMINA," <clave>=<valor> ó <clave>#<valor>");
        print("\t- Elimina filas según UN criterio especificado por una clave y un valor.");
        print("\t  El uso es análogo al del comando ",Controlador.CMD_BUSCA);

        print("\n<nombreTabla> ",Controlador.CMD_ORDENA," <clave> [ desc ]");
        print("\t- Ordena la tabla según el valor de la clave de cada fila.");
        print("\t- Si se proporciona el argumento 'desc', ordena en orden descendente. Si no, ascendente");

        print("\n",Controlador.CMD_EXPORTA,"<nombreArchivo> : exporta el contenido de la base de datos a un archivo\n");

    def repite(c,nVeces):
        for i in range(0,nVeces):
            print(c,end="")

    def ancho_fijo(texto,ancho):
        if texto is None:
            InterfazUsuario.repite(' ',ancho)
        else:
            if len(texto)>ancho:
                print(texto[0:ancho])
            else:
                print(texto,end="")
                InterfazUsuario.repite(' ',ancho-len(texto))


    def println(self,texto):
        if not InterfazUsuario.corrigiendo:
            print(texto)
        InterfazUsuario.last_println_con_arg = texto

    def print(self,texto):
        if not InterfazUsuario.corrigiendo:
            print(texto,end="")
        InterfazUsuario.last_print_con_arg = texto

    def reset_last_println(self):
        InterfazUsuario.last_println_con_arg=""

    def reset_last_print(self):
        InterfazUsuario.last_print_con_arg=""

    def reset_all_last_prints(self):
        InterfazUsuario.last_println_con_arg = ""
        InterfazUsuario.last_print_con_arg=""

    def presenta_resultados(self,cabeceras_tabla,filas):
        ancho_tabla = (Controlador.ANCHO_COLUMNA + 1)*len(cabeceras_tabla) + 1
        InterfazUsuario.repite('=',ancho_tabla)
        print()
        for cabecera in cabeceras_tabla:
            print("|",end="")
            InterfazUsuario.ancho_fijo(cabecera,Controlador.ANCHO_COLUMNA)
        print("|")
        InterfazUsuario.repite('-',ancho_tabla)
        print()
        for fila in filas:
            for cabecera in cabeceras_tabla:
                print("|", end="")
                InterfazUsuario.ancho_fijo(fila.get(cabecera),Controlador.ANCHO_COLUMNA)
            print("|")
        InterfazUsuario.repite('=',ancho_tabla)
        print()




