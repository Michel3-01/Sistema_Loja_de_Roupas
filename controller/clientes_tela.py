from controller.card_cliente import CardCliente
from qt_core import *
import model.clientes_dao as funções_clientes

FILE_UI = 'view/clientes_page.ui'
class ClientesPage(QWidget):
    def __init__(self,janela_cliente):
        super().__init__()
        uic.loadUi(FILE_UI,self)


        self.janela_cliente = janela_cliente
        self.load()
        


    def load(self):
        lista = funções_clientes.listar_clientes()
        for self.cliente in lista:
            self.painel_clientes_scrollarea.addWidget(CardCliente(self.cliente, self.janela_cliente))

