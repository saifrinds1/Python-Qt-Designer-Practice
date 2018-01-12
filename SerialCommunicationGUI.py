# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SerialCommunicationGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SerialCommunicationWindow(object):
    def setupUi(self, SerialCommunicationWindow):
        SerialCommunicationWindow.setObjectName("SerialCommunicationWindow")
        SerialCommunicationWindow.setWindowModality(QtCore.Qt.WindowModal)
        SerialCommunicationWindow.setEnabled(True)
        SerialCommunicationWindow.resize(452, 401)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SerialCommunicationWindow.sizePolicy().hasHeightForWidth())
        SerialCommunicationWindow.setSizePolicy(sizePolicy)
        SerialCommunicationWindow.setMinimumSize(QtCore.QSize(260, 260))
        SerialCommunicationWindow.setMaximumSize(QtCore.QSize(8000, 6000))
        SerialCommunicationWindow.setSizeIncrement(QtCore.QSize(1, 1))
        SerialCommunicationWindow.setWindowTitle("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Pictures/serial-port-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SerialCommunicationWindow.setWindowIcon(icon)
        SerialCommunicationWindow.setAutoFillBackground(False)
        SerialCommunicationWindow.setIconSize(QtCore.QSize(96, 48))
        SerialCommunicationWindow.setDocumentMode(False)
        SerialCommunicationWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        SerialCommunicationWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(SerialCommunicationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 451, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(True)
        self.comboBox.setEditable(False)
        self.comboBox.setMaxVisibleItems(15)
        self.comboBox.setMaxCount(1000)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.refresh = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refresh.sizePolicy().hasHeightForWidth())
        self.refresh.setSizePolicy(sizePolicy)
        self.refresh.setObjectName("refresh")
        self.horizontalLayout_3.addWidget(self.refresh)
        self.btnConnect = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnConnect.sizePolicy().hasHeightForWidth())
        self.btnConnect.setSizePolicy(sizePolicy)
        self.btnConnect.setIconSize(QtCore.QSize(0, 0))
        self.btnConnect.setObjectName("btnConnect")
        self.horizontalLayout_3.addWidget(self.btnConnect)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setMaximumSize(QtCore.QSize(8000, 6000))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.btnClear = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnClear.setObjectName("btnClear")
        self.horizontalLayout_4.addWidget(self.btnClear)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.etxtMsg = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.etxtMsg.sizePolicy().hasHeightForWidth())
        self.etxtMsg.setSizePolicy(sizePolicy)
        self.etxtMsg.setInputMask("")
        self.etxtMsg.setText("")
        self.etxtMsg.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.etxtMsg.setObjectName("etxtMsg")
        self.horizontalLayout.addWidget(self.etxtMsg)
        self.btnSend = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSend.sizePolicy().hasHeightForWidth())
        self.btnSend.setSizePolicy(sizePolicy)
        self.btnSend.setObjectName("btnSend")
        self.horizontalLayout.addWidget(self.btnSend)
        self.verticalLayout.addLayout(self.horizontalLayout)
        SerialCommunicationWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SerialCommunicationWindow)
        QtCore.QMetaObject.connectSlotsByName(SerialCommunicationWindow)

    def retranslateUi(self, SerialCommunicationWindow):
        _translate = QtCore.QCoreApplication.translate
        self.refresh.setText(_translate("SerialCommunicationWindow", "Search Ports"))
        self.btnConnect.setText(_translate("SerialCommunicationWindow", "Connect"))
        self.label.setText(_translate("SerialCommunicationWindow", "Disconnected"))
        self.btnClear.setText(_translate("SerialCommunicationWindow", "Clear"))
        self.btnSend.setText(_translate("SerialCommunicationWindow", "Send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SerialCommunicationWindow = QtWidgets.QMainWindow()
    ui = Ui_SerialCommunicationWindow()
    ui.setupUi(SerialCommunicationWindow)
    SerialCommunicationWindow.show()
    sys.exit(app.exec_())

