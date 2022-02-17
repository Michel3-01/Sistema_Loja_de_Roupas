from controller.funcionario_page import CadFuncionario
from controller.funcionarios_tela import FuncionarioPage
from controller.tela_ediçao_func import EdicaoFuncPage
from qt_core import *

FILE_UI = 'view/funcionarios_tela_principal.ui'

class FuncionariosTelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)


        #Ações dos botões.
        self.listar_funcionarios_btn.clicked.connect(self.show_listar_funcionarios)
        self.cadastrar_funcionarios_btn.clicked.connect(self.show_cad_funcionario)

        self.show_funcionarios_page()
    #Funções dos botões.
    def show_listar_funcionarios(self):
        self.painel_funcionarios.insertWidget(1,FuncionarioPage(self))
        self.painel_funcionarios.setCurrentIndex(1)
    def show_cad_funcionario(self):
        self.painel_funcionarios.insertWidget(0,CadFuncionario())
        self.painel_funcionarios.setCurrentIndex(0)
    def show_funcionarios_page(self):
        self.painel_funcionarios.insertWidget(1,FuncionarioPage(self))
        self.painel_funcionarios.setCurrentIndex(1)
    def show_tela_edicao_func(self,funcionario=None):
        self.painel_funcionarios.insertWidget(2,EdicaoFuncPage(self,funcionario))
        self.painel_funcionarios.setCurrentIndex(2)
