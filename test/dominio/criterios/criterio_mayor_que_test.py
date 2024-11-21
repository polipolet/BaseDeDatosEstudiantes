from test.CorrectorGlobal import SuperClassForTests
from src.dominio.criterios.criterio_mayor_que import CriterioMayorQue
from src.dominio.fila_datos import FilaDatos
import traceback

class CriterioMayorQueTest(SuperClassForTests):


    numErrorsBefore = 0

    numInstances = 0

    nota = 0.0

    def __init__(self,*args, **kwargs):
        SuperClassForTests.__init__(self, *args, **kwargs)
        CriterioMayorQueTest.numInstances = CriterioMayorQueTest.numInstances + 1
        if CriterioMayorQueTest.numInstances == 1:
            CriterioMayorQueTest.numErrorsBefore = len(SuperClassForTests.indErrors)


    def setUpClass():
        # SuperClassForTests.nota = {}
        CriterioMayorQueTest.nota = 0.0
        print("\n\nCORRIGIENDO clase CriterioMayorQue")
        print("**************************")

    def tearDownClass():
        SuperClassForTests.showErrors(SuperClassForTests.indErrors, "CriterioMayorQue")
        SuperClassForTests.acumulaErrores()
        SuperClassForTests.indErrors = []
        CriterioMayorQueTest.nota = SuperClassForTests.puntosTotales
        SuperClassForTests.puntosTotales = 0

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test01__init__(self):
        valorTotal = 1.0
        num_tests = 6
        toThrow = None
        error = None
        puntosAntes = SuperClassForTests.puntosTotales
        try:
            print(f"\n\tCriterioMayorQue::__init__(nombre_clave,valor_a_comprobar). Valor: {valorTotal}" )
            individual_per = valorTotal/num_tests
            nombre_clave = "nombreClave-1"
            valor_a_comparar = "20"
            instance = CriterioMayorQue(nombre_clave,valor_a_comparar)
            #Comprobar atributo 'nombre_clave'
            self.checkAttributeAfterConstructor(instance,"nombre_clave",nombre_clave,valorTotal,individual_per,individual_per,1)
            #Comprobar atributo 'valor_a_comparar'
            self.checkAttributeAfterConstructor(instance,"valor_a_comparar",valor_a_comparar,valorTotal,individual_per,individual_per,3)
            #Comprobar atributo 'valor_numerico_a_comparar'
            self.checkAttributeAfterConstructor(instance,"valor_numerico_a_comparar",float(valor_a_comparar),valorTotal,individual_per,individual_per,3)
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
            print(f"\n\tCriterioMayorQue::se_cumple(filaDatos). Valor: {valorTotal}" )
            fila = self.crear_fila_datos_valida()
            nombre_clave = "nombreClave-1"
            valor_a_comparar = "19.0"
            instance = CriterioMayorQue(nombre_clave,valor_a_comparar)
            print("\tTest 1: comprobación cuando la fila de datos tiene mapeado con la clave un valor (20.0) mayor que "
                  +"el valor a comprobar (19.0)")
            error = self.sAssertTrue(instance.se_cumple(fila),valorTotal/num_tests,"Error. La fila de datos tenía "
                + "mapeado con la clave un valor mayor que el valor a comprobar, pero el método ha devuelto False")
            self.toThrow(error,toThrow)
            #
            print("\tTest 2: comprobación cuando la fila de datos tiene mapeado con la clave un valor (20.0) menor que "
                  "el valor a comprobar (23.0)")
            valor_a_comparar = "23.0"
            instance = CriterioMayorQue(nombre_clave,valor_a_comparar)
            error = self.sAssertFalse(instance.se_cumple(fila),valorTotal/num_tests,"Error. La fila de datos tenía "
                + "mapeado con la clave un valor menor que valor a comprobar, pero el método ha devuelto True")
            self.toThrow(error,toThrow)
            #
            print("\tTest 3: comprobación cuando la fila de datos tiene mapeado con la clave un valor (20.0) igual que "
                  "el valor a comprobar (20.0)")
            valor_a_comparar = "20.0"
            instance = CriterioMayorQue(nombre_clave,valor_a_comparar)
            error = self.sAssertFalse(instance.se_cumple(fila),valorTotal/num_tests,"Error. La fila de datos tenía "
                + "mapeado con la clave un valor igual que valor a comprobar, pero el método ha devuelto True")
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
            fila.put("nombreClave-" + str(i+1),""+str(i+20.0))
        return fila
