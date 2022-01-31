from model.produtos import Produtos
from qt_core import *
import model.clientes_dao as funções_clientes
import model.produtos_dao as funções_produtos


FILE_UI = 'view/cadastro_vendas_page.ui'
class CadastroVendas(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI,self)
        #Listas
        self.lista_clientes = None
        self.lista_produtos = None
        self.lista_produto = []
        #cliente_atual.
        self.cliente_atual = None
        #produto atual.
        self.produto_atual = None
        #valor_quantidade_por_preço.
        self.quant_preco = None
        #valor_total.
        self.valor_total = None
        #valor_pago.
        self.valor_pago = 0
        #Lista de clientes
        #self.lista_clientes = funções_clientes.lista_clientes

        #temp_list = [] #Armazena os nomes dos clientes.
        #for x in self.lista_clientes:
            #temp_list.append(x.nome)

        #self.clientes_combobox.addItems(temp_list)

        #Evento do botão finalizar venda.
        self.finalizar_venda_btn.clicked.connect(self.finalizar_venda)
        self.adicionar_btn.clicked.connect(self.add_produto_lista)

        #self.carrega_clientes()
        self.carrega_produtos()
    
    """def carrega_clientes(self):
        #lista de peças.
        
        #Lista de clientes
        self.lista_clientes = funções_clientes.lista_clientes

        temp_list = [] #Armazena os nomes dos clientes.
        for x in self.lista_clientes:
            temp_list.append(x.nome)

        self.clientes_combobox.addItems(temp_list)
        #Evento que pega o INDEX do cliente selecionado.
        self.clientes_combobox.currentIndexChanged.connect(self.pega_cliente)"""
        #adicionar um produto.
        
        
    def add_produto_lista(self,index):
        lista_compra = self.lista_produto
        if self.quantidade.text() == '' or self.valor_unitario.text() == '':
            print('Insira os dados obrigatorios.')
        else:
            self.produto_atual = funções_produtos.lista_produtos[index]

            #Calcula o valor unitario do produto vezes a quantidade de produtos.
            self.quant_preco = int(self.quantidade.text()) * int(self.valor_unitario.text())
            produto = {'id':len(lista_compra),'quantidade': self.quantidade.text(), 'nome':self.produto_atual.nome_prod,'total':self.quant_preco}
            lista_compra.append(produto)
            print(self.quant_preco)
            self.atualiza_dados_venda()
           
    def  atualiza_dados_venda(self):
        #atualiza a quantidade de itens e o valor_total.
        #Lista de produtos
        self.valor_total = 0
        for produtos in self.lista_produto:
            print(produtos)
            print(type(produtos['total']))
            self.valor_total = self.valor_total + produtos['total']

            self.subtotal.setText(f'R$ {self.valor_total}')

            print('Valor total dos produtos:',self.valor_total)
            #Calcula o troco.
            

        lista_prod = self.lista_produto

        self.tabela_produtos.setRowCount(0)#Zera as linhas da tabela.

        for produtos in lista_prod:
            self.add_linha(produtos)
    def add_linha(self, produtos):
        rowCount = self.tabela_produtos.rowCount()
        self.tabela_produtos.insertRow(rowCount)

        #Elementos de cada coluna da tabela.
        id = QTableWidgetItem(str(produtos['id']))
        nome = QTableWidgetItem(produtos['nome'])
        quantidade = QTableWidgetItem(produtos['quantidade'])
        total = QTableWidgetItem(str(produtos['total']))

        #Insere os elementos da tabela na coluna correspondente.
        self.tabela_produtos.setItem(rowCount,0,id)
        self.tabela_produtos.setItem(rowCount,1,nome)
        self.tabela_produtos.setItem(rowCount,2,quantidade)
        self.tabela_produtos.setItem(rowCount,3,total)
    def carrega_produtos(self):
        #Lista de produtos.
        self.lista_produtos = funções_produtos.lista_produtos
        for y in self.lista_produtos:
            self.produtos_listWidget.addItem(y.nome_prod)
        
        self.produtos_listWidget.currentRowChanged.connect(self.pega_produto)
    def pega_produto(self, index):
        self.produto_atual = self.lista_produtos[index]
        self.valor_unitario.setText(str(self.produto_atual.valor_prod))
        #print(self.produto_atual.nome_prod)
    def pega_cliente(self,index):
        self.cliente_atual = self.lista_clientes[index]
        self.label_id.setText(f'{self.cliente_atual.id}')

    def finalizar_venda(self):
        self.valor_pago = 0
        self.valor_pago = int(self.total_pago.text()) 
        valor_troco =  self.valor_pago - self.valor_total
        self.troco.setText(f'R$ {valor_troco}')
        
            
       
