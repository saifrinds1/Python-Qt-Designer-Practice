# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SerialCommunicationGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(210, 242)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowTitle("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Pictures/serial-port-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QtCore.QSize(96, 48))
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnConnect = QtWidgets.QPushButton(self.centralwidget)
        self.btnConnect.setGeometry(QtCore.QRect(135, 5, 70, 25))
        self.btnConnect.setIconSize(QtCore.QSize(0, 0))
        self.btnConnect.setObjectName("btnConnect")
        self.btnSend = QtWidgets.QPushButton(self.centralwidget)
        self.btnSend.setGeometry(QtCore.QRect(135, 190, 70, 25))
        self.btnSend.setObjectName("btnSend")
        self.etxtMsg = QtWidgets.QLineEdit(self.centralwidget)
        self.etxtMsg.setGeometry(QtCore.QRect(5, 190, 125, 25))
        self.etxtMsg.setInputMask("")
        self.etxtMsg.setText("")
        self.etxtMsg.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.etxtMsg.setObjectName("etxtMsg")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(5, 35, 200, 150))
        self.listWidget.setObjectName("listWidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(5, 5, 90, 25))
        self.comboBox.setObjectName("comboBox")
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(100, 5, 30, 25))
        self.refresh.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Pictures/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh.setIcon(icon1)
        self.refresh.setObjectName("refresh")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 210, 21))
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
        self.btnConnect.setText(_translate("MainWindow", "Connect"))
        self.btnSend.setText(_translate("MainWindow", "Send"))
        self.actionSEND.setText(_translate("MainWindow", "SEND"))

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
"""
