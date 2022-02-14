from qt_core import *
from assets.color import getColor

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


        cor = getColor()
        style_sheet = f'border: 1px solid black; border-radius: 10px; background-color: {cor};' 

        self.label_nome.setStyleSheet(style_sheet)
    def editar(self):
        self.janela_cliente.show_tela_edicao_cliente(self.cliente)
    def excluir(self):
        pass