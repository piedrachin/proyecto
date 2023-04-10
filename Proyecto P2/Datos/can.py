 """ self.o_registro = Articulo()
        self.fila = self.ui.tbl_registro_articulos.rowCount()
        self.ui.tbl_registro_articulos.insertRow(self.fila)
        celdaDescripcion = QtWidgets.QTableWidgetItem(self.o_registro.descripcion)
        celdaCodigo = QtWidgets.QTableWidgetItem(self.o_registro.codigo)
        celdaCosto = QtWidgets.QTableWidgetItem(self.o_registro.costo)
        celdaCantidad = QtWidgets.QTableWidgetItem(self.o_registro.cantidad)
        celdaFecha = QtWidgets.QTableWidgetItem(self.o_registro.fecha)
        
        self.ui.tbl_registro_articulos.setItem(self.fila,0,celdaDescripcion)
        self.ui.tbl_registro_articulos.setItem(self.fila,1,celdaCodigo)
        self.ui.tbl_registro_articulos.setItem(self.fila,2,celdaCosto)
        self.ui.tbl_registro_articulos.setItem(self.fila,3,celdaCantidad)
        self.ui.tbl_registro_articulos.setItem(self.fila,4,celdaFecha)"""
        
        
        
        
    def registro_art_txt(self):
        descripcion = self.ui.txt_nombre.text()
        codigo = self.ui.txt_codigo.text()
        cantidad = str(self.ui.spBox_cantidad.value())
        costo = str(self.ui.txt_costo.text())
      # bodega = self.ui.cmb_bodega.currentText()
       # fecha = str(self.ui.dateEdit.date())
        fecha = str(self.ui.dateTimeEdit.text()) 
        i = 0
        #self.datos = (self.Nombre, self.Codigo, self.Cantidad)
        file = open("registro.txt", "a")
        file.write(str(i+1))
        file.write("\n---------- ARTICULOS REGISTRADOS ----------")
      #  file.write(str(i))
        file.write("\nDescripcion: "+descripcion+"\nCodigo: "+codigo+"\nCantidad: "
                   +cantidad+"\nCosto: "+costo+
            "\nFecha: "+fecha+"\n")
        file.write("\n")
        i += 1
        file.close()    
        
        
        
         self.ui.tbl_registro_articulos.setRowCount(0)
        num_fila = self.ui.tbl_registro_articulos.rowCount()
         
        for item in Persistencia.obtener_registro():
            self.ui.tbl_registro_articulos.insertRow(num_fila)
            descripcion = QtWidgets.QTableWidgetItem(item.descripcion)
            codigo = QtWidgets.QTableWidgetItem(str(item.codigo))
            costo = QtWidgets.QTableWidgetItem(str(item.costo))
            cantidad = QtWidgets.QTableWidgetItem(str(item.cantidad))
            fecha = QtWidgets.QTableWidgetItem(str(item.fecha))
            
            self.ui.tbl_registro_articulos.setItem(num_fila,0,descripcion)
            self.ui.tbl_registro_articulos.setItem(num_fila,1,codigo)
            self.ui.tbl_registro_articulos.setItem(num_fila,2,costo)
            self.ui.tbl_registro_articulos.setItem(num_fila,3,cantidad)
            self.ui.tbl_registro_articulos.setItem(num_fila,4,fecha)
            
            num_fila +=1
            
            
            
            
            
  def registro_art_txt(self):
        self.o_registro.descripcion = self.ui.txt_nombre.text()
        self.o_registro.codigo = self.ui.txt_codigo.text()
        self.o_registro.cantidad = str(self.ui.spBox_cantidad.value())
        self.o_registro.costo = str(self.ui.txt_costo.text())
      # bodega = self.ui.cmb_bodega.currentText()
       # fecha = str(self.ui.dateEdit.date())
        self.o_registro.fecha = str(self.ui.dateTimeEdit.text()) 
        i = 0
        #self.datos = (self.Nombre, self.Codigo, self.Cantidad)
        file = open("registro.txt", "a")
        file.write(str(i+1))
        file.write("\n---------- ARTICULOS REGISTRADOS ----------")
      #  file.write(str(i))
        file.write("\nDescripcion: "+self.o_registro.descripcion+"\nCodigo: "+self.o_registro.codigo+"\nCantidad: "
                   +self.o_registro.cantidad+"\nCosto: "+self.o_registro.costo+
            "\nFecha: "+self.o_registro.fecha+"\n")
        file.write("\n")
        i += 1
        file.close()   
        