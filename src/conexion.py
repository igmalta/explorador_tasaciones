#!/usr/bin/env python
# -*- coding: utf-8 -*
# Python Version: 3.7.4

import mysql.connector
from tkinter import messagebox

class Basededatos():
    """
    La clase contiene los métodos necesarios para establecer una conexión a MySQL y si es necesario
    crear una base de datos junto con una tabla definida.
    """

    def __init__(self):
        pass
        
    def acceso_mysql(self):
        """
        Verifica si la aplicación MySQL está funcionando.
        """
        try:
            conexion = mysql.connector.connect(host = "localhost", user = "root", passwd = "")
            return conexion
        except:
            messagebox.showerror("Error", "Acceso denegado. Inicie MySQL y reinicie el programa")
            return None
    
    def crear_tabla(self):
        """
        Se realiza la conexión a la bd "tasaciones" y crea la tabla "registros".
        """
        # Conexón a la bd
        conexion = mysql.connector.connect(host = "localhost", user = "root", passwd = "", 
                                                database = "tasaciones")
        cursor = conexion.cursor()
        # Se crea la tabla "registros"
        cursor.execute(
                       """ 
                       CREATE TABLE registros(
                       id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
                       cliente VARCHAR (128) COLLATE utf8_spanish2_ci NOT NULL,
                       tipo VARCHAR (128) COLLATE utf8_spanish2_ci NOT NULL,
                       tasador VARCHAR (128) COLLATE utf8_spanish2_ci NOT NULL,
                       fecha DATE NOT NULL,
                       pais VARCHAR (128) COLLATE utf8_spanish2_ci NOT NULL,
                       provincia VARCHAR (128) COLLATE utf8_spanish2_ci NOT NULL,
                       ciudad VARCHAR (128) COLLATE utf8_spanish2_ci NOT NULL,
                       cp INT (10) NOT NULL,
                       domicilio VARCHAR (128) COLLATE utf8_spanish2_ci NOT NULL,
                       nro INT (10) NOT NULL,
                       sup_util DECIMAL(6,2) NOT NULL,
                       sup_const DECIMAL(6,2) NOT NULL,
                       antiguedad INT (3),
                       reformado VARCHAR (2) COLLATE utf8_spanish2_ci NOT NULL,
                       valuacion DECIMAL(10,2) NOT NULL,
                       imagenes TEXT COLLATE utf8_spanish2_ci
                       )
                       """
                      )
        # Se cierra la conexión              
        conexion.close() 
    
    def conectar_bd(self):
            """ 
            En primer lugar se trata de conectar a la bd "tasaciones". Si no es posible la conexión 
            se verifica que MySQL esté en funcionamiento, de ser así, significa que no existe la bd 
            y se crea junto con la tabla "registros". Por último, se intenta establecer nuevamente la 
            conexión a la bd "tasaciones".
            """
            # Se trata de conectar a la bd
            try:
                conexion = mysql.connector.connect(host = "localhost", user = "root", passwd = "", 
                                                   database = "tasaciones")           
                return conexion
            except:
                # Se verifica el acceso a MySQL
                conexion = self.acceso_mysql()
                if conexion:
                    cursor = conexion.cursor()
                    # Si hay acceso a MySQL crea la bd "tasaciones"
                    cursor.execute("CREATE DATABASE IF NOT EXISTS tasaciones")
                    conexion.close()
                    # Se crea la tabla "registros" en la bd
                    self.crear_tabla()
                    # Se vuelve a intentar la conexión con la bd
                    return self.conectar_bd()
                    
 

        
     






    






