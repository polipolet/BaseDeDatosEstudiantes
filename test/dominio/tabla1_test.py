from src.dominio.clave import Clave
from src.dominio.esquema import Esquema
from src.dominio.excepcionesDominio import ClaveYaExisteException, ClaveInexistenteException, ValorClaveUnicaException
from src.dominio.fila_datos import FilaDatos
from src.dominio.tabla import Tabla
import traceback
from test.CorrectorGlobal import SuperClassForTests


class Tabla1Test(SuperClassForTests):


    numErrorsBefore = 0

    numInstances = 0

    nota = 0.0

    def __init__(self,*args, **kwargs):
        SuperClassForTests.__init__(self, *args, **kwargs)
        Tabla1Test.numInstances = Tabla1Test.numInstances + 1
        if Tabla1Test.numInstances == 1:
            Tabla1Test.numErrorsBefore = len(SuperClassForTests.indErrors)


    def setUpClass():
        # SuperClassForTests.nota = {}
        Tabla1Test.nota = 0.0
        print("\n\nCorrigiendo clase Tabla menos métodos:\n\t "
                + "public List<FilaDatos> busca(Criterio criterio).\n\t "
                + "public List<FilaDatos> elimina(Criterio criterio).")
        print("**********************************")

    def tearDownClass():
        SuperClassForTests.showErrors(SuperClassForTests.indErrors, "Tabla1")
        SuperClassForTests.acumulaErrores()
        SuperClassForTests.indErrors = []
        Tabla1Test.nota = SuperClassForTests.puntosTotales
        SuperClassForTests.puntosTotales = 0

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test01__init__(self):
        valorTotal = 1.0
        individualVal = valorTotal / 7
        individualPer = 1.0/7
        puntosAntes = SuperClassForTests.puntosTotales
        nombre = "claveUnica"
        unica = True
        toThrow = None
        try:
            print(f"\n\tTabla::__init__(nombre,esquema). Valor: {valorTotal}")
            esquema = Esquema()
            nombre = "nombreTabla"
            instance = Tabla(nombre,esquema)
            #Comprobando atributo 'nombre'
            self.checkAttributeAfterConstructor(instance,"nombre",nombre,valorTotal,individualPer,individualPer,1)
            #Comprobando atributo 'esquema'
            self.checkAttributeAfterConstructor(instance,"esquema",esquema,valorTotal,individualPer,individualPer,3)
            # Comprobando atributo 'filas'
            #. Comprobar que existe
            print("\tTest 5: comprobación de que el atributo 'filas' existe")
            error = self.checkFieldExists("filas",instance,individualVal,toThrow)
            self.toThrow(error,toThrow)
            if instance.filas is not None:
                print("\tTest 6: comprobación de quine el atributo 'filas' es una lista")
                error = self.checkFieldIsOfASpecificClassByName("filas",instance,"list",individualVal,toThrow)
                self.toThrow(error, toThrow)
                if error is None:
                    print("\tTest 7: comprobación de que la lista 'filas' está vacía")
                    error = self.sAssertTrue(len(instance.filas)==0,individualVal,"Error. El atributo 'filas' debe ser "
                        + f"una lista vacía, pero tiene {len(instance.filas)} elementos")
                    self.toThrow(error, toThrow)
            else:
                error = self.sAssertTrue(False,0,"Error. El atributo 'filas' tiene un valor None")
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

    def test02_anyade(self):
        valorTotal = 5.5
        puntosAntes = SuperClassForTests.puntosTotales
        num_tests = 7
        toThrow = None
        print(f"\n\tTabla::anyade(fila_datos). Valor: {valorTotal}")
        try:
            print(f"\tTest 1: Se añade una fila correcta a una tabla vacía")
            esquema = self.create_esquema()
            nombre = "nombreTabla"
            non_empty_instance = Tabla(nombre, esquema)
            fila_correcta = self.create_fila_datos_valida()
            try:
                non_empty_instance.anyade(fila_correcta)
                self.sAssertTrue(True,valorTotal/num_tests,"")
            except Exception as ex:
                error = self.sAssertTrue(False, 0.0, "Error. Se ha intentado añadir "
                        + "una fila válida con respecto al esquema, pero el método ha "
                        + f"lanzado una excepción de clase {type(ex)}")
                self.toThrow(error,toThrow)
            #
            try:
                print("\tTest 2: Se intenta añadir una fila que no tiene la "
                              + "clave única a una tabla vacía")
                esquema = self.create_esquema()
                instance = Tabla(nombre,esquema)
                fila_incorrecta = self.create_fila_datos_no_valida_por_clave()
                instance.anyade(fila_incorrecta)
                error = self.sAssertTrue(False, 0.0,"Error. Se ha podido añadir "
                        + "una fila inválida con respecto al esquema, cuando el método debería haber "
                        + "lanzado una excepción")
                self.toThrow(error, toThrow)
            except Exception as ex:
                if isinstance(ex, ClaveInexistenteException):
                    error = self.sAssertTrue(True, valorTotal / num_tests, "")
                else:
                    error = self.sAssertTrue(False, 0, "Error. Se ha intentado añadir "
                            + "una fila inválida con respecto al esquema, porque no tiene la "
                            + "clave única pero el método NO ha "
                            + "lanzado una excepción de clase ClaveInexistenteException; "
                            + f"en su lugar ha lanzado una excepción de clase {type(ex)}");
                    self.toThrow(error, toThrow)
            #
            try:
                print("\tTest 3: Se intenta añadir una fila que tiene la "
                        + "clave única pero tiene claves que no están en el esquema a una tabla vacía")
                esquema = self.create_esquema()
                instance = Tabla(nombre, esquema)
                fila_incorrecta = self.create_fila_datos_no_valida_por_tamanyo()
                instance.anyade(fila_incorrecta)
                error = self.sAssertTrue(False, 0.0, "Error. Se ha podido añadir "
                                         + "una fila inválida, porque tiene claves que no están en el esquema, "
                                         +  "cuando el método debería haber lanzado una excepción")
                self.toThrow(error, toThrow)
            except Exception as ex:
                if isinstance(ex, ClaveInexistenteException):
                    error = self.sAssertTrue(True, valorTotal / num_tests, "")
                else:
                    error = self.sAssertTrue(False, 0, "Error. Se ha intentado añadir "
                                             + "una fila inválida con respecto al esquema, porque tiene "
                                             + "claves que no están en el esquema pero el método NO ha "
                                             + "lanzado una excepción de clase ClaveInexistenteException; "
                                             + f"en su lugar ha lanzado una excepción de clase {type(ex)}");
                    self.toThrow(error, toThrow)
            #
            try:
                print("\tTest 4: Se intenta añadir una fila una fila correcta en "
                        + "una tabla no vacía")
                fil_correcta = self.create_otra_fila_datos_valida()
                non_empty_instance.anyade(fil_correcta)
                self.sAssertTrue(True,valorTotal/num_tests,"")
            except Exception as ex:
                error = self.sAssertTrue(False, 0.0, "Error. Se ha intentado añadir "
                        + "una fila válida con respecto al esquema, pero el método ha "
                        + f"lanzado una excepción de clase {type(ex)}")
                self.toThrow(error, toThrow)
            #
            try:
                print("\tTest 5: Se intenta añadir una fila incorrecta "
                        + "porque contiene una clave única con un valor que ya "
                        + "está en otra fila, en una tabla no vacía");
                #Crear una fila y añadirla a la tabla")
                fila_incorrecta = self.create_otra_fila_datos_no_valida_por_valor_clave_unica()
                non_empty_instance.anyade(fila_incorrecta)
                error = self.sAssertTrue(False, 0.0, "Error. Se ha podido añadir "
                        + "una fila inválida que contiene la clave única repetida, cuando el método debería haber "
                        + "lanzado una excepción")
                self.toThrow(error, toThrow)
            except Exception as ex:
                if isinstance(ex, ValorClaveUnicaException):
                    error = self.sAssertTrue(True, valorTotal / num_tests, "")
                else:
                    error = self.sAssertTrue(False, 0, "Error. Se ha intentado añadir "
                            + "una fila inválida con respecto al esquema, porque no tiene la "
                            + "clave única pero el método NO ha "
                            + "lanzado una excepción de clase ValorClaveUnicaException; "
                            + "en su lugar ha lanzado una excepción de clase {type(ex)}");
                    self.toThrow(error, toThrow)
            #
            try:
                print("\tTest 6: Se intenta añadir una fila incorrecta "
                        + "porque contiene una clave que no existe en el esquema, en una tabla no vacía ")
                #Crear una fila y añadirla a la tabla")
                fila_incorrecta = self.create_otra_fila_datos_no_valida_por_clave_inexistente()
                non_empty_instance.anyade(fila_incorrecta)
                error = self.sAssertTrue(False, 0.0, "Error. Se ha podido añadir "
                        + "una fila inválida que contiene una clave inexistente, cuando el método debería haber "
                        + "lanzado una excepción")
                self.toThrow(error, toThrow)
            except Exception as ex:
                if isinstance(ex, ClaveInexistenteException):
                    error = self.sAssertTrue(True, valorTotal / num_tests, "")
                else:
                    error = self.sAssertTrue(False, 0, "Error. Se ha intentado añadir "
                            + "una fila inválida con respecto al esquema, porque su clave no existe "
                            + "pero el método NO ha lanzado una excepción de clase ClaveInexistenteException; "
                            + "en su lugar ha lanzado una excepción de clase {type(ex)}");
                    self.toThrow(error, toThrow)
            #
            try:
                print("\tTest 7: Se intenta añadir una fila incorrecta "
                        + "porque no contiene el mismo número de claves que el esquema, en una tabla no vacía ")
                #Crear una fila y añadirla a la tabla")
                fila_incorrecta = self.create_fila_datos_no_valida_por_tamanyo()
                non_empty_instance.anyade(fila_incorrecta)
                error = self.sAssertTrue(False, 0.0, "Error. Se ha podido añadir "
                        + "una fila inválida con un número de claves diferente al número de claves del esquema, "
                          "cuando el método debería haber lanzado una excepción")
                self.toThrow(error, toThrow)
            except Exception as ex:
                if isinstance(ex, ClaveInexistenteException):
                    error = self.sAssertTrue(True, valorTotal / num_tests, "")
                else:
                    error = self.sAssertTrue(False, 0, "Error. Se ha intentado añadir "
                            + "una fila inválida con respecto al esquema, porque el número de claves no es igual "
                            + "al número de claves del esquema, pero el método NO ha lanzado una excepción de clase "
                            +  "ClaveInexistenteException; en su lugar ha lanzado una excepción de clase {type(ex)}");
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

    def test03_busca_todo(self):
        valorTotal = 0.5
        puntosAntes = SuperClassForTests.puntosTotales
        num_tests = 4
        toThrow = None
        print(f"\n\tTabla::busca_todo(). Valor: {valorTotal}")
        try:
            esquema = self.create_esquema()
            nombre = "nombreTabla"
            tabla = Tabla(nombre,esquema)
            fila = self.create_fila_datos_valida()
            tabla.anyade(fila)
            fila = self.create_otra_fila_datos_valida()
            tabla.anyade(fila)
            fila = self.create_tercera_fila_datos_valida()
            tabla.anyade(fila)
            if tabla.filas is not None:
                filas_expected = tabla.filas
                filas_retrieved = tabla.busca_todo()
                if filas_retrieved is not None:
                    error = self.sAssertEquals(len(filas_expected),len(filas_retrieved),valorTotal/num_tests,"Error. El número de "
                    "filas en la lista recuperada NO es el mismo que el número de filas en el atributo 'filas'")
                    self.toThrow(error, toThrow)
                    if error is None:
                        for i in range(0,len(filas_expected)):
                            if filas_expected[i]==filas_retrieved[i]:
                                self.sAssertTrue(True,valorTotal/num_tests,"");
                            else:
                                error = self.AssertTrue(False,0,f"Error. Las filas con índice {i} NO son el mismo objeto. "
                                    "Deberían serlo")
                                self.toThrow(error, toThrow)
                else:
                    error = self.AssertTrue(False, 0, f"Error. El método ha devuelto None. No debería haberlo hecho")
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

    def test04_get_esquema(self):
        valorTotal = 0.5
        puntosAntes = SuperClassForTests.puntosTotales
        num_tests = 1
        toThrow = None
        print(f"\n\tTabla::get_esquema(). Valor: {valorTotal}")
        try:
            esquema = self.create_esquema()
            nombre = "nombreTabla"
            tabla = Tabla(nombre, esquema)
            esquema_retrieved = tabla.get_esquema()
            if tabla.esquema is None:
                error = self.AssertTrue(False, 0, f"Error. El atributo 'esquema' es None. No debería serlo")
                self.toThrow(error, toThrow)
            else:
                if esquema_retrieved is not None:
                    error = self.sAssertEquals(esquema,esquema_retrieved,valorTotal,"Error. El esquema retornado NO es el "
                        "mismo objeto que el esquema que hay en el atributo 'esquema'")
                    self.toThrow(error, toThrow)
                else:
                    error = self.AssertTrue(False, 0, f"Error. El método ha devuelto None. No debería haberlo hecho")
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

    def test05_get_cabeceras(self):
        valorTotal = 2
        puntosAntes = SuperClassForTests.puntosTotales
        num_tests = 1
        toThrow = None
        print(f"\n\tTabla::get_cabeceras(). Valor: {valorTotal}")
        try:
            esquema = self.create_esquema()
            nombre = "nombreTabla"
            tabla = Tabla(nombre, esquema)
            expected = set()
            for i in range(0,5):
                expected.add("nombreClave-" + str(i+1))
            retrieved = tabla.get_cabeceras()
            retrieved_set = set()
            for i in range(0,len(retrieved)):
                retrieved_set.add(retrieved[i])
            error = self.sAssertEquals(expected,retrieved_set,valorTotal,"Error. La lista de cabeceras recuperada "
                "NO es la esperada")
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

    def test06_ordena(self):
        valorTotal = 0.5
        puntosAntes = SuperClassForTests.puntosTotales
        num_tests = 2
        toThrow = None
        print(f"\n\tTabla::ordena(). Valor: {valorTotal}")
        try:
            esquema = self.create_esquema()
            nombre = "nombreTabla"
            tabla = Tabla(nombre, esquema)
            fila_1 = self.create_fila_datos_valida()
            fila_2 = self.create_otra_fila_datos_valida()
            fila_3 = self.create_tercera_fila_datos_valida()
            tabla.anyade(fila_1)
            tabla.anyade(fila_2)
            tabla.anyade(fila_3)
            #
            print("\tTest 1: Se ordena en orden ascendente")
            tabla.ordena("nombreClave-3",True)
            if tabla.filas[0]==fila_3 and tabla.filas[1]==fila_1 and tabla.filas[2]==fila_2:
                self.sAssertTrue(True,valorTotal/num_tests,"")
            else:
                error = self.sAssertTrue(False,0,"Error. La lista de filas NO ha sido ordenada en orden ascendente "
                    "de forma correcta según la columna 'nombreClave-3'")
                self.show_puntos(puntosAntes)
            #
            print("\tTest 2: Se ordena en orden descendente")
            tabla.ordena("nombreClave-3",False)
            if tabla.filas[0]==fila_2 and tabla.filas[1]==fila_1 and tabla.filas[2]==fila_3:
                self.sAssertTrue(True,valorTotal/num_tests,"")
            else:
                error = self.sAssertTrue(False,0,"Error. La lista de filas NO ha sido ordenada en orden descendente "
                    "de forma correcta según la columna 'nombreClave-3'")
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
