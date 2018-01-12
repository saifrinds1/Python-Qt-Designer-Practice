import SerialCommunicationGUI
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import glob
import SerialMethods
from threading import Thread
from time import sleep

serialConnection = SerialMethods.Connection(baudrate=9600)


def threaded():
    while True:
        sleep(.001)
        MainWindowGUI.label.setText('Connected to {}'.format(serialConnection.isConnectedToPort()))
        recv = serialConnection.read()
        if  recv is not None:
            MainWindowGUI.listWidget.addItem("rx:{}".format(recv.decode()))
            MainWindowGUI.listWidget.scrollToBottom()
        
#Connect Button Function
def ConnectButtonClicked():
    if serialConnection.connect(MainWindowGUI.comboBox.currentText()):
        MainWindowGUI.btnSend.setEnabled(True)
        MainWindowGUI.etxtMsg.setEnabled(True)
    else:
        MainWindowGUI.btnSend.setEnabled(False)
        MainWindowGUI.etxtMsg.setEnabled(False)
        pass            

#Send Button Function    
def SendButtonClicked():
    if serialConnection.send(MainWindowGUI.etxtMsg.text().encode()):
        MainWindowGUI.listWidget.addItem("tx:{}".format(MainWindowGUI.etxtMsg.text()))
        MainWindowGUI.etxtMsg.clear()
        MainWindowGUI.listWidget.scrollToBottom()
        print("Send")

#comboBox Update Function
def ComboBoxUpdate():
    MainWindowGUI.comboBox.clear()
    MainWindowGUI.comboBox.addItems(SerialMethods.close_ports())

#Adjust layout when the window is resized
def layoutAdjust():
    print("Hello layout")

#Clear the monitor
def clearMonitor():
    MainWindowGUI.listWidget.clear()

#Intialize GUI
application = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindowGUI = SerialCommunicationGUI.Ui_SerialCommunicationWindow()
MainWindowGUI.setupUi(MainWindow)
MainWindowGUI.btnConnect.clicked.connect(ConnectButtonClicked)
MainWindowGUI.btnSend.clicked.connect(SendButtonClicked)
MainWindowGUI.refresh.clicked.connect(ComboBoxUpdate)
MainWindowGUI.etxtMsg.returnPressed.connect(SendButtonClicked)
MainWindowGUI.btnClear.clicked.connect(clearMonitor)
MainWindowGUI.listWidget.setAutoScroll(True)
MainWindowGUI.btnSend.setEnabled(False)
MainWindowGUI.etxtMsg.setEnabled(False)
MainWindow.show()

#Initiallizing thread for recieve of data from serialPort
threadRead = Thread(target=threaded ,name="Read")
threadRead.start()

sys.exit(application.exec_())