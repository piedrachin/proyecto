# esta clase se encargara de guardar mis articulos en una especie de registro
# importando los metodos desde mi carpeta Datos, concernientes a la clase Articulo donde se almacena
# toda la informacion respecto a como se podria ingresar un articulo.

import sys
from Aplicacion.clasePersistencia import *
from UI.uiReg_distribuidor import Ui_ventana_distribuidor
from UI.uiControl_Inventario import Ui_V_Registro_Inventario
from Datos.claseBodega import *
from Datos.claseDistribuidor import *
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QComboBox
from UI.uiCrear_bodega import Ui_Registro_bodega
from UI.uiRegistro import Ui_Registro_Ui  # para importar los objetos creados en mi QT y manipularlos
from Datos.claseArticulo import Registro_articulo # con esto puedo manipular los objetos creado en mi clase articulo
formato_codigo = "CP#{0}"# estos atributos me ayudaran a dar formato a mis codigos
codigo_consecutivo = 1 # para que los de aleaotoriamente
lista_distribuidor = []


#formato_codigo = "PP#{0}"
#constante_codigo = 1

class Frm_Registro_Articulo(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Registro_Ui() #La propieda ui contiene la instancia de la interfaz grafica que dibujamos
        self.ui.setupUi(self) #Esta linea dibuja la interfaz grafica
        self.operacion_registro = None # esto me permitira manipular mi clase Articulo, al instanciar
        self.inicializar_controladores()
        self.ui.btn_registrar_articulo.clicked.connect(self.btnAgregar_Al_darle_click_en_Registro_Articulo)
        
      
        # con esto puedo enviar mi modelo registro a un list view previamente creado
        self.modelolista = QtGui.QStandardItemModel() # con esto lo nombro
        self.ui.list_bodega_Madera.setModel(self.modelolista)# aca indico donde quiero que se vea
       # self.modelo_mortero = QtGui.QStandardItemModel()
        #self.ui.listView_bodeg_Morteros.setModel(self.modelo_mortero)
        
        
         
        reg_ex = QtCore.QRegularExpression("^[0-9]*(\.[0-9]{1,2})?$")# con esto permito que solo sean numeros, no texto
        input_validator = QtGui.QRegularExpressionValidator(reg_ex, self.ui.txt_costo_articulo)# con esto lo que hago es seleccionar que va en numeros no txt
        self.ui.txt_costo_articulo.setValidator(input_validator)
        reg_ex_two = QtCore.QRegularExpression("^[0-9]*(\.[0-9]{1,2})?$")
        input_validator_two = QtGui.QRegularExpressionValidator(reg_ex_two, self.ui.txt_cantidad_articulo)
        self.ui.txt_cantidad_articulo.setValidator(input_validator_two)
     #   self.ui.txt_codigo_articulo.setText(formato_codigo)
        self.ui.txt_codigo_articulo.setReadOnly(True)
     #  self.ui.txt_codigo_articulo.setT
        
       # self.ui.cbx_bodega1.stateChanged.connect(self.allow)
       # self.ui.cbx_bodega1.stateChanged.connect(self.btnAgregar_Al_darle_click_en_Registro_Articulo)
        
        
        #lista_codigo.append[self.ui.txt_codigo_articulo]
       # self.crear_bodega = Crear_Bodegas()
        #
        '''NOTA: >>> este codigo me permite agregar a mi comboBox, nuevos items
           # self.ui.btn_add_to_cbx.clicked.connect(self.add_new_item_to_cmb)        
    #def add_new_item_to_cmb(self):   
     #   new_item = self.ui.txt_nuevo_cbx.text()
      #  self.ui.comboBox_list.addItem(new_item)
        '''
    def inicializar_controladores(self):# con esto inicializo my fecha en py pantalla window
        self.ui.date_fecha_articulo.setDate(QtCore.QDate.currentDate())
    
    def btnAgregar_Al_darle_click_en_Registro_Articulo(self):

        global codigo_consecutivo # esto me ayuda a darle un formato a mi codigo producto 
        codigo_consecutivo = codigo_consecutivo + 1
        num_codigo = str(codigo_consecutivo).rjust(3,'0')
        
        self.operacion_registro = Registro_articulo()# con esto instancio mi objeto y puedo usar los atributos
        # que se encuentran en mi clase "Registro_articulo" guardados
        self.operacion_registro.codigo_articulo = formato_codigo.format(num_codigo)# con esto le doy forma 
        self.ui.txt_codigo_articulo.setText(""+ self.operacion_registro.codigo_articulo)#-->>
        
        self.operacion_registro.nombre_articulo = self.ui.txt_nombre_articulo.text()# para el nombre
       # self.crear_bodega = Crear_Bodegas()

      
        #nueva_bodega = self.crear_bodega.ui.txt_nombre_bodega.text()
        #self.ui.cbx_bodega_N.addItem(nueva_bodega) 
      #  self.crear_bodega.ui.cmb_bodegas_creadas = self.ui.cbx_bodega_N.currentIndex()

        self.operacion_registro.cantidad_articulo = float(self.ui.txt_cantidad_articulo.text())# para la cantidad
        self.operacion_registro.costo_articulo = float(self.ui.txt_costo_articulo.text())# para el costo 
        #selecciono alguno de mis combo box
        itemView = (self.operacion_registro.nombre_articulo  # con esto me permite crear una variable
                    +" -- "+self.operacion_registro.codigo_articulo+  # que me contendra todo lo perteneciente a mi clase
                    " -- "+ # registro, y se imprimira en mi listview, sea de maderas o morteros
                    str(self.operacion_registro.costo_articulo)+"  "
                    +str(self.operacion_registro.cantidad_articulo)) #+" "
                   # +self.ui.date_fecha_articulo.setDate(QtCore.QDate.currentDate()))
                    
        item = QtGui.QStandardItem(itemView)
      #  item_two = QtGui.QStandardItem(itemView)
    
       # self.modelo_mortero.appendRow(item_two)   
        self.modelolista.appendRow(item)
        #elf.modelo_mortero.appendRow(item)
       
        Persistencia.agregar_articulo(self.operacion_registro)
     
    
class Control_Inventario(QtWidgets.QDialog):
    
   def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_V_Registro_Inventario() # metodo para manejar mi inventario
        self.ui.setupUi(self)
        self.ui.btn_imprimirir_inventario.clicked.connect(self.lista_inventario_onClick)

   def lista_inventario_onClick(self):
        self.ui.tabla_inventario.setRowCount(0)
        
        num_filas = self.ui.tabla_inventario.rowCount()
        
        # con esto se supone que llenare mi tabla... 
        # esta tentativo
        for cada_articulo in Persistencia.control_articulo():
            self.ui.tabla_inventario.insertRow(num_filas)
            Nombre = QtWidgets.QTableWidgetItem(cada_articulo.nombre_articulo)
            Codigo = QtWidgets.QTableWidgetItem(cada_articulo.codigo_articulo)
            Cantidad = QtWidgets.QTableWidgetItem(str(cada_articulo.cantidad_articulo))
            Costo = QtWidgets.QTableWidgetItem(str(cada_articulo.costo_articulo))
            Fecha = QtWidgets.QTableWidgetItem(cada_articulo.date_fecha_articulo)
            
            self.ui.tabla_inventario.setItem(num_filas,0,Nombre)
            self.ui.tabla_inventario.setItem(num_filas,1,Codigo)
            self.ui.tabla_inventario.setItem(num_filas,2,Cantidad)
            self.ui.tabla_inventario.setItem(num_filas,3,Costo)
            self.ui.tabla_inventario.setItem(num_filas,4,Fecha)
            
            num_filas += 1


class Crear_Bodegas(QtWidgets.QDialog): # contendra lo perteneciente a las bodegas
  
  
        def __init__(self) -> None:
             super().__init__()
             self.ui = Ui_Registro_bodega() # metodo para manejar mi inventario
             self.ui.setupUi(self)
             self.ui.btn_crear_bodega.clicked.connect(self.onClick_crear_bodega)
             self.crear_bodega = None
            # self.comboBox = Registro_articulo(QComboBox)
             self.modelolista = QtGui.QStandardItemModel() # con esto lo nombro
             self.ui.listView_bodegas.setModel(self.modelolista)
            
             self.re_comboBox = Frm_Registro_Articulo()# re_comboBox = registrar en comboBox
             
             
        def onClick_crear_bodega(self):

                self.crear_bodega = Bodega()# instancio para usar los metodos de mi clase objeto
                self.crear_bodega.nombre_bodega = self.ui.txt_nombre_bodega.text()
                nueva_bodega = self.ui.txt_nombre_bodega.text()
               # self.re_comboBox.ui.cbx_bodega_N = self.ui.cmb_bodegas_creadas
                self.ui.cmb_bodegas_creadas.addItem(nueva_bodega)
              
                #self.re_comboBox.addItem(nueva_bodega)
                itemView = (self.crear_bodega.nombre_bodega)
                item = QtGui.QStandardItem(itemView)
                self.modelolista.appendRow(item)
                           

'''NOTA: >>> este codigo me permite agregar a mi comboBox, nuevos items
           # self.ui.btn_add_to_cbx.clicked.connect(self.add_new_item_to_cmb)        
    #def add_new_item_to_cmb(self):   
     #   new_item = self.ui.txt_nuevo_cbx.text()
      #  self.ui.comboBox_list.addItem(new_item)'''

class Crear_Distribuidor(QtWidgets.QDialog):
  def __init__(self) -> None:
       super().__init__()
       self.ui = Ui_ventana_distribuidor()
       self.ui.setupUi(self)
       self.reg_distribuidor = None
       self.distribuidores = []
       #self.ui.btn_crear_distribuidor(command =lambda:my_insert())
       self.ui.btn_crear_distribuidor.clicked.connect(self.onClick_crea_distribuidor)
  
    
    
  def onClick_crea_distribuidor(self):
    self.reg_distribuidor = Distribuidor()
    self.reg_distribuidor.ced_juridica_distribuidor = float(self.ui.txt_ced_juridica_dist.text())
    self.reg_distribuidor.nombre_distribuidor = self.ui.txt_nombre_dist.text()
    self.reg_distribuidor.telefono_distribuidor = float(self.ui.txt_telefono_dist.text())
   # self.ui.cmb_distribuidores.addItem(" ") = self.reg_distribuidor.nombre_distribuidor.text()
    #self.ui.cmb_distribuidores.addItem[str](self.reg_distribuidor.nombre_distribuidor.text())
 
  class Articulo:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Bodega:
    def __init__(self):
        self.inventario = []

    def agregar_articulo(self, articulo):
        self.inventario.append(articulo)
        print("Artículo agregado a la bodega.")

    def mostrar_inventario(self):
        print("Inventario actual:")
        for articulo in self.inventario:
            print(f"{articulo.nombre} - Cantidad: {articulo.cantidad} - Precio: {articulo.precio}")

# Creación de los artículos
articulo_a = Articulo("Laptop", 1500, 10)
articulo_b = Articulo("Celular", 800, 20)

# Preguntar al usuario qué artículo desea agregar a la bodega
opcion = input("¿Qué artículo desea agregar a la bodega? (a/b): ")

# Crear la bodega
bodega = Bodega()

# Agregar el artículo elegido a la bodega
if opcion == "a":
    bodega.agregar_articulo(articulo_a)
elif opcion == "b":
    bodega.agregar_articulo(articulo_b)
else:
    print("Opción no válida.")

# Mostrar el inventario actual de la bodega
bodega.mostrar_inventario()
