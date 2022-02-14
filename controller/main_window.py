from qt_core import *
from controller.clientes_tela_principal import ClientesTelaPrincipal
from controller.funcionario_page import FuncionarioPage
from controller.estoque_page import EstoquePage
from controller.relatorio_page import RelatorioPage
from controller.vendas_page import CadastroVendas
from controller.produtos_tela_principal import ProdutosTelaPrincipal
FILE_UI='view/main_window.ui'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)
        #Objetos referente as páginas.
        
        self.relatorio_page = RelatorioPage()
        self.estoque_page = EstoquePage()
        self.cliente_page = ClientesTelaPrincipal()
        self.func_page = FuncionarioPage()
        self.vendas_page = CadastroVendas()
        self.prod_tela_principal = ProdutosTelaPrincipal()

        #Adiciona ás páginas ao painel principal.
        self.painel_principal.insertWidget(0, self.relatorio_page)
        self.painel_principal.insertWidget(1, self.estoque_page)
        self.painel_principal.insertWidget(2, self.cliente_page)
        self.painel_principal.insertWidget(3, self.func_page)
        self.painel_principal.insertWidget(4, self.vendas_page)
        self.painel_principal.insertWidget(5, self.prod_tela_principal)

        #Define os eventos/ações dos botões.
        self.relatorio_btn.clicked.connect(self.show_relatorio)
        self.estoque_btn.clicked.connect(self.show_estoque)
        self.cad_clientes_btn.clicked.connect(self.show_cad_clientes)
        self.cad_func_btn.clicked.connect(self.show_cad_func)
        self.vendas_btn.clicked.connect(self.show_cad_vendas)
        self.produtos_btn.clicked.connect(self.show_prod_tela_principal)
        

    def show_relatorio(self):
        self.painel_principal.setCurrentIndex(0)
    def show_estoque(self):
        self.painel_principal.setCurrentIndex(1)
    def show_cad_clientes(self):
        self.painel_principal.setCurrentIndex(2)
    def show_cad_func(self):
        self.painel_principal.setCurrentIndex(3)
    def show_cad_vendas(self):
        self.painel_principal.setCurrentIndex(4)
    def show_prod_tela_principal(self):
        self.painel_principal.setCurrentIndex(5)
 