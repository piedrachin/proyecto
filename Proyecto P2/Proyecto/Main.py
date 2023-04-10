import sys
from Pantalla import *
#import TablaPagos as Tbl
from Datos import Persona
import numpy_financial as npf

#import tabulate as tab
#numpy_financial = 0

class FrmUsuario(QtWidgets.QDialog):
    def __init__(self):        
        super().__init__()
        self.ui = Ui_PantallaMenu()
        self.ui.setupUi(self)
        self.Tabla = []
        self.ui.btnFinalizar_2.clicked.connect(self.iniciarMetodos)
        self.ui.btnFinalizar.clicked.connect(self.terminar)
        self.objPersona = None

    def terminar(self):
        app.quit()

    def iniciarMetodos(self):
        self.Tabla = self.generarTablaPagos()
        self.dibujaTabla()
        self.finalizar()
        self.registrarPersona()
        
    
    def Tbl2(self):
         monto = self.ui.txtMonto.text()

    def finalizar(self): #Boton para finalizar impresion
        
        monto = self.ui.txtMonto.text()
        self.fila = self.ui.tblBitacora2.rowCount()
        nombre = self.ui.txtNombre.text()
        cedula = self.ui.txtCedula.text()
        genero = self.ui.cmbGenero.currentText()
        sector = self.ui.cmbSector.currentText()
        Credito = self.ui.cmbTipoCredito.currentText()
        plazo = self.ui.cmbPlazo.currentText()
        #tasa = self.ui.cmbTaza.currentText()
        if (Credito == "Consumo"):
            tasa = "20%"
        else:
            tasa = "10%"

        archivo = open("Imprecion.txt", "a")
        archivo.write( "-----------------DATOS USUARIO-----------------" +"\r")
        archivo.write("Cedula: "+ cedula +"\r" +"Nombre: "+ nombre +"\r" +"Genero: "+ genero +"\r" +"Sector: "+ sector +"\r" )
        archivo = open("Imprecion.txt", "a")
        archivo.write("-----------------DATOS CREDITO-----------------" +"\r")
        archivo.write("Credito: "+Credito +"\r" + "Monto Formalizacion: "+ monto +"\r" +"Tasa: "+ tasa +"\r")  
        archivo.write("Cantidad de plasos: "+ plazo+"\r")

        archivo.close()

    def generarTablaPagos(self):
        Credito = self.ui.cmbTipoCredito.currentText()
        plazo = int(self.ui.cmbPlazo.currentText())
        if (Credito == "Consumo"):
            tasa = (0.20/plazo)
        else:
            tasa = (0.10/plazo)
        capital = int(self.ui.txtMonto.text())
        
        cuota = round(npf.pmt(tasa, plazo, -capital, 0), 0)
        datos = []
        saldo = capital
        Credito = self.ui.cmbTipoCredito.currentText()
        
        for i in range(1, plazo+1):
            pago_capital = npf.ppmt(tasa, i, plazo, -capital, 0)
            pago_int = cuota - pago_capital
            saldo -= pago_capital
            linea = [i, format(cuota, '0,.0f'), format(pago_capital, '0,.0f'), format(pago_int, '0,.0f'), format(saldo, '0,.0f')]
            datos.append(linea)
        return datos

    def dibujaTabla(self):
        i = 0
        for pago in self.Tabla:
            self.ui.tblBitacora.insertRow(i)
            #print(pago[0])
            periodo = QtWidgets.QTableWidgetItem(str(i))
            cuota = QtWidgets.QTableWidgetItem(pago[1])
            capital = QtWidgets.QTableWidgetItem(pago[2])
            intereses = QtWidgets.QTableWidgetItem(pago[3])
            saldo = QtWidgets.QTableWidgetItem(pago[4])           
            
            self.ui.tblBitacora.setItem(i,0,periodo)
            self.ui.tblBitacora.setItem(i,1,cuota)
            self.ui.tblBitacora.setItem(i,2,capital)
            self.ui.tblBitacora.setItem(i,3,intereses)
            self.ui.tblBitacora.setItem(i,4,saldo)
            i+=1

    def registrarPersona(self): 
        
        self.fila = self.ui.tblBitacora2.rowCount()
        nombre = self.ui.txtNombre.text()
        cedula = self.ui.txtCedula.text()
        genero = self.ui.cmbGenero.currentText()
        sector = self.ui.cmbSector.currentText()
        monto = self.ui.txtMonto.text()

        self.objPersona = Persona(nombre, cedula, genero, sector, monto)
        self.ui.tblBitacora2.insertRow(self.fila)
        
        celdaCedula = QtWidgets.QTableWidgetItem(self.objPersona.cedula)
        celdaNombre = QtWidgets.QTableWidgetItem(self.objPersona.nombre)
        celdaGenero = QtWidgets.QTableWidgetItem(self.objPersona.genero)
        celdaSector = QtWidgets.QTableWidgetItem(self.objPersona.sector)
        

        self.ui.tblBitacora2.setItem(self.fila,0,celdaCedula)
        self.ui.tblBitacora2.setItem(self.fila,1,celdaNombre)
        self.ui.tblBitacora2.setItem(self.fila,2,celdaGenero)
        self.ui.tblBitacora2.setItem(self.fila,3,celdaSector)
        self.inicializarControles()
    

    def inicializarControles(self):
        self.ui.txtNombre.clear()
        self.ui.txtCedula.clear()
        self.ui.cmbGenero.setCurrentIndex(0)
        self.ui.cmbSector.setCurrentIndex(0)
        
   

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)    
    myapp = FrmUsuario()        
    myapp.show()
    sys.exit(app.exec())