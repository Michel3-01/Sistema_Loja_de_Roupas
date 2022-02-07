from controller.produtos_page import CadProduto
from qt_core import *
from controller.produtos_tela import ProdutoPage

FILE_UI = 'view/produtos_tela_principal.ui'
class ProdutosTelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI,self)

        
        self.painel_produtos.insertWidget(0,ProdutoPage())
        #Evento do botão.
        self.cadastrar_produto_btn.clicked.connect(self.show_cad_prod)
        self.listar_produtos_btn.clicked.connect(self.show_listar_produtos)

    
    def show_cad_prod(self):
        self.painel_produtos.insertWidget(1,CadProduto(self))
        self.painel_produtos.setCurrentIndex(1)
    def show_listar_produtos(self):
        self.painel_produtos.insertWidget(0,ProdutoPage())
        self.painel_produtos.setCurrentIndex(0)

    def show_produtos_page(self):
        self.painel_produtos.insertWidget(0,ProdutoPage())
        self.painel_produtos.setCurrentIndex(0)
       