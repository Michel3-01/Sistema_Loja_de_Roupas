from controller.card_cliente import FILE_UI
from qt_core import *

FILE_UI = 'view/card_funcionario.ui'

class CardFuncionario(QWidget):
    def __init__(self, funcionario,janela_funcionario):
        super().__init__()
        uic.loadUi(FILE_UI,self)

        self.janela_funcionario = janela_funcionario
        self.funcionario = funcionario

        
