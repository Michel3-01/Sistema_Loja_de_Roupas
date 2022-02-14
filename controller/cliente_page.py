from qt_core import *
from model.clientes import Clientes
import model.clientes_dao as funções_clientes
from model import database

#Variavel que contém o arquivo ui.
FILE_UI = 'view/cadastro_clientes.ui'

class CadClientes(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI,self)
        
        
        self.listar_clientes = funções_clientes.lista_clientes
        self.cliente_atual = None
        

        
        
        self.carrega_dados()
        #Evento dos botões.
        self.cancelar_btn.clicked.connect(self.fechar_janela)
        self.salvar_btn.clicked.connect(self.salvar)
        self.editar_btn.clicked.connect(self.editar)
        self.excluir_btn.clicked.connect(self.excluir)
    #Função de editar um cliente.
    def editar(self):
        pass
    #Função de excluir um cliente.
    def excluir(self):
        pass

    def fechar_janela(self):
        self.close()
    def salvar(self):
        #Pega os dados dos clientes.
        if self.nome.text == '' or self.email.text() == '' or self.telefone.text == '':
            self.alerta.setText('Preencha todos os campos!')
        else:
            nome = self.nome.text()
            email = self.email.text()
            telefone = self.telefone.text()
        
            #criar o objeto.
            cliente = Clientes(None,nome,email,telefone)
            funções_clientes.adicionar(cliente)


            self.carrega_dados()
            
        
        #Carrega os dados na minha tabela.
         
        #Pegar a lista de todos os clientes.
    def carrega_dados(self):
    
        try:
            
            conn = database.connect()#Conecta
            consulta_sql = "SELECT * FROM Clientes"
            cursor = conn.cursor()#Se move no banco
            cursor.execute(consulta_sql)
            linhas = cursor.fetchall()
        
            for cliente in linhas:
                self.add_linha(cliente)
                
                
            
        
        except Exception as e:
            print('Deu erro!')
            print(e)
        finally:
            conn.close()
        
        funções_clientes.listar_clientes()
        #Fechar a janela.
        #self.tabela_clientes.currentRow(self.pega_cliente)

        
        