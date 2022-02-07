#Centraliza o acesso a dados dos objetos funcionários.
from model import database_funcionarios
from model.funcionarios import Funcionarios




#Adicionar um funcionario.
def adicionar_func(novo_funcionario):
    try:
        conn = database_funcionarios.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Funcionarios (nome, email, cargo)
        VALUES (?,?,?);"""
        cursor.execute(sql, novo_funcionario.getFuncionario())
        conn.commit()

    except Exception as e:
        print(e)

    finally:
        conn.close()
    
   
#Editar funcionário.
def editar(func):
    try:
        conn = database_funcionarios.connect()
        cursor = conn.cursor()
        sql = """UPDATE Funcionarios SET nome=?, email=?, cargo=?;"""
        cursor.execute(sql, func.getFuncionario())
        conn.commit()

    except Exception as e:
        print(e)

    finally:
        conn.close()

#Excluir funcionário.
def excluir(id_func):
    try:
        conn = database_funcionarios.connect()
        cursor = conn.cursor()
        sql = """DELETE FROM Funcionarios WHERE id=?;"""
        cursor.execute(sql,[id])
        conn.commit()

    except Exception as e:
        print(e)

    finally:
        conn.close()

#Listar todos os funcionários.
def listar_todos():
    lista = []
    try:
        conn = database_funcionarios.connect()
        cursor = conn.cursor()
        sql = "SELECT * FROM Funcionarios"
        cursor.execute(sql)
        result = cursor.fetchall()
        for x in result:
            novo_func = Funcionarios(x[1],x[2],x[3],x[4],x[5],x[6],x[7])
            lista.append(novo_func)
            

    except Exception as e:
        print(e)
    finally:
        conn.close()
    
    


