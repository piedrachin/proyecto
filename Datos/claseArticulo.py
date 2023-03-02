# Esta clase contiene toda la informacion, respecto a un articulo
# como "marca","tipo","precio", etc
# Se registraran los articulos
lista_articulos = [] # aca me almacenara todos los articulos
class Articulo:
    
    def __init__(self,marca,tipo,costo) -> None:
        self.marca = marca # para añadirle una marca al articulo
        self.tipo = tipo  # para distinguir el tipo de articulo
        self.costo = costo # para determinar el costo del articulo
        

#anañir = lista_articulos[lista_articulos]
#anañir = lista_articulos.append(input("Que articulo desea añadir: "))
#print(lista_articulos)
lista_articulos.append(input("Que desea añadir"))       
#añadir = Articulo()

#añadir.tipo=        