import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QFormLayout, QDialog
#Yen vs Dolar Can.
# 

class VentanaComparacion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600,500)
        self.setWindowTitle("Grupo 4: Yen vs Dólar Canadience")
        layout = QVBoxLayout()
        
        messageL = QLabel('Bienvenido')
        layout.addWidget(messageL)
        self.botonComparar = QPushButton('Comparar')
        self.botonComparar.clicked.connect(self.comparar)
        
        layout.addWidget(self.botonComparar)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        
        
        
    def comparar():
        pass
        
class Divisa:
    def __init__(self,nombredivisa,valordivisa):
        self.nombredivisa = nombredivisa
        self.valordivisa = float(valordivisa)


class VentanaComparacion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600,500)
        
        self.setWindowTitle("Grupo 4: Yen vs Dólar Canadience")
        
        self.botonComparar = QPushButton('Comparar')
        self.botonComparar.clicked.connect(self.comparar)
        layout = QVBoxLayout()
        layout.addWidget(self.botonComparar)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def comparar(self):
        # Creamos una instancia de la ventana secundaria y la mostramos
        ventanaDatos = QDialog()
        ventanaDatos.setWindowTitle("Ingresar nueva divisa")
        etiquetaNombre = QLabel("Nombre de la divisa:")
        entradaNombre = QLineEdit()
        etiquetaValor = QLabel("Valor de la divisa:")
        entradaValor = QLineEdit()
        botonAceptar = QPushButton("Aceptar")
        botonAceptar.clicked.connect(ventanaDatos.accept)
        botonCancelar = QPushButton("Cancelar")
        botonCancelar.clicked.connect(ventanaDatos.reject)

        layout = QVBoxLayout()
        layout.addWidget(etiquetaNombre)
        layout.addWidget(entradaNombre)
        layout.addWidget(etiquetaValor)
        layout.addWidget(entradaValor)
        layout.addWidget(botonAceptar)
        layout.addWidget(botonCancelar)

        ventanaDatos.setLayout(layout)

        if ventanaDatos.exec() == QDialog.Accepted:
            nombreDivisa = entradaNombre.text()
            valorDivisa = entradaValor.text()
            divisa = Divisa(nombreDivisa, valorDivisa)
            print(f'Se ingresó una nueva divisa: {divisa.nombredivisa} = {divisa.valordivisa}')
    
app = QApplication(sys.argv)
ventana = VentanaComparacion()
ventana.show()
sys.exit(app.exec())    
        