import sys
from PyQt6 import QtCore,QtWidgets,QtGui
from PyQt6.QtWidgets import QWidget
from UI.uiDistribuidor import Ui_Distribuidor
from PyQt6.QtCore import Qt
from Clases.claseDistribuidor import *
import datetime
from .permanencia import *

class DistribuidorVentana(QtWidgets.QWidget):
    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Distribuidor()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowType.Window)
        self.inicializar_controladores()
        self.ob_distribuidor = None
        self.ui.btn_crear_dist.clicked.connect(self.crear_distribuidor)
        self.ui.btn_refrescar.clicked.connect(self.tabla_distribuidores)
        
    def inicializar_controladores(self):# con esto inicializo my fecha en py pantalla window
        self.ui.dateEdit.setDate(QtCore.QDate.currentDate())
    
    
    def tabla_distribuidores(self):
        
        self.ui.tbl_distribuidores.setRowCount(0)
        
        self.num_fila = self.ui.tbl_distribuidores.rowCount()
         
        for item in Persistencia.obtener_distribuidor():
            self.ui.tbl_distribuidores.insertRow(num_fila)
            nombre = QtWidgets.QTableWidgetItem(item.nombre_emp)
            cedula = QtWidgets.QTableWidgetItem(str(item.ced_juridica_emp))
            telefono = QtWidgets.QTableWidgetItem(str(item.telefono_emp))
            fecha = QtWidgets.QTableWidgetItem(str(item.fecha))
            
            self.ui.tbl_distribuidores.setItem(num_fila,0,nombre) 
            self.ui.tbl_distribuidores.setItem(num_fila,1,cedula)
            self.ui.tbl_distribuidores.setItem(num_fila,2,telefono)
            self.ui.tbl_distribuidores.setItem(num_fila,3,fecha)
            
            num_fila +=1
        
        
    
    def crear_distribuidor(self):
        self.ob_distribuidor = Distribuidor() # para usar las variables de mi clase distribuidor
        self.ob_distribuidor.nombre_emp = self.ui.txt_nombre_emp.text()
        self.ob_distribuidor.ced_juridica_emp = self.ui.txt_ced_juri_emp.text()
        self.ob_distribuidor.telefono_emp = self.ui.txt_telefono_emp.text()
        self.ob_distribuidor.fecha = self.ui.dateEdit.text()
       
        # a continuacion agregar esto a una tabla, que me contendra la lista de los distribuidores
        Persistencia.registro_distribuidor(self.ob_distribuidor)
        self.limpiar_entradas()
    
        # para que me limpie las entradas una vez terminado tood
    
    def limpiar_entradas(self): # metodo para limpiar las etiquetas una vez escrito algo
        self.ui.txt_nombre_emp.clear()
        self.ui.txt_telefono_emp.clear()
        self.ui.txt_ced_juri_emp.clear()
        
        