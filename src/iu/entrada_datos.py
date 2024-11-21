import os

class EntradaDatos:

    desde_teclado = True

    fichero = None

    def desde_teclado():
        EntradaDatos.desde_teclado = True
        EntradaDatos.fichero = None

    def desde_fichero(path_name):
        EntradaDatos.fichero = open(path_name,"r")
        EntradaDatos.desde_teclado = False

    def lee_linea():
        if EntradaDatos.desde_teclado:
            return input()
        if EntradaDatos.fichero!=None:
            linea = EntradaDatos.fichero.readline()
            print(linea,end="")
            return linea

    def palabras():
        return EntradaDatos.lee_linea().split()





    