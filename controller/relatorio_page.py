from qt_core import *
import model.vendas_dao as funções_vendas


FILE_UI='view/relatorio.ui'

class RelatorioPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)


        #Função do botão calcular.
        self.calcular_btn.clicked.connect(self.calcular_lucro_prejuizo)

        self.carrega_vendas()
    def carrega_vendas(self):


        lista = funções_vendas.listar_vendas()
        self.tabela_relatorio.setRowCount(0) #Zera as linhas da tabela.
        lista_valores_venda = []
        for vendas in lista:
            self.add_linha(vendas)
            lista_valores_venda.append(vendas.valor)
        self.valor_total_vendas = 0
        for x in lista_valores_venda:
                self.valor_total_vendas += x
               
        self.label_valor_total.setText(str(self.valor_total_vendas))
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
    
    def calcular_lucro_prejuizo(self):
        despesas = int(self.label_despesas.text())
        resultado = self.valor_total_vendas - despesas
        if resultado > 0:
            self.label_lucro_prejuizo.setText(f"A empresa teve lucro de R$:{resultado}")
            self.label_lucro_prejuizo.setStyleSheet("color: green; background-color: black; font-size: 35px")
        elif resultado == 0:
            self.label_lucro_prejuizo.setText(f"A empresa não teve lucros nem prejuizo de R$:{resultado}")
            self.label_lucro_prejuizo.setStyleSheet("color: white; background-color: black; font-size: 35px")
        else:
            self.label_lucro_prejuizo.setText(f"A empresa teve prejuizo de R$:{resultado * (-1)}")
            self.label_lucro_prejuizo.setStyleSheet("color: red; background-color: black; font-size: 35px")
            
         
      
            