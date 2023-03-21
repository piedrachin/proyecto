# Esta clase contiene toda la informacion, respecto a un articulo
# como "marca","tipo","precio", etc
# Se registraran los articulos
#lista_articulos = [] # aca me almacenara todos los articulos

# Esta sera mi clase encargada de registrar los articulos

class Registro_articulo:
    
    def __init__(self) -> None:
        self.nombre_articulo = None # para añadirle una marca al articulo
        self.codigo_articulo = None  # para distinguir el tipo de articulo
        self.costo_articulo = None # para determinar el costo del articulo
        self.cantidad_articulo = None
        self.añadir_articulo_a = None
        self.fecha_se_añade_articulo = None
        
       # self.formato_codigo = "PP#{0}"
        #self.codigo_consecutivo = 1  

#anañir = lista_articulos[lista_articulos]
#anañir = lista_articulos.append(input("Que articulo desea añadir: "))
#print(lista_articulos)
#lista_articulos.append(input("Que desea añadir"))       
#añadir = Articulo()
#print(lista_articulos())
#añadir.tipo=        