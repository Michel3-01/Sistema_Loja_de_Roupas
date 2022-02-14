#Centraliza o acesso a dados dos objeto venda.
from model import database_vendas
from model.vendas import Vendas



lista_vendas = []
#Adicionar uma nova venda.
def adicionar_vendas(nova_venda):
    lista_vendas.append(nova_venda)
    try:
        conn = database_vendas.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Vendas (nome, email, valor)
        VALUES (?,?,?);"""
        cursor.execute(sql, nova_venda.getVendas())
        conn.commit()

    except Exception as e:
        print(e)
    finally:
        conn.close()



"""#Editar uma venda.
def editar_venda(venda):
    for i in range(0,len(lista_vendas)):
        venda_atual = lista_vendas[i]
        if venda.id == venda_atual.id:
            lista_vendas[i] = venda


#Excluir uma venda.
def excluir_venda(id_venda):
    for i in range(0,len(lista_vendas)):
        venda_atual = lista_vendas[i]
        if id_venda == venda_atual.id:
            del venda_atual"""


#Lista todas as vendas.
def listar_vendas():
    lista = []
    try:
        conn = database_vendas.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM Vendas"""
        cursor.execute(sql)
        conn.commit()
        linhas = cursor.fetchall()
        #salvar os dados.
        for venda in linhas:
            id = venda[0]
            nome = venda[1]
            email = venda[2]
            valor = venda[3]
            nova_venda = Vendas(id, nome, email, valor)
            lista.append(nova_venda)

    except Exception as e:
        print(e)
    finally:
        conn.close()
    return lista
    

"""#Valor total da venda.
def pegar_valor_produto():
    for x in funções_produtos.lista_produtos:
        return x.valor

#Pegar o valor dos produtos.

lista_prod = funções_produtos.lista_produtos
valor_total = 0
def valor_total(self,produtos):
    valor_total = self.valor * self.quantidade"""



    
    


#Lista venda específica.