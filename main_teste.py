from model.clientes import Clientes
import model.clientes_dao as funções_clientes
from model.produtos import Produtos
from model.vendas import Vendas
import model.vendas_dao as funções_vendas

def carrega_dados(self):
    for i in range(0,10):
        novo_cliente = Clientes(i,f'Cliente{i}','@gmail.com','99666999')
        funções_clientes.adicionar(novo_cliente)

funções_clientes.listar_todos()

#get_cliente = funções_clientes.pegar_cliente(7)
#get_cliente.print()
#get_cliente.nome = 'Michele da hora'
#get_cliente.print()

produto1 = Produtos(0,'pasta',2.8,'higienico','x',3)
produto2 = Produtos(0,'pasta',3,'higienico','x',3)
lista_de_produtos = [produto1,produto2]
venda01 = Vendas(0,lista_de_produtos,None,3)

venda01.funções_vendas.valor_total()
