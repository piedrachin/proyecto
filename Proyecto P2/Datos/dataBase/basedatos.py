import pyodbc

con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\pablo\OneDrive\Escritorio\Proyecto_Final_Progra2\proyecto\Proyecto P2\Datos\dataBase\MiBaseDatos1.accdb;'
#msa_drivers = [x for x in pyodbc.drivers() if 'ACCESS' in x.upper() ]
#print(f'MS_Access Drivers : {msa_drivers}')
def ingresar_articulos(oArticulo):

    try:
      #  con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\pablo\OneDrive\Escritorio\Proyecto_Final_Progra2\Proyecto P2\Datos\dataBase\MiBaseDatos1.accdb;'
        conn = pyodbc.connect(con_string)
        print("Connected to db")
        

        sql =  ("""INSERT INTO inventario (descripcion, codigo, costo, cantidad, fecha,bodega)
  
                VALUES (?,?,?,?,?,?)""")
        
        valores = (oArticulo.descripcion,oArticulo.codigo,
               oArticulo.costo,oArticulo.cantidad,
               oArticulo.fecha, oArticulo.bodega)#, oArticulo.bodega
    
        cursor = conn.cursor()

        cursor.execute(sql, valores)
        conn.commit()
        print("Data inserted en tabla inventario")

    except pyodbc.Error as e:
        print("Error Conexion" + str(e))
        
def actualizar_articulos(oArticulo):#oArticulo
    conn = pyodbc.connect(con_string)# con esto creo mi conexion automaticamente
    print("Se conecto a BD") 
    try:
        sql = ("UPDATE MibaseDatos.inventario "+ 
                    "SET descripcion = ?,"+
                        "codigo = ?,"+
                       "costo = ?,"+
                       "cantidad = ?,"+
                        "fecha = ?,"+
                       " bodega = ?"+
            "WHERE consecutivo =?")
    
        valores = (oArticulo.descripcion,oArticulo.codigo,
                oArticulo.costo,oArticulo.cantidad,
                oArticulo.bodega, oArticulo.fecha, oArticulo.consecutivo)
    
        cur = conn.cursor()
        cur.execute(sql,valores)
        conn.commit()
        print("Actualizacion correcta de articulo")
        return True
    except pyodbc.Error as e:
        print("Error actualizando registro: "+ str(e))
    finally:
        if conn:
           cur.close()
           conn.close()
            
            
def seleccionar_articulos():
    conn = pyodbc.connect(con_string)# para conectarme a mi base 
    sql = """SELECT * FROM inventario """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        registro_articulos = cur.fetchall() # con esto me traigo todo lo que esta registrado
        return registro_articulos
    except pyodbc.Error as e:
        print(" Error al selecionar articulos "+ str(e))
    finally:
        if conn:
            cur.close()
            conn.close()
            
            
def eliminarArticulo(id):
    conn = pyodbc.connect(con_string)# para conectarme a mi base 
    print("Se conecto a BD")
    
    sql = (f"Delete from inventario where consecutivo = {id}")  
    try:              
        
        
        cur = conn.cursor() 
        cur.execute(sql)
        conn.commit()
        print("Articulo eliminado")
        return True
    except pyodbc.Error as e:
        print("Error al eliminar: "+ str(e))
    
    finally:
        if conn:
            cur.close()
            conn.close()
    
    
def crear_bodega(oBodega):
    try:
        conn = pyodbc.connect(con_string)
        sql = ("""INSERT INTO bodega (nombre) 
               VALUES(?)""")
        valores = (oBodega.nombre)
        cursor = conn.cursor()
        cursor.execute(sql, valores)
        conn.commit()
        print("Data inserted en tabla bodega (inventario)")

    except pyodbc.Error as e:
        print("Error Conexion" + str(e))

def obtener_lista_bodegas():
    conn = pyodbc.connect(con_string)# para conectarme a mi base 
    print("Conexion A BD")
    sql = (""" SELECT bodega FROM inventario """)
    try:
        cur = conn.cursor()
        cur.execute(sql)
       # data = cur.fetchall()
       # for category in data:
          #  data.append(category[0])
         #   print(category[0])
        lista_bodegas = cur.fetchall() # con esto me traigo todo lo que esta registrado
        return lista_bodegas
        #return data
    except pyodbc.Error as e:
        print(" Error al llamar bodega "+ str(e))
        
def eliminar_bodega(id):
    conn = pyodbc.connect(con_string)# para conectarme a mi base 
    print("Se conecto a BD ")
    sql = (f"Delete from inventario where id_bod = {id}")
  #  sql = (f"Delete from bodega Where id_bod = {id}")  
    try:              
        cur = conn.cursor() 
        cur.execute(sql)
        conn.commit()
        print("Bodega eliminada")
        return True
    except pyodbc.Error as e:
        print("Error al eliminar: "+ str(e))
    
    finally:
        if conn:
            cur.close()
            conn.close()
    
    
        
def registrar_distribuidor(oDistribuidor):
    
    try:
        conn = pyodbc.connect(con_string)# para conectarme a mi base 
        print("Conectado a BD")
        sql = ("""INSERT INTO distribuidor (Distribuidor, Telefono, Cedula, Fecha)
                 VALUES (?,?,?,?)""")
        valores = (oDistribuidor.distribuidor, oDistribuidor.telefono, oDistribuidor.cedula,
                   oDistribuidor.fecha)
        cursor = conn.cursor()
        cursor.execute(sql, valores)
        conn.commit()
        print("Se inserto dato en tabla Distribuidor")
        
    except pyodbc.Error as e:
        print("Error de Conexion "+ str(e) )

def obtener_lista_distribuidor():
    conn = pyodbc.connect(con_string)# para conectarme a mi base 
    print("Conexion A BD")
    sql = (""" SELECT Distribuidor,Telefono,Cedula, Fecha FROM distribuidor """)
    
    try:
        cur = conn.cursor()
        cur.execute(sql)

        lista_dist = cur.fetchall() # con esto me traigo todo lo que esta registrado
        return lista_dist
    except pyodbc.Error as e:
        print("Error de Conexion "+ str(e) ) 
        
def obtener_nombre_dist():
    conn = pyodbc.connect(con_string)# para conectarme a mi base 
    print("Conexion A BD")
    sql = (""" SELECT Distribuidor FROM distribuidor """)
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        lista_dist = cur.fetchall() # con esto me traigo todo lo que esta registrado
        print("Se obtuvo el nombre.")
        return lista_dist
    except pyodbc.Error as e:
        print("Error de Conexion "+ str(e) ) 
        
def eliminar_de_lista_distribuidor(id):
    conn = pyodbc.connect(con_string)# para conectarme a mi base 
    print("Se conecto a BD ")
    sql = (f"Delete from distribuidor where id_dist = {id}")
    try:              
        cur = conn.cursor() 
        cur.execute(sql)
        conn.commit()
        print("Distribuidor eliminado")
        return True
    except pyodbc.Error as e:
        print("Error al eliminar: "+ str(e))
    
    finally:
        if conn:
            cur.close()
            conn.close()
      
