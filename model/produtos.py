class Produtos():
    def __init__(self,id, nome_prod, tipo_prod, genero,tamanho, quant_estoque, valor_prod):
        self.id = id
        self.nome_prod = nome_prod
        self.tipo_prod = tipo_prod
        self.genero = genero
        self.tamanho = tamanho
        self.quant_estoque = quant_estoque
        #self.excluir = excluir
        self.valor_prod = valor_prod
    def getProdutos(self):
       return [self.nome_prod, self.tipo_prod, self.genero, self.tamanho , self.quant_estoque, self.valor_prod]
    def getNome(self):
        return [self.nome_prod]
        