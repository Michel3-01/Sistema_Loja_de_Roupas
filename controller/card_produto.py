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
        self.label_id.setText(str(self.produto.id))
        self.label_nome.setText(produto.nome_prod)
        self.label_valor.setText(str(produto.valor_prod))
        self.label_tipo.setText(produto.tipo_prod)
        self.label_tamanho.setText(produto.tamanho)
        self.label_genero.setText(produto.genero)
        #Stylesheet dos labels .
        self.label_nome.setStyleSheet('border: 1px double black; border-radius: 10px; background-color:rgb(25, 0, 77); color:white; font-size: 15px; text-align:center;')
        self.label_id.setStyleSheet('border: 1px dotted black; background-color:rgb(148, 77, 255); color:white; font-size:15px;')
        self.label_tipo.setStyleSheet('font-size: 18px; color: white;')
        self.label_tamanho.setStyleSheet('font-size: 18px; color: white;')
        self.label_genero.setStyleSheet('font-size: 18px; color: white;')
        self.label_valor.setStyleSheet('font-size: 18px; color: white;')

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

    
    
       
        
        

        
       


    