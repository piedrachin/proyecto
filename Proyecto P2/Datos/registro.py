import pyodbc

import sys
from Datos.dataBase.basedatos import con_string
from PyQt6 import QtCore,QtWidgets,QtGui
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtCore import *
from UI.uiRegistro import Ui_Control
from Clases.claseArticulo import Articulo
from Clases.claseDistribuidor import Distribuidor
from Clases.claseBodega import Bodega
from PyQt6.QtWidgets import *
#from .registro import Articulo
from .permanencia import *
#from .mibasedatos import registrar_articulo_en_bd

from Datos.dataBase.basedatos import crear_bodega,ingresar_articulos,seleccionar_articulos,eliminarArticulo,con_string,actualizar_articulos, obtener_lista_bodegas,buscar_articulo

import datetime


#articulos_reg = []

class Registro(QtWidgets.QDialog):
    
    def __init__(self, parent = None, _id = None):
        super(Registro, self).__init__(parent)
        self.ui = Ui_Control()
        self.ui.setupUi(self)
        self.o_registro = None
        self.ob_bodega = None
        self.modo = 'M'
        self.ui.tbl_lista_bodegas.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.tbl_registro_articulos.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.habilitar_controles(False)
        self.encabezado_tabla_bodegas()
        self.ancho_de_columnas_en_tablas()
        self.inicializar_controladores()
        self.obtener_lista_bodegas_e_insertar_en_cmb()
      #  self.crear_tabla_bodegas()
        #self.iniciar_todos_los_botones_de_mi_vent_principal()
       # self.llenar_tabla_bodegas_en_Bd(obtener_lista_bodegas())
        self.llenar_tabla_bodegas_en_Bd(seleccionar_articulos())
       # self.llenar_tabla_con_bd(seleccionar_articulos())
        self.ui.btn_editar_articull.clicked.connect(lambda: self.establecerModoPantalla(self.ui.btn_editar_articull))   
        self.ui.btn_nuevo_in.clicked.connect(lambda: self.establecerModoPantalla(self.ui.btn_nuevo_in))
       # self.ui.btn_editar_articull.clicked.connect(self.metodo_actualizar_articulo)
        self.ui.btn_agregar.clicked.connect(self.registrar_articulo)   
        self.ui.btn_vent_pedido.clicked.connect(self.ventana_control_pedidos)
        self.ui.btn_distribuidor.clicked.connect(self.ventana_perfil_distribuidor)
        #self.ui.btn_crear_bodega.clicked.connect(self.ventana_crear_bodega)
        self.ui.btn_refrescar.clicked.connect(lambda: self.llenar_tabla_con_bd(seleccionar_articulos()))
        self.ui.btn_eliminar_tabla.clicked.connect(self.eliminar_articulos)
        self.ui.btn_crear_bodega_2.clicked.connect(self.crear_bodega_en_CMB)
        reg_ex = QtCore.QRegularExpression("^[0-9]*(\.[0-9]{1,2})?$") # esto es para que solo me permita numeros
        input_validator = QtGui.QRegularExpressionValidator(reg_ex, self.ui.txt_costo)# y no se introduzcan letras
        self.ui.txt_costo.setValidator(input_validator)
       # self.crear_tabla_bodegas()
        self.ui.tbl_registro_articulos.clicked.connect(self.metodo_cargar_datos_en_controles)
        
        self.ui.btn_actualizar_bod.clicked.connect(lambda:self.llenar_tabla_bodegas_en_Bd(obtener_lista_bodegas()))
        # este metodo me permite obtener las bodegas creadas de mi combobox

        # este medodo me permite obtener, todas aquellas bodegas creadas en mi ventana bodega 
        # o bien desde la principal, y actualizarlos en mi ventana de inicio
   # este metodo se encarga de actualizarme el combobox, cuando creo una nueva bodega
    def obtener_lista_bodegas_e_insertar_en_cmb(self):
        try:
            self.conn = pyodbc.connect(con_string)# para conectarme a mi base 
            print("Conexion A BD")
            self.cur = self.conn.cursor()
            self.cur.execute('''SELECT nombre FROM bodega ''')
            data = self.cur.fetchall()
            for category in data:
               self.ui.cmb_registro.addItem(category[0])
        except pyodbc.Error as e:
            print(" Error al llamar bodega "+ str(e))     
                            
   # se creo con el fin de ajustar las columnas de mis tablas..
    def ancho_de_columnas_en_tablas(self):
        self.ui.tbl_registro_articulos.setColumnWidth(0, 0)
        self.ui.tbl_registro_articulos.setColumnWidth(1,230)
       # self.ui.tbl_bodega.setColumnWidth(1,230)
       
    # este metodo es para crear las bodegas y agregarlas a mi comboBox o bien a mi tabla en BD        
    def crear_bodega_en_CMB(self):
        self.nombre_bodega = Bodega()
        self.nombre_bodega.nombre = self.ui.txt_nombrebodega.text()
        self.ui.cmb_registro.addItem(self.nombre_bodega.nombre)
        crear_bodega(self.nombre_bodega)
        Persistencia.crear_bodega(self.nombre_bodega)
        self.ui.txt_nombrebodega.clear()

        # metodo para eliminar articulos que estan dentro de mi tabla, que despliega los articulos existentes
        # y los 
    def establecerModoPantalla(self,oButton:QtWidgets.QPushButton):
        
        if oButton.text() == "Nuevo":
            self.modoPantalla = 'N'           
            self.ui.btn_editar_articull.setEnabled(True)
            self.ui.btn_eliminar_tabla.setEnabled(True)
            self.ui.btn_nuevo_in.setEnabled(True)
            self.ui.btn_agregar.setEnabled(True)            
            self.inicializar_controladores()
            self.habilitar_controles(True)
            self.ui.lineEdit.setFocus() 
            return
        
               
        if oButton.text() == "Editar":
            pos = self.ui.tbl_registro_articulos.selectedItems()
            if not pos:
                msg = QtWidgets.QMessageBox(self)
                msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
                msg.setWindowTitle("Modificar registro")
                msg.setText("Seleccione un articulo.")
                msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                msg.exec()
                return
            self.modoPantalla = 'M'
            self.ui.btn_nuevo_in.setEnabled(True)
            self.ui.btn_editar_articull.setEnabled(True)
            self.ui.btn_eliminar_tabla.setEnabled(True)
            self.ui.btn_agregar.setEnabled(True)
            self.habilitar_controles(True)
            self.ui.lineEdit.setEnabled(False)
            self.ui.txt_nombre.setEnabled(False)
            self.ui.lineEdit.setFocus()
            return
        
    
    def metodo_para_llenar_controles(self):
        
       try:
            self.ui.txt_codigo.setText(str(self.o_registro.codigo))
            self.ui.txt_costo.setText(str(self.o_registro.costo))
            self.ui.txt_nombre.setText(str(self.o_registro.descripcion))
            self.ui.spBox_cantidad.setValue(int(self.o_registro.cantidad))
          #  self.ui.dateEdit.setCurrentSection(str(self.o_registro.fecha))
            self.ui.cmb_registro.setCurrentText(str(self.o_registro.bodega))
            
       except pyodbc.Error as e:
           print("Error en datos "+ str(e))

    def metodo_cargar_datos_en_controles(self):
        try:
            pos = self.ui.tbl_registro_articulos.selectedItems()
            fila = pos[0].row()
            id_fila = self.ui.tbl_registro_articulos.item(fila,0).text()
            rs = buscar_articulo(id_fila)
            if rs != None:               
                self.o_registro = Articulo()
                self.o_registro.descripcion = str(rs[1])
                self.o_registro.codigo= str(rs[2])
                self.o_registro.costo = str(rs[3])
                self.o_registro.cantidad = str(rs[4])
        #       self.o_registro.fecha = str(rs[4])
                self.o_registro.bodega = str(rs[6])
                self.metodo_para_llenar_controles()
        except pyodbc.Error as e:
            print("error de conexion "+str(e))
            
    def habilitar_controles(self, sehabilita):
        self.ui.txt_codigo.setEnabled(sehabilita)
        self.ui.txt_nombre.setEnabled(sehabilita)
        self.ui.cmb_registro.setEnabled(sehabilita)
        self.ui.txt_costo.setEnabled(sehabilita)
        self.ui.lineEdit.setEnabled(sehabilita)# este es mi consecutivo el lineEdit
    # este metodo me permitira actualizar mi inventario
    def metodo_actualizar_articulo(self):
        self.ui.tbl_registro_articulos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        if  self.modoPantalla == 'M':
                msgBox = QtWidgets.QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msgBox.setText("Desea modificar al Articulo {}".format(self.ui.lineEdit.text()))
                msgBox.setWindowTitle("Confirmar Modificar Articulo")
                msgBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)                
                returnValue = msgBox.exec()
                if returnValue == QtWidgets.QMessageBox.StandardButton.Yes:                         
                    self.o_registro = Articulo()#       
                    self.o_registro.descripcion = self.ui.txt_nombre.text()
                    self.o_registro.codigo = (self.ui.txt_codigo.text())
                    self.o_registro.cantidad = (self.ui.spBox_cantidad.value())
                    
                    #self.o_registro.costo = (self.ui.txt_costo.text())
         #   self.o_registro.fecha = (self.ui.dateEdit.text())
                    bodega = self.ui.cmb_registro.currentIndex()   
                    self.o_registro.bodega = bodega 
                    self.o_registro.consecutivo = self.ui.lineEdit.text()
                    actualizar_articulos(self.o_registro)
                    self.ui.btn_editar_articull.setEnabled(True)
                    self.ui.btn_eliminar_tabla.setEnabled(True)
          #  self.metodo_cargar_datos_en_controles() 
                    self.llenar_tabla_registro()   
                    self.habilitar_controles(False)
                    self.limpiar_entrada()
                    
      #  except pyodbc.Error as e:
       #     print("Error al actualizar, favor verifique..!!"+ str(e))
        
    def eliminar_articulos(self):
        # esto me permetira seleccionar una fila completa, sin poder editar, solo elimar todo.
        self.ui.tbl_registro_articulos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        selec_fila = self.ui.tbl_registro_articulos.selectedItems()
        
        if selec_fila:
            articulo_id = int(selec_fila[0].text())
            fila = selec_fila[0].row()
            if eliminarArticulo(articulo_id):
               self.ui.tbl_registro_articulos.removeRow(fila)
               
        
          
   # este metodo se hizo con el fin de tener un reporte o ma
   # manejo de txt de todo aquello que se registra.         
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
 # metodo para iniciar la fecha actual en mi pantalla
    def inicializar_controladores(self):# con esto inicializo my fecha en py pantalla window
        self.ui.dateEdit.setDate(QtCore.QDate.currentDate())
   
   # este metodo me permite ir a la ventana pedidos
    def ventana_control_pedidos(self):
        from .pedido import VentanaPedido
        self.ventana_pedido = VentanaPedido()
        self.ventana_pedido.show()
        # este metodo me permite ir a la ventana del distribuidor
    # este metodo me permite ir a la ventana donde creo mi distribuidor
    def ventana_perfil_distribuidor(self):
        from .distribuidor import DistribuidorVentana
        self.ventana_distribuidor = DistribuidorVentana(self)
        self.ventana_distribuidor.show()# con este metodo muestro mi ventana
    
     # este metodo me permite ir a la ventana de crear bodega
    
    # este metodo me permite ir a la ventana bodega y crear una nueva
    def ventana_crear_bodega(self):
        from .bodega import VentanaBodega # importo mi clase de bodega
        self.ventana_bodega = VentanaBodega(self)
        self.ventana_bodega.show()
      
      
      # este metodo me permite registrar o bien crear un articulo, que se vera en mi tabla    
  
   # este metodo me permite registrar mis articulos de bodega
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
       
        encabezados_columnas = ("Bodega","Descripcion","Codigo","Cantidad")
        self.ui.tbl_lista_bodegas.setColumnCount(len(encabezados_columnas))
        self.ui.tbl_lista_bodegas.setHorizontalHeaderLabels(encabezados_columnas)
        
    
    def llenar_tabla_bodegas_en_Bd(self, data):
        self.crear_tabla_bodegas()
        self.ui.tbl_lista_bodegas.setRowCount(len(data))
        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.ui.tbl_lista_bodegas.setItem(index_row, index_cell,QTableWidgetItem(str(cell))) 
                
    def crear_tabla_bodegas(self):# esta tabla me permitira obtener la bodega y su respectivo material y cantidad
        art_cread = seleccionar_articulos()
        self.ui.tbl_lista_bodegas.setRowCount(0)
        num_fila = self.ui.tbl_lista_bodegas.rowCount()    
        for item in art_cread:
       # for item in obtener_lista_bodegas():
            self.ui.tbl_lista_bodegas.insertRow(num_fila)
            bodega = QtWidgets.QTableWidgetItem(item.bodega)                                
            descripcion  = QtWidgets.QTableWidgetItem(str(item.descripcion))
            codigo = QtWidgets.QTableWidgetItem(str(item.codigo))
            cantidad = QtWidgets.QTableWidgetItem(str(item.cantidad))
            
            self.ui.tbl_lista_bodegas.setItem(num_fila,0,bodega)
            self.ui.tbl_lista_bodegas.setItem(num_fila,1,descripcion)
            self.ui.tbl_lista_bodegas.setItem(num_fila,2,codigo)
            self.ui.tbl_lista_bodegas.setItem(num_fila,3,cantidad)
              
            num_fila += 1 # para que me sume mas filas
      #  for item in Persistencia.obtener_registro():
            
    
            # este metodo me permite llenar mi tabla de articulos con base de datos
    def llenar_tabla_con_bd(self, data):        
         
        self.ui.tbl_registro_articulos.setRowCount(len(data))
        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.ui.tbl_registro_articulos.setItem(index_row, index_cell,QTableWidgetItem(str(cell)))
    
    def llenar_tabla_registro(self):
         
        datos = seleccionar_articulos()     
        num_fila = self.ui.tbl_registro_articulos.rowCount()
         
        for item in datos:
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
       
         # metodo que me limpia mis bandejas donde agrego los datos, para ingresar uno nuevo                            
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
            
            msg = QtWidgets.QMessageBox(text=" Dejaste Algun Espacio Vacio. "+
                                        "\nPor Favor Verificar.")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.StandardButton(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
        
           
                
            
        
        
        
   

   
   
   
   
   
   





