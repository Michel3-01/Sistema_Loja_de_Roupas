#Padrão DAO (Data Access Object);
#Centraliza o acesso a dados dos objetos cliente.
from model import database

#Adicionar um cliente.
def adicionar(novo_cliente):
    try:
        conn = database.connect()#Conecta
        cursor = conn.cursor()#Se move no banco
        sql = """INSERT INTO Clientes (nome, email, telefone)
        VALUES (?,?,?);"""
        cursor.execute(sql, novo_cliente.getCliente())
        conn.commit()
    except Exception as e:
        print('Deu erro!')
        print(e)
    finally:
        conn.close()

def pegar_cliente(id_cliente):
    #percorre a lista de clientes:
    #for cliente in lista_clientes:
        #if cliente.id == id_cliente:
            #return cliente
            pass
#Editar um cliente.
#def editar(cliente):
    #for i in range(0,len(lista_clientes)):
        #cliente_atual = lista_clientes[i]
        #if cliente.id == cliente_atual.id:
            #lista_clientes[i] = cliente
#Excluir um cliente.
#def excluir(id_cliente):
    #for i in range(0,len(lista_clientes)):
        #cliente_atual = lista_clientes[i]
        #if id_cliente == cliente_atual.id:
            #del lista_clientes[i]

    
#Lista todos os clientes.
#def listar_todos():
    #for clientes in lista_clientes:
        #clientes.print()

#Pegar um cliente específico.