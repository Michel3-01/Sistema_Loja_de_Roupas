#Classe que irá controlar as janelas.
from qt_core import *
from controller.main_window import MainWindow

import model.produtos_dao as funções_produtos
from model.produtos import Produtos
from model.clientes import Clientes
import model.clientes_dao as funções_clientes
    
app = QApplication(sys.argv)


window = MainWindow()
window.show()
app.exec()
