# Esta clase contiene toda la informacion, respecto a un articulo
# como "marca","tipo","precio", etc
# Se registraran los articulos
lista_articulos = [] # aca me almacenara todos los articulos
class Articulo:
    
    def __init__(self) -> None:
        self.nombre_articulo = None # para añadirle una marca al articulo
        self.tipo_articulo = None  # para distinguir el tipo de articulo
        self.costo_articulo = None # para determinar el costo del articulo
        self.distribuidr_articulo = None
       # self.añadir_articulo = añadir_articulo
        

#anañir = lista_articulos[lista_articulos]
#anañir = lista_articulos.append(input("Que articulo desea añadir: "))
#print(lista_articulos)
lista_articulos.append(input("Que desea añadir"))       
#añadir = Articulo()
print(lista_articulos())
#añadir.tipo=        