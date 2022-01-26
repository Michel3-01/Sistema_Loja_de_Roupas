#Padrão DAO (Data Access Object);
#Centraliza o acesso a dados dos objetos cliente.

#Lista que armazena as informações clientes.
lista_clientes = []
#Adicionar um cliente.
def adicionar(novo_cliente):
    #Inserir o Id do cliente.
    novo_id = len(lista_clientes)+1
    novo_cliente.id = novo_id
    lista_clientes.append(novo_cliente)

def pegar_cliente(id_cliente):
    #percorre a lista de clientes:
    for cliente in lista_clientes:
        if cliente.id == id_cliente:
            return cliente
#Editar um cliente.
def editar(cliente):
    for i in range(0,len(lista_clientes)):
        cliente_atual = lista_clientes[i]
        if cliente.id == cliente_atual.id:
            lista_clientes[i] = cliente
#Excluir um cliente.
def excluir(id_cliente):
    for i in range(0,len(lista_clientes)):
        cliente_atual = lista_clientes[i]
        if id_cliente == cliente_atual.id:
            del lista_clientes[i]

    
#Lista todos os clientes.
def listar_todos():
    for clientes in lista_clientes:
        clientes.print()

#Pegar um cliente específico.