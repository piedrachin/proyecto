import sqlite3
from sqlite3 import Error
#from BD.conexion import crear_conexion # este medoto para no tener que estar a cada rato 

def registrar_articulo_en_bd(oArticulo): #data iba antes
    conn = sqlite3.connect('projecto.db')
   # conn = crear_conexion()
    #c = conn.cursor()
   # c.execute(''' CREATE TABLE inventario IF NOT EXIST (Descripcion, Codigo, Costo, Cantidad, Fecha, Bodega) ''')
    
    sql =  ("""INSERT INTO inventario (Descripcion, Codigo, Costo, Cantidad, Fecha, Bodega) 
               VALUES(?,?,?,?,?,?)""")
   # valores = (oArticulo.descripcion,oArticulo.codigo,
    #           oArticulo.costo,oArticulo.cantidad,
     #          oArticulo.fecha, oArticulo.bodega)
    
    try:
        cur = conn.cursor()
        cur.execute(sql, oArticulo)
        conn.commit()# para que me guarde y surja efecto
        print ("Ingreso exitoso")
        return True
    except Error as e:
        print("Ocurrio un error: "+str(e))
    finally:
        if conn: #si la conexion existe
            cur.close()
            conn.close()

def registrarArticulo(oArticulo):
   # cursorDB = miConexion.cursor()
    conn = sqlite3.connect('projecto.db')
    #conn = crear_conexion()
    cursor = conn.cursor()
    sentenciaSQL = ("INSERT INTO inventario "+
                    "(`Descripcion`,"+
                    "`Codigo`,"+
                    "`Costo`,"+
                    "`Cantidad`,"+
                    "`Fecha`,"+"`Bodega`)"+
                    "VALUES (%s,%s,%s,%s,%s,%s,%s)")
    valores = (oArticulo.descripcion,oArticulo.codigo,
               oArticulo.costo,oArticulo.cantidad,
               oArticulo.fecha, oArticulo.bodega)
    
    cursor.execute(sentenciaSQL, valores)
    conn.commit()
 #   try:
  #      cur = conn.cursor()
   #     cur.execute(sentenciaSQL, valores)
    #    conn.commit()# para que me guarde y surja efecto
     #   print ("Ingreso exitoso")
      #  return True
   # except Error as e:
    #    print("Ocurrio un error: "+str(e))
    #finally:
     #   if conn: #si la conexion existe
      #      cur.close()
       #     conn.close()
    
 #   cursorDB.execute(sentenciaSQL,valores)
  #  miConexion.commit()
    
