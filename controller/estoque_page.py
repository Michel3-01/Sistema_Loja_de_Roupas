from qt_core import *

FILE_UI='view/estoque.ui'

class EstoquePage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)