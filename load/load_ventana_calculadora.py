from PyQt5 import QtWidgets, uic
from clases.calculadora import Calculadora

class VentanaCalculadora(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI/Ventana_Calculadroa.ui", self)
        self.show()
        self.boton_sumar.clicked.connect(self.botnSumarCick)
        
    def botnSumarCick(self):
        #Enlacar propiedades con componentes
        num1 = int(self.edit_numero1.text())
        num2 = int(self.edit_numero2.text())
        
        cal = Calculadora(num1, num2)
        
        cal.calcular_suma()
        
        self.label_resultado.setText(str(cal.resultado))