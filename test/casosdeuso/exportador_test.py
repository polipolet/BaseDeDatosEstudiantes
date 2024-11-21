import traceback
import os
from src.casosdeuso.exportador import Exportador
from test.CorrectorGlobal import SuperClassForTests
from test.utils.lector_datos import LectorDatos

class ExportadorTest(SuperClassForTests):


    numErrorsBefore = 0

    numInstances = 0

    nota = 0.0

    def __init__(self,*args, **kwargs):
        SuperClassForTests.__init__(self, *args, **kwargs)
        ExportadorTest.numInstances = ExportadorTest.numInstances + 1
        if ExportadorTest.numInstances == 1:
            ExportadorTest.numErrorsBefore = len(SuperClassForTests.indErrors)
        self.lector = LectorDatos()


    def setUpClass():
        # SuperClassForTests.nota = {}
        ExportadorTest.nota = 0.0
        print("\n\nCORRIGIENDO clase Exportador")
        print("**************************")

    def tearDownClass():
        SuperClassForTests.showErrors(SuperClassForTests.indErrors, "Exportador")
        SuperClassForTests.acumulaErrores()
        SuperClassForTests.indErrors = []
        ExportadorTest.nota = SuperClassForTests.puntosTotales
        SuperClassForTests.puntosTotales = 0

    def setUp(self):
        pass

    def tearDown(self):
        pass

    base_path = os.getcwd() + "/paracorreccion/para_correctores/controlador_test/"

    def test01_exportar(self):
        valorTotal = 10
        puntosAntes = SuperClassForTests.puntosTotales
        toThrow = None
        print(f"\n\tExportador::exportar(). Valor: {valorTotal}")
        error = None
        toThrow = None
        try:
            exportador = Exportador()
            controlador = None
            continuar = True
            try:
                path = os.getcwd() + "/paracorreccion/para_correctores/controlador_test/exportar/todos_casos_antes.xml"
                controlador = self.lector.lee_cnt_from_path(path)
                controlador.exportador = exportador
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
                f_name = os.getcwd() + "/paracorreccion/para_correctores/controlador_test/exportar/baseDatosExportada_alprog.txt"
                exportador.exporta(controlador.tablas,f_name)
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

