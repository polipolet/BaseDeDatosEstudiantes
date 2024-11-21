import xml.etree.ElementTree as et
from src.casosdeuso.controlador import Controlador
from src.dominio.clave import Clave
from src.dominio.esquema import Esquema
from src.dominio.tabla import Tabla
from src.dominio.fila_datos import FilaDatos
import os
import re


class LectorDatos:

    def __init__(self):
        pass

    def lee_cnt(self,clase,metodo,test,antes):
        #Obtener el path del archivo
        ultimo = ""
        if antes:
            ultimo = "_antes.xml"
        else:
            ultimo = "_despues.xml"
        path = os.getcwd() + "/../paracorreccion/para_correctores/"+clase+"/"+metodo+"/"+test+ultimo
        return self.lee_cnt_from_path(path)

    def lee_cnt_from_path(self,path):
        controlador = Controlador.crea_controlador_vacio()
        tree = et.parse(path)
        tablas = tree.findall("Tabla")
        for el_tabla in tablas:
            self.crear_tabla(controlador,el_tabla)
        return controlador

    def crear_tabla(self, controlador, el_tabla):
        tabla = Tabla.crear_sin_argumentos()
        tabla.nombre = el_tabla.get("nombre")
        controlador.tablas[tabla.nombre]=tabla
        self.crea_esquema(el_tabla, tabla)
        self.crea_filas(el_tabla, tabla)

    def crea_filas(self,el_tabla,tabla):
        els_filas = el_tabla.findall("Fila")
        for el_fila in els_filas:
            fila = FilaDatos.crea_fila_vacia()
            tabla.filas.append(fila)
            claves_valor = el_fila.findall("./*")
            for par in claves_valor:
                fila.claves_valor[par.tag]=par.text

    def crea_esquema(self,elemento,tabla):
        esquema = Esquema.crea_esquema_vacio()
        tabla.esquema = esquema
        esq_el = elemento.find("Esquema")
        claves = esq_el.findall("clave")
        for el_clave in claves:
            clave = Clave.crea_clave_vacia()
            clave.nombre = el_clave.get("nombre")
            esquema.campos[clave.nombre] = clave
            unica = False
            val_attr_unica = el_clave.get("unica")
            if val_attr_unica=="true":
                unica = True
            clave.unica = unica


    def lee_archivo_sobre_string(path):
        file = open(path,'r')
        result = ""
        linea = file.readline().strip()
        result += linea
        while linea:
            linea = file.readline().strip()
            if linea:
                result += "\n" + linea
        file.close()
        normalized_result = re.sub("(?:(?!\n)\s)+", ' ', result)
        return normalized_result



# lector = LectorDatos()
# clase = "controlador_test"
# metodo = "crea_tabla"
# test = "test_27"
# controlador = lector.lee_cnt(clase,metodo,test,False)
# print(controlador)

