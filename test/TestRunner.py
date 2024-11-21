import importlib
from test.CorrectorGlobal import SuperClassForTests


class TestRunner:
    notas = {}  # es un mapa <string (clase), float (puntos obtenidos)>

    def __init__(self):
        self.toBeRun = [
            "test.dominio.clave_test.ClaveTest" \
            , "test.dominio.esquema_test.EsquemaTest" \
            , "test.dominio.fila_datos_test.FilaDatosTest" \
            , "test.dominio.tabla1_test.Tabla1Test"\
            , "test.dominio.criterios.criterio_igual_test.CriterioIgualTest" \
            , "test.dominio.criterios.criterio_contiene_test.CriterioContieneTest" \
            , "test.dominio.criterios.criterio_mayor_que_test.CriterioMayorQueTest" \
            , "test.dominio.criterios.criterio_menor_que_test.CriterioMenorQueTest" \
            , "test.dominio.tabla2_test.Tabla2Test"\
            , "test.casosdeuso.exportador_test.ExportadorTest"\
            , "test.casosdeuso.controlador_test.ControladorTest"\
            ]
        self.porcentajes = [6,8,8,8,7,7,7,7,8,8,26]
        self.clasesAPorcentajes = {}  # mapa <string (clase),float (porcentaje)>
        self.clases = []  # secuencia de clases test
        i = 0

        for pkgClassName in self.toBeRun:
            c = self.get_class(pkgClassName)
            TestRunner.notas[c.__name__] = 0.0
            self.clasesAPorcentajes[c.__name__] = self.porcentajes[i]
            TestRunner.notas[c.__name__] = 0.0
            i = i + 1

    def show_grades(self):
        print("\n\n")
        SuperClassForTests.showAlldErrors()
        print("\n\n")
        notaFinal = 0.0
        for clase, nota in TestRunner.notas.items():
            notaParcial = nota * self.clasesAPorcentajes[clase] / 100.0
            notaFinal = notaFinal + notaParcial
            print(
                f"\n\nNota en clase {clase}: {format(nota, '.2f')} (Porcentaje en nota final: {self.clasesAPorcentajes[clase]}%). Contribucion a nota final: {format(notaParcial, '.3f')}")
        print(f"\nNOTA FINAL DE CORRECCIÓN AUTOMÁTICA: {format(notaFinal, '.3f')}");
        print("----------------- ------------------ ");

    def get_class(self, kls):
        parts = kls.split('.')
        module = ".".join(parts[:-1])
        m = importlib.import_module(module)
        return getattr(m, parts[len(parts) - 1])

    def runTestSuite(self):
        for testerClass in self.toBeRun:
            c = self.get_class(testerClass)
            b = c()
            methods = dir(c)
            # print(str(methods))
            # print(str(methods))
            obMethod = getattr(c, "setUpClass")
            obMethod()
            for method in methods:
                if method.startswith("test"):
                    obMethod = getattr(b, "setUp")
                    obMethod()
                    obMethod = getattr(b, method)
                    obMethod()
                    obMethod = getattr(b, "tearDown")
                    obMethod()
            obMethod = getattr(c, "tearDownClass")
            obMethod()
            TestRunner.notas[c.__name__] = getattr(c, "nota")


runner = TestRunner()
runner.runTestSuite()
runner.show_grades()
