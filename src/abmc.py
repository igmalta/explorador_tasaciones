#!/usr/bin/env python
# -*- coding: utf-8 -*
# Python Version: 3.7.4

from src.conexion import Basededatos

class Abmc(Basededatos):
    """
    La clase permite realizar operaciones básicas en la base de datos. Hereda como padre de la 
    clase Basededatos para acceder a los métodos de conexión. 
    """
  
    def __init__(self):
        """ 
        Se intenta abrir la conexión a la tabla "registros" de la bd.
        """
        self.conexion = self.conectar_bd()
    
    def consulta(self):
        """
        Si hay conexión a la tabla "registros" de la bd "tasaciones" devuelve los valores de la 
        tabla.
        """
        if self.conexion:
            # Trata de recuperar los valores de la tabla
            try:
                cursor = self.conexion.cursor()
                # Se consulta la bd
                sql = 'SELECT * FROM registros'
                cursor.execute(sql)
                db_rows = cursor.fetchall()
                return db_rows
            except:
                messagebox.showwarning("Alerta", "No se puede realizar la consulta") 
            # Se cierra la conexión    
            finally:
                if self.conexion:
                    self.conexion.close()
        else:
            return None
           
    def alta(self, args):
        """
        Inserta un nuevo registro en la tabla "registros" de la bd "tasaciones". 
        """
        # Se intenta insertar un registro en la bd
        try:
            cursor = self.conexion.cursor()
            # Se inserta nuevo registro en la bd
            sql = """
                INSERT INTO registros(cliente, tipo, tasador, fecha, pais, provincia, ciudad, cp, 
                domicilio, nro, sup_util, sup_const, antiguedad, reformado, valuacion, imagenes) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """    
            cursor.execute(sql, args)
            self.conexion.commit()
            print("Nuevo registro agregado correctamente")
        except:
            messagebox.showwarning("Alerta", "No se puede realizar la operación") 
        # Se cierra la conexión    
        finally:
            if self.conexion:
                self.conexion.close()

    def update(self, args):
        """
        Actualiza el registro designado en la tabla "registros" de la bd "tasaciones".
        """
        # Se intenta actualizar un registro
        try:
            cursor = self.conexion.cursor()
            # Se actualiza el registro designado en la bd
            sql = """
                UPDATE registros SET cliente=%s , tipo=%s, tasador=%s, fecha=%s, pais=%s,
                provincia=%s, ciudad=%s, cp=%s, domicilio=%s, nro=%s, sup_util=%s, sup_const=%s, 
                antiguedad=%s, reformado=%s, valuacion=%s, imagenes=%s WHERE registros.id=%s
                """   
            cursor.execute(sql, args)
            self.conexion.commit()
            print("Registro actualizado correctamente")
        except:
            messagebox.showwarning("Alerta", "No se pueden actualizar los datos") 
        # Se cierra la conexión    
        finally:
            if self.conexion:
                self.conexion.close()
    
    def eliminar(self, id):
        """
        Se elimina el registro con el id indicado de la bd.
        """
        # Se intenta eliminar un registro
        try:
            cursor = self.conexion.cursor()
            # Se elimina el registro de la bd
            sql = "DELETE FROM registros WHERE registros.id=%s"
            cursor.execute(sql, (id,) )
            self.conexion.commit()
            print("Registro eliminado correctamente")
        except:
            messagebox.showwarning("Alerta", "No se pueden eliminar los datos") 
        # Se cierra la conexión    
        finally:
            if self.conexion:
                self.conexion.close()
    
    def eliminar_todo(self):
        """
        Se eliminan todos las filas en la tabla "registros" de la bd.
        """
        # Se intenta eliminar un registro
        try:
            cursor = self.conexion.cursor()
            # Se elimina el registro de la bd
            sql_del = "DELETE FROM registros"
            # Se reinicia el id autoincremental en 1
            sql_inc = "ALTER TABLE registros AUTO_INCREMENT = 1"
            cursor.execute(sql_del)
            self.conexion.commit()
            cursor.execute(sql_inc)
            self.conexion.commit()
            print("Todos los registros fueron eliminados correctamente")
        except:
            messagebox.showwarning("Alerta", "No se pueden eliminar los datos") 
        # Se cierra la conexión    
        finally:
            if self.conexion:
                self.conexion.close()