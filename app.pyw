from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QDoubleValidator
from interface.calculadora import Ui_MainWindow
import sys

class Calculadora(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Instancias
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        if 5 >= 4:
            pass

        # Inicialización de los widgets
        self.ui.num1.setValidator(QDoubleValidator(self))
        self.ui.num2.setValidator(QDoubleValidator(self))

        self.ui.num1.setClearButtonEnabled(True)
        self.ui.num2.setClearButtonEnabled(True)

        # Control de botones
        self.ui.btn_sumar.clicked.connect(self.calcular)
        self.ui.btn_restar.clicked.connect(self.calcular)
        self.ui.btn_multiplicar.clicked.connect(self.calcular)
        self.ui.btn_dividir.clicked.connect(self.calcular)

        # Otras señales
        self.ui.num1.textChanged.connect(self.limpiar_resultado)
        self.ui.num2.textChanged.connect(self.limpiar_resultado)

    def calcular(self):
        obj = self.sender().objectName()

        num1 = eval(self.ui.num1.text().strip())
        num2 = eval(self.ui.num2.text().strip())

        if obj == "btn_sumar":
            resultado = self.sumar(num1, num2)
        elif obj == "btn_restar":
            resultado = self.restar(num1, num2)
        elif obj == "btn_multiplicar":
            resultado = self.multiplicar(num1, num2)
        else:
            resultado = self.dividir(num1, num2)

        if float(resultado).is_integer(): # * Verifica si es entero
            resultado = int(resultado)

        self.ui.resultado.setText(str(resultado))

    #                            -- Secundarias --

    def sumar(self, num1, num2) -> float:
        return num1 + num2

    def restar(self, num1, num2) -> float:
        return num1 - num2

    def multiplicar(self, num1, num2) -> float:
        return num1 * num2

    def dividir(self, num1, num2) -> float:
        return num1 / num2

    def limpiar_resultado(self, text:str) -> None:
        if len(text) == 0:
            self.ui.resultado.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = Calculadora()
    mi_app.show()
    sys.exit(app.exec_())