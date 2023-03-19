import sys
from  PyQt6 import QtCore,QtGui,QtWidgets



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Frm_Registro_Articulo()
    window.show()
    sys.exit(app.exec())
