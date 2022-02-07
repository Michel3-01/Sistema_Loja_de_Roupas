#Padrão DAO (Data Access Object);
#Centraliza o acesso a dados dos objetos cliente.
from model import database
from model.clientes import Clientes

lista_de_clientes = []
#Adicionar um cliente.
def adicionar(novo_cliente):
    lista_de_clientes.append(novo_cliente)
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

#def pegar_cliente(id_cliente):
    #percorre a lista de clientes:
    #for cliente in lista_clientes:
        #if cliente.id == id_cliente:
            #return cliente
            #pass
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


lista_clientes = []
x = []
def listar_clientes():
    lista = []
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = "SELECT * FROM Clientes"
        cursor.execute(sql)
        linhas = cursor.fetchall()
        for cliente in linhas:
            #Pega as informações dos clientes.
            id = cliente[0]
            nome = cliente[1]
            email = cliente[2]
            telefone = cliente[3]
            excluir = cliente[4]

            novo_cliente = Clientes(id, nome, email, telefone,excluir)
            lista.append(novo_cliente)
            for cliente in linhas:
                x.append(cliente) 
            for clientes in x:
                lista_clientes.append(clientes) 

    except Exception as e:
        print(e)
    finally:
        conn.close()
    

#Pegar um cliente específico.