from qt_core import *
import model.vendas_dao as funções_vendas


FILE_UI='view/relatorio.ui'

class RelatorioPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.carrega_vendas()
    def carrega_vendas(self):


        lista = funções_vendas.listar_vendas()
        self.tabela_relatorio.setRowCount(0) #Zera as linhas da tabela.
        lista_valores_venda = []
        for vendas in lista:
            self.add_linha(vendas)
            lista_valores_venda.append(vendas.valor)
        valor_total_vendas = 0
        for x in lista_valores_venda:
                valor_total_vendas += x
               
        self.label_valor_total.setText(str(valor_total_vendas))
        self.label_quantidade.setText(str(len(lista_valores_venda)))

    def add_linha(self, vendas):
        rowCount = self.tabela_relatorio.rowCount()
        self.tabela_relatorio.insertRow(rowCount)

        #Elemento de cada coluna da tabela.
        id = QTableWidgetItem(str(vendas.id))
        nome = QTableWidgetItem(vendas.nome)
        email = QTableWidgetItem(vendas.email)
        valor = QTableWidgetItem(str(vendas.valor))

        #Insere os elementos nas colunas correspondentes.
        self.tabela_relatorio.setItem(rowCount,0,id)
        self.tabela_relatorio.setItem(rowCount,1,nome)
        self.tabela_relatorio.setItem(rowCount,2,email)
        self.tabela_relatorio.setItem(rowCount,3,valor)
         
      
            