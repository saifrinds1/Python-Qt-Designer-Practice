import MyFirstGUI
from PyQt5 import QtCore, QtGui, QtWidgets
import sys



def ConnectClicked(self):
    print("Connect Clicked")

def SendClicked(self):
    print("Send Clicked")    

app=QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = MyFirstGUI.Ui_MainWindow()
ui.setupUi(MainWindow)
ui.btnConnect.clicked.connect(ConnectClicked)
ui.btnSend.clicked.connect(SendClicked)

MainWindow.show()
sys.exit(app.exec_())

