import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QPushButton

#Yen vs Dolar Can.
#
class Divisa:
    def init(self,nombredivisa,valordivisa):
        self.nombredivisa = nombredivisa
        self.valordivisa = valordivisa

def calcular_equivalenteUSD(self):
    if self.nombredivisa == "Yen Japones":
        return self.valordivisa /134,80
    if self.nombredivisa == "Dolar Canadiense":
        return self.valordivisa/1,3371

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
        
    def comparar():
        pass
        

    
    
app = QApplication(sys.argv)
ventana = VentanaComparacion()
ventana.show()
sys.exit(app.exec())    
        