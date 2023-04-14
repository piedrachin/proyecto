import sys
from  PyQt6 import QtCore,QtGui,QtWidgets

#from Datos.registro import Registro
from Datos.registro import Registro

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Registro()
    window.show()
    sys.exit(app.exec())
