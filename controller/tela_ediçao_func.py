from qt_core import *
from model.funcionarios import Funcionarios
import model.funcionarios_dao as funções_funcionarios




FILE_UI='view/tela_edição_func.ui'

class EdicaoFuncPage(QWidget):
    def __init__(self,janela_funcionario,funcionario):
        super().__init__()
        uic.loadUi(FILE_UI, self)
        self.funcionario = funcionario
        self.janela_funcionario = janela_funcionario #Referencia a janela func.

        #Eventos dos botões.
        self.salvar_func_btn.clicked.connect(self.salvar_edicao)
        self.cancelar_func_btn.clicked.connect(self.cancelar_edicao)

        self.pega_dados_func()

    def pega_dados_func(self):
        #pega os valores antigos.
        self.nome.setText(self.funcionario.nome_func)
        self.email.setText(self.funcionario.email_func)
        self.cargo.setText(self.funcionario.cargo_func)
    def salvar_edicao(self):
        nome = self.nome.text()
        email = self.email.text()
        cargo = self.cargo.text()

        nova_edicao = Funcionarios(self.funcionario.id, nome, email, cargo)
        funções_funcionarios.editar(nova_edicao)
        

        
    def cancelar_edicao(self):
        self.janela_funcionario.show_funcionarios_page()
    