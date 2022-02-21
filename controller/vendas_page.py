from controller.estoque_page import EstoquePage
from model.estoque import Estoque
from model.produtos import Produtos
from qt_core import *
import model.clientes_dao as funções_clientes
import model.produtos_dao as funções_produtos
import model.estoque_dao as funções_estoque
import model.vendas_dao as funções_vendas
from model.vendas import Vendas
from model import database
from model import database_produtos


FILE_UI = 'view/cadastro_vendas_page.ui'
class CadastroVendas(QWidget):
    def __init__(self,main_window):
        super().__init__()
        uic.loadUi(FILE_UI,self)
        #Listas
        self.lista_produtos = None
        self.lista_produto = []
        #produto atual.
        self.produto_atual = None
        #valor_quantidade_por_preço.
        self.quant_preco = None
        #valor_total.
        self.valor_total = None
        #valor_pago.
        self.valor_pago = 0
        #Lista de clientes
        
        self.cliente_atual = None
        self.lista_pega_dados_clientes = []
        self.main_window = main_window
    

  
        self.carrega_produtos()

        #Evento do botão finalizar venda.
        self.finalizar_venda_btn.clicked.connect(self.finalizar_venda)
        self.adicionar_btn.clicked.connect(self.add_produto_lista)
       
       
        self.carrega_clientes()
        self.carrega_produtos()
        self.atualiza_dados_venda()
        
    
 
   
    #Função carrega clientes no combobox.
    def carrega_clientes(self):
 
        self.lista_nome_clientes = []
        lista = funções_clientes.listar_clientes()
        for cliente in lista:
            self.lista_nome_clientes.append(cliente.nome)
  
        self.clientes_combobox.addItems(self.lista_nome_clientes)
    
        #Evento que pega o INDEX do cliente selecionado.
        self.clientes_combobox.currentIndexChanged.connect(self.pega_cliente)
        #adicionar um produto.
        
        
    def add_produto_lista(self,index):
        #lista_compra = self.lista_produto
        if self.quantidade.text() == '' or self.valor_unitario.text() == '':
            print('Insira os dados obrigatorios.')
        else:
            
            nome = self.produto_atual.nome_prod
           

            #Calcula o valor unitario do produto vezes a quantidade de produtos.
            self.quant_preco = int(self.quantidade.text()) * int(self.valor_unitario.text())
            produto = {'id':len(self.lista_produto),'quantidade': self.quantidade.text(), 'nome':nome,'total':self.quant_preco}
            self.lista_produto.append(produto)
            self.atualiza_dados_venda()
            vendidos = 0
            #Atualizando o estoque:
            nome_prod = self.produto_atual.nome_prod
            quant_inicial = self.produto_atual.quant_estoque
            vendidos = int(self.quantidade.text())
            quant_atual = int(self.produto_atual.quant_estoque) - vendidos
            if quant_atual <= 100:
                situacao = 'Vermelho'
            elif quant_atual >= 500:
                situacao = 'Verde'
            else:
                situacao = 'Normal'
            
        
            estoque = Estoque(None,nome_prod, quant_inicial, vendidos, quant_atual, situacao,self.produto_atual.id)
            funções_estoque.adicionar(estoque)
          

    


                    
               
                  

           
    def  atualiza_dados_venda(self):
        #atualiza a quantidade de itens e o valor_total.
        #Lista de produtos
        self.valor_total = 0
        self.lista_valores_venda = [] #Guarda os valores das vendas realizadas.
        for produtos in self.lista_produto:
     
            self.valor_total = self.valor_total + produtos['total']

            self.subtotal.setText(f'R$ {self.valor_total}')
            self.lista_valores_venda.append(self.valor_total)

            print('Valor total dos produtos:',self.valor_total)
          
            


        
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
   
            lista = funções_produtos.listar_produtos()
            for produto in lista:
                self.produtos_listWidget.addItem(produto.nome_prod)
                
     
        
            self.produtos_listWidget.currentRowChanged.connect(self.pega_produto)
    #Função de pegar um produto.
    def pega_produto(self, index):
    
 
            lista = funções_produtos.listar_produtos()
            self.listar_produtos = []
            x = []
            for produto in lista:
                x.append(produto)
            for produtos in x:
                self.listar_produtos.append(produtos)
            self.produto_atual = self.listar_produtos[index]
            
            self.valor_unitario.setText(str(self.produto_atual.valor_prod))
  
        #Set o valor do campo valor unitário para o valor do produto atual.
        
            

    #Função de pegar um cliente.
    def pega_cliente(self, index):

        self.listar_cliente = []
        x = []
        lista = funções_clientes.listar_clientes()
        for cliente in lista:
            x.append(cliente)
        for cliente in x:
            self.listar_cliente.append(cliente)
        self.cliente_atual = self.listar_cliente[index]
        
     
        self.label_id.setText(str(self.cliente_atual.id))
    
        
        

    def finalizar_venda(self):
        self.valor_pago = 0
        self.valor_pago = int(self.total_pago.text()) 
        valor_troco =  self.valor_pago - self.valor_total
        self.troco.setText(f'R$ {valor_troco}')
        

        self.salvar_vendas()

        
      
    def salvar_vendas(self):
        #Salva os dados da venda.
        nome = self.cliente_atual.nome
        email = self.cliente_atual.email   
        valor = self.valor_total
        nova_venda = Vendas(None, nome, email,valor)
        funções_vendas.adicionar_vendas(nova_venda)
        self.close()
        self.main_window.show_estoque()



        

        
          
            
        #Pega os dados.
        #nome = self.cliente_atual[1]
        #email = self.cliente_atual[2]
        #O valor referente ao total da venda.
        #valor = self.valor_total
        #Adiciona uma venda no relatório.
        #nova_venda = Vendas(None,nome,email,valor)
        #funções_vendas.adicionar_vendas(nova_venda)
        #print(nova_venda.nome)
        
       
     

        
        
            
       
