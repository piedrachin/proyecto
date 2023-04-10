def registrar_articulo_en_bd(data):
    conn = crear_conexion()
    sql =  """INSERT INTO registro_articulos(Descripcion, Codigo, Costo, Cantidad) 
               VALUES(?,?,?,?)"""
    

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()# para que me guarde y surja efecto
        print ("Ingreso exitoso")
        return True
    except Error as e:
        print("Ocurrio un error: "+str(e))
    finally:
        if conn: #si la conexion existe
            cur.close()
            conn.close()
            
           
           
           
def actualizar_articulos(id, data):
    conn = crear_conexion()# con esto creo mi conexion automaticamente
    
    sql = """ UPDATE registro_articulos SET 
                            Descripcion = ?,
                            Codigo = ?,
                            Costo = ?,
                            Cantidad = ?
              WHERE ID = {id}""" # por la ide del articulo modificaremos
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Actualizacion correcta")
        return True
    except Error as e:
        print("Error actualizando registro: "+ str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def eliminar_articulos(id):
    conn = crear_conexion()
    sql = f"DELETE FROM registro_articulos WHERE ID = {id}"
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Articulo eliminado")
        return True
    except Error as e:
        print("Error al eliminar articulo "+ str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def seleccionar_articulos():
    conn = crear_conexion()
    sql = """SELECT * FROM registro_articulos"""
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        registro_articulos = cur.fetchall() # con esto me traigo todo lo que esta registrado
        return registro_articulos
    except Error as e:
        print(" Error al selecionar articulos "+ str(e))
    finally:
        if conn:
            cur.close()
            conn.close()


# se crean con el fin tentativo de poder sacar un articulo

def seleccionar_articulo_por_id(id):
    conn = crear_conexion()
    sql = f"SELECT * FROM registro_articulos WHERE ID = {id}"
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        registro_articulos = cur.fetchall()
        return registro_articulos
    except Error as e:
        print("Error selecionando por ID: "+ str(e))
    finally:
        if conn:
            cur.close()
            conn.close()
def selecionar_articulo_por_nombre(Descripcion):
    conn = crear_conexion()
    sql = f"SELECT * FROM registro_articulos WHERE Descripcion LIKE '%{Descripcion}%'"
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        registro_articulos = cur.fetchall()
        return registro_articulos
    except Error as e:
        print("Error al selecionar por descripcion: "+ str(e))
    
    finally:
        if conn:
            cur.close()
            conn.close()
            
        
        
    


