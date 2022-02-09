from qt_core import *
import model.produtos_dao as funções_produto
from controller.card_produto import CardProduto
from model import database_produtos


FILE_UI='view/produtos_page.ui'

class ProdutoPage(QWidget):
    def __init__(self, mainwindow):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.mainwindow = mainwindow
        self.load()

    def load(self):
        
          lista = funções_produto.listar_produtos()
          for produto in lista:
            self.painel_scrollarea.addWidget(CardProduto(produto, self.mainwindow))
            
            
                
                
                
                
       
        