import httpx
import http
from qt_core import *


FILE_UI='view/card_produto.ui'

class CardProduto(QWidget):
    def __init__(self, produto):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.label_nome.setText(produto.nome_prod)
        self.label_valor.setText(produto.valor_prod)
       


    