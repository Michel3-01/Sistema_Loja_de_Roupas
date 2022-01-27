import email
from qt_core import *
from model.clientes import Clientes
import model.clientes_dao as funções_clientes
#Variavel que contém o arquivo ui.
FILE_UI = 'view/cadastro_clientes.ui'

class ClientePage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI,self)

        
        
        self.carrega_dados()
        #Evento dos botões.
        self.cancelar_btn.clicked.connect(self.fechar_janela)
        self.salvar_btn.clicked.connect(self.salvar)

    def fechar_janela(self):
        self.close()
    def salvar(self):
        #Pega os dados dos clientes.
        nome = self.nome.text()
        email = self.email.text()
        telefone = self.telefone.text()
        
        #criar o objeto.
        novo_cliente = Clientes(None,nome,email,telefone)
        funções_clientes.adicionar(novo_cliente)

        
        #Carrega os dados na minha tabela.
         
        self.carrega_dados()
        #Pegar a lista de todos os clientes.
    def carrega_dados(self):
        lista_clientes = funções_clientes.lista_clientes
        #Zera a tabela e reconstroi.
        self.tabela_clientes.setRowCount(0) #Zera as linhas da tabela.
        for cliente in lista_clientes:
            self.add_linha(cliente)
        #Fechar a janela.
    def add_linha(self, cliente):
        rowCount = self.tabela_clientes.rowCount()
        self.tabela_clientes.insertRow(rowCount)

        #Elementos de cada coluna da tabela.
        id = QTableWidgetItem(str(cliente.id))
        nome = QTableWidgetItem(cliente.nome)
        email =QTableWidgetItem(cliente.email)
        telefone = QTableWidgetItem(cliente.telefone)

        #Insere os elementos da tabela na coluna correspondente.
        self.tabela_clientes.setItem(rowCount, 0 , id)
        self.tabela_clientes.setItem(rowCount, 1 , nome)
        self.tabela_clientes.setItem(rowCount, 2 , email)
        self.tabela_clientes.setItem(rowCount, 3 , telefone)