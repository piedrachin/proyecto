import pyodbc
import sys

from PyQt6 import QtCore,QtWidgets,QtGui
from PyQt6.QtWidgets import *
from UI.uiBodega import Ui_Bodega
from PyQt6.QtCore import Qt
from Clases.claseBodega import *
from .permanencia import *
#from Datos.dataBase.basedatos import con_string
from Datos.dataBase.basedatos import obtener_lista_bodegas, eliminar_bodega, crear_bodega, seleccionar_articulos

class VentanaBodega(QtWidgets.QWidget):
    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Bodega()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowType.Window) # esto me permite que mi nueva ventana pueda ser manipulada,
        # sobre mi ventana padre.
     
        self.ancho_de_columnas_en_tablas()
   
  
        self.encabezados_de_mi_tabla_bodega()
        self.lista_articulos_registrados_x_bodega_en_BD(seleccionar_articulos())
        self.ob_bodega = None
        self.ui.btn_crear_bodega.clicked.connect(self.crear_bodega_en_cmb) # al darle click me creara la bodega en mi combobox
      #  self.ui.btn_eliminar_bodega.clicked.connect(self.eliminar_bodegas)
     #   self.ui.btn_eliminar_bodega.clicked.connect(self.eliminar_bodegas_creadas)
        self.ui.btn_actualizar.clicked.connect(lambda:self.crear_tabla_bodegas(obtener_lista_bodegas()) )
        #self.ui.btn_actualizar.clicked.connect(lambda: self.lista_articulos_registrados_x_bodega_en_BD(seleccionar_articulos()))
    def eliminar_bodegas_creadas(self):
        selec_fila = self.ui.tbl_bodegas_cr.selectedItems()
        
        if selec_fila:
            articulo_id = (selec_fila[0].text())
            fila = selec_fila[0].row()
            if eliminar_bodega(articulo_id):
               self.ui.tbl_bodegas_cr.removeRow(fila)
        
    def ancho_de_columnas_en_tablas(self):
      #  self.ui.tbl_bodegas_cr.setColumnWidth(0, 0)
        self.ui.tbl_bodegas_cr.setColumnWidth(0, 100)
        self.ui.tbl_bodegas_cr.setColumnWidth(1,230)
     # este metodo me crea las bodegas y las inserta en ACCESS
    def crear_bodega_en_cmb(self):
        self.ob_bodega = Bodega()
        self.ob_bodega.nombre = self.ui.txt_nombre_bodega.text()  
        crear_bodega(self.ob_bodega)
        Persistencia.crear_bodega(self.ob_bodega)
        self.ui.txt_nombre_bodega.clear()
        
    def crear_tabla_bodegas(self, data):
      #  self.agregar_articulos_a_mi_tabla_bodegas()
        self.ui.tbl_bodegas_cr.setRowCount(len(data))
        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.ui.tbl_bodegas_cr.setItem(index_row, index_cell,QTableWidgetItem(str(cell)))
                
    def eliminar_bodegas(self):
        selec_fila = self.ui.tbl_bodegas_cr.selectedItems()  
        try:
            if selec_fila:
                articulo_id = int(selec_fila[0].text())
                fila = selec_fila[0].row()
                if eliminar_bodega(articulo_id):
                    self.ui.tbl_bodegas_cr.removeRow(fila)
        except:
            print("No se pudo eliminar, ocurrio un error.")    
               
    def encabezados_de_mi_tabla_bodega(self):
        encabezados_columnas = ("Bodega","Articulo", "Codigo","Costo","Cantidad")
        self.ui.tbl_bodegas_cr.setColumnCount(len(encabezados_columnas))
        self.ui.tbl_bodegas_cr.setHorizontalHeaderLabels(encabezados_columnas)
        
    def lista_articulos_registrados_x_bodega_en_BD(self, data):
        self.ui.tbl_bodegas_cr.setRowCount(len(data))
        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.ui.tbl_bodegas_cr.setItem(index_row, index_cell,QTableWidgetItem(str(cell)))    
# este metood esta en veremos, esta tentativo
    def agregar_articulos_a_mi_tabla_bodegas(self):
       # art_cread = seleccionar_articulos()
        self.ui.tbl_bodegas_cr.setRowCount(0)
        num_fila = self.ui.tbl_bodegas_cr.rowCount()
        for item in Persistencia.obtener_registro():
    #    for item in Persistencia.obtener_registro():
            self.ui.tbl_bodegas_cr.insertRow(num_fila)
          #  bodega = QtWidgets.QTableWidgetItem(item.nombre)
            descripcion  = QtWidgets.QTableWidgetItem(str(item.descripcion))
            cantidad = QtWidgets.QTableWidgetItem(str(item.cantidad))
            codigo = QtWidgets.QTableWidgetItem(str(item.codigo))
            
           # self.ui.tbl_bodegas_cr.setItem(num_fila,0,bodega)
            self.ui.tbl_bodegas_cr.setItem(num_fila,1,descripcion)
            self.ui.tbl_bodegas_cr.setItem(num_fila,3,cantidad)
            self.ui.tbl_bodegas_cr.setItem(num_fila,2,codigo)
            
            num_fila += 1
      
      
            
    def crear_tabla_bodega(self):
        #obtener_lista_bodegas()
        self.ui.tbl_bodegas_cr.setRowCount(0)
        num_fila = self.ui.tbl_bodegas_cr.rowCount()
    
        for item in Persistencia.obtener_registro():
            self.ui.tbl_bodegas_cr.insertRow(num_fila)
            bodega = QtWidgets.QTableWidgetItem(str(item.bodega))
            descripcion  = QtWidgets.QTableWidgetItem(str(item.descripcion))
            cantidad = QtWidgets.QTableWidgetItem(str(item.cantidad))
            codigo = QtWidgets.QTableWidgetItem(str(item.codigo))
            cantidad = QtWidgets.QTableWidgetItem(str(item.cantidad))
            
            self.ui.tbl_bodegas_cr.setItem(num_fila,0,bodega)
            self.ui.tbl_bodegas_cr.setItem(num_fila,1,descripcion)
            self.ui.tbl_bodegas_cr.setItem(num_fila,3,cantidad)
            self.ui.tbl_bodegas_cr.setItem(num_fila,2,codigo)
            
            
           # self.ui.tbl_bodegas_cr.setItem(num_fila,0,bodega)
               
              