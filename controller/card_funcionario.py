from qt_core import *
import model.funcionarios_dao as funções_funcionarios

FILE_UI = 'view/card_funcionario.ui'

class CardFuncionario(QWidget):
    def __init__(self, funcionario,janela_funcionario):
        super().__init__()
        uic.loadUi(FILE_UI,self)

        self.janela_funcionario = janela_funcionario
        self.funcionario = funcionario
        #StyleSheet dos labels.
        self.label_id.setStyleSheet('border: 1px dotted black; background-color:rgb(148, 77, 255); color:white; font-size:15px;')
        self.label_nome.setStyleSheet('border: 1px double black; border-radius: 10px; background-color:rgb(25, 0, 77); color:white; font-size: 15px; text-align:center;')
        self.label_email.setStyleSheet('font-size: 18px; color: white;')
        self.label_cargo.setStyleSheet('font-size: 18px; color: white;')
        #Valores dos labels.
        self.label_id.setText(str(funcionario.id))
        self.label_nome.setText(funcionario.nome_func)
        self.label_email.setText(funcionario.email_func)
        self.label_cargo.setText(funcionario.cargo_func)

        self.editar_btn.clicked.connect(self.editar)
        self.excluir_btn.clicked.connect(self.excluir)



    def excluir(self):
        id = self.funcionario.id
        print(id)
        funções_funcionarios.excluir(id)

        self.janela_funcionario.show_funcionarios_page()


    def editar(self):
        self.janela_funcionario.show_tela_edicao_func(self.funcionario)

        
