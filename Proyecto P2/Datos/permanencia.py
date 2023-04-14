class Persistencia:
    lista_articulos = []
    lista_distribuidor = []
    lista_bodega = []
    @classmethod
    def registro_Articulo(self,objeto):
        self.lista_articulos.append(objeto)  
    @classmethod    
    def obtener_registro(self):
        return self.lista_articulos
    
    @classmethod
    def registro_distribuidor(self, objeto):
        self.lista_distribuidor.append(objeto)
    @classmethod
    def obtener_distribuidor(self):
        return self.lista_distribuidor
    @classmethod    
    def eliminarDistribuidor(self, numero):
        self.lista_bodega.pop(numero)
    
    
    @classmethod
    def crear_bodega(self, obodega):
        self.lista_bodega.append(obodega)
    @classmethod
    def obtener_bodega(self):
        return self.lista_bodega
    @classmethod    
    def eliminarBodega(self, numero):
        self.lista_bodega.pop(numero)
    