import sys
from  PyQt6 import QtCore,QtGui,QtWidgets
from Aplicacion.registro_articulos import Frm_Registro_Articulo





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Frm_Registro_Articulo()
    window.show()
    sys.exit(app.exec())
