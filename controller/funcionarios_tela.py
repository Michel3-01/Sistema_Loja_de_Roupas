from controller.card_funcionario import CardFuncionario
from qt_core import *
import model.funcionarios_dao as funções_funcionario

FILE_UI = 'view/funcionarios_page.ui'

class FuncionarioPage(QWidget):
    def __init__(self, janela_funcionario):
        super().__init__()
        uic.loadUi(FILE_UI, self)
        self.janela_funcionario = janela_funcionario

        self.load()

    def load(self):#Insere os card_funcionários.
        lista = funções_funcionario.listar_todos()
        for funcionarios in lista:
            
            self.painel_funcionarios_scrollarea.addWidget(CardFuncionario(funcionarios, self.janela_funcionario))
