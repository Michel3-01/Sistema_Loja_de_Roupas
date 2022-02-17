from controller.card_estoque import CardEstoque
from qt_core import *
import model.produtos_dao as funções_produto
import model.estoque_dao as funções_estoque

FILE_UI='view/estoque.ui'

class EstoquePage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)

    
        self.load()
    def load(self):
        lista_estoque = funções_estoque.listar_estoque()
        for estoque in lista_estoque:
            pass
        lista = funções_produto.listar_produtos()
        for produtos in lista:
            self.painel_estoque_scrollarea.addWidget(CardEstoque(produtos,estoque))
           