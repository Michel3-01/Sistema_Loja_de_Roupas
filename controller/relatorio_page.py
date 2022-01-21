from qt_core import *


FILE_UI='view/relatorio.ui'

class RelatorioPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)