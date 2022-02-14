class Vendas():
    def __init__(self,id,nome,email,valor):
        self.id = id
        self.nome = nome
        self.email = email
        self.valor = valor
    def getVendas(self):
        return [self.nome, self.email, self.valor]
    
    