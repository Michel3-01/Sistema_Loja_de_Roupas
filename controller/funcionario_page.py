from qt_core import *
from model.funcionarios import Funcionarios
import model.funcionarios_dao as funções_funcionarios

FILE_UI='view/cadastro_funcionarios.ui'

class FuncionarioPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        #eventos dos botões.
        self.salvar_btn.clicked.connect(self.salvar)
        self.cancelar_btn.clicked.connect(self.fechar_janela)

    def salvar(self):
        nome = self.nome_func.text()
        email = self.email_func.text()
        cargo = self.cargo_func.text()

        novo_func = Funcionarios(None,nome,email,cargo)
        funções_funcionarios.adicionar_func(novo_func)


        self.carrega_dados()

    def carrega_dados(self):
        #Zera as linhas da tabela.
        self.tabela_funcionarios.setRowCount(0) 
        for funcionario in funções_funcionarios.lista_funcionarios:
            self.add_linha(funcionario)
        
    def add_linha(self,funcionario):
         rowCount = self.tabela_funcionarios.rowCount()
         self.tabela_funcionarios.insertRow(rowCount)

         #Cria o elemento de cada coluna da tabela
         id = QTableWidgetItem(str(funcionario.id))
         nome = QTableWidgetItem(funcionario.nome_func)
         email = QTableWidgetItem(funcionario.email_func)
         cargo = QTableWidgetItem(funcionario.cargo_func)

         #Insere os elementos coluna correspondente.

         self.tabela_funcionarios.setItem(rowCount, 0, id)
         self.tabela_funcionarios.setItem(rowCount, 1, nome)
         self.tabela_funcionarios.setItem(rowCount, 2 , email)
         self.tabela_funcionarios.setItem(rowCount, 3 , cargo)


    def fechar_janela(self):
        pass
       

