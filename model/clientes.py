class Clientes():
    def __init__(self,id,nome,email,telefone):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
    def print(self):
        print(f'{self.id}, {self.nome}, {self.email}, {self.telefone}')