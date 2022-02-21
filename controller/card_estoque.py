from qt_core import *
import model.estoque_dao as funções_estoque
import model.produtos_dao as funções_produtos


FILE_UI = 'view/card_estoque.ui'

class CardEstoque(QWidget):
    def __init__(self,produto):
        super().__init__()
        uic.loadUi(FILE_UI,self)
        
        self.produto = produto
        self.label_id.setText(str(self.produto.id))
        self.label_nome.setText(self.produto.nome_prod)
        self.label_quant_inicial.setText(str(self.produto.quant_estoque))

        x = []
        for estoque in funções_estoque.listar_estoque():
            if self.produto.id == estoque.id_estoque:
                x.append(estoque.vendidos)
                total = 0
                for y in x:
                    total = total + y
                    rq = self.produto.quant_estoque - total #rq guarda o valor da quantidade de produtos atual.
                    if rq <= 100:
                        estoque.situacao = 'Vermelho'
                        self.label_situacao.setStyleSheet('font-size: 22px; color: red;')
                    elif rq > 800:
                        estoque.situacao = 'Verde'
                        self.label_situacao.setStyleSheet('font-size: 22px; color: rgb(0, 255, 0);')
                    else:
                        estoque.situacao = 'Normal'
                        self.label_situacao.setStyleSheet('font-size: 22px; color: white;')


                    self.label_quant_atual.setText(str(rq))
                    self.label_situacao.setText(estoque.situacao)
                    self.label_vendidos.setText(str(total))
        



    
        """for estoque in funções_estoque.listar_estoque():
            x = 0
            if self.produto.id == estoque.id_estoque:
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
                    self.label_situacao.setText(estoque.situacao)"""
                   
  
        


        #StyleSheet.
        self.label_nome.setStyleSheet('border: 1px double black; border-radius: 10px; background-color:rgb(25, 0, 77); color:white; font-size: 15px; text-align:center;')
        self.label_id.setStyleSheet('border: 1px dotted black; background-color:rgb(148, 77, 255); color:white; font-size:15px;')
        self.label_quant_inicial.setStyleSheet('font-size: 18px; color: white;')
        self.label_vendidos.setStyleSheet('font-size: 18px; color: white;')
        self.label_quant_atual.setStyleSheet('font-size: 18px; color: white;')
     
       