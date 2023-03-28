import sqlite3
from sqlite3 import Error #
from .conexion import crear_conexion # me importa el metodo creado en mi db

def registro_articulo(data):
    conn = crear_conexion()
    sql = """ INSERT INTO name_of_db (name_of_colums in db) VALUES (?)"""
              #must use this ? for each column in the db

    try: 
        cursor = conn.cursor()
        cursor.execute(sql,data)
        conn.commit()
        print("Se registro un articulo nuevo")
        return True
    except Error as e:
        print("Error inserting a new articule: "+str(e))
    
    finally:
        if conn:
            cursor.close()
            conn.close()