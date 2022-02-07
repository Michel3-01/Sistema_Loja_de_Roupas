from qt_core import *
from model.clientes import Clientes
import model.clientes_dao as funções_clientes
from model import database

#Variavel que contém o arquivo ui.
FILE_UI = 'view/cadastro_clientes.ui'

class ClientePage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI,self)
        
        
        self.listar_clientes = []
        

        
        
        self.carrega_dados()
        #Evento dos botões.
        self.cancelar_btn.clicked.connect(self.fechar_janela)
        self.salvar_btn.clicked.connect(self.salvar)

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
        
        #Zera a tabela e reconstroi.
        self.tabela_clientes.setRowCount(0) #Zera as linhas da tabela.
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
        
        
        #Fechar a janela.
        
    def add_linha(self,cliente):
        rowCount = self.tabela_clientes.rowCount()
        self.tabela_clientes.insertRow(rowCount)

        #Elementos de cada coluna da tabela.
        id = QTableWidgetItem(str(cliente[0]))
        nome = QTableWidgetItem(cliente[1])
        email =QTableWidgetItem(cliente[2])
        telefone = QTableWidgetItem(cliente[3])

        #Insere os elementos da tabela na coluna correspondente.
        self.tabela_clientes.setItem(rowCount, 0 , id)
        self.tabela_clientes.setItem(rowCount, 1 , nome)
        self.tabela_clientes.setItem(rowCount, 2 , email)
        self.tabela_clientes.setItem(rowCount, 3 , telefone)