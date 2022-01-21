from qt_core import *
#Variavel que contém o arquivo ui.
FILE_UI = 'view/cadastro_clientes.ui'

class ClientePage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI,self)
