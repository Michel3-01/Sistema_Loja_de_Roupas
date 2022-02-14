import httpx
import http
from qt_core import *
import model.produtos_dao as funções_produtos

from model import database_produtos


FILE_UI='view/card_produto.ui'

class CardProduto(QWidget):
    def __init__(self,produto, janela_produtos):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.produto = produto
        self.janela_produtos= janela_produtos
        

        self.produto = produto
        self.label_nome.setText(produto.nome_prod)
        self.label_valor.setText(str(produto.valor_prod))

        #Evento dos botões.
        self.excluir_btn.clicked.connect(self.excluir)
        self.editar_btn.clicked.connect(self.editar)
    
    #Função de excluir um produto.
    def excluir(self):
        id = self.produto.id
        funções_produtos.excluir_prod(id)
        #Carrega a janela de produtos.
        self.janela_produtos.show_produtos_page()

    def editar(self):
        self.janela_produtos.show_tela_edição(self.produto)

    
    
       
        
        

        
       


    