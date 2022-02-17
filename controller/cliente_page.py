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
            cliente = Clientes(None,nome, email, telefone,excluir=0)
            funções_clientes.adicionar(cliente)


            
        
        #Carrega os dados na minha tabela.
         
        #Pegar a lista de todos os clientes.
    
      

        
        