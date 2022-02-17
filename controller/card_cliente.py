from qt_core import *
from assets.color import getColor
import model.clientes_dao as funções_clientes

FILE_UI='view/card_cliente.ui'

class CardCliente(QWidget):
    def __init__(self,cliente, janela_cliente):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.cliente = cliente
        self.janela_cliente = janela_cliente

        #Funções dos botões.
        self.editar_btn.clicked.connect(self.editar)
        self.excluir_btn.clicked.connect(self.excluir)

        self.label_id.setText(str(cliente.id))
        self.label_nome.setText(cliente.nome)
        self.label_email.setText(cliente.email)
        self.label_telefone.setText(cliente.telefone)


        #cor = getColor()
        style_sheet = f'border: 1px double black; border-radius: 10px; background-color:rgb(25, 0, 77); color:white; font-size: 15px; text-align:center;' 

        self.label_nome.setStyleSheet(style_sheet)
        self.label_id.setStyleSheet('border: 1px dotted black; background-color:rgb(148, 77, 255); color:white; font-size:15px;')
        self.label_email.setStyleSheet('font-size: 18px; color: white;')
        self.label_telefone.setStyleSheet('font-size: 18px; color: white;')
     
    def editar(self):
        self.janela_cliente.show_tela_edicao_cliente(self.cliente)
    def excluir(self):
        id = self.cliente.id
        funções_clientes.excluir(id)
        funções_clientes.update_excluir(self.cliente.id, excluir=1)

        self.janela_cliente.show_clientes_page()


  

        