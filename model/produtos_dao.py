#Centraliza o acesso a dados do objeto produto.
from model.produtos import Produtos
from model import database_produtos


lista = []
#Adicionar um produto.

def adicionar_prod(novo_produto):
    lista.append(novo_produto)
    try:
        conn = database_produtos.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Produtos (nome, tipo, genero, tamanho, quant_estoque, valor)
        VALUES (?,?,?,?,?,?);"""
        cursor.execute(sql, novo_produto.getProdutos())
        conn.commit()

    except Exception as e:
        print(e)
    
    finally:
        conn.close()
    

#Editar um produto.
def editar_prod(produto):
    try:
        conn = database_produtos.connect()
        cursor = conn.cursor()
        sql = """UPDATE Produtos SET nome=?, tipo=?, genero=?, tamanho=?, quant_estoque=?, valor=?;"""
        cursor.execute(sql,produto.getProdutos())
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()
    

#Excluir um produto.
def excluir_prod(id_produto):
    try:
        conn = database_produtos.connect()
        cursor = conn.cursor()
        sql = """DELETE FROM Produtos WHERE id = ?;"""
        cursor.execute(sql,[id])
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()
x = []
lista_produtos = []
def listar_produtos():
    lista = []
    try:
        conn = database_produtos.connect()
        cursor = conn.cursor()
        sql = "SELECT * FROM Produtos"
        cursor.execute(sql)
        linhas = cursor.fetchall()
        for produto in linhas:
            id = produto[0]
            nome = produto[1]
            tipo = produto[2]
            genero = produto[3]
            tamanho = produto[4]
            quant_estoque = produto[5]
            valor = produto[6]
            novo_produto = Produtos(id,nome,tipo,genero,tamanho,quant_estoque,valor)
            lista.append(novo_produto)
            for produto in linhas:
                x.append(produto)
            for produtos in x:
                lista_produtos.append(produtos)
                
            
    except Exception as e:
        print(e)
    finally:
        conn.close()
    print(type(x))
    return lista 
  

            
    
    
#Listar um produto específico.