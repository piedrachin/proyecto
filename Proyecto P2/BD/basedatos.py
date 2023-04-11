import mysql.connector


config = {
    'user': 'root',
    'password': 'Blinded3718.@',
    'host': '127.0.0.1',
    'port': '3306',
    'database': 'inventario'
}

miConexion = mysql.connector.connect(**config)

def registrarArticulo(oArticulo):
    cursorDB = miConexion.cursor()
    sentenciaSQL = ("INSERT INTO inventario.registro "+
                    "(`descripcion`,"+
                    "`codigo`,"+
                    "`costo`,"+
                    "`cantidad`,"+
                    "`fecha`)"+
                    "VALUES (%s,%s,%s,%s,%s,%s)")
    valores = (oArticulo.descripcion,oArticulo.codigo,
               oArticulo.costo,oArticulo.cantidad,
               oArticulo.fecha)
    
    cursorDB.execute(sentenciaSQL,valores)
    miConexion.commit() #Sin esto no quedaria guardado en base datos, esto es obligatorio

def modificarArticulo(oCliente):
    cursorDB = miConexion.cursor()
    sentenciaSQL = ("UPDATE cuscatlan.clientes "+                    
                    "set nomCliente = %s,"+
                    "    ape1Cliente = %s,"+
                    "    ape2Cliente = %s,"+
                    "    generoClien = %s,"+
                    "    CantViajes = %s,"+
                    "    Salario = %s "+
                    "WHERE IdeCliente = %s")
    valores = (oCliente.nomCliente,oCliente.ape1Cliente,oCliente.ape2Cliente,
               oCliente.generoClien,oCliente.cantViajes,oCliente.salario,oCliente.ideCliente)
    
    cursorDB.execute(sentenciaSQL,valores)
    miConexion.commit()

def consultarClientes() -> dict:
    cursorDB = miConexion.cursor()
    sentenciaSQL = "Select * from inventario.registro"
    cursorDB.execute(sentenciaSQL)
    rs = cursorDB.fetchall()
    return rs

def buscarCliente(identificacion) -> dict:
    cursorDB = miConexion.cursor()
    sentenciaSQL = "Select * from cuscatlan.clientes Where IdeCliente = %s"    
    valores = (identificacion,)
    cursorDB.execute(sentenciaSQL,valores)
    rs = cursorDB.fetchone()
    return rs

def eliminarArticulo(id):
    conn = pyodbc.connect(con_string)# para conectarme a mi base 
    cur = conn.cursor()
    sql = ("Delete from inventario where ID ART = %s")                
    valores = (id,)    
    cur.execute(sql,valores)
    conn.commit()
        
def eliminarCliente(identificacion):
    cursorDB = miConexion.cursor()
    sentenciaSQL = ("Delete from cuscatlan.clientes Where IdeCliente = %s")                    
    valores = (identificacion,)    
    cursorDB.execute(sentenciaSQL,valores)
    miConexion.commit()
    
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
            