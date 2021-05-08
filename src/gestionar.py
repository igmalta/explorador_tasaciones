#!/usr/bin/env python
# -*- coding: utf-8 -*
# Python Version: 3.7.4

"""
Este módulo contiene funciones que permiten a los módulos "main.py" y "formulario.py" conectar a la
bd o a un archivo externo. Algunas funciones son comunes para ambos módulos.
"""
import json
from tkinter import*
from tkinter.ttk import*

from src.abmc import Abmc

# ==================================================================================================  
# FUNCIONES QUE CONECTAN A UN ARCHIVO EXTERNO
# ==================================================================================================  
# Archivo .json con las provincias, localidades y cp de Argentina
localidades = json.load(open('data/localidades.json', encoding='utf-8'))

def get_localidad(ciudad, provincia):
    """
    Se filtran las localidades de acuerdo a la provincia seleccionada. 
    """
    ciudad["values"] = sorted(list(set([x["loc_nombre"] for x in localidades 
                       if x["prv_nombre"] == provincia.get()])))
   
def set_cp(ciudad, entrada_cp):
    """
    Se inserta en la entrada "CP" el código postal de la ciudad elegida.
    Si hay varias opciones cp para una ciudad, se elige la primera opción.
    """
    cp = [x["loc_cpostal"] for x in localidades if x["loc_nombre"] == ciudad.get()]
    entrada_cp.delete(0, END)
    entrada_cp.insert(0, cp[0])

# ==================================================================================================  
# FUNCIONES QUE CONECTAN A LA BASE DE DATOS
# ================================================================================================== 
# Visualizar cambios en tabla
def vista_tasacion(tabla):
    """ 
    Muestra los registros de la bd en la tabla de la ventana principal. Es decir, se conecta a la 
    bd, se recuperan los valores de la tabla "registros" y se insertan en la tabla de la ventana 
    de inicio del programa.
    """
    # Se trata de conectar y consultar los registros de la tabla en la bd
    db_consulta = Abmc().consulta()
    # Si hay conexión se ejecuta el código
    if  isinstance(db_consulta, list):
        # Se eliminan (limpian) las filas existentes en la tabla del programa
        records = tabla.get_children()
        for element in records:
            tabla.delete(element)
        # Se llena la tabla con las filas actualizadas
        for row in db_consulta:
            tabla.insert('', "end", text = row, values = row)
        return True
    else:
        # Cuando falla la conexión a la tabla de la bd
        return None
       
def alta_tabla(tabla, args):
    """
    Crea un nuevo registro con los datos cargados en el formulario.
    """
    # Crea el registro en la bd
    Abmc().alta(args)
    # Actualiza los datos de la tabla en la ventana principal del programa
    vista_tasacion(tabla)

def update_tabla(tabla, args):
    """
    Actualiza un registro con las modificaciones realizadas en el formulario.
    """
    # Actualiza el registro modificado en la bd
    Abmc().update(args)
    # Actualiza los datos de la tabla en la ventana principal del programa
    vista_tasacion(tabla)

def eliminar_registro(tabla, id):
    """
    Elimina un registro seleccionado en la tabla de la ventana principal del programa.
    """
    # Elimina el registro de la bd con el id correspondiente
    Abmc().eliminar(id)
    # Actualiza los datos de la tabla en la ventana principal del programa
    vista_tasacion(tabla)

def eliminar_todo(tabla):
    """
    Elimina todos los registros existentes en la tabla de la ventana principal del programa.
    """
    # Elimina el registro de la bd con el id correspondiente
    Abmc().eliminar_todo()
    # Actualiza los datos de la tabla en la ventana principal del programa
    vista_tasacion(tabla)



        
        
        
        


