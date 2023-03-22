from PyQt6 import QtCore, QtGui, QtWidgets
from UI.uiMainWindow import Ui_Main_Window # para hacer uso de mi ventana Main, para poder usar las subventanas
from Aplicacion.registro_articulos import *


class Ventana_Main(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Main_Window() # con esto puedo hacer uso de mi ventana main
        self.ui.setupUi(self)# con esto inicializo mis controles
        self.ui.actionRegistro_Articulos.triggered.connect(self.OnClick_Registro_Articulos)
        self.ui.actionInventario_Articulos.triggered.connect(self.OnClick_Control_Articulos)
        self.ui.actionBodegas.triggered.connect(self.OnClick_Manejo_Bodegas)
        self.ui.actionDistribuidores.triggered.connect(self.OnClick_Registro_Distribuidores)
        
        self.pantalla_registro = None
        self.pantalla_bodega = None
        self.pantalla_control_articulos = None
        self.pantalla_distribuidores = None
    
    
    def OnClick_Registro_Articulos(self):
        self.pantalla_registro = Frm_Registro_Articulo()
        self.pantalla_registro.show()# con el metodo show hago visible la ventana
    
    def OnClick_Manejo_Bodegas(self):
        self.pantalla_bodega = Crear_Bodegas()
        self.pantalla_bodega.show()
    
    def OnClick_Registro_Distribuidores(self):
        self.pantalla_distribuidores = Crear_Distribuidor()
        self.pantalla_distribuidores.show()
    
    def OnClick_Control_Articulos(self):
        self.pantalla_control_articulos = Control_Inventario()
        self.pantalla_control_articulos.show()
#