import pyodbc
import sys
import datetime
import os
from PyQt6.QtGui import *
from PyQt6 import QtCore,QtWidgets,QtGui
from PyQt6.QtWidgets import *
from UI.uiVentPedido import Ui_Registro
from .permanencia import *
from PyQt6.QtCore import Qt
from Clases.claseArticulo import Articulo
formato_registro = "REG#{0}"
consecutivo_registro = 1
from Datos.dataBase.basedatos import buscar_articulo,seleccionar_articulos, con_string, ingresar_articulos, actualizar_articulos_en_pedido

class VentanaPedido(QtWidgets.QDialog):
    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Registro()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowType.Window) # esto me permite que mi nueva ventana pueda ser manipulada,
        # sobre mi ventana padre.
        self.ob_art = None
        self.modo = 'M'
        self.habilitar_controles(False)
        self.inicializar_controladores()
        self.ui.tbl_lista_articulos_regis.clicked.connect(self.metodo_cargar_datos_en_controles)
        self.ui_path = os.path.dirname(os.path.abspath(__file__))
        self.lista_articulos_registrados_en_BD(seleccionar_articulos())
        self.encabezados_de_mi_tabla_lista_articulos_regis()
        self.ui.btn_refrescar_vent.clicked.connect(lambda:self.lista_articulos_registrados_en_BD(seleccionar_articulos()) )
        self.ui.btn_agregar_tabla.clicked.connect(self.control_articulos_ingresados)
        self.ui.btn_abrir_reporte.clicked.connect(self.abrir_ventana_reporte_OnClicked)
       # para que nadie pueda modificar mis filas
        self.ui.tbl_lista_articulos_regis.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
       # para que me seleccione una sola fila
        self.ui.tbl_lista_articulos_regis.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.obtener_lista_bodegas_a_cmb()
        self.obtener_lista_distribuidores_a_cmb()

        self.modelolista = QtGui.QStandardItemModel()
        self.ui.tbl_lista_por_imp.setModel(self.modelolista)
       # self.ui.tbl_lista_por_imp.sele
       # self.ui.btn_abrir_reporte.clicked.connect(self.dsplegar_registros_de_ingresos_desde_txt)
        self.ui.tbl_lista_articulos_regis.setColumnWidth(0,0)
        self.ui.txt_consecutivo.setReadOnly(True)
        self.ui.textEdit_reportes.setReadOnly(True)
        self.ui.btn_editar.clicked.connect(lambda: self.establecerModoPantalla(self.ui.btn_editar)) 
        
        
           
    def inicializar_controladores(self):# con esto inicializo my fecha en py pantalla window
        self.ui.dateEdit.setDate(QtCore.QDate.currentDate())   
    
      
    def metodo_para_llenar_controles(self):
        
       try:
          
            self.ui.txt_nombre_art.setText(str(self.ob_art.descripcion))#2
            self.ui.txt_codigo_art.setText(str(self.ob_art.codigo))#1
          #  self.ui.spBox_cantidad.setValue(int(self.ob_art.cantidad))#3   
            self.ui.cmbox_bodegas.setCurrentText(str(self.ob_art.bodega))#4
            self.ui.cmbox_distribuidor.setCurrentText(str(self.ob_art.distribuidor))#5
            self.ui.cmb_estado.setCurrentText(str(self.ob_art.estado))#6
            
       except pyodbc.Error as e:
           print("Error en datos "+ str(e))
           
    def establecerModoPantalla(self,oButton:QtWidgets.QPushButton):
        
        if oButton.text() == "Editar":
            pos = self.ui.tbl_lista_articulos_regis.selectedItems()
            if not pos:
                msg = QtWidgets.QMessageBox(self)
                msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                msg.setWindowTitle("Modificar registro")
                msg.setText("Seleccione un articulo.")
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.exec()
                return
            self.modoPantalla = 'M'
            self.ui.btn_editar.setEnabled(True)
            self.ui.btn_agregar_tabla.setEnabled(True)
            self.habilitar_controles(True)
            self.ui.txt_consecutivo.setEnabled(False)
            self.ui.txt_nombre_art.setEnabled(False)
            self.ui.txt_consecutivo.setFocus()
            return
        
    
    def metodo_cargar_datos_en_controles(self):
        try:
            pos = self.ui.tbl_lista_articulos_regis.selectedItems()
            fila = pos[0].row()
            id_fila = self.ui.tbl_lista_articulos_regis.item(fila,0).text()
            rs = buscar_articulo(id_fila)
            if rs != None:               
                self.ob_art= Articulo()
                self.ob_art.descripcion = str(rs[1])
                self.ob_art.codigo= str(rs[2])
                self.ob_art.cantidad = str(rs[3])
            #    self.ob_art.cantidad = str(rs[4])
        #       self.o_registro.fecha = str(rs[4])
                self.ob_art.bodega = str(rs[5])
                self.ob_art.distribuidor = str(rs[6])
                self.ob_art.estado = str(rs[7])
                self.metodo_para_llenar_controles()
        except pyodbc.Error as e:
            print("error de conexion "+str(e))  
    
    def habilitar_controles(self, sehabilita):
    
        self.ui.txt_nombre_art.setEnabled(sehabilita)
        self.ui.cmbox_bodegas.setEnabled(sehabilita)
        self.ui.cmbox_distribuidor.setEnabled(sehabilita)
        self.ui.txt_codigo_art.setEnabled(sehabilita)
        self.ui.cmb_estado.setEnabled(sehabilita)
        self.ui.txt_consecutivo.setEnabled(sehabilita)
       # self.ui.spBox_cantidad.setEnabled(sehabilita)
        
    
    def metodo_editar_items_de_pantall(self):
         if  self.modoPantalla == 'M':
                msgBox = QtWidgets.QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msgBox.setText("Desea modificar al Articulo {}".format(self.ui.txt_consecutivo.text()))
                msgBox.setWindowTitle("Confirmar Modificar Articulo")
                msgBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)                
                returnValue = msgBox.exec()
                if returnValue == QtWidgets.QMessageBox.StandardButton.Yes:                         
                    self.ob_art = Articulo()#       
                    self.ob_art.descripcion = self.ui.txt_nombre_art.text()#1
                    self.ob_art.codigo = (self.ui.txt_codigo_art.text())#2
                    self.ob_art.cantidad = (self.ui.spBox_cantidad.value())#3
                   # self.ob_art.costo = (self.ui.txt_tx.text())
          #          self.ob_art.fecha = (self.ui.dateEdit.text())
                    estado = self.ui.cmb_estado.currentIndex()#4
                    self.ob_art.estado = estado
                    distribuidor = self.ui.cmbox_distribuidor.currentIndex()#5
                    self.ob_art.distribuidor = distribuidor
                    bodega = self.ui.cmbox_bodegas.currentIndex()#6   
                    self.ob_art.bodega = bodega 
                    self.ob_art.consecutivo = self.ui.txt_consecutivo.text()#7
                    actualizar_articulos_en_pedido(self.ob_art)
                    self.ui.btn_editar.setEnabled(True)
                    self.habilitar_controles(False)
                    self.limpiar_bandejas_entrada()
    
    def obtener_lista_distribuidores_a_cmb(self):
        #def obtener_nombre_dist():
        try:
            self.conn = pyodbc.connect(con_string)# para conectarme a mi base 
            print("Conexion A BD")
            self.cur = self.conn.cursor()
            self.cur.execute('''SELECT Distribuidor FROM distribuidor ''')
            data = self.cur.fetchall()
            for category in data:
               self.ui.cmbox_distribuidor.addItem(category[0])
        except pyodbc.Error as e:
            print("Error de Conexion "+ str(e) ) 

    def control_articulos_ingresados(self):
 
        global consecutivo_registro
        consecutivo_registro = consecutivo_registro + 1
        numero_registro =str(consecutivo_registro).rjust(4,'0')
        self.ob_art = Articulo()
        self.ob_art.consecutivo = formato_registro.format(numero_registro)
        self.ui.txt_consecutivo.setText(" "+ self.ob_art.consecutivo)
        self.ob_art.consecutivo = self.ui.txt_consecutivo.text()
        self.ob_art.descripcion = self.ui.txt_nombre_art.text()
        self.ob_art.codigo = str(self.ui.txt_codigo_art.text())
        self.ob_art.cantidad = str(self.ui.spBox_cantidad.value())
        self.ob_art.fecha = str(self.ui.dateEdit.text())
        self.ob_art.bodega = str(self.ui.cmbox_bodegas.currentText())
        self.ob_art.distribuidor = str(self.ui.cmbox_distribuidor.currentText())
        estado_registro = self.ui.cmb_estado.currentIndex()
        self.ob_art.estado = 'ENTRADA' if estado_registro == 0 else 'SALIDA'
        
        ingresar_articulos(self.ob_art)
        itemView = ("\nRegistro Numero: "+self.ob_art.consecutivo+
                    "\nDescripcion: "+self.ob_art.descripcion+
                    "\nCodigo: "+self.ob_art.codigo+
                    "\nCantidades: "+self.ob_art.cantidad+
                    "\nEstado: "+self.ob_art.estado+
                    "\nFecha Ingreso: "+self.ob_art.fecha+
                    "\nBodega: "+self.ob_art.bodega+
                    "\nDistribuidor: "+self.ob_art.distribuidor)
        item = QtGui.QStandardItem(itemView)
       # item = QtWidgets.QTreeWidgetItem(itemView)
        self.modelolista.appendRow(item)
        self.metodo_imprimir_formato_txt()
        self.limpiar_bandejas_entrada()# metodo para que me permita añadir un atributo nuevo
        
    def metodo_imprimir_formato_txt(self):  
        consecutivo_registro = self.ui.txt_consecutivo.text()
        descripcion = self.ui.txt_nombre_art.text()
        codigo = self.ui.txt_codigo_art.text()
        cantidad = str(self.ui.spBox_cantidad.value())
        bodega = self.ui.cmbox_bodegas.currentText()
        distribuidor = self.ui.cmbox_distribuidor.currentText()
        estado = self.ui.cmb_estado.currentText()
        fecha = str(self.ui.dateEdit.text()) 
       # i = 0
        file = open(os.path.join(self.ui_path,"IngresosNuevos.txt"), "a")
        file.write("\n---------- NUEVOS REGISTROS EN SISTEMA ----------")
       
        file.write("\nCONSECUTIVO DE NUEVOS REGISTROS: "+consecutivo_registro+
                   "\nDescripcion: "+descripcion+"\nCodigo: "+codigo+"\nCantidad: "
                   +cantidad+"\nFecha "+fecha+
            "\nDistribuidor: "+distribuidor+"\n"+ "\nBodega: "+bodega+
            "\nEstado: "+estado)
        file.write("\n")
       # i +=1
        file.close()   
        
        #este medodo me permetira abrir el lugar donde se encuentran mis entradas de producto, con su respectivo proveedor
        
    def abrir_ventana_reporte_OnClicked(self):
        try:
            archivo = open(os.path.join(self.ui_path,"IngresosNuevos.txt"),'r')  
            texto = archivo.read()      
            self.ui.textEdit_reportes.setPlainText(texto)
            archivo.close()
            
        except:
            print("No se encontro")
      
        
    def obtener_lista_bodegas_a_cmb(self):
        try:
            self.conn = pyodbc.connect(con_string)# para conectarme a mi base 
            print("Conexion A BD")
            self.cur = self.conn.cursor()
            self.cur.execute('''SELECT nombre FROM bodega ''')
            data = self.cur.fetchall()
            for category in data:
               self.ui.cmbox_bodegas.addItem(category[0])
        except pyodbc.Error as e:
            print(" Error al llamar bodega "+ str(e))       
        
    def encabezados_de_mi_tabla_lista_articulos_regis(self):
        encabezados_columnas = ("ID", "Descripcion","Codigo","Costo","Cantidad","Fecha","Bodega","Distribuidor","Estado")
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
            distribuidor =QtWidgets.QTableWidgetItem(str(items.distribuidor))
            estado = QtWidgets.QTableWidgetItem(str(items.estado))
            
            self.ui.tbl_lista_articulos_regis.setItem(self.numFila,0,descripcion) 
            self.ui.tbl_lista_articulos_regis.setItem(self.numFila,1,codigo)
            self.ui.tbl_lista_articulos_regis.setItem(self.numFila,2,costo)
            self.ui.tbl_lista_articulos_regis.setItem(self.numFila,3,cantidad)
            self.ui.tbl_lista_articulos_regis.setItem(self.numFila,4,fecha)
            self.ui.tbl_lista_articulos_regis.setItem(self.numFila,5,bodega)
            self.ui.tbl_lista_articulos_regis.setItem(self.numFila,6,distribuidor)
            self.ui.tbl_lista_articulos_regis.setItem(self.numFila,7,estado) 

            self.numFila +=1 # para sumar mas filas
        
    def limpiar_bandejas_entrada(self):
        self.ui.txt_codigo_art.clear()
        self.ui.txt_nombre_art.clear()
        self.ui.spBox_cantidad.setValue(0)
               