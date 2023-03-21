# Esta clase corresponde a la bodega, como se organizara,
# que materiales tendra y marca
# y tambien la creacion de una nueva bodega de ser necesaria
class Bodega:
    def __init__(self) -> None:
        self.nombre_bodega = None # metodo para nombrar mi bodega
        self.cantidad_articulos = None # que tipo de materiales contendra mi bodega
        #self.distribuidor_materiales = distribuidor # Quien me distribuye los materiales de mi bodega
       # self.tipo_bodega = tipo_bodega # este metodo es para diferenciar mi bodega
        self.crear_bodega = None # me permitira crear una bodega
