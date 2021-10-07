import sys
from clients import *
import var

class Eventos():
        def Salir(self):
            try:
                var.dlgaviso.show()
                if var.dlgaviso.exec():
                    sys.exit(self)
                else:
                    var.dlgaviso.hide()
            except Exception as error:
                print('Error en módulo salir ', error)

        def validoDNI():
            try:
                dni = var.ui.editDni.text()
                if Clients.validarDNI(dni):
                    var.ui.lblValido.setStyleSheet('QLabel {color: green;}')
                    var.ui.lblValido.setText('V')
                    var.ui.edirDni.setText(dni.upper())
                else:
                    var.ui.lblValido.setStyleSheet('QLabel {color: red;}')
                    var.ui.lblValido.setText('X')
                    var.ui.editDni.setText(dni.upper())

            except Exception as error:
                print('Error: %s ' % str(error))