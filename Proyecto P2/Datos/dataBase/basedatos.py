import pyodbc

con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\pablo\OneDrive\Escritorio\Proyecto_Final_Progra2\proyecto\Proyecto P2\Datos\dataBase\MiBaseDatos1.accdb;'
#msa_drivers = [x for x in pyodbc.drivers() if 'ACCESS' in x.upper() ]
#print(f'MS_Access Drivers : {msa_drivers}')
def ingresar_articulos(oArticulo):

    try:
      #  con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\pablo\OneDrive\Escritorio\Proyecto_Final_Progra2\Proyecto P2\Datos\dataBase\MiBaseDatos1.accdb;'
        conn = pyodbc.connect(con_string)
        print("Connected to db")
        
        sql =  ("""INSERT INTO inventario (Descripcion, Codigo, Costo, Cantidad, Fecha, Bodega) 
               VALUES(?,?,?,?,?,?)""")
        valores = (oArticulo.descripcion,oArticulo.codigo,
               oArticulo.costo,oArticulo.cantidad,
               oArticulo.fecha, oArticulo.bodega)
    
        cursor = conn.cursor()

        cursor.execute(sql, valores)
        conn.commit()
        print("Data inserted")

    except pyodbc.Error as e:
        print("Error Conexion")

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
            
def crear_bodega(oBodega):
    try:
        conn = pyodbc.connect(con_string)
        sql = ("""INSERT INTO bodega (Nombre) 
               VALUES(?)""")
        valores = (oBodega.nombre)
        cursor = conn.cursor()
        cursor.execute(sql, valores)
        conn.commit()
        print("Data inserted")

    except pyodbc.Error as e:
        print("Error Conexion" + str(e))

def obtener_lista_bodegas():
    conn = pyodbc.connect(con_string)# para conectarme a mi base 
    print("Conexion A BD")
    sql = """ SELECT * FROM bodega """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        lista_bodegas = cur.fetchall() # con esto me traigo todo lo que esta registrado
        return lista_bodegas
    
    except pyodbc.Error as e:
        print(" Error al llamar bodega "+ str(e))

