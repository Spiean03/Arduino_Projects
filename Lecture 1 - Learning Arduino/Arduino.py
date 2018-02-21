# -*- coding: utf-8 -*-
"""
@author: Andreas Spielhofer
"""

import serial

class Arduino:
    def __init__(self,debug=False):
        """ Initializes the Arduino. The routine is as follows:
            - scans the computer for available ports and returns a list of available ports
            - tries to connect to every port and is looking for the right response from the port.
              If the response is "Arduino2018" from the port, it knows that this is the Arduino you are looking for
              If the response is not "Arduino2018", it goes goes to the next port and tries to connect
        """
        self.debug = debug
        self.scan()
        for port in self.available_ports:
            device = port
            try:
                self.device = serial.Serial(device,baudrate=115200,timeout=0.5)
                if self.debug:
                    print "Try to connect to %s..." % (device)  
                attempts = 0
                for i in range(5):
                    try:
                        if self.getResp() == "Arduino2018":
                            print '\rGot Response: "Arduino2018".\nArduino is connected to %s \r\n' % (device)
                            return
                        attempts = attempts + 1
                    except:
                       attempts = attempts + 1
                if attempts ==5:
                    self.device.close()
                    if self.debug:
                        print "Unable to communicate to port %s. Seems this is not the Arduino you are looking for.\r\n" % (device)
#                   exit
#                break
            except:
                continue
                
    def scan(self):
        """scan for available ports. return a list of the available ports"""
        print "Scanning available ports..."
        self.available_ports = []
        for i in range(256):
            port = "COM%d" %(i)
            try:
                s = serial.Serial(port)
                self.available_ports.append(s.portstr)
                s.close()   # explicit close 'cause of delayed GC in java
            except serial.SerialException:
                pass
        if self.debug:
            print "Ports available: %s" %(self.available_ports)
        return self.available_ports
            
    def serial_open(self):
        """opens the serial port"""
        if self.device.is_open == False:
            self.device.open()
            attempts = 0
            for i in range(5):
                try:
                    if self.getResp() == "Arduino2018":
                        print 'Got Response: "Arduino2018". Connected to %s' % (self.device.port)
                        return
                    attempts = attempts + 1
                except:
                   attempts = attempts + 1
            print "Attempts to communicate = %s" %(attempts)
            if attempts ==5:
                self.device.close()
                print "Unable to communicate to port %s \r\n" % (self.device.port)
        elif self.device.is_open == True:
            print "%s to Arduino is already open." %(self.device.port) 
        else:
            print "Seems there is an issue with opening the port..."               
        
    def serial_close(self):
        """closes the serial port"""
        if self.device.is_open == False:
            print "%s to Arduino is already closed." %(self.device.port)
        elif self.device.is_open == True:
            self.device.close()
            print "%s to Arduino is closed." %(self.device.port)
        else:
            print "Seems there is an issue with closing the port..."
                   
    def send(self,str):
        self.device.write(str+"\n")
        
    def getResp(self):
        str = self.device.readline()
        str = str.replace("\n","")
        str = str.replace("\r","")
        return str

        
a = Arduino() 
a.send('Hello.')
response = a.getResp()
print response

a.send("What is your name?")
response = a.getResp()
print response

a.send("How old are you?")
response = a.getResp()
print response

a.send("bye")
response = a.getResp()
print response