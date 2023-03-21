import sys
from  PyQt6 import QtCore,QtGui,QtWidgets
#from Aplicacion.registro_articulos import Frm_Registro_Articulo
from Aplicacion.ventanaMain import Ventana_Main # con esto importo mi ventana principal.




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ventana_Main()
    window.show()
    sys.exit(app.exec())
