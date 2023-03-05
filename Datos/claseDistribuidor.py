# Esta clase contendra la informacion pertenesiente al proveedor, de forma breve
# como nombre, producto, 
#

class Distribuidor:
    def __init__(self, nombre, ced_juridica, producto) -> None:
        self.nombre = nombre
        self.ced_juridica = ced_juridica
        self.producto = producto