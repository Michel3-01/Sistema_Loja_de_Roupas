from controller.produtos_page import CadProduto
from qt_core import *
from controller.tela_ediçao_produto import EdicaoProdutoPage
from controller.produtos_tela import ProdutoPage
import model.produtos_dao as funções_produtos

FILE_UI = 'view/produtos_tela_principal.ui'
class ProdutosTelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI,self)

   
        
        #Carrega a página inicial.
        self.show_produtos_page()
        
        #Evento do botão.
        self.cadastrar_produto_btn.clicked.connect(self.show_cad_prod)
        self.listar_produtos_btn.clicked.connect(self.show_listar_produtos)
        
    
    def show_cad_prod(self):
        self.painel_produtos.insertWidget(1,CadProduto(self))
        self.painel_produtos.setCurrentIndex(1)
    def show_listar_produtos(self):
        self.painel_produtos.insertWidget(0,ProdutoPage(self))
        self.painel_produtos.setCurrentIndex(0)

    def show_produtos_page(self):
        self.painel_produtos.insertWidget(0,ProdutoPage(self))
        self.painel_produtos.setCurrentIndex(0)
    def show_tela_edição(self, produto=None):
        self.painel_produtos.insertWidget(2,EdicaoProdutoPage(self,produto))
        self.painel_produtos.setCurrentIndex(2)

    

        
       