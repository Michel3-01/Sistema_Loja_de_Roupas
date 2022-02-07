class Clientes():
    def __init__(self,id,nome,email,telefone,excluir=0):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.excluir = excluir
    def getCliente(self):
        return [self.nome, self.email, self.telefone]