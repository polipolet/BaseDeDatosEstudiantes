from test.CorrectorGlobal import SuperClassForTests
from src.dominio.criterios.criterio_contiene import CriterioContiene
from src.dominio.fila_datos import FilaDatos
import traceback

class CriterioContieneTest(SuperClassForTests):


    numErrorsBefore = 0

    numInstances = 0

    nota = 0.0

    def __init__(self,*args, **kwargs):
        SuperClassForTests.__init__(self, *args, **kwargs)
        CriterioContieneTest.numInstances = CriterioContieneTest.numInstances + 1
        if CriterioContieneTest.numInstances == 1:
            CriterioContieneTest.numErrorsBefore = len(SuperClassForTests.indErrors)


    def setUpClass():
        # SuperClassForTests.nota = {}
        CriterioContieneTest.nota = 0.0
        print("\n\nCORRIGIENDO clase CriterioContiene")
        print("**************************")

    def tearDownClass():
        SuperClassForTests.showErrors(SuperClassForTests.indErrors, "CriterioContiene")
        SuperClassForTests.acumulaErrores()
        SuperClassForTests.indErrors = []
        CriterioContieneTest.nota = SuperClassForTests.puntosTotales
        SuperClassForTests.puntosTotales = 0

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test01__init__(self):
        valorTotal = 1.0
        num_tests = 4
        toThrow = None
        error = None
        puntosAntes = SuperClassForTests.puntosTotales
        try:
            print(f"\n\tCriterioContiene::__init__(nombre,unica). Valor: {valorTotal}" )
            individual_per = valorTotal/num_tests
            nombre_clave = "nombreClave-1"
            valor_a_comparar = "valor-1"
            instance = CriterioContiene(nombre_clave,valor_a_comparar)
            #Comprobar atributo 'nombre_clave'
            self.checkAttributeAfterConstructor(instance,"nombre_clave",nombre_clave,valorTotal,individual_per,individual_per,1)
            #Comprobar atributo 'valor_a_comparar'
            self.checkAttributeAfterConstructor(instance,"valor_a_comparar",valor_a_comparar,valorTotal,individual_per,individual_per,3)
        except Exception as ex:
            print("*** Se ha capturado una excepción que probablemente "
                    + "ha sido lanzada por tu código. Mira la traza para "
                    + "detectar en qué punto ha sido creada y lanzada...")
            traceback.print_exc()
            stack = traceback.extract_stack()
            self.printStackTraceUpc(stack)

        self.acumula(SuperClassForTests.puntos)
        self.show_puntos(puntosAntes)


    def test02_se_cumple(self):
        valorTotal = 9.0
        num_tests = 3
        toThrow = None
        error = None
        puntosAntes = SuperClassForTests.puntosTotales
        try:
            print(f"\n\tCriterioContiene::se_cumple(filaDatos). Valor: {valorTotal}" )
            fila = self.crear_fila_datos_valida()
            nombre_clave = "nombreClave-1"
            valor_a_comparar = "val"
            instance = CriterioContiene(nombre_clave,valor_a_comparar)
            print("\tTest 1: comprobación cuando la fila de datos tiene mapeado con la clave un valor (\'valor-1\') que contiene al "
                  + "valor a comprobar (\'val\') pero que no es igual")
            error = self.sAssertTrue(instance.se_cumple(fila),valorTotal/num_tests,"Error. La fila de datos tenía "
                + "mapeado con la clave un valor que contiene al valor a comprobar (no igual), pero el método ha devuelto False")
            self.toThrow(error,toThrow)
            #
            print("\tTest 2: comprobación cuando la fila de datos tiene mapeado con la clave un valor (\'valor-1\') igual "
                  + "al valor a comprobar (\'valor-1\'), y por tanto, lo contiene")
            instance = CriterioContiene(nombre_clave,"valor-1")
            error = self.sAssertTrue(instance.se_cumple(fila),valorTotal/num_tests,"Error. La fila de datos tenía "
                + "mapeado con la clave un valor igual al valor a comprobar, pero el método ha devuelto False")
            self.toThrow(error,toThrow)
            #
            print("\tTest 3: comprobación cuando la fila de datos tiene mapeado con la clave un valor (\'valor-1\') que NO contiene "
                  + "al valor a comprobar (\'otro\')")
            instance = CriterioContiene(nombre_clave,"otro")
            error = self.sAssertFalse(instance.se_cumple(fila),valorTotal/num_tests,"Error. La fila de datos tenía "
                + "mapeado con la clave un valor que NO contiene al valor a comprobar, pero el método ha devuelto True")
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

    def crear_fila_datos_valida(self):
        fila = FilaDatos()
        for i in range(0,5):
            fila.put("nombreClave-" + str(i+1),"valor-"+str(i+1))
        return fila
