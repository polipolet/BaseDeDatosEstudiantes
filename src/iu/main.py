from io import StringIO
from src.casosdeuso.controlador import Controlador
from src.casosdeuso.exportador import Exportador
from src.iu.entrada_datos import EntradaDatos
from src.iu.interfaz_usuario import InterfazUsuario
import os

##
##
## MODO 1.
##  CÓDIGO QUE LEE LOS COMANDOS DEL ARCHIVO input.txt que se encuentra en el directorio de despliegue del proyecto
##  y los ejecuta.
##
print("Gestor de base de datos 1.0")
print("===========================")
input_file = os.getcwd()+ "/../../input.txt"
exportador = Exportador()
controlador = Controlador(exportador)
iu = InterfazUsuario(controlador,exportador)
controlador.set_iu(iu)
EntradaDatos.desde_fichero(input_file)
while not iu.procesa_comando():
    pass
print("\nAdios!\n")

##
##
## MODO 2.
##  CÓDIGO QUE PIDE Y LEE COMANDOS DE LA CONSOLA. PODÉIS IR COPIANDO LOS COMANDOS QUE HAY EN EL ARCHIVO
## input.txt mencionado anteriormente. Para acabar pulsad RETURN cuando el programa os pregunte.
##
# print("Gestor de base de datos 1.0")
# print("===========================")
# exportador = Exportador()
# controlador = Controlador(exportador)
# iu = InterfazUsuario(controlador,exportador)
# controlador.set_iu(iu)
# EntradaDatos.desde_teclado()
# while not iu.procesa_comando():
#     pass
# print("\nAdios!\n")