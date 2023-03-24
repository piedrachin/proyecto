class Persistencia:
    listado_Articulos = []
    lista_bodegas = []
    
    @classmethod
    def agregar_articulo(self,objeto):
        self.listado_Articulos.append(objeto)
    
    @classmethod    
    def control_articulo(self):
        return self.listado_Articulos
    
    @classmethod
    def crear_bodegas(self,objeto_bodega): 
        self.lista_bodegas.append(objeto_bodega)
    @classmethod    
    def asignar_bodega(self):
        return self.lista_bodegas
    
    
    @classmethod
    def perfil_distribuidores(self):
        pass