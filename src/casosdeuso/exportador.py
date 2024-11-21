from src.casosdeuso.controlador import Controlador

class Exportador:

    ##@brief
    #Constructor; NO hace nada (instrucción pass)
    #
    def __init__(self):
        pass

    ##@brief
    # Guarda en un archivo de disco (cuyo nombre se pasa como parámetro)
    # la secuencia de comandos (uno por línea) que generaría las tablas que hay en memoria,con su contenido actual.
    # Por ejemplo, si tuviéramos las siguientes tablas en memoria:
    #
    # TABLA coches:
    # marca          |matricula      |modelo
    # -------------- | -------------| ------------
    # Ferrari        |1566GGH       |Testarrossa
    # Ford           |4566GGH       |Escort
    # Seat           |4456GVG       |Córdoba
    #
    # TABLA multas (donde matricula es clave única):
    # cuantia         |matricula
    # -------------- | -------------
    # 101             |2345FXZ
    # 100             |B1234XD
    # 60              |B1234XD
    #
     # <p>Y se invocara el método exporta("tablas.txt"), se generaría un archivo de texto
    # llamado 'tablas.txt' cuyo contenido sería el siguiente:</p>
    #
    # multas crea cuantia matricula\n
    # multas anyade cuantia=101 matricula=2345FXZ\n
    # multas anyade cuantia=100 matricula=B1234XD\n
    # multas anyade cuantia=60 matricula=B1234XD\n
    # coches crea marca #matricula modelo\n
    # coches anyade marca=Ferrari matricula=1566GGH modelo=Testarrossa\n
    # coches anyade marca=Ford matricula=4566GGH modelo=Escort\n
    # coches anyade marca=Seat matricula=4456GVG modelo=Córdoba\n
    #
    #
    # @param tablas el mapa con las tablas del controlador
    # @param pathName Nombre del archivo en el que se guardará el archivo de exportación
    #
    def exporta(self,tablas,pathName):
        from src.dominio.excepcionesDominio import MetodoNoImplementadoException
        raise MetodoNoImplementadoException("Exportador::exporta(...) NO SE HA IMPLEMENTADO")
