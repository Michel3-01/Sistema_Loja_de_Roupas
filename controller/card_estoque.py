from qt_core import *
import model.estoque_dao as funções_estoque


FILE_UI = 'view/card_estoque.ui'

class CardEstoque(QWidget):
    def __init__(self,produto,estoque):
        super().__init__()
        uic.loadUi(FILE_UI,self)
        self.estoque = estoque
        self.produto = produto
        self.label_id.setText(str(self.produto.id))
        self.label_nome.setText(self.produto.nome_prod)
        self.label_quant_inicial.setText(str(self.produto.quant_estoque))


        

    
        if self.produto.id == estoque.id_estoque:
            if estoque.quant_atual < 0:
                self.label_quant_atual.setText('0')
            else:
                x = 0
                for estoque in funções_estoque.listar_estoque():
                    x = x - estoque.vendidos
                    estoque.quant_atual = self.produto.quant_estoque +(x)
                    self.label_quant_atual.setText(str(estoque.quant_atual))
                    estoque.vendidos = self.produto.quant_estoque - estoque.quant_atual
                    self.label_vendidos.setText(str(estoque.vendidos))
                    if estoque.quant_atual <= 100:
                        estoque.situacao = 'Vermelho'
                    elif estoque.quant_atual >= 500:
                        estoque.situacao = 'Verde'
                    else:
                        estoque.situacao = 'Normal'
                    self.label_situacao.setText(estoque.situacao)
                   
                  
        else:
            self.label_vendidos.setText('0')
            self.label_situacao.setText('Normal')
            self.label_quant_atual.setText('0')
            
        


        #StyleSheet.
        self.label_nome.setStyleSheet('border: 1px double black; border-radius: 10px; background-color:rgb(25, 0, 77); color:white; font-size: 15px; text-align:center;')
        self.label_id.setStyleSheet('border: 1px dotted black; background-color:rgb(148, 77, 255); color:white; font-size:15px;')