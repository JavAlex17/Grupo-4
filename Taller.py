import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QFormLayout 
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
        
    
    
app = QApplication(sys.argv)
ventana = VentanaComparacion()
ventana.show()
sys.exit(app.exec())    
        