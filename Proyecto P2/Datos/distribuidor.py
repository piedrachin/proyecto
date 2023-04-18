

import sys

from PyQt6 import QtCore,QtWidgets,QtGui
from PyQt6.QtWidgets import *
from UI.uiDistribuidor import Ui_Distribuidor
from PyQt6.QtCore import Qt
from Clases.claseDistribuidor import *
import datetime
from .permanencia import *
from Datos.dataBase.basedatos import (registrar_distribuidor,obtener_lista_distribuidor,
                                      eliminar_de_lista_distribuidor)

class DistribuidorVentana(QtWidgets.QWidget):
    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Distribuidor()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowType.Window)
        self.inicializar_controladores()
        self.llenar_tabla_con_BD(obtener_lista_distribuidor())
        self.ob_distribuidor = None
        #este metodo no me funciono, me genero un error por lo cual lo quite
      #  self.ui.btn_eliminar_dist.clicked.connect(self.eliminar_distribuidor)
        self.ui.btn_crear_dist.clicked.connect(self.crear_distribuidor)
        self.ui.btn_refrescar.clicked.connect(lambda: self.llenar_tabla_con_BD(obtener_lista_distribuidor()))
       # self.ui.tbl_distribuidores.setColumnWidth(0,0)
        self.ui.tbl_distribuidores.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.tbl_distribuidores.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
    def inicializar_controladores(self):# con esto inicializo my fecha en py pantalla window
        self.ui.dateEdit.setDate(QtCore.QDate.currentDate())
    
    def llenar_tabla_con_BD(self,data):
      #  data = obtener_lista_distribuidor()
        self.ui.tbl_distribuidores.setRowCount(len(data))
        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.ui.tbl_distribuidores.setItem(index_row, index_cell,QTableWidgetItem(str(cell)))
            
    
    def tabla_distribuidores(self):
        dato_dist = obtener_lista_distribuidor()
        self.ui.tbl_distribuidores.setRowCount(0)
        
        num_fila = self.ui.tbl_distribuidores.rowCount()
         
        for item in dato_dist:
            self.ui.tbl_distribuidores.insertRow(num_fila)
            distribuidor = QtWidgets.QTableWidgetItem(item.distribuidor)
            cedula = QtWidgets.QTableWidgetItem(str(item.cedula))
            telefono = QtWidgets.QTableWidgetItem(str(item.telefono))
            fecha = QtWidgets.QTableWidgetItem(str(item.fecha))
            
            self.ui.tbl_distribuidores.setItem(num_fila,1,distribuidor) 
            self.ui.tbl_distribuidores.setItem(num_fila,2,telefono)
            self.ui.tbl_distribuidores.setItem(num_fila,3,cedula)
            self.ui.tbl_distribuidores.setItem(num_fila,4,fecha)
            
            num_fila +=1
        
    def eliminar_distribuidor(self):  
        self.ui.tbl_distribuidores.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)  
        selec_fila = self.ui.tbl_distribuidores.selectedItems() 
        try:
            if selec_fila:
                articulo_id = int(selec_fila[0].text())
                fila = selec_fila[0].row()
                if eliminar_de_lista_distribuidor(articulo_id):
                    self.ui.tbl_distribuidores.removeRow(fila)
        except:
            print("No se pudo eliminar, ocurrio un error.")       
    def crear_distribuidor(self):
        self.ob_distribuidor = Distribuidor() # para usar las variables de mi clase distribuidor
        self.ob_distribuidor.distribuidor = str(self.ui.txt_nombre_emp.text())
        self.ob_distribuidor.cedula = str(self.ui.txt_ced_juri_emp.text())
        self.ob_distribuidor.telefono = str(self.ui.txt_telefono_emp.text())
        self.ob_distribuidor.fecha = str(self.ui.dateEdit.text())
        registrar_distribuidor(self.ob_distribuidor)
        # a continuacion agregar esto a una tabla, que me contendra la lista de los distribuidores
        Persistencia.registro_distribuidor(self.ob_distribuidor)
        self.limpiar_entradas()
    
        # para que me limpie las entradas una vez terminado tood
    
    def limpiar_entradas(self): # metodo para limpiar las etiquetas una vez escrito algo
        self.ui.txt_nombre_emp.clear()
        self.ui.txt_telefono_emp.clear()
        self.ui.txt_ced_juri_emp.clear()
        
        