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

#Editar um cliente.
def editar(cliente):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """UPDATE Clientes SET nome=?,email=?,telefone=? WHERE id = ?;"""
        l = cliente.getCliente()
        l.append(cliente.id)
        cursor.execute(sql,l)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()
#Excluir um cliente.
def excluir(id_cliente):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """DELETE FROM Clientes WHERE id = ?;"""
        cursor.execute(sql,[id_cliente])
        conn.commit()

    except Exception as e:
        print(e)
    finally:
        conn.close()
    
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
            

            novo_cliente = Clientes(id, nome, email, telefone)
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
lista_02 = []
def pega_dados_clientes():
    lista_01 = []
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
           

            novo_cliente = Clientes(id, nome, email, telefone)
            lista_01.append(novo_cliente)
            for x in lista_01:
                lista_02.append(x)
                print(x)
           
    except Exception as e:
        print(e)
    finally:
        conn.close()
    print(lista_01)
    print(lista_02)
    