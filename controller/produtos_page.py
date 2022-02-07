from model.produtos import Produtos
import model.produtos_dao as funções_produto
from qt_core import *
import httpx
import http

FILE_UI='view/cadastro_produtos.ui'

class CadProduto(QWidget):
    def __init__(self,janela_produtos):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.janela_produtos = janela_produtos

        self.salvar_prod_btn.clicked.connect(self.salvar_produto)
        self.cancelar_prod_btn.clicked.connect(self.cancelar_page)

    def salvar_produto(self):
        nome_prod = self.nome.text()
        tipo_prod = self.marca.text()
        genero = self.genero.text()
        tamanho = self.tamanho.text()
        quant_estoque = self.quant_estoque.text()
        valor_prod = self.valor.text()
        
        #Criando um objeto.
        novo_produto = Produtos(None,nome_prod, tipo_prod,genero,tamanho,quant_estoque,valor_prod)
        funções_produto.adicionar_prod(novo_produto)


        self.janela_produtos.show_produtos_page()

    def cancelar_page(self):
        self.painel_produtos.setCurrentIndex(0)
    



        