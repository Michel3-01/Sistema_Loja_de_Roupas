class Estoque():
    def __init__(self,id,nome_produto,quant_inicial,vendidos,quant_atual,situacao,id_estoque):
        self.id = id
        self.nome_produto = nome_produto
        self.quant_inicial = quant_inicial
        self.vendidos = vendidos
        self.quant_atual = quant_atual
        self.situacao = situacao
        self.id_estoque = id_estoque
    def getEstoque(self):
        return [self.nome_produto, self.quant_inicial, self.vendidos, self.quant_atual, self.situacao,self.id_estoque]
