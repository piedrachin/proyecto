# este medodo es para poderme conectar a mi base de datos
# lo vamos a importar para utilizarlo en mis otros metodos

import sqlite3
from sqlite3 import Error

def crear_conexion():
    try:
        conn = sqlite3.connect('projecto.db')
        return conn # si ocurrie algun error
    except Error as e:
        print("Error de conexion"+ str(e))
        
    