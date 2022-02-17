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
        sql = """INSERT INTO Clientes (nome, email, telefone,excluir)
        VALUES (?,?,?,0);"""
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


def update_excluir(id, excluir):
    # atualiza contato

    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """UPDATE Contatos SET excluir=? WHERE id=?;"""
        cursor.execute(sql, [excluir, id])
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
        sql = "SELECT * FROM Clientes WHERE excluir = 0;"
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

    except Exception as e:
        print(e)
    finally:
        conn.close()
    return lista 
    
    

#Pegar um cliente específico.

    