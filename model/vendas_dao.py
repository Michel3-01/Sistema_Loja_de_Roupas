#Centraliza o acesso a dados dos objeto venda.
import model.produtos_dao as funções_produtos
from model.produtos import Produtos

lista_vendas = []
#Adicionar uma nova venda.
def adicionar_vendas(nova_venda):
    id_atual = len(lista_vendas)+1
    nova_venda.id = id_atual
    lista_vendas.append(nova_venda)

#Editar uma venda.
def editar_venda(venda):
    for i in range(0,len(lista_vendas)):
        venda_atual = lista_vendas[i]
        if venda.id == venda_atual.id:
            lista_vendas[i] = venda


#Excluir uma venda.
def excluir_venda(id_venda):
    for i in range(0,len(lista_vendas)):
        venda_atual = lista_vendas[i]
        if id_venda == venda_atual.id:
            del venda_atual


#Lista todas as vendas.
def listar_vendas():
    for vendas in lista_vendas:
        vendas.print()

#Valor total da venda.
def pegar_valor_produto():
    for x in funções_produtos.lista_produtos:
        return x.valor

#Pegar o valor dos produtos.

lista_prod = funções_produtos.lista_produtos
valor_total = 0
def valor_total(self,produtos):
    valor_total = self.valor * self.quantidade 




    
    


#Lista venda específica.