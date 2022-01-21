class Funcionarios():
    def __init__(self,id,nome_func,cargo_func):
        self.id = id
        self.nome_func = nome_func
        self.cargo_func = cargo_func
    def print(self):
        print(f'{self.id}, {self.nome_func}, {self.cargo_func}')