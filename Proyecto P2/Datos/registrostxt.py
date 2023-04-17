import os
import sys
from PyQt6 import QtCore,QtGui,QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from UI.uiRegistrosTXT import Ui_Registros

class VentanaRegistrosDelTxt(QtWidgets.QDialog):
    def __init__(self, parent = None) :
        super().__init__(parent)
        self.ui = Ui_Registros()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowType.Window) # esto me permite que mi nueva ventana pueda ser manipulada,
        # sobre mi ventana padre.
        
        self.ui_path = os.path.dirname(os.path.dirname(__file__))#__file__
        self.ui.btn_ver_registro.clicked.connect(self.obtener_registros_de_mi_ventana_txt)
        self.ui.plainTextEdit.setReadOnly(True)
    def obtener_registros_de_mi_ventana_txt(self):
        try:
            archivo = open(os.path.join(self.ui_path,"IngresosNuevos.txt"),'r')  
            texto = archivo.read()      
            self.ui.plainTextEdit.setPlainText(texto)
            archivo.close()
            
        except:
            print("No se encontro")
      
