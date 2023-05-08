import sys
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QDialog, QFormLayout


class Divisa:
    def __init__(self, nombre, valordivisa):
        self.nombre = nombre
        self.valordivisa = valordivisa

    def calcular_equivalente_usd(self):
        if self.nombre == "Yen Japones":
            return self.valordivisa / 134.80
        elif self.nombre == "Dolar Canadiense":
            return self.valordivisa / 1.3371


class DatosDivisaDialog(QDialog):
    def __init__(self, divisa):
        super().__init__()
        self.setWindowTitle("Ingresar Datos de Divisa")
        self.divisa = divisa
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        form_layout = QFormLayout()

        self.input_nombre = QLineEdit()
        self.input_nombre.setText(self.divisa.nombre)
        form_layout.addRow("Nombre:", self.input_nombre)

        self.input_valordivisa = QLineEdit()
        self.input_valordivisa.setText(str(self.divisa.valordivisa))
        form_layout.addRow("Valor Divisa:", self.input_valordivisa)

        layout.addLayout(form_layout)

        btn_guardar = QPushButton("Guardar")
        btn_guardar.clicked.connect(self.guardar_datos)
        layout.addWidget(btn_guardar)

        self.setLayout(layout)

    def guardar_datos(self):
        self.divisa.nombre = self.input_nombre.text()
        self.divisa.valordivisa = float(self.input_valordivisa.text())
        self.accept()


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 300)
        self.setWindowTitle("Comparación de Divisas")
        self.divisa_izquierda = Divisa("Yen Japones", 0.0)
        self.divisa_derecha = Divisa("Dolar Canadiense", 0.0)
        self.setup_ui()
        self.resize(600,300)
        self.setFont(QFont('Arial', 10))
        
    def setup_ui(self):
        layout = QVBoxLayout()

        # Texto de bienvenida
        label_bienvenida = QLabel("¡Bienvenido! Ingresa los datos de las divisas:")
        layout.addWidget(label_bienvenida)

        # Texto de instrucciones
        label_instrucciones = QLabel("Ingrese el valor de la divisa en su respectiva moneda:")
        layout.addWidget(label_instrucciones)

        # Panel de comparación
        panel_comparacion = QHBoxLayout()

        # Despliegue de información del objeto a la izquierda
        self.label_izquierda = QLabel()
        panel_comparacion.addWidget(self.label_izquierda)

        # Texto central que indica quién es mayor
        self.label_comparacion = QLabel()
        panel_comparacion.addWidget(self.label_comparacion)

        # Despliegue de información del objeto a la derecha
        self.label_derecha = QLabel()
        panel_comparacion.addWidget(self.label_derecha)

        layout.addLayout(panel_comparacion)

        # Botón de actualización de comparación
        btn_actualizar = QPushButton("Actualizar Comparación")
        btn_actualizar.clicked.connect(self.actualizar_comparacion)
        btn_actualizar.setStyleSheet("QPushButton { background-color: #d199f2; color: purple; }")
        layout.addWidget(btn_actualizar)
        btn_actualizar.setFixedSize(450, 50)

        # Botones de ingreso de datos
        btn_izquierda = QPushButton("Agregar Datos (Izquierda)")
        btn_izquierda.clicked.connect(self.abrir_dialogo_izquierda)
        btn_izquierda.setStyleSheet("QPushButton { background-color: #d199f2; color: purple; }")
        layout.addWidget(btn_izquierda)
        btn_izquierda.setFixedSize(450, 50)

        
        btn_derecha = QPushButton("Agregar Datos (Derecha)")
        btn_derecha.clicked.connect(self.abrir_dialogo_derecha)
        btn_derecha.setStyleSheet("QPushButton { background-color: #d199f2; color: purple; }")
        layout.addWidget(btn_derecha)
        btn_derecha.setFixedSize(450, 50)

        self.setLayout(layout)

    def abrir_dialogo_izquierda(self):
        dialog = DatosDivisaDialog(self.divisa_izquierda)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.actualizar_comparacion()

    def abrir_dialogo_derecha(self):
        dialog = DatosDivisaDialog(self.divisa_derecha)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.actualizar_comparacion()

    def actualizar_comparacion(self):
        equivalente_izquierda = self.divisa_izquierda.calcular_equivalente_usd()
        equivalente_derecha = self.divisa_derecha.calcular_equivalente_usd()

        if equivalente_izquierda > equivalente_derecha:
            self.label_comparacion.setText(">")
        elif equivalente_izquierda < equivalente_derecha:
            self.label_comparacion.setText("<")
        else:
            self.label_comparacion.setText("=")

        self.label_izquierda.setText(f"{self.divisa_izquierda.nombre}: {equivalente_izquierda}")
        self.label_derecha.setText(f"{self.divisa_derecha.nombre}: {equivalente_derecha}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec())

        