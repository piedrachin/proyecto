import sys
from PyQt6 import QtCore,QtWidgets,QtGui
from PyQt6.QtWidgets import QWidget
from UI.uiBodega import Ui_Bodega
from PyQt6.QtCore import Qt
from Clases.claseBodeg import Bodega
from .permanencia import *

class Bodega(QtWidgets.QWidget):
    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Bodega()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowType.Window) # esto me permite que mi nueva ventana pueda ser manipulada,
        # sobre mi ventana padre.
        
        self.ob_bodega = None
        self.ui.btn_crear_bodega.clicked.connect(self.crear_bodega_en_cmb) # al darle click me creara la bodega en mi combobox
    
    def crear_bodega_en_cmb(self):
        self.ob_bodega = Bodega()
        nombre = self.ui.txt_nombre_bodega.text()
        Persistencia.crear_bodega(nombre)
        self.ui.txt_nombre_bodega.clear()