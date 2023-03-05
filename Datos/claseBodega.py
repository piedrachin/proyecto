# Esta clase corresponde a la bodega, como se organizara,
# que materiales tendra y marca
# y tambien la creacion de una nueva bodega de ser necesaria
class Bodega:
    def __init__(self, materiales, marca, tipo_bodega, crear_bodega) -> None:
        self.materiales = materiales
        self.marca = marca
        self.tipo_bodega = tipo_bodega # este metodo es para diferenciar mi bodega
        self.crear_bodega = crear_bodega # me permitira crear una bodega
