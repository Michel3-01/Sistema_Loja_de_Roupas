from model import database_estoque
from model.estoque import Estoque

lista = []

def adicionar(estoque):
    lista.append(estoque)
    try:
        conn = database_estoque.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Estoque (nomeProd, quant_inicial, vendidos, quant_atual, situacao, id_produto)
        VALUES (?,?,?,?,?,?);"""
        cursor.execute(sql,estoque.getEstoque())
        conn.commit()

    except Exception as e:
        print(e)
    
    finally:
        conn.close()



def listar_estoque():
    lista = []
    try:
        conn = database_estoque.connect()
        cursor = conn.cursor()
        sql = "SELECT * FROM Estoque;"
        cursor.execute(sql)
        linhas = cursor.fetchall()
        for estoque in linhas:
            id = estoque[0]
            nome_produto = estoque[1]
            quant_incial = estoque[2]
            vendidos = estoque[3]
            quant_atual = estoque[4]
            situacao = estoque[5]
            id_estoque = estoque[6]
            
            
            estoque = Estoque(id,nome_produto, quant_incial, vendidos, quant_atual, situacao,id_estoque)
            lista.append(estoque)

            

    except Exception as e:
        print(e)
    finally:
        conn.close()
    return lista 


def editar(estoque):
    try:
        conn = database_estoque.connect()
        cursor = conn.cursor()
        sql = """UPDATE Estoque SET nomeProd=?,  quant_inicial=?,  vendidos=?,  quant_atual=? situacao=?, id_produto=?;"""
        cursor.execute(sql, estoque.getEstoque())
        conn.commit()

    except Exception as e:
        print(e)

    finally:
        conn.close()