from qt_core import *
import model.produtos_dao as funções_produto
from controller.card_produto import CardProduto
from model import database_produtos


FILE_UI='view/produtos_page.ui'

class ProdutoPage(QWidget):
    def __init__(self,janela_produtos):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.janela_produtos = janela_produtos
        self.load()
    


    def load(self):
        lista = funções_produto.listar_produtos()
        for self.produto in lista:
            self.painel_scrollarea.addWidget(CardProduto(self.produto, self.janela_produtos))
    
    
        
    
            

            
    
    
            
            
                
                
                
                
       
        