from src.dominio.clave import Clave
from src.dominio.esquema import Esquema
from src.dominio.excepcionesDominio import ClaveYaExisteException, ClaveInexistenteException
from src.dominio.fila_datos import FilaDatos
import traceback
from test.CorrectorGlobal import SuperClassForTests

class FilaDatosTest(SuperClassForTests):


    numErrorsBefore = 0

    numInstances = 0

    nota = 0.0

    def __init__(self,*args, **kwargs):
        SuperClassForTests.__init__(self, *args, **kwargs)
        FilaDatosTest.numInstances = FilaDatosTest.numInstances + 1
        if FilaDatosTest.numInstances == 1:
            FilaDatosTest.numErrorsBefore = len(SuperClassForTests.indErrors)


    def setUpClass():
        # SuperClassForTests.nota = {}
        FilaDatosTest.nota = 0.0
        print("\n\nCORRIGIENDO clase FilaDatos")
        print("**************************")

    def tearDownClass():
        SuperClassForTests.showErrors(SuperClassForTests.indErrors, "Esquema")
        SuperClassForTests.acumulaErrores()
        SuperClassForTests.indErrors = []
        FilaDatosTest.nota = SuperClassForTests.puntosTotales
        SuperClassForTests.puntosTotales = 0

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test01__init__(self):
        valorTotal = 2.0
        puntosAntes = SuperClassForTests.puntosTotales
        nombre = "claveUnica"
        unica = True
        toThrow = None
        try:
            print(f"\n\tFilaDatos::__init__(). Valor: {valorTotal}")
            instance = FilaDatos()
            error = self.checkFieldExists("claves_valor", instance, valorTotal / 2, toThrow)
            toThrow = self.toThrow(error, toThrow)
            if instance.claves_valor is not None:
                error = self.checkFieldIsOfASpecificClassByName("claves_valor",instance,"dict",valorTotal/2,toThrow)
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

    def test02_put(self):
        valorTotal = 1.0
        puntosAntes = SuperClassForTests.puntosTotales
        toThrow = None
        try:
            print(f"\n\tFilaDatos::put(...). Valor: {valorTotal}")
            nombre = "nombreClave"
            valor = "valor"
            instance = FilaDatos()
            instance.put(nombre,valor)
            print("\t\tTest 1: comprobar que se ha añadido una entrada con la clave correcta")
            error = self.sAssertTrue(instance.claves_valor.get("nombreClave") is not None,valorTotal / 2, "Error: debería "
                        + "haberse añadido un par <clave valor>, pero no se ha "
                        + "encontrado ningún par con la clave correcta")
            toThrow = self.toThrow(error, toThrow)
            if error is None:
                print("\t\tTest 2: comprobar que se ha añadido una entrada con el valor correcto mapeado con la clave correcta")
                valor_retornado = instance.claves_valor.get("nombreClave")
                error = self.sAssertTrue(valor_retornado=="valor", valorTotal / 2,
                                         "Error: debería "
                                         + "haberse añadido un par <clave valor>, pero el par "
                                         + "añadido no es el que se pretendía añadir: el valor mapeado con la "
                                         + f"clave ('valor') no es el recuperado ({valor_retornado})")
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

    def test03_get(self):
        valorTotal = 1.0
        puntosAntes = SuperClassForTests.puntosTotales
        nombre = "claveUnica"
        unica = True
        toThrow = None
        try:
            print(f"\n\tFilaDatos::get(). Valor: {valorTotal}")
            nombre = "nombreClave"
            valor = "valor"
            instance = FilaDatos()
            instance.put(nombre,valor)
            print("\tTest 1: se invoca a get con el nombre de una clave que ESTÁ en "
                          + "el objeto FilaDatos")
            returned = instance.get(nombre)
            error = self.sAssertEquals(valor,returned,valorTotal/2,f"Error: se ha mapeado la clave '{nombre}' al "
                    + f"valor '{valor}', pero el método get() ha devuelto como valor '{returned}'")
            toThrow = self.toThrow(error, toThrow)
            #
            print("\tTest 2: se invoca a get con el nombre de una clave que NO está en "
                          + "el objeto FilaDatos")
            returned = instance.get("otroNombre")
            error = self.sAssertEquals(None,returned,valorTotal/2,f"Error: se ha mapeado la clave '{nombre}' al "
                    + f"valor '{valor}', pero el método get('otroNombre') ha devuelto como valor '{returned}' en lugar "
                      f"de None")
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

    def test04_valida(self):
        valorTotal = 6.0
        numTests = 6
        puntosAntes = SuperClassForTests.puntosTotales
        nombre = "claveUnica"
        unica = True
        toThrow = None
        try:
            print(f"\n\tFilaDatos::valida(). Valor: {valorTotal}")
            #
            print("\tTest 1: Esquema y FilaDatos vacíos")
            esquema = Esquema()
            instance = FilaDatos()
            try:
                instance.valida(esquema)
                self.sAssertTrue(True,valorTotal/numTests,"")
            except Exception as ex:
                error = self.sAssertTrue(False, valorTotal / numTests, "Error: "
                        + "la fila está vacía y el esquema también. No debería "
                        + "haberse lanzado ninguna excepción, y sin embargo, se "
                        + "ha lanzado");
                self.toThrow(error, toThrow)
            #
            print("\tTest 2: Esquema vacío y fila NO vacía")
            instance.put("clave1","valor1")
            try:
                instance.valida(esquema)
                error = self.sAssertTrue(False, 0, "Error: "
                        + "la fila está vacía y el esquema también. Debería "
                        + "haberse lanzado una excepción, y sin embargo, NO se "
                        + "ha lanzado");
            except Exception as ex:
                if isinstance(ex,ClaveInexistenteException):
                    error = self.sAssertTrue(True,valorTotal/numTests,"")
                else:
                    error = self.sAssertTrue(False, 0, "Error: "
                                             + "la fila está vacía y el esquema también. Debería "
                                             + "haberse lanzado una excepción ClaveInexistenteException, y sin embargo, "
                                             + f"ha lanzado una excepción {type(ex)}");
                    self.toThrow(error, toThrow)
            #
            print("\tTest 3: Esquema NO vacío y fila vacía")
            instance = FilaDatos()
            clave1 = Clave.create_with_name_only("nClave1")
            esquema.add_clave(clave1)
            try:
                instance.valida(esquema)
                error = self.sAssertTrue(False,0,"Error: "
                        + "la fila  está vacía pero el esquema NO lo está. Debería "
                        + "haberse lanzado una excepción ClaveInexistenteException, y sin embargo, NO se "
                        + "ha lanzado")
                self.toThrow(error, toThrow)
            except Exception as ex:
                if isinstance(ex,ClaveInexistenteException):
                    error = self.sAssertTrue(True, valorTotal / numTests, "")
                else:
                    error = self.sAssertTrue(False, 0, "Error: "
                                             + "la fila está vacía pero el esquema NO lo está. Debería "
                                             + "haberse lanzado una excepción ClaveInexistenteException, y sin embargo, "
                                             + f"ha lanzado una excepción {type(ex)}");
                    self.toThrow(error, toThrow)
            #
            print("\tTest 4: Esquema NO vacío y fila NO vacía Y diferentes tamaños")
            esquema = self.create_esquema()
            if esquema is not None:
                instance = self.create_fila_datos_no_valida_por_tamanyo()
                try:
                    instance.valida(esquema)
                    error = self.sAssertTrue(False, 0, "Error: "
                                 + "la fila generada NO es válida respecto al esquema por razón de su tamaño. Debería "
                                 + "haberse lanzado una excepción ClaveInexistenteException, y sin embargo, NO ha "
                                 + "lanzado ninguna excepción");
                    self.toThrow(error, toThrow)
                except Exception as ex:
                    if isinstance(ex, ClaveInexistenteException):
                        error = self.sAssertTrue(True, valorTotal / numTests, "")
                    else:
                        error = self.sAssertTrue(False, 0, "Error: "
                                                 + "la fila NO es válida respecto al esquema por razón de su tamaño. Debería "
                                                 + "haberse lanzado una excepción ClaveInexistenteException, y sin embargo, "
                                                 + f"ha lanzado una excepción {type(ex)}");
                        self.toThrow(error, toThrow)
            #
            print("\tTest 5: Esquema NO vacío y fila NO vacía E IGUALES tamaños pero errónea por clave")
            esquema = self.create_esquema()
            if esquema is not None:
                instance = self.create_fila_datos_no_valida_por_clave()
                try:
                    instance.valida(esquema)
                    error = self.sAssertTrue(False, 0, "Error: "
                                 + "la fila generada NO es válida respecto al esquema por razón de una clave. Debería "
                                 + "haberse lanzado una excepción ClaveInexistenteException, y sin embargo, NO ha "
                                 + "lanzado ninguna excepción");
                    self.toThrow(error, toThrow)
                except Exception as ex:
                    if isinstance(ex, ClaveInexistenteException):
                        error = self.sAssertTrue(True, valorTotal / numTests, "")
                    else:
                        error = self.sAssertTrue(False, 0, "Error: "
                                                 + "la fila NO es válida respecto al esquema por razón de una clave. Debería "
                                                 + "haberse lanzado una excepción ClaveInexistenteException, y sin embargo, "
                                                 + f"ha lanzado una excepción {type(ex)}");
                        self.toThrow(error, toThrow)
            #
            print("\tTest 6: Esquema NO vacío y fila NO vacía Y VÁLIDA")
            esquema = self.create_esquema()
            if esquema is not None:
                instance = self.create_fila_datos_valida()
                try:
                    instance.valida(esquema)
                    error = self.sAssertTrue(True, valorTotal / numTests, "")
                except Exception as ex:
                    error = self.sAssertTrue(False, 0, "Error: "
                                    + "la fila ES válida respecto al esquema. No debería "
                                    + "haberse lanzado ninguna excepción, y sin embargo, "
                                    + f"ha lanzado una excepción {type(ex)}");
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

    def create_esquema(self):
        esquema = Esquema()
        clave = None
        try:
            for i in range(0,5):
                if i!=3:
                    clave = Clave("nombreClave-"+str(i+1),False)
                else:
                    clave = Clave("nombreClave-"+str(i+1),True)
                esquema.add_clave(clave)
        except ClaveYaExisteException as ex:
            print("\n\tError al crear el esquema. No debería darse si el corrector "
                          + "ha otorgado las máximas puntuaciones en las clases Clave, Esquema y "
                          + "se han creado correctamente las clases BaseDatosException, "
                          + "ClaveYaExisteException, ClaveInexistenteException. Si todas estas "
                          + "condiciones se dan, consulta con el profesorado")
            return None
        return esquema

    def create_fila_datos_valida(self):
        fila = FilaDatos()
        for i in range(0,5):
            fila.put("nombreClave-"+str(i+1),"valor-"+str(i+1))
        return fila

    def create_fila_datos_no_valida_por_tamanyo(self):
        fila = FilaDatos()
        for i in range(0,4):
            fila.put("nombreClave-"+str(i+1),"valor-"+str(i+1))
        return fila

    def create_fila_datos_no_valida_por_clave(self):
        fila = FilaDatos()
        for i in range(0,5):
            if i<4:
                fila.put("nombreClave-"+str(i+1),"valor-"+str(i+1))
            else:
                fila.put("malNombreClave", "valor-" + str(i + 1))
        return fila
