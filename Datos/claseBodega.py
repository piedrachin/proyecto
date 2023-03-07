# Esta clase corresponde a la bodega, como se organizara,
# que materiales tendra y marca
# y tambien la creacion de una nueva bodega de ser necesaria
class Bodega:
    def __init__(self,tipo_materiales, distribuidor, tipo_bodega) -> None:
        self.nombre_bodega = None # metodo para nombrar mi bodega
        self.tipo_materiales = tipo_materiales # que tipo de materiales contendra mi bodega
        self.distribuidor_materiales = distribuidor # Quien me distribuye los materiales de mi bodega
        self.tipo_bodega = tipo_bodega # este metodo es para diferenciar mi bodega
       # self.crear_bodega = crear_bodega # me permitira crear una bodega
