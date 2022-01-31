from qt_core import *
import model.produtos_dao as funções_produto
from controller.card_produto import CardProduto


FILE_UI='view/produtos_page.ui'

class ProdutoPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.load()

    def load(self):
        lista = funções_produto.lista_produtos
        for novo_produto in lista:
            self.painel_scrollarea.addWidget(CardProduto(novo_produto))
        