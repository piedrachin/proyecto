import pyodbc
import sys

from PyQt6 import QtCore,QtWidgets,QtGui
from PyQt6.QtWidgets import *
from UI.uiVentPedido import Ui_Registro
from .permanencia import *
from PyQt6.QtCore import Qt
from Datos.dataBase.basedatos import seleccionar_articulos

class VentanaPedido(QtWidgets.QDialog):
    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Registro()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowType.Window) # esto me permite que mi nueva ventana pueda ser manipulada,
        # sobre mi ventana padre.
        self.lista_articulos_registrados_en_BD(seleccionar_articulos())
        self.encabezados_de_mi_tabla_lista_articulos_regis()
        self.ui.btn_refrescar_vent.clicked.connect(lambda:self.lista_articulos_registrados_en_BD(seleccionar_articulos()) )
    def encabezados_de_mi_tabla_lista_articulos_regis(self):
        encabezados_columnas = ("ID", "Descripcion","Codigo","Costo","Cantidad","Fecha","Bodega")
        self.ui.tbl_lista_articulos_regis.setColumnCount(len(encabezados_columnas))
        self.ui.tbl_lista_articulos_regis.setHorizontalHeaderLabels(encabezados_columnas)
      #  self.ui.tbl_lista_articulos_regis.setColumnWidth(0,0)
    # este medoto me obtendra todos los articulos registrados en mi bd
    #data me permite obtener la lista completa de los items en mi tabla inventario
    def lista_articulos_registrados_en_BD(self, data):
        self.ui.tbl_lista_articulos_regis.setRowCount(len(data))
        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.ui.tbl_lista_articulos_regis.setItem(index_row, index_cell,QTableWidgetItem(str(cell)))
    
    def lista_articulos_registrados(self):
        art_creado = seleccionar_articulos()
        self.ui.tbl_lista_articulos_regis.setRowCount(0)
        self.numFila = self.ui.tbl_lista_articulos_regis.rowCount()
        
        for items in art_creado():
            self.ui.tbl_lista_articulos_regis.insertRow(self.numFila)
            descripcion = QtWidgets.QTableWidgetItem(items.descripcion)
            codigo = QtWidgets.QTableWidgetItem(str(items.codigo))
            costo = QtWidgets.QTableWidgetItem(str(items.costo))
            cantidad = QtWidgets.QTableWidgetItem(str(items.cantidad))
            fecha = QtWidgets.QTableWidgetItem(str(items.fecha))
            bodega = QtWidgets.QTableWidgetItem(str(items.bodega))
            
            self.ui.tbl_lista_articulos_regis.setItem(self.numFila,0,descripcion) 
            self.ui.tbl_lista_articulos_regis.setItem(self.numFila,1,codigo)
            self.ui.tbl_lista_articulos_regis.setItem(self.numFila,2,costo)
            self.ui.tbl_lista_articulos_regis.setItem(self.numFila,3,cantidad)
            self.ui.tbl_lista_articulos_regis.setItem(self.numFila,4,fecha)
            self.ui.tbl_lista_articulos_regis.setItem(self.numFila,5,bodega) 

            self.numFila +=1 # para sumar mas filas
        
           