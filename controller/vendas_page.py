import email
from model.produtos import Produtos
from qt_core import *
import model.clientes_dao as funções_clientes
import model.produtos_dao as funções_produtos
import model.vendas_dao as funções_vendas
from model.vendas import Vendas
from model import database
from model import database_produtos


FILE_UI = 'view/cadastro_vendas_page.ui'
class CadastroVendas(QWidget):
    def __init__(self):
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
        self.lista_clientes = funções_clientes.lista_clientes
        self.cliente_atual = None
        self.lista_pega_dados_clientes = []
    


    
        self.carrega_produtos()

        #Evento do botão finalizar venda.
        self.finalizar_venda_btn.clicked.connect(self.finalizar_venda)
        self.adicionar_btn.clicked.connect(self.add_produto_lista)
       
        self.carrega_dados_clientes()
        self.carrega_clientes()
        self.carrega_produtos()
        self.atualiza_dados_venda()
    #Função que pega os dados dos clientes.
    def carrega_dados_clientes(self):
   
        for x in funções_clientes.lista_clientes:
            self.lista_pega_dados_clientes.append(x)
   
    #Função carrega clientes no combobox.
    def carrega_clientes(self):
            self.lista_nome_clientes = []
            for x in self.lista_pega_dados_clientes:
                self.lista_nome_clientes.append(x[1])
                
      
            self.clientes_combobox.addItems(self.lista_nome_clientes)
            

       
        #Evento que pega o INDEX do cliente selecionado.
            self.clientes_combobox.currentIndexChanged.connect(self.pega_cliente)
        #adicionar um produto.
        
        
    def add_produto_lista(self,index):
        #lista_compra = self.lista_produto
        if self.quantidade.text() == '' or self.valor_unitario.text() == '':
            print('Insira os dados obrigatorios.')
        else:
            
            nome = self.produto_atual[1]
           

            #Calcula o valor unitario do produto vezes a quantidade de produtos.
            self.quant_preco = int(self.quantidade.text()) * int(self.valor_unitario.text())
            produto = {'id':len(self.lista_produto),'quantidade': self.quantidade.text(), 'nome':nome,'total':self.quant_preco}
            self.lista_produto.append(produto)
            self.atualiza_dados_venda()
           
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
        try:
            
            conn = database_produtos.connect()#Conecta
            consulta_sql = "SELECT * FROM Produtos"
            cursor = conn.cursor()#Se move no banco
            cursor.execute(consulta_sql)
            linhas = cursor.fetchall()
            listar_produtos = []
            x = []      
            for produto in linhas:
                x.append(produto[1])
            for produtos in x:
                listar_produtos.append(produtos)
                self.produtos_listWidget.addItem(produtos)
           
  
        except Exception as e:
            print('Deu erro!')
            print(e)
        finally:
            conn.close()
        
        
        self.produtos_listWidget.currentRowChanged.connect(self.pega_produto)
    #Função de pegar um produto.
    def pega_produto(self, index):
    
        try:
            
            conn = database_produtos.connect()#Conecta
            consulta_sql = "SELECT * FROM Produtos"
            cursor = conn.cursor()#Se move no banco
            cursor.execute(consulta_sql)
            linhas = cursor.fetchall()
            self.listar_produtos = []
            x = []      
            for produto in linhas:
                x.append(produto)
            for produtos in x:
                self.listar_produtos.append(produtos)
            self.produto_atual = self.listar_produtos[index]
            self.valor_unitario.setText(str(self.produto_atual[6]))
            print(self.produto_atual)

            
               
        
        
        except Exception as e:
            print('Deu erro! tela produto!')
            print(e)
        finally:
            conn.close()
                
                
 
        #Set o valor do campo valor unitário para o valor do produto atual.
        
            

    #Função de pegar um cliente.
    def pega_cliente(self, index):
       
            for x in self.lista_pega_dados_clientes:
                self.cliente_atual = x
            print(self.cliente_atual[index]) 
                
           
        
        
        

    def finalizar_venda(self):
        self.valor_pago = 0
        self.valor_pago = int(self.total_pago.text()) 
        valor_troco =  self.valor_pago - self.valor_total
        self.troco.setText(f'R$ {valor_troco}')
        valor_total_vendas = 0
        for x in self.lista_valores_venda:
            valor_total_vendas += x
        print(valor_total_vendas)


        
          
            
        #Pega os dados.
        #nome = self.cliente_atual[1]
        #email = self.cliente_atual[2]
        #O valor referente ao total da venda.
        #valor = self.valor_total
        #Adiciona uma venda no relatório.
        #nova_venda = Vendas(None,nome,email,valor)
        #funções_vendas.adicionar_vendas(nova_venda)
        #print(nova_venda.nome)
        
       
     

        
        
            
       
