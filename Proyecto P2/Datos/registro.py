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
from Clases.claseBodega import Bodega
#from .registro import Articulo
from .permanencia import *
#from .mibasedatos import registrar_articulo_en_bd

from Datos.dataBase.basedatos import (ingresar_articulos,seleccionar_articulos,
                                      eliminarArticulo, obtener_lista_bodegas,
                                      crear_bodega, eliminar_bodega)

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

        self.obtener_lista_bodegas_a_cmb()
        self.ancho_de_columnas_en_tablas()
        self.inicializar_controladores()
        self.iniciar_todos_los_botones_de_mi_vent_principal()
        self.llenar_tabla_con_bd(seleccionar_articulos())
      
        reg_ex = QtCore.QRegularExpression("^[0-9]*(\.[0-9]{1,2})?$") # esto es para que solo me permita numeros
        input_validator = QtGui.QRegularExpressionValidator(reg_ex, self.ui.txt_costo)# y no se introduzcan letras
        self.ui.txt_costo.setValidator(input_validator)
        
      #  self.ui.tbl_bodega.setColumnWidth(1,0)
       # self.ui.tbl_bodega.setColumnWidth(2,0)
        #self.ui.tbl_bodega.setColumnWidth(3,0)
        
        # este metodo me permite obtener las bodegas creadas de mi combobox
    def iniciar_todos_los_botones_de_mi_vent_principal(self):
        self.ui.btn_vent_pedido.clicked.connect(self.ventana_control_pedidos)
        self.ui.btn_refrescar_bodega.clicked.connect(self.crear_tabla_bodegas)
        self.ui.btn_crear_bdg.clicked.connect(self.crear_bodega_en_CMB)
        self.ui.btn_agregar.clicked.connect(self.registrar_articulo)   
        self.ui.btn_distribuidor.clicked.connect(self.ventana_perfil_distribuidor)
        self.ui.btn_crear_bodega.clicked.connect(self.ventana_crear_bodega)
        self.ui.btn_refrescar.clicked.connect(lambda: self.llenar_tabla_con_bd(seleccionar_articulos()))
        self.ui.btn_eliminar_tabla.clicked.connect(self.eliminar_articulos)
        self.ui.btn_refrescar_bodega.clicked.connect(lambda: self.llenar_tabla_bodegas_en_Bd(obtener_lista_bodegas()))
        self.ui.btn_elimar_tabla_bod.clicked.connect(self.eliminar_de_tabla_bodega)
    
    def limpiador_de_combobox_bodegas(self):
        self.ui.cmb_registro.clear()
        
    def obtener_lista_bodegas_a_cmb(self):
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
            
    def crear_bodega_en_CMB(self):
        self.nombre_bodega = Bodega()
        self.nombre_bodega.nombre = self.ui.txt_nombre_bodega.text()
        self.ui.cmb_registro.addItem(self.nombre_bodega.nombre)
        crear_bodega(self.nombre_bodega)
        Persistencia.crear_bodega(self.nombre_bodega)
        self.ui.txt_nombre_bodega.clear()
        
        #self.ui.txt_nombre_bodega.clear()
    def eliminar_articulos(self):
        selec_fila = self.ui.tbl_registro_articulos.selectedItems()
        
        if selec_fila:
            articulo_id = int(selec_fila[0].text())
            fila = selec_fila[0].row()
            if eliminarArticulo(articulo_id):
               self.ui.tbl_registro_articulos.removeRow(fila)
          # self.ui.tbl_registro_articulos.removeRow(fila)
          
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
   
   # este metodo me permite ir a la ventana pedidos
    def ventana_control_pedidos(self):
        from .pedido import VentanaPedido
        self.ventana_pedido = VentanaPedido()
        self.ventana_pedido.show()
        # este metodo me permite ir a la ventana del distribuidor
    
    def ventana_perfil_distribuidor(self):
        from .distribuidor import DistribuidorVentana
        self.ventana_distribuidor = DistribuidorVentana(self)
        self.ventana_distribuidor.show()# con este metodo muestro mi ventana
    
     # este metodo me permite ir a la ventana de crear bodega
    def ventana_crear_bodega(self):
        from .bodega import VentanaBodega # importo mi clase de bodega
        self.ventana_bodega = VentanaBodega(self)
        self.ventana_bodega.show()
      
      
      # este metodo me permite registrar o bien crear un articulo, que se vera en mi tabla    
    def registrar_articulo(self):
    
        self.o_registro = Articulo()#       
        self.o_registro.descripcion = self.ui.txt_nombre.text()
        self.o_registro.codigo = str(self.ui.txt_codigo.text())
        self.o_registro.cantidad = str(self.ui.spBox_cantidad.value())
        self.o_registro.costo = str(self.ui.txt_costo.text())
        self.o_registro.fecha = str(self.ui.dateEdit.text())
        self.o_registro.bodega = str(self.ui.cmb_registro.currentText()) 
                 
        ingresar_articulos(self.o_registro)
        
        self.check_espacios_vacios()

        # metodo para veirifcar si deje espacio en blanco
        #self.registro_art_txt() # me permite llevar un registro txt de todo
        Persistencia.registro_Articulo(self.o_registro) # para guardarlo y actualizarlo en mi tabla 
        self.limpiar_entrada()
    
    def encabezado_tabla_bodegas(self):
       
        encabezados_columnas = ("ID","Bodega","Descripcion","Codigo","Cantidad")
        self.ui.tbl_bodega.setColumnCount(len(encabezados_columnas))
        self.ui.tbl_bodega.setHorizontalHeaderLabels(encabezados_columnas)
        
    def eliminar_de_tabla_bodega(self):
        #selec_fila = self.ui.tbl_bodega.selectedItems()
        selec_fila = self.ui.tbl_bodega.selectedItems()  
        if selec_fila:
            bodega_id= str(selec_fila[0].text())
            try:
                
                int(bodega_id)
            except:
                print("no se puede convertir,", str, " a int")
            #bodega_id = int(selec_fila[0].text())
            fila = selec_fila[0].row()
            if eliminar_bodega(bodega_id):
               self.ui.tbl_bodega.removeRow(fila)
        #try:
        
         #   if selec_fila:
          #     articulo_id = int(selec_fila[0].text())
           #    fila = selec_fila[0].row()
            #if eliminar_bodega(articulo_id):
             #  self.ui.tbl_bodega.removeRow(fila)
        #except 
               
    def llenar_tabla_bodegas_en_Bd(self, data):
      #  self.obtener_lista_bodegas_a_cmb()
        self.obtener_lista_bodegas_a_cmb()
        self.ui.tbl_bodega.setRowCount(len(data))
        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.ui.tbl_bodega.setItem(index_row, index_cell,QTableWidgetItem(str(cell))) 
                
    def crear_tabla_bodegas(self):# esta tabla me permitira obtener la bodega y su respectivo material y cantidad
        self.ui.tbl_bodega.setRowCount(0)
        num_fila = self.ui.tbl_bodega.rowCount()
        
        
        
        for item in Persistencia.obtener_registro():
        #for item in obtener_lista_bodegas():
            self.ui.tbl_bodega.insertRow(num_fila)
            bodega = QtWidgets.QTableWidgetItem(item.nombre)
            descripcion  = QtWidgets.QTableWidgetItem(str(item.descripcion))
            codigo = QtWidgets.QTableWidgetItem(str(item.codigo))
            cantidad = QtWidgets.QTableWidgetItem(str(item.cantidad))
            
            self.ui.tbl_bodega.setItem(num_fila,0,bodega)
            self.ui.tbl_bodega.setItem(num_fila,1,descripcion)
            self.ui.tbl_bodega.setItem(num_fila,2,codigo)
            self.ui.tbl_bodega.setItem(num_fila,3,cantidad)
    
      #  for item in Persistencia.obtener_registro():
            
    
            
    def llenar_tabla_con_bd(self, data):        

        self.ui.tbl_registro_articulos.setRowCount(len(data))
        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.ui.tbl_registro_articulos.setItem(index_row, index_cell,QTableWidgetItem(str(cell)))
            
    def crear_tabla_registro(self, data):# agregar data 
      #  registro_art = seleccionar_articulos()      
        self.ui.tbl_registro_articulos.setRowCount(0)
        
        num_fila = self.ui.tbl_registro_articulos.rowCount()
         
        for item in Persistencia.obtener_registro():
       # for item in seleccionar_articulos():       
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
      
      
      # este meto me persuadira si existe algun espacio vacio
      
    def check_espacios_vacios(self):
        msg = QMessageBox() # 
        codigo =  self.ui.txt_codigo.text()
        costo =  self.ui.txt_costo.text()
        nombre = self.ui.txt_nombre.text()
        cantidad = self.ui.spBox_cantidad.value()
        
        if codigo == '' or costo == '' or nombre == '' or cantidad == '':
            
            msg = QtWidgets.QMessageBox(text=" Dejaste algun espacio Vacio. ")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.StandardButton(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
        
           
                
            
        
        
        
   

   
   
   
   
   
   





