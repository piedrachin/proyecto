import sqlite3
from sqlite3 import Error # para capturar cualquier error en mi sistema


# este metodo es para confirmar si ahi o no conexion a mi db

def crear_conexion():
    try:
        #aca creo una variable con la cual conectar a mi db
        conn = sqlite3.connect("name of database.db")
        return conn
    except Error as e: 
        print("Error connecting to db: "+ str(e))
        
# a continuacion se crearan nuestras consultas para la base de tados.        
        
