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
from Datos.dataBase.basedatos import seleccionar_articulos, con_string, ingresar_articulos

class VentanaPedido(QtWidgets.QDialog):
    
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Registro()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowType.Window) # esto me permite que mi nueva ventana pueda ser manipulada,
        # sobre mi ventana padre.
        self.ob_art = None
        self.ui_path = os.path.dirname(os.path.abspath(__file__))
        self.lista_articulos_registrados_en_BD(seleccionar_articulos())
        self.encabezados_de_mi_tabla_lista_articulos_regis()
        self.ui.btn_refrescar_vent.clicked.connect(lambda:self.lista_articulos_registrados_en_BD(seleccionar_articulos()) )
        self.ui.btn_agregar_tabla.clicked.connect(self.control_articulos_ingresados)
        self.ui.btn_abrir_reporte.clicked.connect(self.abrir_ventana_reporte_OnClicked)
        self.obtener_lista_bodegas_a_cmb()
        self.obtener_lista_distribuidores_a_cmb()
        self.inicializar_controladores()
        self.modelolista = QtGui.QStandardItemModel()
        self.ui.tbl_lista_por_imp.setModel(self.modelolista)
       # self.ui.tbl_lista_por_imp.sele
       # self.ui.btn_abrir_reporte.clicked.connect(self.dsplegar_registros_de_ingresos_desde_txt)
        self.ui.tbl_lista_articulos_regis.setColumnWidth(0,0)
        self.ui.txt_consecutivo.setReadOnly(True)
        self.ui.textEdit_reportes.setReadOnly(True)
    def dsplegar_registros_de_ingresos_desde_txt(self):
        from .registrostxt import VentanaRegistrosDelTxt
        self.ventana_reportes = VentanaRegistrosDelTxt(self)
        self.ventana_reportes.show()
        
        
        
           
    def inicializar_controladores(self):# con esto inicializo my fecha en py pantalla window
        self.ui.dateEdit.setDate(QtCore.QDate.currentDate())   
    
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
        
        ingresar_articulos(self.ob_art)
        itemView = ("\nRegistro Numero: "+self.ob_art.consecutivo+
                    "\nDescripcion: "+self.ob_art.descripcion+
                    "\nCodigo: "+self.ob_art.codigo+
                    "\nCantidades: "+self.ob_art.cantidad+
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
        fecha = str(self.ui.dateEdit.text()) 
       # i = 0
        file = open(os.path.join(self.ui_path,"IngresosNuevos.txt"), "a")
        file.write("\n---------- NUEVOS INGRESOS AL SISTEMA ----------")
       
        file.write("\nCONSECUTIVO DE NUEVOS INGRESOS: "+consecutivo_registro+
                   "\nDescripcion: "+descripcion+"\nCodigo: "+codigo+"\nCantidad: "
                   +cantidad+"\nFecha "+fecha+
            "\nDistribuidor: "+distribuidor+"\n"+ "\nBodega: "+bodega)
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
        encabezados_columnas = ("ID", "Descripcion","Codigo","Costo","Cantidad","Fecha","Bodega","Distribuidor")
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
            
            self.ui.tbl_lista_articulos_regis.setItem(self.numFila,0,descripcion) 
            self.ui.tbl_lista_articulos_regis.setItem(self.numFila,1,codigo)
            self.ui.tbl_lista_articulos_regis.setItem(self.numFila,2,costo)
            self.ui.tbl_lista_articulos_regis.setItem(self.numFila,3,cantidad)
            self.ui.tbl_lista_articulos_regis.setItem(self.numFila,4,fecha)
            self.ui.tbl_lista_articulos_regis.setItem(self.numFila,5,bodega)
            self.ui.tbl_lista_articulos_regis.setItem(self.numFila,6,distribuidor) 

            self.numFila +=1 # para sumar mas filas
        
    def limpiar_bandejas_entrada(self):
        self.ui.txt_codigo_art.clear()
        self.ui.txt_nombre_art.clear()
        self.ui.spBox_cantidad.setValue(0)
               