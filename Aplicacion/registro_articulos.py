# esta clase se encargara de guardar mis articulos en una especie de registro
# importando los metodos desde mi carpeta Datos, concernientes a la clase Articulo donde se almacena
# toda la informacion respecto a como se podria ingresar un articulo.

import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from UI.uiRegistro import Ui_Registro_Ui  # para importar los objetos creados en mi QT y manipularlos
from Datos.claseArticulo import Registro_articulo # con esto puedo manipular los objetos creado en mi clase articulo

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
        self.modelo_mortero = QtGui.QStandardItemModel()
        self.ui.listView_bodeg_Morteros.setModel(self.modelo_mortero)
        
        
         
        reg_ex = QtCore.QRegularExpression("^[0-9]*(\.[0-9]{1,2})?$")# con esto permito que solo sean numeros, no texto
        input_validator = QtGui.QRegularExpressionValidator(reg_ex, self.ui.txt_costo_articulo)# con esto lo que hago es seleccionar que va en numeros no txt
        self.ui.txt_costo_articulo.setValidator(input_validator)
        reg_ex_two = QtCore.QRegularExpression("^[0-9]*(\.[0-9]{1,2})?$")
        input_validator_two = QtGui.QRegularExpressionValidator(reg_ex_two, self.ui.txt_cantidad_articulo)
        self.ui.txt_cantidad_articulo.setValidator(input_validator_two)
        
        
        #self.ui.cbx_bodega_N.mouseDoubleClickEvent.c
        
        
        
    def inicializar_controladores(self):# con esto inicializo my fecha en py pantalla window
        self.ui.date_fecha_articulo.setDate(QtCore.QDate.currentDate())
    
    def btnAgregar_Al_darle_click_en_Registro_Articulo(self):
        self.operacion_registro = Registro_articulo()# con esto instancio mi objeto y puedo usar los atributos
        # que se encuentran en mi clase "Registro_articulo" guardados
        self.operacion_registro.nombre_articulo = self.ui.txt_nombre_articulo.text()# para el nombre
        self.operacion_registro.codigo_articulo = self.ui.txt_codigo_articulo.text()# para el codigo
        self.operacion_registro.cantidad_articulo = float(self.ui.txt_cantidad_articulo.text())# para la cantidad
        self.operacion_registro.costo_articulo = float(self.ui.txt_costo_articulo.text())# para el costo
        #self.operacion_registro.añadir_articulo_a = self.ui.cbx_bodega_N.currentIndex()
        añadir_a = self.ui.cbx_bodega_N.currentIndex()
        self.operacion_registro.añadir_articulo_a = 'A' if añadir_a == 0 else 'I'
       # con esto tentativo
        #self.operacion_registro.añadir_articulo_a = "1" if añadir_a == self.modelolista else self.modelo_mortero
      
        #selecciono alguno de mis combo box
        itemView = (self.operacion_registro.nombre_articulo+# con esto me permite crear una variable
                    "  "+self.operacion_registro.codigo_articulo+# que me contendra todo lo perteneciente a mi clase
                    "  "+ # registro, y se imprimira en mi listview, sea de maderas o morteros
                    str(self.operacion_registro.costo_articulo)+"  "
                    +str(self.operacion_registro.cantidad_articulo))#" "+
                   # str(self.ui.date_fecha_articulo.setCalendar(self,calendar: Qcalendar)))
        item = QtGui.QStandardItem(itemView)
       # item_two = QtGui.QStandardItem(itemView)
      #  self.modelo_mortero.appendRow(item_two)   
        self.modelolista.appendRow(item)
        #elf.modelo_mortero.appendRow(item)
