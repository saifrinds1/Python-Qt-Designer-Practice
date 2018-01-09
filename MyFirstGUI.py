# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyFirstGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(391, 289)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Pictures/serial-port-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QtCore.QSize(96, 48))
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnConnect = QtWidgets.QPushButton(self.centralwidget)
        self.btnConnect.setGeometry(QtCore.QRect(12, 9, 75, 23))
        self.btnConnect.setObjectName("btnConnect")
        self.etxtSerialPortName = QtWidgets.QLineEdit(self.centralwidget)
        self.etxtSerialPortName.setGeometry(QtCore.QRect(92, 10, 113, 20))
        self.etxtSerialPortName.setInputMask("")
        self.etxtSerialPortName.setText("")
        self.etxtSerialPortName.setEchoMode(QtWidgets.QLineEdit.NoEcho)
        self.etxtSerialPortName.setObjectName("etxtSerialPortName")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 40, 371, 191))
        self.listView.setObjectName("listView")
        self.btnSend = QtWidgets.QPushButton(self.centralwidget)
        self.btnSend.setGeometry(QtCore.QRect(307, 239, 75, 23))
        self.btnSend.setObjectName("btnSend")
        self.etxtMsg = QtWidgets.QLineEdit(self.centralwidget)
        self.etxtMsg.setGeometry(QtCore.QRect(10, 240, 291, 20))
        self.etxtMsg.setInputMask("")
        self.etxtMsg.setText("")
        self.etxtMsg.setEchoMode(QtWidgets.QLineEdit.NoEcho)
        self.etxtMsg.setObjectName("etxtMsg")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 391, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSEND = QtWidgets.QAction(MainWindow)
        self.actionSEND.setObjectName("actionSEND")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnConnect.setText(_translate("MainWindow", "Connect"))
        self.btnSend.setText(_translate("MainWindow", "Send"))
        self.actionSEND.setText(_translate("MainWindow", "SEND"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

