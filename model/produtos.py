class Produtos():
    def __init__(self,id,nome_prod,tipo_prod,genero,tamanho):
        self.id = id
        self.nome_prod = nome_prod
        self.tipo_prod = tipo_prod
        self.genero = genero
        self.tamanho = tamanho
    def print(self):
        print(f'{self.id}, {self.nome_prod}, {self.tipo_prod},{self.genero}, {self.tamanho}')
        