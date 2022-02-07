class Vendas():
    def __init__(self,id,nome,email,valor):
        self.id = id
        self.valor = nome
        self.email = email
        self.valor = valor
    def valor_total_vendas(self):
        valor_total_vendas = 0
        for produto in self.lista_valores_venda:
            valor_total_vendas += produto
            print(valor_total_vendas)
    