class Funcionarios():
    def __init__(self,id,nome_func, email_func,cargo_func):
        self.id = id
        self.nome_func = nome_func
        self.email_func = email_func
        self.cargo_func = cargo_func
    def getFuncionario(self):
        return [self.nome_func, self.email_func, self.cargo_func]