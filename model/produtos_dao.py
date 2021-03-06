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
        sql = """INSERT INTO Produtos (nome, tipo, genero, tamanho, quant_estoque, valor, excluir)
        VALUES (?,?,?,?,?,?,0);"""
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
        sql = """UPDATE Produtos SET nome=?, tipo=?, genero=?, tamanho=?, quant_estoque=?, valor=? WHERE id = ?;"""
        l = produto.getProdutos()
        l.append(produto.id)
        cursor.execute(sql,l)
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
        cursor.execute(sql,[id_produto])
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def listar_produtos():
    lista = []
    try:
        conn = database_produtos.connect()
        cursor = conn.cursor()
        sql = "SELECT * FROM Produtos WHERE excluir=0;"
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
            excluir = produto[7]
            novo_produto = Produtos(id,nome,tipo,genero,tamanho,quant_estoque,valor,excluir)
            lista.append(novo_produto)
            

    except Exception as e:
        print(e)
    finally:
        conn.close()
    return lista 
  
#Listar um produto espec??fico.
def pesquisar_prod(nome_produto):
    lista_prod_pesquisa = []
    try:
        conn = database_produtos.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM Produtos WHERE nome=?;"""
        cursor.execute(sql,nome_produto)
        linha = cursor.fetchall()
        conn.commit()
        for x in linha:
           lista_prod_pesquisa.append(x)
           print(x)
    except Exception as e:
        print(e)
    finally:
        conn.close()
