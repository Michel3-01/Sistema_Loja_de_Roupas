#Classe que irá controlar as janelas.
from qt_core import *
from controller.main_window import MainWindow

import model.produtos_dao as funções_produtos
from model.produtos import Produtos
from model.clientes import Clientes
import model.clientes_dao as funções_clientes
    
#def carrega_produtos():
    #for i in range(0,5):
       # novo_produto = Produtos(None,f'produto{i}',50*i,'3.00','Feminino','médio')
        #funções_produtos.adicionar_prod(novo_produto)

app = QApplication(sys.argv)
#carrega_produtos()

window = MainWindow()
window.show()
app.exec()
