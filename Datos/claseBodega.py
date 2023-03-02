# Esta clase corresponde a la bodega, como se organizara,
# que materiales tendra y marca
class Bodega:
    def __init__(self, materiales, marca, ubicacion_materiales) -> None:
        self.materiales = materiales
        self.marca = marca
        self.ubicacion_materiales = ubicacion_materiales
