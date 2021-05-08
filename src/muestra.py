#!/usr/bin/env python
# -*- coding: utf-8 -*
# Python Version: 3.7.4

"""
IMPORTANTE:
la siguiente función se coloca solo a los fines de crear una muestra rápida de registros para probar 
el programa, y no se considera parte de su estructura.
"""
from PIL import ImageTk
from PIL import Image as PILImage
from random import randint
from tkinter import messagebox
import os

from src.gestionar import*

# Nombre de imágenes en directorio
name_img_01 = ['viv_CZ_01.jpg', 'viv_CZ_02.jpg']
name_img_02 = ['viv_JF_01.jpg', 'viv_JF_02.jpg', 'viv_JF_03.jpg']
name_img_03 = ['viv_MP_01.jpg', 'viv_MP_02.jpg']
name_img_04 = ['viv_SB_01.jpg', 'viv_SB_02.jpg', 'viv_SB_03.jpg', 'viv_SB_04.jpg']

# Ruta de imágenes en directorio
ruta_img_01 = ["img/imagenes_muestras/" + i for i in name_img_01]
ruta_img_02 = ["img/imagenes_muestras/" + i for i in name_img_02]
ruta_img_03 = ["img/imagenes_muestras/" + i for i in name_img_03]
ruta_img_04 = ["img/imagenes_muestras/" + i for i in name_img_04]

def crear_muestra(tabla):
    """ 
    Se definen cuatro listas con datos correspondientes a tasaciones que se inyectan a la tabla
    "registros" de la bd "tasaciones" si se ejecuta el botón "Muestra". Para evitar errores, los
    nombres de las imágenes deben cambiar si se realizan varias muestras, obviamente los datos de las
    tasaciones no cambian.
    """
    # Se crea un nombre aleatorio
    rand_img_01 = ["viv_CZ_" + str(randint(0,1000)) + ".jpg", "viv_CZ_" + str(randint(0,1000)) + ".jpg"]
    rand_img_02 = ["viv_JF_" + str(randint(0,1000)) + ".jpg", "viv_JF_" + str(randint(0,1000)) + ".jpg", 
                   "viv_JF_" + str(randint(0,1000)) + ".jpg"]
    rand_img_03 = ["viv_MP_" + str(randint(0,1000)) + ".jpg", "viv_MP_" + str(randint(0,1000)) + ".jpg"]
    rand_img_04 = ["viv_SB_" + str(randint(0,1000)) + ".jpg", "viv_SB_" + str(randint(0,1000)) + ".jpg", 
                   "viv_SB_" + str(randint(0,1000)) + ".jpg", "viv_SB_" + str(randint(0,1000)) + ".jpg"]

    # Datos de Tasaciones
    tasacion_01 = ["Juan Peréz", "casa", "Federico González", "2019-12-09", "Argentina", 
                    "Catamarca", "Achalco", 4235, "Av. Roca", 437, 300, 109, 1, "No", 3567898, 
                    str(rand_img_01)]

    tasacion_02 = ["Carlos García", "casa", "Eduardo Gómez", "2019-05-06", "Argentina", 
                    "Jujuy", "Zapla", 4612, "Belgrano", 128, 423.50, 156.78, 14, "Si", 4234123, 
                    str(rand_img_02)]

    tasacion_03 = ["Mercedes Funes", "PH", "Héctor Díaz", "2018-10-10", "Argentina", 
                    "Chaco", "Mieres", 3524, "San Martín", 1156, 545, 189, 3, "No", 3000000, 
                    str(rand_img_03)]

    tasacion_04 = ["Ramón Rodriguez", "casa", "Fernando Ruíz", "2017-02-11", "Argentina", 
                    "Santa Fe", "Las Rosas", 4405, "Chacabuco", 250, 350, 134, 20, "Si", 2500000, 
                str(rand_img_04)]

    # Se juntan los datos en una lista
    valores = [tasacion_01, tasacion_02, tasacion_03, tasacion_04]
    names_img = [rand_img_01, rand_img_02, rand_img_03, rand_img_04]
    rutas_img = [ruta_img_01, ruta_img_02, ruta_img_03, ruta_img_04]

    consulta =  messagebox.askokcancel('Muestra', "¿Desea crear una muestra de tasaciones?")
    if consulta:
        for n in range(len(valores)):          
            # Se guardan los datos en la base de datos
            alta_tabla(tabla, valores[n])
            # Si no existe, se crea el directorio "imagenes" para guardar las imágenes subidas
            directorioParaImgs = os.path.join("img/imagenes")
            if not os.path.exists(directorioParaImgs):
                os.mkdir(directorioParaImgs)
            # Se guardan las imágenes cargadas (si hubieran) en el directorio
            for i in range(len(rutas_img[n])):
                name_file = names_img[n][i]
                with PILImage.open(rutas_img[n][i]) as abrir_img:
                    guardar_img = os.path.join(directorioParaImgs, name_file)
                    abrir_img.save(guardar_img)
        print("Muestra creada correctamente")
          

                