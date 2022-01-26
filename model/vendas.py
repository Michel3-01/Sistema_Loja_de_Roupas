class Vendas():
    def __init__(self,id,lista_produto,valor,quantidade):
        self.lista_produto = lista_produto #Lista de produtos a serem comprados
        self.valor = valor
        self.quantidade = quantidade
    def print(self):
        print(f'{self.produto}, {self.valor}, {self.quantidade}')
    def valor_total(self):
        valor_total = 0
        for produto in self.lista_produto:
            valor_total += produto.valor
            return valor_total
    def valor_por_quant(self):
        valor_por_quant = 0
        for produto in self.lista_produto:
            valor_por_quant = produto.valor * self.quantidade