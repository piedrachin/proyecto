import pyodbc

import sys
from Datos.dataBase.basedatos import con_string
from PyQt6 import QtCore,QtWidgets,QtGui
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtCore import *
from UI.uiRegistro import Ui_Dialog
from Clases.claseArticulo import Articulo
from Clases.claseDistribuidor import Distribuidor
from Clases.claseBodeg import Bodega
#from .registro import Articulo
from .permanencia import *
#from .mibasedatos import registrar_articulo_en_bd

from Datos.dataBase.basedatos import (ingresar_articulos,seleccionar_articulos,
                                      crear_bodega)

import datetime


#articulos_reg = []

class Registro(QtWidgets.QDialog):
    
    def __init__(self, parent = None):
        super(Registro, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.o_registro = None
        self.ob_bodega = None
        self.tabla_articulos = []
       # self.Cargar_Combobox(obtener_lista_bodegas())
        self.obtener_lista_bodegas()
      # self.agregar_bodegas_a_cmb(obtener_lista_bodegas())
        self.ancho_de_columnas_en_tablas()
        self.inicializar_controladores()
        self.llenar_tabla_con_bd(seleccionar_articulos())
       # self.crear_tabla_registro(seleccionar_articulos())
        self.ui.btn_refrescar_bodega.clicked.connect(self.crear_tabla_bodegas)
        self.ui.btn_imprimir_txt.clicked.connect(self.crear_bodega_en_CMB)
        self.ui.btn_agregar.clicked.connect(self.registrar_articulo)   
        self.ui.btn_distribuidor.clicked.connect(self.ventana_perfil_distribuidor)
        self.ui.btn_crear_bodega.clicked.connect(self.ventana_crear_bodega)
        self.ui.btn_refrescar.clicked.connect(self.crear_tabla_registro)
        
        
        reg_ex = QtCore.QRegularExpression("^[0-9]*(\.[0-9]{1,2})?$") # esto es para que solo me permita numeros
        input_validator = QtGui.QRegularExpressionValidator(reg_ex, self.ui.txt_costo)# y no se introduzcan letras
        self.ui.txt_costo.setValidator(input_validator)
        
    def obtener_lista_bodegas(self):
        try:
            self.conn = pyodbc.connect(con_string)# para conectarme a mi base 
            print("Conexion A BD")
            self.cur = self.conn.cursor()
            self.cur.execute('''SELECT Nombre FROM bodega ''')
            data = self.cur.fetchall()
            for category in data:
               self.ui.cmb_registro.addItem(category[0])
        except pyodbc.Error as e:
            print(" Error al llamar bodega "+ str(e))                      
    def ancho_de_columnas_en_tablas(self):
        self.ui.tbl_registro_articulos.setColumnWidth(0, 0)
        self.ui.tbl_registro_articulos.setColumnWidth(1,230)
        self.ui.tbl_bodega.setColumnWidth(1,230)
    def Cargar_Combobox(self,data):
        self.ui.cmb_registro.addItem(data)
        
     #   self.ui.cmb_registro.currentText()
       # combo = self.ui.cmb_registro      
        #model = obtener_lista_bodegas()
        
        #combo.setModel(model)
        #combo.setModelColumn(1)
            
    def crear_bodega_en_CMB(self):
        self.nombre_bodega = Bodega()
        self.nombre_bodega.nombre = self.ui.txt_nombre_bodega.text()
        self.ui.cmb_registro.addItem(self.nombre_bodega.nombre)
        crear_bodega(self.nombre_bodega)
        
        self.ui.txt_nombre_bodega.clear()


   
    def registro_art_txt(self):
        descripcion = self.ui.txt_nombre.text()
        codigo = self.ui.txt_codigo.text()
        cantidad = str(self.ui.spBox_cantidad.value())
        costo = str(self.ui.txt_costo.text())
        bodega = self.ui.cmb_registro.currentText()
       # fecha = str(self.ui.dateEdit.date())
        fecha = str(self.ui.dateEdit.text()) 
        i = 0
        #self.datos = (self.Nombre, self.Codigo, self.Cantidad)
        file = open("registro.txt", "a")
        file.write(str(i+1))
        file.write("\n---------- ARTICULOS REGISTRADOS ----------")
      #  file.write(str(i))
        file.write("\nDescripcion: "+descripcion+"\nCodigo: "+codigo+"\nCantidad: "
                   +cantidad+"\nCosto: "+costo+
            "\nFecha: "+fecha+"\n"+ "\nBodega: "+bodega)
        file.write("\n")
        i += 1
        file.close()    
 
    def inicializar_controladores(self):# con esto inicializo my fecha en py pantalla window
        self.ui.dateEdit.setDate(QtCore.QDate.currentDate())
    
    def ventana_perfil_distribuidor(self):
        from .distribuidor import DistribuidorVentana
        self.ventana_distribuidor = DistribuidorVentana(self)
        self.ventana_distribuidor.show()# con este metodo muestro mi ventana
    def ventana_crear_bodega(self):
        from .bodega import Bodega # importo mi clase de bodega
        self.ventana_bodega = Bodega(self)
        self.ventana_bodega.show()
        
    def registrar_articulo(self):
        self.o_registro = Articulo()#       
        self.o_registro.descripcion = self.ui.txt_nombre.text()
        self.o_registro.codigo = str(self.ui.txt_codigo.text())
        self.o_registro.cantidad = str(self.ui.spBox_cantidad.value())
        self.o_registro.costo = str(self.ui.txt_costo.text())
        self.o_registro.fecha = str(self.ui.dateEdit.text())
        self.o_registro.bodega = self.ui.cmb_registro.currentText()
       # BD.registrarArticulo(self.o_registro)
        ingresar_articulos(self.o_registro)
        #ingresar_articulos(self.o_registro)
        # metodo para veirifcar si deje espacio en blanco
        self.registro_art_txt() # me permite llevar un registro txt de todo
        Persistencia.registro_Articulo(self.o_registro) # para guardarlo y actualizarlo en mi tabla 
        self.limpiar_entrada()
     
    def crear_tabla_bodegas(self):# esta tabla me permitira obtener la bodega y su respectivo material y cantidad
        self.ui.tbl_bodega.setRowCount(0)
        num_fila = self.ui.tbl_bodega.rowCount()
        for item in Persistencia.obtener_registro():
            self.ui.tbl_bodega.insertRow(num_fila)
            bodega = QtWidgets.QTableWidgetItem(str(item.bodega))
            descripcion  = QtWidgets.QTableWidgetItem(str(item.descripcion))
            cantidad = QtWidgets.QTableWidgetItem(str(item.cantidad))
            
            self.ui.tbl_bodega.setItem(num_fila,0,bodega)
            self.ui.tbl_bodega.setItem(num_fila,1,descripcion)
            self.ui.tbl_bodega.setItem(num_fila,2,cantidad)
    def llenar_tabla_con_bd(self, data):
        self.ui.tbl_registro_articulos.setRowCount(len(data))
        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.ui.tbl_registro_articulos.setItem(index_row, index_cell,QTableWidgetItem(str(cell)))
            
    def crear_tabla_registro(self, data):# agregar data       
       # self.ui.tbl_registro_articulos.setRowCount(len(data))
      #  for (index_row, row) in enumerate(data):
     #       for(index_cell, cell) in enumerate(row):
    #            self.ui.tbl_registro_articulos.setItem(index_row, index_cell,QTableWidgetItem(str(cell)))
              
        self.ui.tbl_registro_articulos.setRowCount(0)
        
        num_fila = self.ui.tbl_registro_articulos.rowCount()
         
        for item in Persistencia.obtener_registro():
                
            self.ui.tbl_registro_articulos.insertRow(num_fila)
            descripcion = QtWidgets.QTableWidgetItem(item.descripcion)
            codigo = QtWidgets.QTableWidgetItem(str(item.codigo))
            costo = QtWidgets.QTableWidgetItem(str(item.costo))
            cantidad = QtWidgets.QTableWidgetItem(str(item.cantidad))
            fecha = QtWidgets.QTableWidgetItem(str(item.fecha))
            bodega = QtWidgets.QTableWidgetItem(str(item.bodega))
            
            self.ui.tbl_registro_articulos.setItem(num_fila,0,descripcion) 
            self.ui.tbl_registro_articulos.setItem(num_fila,1,codigo)
            self.ui.tbl_registro_articulos.setItem(num_fila,2,costo)
            self.ui.tbl_registro_articulos.setItem(num_fila,3,cantidad)
            self.ui.tbl_registro_articulos.setItem(num_fila,4,fecha)
            self.ui.tbl_registro_articulos.setItem(num_fila,5,bodega) 
            num_fila +=1
       
                                     
    def limpiar_entrada(self):
       self.ui.txt_nombre.clear()
       self.ui.txt_codigo.clear()
       self.ui.txt_costo.clear()
       self.ui.spBox_cantidad.setValue(0)
      # self.ui.cmb_bodega.clear()
      
    def check_espacios_vacios(self):
        msg = QMessageBox() # 
        codido =  self.ui.txt_codigo.text()
        costo =  self.ui.txt_costo.text()
        nombre = self.ui.txt_nombre.text()
        cantidad = self.ui.spBox_cantidad.value()
        
        if codido == " ":
            msg = QtWidgets.QMessageBox(text="Degaste el espacio Codigo vacio.")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
        if costo == " ":
            msg = QtWidgets.QMessageBox(text="Dejaste el espacio Costo vacio.")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
        if nombre == " ":
            msg = QtWidgets.QMessageBox(text="Dejaste el espacio Descripcion vacio.")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setStandardButtons(msg.StandardButton.Ok)
            msg.exec()
        if cantidad == " ":
            msg = QtWidgets.QMessageBox(text="Dejaste el espacio Cantidad Vacio.")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
        
            
        
           
                
            
        
        
        
   

   
   
   
   
   
   





