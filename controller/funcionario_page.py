from qt_core import *
from model.funcionarios import Funcionarios
import model.funcionarios_dao as funções_funcionarios
from model import database_funcionarios

FILE_UI='view/cadastro_funcionarios.ui'

class CadFuncionario(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)


        #eventos dos botões.
        self.salvar_btn.clicked.connect(self.salvar)
        self.cancelar_btn.clicked.connect(self.fechar_janela)
        self.editar_btn.clicked.connect(self.editar)
        self.excluir_btn.clicked.connect(self.excluir)


    #Função de editar um cliente.
    def editar(self):
        pass
    #Função de excluir um cliente.
    def excluir(self):
        pass


    def salvar(self):
        nome = self.nome_func.text()
        email = self.email_func.text()
        cargo = self.cargo_func.text()

        novo_func = Funcionarios(None,nome,email,cargo)
        funções_funcionarios.adicionar_func(novo_func)


    def fechar_janela(self):
        pass
       

