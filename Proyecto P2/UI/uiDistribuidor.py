# Form implementation generated from reading ui file 'distribuidor.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Distribuidor(object):
    def setupUi(self, Distribuidor):
        Distribuidor.setObjectName("Distribuidor")
        Distribuidor.resize(603, 345)
        self.btn_crear_dist = QtWidgets.QPushButton(parent=Distribuidor)
        self.btn_crear_dist.setGeometry(QtCore.QRect(10, 190, 75, 23))
        self.btn_crear_dist.setObjectName("btn_crear_dist")
        self.label = QtWidgets.QLabel(parent=Distribuidor)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Distribuidor)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Distribuidor)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_3.setObjectName("label_3")
        self.txt_nombre_emp = QtWidgets.QLineEdit(parent=Distribuidor)
        self.txt_nombre_emp.setGeometry(QtCore.QRect(120, 10, 221, 20))
        self.txt_nombre_emp.setObjectName("txt_nombre_emp")
        self.txt_ced_juri_emp = QtWidgets.QLineEdit(parent=Distribuidor)
        self.txt_ced_juri_emp.setGeometry(QtCore.QRect(120, 40, 221, 20))
        self.txt_ced_juri_emp.setObjectName("txt_ced_juri_emp")
        self.txt_telefono_emp = QtWidgets.QLineEdit(parent=Distribuidor)
        self.txt_telefono_emp.setGeometry(QtCore.QRect(120, 70, 221, 20))
        self.txt_telefono_emp.setObjectName("txt_telefono_emp")
        self.tbl_distribuidores = QtWidgets.QTableWidget(parent=Distribuidor)
        self.tbl_distribuidores.setGeometry(QtCore.QRect(120, 140, 471, 191))
        self.tbl_distribuidores.setObjectName("tbl_distribuidores")
        self.tbl_distribuidores.setColumnCount(4)
        self.tbl_distribuidores.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_distribuidores.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_distribuidores.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_distribuidores.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_distribuidores.setHorizontalHeaderItem(3, item)
        self.dateEdit = QtWidgets.QDateEdit(parent=Distribuidor)
        self.dateEdit.setGeometry(QtCore.QRect(120, 100, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label_4 = QtWidgets.QLabel(parent=Distribuidor)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 47, 13))
        self.label_4.setObjectName("label_4")
        self.btn_refrescar = QtWidgets.QPushButton(parent=Distribuidor)
        self.btn_refrescar.setGeometry(QtCore.QRect(10, 240, 75, 23))
        self.btn_refrescar.setObjectName("btn_refrescar")

        self.retranslateUi(Distribuidor)
        QtCore.QMetaObject.connectSlotsByName(Distribuidor)

    def retranslateUi(self, Distribuidor):
        _translate = QtCore.QCoreApplication.translate
        Distribuidor.setWindowTitle(_translate("Distribuidor", "Form"))
        self.btn_crear_dist.setText(_translate("Distribuidor", "Crear"))
        self.label.setText(_translate("Distribuidor", "Nombre Empresa"))
        self.label_2.setText(_translate("Distribuidor", "Cedula Juridica"))
        self.label_3.setText(_translate("Distribuidor", "Telefono"))
        item = self.tbl_distribuidores.horizontalHeaderItem(0)
        item.setText(_translate("Distribuidor", "Nombre"))
        item = self.tbl_distribuidores.horizontalHeaderItem(1)
        item.setText(_translate("Distribuidor", "Cedula Juridica"))
        item = self.tbl_distribuidores.horizontalHeaderItem(2)
        item.setText(_translate("Distribuidor", "Telefono"))
        item = self.tbl_distribuidores.horizontalHeaderItem(3)
        item.setText(_translate("Distribuidor", "Fecha"))
        self.label_4.setText(_translate("Distribuidor", "Fecha"))
        self.btn_refrescar.setText(_translate("Distribuidor", "Refrescar"))
