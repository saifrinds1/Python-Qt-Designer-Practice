import serial
import sys

#
const_baudrate = 9600

#
def check_port(port):    
    try:
        s = serial.Serial(port)
        s.close()
        return True
    except(OSError, serial.SerialException):
        return False  

#
def close_ports():
    from glob import glob

    if sys.platform.startswith("win"):
        ports=[]
        for i in range(256):
            ports.append("COM{}".format(i))

    elif sys.platform.startswith("linux") or sys.platform.startswith('cygwin'):
        ports = glob('/dev/tty/[A-Za-z]*')# "glob('/dev/tty/[A-Za-z]*')" returns all ports

    elif sys.platform.startswith('darwin'):
        ports = glob('/dev/tty.*')

    else:
        raise EnvironmentError('platform "{}" is not supported!'.format(sys.platform))
            
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result            

#
class Connection:

    
    #
    def __init__(self, port=None, baudrate=None):
        self.serialPort = serial.Serial()
        if port is not None:
            self.set_port(port)
        if baudrate is not None:
            self.set_Baudrate(baudrate)

    #
    def connect(self, port=None, baudrate=None):
        if self.serialPort.is_open:
            self.serialPort.close()
        if port is not None:
            self.serialPort.setPort(port)
        if baudrate is not None:
            self.serialPort.baudrate=baudrate        
        if not check_port(self.serialPort.port):
            return False
        try:
            self.serialPort.open()
            return True
        except(OSError, serial.SerialException):
            return False    
            pass   

    #
    def send(self, Msg=""):
        try:
            self.serialPort.write(Msg)
            print(Msg)
            return True            
        except:
            return False
            pass
    
    #Read data from SerialPort
    def read(self):
        if self.isConnected():
            try:
                if self.serialPort.in_waiting>0:
                    a = self.serialPort.readline(self.serialPort.in_waiting)
                    return a
            except:
                pass    
        return None          
                
    #
    def disconnect(self):
        try:
            self.serialPort.close()
        except:
            pass             

    #
    def isConnected(self):
        return self.serialPort.is_open

    def isConnectedToPort(self):
        if self.isConnected():
            return self.get_port()
        else:
            return None

    #
    def get_Baudrate(self):
        return self.serialPort.baudrate

    #
    def set_Baudrate(self, baudrate):
        self.serialPort.baudrate = baudrate
        
    #    
    def get_port(self):
        if None is self.serialPort.port:
            return False
        else:
            return self.serialPort.port
    #
    def set_port(self, port):
        if check_port(port):
            self.serialPort.setPort(port)
            return True
        else:
            return False

