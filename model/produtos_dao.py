#Centraliza o acesso a dados do objeto produto.

lista_produtos = []
#Adicionar um produto.
def adicionar_prod(novo_produto):
    lista_produtos.append(novo_produto)

#Editar um produto.
def editar_prod(produto):
    for i in range(0,len(lista_produtos)):
        produto_atual = lista_produtos[i]
        if produto.id == produto_atual.id:
            produto_atual = produto

#Excluir um produto.
def excluir_prod(id_produto):
    for i in range(0,len(lista_produtos)):
        produto_atual = lista_produtos[i]
        if id_produto == produto_atual.id:
            del produto_atual


#Listar todos os produtos.
def listar_produtos():
    for produto in lista_produtos:
        produto.print()

#Listar um produto específico.