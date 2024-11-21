import traceback
import os
import re
from src.casosdeuso.controlador import Controlador
from src.casosdeuso.exportador import Exportador
from src.iu.interfaz_usuario import InterfazUsuario
from test.CorrectorGlobal import SuperClassForTests
from test.utils.list_utils import ListUtils
from test.utils.lector_datos import LectorDatos
from src.utils.string_builder import StringBuilder


class ControladorTest(SuperClassForTests):

    numErrorsBefore = 0

    numInstances = 0

    nota = 0.0

    base_path = os.getcwd() + "/paracorreccion/para_correctores/controlador_test/"

    matriz_datos_coches = [
        ["marca", "Seat", "modelo", "Ibiza", "matricula", "B1234XD"],
        ["marca","Seat","modelo","Córdoba","matricula","4456GVG"],
        ["marca","Ford","modelo","Fiesta","matricula","2345FXZ"],
        ["marca","Ferrari","modelo","Testarrossa","matricula","1566GGH"],
        ["marca","Ford","modelo","Escort","matricula","4566GGH"]
    ]

    matriz_datos_multas = [
        ["matricula","B1234XD","cuantia","100"],
        ["matricula","2345FXZ","cuantia","101"],
        ["matricula","B1234XD","cuantia","60"],
        ["matricula","1566GGH","cuantia","100"]
    ]

    def __init__(self,*args, **kwargs):
        SuperClassForTests.__init__(self, *args, **kwargs)
        ControladorTest.numInstances = ControladorTest.numInstances + 1
        if ControladorTest.numInstances == 1:
            ControladorTest.numErrorsBefore = len(SuperClassForTests.indErrors)
        #
        self.tabla_coches = None
        self.tabla_multas = None
        self.filas_tabla_coches = []
        self.filas_tabla_multas = []
        InterfazUsuario.corrigiendo = True
        #
        data = os.getcwd()
        self.lector = LectorDatos()

    def setUpClass():
        # SuperClassForTests.nota = {}
        ControladorTest.nota = 0.0
        print("\n\nCORRIGIENDO clase Controlador")
        print("**************************")

    def tearDownClass():
        SuperClassForTests.showErrors(SuperClassForTests.indErrors, "Controlador")
        SuperClassForTests.acumulaErrores()
        SuperClassForTests.indErrors = []
        ControladorTest.nota = SuperClassForTests.puntosTotales
        SuperClassForTests.puntosTotales = 0

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test01_init(self):
        valorTotal = 0.25
        puntosAntes = SuperClassForTests.puntosTotales
        num_tests = 8
        toThrow = None
        print(f"\n\tControlador::__init__(). Valor: {valorTotal}")
        error = None
        toThrow = None
        try:
            exportador = Exportador()
            controlador = Controlador(exportador)
            indVal = valorTotal/num_tests
            #Comprobar atributo 'iu'
            print("\tTest 1: comprobación de que el atributo \'iu\' existe")
            error = self.checkFieldExists('iu',controlador,indVal,None)
            self.toThrow(error,toThrow)
            if error == None:
                print("\tTest 2: comprobación de que el atributo \'iu\' tiene un valor None")
                error = self.sAssertEquals(controlador.iu,None,indVal,None)
                self.toThrow(error,toThrow)
            #Comprobar atributo 'tablas'
            print("\tTest 3: comprobación de que el atributo \'tablas\' existe")
            error = self.checkFieldExists('tablas',controlador,indVal,None)
            toThrow = self.toThrow(error, toThrow)
            if error == None:
                print("\tTest 4: comprobación de que el atributo \'tablas\' es un mapa")
                error = self.checkFieldIsOfASpecificClassByName("tablas", controlador, "dict", indVal, toThrow)
                self.toThrow(error, toThrow)
                print("\tTest 5: comprobación de que el valor del atributo \'tablas\' no es None")
                error = self.sAssertFalse(controlador.tablas==None, indVal, toThrow)
                self.toThrow(error, toThrow)
                print("\tTest 6: comprobación de que el atributo \'tablas\' está vacío")
                error = self.sAssertEquals(0, len(controlador.tablas), indVal, toThrow)
                self.toThrow(error, toThrow)
            #Comprobar atributo 'exportador'
            print("\tTest 7: comprobación de que el atributo \'exportador\' existe")
            error = self.checkFieldExists('exportador',controlador,indVal,None)
            toThrow = self.toThrow(error, toThrow)
            if error == None:
                print("\tTest 8: comprobación de que el valor del atributo \'exportador\' es el argumento pasado")
                error = self.sAssertTrue(controlador.exportador==exportador, indVal, toThrow)
                self.toThrow(error, toThrow)

        except Exception as ex:
            print("*** Se ha capturado una excepción que probablemente "
                    + "ha sido lanzada por tu código. Mira la traza para "
                    + "detectar en qué punto ha sido creada y lanzada...")
            traceback.print_exc()
            stack = traceback.extract_stack()
            self.printStackTraceUpc(stack)

        self.acumula(SuperClassForTests.puntos)
        self.show_puntos(puntosAntes)

    def test02_set_iu(self):
        valorTotal = 0.25
        puntosAntes = SuperClassForTests.puntosTotales
        num_tests = 1
        toThrow = None
        print(f"\n\tControlador::set_iu(). Valor: {valorTotal}")
        error = None
        toThrow = None
        try:
            exportador = Exportador()
            controlador = Controlador(exportador)
            iu = InterfazUsuario(controlador,exportador)
            controlador.set_iu(iu)
            error = self.sAssertTrue(controlador.iu == iu, valorTotal,"Error. El valor del atributo \'iu\' NO es " \
                                                                     "el del argumento pasado al método")
            self.toThrow(error,toThrow)
        except Exception as ex:
            print("*** Se ha capturado una excepción que probablemente "
                    + "ha sido lanzada por tu código. Mira la traza para "
                    + "detectar en qué punto ha sido creada y lanzada...")
            traceback.print_exc()
            stack = traceback.extract_stack()
            self.printStackTraceUpc(stack)

        self.acumula(SuperClassForTests.puntos)
        self.show_puntos(puntosAntes)

    mensajes_tests_crea_tabla = [
        "comando de menos de 3 palabras. Se envía mensaje a interfaz de usuario. No se crea tabla",
        "comando con dos claves idénticas. Debe lanzarse y recogerse internamente una excepción ClaveYaExisteException. "
        +"Debe enviarse un mensaje al interfaz de usuario. Se crea la nueva tabla",
        "comando que intenta generar una tabla con nombre ya asociado a otra tabla. Debe enviarse un mensaje. "
        +"NO se crea ninguna tabla",
        "comando que crea una nueva tabla con éxito"
     ]

    folder_controladores_crea_tabla = base_path+"crea_tabla/"

    comandos_crea_tabla = [
        "coches crea",
        "coches crea marca marca *matricula",
        "coches crea marca modelo *matricula",
        "multas crea *matricula cuantia"
    ]

    enviar_mensaje_crea_tabla = [True,True,True,False]

    def test03_crea_tabla(self):
        valorTotal = 1.5
        puntosAntes = SuperClassForTests.puntosTotales
        num_tests = 8
        valorInd = valorTotal/num_tests
        toThrow = None
        print(f"\n\tControlador::crea_tabla(). Valor: {valorTotal}")
        error = None
        toThrow = None
        try:
            controlador = None
            for i in range(0,len(ControladorTest.comandos_crea_tabla)):
                continuar_test = True
                nf_inicial = ControladorTest.folder_controladores_crea_tabla+"test_"+str(i+1)+"_antes.xml"
                nf_esperado = ControladorTest.folder_controladores_crea_tabla+"test_"+str(i+1)+"_despues.xml"
                try:
                    controlador = self.lector.lee_cnt_from_path(nf_inicial)
                    iu = InterfazUsuario(controlador,None)
                    controlador.iu = iu
                    iu.reset_all_last_prints()
                except Exception as ex:
                    print(
                        "*** Contacta con el profesorado. El corrector ha tratado de acceder a un archivo de corrección "
                        + "sin conseguirlo. A continuación se detalla la traza de la excepción.")
                    traceback.print_exc()
                    stack = traceback.extract_stack()
                    self.printStackTraceUpc(stack)
                    contiuar_test = False
                if continuar_test:
                    self.check_mensaje_y_estado_despues_invocar_metodo(controlador.crear_tabla,
                        ControladorTest.comandos_crea_tabla[i],nf_esperado,controlador,ControladorTest.enviar_mensaje_crea_tabla[i],
                        ControladorTest.mensajes_tests_crea_tabla[i],(i+1),valorInd)
        except Exception as ex:
            print("*** Se ha capturado una excepción que probablemente "
                    + "ha sido lanzada por tu código. Mira la traza para "
                    + "detectar en qué punto ha sido creada y lanzada...")
            traceback.print_exc()
            stack = traceback.extract_stack()
            self.printStackTraceUpc(stack)

        self.acumula(SuperClassForTests.puntos)
        self.show_puntos(puntosAntes)

    mensajes_tests_anyadir = [
        "comando de menos de 3 palabras. Debería enviarse un mensaje de error y dejar la base de datos inalterada",
        "comando con un NOMBRE DE TABLA QUE NO EXISTE. Debería enviarse un mensaje de error. Base de datos inalterada",
        "comando con CLAVE ERRÓNEA. Debería enviarse un mensaje de error. Base de datos inalterada",
        "comando CORRECTO. No debería enviar ningún mensaje. Base de Datos con la nueva fila",
        "comando CLAVE ÚNICA REPETIDA. Debería enviarse un mensaje de error. Base de datos inalterada",
        "segundo comando CORRECTO. Base de Datos con la nueva fila"
    ]

    folder_controladores_anyadir = base_path+"anyadir/"

    comandos_anyadir = [
        "coches anyadir",
        "coche anyadir matricula=1234GGD marca=Seat modelo=Ibiza",
        "coches anyadir matriculas=1234GGD marca=Seat modelo=Ibiza",
        "coches anyadir matricula=1234GGD marca=Seat modelo=Ibiza",
        "coches anyadir matricula=1234GGD marca=Renault modelo=Clio",
        "coches anyadir matricula=56789XF marca=Renault modelo=Clio"
    ]

    enviar_mensaje_anyadir = [True,True,True,False,True,False]

    def test04_anyadir(self):
        valorTotal = 1.5
        puntosAntes = SuperClassForTests.puntosTotales
        num_tests = 12
        valorInd = valorTotal/num_tests
        toThrow = None
        print(f"\n\tControlador::anyadir(). Valor: {valorTotal}")
        error = None
        toThrow = None
        continuar = True
        try:
            controlador = None
            for i in range(0,len(ControladorTest.comandos_anyadir)):
                continuar_test = True
                nf_inicial = ControladorTest.folder_controladores_anyadir+"test_"+str(i+1)+"_antes.xml"
                nf_esperado = ControladorTest.folder_controladores_anyadir+"test_"+str(i+1)+"_despues.xml"
                try:
                    controlador = self.lector.lee_cnt_from_path(nf_inicial)
                    iu = InterfazUsuario(controlador,None)
                    controlador.iu = iu
                    iu.reset_all_last_prints()
                except Exception as ex:
                    print(
                        "*** Contacta con el profesorado. El corrector ha tratado de acceder a un archivo de corrección "
                        + "sin conseguirlo. A continuación se detalla la traza de la excepción.")
                    traceback.print_exc()
                    stack = traceback.extract_stack()
                    self.printStackTraceUpc(stack)
                    contiuar_test = False
                if continuar_test:
                    self.check_mensaje_y_estado_despues_invocar_metodo(controlador.anyadir,
                        ControladorTest.comandos_anyadir[i],nf_esperado,controlador,ControladorTest.enviar_mensaje_anyadir[i],
                        ControladorTest.mensajes_tests_anyadir[i],(i+1),valorInd)
        except Exception as ex:
            print("*** Se ha capturado una excepción que probablemente "
                    + "ha sido lanzada por tu código. Mira la traza para "
                    + "detectar en qué punto ha sido creada y lanzada...")
            traceback.print_exc()
            stack = traceback.extract_stack()
            self.printStackTraceUpc(stack)

        self.acumula(SuperClassForTests.puntos)
        self.show_puntos(puntosAntes)

    def check_mensaje_y_estado_despues_invocar_metodo(self,metodo,comando_str,nf_esperado,controlador,debe_enviar_mensaje,
                mensaje_de_test,num_test,valorInd):
        toThrow = None
        print("\tTest "+str(num_test)+": "+mensaje_de_test)
        contr_esperado = None
        try:
            contr_esperado = self.lector.lee_cnt_from_path(nf_esperado)
        except Exception as ex:
            print("*** Contacta con el profesorado. El corrector ha tratado de acceder a un archivo de corrección "
                    + "sin conseguirlo. A continuación se detalla la traza de la excepción.")
            traceback.print_exc()
            stack = traceback.extract_stack()
            self.printStackTraceUpc(stack)
            return
        controlador.iu.reset_all_last_prints()
        try:
            metodo(comando_str.split())
        except Exception as ex:
            print("*** Se ha capturado una excepción que probablemente "
                    + "ha sido lanzada por tu código. Mira la traza para "
                    + "detectar en qué punto ha sido creada y lanzada...")
            traceback.print_exc()
            stack = traceback.extract_stack()
            self.printStackTraceUpc(stack)
            return

        #
        # Comprobar si se ha enviado el mensaje de error
        if debe_enviar_mensaje:
            error = self.sAssertTrue(len(InterfazUsuario.last_println_con_arg) != 0, valorInd, "Error. El método "
                             + "debería haber enviado un mensaje de error al interfaz de usuario. Sin embargo NO ha sido así")
            self.toThrow(error, toThrow)
        else:
            error = self.sAssertTrue(len(InterfazUsuario.last_println_con_arg) == 0, valorInd, "Error. El método "
                             + "NO debería haber enviado un mensaje de error al interfaz de usuario. Sin embargo lo ha enviado")
            self.toThrow(error, toThrow)
        #
        # Comprobar si el estado del controlador es el correcto
        mensaje = StringBuilder()
        iguales = contr_esperado.compara(controlador,"\t\t\t",mensaje)
        if iguales:
            error = self.sAssertTrue(True,valorInd,"")
        else:
            error = self.sAssertFalse(True,0,"Error. El estado del controlador NO es el esperado. En el mensaje "
                                            "que sigue, 'este' es el esperado y 'otro' es el que se ha obtenido\n")
            print(mensaje.to_string())
            self.toThrow(error, toThrow)

    folder_controladores_get_cabeceras = base_path+"get_cabeceras/"

    def test05_get_cabeceras(self):
        valorTotal = 0.25
        puntosAntes = SuperClassForTests.puntosTotales
        num_tests = 1
        toThrow = None
        print(f"\n\tControlador::get_cabeceras(). Valor: {valorTotal}")
        error = None
        toThrow = None
        try:
            controlador = None
            continuar_test = True
            nf = ControladorTest.folder_controladores_get_cabeceras+"todos_casos_antes.xml"
            try:
                controlador = self.lector.lee_cnt_from_path(nf)
                iu = InterfazUsuario(controlador,None)
                controlador.iu = iu
                iu.reset_all_last_prints()
            except Exception as ex:
                print(
                    "*** Contacta con el profesorado. El corrector ha tratado de acceder a un archivo de corrección "
                    + "sin conseguirlo. A continuación se detalla la traza de la excepción.")
                traceback.print_exc()
                stack = traceback.extract_stack()
                self.printStackTraceUpc(stack)
                contiuar_test = False
            if continuar_test:
                cabeceras = controlador.get_cabeceras("coches")
                esperadas = ["marca","modelo","matricula"]
                error = self.sAssertEquals(esperadas, cabeceras,valorTotal,"Error. No se ha obtenido la lista "
                    +"de cabeceras esperada. Se esperaba la lista " + str(esperadas) + ". Se ha obtenido la lista " + str(cabeceras))
                self.toThrow(error,toThrow)

        except Exception as ex:
           print("*** Se ha capturado una excepción que probablemente "
                 + "ha sido lanzada por tu código. Mira la traza para "
                 + "detectar en qué punto ha sido creada y lanzada...")
           traceback.print_exc()
           stack = traceback.extract_stack()
           self.printStackTraceUpc(stack)

        self.acumula(SuperClassForTests.puntos)
        self.show_puntos(puntosAntes)

    folder_controladores_interpreta_criterio = base_path+"interpreta_criterio/"

    comandos_interpreta_criterio = [
        "coches busca",
        "coches busca matricula&12345",
        "coches busca matricula=12345",
        "coches busca matricula#12345",
        "coches busca matricula>12345",
        "coches busca matricula<12345"
    ]

    texto_casos_interpreta_criterio = [
        "\tTest 1. Comando: '" + comandos_interpreta_criterio[0] + "; comando de menos de 3 palabras. Debe devolver None",
        "\tTest 2. Comando: '" + comandos_interpreta_criterio[1] + "; comando no contiene el símbolo de ningún criterio válido. Debe devolver None",
        "\tTest 3. Comando: '" + comandos_interpreta_criterio[2] + "; comando contiene el símbolo = (CriterioIgual). Debe devolver objeto CriterioIgual",
        "\tTest 4. Comando: '" + comandos_interpreta_criterio[3] + "; comando contiene el símbolo # (CriterioContiene). Debe devolver objeto CriterioContiene",
        "\tTest 5. Comando: '" + comandos_interpreta_criterio[4] + ";  comando contiene el símbolo > (CriterioMayorQue). Debe devolver objeto CriterioMayorQue",
        "\tTest 6. Comando: '" + comandos_interpreta_criterio[5] + "; comando contiene el símbolo < (CriterioMenorQue). Debe devolver objeto CriterioMenorQue"
    ]

    resultados_esperados_interpreta_criterio = [
        None,
        None,
        "CriterioIgual<matricula,12345>",
        "CriterioContiene<matricula,12345>",
        "CriterioMayorQue<matricula,12345,12345.0>",
        "CriterioMenorQue<matricula,12345,12345.0>"
    ]

    textos_si_error_interpreta_criterio = [
        "Error. El comando tenía menos de 3 palabras pero   el método NO ha devuelto None",
        "Error. El comando no contiene ningún símbolo  correspondiente a un criterio y el método NO ha devuelto None",
        "Error. El comando contiene símbolo de CriterioIgual pero NO ha devuelto $A; en su lugar, ha devuelto $B",
        "Error. El comando contiene símbolo de CriterioContiene pero NO ha devuelto $A; en su lugar, ha devuelto $B",
        "Error. El comando contiene símbolo de CriterioMayorQue pero NO ha devuelto $A; en su lugar, ha devuelto $B",
        "Error. El comando contiene símbolo de CriterioMenorQue pero NO ha devuelto $A; en su lugar, ha devuelto $B"
    ]

    def test07_interpreta_criterio(self):
        valorTotal = 1.25
        puntosAntes = SuperClassForTests.puntosTotales
        num_tests = 12
        indVal = valorTotal/num_tests
        toThrow = None
        print(f"\n\tControlador::interpreta_criterio(). Valor: {valorTotal}")
        error = None
        toThrow = None
        try:
            controlador = None
            continuar_test = True
            nf = ControladorTest.folder_controladores_interpreta_criterio+"todos_casos_antes.xml"
            try:
                controlador = self.lector.lee_cnt_from_path(nf)
                iu = InterfazUsuario(controlador,None)
                controlador.iu = iu
                iu.reset_all_last_prints()
                controlador_esperado = self.lector.lee_cnt_from_path(nf)
            except Exception as ex:
                print(
                    "*** Contacta con el profesorado. El corrector ha tratado de acceder a un archivo de corrección "
                    + "sin conseguirlo. A continuación se detalla la traza de la excepción.")
                traceback.print_exc()
                stack = traceback.extract_stack()
                self.printStackTraceUpc(stack)
                contiuar_test = False
            if(continuar_test):
                for i in range(0, len(ControladorTest.comandos_interpreta_criterio)):
                   self.check_resultado_devuelto_y_estado(Controlador.interpreta_criterio,
                        ControladorTest.comandos_interpreta_criterio[i],controlador,controlador_esperado,
                        ControladorTest.resultados_esperados_interpreta_criterio[i],
                        ControladorTest.texto_casos_interpreta_criterio[i],
                        ControladorTest.textos_si_error_interpreta_criterio[i],indVal)

        except Exception as ex:
            print("*** Se ha capturado una excepción que probablemente "
                  + "ha sido lanzada por tu código. Mira la traza para "
                  + "detectar en qué punto ha sido creada y lanzada...")
            traceback.print_exc()
            stack = traceback.extract_stack()
            self.printStackTraceUpc(stack)

        self.acumula(SuperClassForTests.puntos)
        self.show_puntos(puntosAntes)

    def check_resultado_devuelto_y_estado(self,metodo,comando,controlador,controlador_esperado,resultado_esperado,
         texto_test,txt_si_error_resultado,indVal):
        resultado =None
        toThrow = None
        print(texto_test)
        try:
            resultado = metodo(comando.split())
        except Exception as ex:
            print("*** Se ha capturado una excepción que probablemente "
                  + "ha sido lanzada por tu código. Mira la traza para "
                  + "detectar en qué punto ha sido creada y lanzada...")
            traceback.print_exc()
            stack = traceback.extract_stack()
            self.printStackTraceUpc(stack)
            return
        #Comprobando resultado
        mssg_error = txt_si_error_resultado
        if resultado_esperado is not None :
            mssg_error = txt_si_error_resultado.replace("$A", str(resultado_esperado))
        if resultado is not None:
            mssg_error = mssg_error.replace("$B", str(resultado))
        if resultado is None:
            error = self.sAssertEquals(resultado_esperado,resultado, indVal, mssg_error)
        else:
            error = self.sAssertEquals(resultado_esperado,str(resultado), indVal, mssg_error)
        self.toThrow(error, toThrow)
        #
        #Comprobando estado de la base de datos
        mensaje = StringBuilder()
        iguales = controlador_esperado.compara(controlador,"\t\t\t",mensaje)
        if iguales:
            error = self.sAssertTrue(True,indVal,"")
        else:
            error = self.sAssertFalse(True,0,"Error. El estado del controlador NO es el esperado. En el mensaje "
                                            "que sigue, 'este' es el esperado y 'otro' es el que se ha obtenido\n")
            print(mensaje.to_string())
            self.toThrow(error, toThrow)

    comandos_buscar = [
        "coches busca matricula#1234GGD",
        "coches busca ",
        "coches busca marca=Seat",
        "multas busca cuantia=100",
        "multas busca cuantia>60",
        "multas busca cuantia<101",
        "coches busca marca#Fo",
        "coches busca marca#Mer",
        "coches busca marca=Mercedes",
        "multas busca cuantia=550",
        "multas busca cuantia>550",
        "multas busca cuantia<20"
    ]

    texto_casos_buscar = [
"\tTest 1. Comando: '" + comandos_buscar[0] + "'; intento de búsqueda en tabla que NO existe. Se devuelve lista vacía. A continuación se muestra la salida por consola",
"\tTest 2. Comando: '" + comandos_buscar[1] + "'; intento de búsqueda sin criterio. Se devuelve lista con todas las filas. A continuación se muestra la salida por consola",
"\tTest 3. Comando: '" + comandos_buscar[2] + "'; intento de búsqueda con criterio = NO numérico. Se devuelve lista con las filas que cumplen el criterio. A continuación se muestra la salida por consola",
"\tTest 4. Comando: '" + comandos_buscar[3] + "'; intento de búsqueda con criterio = numérico. Se devuelve lista con las filas que cumplen el criterio. A continuación se muestra la salida por consola",
"\tTest 5. Comando: '" + comandos_buscar[4] + "'; intento de búsqueda con criterio > numérico. Se devuelve lista con las filas que cumplen el criterio. A continuación se muestra la salida por consola",
"\tTest 6. Comando: '" + comandos_buscar[5] + "'; intento de búsqueda con criterio < numérico. Se devuelve lista con las filas que cumplen el criterio. A continuación se muestra la salida por consola",
"\tTest 7. Comando: '" + comandos_buscar[6] + "'; intento de búsqueda con criterio #. Se devuelve lista con las filas que cumplen el criterio. A continuación se muestra la salida por consola",
"\tTest 8. Comando: '" + comandos_buscar[7] + "'; intento de búsqueda con criterio # que NO se cumple. Se devuelve lista vacía. A continuación se muestra la salida por consola",
"\tTest 9. Comando: '" + comandos_buscar[8] + "'; intento de búsqueda con criterio = NO numérico que NO se cumple. Se devuelve lista vacía. A continuación se muestra la salida por consola",
"\tTest 10. Comando: '" + comandos_buscar[9] + "'; intento de búsqueda con criterio = numérico que NO se cumple. Se devuelve lista vacía. A continuación se muestra la salida por consola",
"\tTest 11. Comando: '" + comandos_buscar[10] + "'; intento de búsqueda con criterio > que NO se cumple. Se devuelve lista vacía. A continuación se muestra la salida por consola",
"\tTest 12. Comando: '" + comandos_buscar[11] + "'; intento de búsqueda con criterio < que NO se cumple. Se devuelve lista vacía. A continuación se muestra la salida por consola"]

    texto_comparar_filas_buscar = [
        f"Error. Se buscaba algo que no existe en la tabla. El comando debería haber devuelto la lista: $A, pero ha devuelto la lista: $B",
        f"Error. El comando no tenía criterio. El comando debería haber devuelto la lista: $A, pero ha devuelto la lista: $B",
        f"Error. El comando debería haber devuelto la lista: $A, pero ha devuelto la lista: $B"
    ]

    texto_comparar_bd_buscar = f"Error. La base de datos NO tiene los contenidos esperados. Debería tener $A, pero " \
                               "tiene $B"

    resultados_esperados_buscar = [
        "Lista<>",
        "Lista<FilaDatos[marca:Seat,modelo:Ibiza,matricula:B1234XD],FilaDatos[marca:Seat,modelo:Córdoba,matricula:4456GVG],FilaDatos[marca:Ford,modelo:Fiesta,matricula:2345FXZ],FilaDatos[marca:Ferrari,modelo:Testarrossa,matricula:1566GGH],FilaDatos[marca:Ford,modelo:Escort,matricula:4566GGH]>",
        "Lista<FilaDatos[marca:Seat,modelo:Ibiza,matricula:B1234XD],FilaDatos[marca:Seat,modelo:Córdoba,matricula:4456GVG]>",
        "Lista<FilaDatos[matricula:B1234XD,cuantia:100],FilaDatos[matricula:1566GGH,cuantia:100]>",
        "Lista<FilaDatos[matricula:B1234XD,cuantia:100],FilaDatos[matricula:2345FXZ,cuantia:101],FilaDatos[matricula:1566GGH,cuantia:100]>",
        "Lista<FilaDatos[matricula:B1234XD,cuantia:100],FilaDatos[matricula:B1234XD,cuantia:60],FilaDatos[matricula:1566GGH,cuantia:100]>",
        "Lista<FilaDatos[marca:Ford,modelo:Fiesta,matricula:2345FXZ],FilaDatos[marca:Ford,modelo:Escort,matricula:4566GGH]>",
        "Lista<>",
        "Lista<>",
        "Lista<>",
        "Lista<>",
        "Lista<>",
    ]

    folder_controladores_buscar = base_path+"buscar/"

    def test07_buscar(self):
        valorTotal = 1.9
        puntosAntes = SuperClassForTests.puntosTotales
        num_tests = 24
        indVal = valorTotal/num_tests
        toThrow = None
        print(f"\n\tControlador::buscar(). Valor: {valorTotal}")
        error = None
        toThrow = None
        try:
            controlador = None
            continuar_test = True
            nf = ControladorTest.folder_controladores_buscar+"todos_casos_despues.xml"
            try:
                controlador = self.lector.lee_cnt_from_path(nf)
                iu = InterfazUsuario(controlador,None)
                controlador.iu = iu
                iu.reset_all_last_prints()
                controlador_esperado = self.lector.lee_cnt_from_path(nf)
            except Exception as ex:
                print(
                    "*** Contacta con el profesorado. El corrector ha tratado de acceder a un archivo de corrección "
                    + "sin conseguirlo. A continuación se detalla la traza de la excepción.")
                traceback.print_exc()
                stack = traceback.extract_stack()
                self.printStackTraceUpc(stack)
                contiuar_test = False
            if continuar_test:
                for i in range(0, 12):
                    iu.reset_all_last_prints()
                    if i < 2:
                        texto_para_error_filas = ControladorTest.texto_comparar_filas_buscar[i]
                    else:
                        texto_para_error_filas = ControladorTest.texto_comparar_filas_buscar[2]
                    # texto para notificar error de contenido de base de datos
                    texto_para_error_bd = ControladorTest.texto_comparar_bd_buscar[0]
                    self.ejecuta_caso_de_test(controlador.buscar, i, ControladorTest.texto_casos_buscar[i], indVal,
                                              controlador, iu, ControladorTest.comandos_buscar,
                                              ControladorTest.resultados_esperados_buscar,
                                              controlador_esperado,
                                              texto_para_error_filas, texto_para_error_bd)

        except Exception as ex:
            print("*** Se ha capturado una excepción que probablemente "
                    + "ha sido lanzada por tu código. Mira la traza para "
                    + "detectar en qué punto ha sido creada y lanzada...")
            traceback.print_exc()
            stack = traceback.extract_stack()
            self.printStackTraceUpc(stack)

        self.acumula(SuperClassForTests.puntos)
        self.show_puntos(puntosAntes)

    comandos_eliminar = [
        "coches elimina matricula#1234GGD",
        "coches elimina ",
        "coches elimina marca=Seat",
        "multas elimina cuantia=100",
        "multas elimina cuantia>60",
        "multas elimina cuantia<101",
        "coches elimina marca#Fo",
        "coches elimina marca#Mer",
        "coches elimina marca=Mercedes",
        "multas elimina cuantia=550",
        "multas elimina cuantia>550",
        "multas elimina cuantia<20"
    ]

    texto_casos_eliminar = [
        "\tTest 1. Comando: '" + comandos_eliminar[0] + "'; intento de eliminación en tabla que NO existe. Se devuelve lista vacía. ",
        "\tTest 2: Comando: '" + comandos_eliminar[1] + "'; intento de eliminación sin criterio. Se devuelve lista vacia. ",
        "\tTest 3: Comando: '" + comandos_eliminar[2] + "'; intento de eliminación con criterio = NO numérico. Se devuelve lista con las filas que cumplen el criterio.",
        "\tTest 4: Comando: '" + comandos_eliminar[3] + "'; intento de eliminación con criterio = numérico. Se devuelve lista con las filas que cumplen el criterio.",
        "\tTest 5: Comando: '" + comandos_eliminar[4] + "'; intento de eliminación con criterio > numérico. Se devuelve lista con las filas que cumplen el criterio. ",
        "\tTest 6: Comando: '" + comandos_eliminar[5] + "'; intento de eliminación con criterio < numérico. Se devuelve lista con las filas que cumplen el criterio.",
        "\tTest 7: Comando: '" + comandos_eliminar[6] + "'; intento de eliminación con criterio #. Se devuelve lista con las filas que cumplen el criterio. ",
        "\tTest 8: Comando: '" + comandos_eliminar[7] + "'; intento de eliminación con criterio # que NO se cumple. Se devuelve lista vacía.",
        "\tTest 9: Comando: '" + comandos_eliminar[8] + "'; intento de eliminación con criterio = NO numérico que NO se cumple. Se devuelve lista vacía.",
        "\tTest 10: Comando: '" + comandos_eliminar[9] + "'; intento de eliminación con criterio = numérico que NO se cumple. Se devuelve lista vacía.",
        "\tTest 11: Comando: '" + comandos_eliminar[10] + "'; intento de eliminación con criterio > que NO se cumple. Se devuelve lista vacía. ",
        "\tTest 12: Comando: '" + comandos_eliminar[11] + "'; intento de eliminación con criterio < que NO se cumple. Se devuelve lista vacía."
    ]

    texto_error_filas_eliminar = [
        f"Error. Se intentaba eliminar algo que no existe en la tabla. El comando debería haber devuelto la lista: $A, pero ha devuelto la lista: $B",
        f"Error. El comando no tenía criterio. El comando debería haber devuelto la lista: $A, pero ha devuelto la lista: $B",
        f"Error. El comando debería haber devuelto la lista: $A, pero ha devuelto la lista: $B"
    ]

    texto_error_bd_eliminar = f"Error. La base de datos NO tiene los contenidos esperados. Debería tener $A, pero " \
                                 "tiene $B"

    resultados_esperados_eliminar = [
        "Lista<>",
        "Lista<>",
        "Lista<FilaDatos[marca:Seat,modelo:Ibiza,matricula:B1234XD],FilaDatos[marca:Seat,modelo:Córdoba,matricula:4456GVG]>",
        "Lista<FilaDatos[matricula:B1234XD,cuantia:100],FilaDatos[matricula:1566GGH,cuantia:100]>",
        "Lista<FilaDatos[matricula:B1234XD,cuantia:100],FilaDatos[matricula:2345FXZ,cuantia:101],FilaDatos[matricula:1566GGH,cuantia:100]>",
        "Lista<FilaDatos[matricula:B1234XD,cuantia:100],FilaDatos[matricula:B1234XD,cuantia:60],FilaDatos[matricula:1566GGH,cuantia:100]>",
        "Lista<FilaDatos[marca:Ford,modelo:Fiesta,matricula:2345FXZ],FilaDatos[marca:Ford,modelo:Escort,matricula:4566GGH]>",
        "Lista<>",
        "Lista<>",
        "Lista<>",
        "Lista<>",
        "Lista<>"
    ]

    folder_controladores_eliminar = base_path+"eliminar/"

    def test08_eliminar(self):
        valorTotal = 2
        puntosAntes = SuperClassForTests.puntosTotales
        num_tests = 24
        indVal = valorTotal/num_tests
        toThrow = None
        print(f"\n\tControlador::eliminar(). Valor: {valorTotal}")
        error = None
        toThrow = None
        try:
            controlador = None
            continuar_test = True
            nf_antes = ControladorTest.folder_controladores_eliminar+"todos_casos_antes.xml"

            for i in range(0, 12):
                sigue = True
                try:
                    controlador = self.lector.lee_cnt_from_path(nf_antes)
                    iu = InterfazUsuario(controlador, None)
                    controlador.iu = iu
                    iu.reset_all_last_prints()
                    nf_esperado = ControladorTest.folder_controladores_eliminar + "test_" + str(
                        i + 1) + "_despues.xml"
                    controlador_esperado = self.lector.lee_cnt_from_path(nf_esperado)
                except Exception as ex:
                    print(
                        "*** Contacta con el profesorado. El corrector ha tratado de acceder a un archivo de corrección "
                        + "sin conseguirlo. A continuación se detalla la traza de la excepción.")
                    traceback.print_exc()
                    stack = traceback.extract_stack()
                    self.printStackTraceUpc(stack)
                    sigue=False
                if sigue:
                    if i < 2:
                        texto_para_error_filas = ControladorTest.texto_error_filas_eliminar[i]
                    else:
                        texto_para_error_filas = ControladorTest.texto_error_filas_eliminar[2]
                    # texto para notificar error de contenido de base de datos
                    texto_para_error_bd = ControladorTest.texto_comparar_bd_buscar[0]
                    self.ejecuta_caso_de_test(controlador.eliminar, i, ControladorTest.texto_casos_eliminar[i], indVal,
                                              controlador, iu, ControladorTest.comandos_eliminar,
                                              ControladorTest.resultados_esperados_eliminar,
                                              controlador_esperado,
                                              texto_para_error_filas, texto_para_error_bd)

        except Exception as ex:
            print("*** Se ha capturado una excepción que probablemente "
                    + "ha sido lanzada por tu código. Mira la traza para "
                    + "detectar en qué punto ha sido creada y lanzada...")
            traceback.print_exc()
            stack = traceback.extract_stack()
            self.printStackTraceUpc(stack)
        self.acumula(SuperClassForTests.puntos)
        self.show_puntos(puntosAntes)

    texto_casos_ordenar = [
        "\tTest 1: intento de ordenar una tabla inexistente. Se envía mensaje. La base de datos NO se altera",
        "\tTest 2: intento de ordenar por una columna inexistente. Se envía mensaje. La base de datos NO se altera",
        "\tTest 3: se ordena en orden ascendente. La base de datos se altera",
        "\tTest 4: se ordena en orden descendente. La base de datos se altera",
    ]

    texto_error_mensaje_a_iu_ordenar = [
        f"Error. Se intentaba ordenar una tabla que NO existe. El comando debería haber enviado un mensaje al interfaz "
        +"de usuario, pero NO lo ha hecho",
        f"Error. Se intentaba ordenar por una columna que NO existe. El comando debería haber enviado un mensaje al interfaz "
        +"de usuario, pero NO lo ha hecho",
        "Error. Se intentaba ordenar correctamente la tabla coches por matrículas en orden ascendente. El comando NO debería haber enviado "
        +"un mensaje al interfaz de usuario, pero lo ha hecho.",
        "Error. Se intentaba ordenar correctamente la tabla coches por matrículas en orden descendente. El comando NO debería haber enviado "
        + "un mensaje al interfaz de usuario, pero lo ha hecho."
    ]

    texto_error_bd_ordenar ="Error. La base de datos NO tiene los contenidos esperados. Debería tener\n\t$A \n\tpero " \
                                 "tiene\n\t$B"

    comandos_ordenar = [
        "multa ordena cuantia",
        "multas ordena foo",
        "coches ordena matricula",
        "coches ordena matricula desc"
    ]

    mensaje_a_iu = [True,True,False,False]

    folder_controladores_ordenar = base_path+"ordenar/"

    def test09_ordenar(self):
        valorTotal = 1
        puntosAntes = SuperClassForTests.puntosTotales
        num_tests = 8
        indVal = valorTotal/num_tests
        toThrow = None
        print(f"\n\tControlador::ordenar(). Valor: {valorTotal}")
        error = None
        toThrow = None
        try:
            controlador = None
            continuar_test = True
            nf = ControladorTest.folder_controladores_ordenar + "todos_casos_antes.xml"
            iu = iu = InterfazUsuario(controlador, None)
            try:
                controlador = self.lector.lee_cnt_from_path(nf)
                controlador.iu = iu
                iu.reset_all_last_prints()
                controlador_esperado = self.lector.lee_cnt_from_path(nf)
            except Exception as ex:
                print(
                    "*** Contacta con el profesorado. El corrector ha tratado de acceder a un archivo de corrección "
                    + "sin conseguirlo. A continuación se detalla la traza de la excepción.")
                traceback.print_exc()
                stack = traceback.extract_stack()
                self.printStackTraceUpc(stack)
                contiuar_test = False
            if continuar_test:
                for i in range(0,len(ControladorTest.comandos_ordenar)):
                    nd = ControladorTest.folder_controladores_ordenar + "test_"+str(i+1)+"_despues.xml"
                    continuar = True
                    iu.reset_all_last_prints()
                    try:
                        controlador_esperado = self.lector.lee_cnt_from_path(nd)
                    except Exception as ex:
                        print(
                            "*** Contacta con el profesorado. El corrector ha tratado de acceder a un archivo de corrección "
                            + "sin conseguirlo. A continuación se detalla la traza de la excepción.")
                        traceback.print_exc()
                        stack = traceback.extract_stack()
                        self.printStackTraceUpc(stack)
                    if continuar:
                        controlador.ordenar(ControladorTest.comandos_ordenar[i].split())
                        self.check_caso_ordenar_nuevo(i + 1, ControladorTest.texto_casos_ordenar[i], ControladorTest.mensaje_a_iu[i],
                            controlador_esperado, controlador,
                            ControladorTest.texto_error_mensaje_a_iu_ordenar[i],
                            ControladorTest.texto_error_bd_ordenar, indVal)

        except Exception as ex:
            print("*** Se ha capturado una excepción que probablemente "
                  + "ha sido lanzada por tu código. Mira la traza para "
                  + "detectar en qué punto ha sido creada y lanzada...")
            traceback.print_exc()
            stack = traceback.extract_stack()
            self.printStackTraceUpc(stack)

        self.acumula(SuperClassForTests.puntos)
        self.show_puntos(puntosAntes)

    def check_caso_ordenar_nuevo(self,id,texto,mensaje_a_iu,controlador_esperado,controlador,error_mssg_a_iu,error_mssg_bd,indVal):
        toThrow = None
        print(texto)
        #Comprobar si se ha enviado mensaje a interfaz de usuario o no
        error = self.sAssertEquals(mensaje_a_iu,len(InterfazUsuario.last_println_con_arg)!=0,indVal,error_mssg_a_iu)
        self.toThrow(error,toThrow)
        #Comprobar contenidos de base de datos
        mensaje = StringBuilder()
        iguales = controlador_esperado.compara(controlador,"\t\t\t",mensaje)
        if iguales:
            error = self.sAssertTrue(True,indVal,"")
        else:
            error = self.sAssertFalse(True,0,"Error. El estado del controlador NO es el esperado. En el mensaje "
                                            "que sigue, 'este' es el esperado y 'otro' es el que se ha obtenido\n")
            print(mensaje.to_string())
            self.toThrow(error, toThrow)

    def check_caso_ordenar(self,id,texto,mensaje_a_iu,contenido_bd_esperado,contenido_bd_recuperado,error_mssg_a_iu,error_mssg_bd,indVal):
        toThrow = None
        print(texto)
        #Comprobar si se ha enviado mensaje a interfaz de usuario o no
        mensaje_check_bd = ""
        mensaje_check_bd = error_mssg_bd.replace("$A",contenido_bd_esperado).replace("$B",contenido_bd_recuperado)

        error = self.sAssertEquals(mensaje_a_iu,len(InterfazUsuario.last_println_con_arg)!=0,indVal,error_mssg_a_iu)
        self.toThrow(error,toThrow)
        #Comprobar contenidos de base de datos
        error = self.sAssertEquals(contenido_bd_esperado,contenido_bd_recuperado,indVal,mensaje_check_bd)
        self.toThrow(error,toThrow)

    folder_controladores_exportar = base_path+"exportar/"

    def test10_exportar(self):
        cwd = os.getcwd() + "/paracorreccion/"
        valorTotal = 0.1
        puntosAntes = SuperClassForTests.puntosTotales
        toThrow = None
        print(f"\n\tControlador::exportar(). Valor: {valorTotal}")
        error = None
        toThrow = None
        try:
            exportador = Exportador()
            controlador = None
            continuar = True
            try:
                path = ControladorTest.folder_controladores_exportar+"todos_casos_antes.xml"
                controlador = self.lector.lee_cnt_from_path(path)
                iu = InterfazUsuario(controlador, None)
                controlador.iu = iu
                controlador.exportador = Exportador()
            except Exception as ex:
                print(
                    "*** Contacta con el profesorado. El corrector ha tratado de acceder a un archivo de corrección "
                    + "sin conseguirlo. A continuación se detalla la traza de la excepción.")
                traceback.print_exc()
                stack = traceback.extract_stack()
                self.printStackTraceUpc(stack)
                continuar = False
            if continuar:
                esperado = "coches crea marca modelo *matricula\ncoches añade marca=Seat modelo=Ibiza matricula=B1234XD\n" \
                           "coches añade marca=Seat modelo=Córdoba matricula=4456GVG\ncoches añade marca=Ford " \
                           "modelo=Fiesta matricula=2345FXZ\ncoches añade marca=Ferrari modelo=Testarrossa " \
                           "matricula=1566GGH\ncoches añade marca=Ford modelo=Escort matricula=4566GGH\nmultas " \
                           "crea cuantia *matricula\nmultas añade cuantia=100 matricula=B1234XD\nmultas añade " \
                           "cuantia=101 matricula=2345FXZ\nmultas añade cuantia=60 matricula=B1234XD\nmultas añade " \
                           "cuantia=100 matricula=1566GGH"
                f_name = cwd + "baseDatosExportada_alprog.txt"
                controlador.exporta(f_name)
                exportado = LectorDatos.lee_archivo_sobre_string(f_name)
                error = self.sAssertEquals(esperado,exportado,valorTotal,"Error. Lo exportado no es igual a lo "
                    + "esperado. Se esperaba el siguiente contenido:\n" + esperado
                    + "\nSin embargo se ha obtenido lo siguiente:\n" + exportado)
                self.toThrow(error,toThrow)

        except Exception as ex:
           print("*** Se ha capturado una excepción que probablemente "
                 + "ha sido lanzada por tu código. Mira la traza para "
                 + "detectar en qué punto ha sido creada y lanzada...")
           traceback.print_exc()
           stack = traceback.extract_stack()
           self.printStackTraceUpc(stack)

        self.acumula(SuperClassForTests.puntos)
        self.show_puntos(puntosAntes)

    def ejecuta_caso_de_test(self, metodo, id_test, texto_test, indVal, controlador, iu, comandos, resultados_esperados, controlador_esperado, texto_para_error_filas, texto_para_error_bd):
        print(texto_test)
        comando = comandos[id_test]
        esperado = resultados_esperados[id_test]
        resultado = metodo(comando.split())
        self.check_resultados_busca_y_elimina(esperado, controlador,
                                              ListUtils.lista_a_String(resultado), controlador_esperado, indVal,
                                              texto_para_error_filas, texto_para_error_bd)

    def check_resultados_busca_y_elimina(self, esperado, controlador, resultado, controlador_esperado,
                                         indVal, texto_cmp_resultado, texto_cmp_bd):
        error = None
        toThrow = None
        texto_cmp_resultado = texto_cmp_resultado.replace("$A",esperado).replace("$B",resultado)
        # Comprobar que se ha devuelto la lista esperada
        contenido_devuelto = ListUtils.lista_a_String(resultado)
        error = self.sAssertEquals(esperado, resultado, indVal, texto_cmp_resultado)
        self.toThrow(error, toThrow)
        # Comprobar que no se ha alterado la base de datos
        mensaje = StringBuilder()
        iguales = controlador_esperado.compara(controlador,"\t\t\t",mensaje)
        if iguales:
            error = self.sAssertTrue(True,indVal,"")
        else:
            error = self.sAssertFalse(True,0,"Error. El estado del controlador NO es el esperado. En el mensaje "
                                            "que sigue, 'este' es el esperado y 'otro' es el que se ha obtenido\n")
            print(mensaje.to_string())
            self.toThrow(error, toThrow)

