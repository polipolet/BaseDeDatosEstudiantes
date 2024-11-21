from src.dominio.clave import Clave
from src.dominio.esquema import Esquema
from src.dominio.excepcionesDominio import ClaveYaExisteException
import traceback
from test.CorrectorGlobal import SuperClassForTests

class EsquemaTest(SuperClassForTests):


    numErrorsBefore = 0

    numInstances = 0

    nota = 0.0

    def __init__(self,*args, **kwargs):
        SuperClassForTests.__init__(self, *args, **kwargs)
        EsquemaTest.numInstances = EsquemaTest.numInstances + 1
        if EsquemaTest.numInstances == 1:
            EsquemaTest.numErrorsBefore = len(SuperClassForTests.indErrors)


    def setUpClass():
        # SuperClassForTests.nota = {}
        EsquemaTest.nota = 0.0
        print("\n\nCORRIGIENDO clase Esquema")
        print("**************************")

    def tearDownClass():
        SuperClassForTests.showErrors(SuperClassForTests.indErrors, "Esquema")
        SuperClassForTests.acumulaErrores()
        SuperClassForTests.indErrors = []
        EsquemaTest.nota = SuperClassForTests.puntosTotales
        SuperClassForTests.puntosTotales = 0

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test01__init__(self):
        valorTotal = 1.0
        puntosAntes = SuperClassForTests.puntosTotales
        nombre = "claveUnica"
        unica = True
        toThrow = None
        try:
            print(f"\n\tEsquema::__init__(nombre,unica). Valor: {valorTotal}" )
            instance = Esquema();
            print("\tTest 1: comprobando que el objeto de clae Esquema tiene un atributo 'campos'")
            error = self.checkFieldExists("campos",instance,valorTotal/3,toThrow)
            self.toThrow(error,toThrow)
            if instance.campos is not None:
                print("\tTest 2: comprobando que el atributo 'campos' es de la clase adecuada")
                error = self.checkFieldIsOfASpecificClassByName("campos",instance,"dict",valorTotal/3,toThrow)
                self.toThrow(error, toThrow)
                print("\tTest 3: comprobando que el atributo 'campos' es un contenedor vacío")
                error=self.sAssertEquals(0,len(instance.campos),valorTotal/3,"Error: el contenedor 'campos' debería "
                                       + f"estar vacío; sin embargo tiene {len(instance.campos)} elementos")
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

    def test02_add_clave(self):
        valorTotal = 6.0
        puntosAntes = SuperClassForTests.puntosTotales
        nombre = "claveUnica"
        unica = True
        toThrow = None
        print(f"\n\tEsquema::add_clave(...). Valor: {valorTotal}")
        try:
            print("\tTest 1: se añade una clave que no existía en el esquema ")
            clave = Clave.create_with_name_only("nombreClave")
            instance = Esquema()
            instance.add_clave(clave)
            error = self.sAssertTrue(instance.campos.get("nombreClave") is not None, valorTotal/3,"Error: debería "
                        + "haberse añadido un par <clave valor>, pero no se ha "
                        + "encontrado ningún par con la clave correcta")
            toThrow = self.toThrow(error,toThrow)
            #
            if error is None:
                clave_retornada = instance.campos.get("nombreClave")
                error = self.sAssertEquals(clave,clave_retornada, valorTotal/3,"Error: debería "
                        + "haberse añadido un par <clave valor>, pero la clave mapeada con "
                        + "el nombre NO es correcta")
                toThrow = self.toThrow(error,toThrow)
            #
            print("\tTest 2: se añade una clave que ya existía en el esquema ")
            clave = Clave.create_with_name_only("nombreClave")
            try:
                instance.add_clave(clave)
                error = self.sAssertTrue(False,0, "Error: al "
                        + "intentar añadir una clave con un nombre de otra clave "
                        + "ya presente en el esquema debería haberse arrojado "
                        + "una excepción ClaveYaExisteException, pero NO "
                        + "se ha arrojado ninguna excepción")
                toThrow = self.toThrow(error, toThrow)
            except Exception as ex:
                if isinstance(ex,ClaveYaExisteException):
                    error = self.sAssertTrue(True,valorTotal/3,"")
                else:
                    error = self.sAssertTrue(False,0,"Error: al "
                            + "intentar añadir una clave con un nombre de otra clave "
                            + "ya presente en el esquema debería haberse arrojado "
                            + "una excepción ClaveYaExisteException; se ha arrojado "
                            + "una excepción, pero NO de esa clase sino de la clase "
                            + type(ex).__name__)
                    toThrow = self.toThrow(error, toThrow)

        except Exception as ex:
            print("*** Se ha capturado una excepción que probablemente "
                    + "ha sido lanzada por tu código. Mira la traza para "
                    + "detectar en qué punto ha sido creada y lanzada...")
            traceback.print_exc()
            stack = traceback.extract_stack()
            self.printStackTraceUpc(stack)

        self.acumula(SuperClassForTests.puntos)
        self.show_puntos(puntosAntes)

    def test03_contiene_clave(self):
        valorTotal = 1.0
        puntosAntes = SuperClassForTests.puntosTotales
        nombre = "claveUnica"
        unica = True
        toThrow = None
        try:
            print(f"\n\tEsquema::contiene_clave(...). Valor: {valorTotal}" )
            clave = Clave.create_with_name_only("nombreClave")
            instance = Esquema();
            instance.add_clave(clave);
            #
            print("\tTest 1: se invoca pasando un nombre de clave que NO está en el esquema ")
            error = self.sAssertFalse(instance.contiene_clave("otroNombre"),
                    valorTotal / 2, "Error: se ha pasado el nombre de una clave que NO está en el "
                    + "esquema, y sin embargo, el método ha devuelto el valor True");
            self.toThrow(error, toThrow);
            #
            print("\tTest 2: se invoca pasando un nombre de clave que ESTÁ en el esquema ")
            error = self.sAssertTrue(instance.contiene_clave("nombreClave"),
                    valorTotal / 2, "Error: se ha pasado el nombre de una clave que SÍ está en el "
                    + "esquema, y sin embargo, el método ha devuelto el valor false");
            self.toThrow(error, toThrow);
        except Exception as ex:
            print("*** Se ha capturado una excepción que probablemente "
                  + "ha sido lanzada por tu código. Mira la traza para "
                  + "detectar en qué punto ha sido creada y lanzada...")
            traceback.print_exc()
            stack = traceback.extract_stack()
            self.printStackTraceUpc(stack)

        self.acumula(SuperClassForTests.puntos)
        self.show_puntos(puntosAntes)

    def test03_get_lista_de_claves(self):
        valorTotal = 1.0
        puntosAntes = SuperClassForTests.puntosTotales
        nombre = "claveUnica"
        unica = True
        toThrow = None
        try:
            print(f"\n\tEsquema::get_lista_de_claves(). Valor: {valorTotal}" )
            instance = Esquema();
            clave1 = Clave.create_with_name_only("nombreClave")
            instance.add_clave(clave1);
            clave2 = Clave.create_with_name_only("otroNombreClave")
            instance.add_clave(clave2)
            instance2 = Esquema()
            #
            print("\tTest 1: se invoca con un esquema en el que no hay ninguna clave")
            error = self.sAssertTrue(len(instance2.get_lista_de_claves())==0,
                    valorTotal / 3, "Error: se ha invocado el método de una lista sin claves "
                    + "y sin embargo, el método ha devuelto una lista NO vacía")
            self.toThrow(error, toThrow)
            #
            print("\tTest 2: se invoca con un esquema en el que hay dos claves")
            #Comprueba el número de claves
            lista_claves = instance.get_lista_de_claves()
            num_claves = len(lista_claves)
            error = self.sAssertTrue(num_claves==2,
                    valorTotal / 3, "Error: se ha invocado el método de una lista con dos claves "
                    + f"y sin embargo, el método ha devuelto una lista con {num_claves} claves")
            self.toThrow(error, toThrow)
            #Comprueba las dos claves
            if num_claves == 2:
                error = self.sAssertTrue(clave1 in lista_claves and clave2 in lista_claves,
                        valorTotal / 3, "Error: se ha invocado el método de una lista con dos claves "
                        + f"y sin embargo, el método ha devuelto una lista que no tiene ambas claves")
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

    def test_05_get_num_campos(self):
        valorTotal = 1.0
        puntosAntes = SuperClassForTests.puntosTotales
        nombre = "claveUnica"
        unica = True
        toThrow = None
        try:
            print(f"\n\tEsquema::get_num_campos(). Valor: {valorTotal}" );
            instance = Esquema();
            clave1 = Clave.create_with_name_only("nombreClave")
            instance.add_clave(clave1);
            clave2 = Clave.create_with_name_only("otroNombreClave")
            instance.add_clave(clave2)
            returned = instance.get_num_campos()
            error = self.sAssertEquals(2, returned, valorTotal, "Error: "
                    + "se ha creado un esquema con dos claves; sin embargo el método "
                    + f"ha devuelto el valor: {returned}")
            self.toThrow(error, toThrow);

        except Exception as ex:
            print("*** Se ha capturado una excepción que probablemente "
                  + "ha sido lanzada por tu código. Mira la traza para "
                  + "detectar en qué punto ha sido creada y lanzada...")
            traceback.print_exc()
            stack = traceback.extract_stack()
            self.printStackTraceUpc(stack)

        self.acumula(SuperClassForTests.puntos)
        self.show_puntos(puntosAntes)

