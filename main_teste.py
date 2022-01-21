from model.clientes import Clientes
import model.clientes_dao as funções_clientes

for i in range(0,10):
    novo_cliente = Clientes(i,f'Cliente{i}','@gmail.com','99666999')
    funções_clientes.adicionar(novo_cliente)

funções_clientes.listar_todos()

get_cliente = funções_clientes.pegar_cliente(7)
get_cliente.print()
get_cliente.nome = 'Michele da hora'
get_cliente.print()