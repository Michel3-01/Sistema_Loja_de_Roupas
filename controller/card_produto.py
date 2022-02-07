import httpx
import http
from qt_core import *
from model import database_produtos


FILE_UI='view/card_produto.ui'

class CardProduto(QWidget):
    def __init__(self,produto):
        super().__init__()
        uic.loadUi(FILE_UI, self)



        self.produto = produto
        self.label_nome.setText(produto.nome_prod)
        self.label_valor.setText(str(produto.valor_prod))
        
        

        
       


    