from qt_core import *

FILE_UI='view/cadastro_produtos.ui'

class ProdutosPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)