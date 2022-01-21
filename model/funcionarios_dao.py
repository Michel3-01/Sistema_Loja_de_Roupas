#Centraliza o acesso a dados dos objetos funcionários.

#Lista que armazena os dados dos funcionários.
lista_funcionarios = []
#Adicionar um funcionario.
def adicionar_func(novo_funcionario):
    lista_funcionarios.append(novo_funcionario)

#Editar funcionário.
def editar(func):
    for i in range(0,len(lista_funcionarios)):
        func_atual = lista_funcionarios[i] 
        if func.id == func_atual.id:
            lista_funcionarios[i] = func


#Excluir funcionário.
def excluir(id_func):
    for i in range(0,len(lista_funcionarios)):
        func_atual = lista_funcionarios[i]
        if id_func == func_atual.id:
            del lista_funcionarios[i]
            return


#Listar todos os funcionários.
def listar_todos():
    for func in lista_funcionarios:
        func.print()

#Pegar um cliente específico.
