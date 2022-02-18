from qt_core import *
from model.funcionarios import Funcionarios
import model.funcionarios_dao as funções_funcionarios
from model import database_funcionarios

FILE_UI='view/cadastro_funcionarios.ui'

class CadFuncionario(QWidget):
    def __init__(self,janela_funcionario):
        super().__init__()
        uic.loadUi(FILE_UI, self)
        self.janela_funcionario = janela_funcionario


        #eventos dos botões.
        self.salvar_btn.clicked.connect(self.salvar)
        self.cancelar_btn.clicked.connect(self.fechar_janela)
      


  

    def salvar(self):
        nome = self.nome_func.text()
        email = self.email_func.text()
        cargo = self.cargo_func.text()

        novo_func = Funcionarios(None,nome,email,cargo)
        funções_funcionarios.adicionar_func(novo_func)

        self.janela_funcionario.show_funcionarios_page()


    def fechar_janela(self):
        self.painel_funcionarios.setCurrentIndex(1)
       

