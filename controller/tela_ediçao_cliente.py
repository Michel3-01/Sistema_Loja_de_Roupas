from qt_core import *
from model.clientes import Clientes
import model.clientes_dao as funções_clientes



FILE_UI='view/tela_edição_cliente.ui'

class EdicaoClientePage(QWidget):
    def __init__(self,janela_cliente,cliente):
        super().__init__()
        uic.loadUi(FILE_UI, self)
        self.cliente = cliente
        self.janela_cliente = janela_cliente #Referencia a janela cliente.

        #Ações dos botões.
        self.salvar_cliente_btn.clicked.connect(self.salvar_edicao)
        self.cancelar_cliente_btn.clicked.connect(self.cancelar_edicao)

        self.pega_dados_clientes()

    def cancelar_edicao(self):
        self.janela_cliente.show_clientes_page()
    def pega_dados_clientes(self):
        #pega os valores antigos.
        self.nome.setText(self.cliente.nome)
        self.email.setText(self.cliente.email)
        self.telefone.setText(self.cliente.telefone)
    def salvar_edicao(self):
        nome = self.nome.text()
        email = self.email.text()
        telefone = self.telefone.text()

        nova_edicao = Clientes(self.cliente.id, nome, email, telefone)
        funções_clientes.editar(nova_edicao)

        self.janela_cliente.show_clientes_page()