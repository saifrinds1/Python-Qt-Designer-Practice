import SerialCommunicationGUI
from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort
import sys
import glob
import serial

#serialPort Initialize 
serialPort = serial.Serial()
serialPort.baudrate = 9600

#Return available serialPorts
def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

#Connect Button Function
def ConnectButtonClicked():
    if ConnectWithPort(serialPort, MainWindowGUI.comboBox.currentText()):
        print("Connected")
        MainWindowGUI.btnSend.setEnabled(True)
        MainWindowGUI.etxtMsg.setEnabled(True)
    else:
        print("Could Not Connected")
        MainWindowGUI.btnSend.setEnabled(False)
        MainWindowGUI.etxtMsg.setEnabled(False)
        pass    
        


#Connect SerialPort with Port
def ConnectWithPort(Serial_Port, PortName):
    if Serial_Port.is_open:
        Serial_Port.close()
    try:
        serialPort.setPort(PortName)
        Serial_Port.open()
        return True
        print("Connected")
    except (OSError , serial.SerialException):
        print(serial.SerialException)
        return False
        pass

#Send Message to SerialPort
def SendMsgWithPort(Serial_Port, Msg):
    try:
        Serial_Port.write(Msg.encode())
        print(Msg)
        return True            
    except:
        return False
        pass        

#Send Button Function    
def SendButtonClicked():
    if SendMsgWithPort(serialPort , MainWindowGUI.etxtMsg.text()):
        MainWindowGUI.listWidget.addItem(MainWindowGUI.etxtMsg.text())
        MainWindowGUI.etxtMsg.clear()
        print("Send")

#comboBox Update Function
def ComboBoxUpdate():
    MainWindowGUI.comboBox.clear()
    MainWindowGUI.comboBox.addItems(serial_ports())
    

#Intialize GUI
application = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindowGUI = SerialCommunicationGUI.Ui_MainWindow()
MainWindowGUI.setupUi(MainWindow)
MainWindowGUI.btnConnect.clicked.connect(ConnectButtonClicked)
MainWindowGUI.btnSend.clicked.connect(SendButtonClicked)
MainWindowGUI.refresh.clicked.connect(ComboBoxUpdate)
MainWindowGUI.btnSend.setEnabled(False)
MainWindowGUI.etxtMsg.setEnabled(False)
MainWindow.show()
sys.exit(application.exec_())