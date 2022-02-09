from qt_core import *
from model.produtos import Produtos
import model.produtos_dao as funções_produtos



FILE_UI='view/tela_edicao.ui'

class EdicaoProdutoPage(QWidget):
    def __init__(self,janela_produtos,produto):
        super().__init__()
        uic.loadUi(FILE_UI, self)
        self.produto = produto
        self.janela_produtos = janela_produtos #Referencia a janela produtos.

        #Evento dos botões.
        self.cancelar_prod_btn.clicked.connect(self.cancelar_edicao)
        self.salvar_prod_btn.clicked.connect(self.salvar_edicao)

        self.pega_dados_produtos()

    def cancelar_edicao(self):
       self.janela_produtos.show_produtos_page()
    def pega_dados_produtos(self):
        #Carrega os valores antigos.
        self.nome01.setText(self.produto.nome_prod)
        self.marca01.setText(self.produto.tipo_prod)
        self.genero01.setText(self.produto.genero)
        self.tamanho01.setText(self.produto.tamanho)
        self.quant_estoque01.setText(str(self.produto.quant_estoque))
        self.valor01.setText(str(self.produto.valor_prod))

    def salvar_edicao(self):
        #Salva os novos dados do produto;
        nome_prod = self.nome01.text()
        tipo_prod = self.marca01.text()
        genero = self.genero01.text()
        tamanho = self.tamanho01.text()
        quant_estoque = self.quant_estoque01.text()
        valor_prod = self.valor01.text()

        nova_edicao = Produtos(self.produto.id, nome_prod, tipo_prod, genero, tamanho, quant_estoque, valor_prod)
        funções_produtos.editar_prod(nova_edicao)
        
        
