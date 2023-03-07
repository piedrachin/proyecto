# Esta clase contendra la informacion pertenesiente al proveedor, de forma breve
# como nombre, producto, 
#

class Distribuidor:
    def __init__(self, nombre, ced_juridica, tipo_producto) -> None:
        self.nombre = nombre
        self.ced_juridica = ced_juridica
        self.tipo_producto = tipo_producto
        self.cantidad_producto= None
        