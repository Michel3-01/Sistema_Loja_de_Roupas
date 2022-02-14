from controller.cliente_page import CadClientes
from controller.clientes_tela import ClientesPage
from qt_core import *

FILE_UI = 'view/clientes_tela_principal.ui'
class ClientesTelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI,self)

        #Eventos dos botões listar e cadastrar.
        self.listar_clientes_btn.clicked.connect(self.listar_clientes)
        self.cadastrar_clientes_btn.clicked.connect(self.cad_clientes)


    def cad_clientes(self):
        self.painel_clientes.insertWidget(0,CadClientes())
        self.painel_clientes.setCurrentIndex(0)
    def listar_clientes(self):
        self.painel_clientes.insertWidget(1,ClientesPage(self) )
        self.painel_clientes.setCurrentIndex(1)
    def show_produtos_page(self):
        self.painel_clientes.insertWidget(1,ClientesPage(self) )
        self.painel_clientes.setCurrentIndex(1)

 
