from src.dominio.clave import Clave
from src.dominio.esquema import Esquema
from src.dominio.criterios.criterio_igual import CriterioIgual
from src.dominio.criterios.criterio_mayor_que import CriterioMayorQue
from src.dominio.criterios.criterio_menor_que import CriterioMenorQue
from src.dominio.criterios.criterio_contiene import CriterioContiene

from src.dominio.excepcionesDominio import ClaveYaExisteException, ClaveInexistenteException, ValorClaveUnicaException
from src.dominio.fila_datos import FilaDatos
from src.dominio.tabla import Tabla
import traceback
from test.CorrectorGlobal import SuperClassForTests


class Tabla2Test(SuperClassForTests):


    numErrorsBefore = 0

    numInstances = 0

    nota = 0.0


    def __init__(self,*args, **kwargs):
        SuperClassForTests.__init__(self, *args, **kwargs)
        Tabla2Test.numInstances = Tabla2Test.numInstances + 1
        if Tabla2Test.numInstances == 1:
            Tabla2Test.numErrorsBefore = len(SuperClassForTests.indErrors)
        self.filas_creadas_array = []
        self.filas_creadas = set()
        self.indices_para_check_busca = {
            "None": [0,1,2,3,4],
            "Igual": [0,4],
            "MayorQue": [1,2,3],
            "MenorQue": [0,1,2,4],
            "Contiene": [0,2,4]
        }
        self.indices_para_check_elimina ={
            "None": [],
            "Igual": [0,4],
            "MayorQue": [1,2,3],
            "MenorQue": [0,1,2,4],
            "Contiene": [0,2,4]
        }
        self.indices_dejados_por_elimina = {
            "None": [0,1,2,3,4],
            "Igual": [1,2,3],
            "MayorQue": [0,4],
            "MenorQue": [3],
            "Contiene": [1,3]
        }

    def setUpClass():
        # SuperClassForTests.nota = {}
        Tabla2Test.nota = 0.0
        print("\n\nCorrigiendo los métodos que se listan a contiunuación de Tabla:\n\t "
                + "public List<FilaDatos> busca(Criterio criterio).\n\t "
                + "public List<FilaDatos> elimina(Criterio criterio).")
        print("**********************************")

    def tearDownClass():
        SuperClassForTests.showErrors(SuperClassForTests.indErrors, "Tabla2")
        SuperClassForTests.acumulaErrores()
        SuperClassForTests.indErrors = []
        Tabla2Test.nota = SuperClassForTests.puntosTotales
        SuperClassForTests.puntosTotales = 0

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test01_busca(self):
        valorTotal = 4.0
        puntosAntes = SuperClassForTests.puntosTotales
        num_tests = 5
        toThrow = None
        print(f"\n\tTabla::busca(). Valor: {valorTotal}")
        try:
            esquema = self.create_esquema()
            nombre = "nombreTabla"
            tabla = Tabla(nombre, esquema)
            self.add_filas_a_tabla(tabla)
            print(f"\tTest 1: Se invoca con un argumento null. Debe devolver todas las filas de la tabla")
            result = tabla.busca(None)
            self.check_busca_result_con_criterio("None",result,valorTotal/num_tests)
            #
            print("\tTest 2: Se invoca con un objeto CriterioIgual.")
            criterio = CriterioIgual("nombreClave-1","1.0")
            result = tabla.busca(criterio)
            self.check_busca_result_con_criterio("Igual",result, valorTotal/num_tests);
            #
            print("\tTest 3: Se invoca con un objeto CriterioMayorQue.")
            criterio = CriterioMayorQue("nombreClave-1","1.0")
            result = tabla.busca(criterio)
            self.check_busca_result_con_criterio("MayorQue",result, valorTotal/num_tests);
            #
            print("\tTest 4: Se invoca con un objeto CriterioMenorQue.")
            criterio = CriterioMenorQue("nombreClave-1","16.0")
            result = tabla.busca(criterio)
            self.check_busca_result_con_criterio("MenorQue",result, valorTotal/num_tests);
            #
            print("\tTest 5: Se invoca con un objeto CriterioContiene.")
            criterio = CriterioContiene("nombreClave-2","2")
            result = tabla.busca(criterio)
            self.check_busca_result_con_criterio("Contiene",result, valorTotal/num_tests);

        except Exception as ex:
            print("*** Se ha capturado una excepción que probablemente "
                    + "ha sido lanzada por tu código. Mira la traza para "
                    + "detectar en qué punto ha sido creada y lanzada...")
            traceback.print_exc()
            stack = traceback.extract_stack()
            self.printStackTraceUpc(stack)

        self.acumula(SuperClassForTests.puntos)
        self.show_puntos(puntosAntes)

    def test02_elimina(self):
        valorTotal = 6.0
        puntosAntes = SuperClassForTests.puntosTotales
        num_tests = 5
        toThrow = None
        print(f"\n\tTabla::elimina(). Valor: {valorTotal}")
        try:
            esquema = self.create_esquema()
            nombre = "nombreTabla"
            tabla = Tabla(nombre, esquema)
            self.add_filas_a_tabla(tabla)
            print("\tTest 1: Se invoca con un argumento null. Debe devolver una lista vacía y dejar la lista de "
                  +"filas de la tabla inalterada")
            self.check_elimina_result_con_criterio("None",tabla,None,valorTotal/num_tests)
            #
            print("\tTest 2: Se invoca con un objeto CriterioIgual. Deve devolver 2 filas y dejar 3 en la tabla")
            criterio = CriterioIgual("nombreClave-1","1.0")
            self.check_elimina_result_con_criterio("Igual",tabla,criterio, valorTotal/num_tests);
            #
            print("\tTest 3: Se invoca con un objeto CriterioMayorQue. Debe devolver 3 y dejar 2")
            tabla = Tabla(nombre, esquema)
            self.add_filas_a_tabla(tabla)
            criterio = CriterioMayorQue("nombreClave-1","1.0")
            self.check_elimina_result_con_criterio("MayorQue",tabla,criterio,valorTotal/num_tests);
            #
            print("\tTest 4: Se invoca con un objeto CriterioMenorQue. Debe eliminar 4 y dejar 1")
            tabla = Tabla(nombre, esquema)
            self.add_filas_a_tabla(tabla)
            criterio = CriterioMenorQue("nombreClave-1","16.0")
            self.check_elimina_result_con_criterio("MenorQue",tabla,criterio, valorTotal/num_tests);
            #
            print("\tTest 5: Se invoca con un objeto CriterioContiene. Debe eliminar 3 y dejar 2")
            tabla = Tabla(nombre, esquema)
            self.add_filas_a_tabla(tabla)
            criterio = CriterioContiene("nombreClave-2","2")
            self.check_elimina_result_con_criterio("Contiene",tabla,criterio, valorTotal/num_tests);

        except Exception as ex:
            print("*** Se ha capturado una excepción que probablemente "
                    + "ha sido lanzada por tu código. Mira la traza para "
                    + "detectar en qué punto ha sido creada y lanzada...")
            traceback.print_exc()
            stack = traceback.extract_stack()
            self.printStackTraceUpc(stack)

        self.acumula(SuperClassForTests.puntos)
        self.show_puntos(puntosAntes)

    def check_elimina_result_con_criterio(self,nombre_criterio,tabla,criterio,valor):
        error = None
        toThrow = None
        return_expected = set()
        indices = self.indices_para_check_elimina[nombre_criterio]
        for i in indices:
            return_expected.add(tabla.filas[i])
        self.toThrow(error,toThrow)
        #Comprobar cómo queda la tabla
        indices_en_tablas = self.indices_dejados_por_elimina[nombre_criterio]
        dejadas_expected = set()
        for i in indices_en_tablas:
            dejadas_expected.add(tabla.filas[i])
        resultado = tabla.elimina(criterio)
        #Comprobar lista devuelta
        error = self.sAssertEquals(return_expected,set(resultado),valor*0.5, "Error. La lista devuelta NO contiene "
             + "las filas esperadas")
        self.toThrow(error,toThrow)
        error = self.sAssertEquals(dejadas_expected,set(tabla.filas), valor*0.5, "Error. La tabla NO HA QUEDADO "
            + "las filas esperadas")
        self.toThrow(error,toThrow)


    def check_busca_result_con_criterio(self,criterio,resultado,valor):
        error = None
        toThrow = None
        return_expected = set()
        indices = self.indices_para_check_busca[criterio]
        for i in indices:
            return_expected.add(self.filas_creadas_array[i])
        #Comprobar lista devuelta
        error = self.sAssertEquals(return_expected,set(resultado),valor, "Error. La lista devuelta NO contiene "
            "las filas esperadas")
        self.toThrow(error,toThrow)

    def create_esquema(self):
        esquema = Esquema()
        clave = None
        try:
            for i in range(0,5):
                if i!=3:
                    clave = Clave("nombreClave-"+str(i+1),False)
                else:
                    clave = Clave("nombreClave-" + str(i + 1), True)
                esquema.add_clave(clave)
        except ClaveYaExisteException as ex:
            print("\n\tError al crear el esquema. No debería darse si el corrector "
                          + "ha otorgado las máximas puntuaciones en las clases Clave, Esquema y "
                          + "se han creado correctamente las clases BaseDatosException, "
                          + "ClaveYaExisteException, ClaveInexistenteException. Si todas estas "
                          + "condiciones se dan, consulta con el profesorado")
            return None
        return esquema

    def create_fila_datos(self):
        result = []
        valor = 1.0
        for j in range(0,4):
            fila = FilaDatos()
            for i in range(0,5):
                fila.put("nombreClave-"+str(i+1),str(valor))
                valor = valor + 1.0
            result.append(fila)
        return result

    def add_filas_a_tabla(self,tabla):
        filas = self.create_fila_datos()
        for fila in filas:
            try:
                tabla.anyade(fila)
                self.filas_creadas_array.append(fila)
                self.filas_creadas.add(fila)
            except  ValorClaveUnicaException or ClaveInexistenteException as ex:
                print("Contacta con el profesorado. El "
                        + "corrector ha generado una fila de datos inválida cuando "
                        + "debería haberla generado válida. Excepción lanzada: "
                        + ex.__class__.__name__)
        fila = FilaDatos()
        valor = 1.0
        for i in range(0,5):
            if i==3:
                fila.put("nombreClave-" + str(i+1),"37")
            else:
                fila.put("nombreClave-" + str(i + 1),str(valor))
            valor = valor +1.0
        self.filas_creadas_array.append(fila)
        self.filas_creadas.add(fila)
        try:
            tabla.anyade(fila)
        except ValorClaveUnicaException or ClaveInexistenteException as ex:
            print("ERROR en Tabla2Test::add_filas_a_tabla(). Contacta con el profesorado. El "
                  + "corrector ha generado una fila de datos inválida cuando "
                  + "debería haberla generado válida. Excepción lanzada: "
                  + ex.__class__.__name__)
            traceback.print_exc()
            stack = traceback.extract_stack()
            self.printStackTraceUpc(stack)

    def create_fila_datos_valida(self):
        fila = FilaDatos()
        for i in range(0,5):
            fila.put("nombreClave-" + str(i + 1), "valor-" + str(i + 1))
        return fila

    def create_otra_fila_datos_valida(self):
        fila = FilaDatos()
        for i in range(0,5):
            fila.put("nombreClave-" + str(i + 1), "valor-" + str(i + 500))
        return fila

    def create_tercera_fila_datos_valida(self):
        fila = FilaDatos()
        for i in range(0,5):
            fila.put("nombreClave-" + str(i + 1), "valor-" + str(i + 200))
        return fila

    def create_otra_fila_datos_no_valida_por_valor_clave_unica(self):
        fila = FilaDatos()
        for i in range(0,5):
            fila.put("nombreClave-" + str(i + 1), "valor-" + str(i + 1))
        return fila

    def create_otra_fila_datos_no_valida_por_clave_inexistente(self):
        fila = FilaDatos()
        for i in range(0,5):
            if i==3:
                fila.put("nombreClave-" + str(i + 1),"valor-200")
            elif i==1:
                fila.put("nombreClave-20" , "valor-200")
            else:
                fila.put("nombreClave-" + str(i + 1), "valor-" + str(i + 1))
        return fila

    def create_fila_datos_no_valida_por_tamanyo(self):
        fila = FilaDatos()
        for i in range(0,4):
            if i==3:
                fila.put("nombreClave-" + str(i + 1), "valor-350")
            else:
                fila.put("nombreClave-" + str(i + 1), "valor-" + str(i + 1))
        return fila

    def create_fila_datos_no_valida_por_clave(self):
        fila = FilaDatos()
        for i in range(0,4):
            if i<4:
                fila.put("nombreClave-" + str(i + 1), "valor-" + str(i + 1))
            else:
                fila.put("malNombreClave", "valor-" + str(i + 1))
        return fila
