from src.dominio.clave import Clave
import traceback
from test.CorrectorGlobal import SuperClassForTests

class ClaveTest(SuperClassForTests):


    numErrorsBefore = 0

    numInstances = 0

    nota = 0.0

    def __init__(self,*args, **kwargs):
        SuperClassForTests.__init__(self, *args, **kwargs)
        ClaveTest.numInstances = ClaveTest.numInstances + 1
        if ClaveTest.numInstances == 1:
            ClaveTest.numErrorsBefore = len(SuperClassForTests.indErrors)


    def setUpClass():
        # SuperClassForTests.nota = {}
        ClaveTest.nota = 0.0
        print("\n\nCORRIGIENDO clase Clave")
        print("**************************")

    def tearDownClass():
        SuperClassForTests.showErrors(SuperClassForTests.indErrors, "Clave")
        SuperClassForTests.acumulaErrores()
        SuperClassForTests.indErrors = []
        ClaveTest.nota = SuperClassForTests.puntosTotales
        SuperClassForTests.puntosTotales = 0

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test01__init__(self):
        valorTotal = 8.0
        puntosAntes = SuperClassForTests.puntosTotales
        nombre = "claveUnica"
        unica = True
        try:
            print(f"\n\tClave::__init__(nombre,unica). Valor: {valorTotal}" );
            instance = Clave(nombre, unica);
            self.checkAttributeAfterConstructor(instance, "nombre", nombre,
                    valorTotal, 0.25, 0.25, 1);
            self.checkAttributeAfterConstructor(instance, "unica", unica,
                    valorTotal, 0.25, 0.25, 3);
        except Exception as ex:
            print("*** Se ha capturado una excepción que probablemente "
                    + "ha sido lanzada por tu código. Mira la traza para "
                    + "detectar en qué punto ha sido creada y lanzada...")
            traceback.print_exc()
            stack = traceback.extract_stack()
            self.printStackTraceUpc(stack)

        self.acumula(SuperClassForTests.puntos)
        self.show_puntos(puntosAntes)

    def test02_get_nombre(self):
        valorTotal = 1.0
        puntosAntes = SuperClassForTests.puntosTotales
        nombre = "claveUnica"
        unica = True
        toThrow = None
        #
        try:
            print(f"\n\tClave::get_nombre()). Valor:  {valorTotal}")
            print("\tTest 1: comprobar que se retorna el valor del atributo "
                    + " 'nombre' al invocar este método.")
            instance = Clave.create_with_name_only(nombre)
            error = self.checkFieldValue("nombre",instance,instance.get_nombre(),valorTotal,toThrow)
            self.toThrow(error, toThrow);
        except Exception as ex:
            print("*** Se ha capturado una excepción que probablemente "
                  + "ha sido lanzada por tu código. Mira la traza para "
                  + "detectar en qué punto ha sido creada y lanzada...")
            self.printStackTraceUpc(ex)

        self.acumula(SuperClassForTests.puntos)
        self.show_puntos(puntosAntes)

    def test03_is_unica(self):
        valorTotal = 1.0
        puntosAntes = SuperClassForTests.puntosTotales
        nombre = "claveUnica"
        unica = True
        toThrow = None
        #
        try:
            print(f"\n\tClave::is_unica()). Valor:  {valorTotal}")
            print("\tTest 1: comprobar que se retorna el valor del atributo "
                    + " 'unica' al invocar este método.")
            instance = Clave(nombre,unica)
            error = self.checkFieldValue("unica",instance,instance.is_unica(),valorTotal,toThrow)
            self.toThrow(error, toThrow);
        except Exception as ex:
            print("*** Se ha capturado una excepción que probablemente "
                  + "ha sido lanzada por tu código. Mira la traza para "
                  + "detectar en qué punto ha sido creada y lanzada...")
            self.printStackTraceUpc(ex)

        self.acumula(SuperClassForTests.puntos)
        self.show_puntos(puntosAntes)


