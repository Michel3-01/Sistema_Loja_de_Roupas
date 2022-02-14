#Classe que irá controlar as janelas.
from qt_core import *
from controller.main_window import MainWindow


app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec()