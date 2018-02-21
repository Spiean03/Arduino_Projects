'''
@author: Andreas Spielhofer
'''


import matplotlib.pyplot as p
import numpy as n
import serial
from serial import SerialException
import os
import datetime
 
class Arduino:
    """This is a simple class which attempts to find an Arduino which has
the Geiger-339 sketch loaded.  It has two methods of interest:
    backlog() which returns number of bytes waiting to be read.
     
    getInterval() which returns a single interval measurement from the queue.
 
    """
    def __init__(self,debug = 2):
        """The debug parameter sets the debugging levels.  The following values are summed (or'd) together to form a value:
        1: debug connect
        2: display data as it is read
        For example, to display all debugging information, initialize the Arduino class with debug=3.
"""
        self.debug = debug
        if self.debug: print("Debugging output active")
        for index in range(10): # iterate over /dev/ttyACM0 to /dev/ttyACM9
            device = "/dev/ttyACM%d" % (index)
            try:
                st = os.stat(device)
            except OSError:
                continue
            if 1 & self.debug: print("Found a potential Arduino device at %s, going to try opening it" %(device))
            try:
                self.handle = serial.Serial(device,baudrate=115200)
            except SerialException:
                raise RuntimeError("Problem connecting to device! \n\nCheck that device is not open somewhere else\n(serial monitor?)")
            if 1 & self.debug: print("Device open!  Going to reboot it")
            for tries in range(5):
                self.handle.dtr = 0
                self.handle.dtr = 1
                if 1 & self.debug: print("Clearing I/O buffer")
                self.handle.timeout = 0
                resp = self.handle.read(1048756)
                if 1 & self.debug: print("Cleared %d bytes of junk" % (len(resp)))
                if 1 & self.debug: print("Waiting for wakeup")
                self.handle.timeout = 2;
                resp = self.handle.readline()
                if b"Geiger 2018\r\n" == resp:
                    if 1 & debug: print("got the expected response: ''%s'', returning initialized Arduino object"%(resp))
                    self.handle.timeout = 2000
                    return
                if 1 & self.debug: print("Unexpected response: ''%s'', going to retry..."%(resp))
            if 1 & self.debug: print("Giving up on device ''%s''"%(device))
        raise RuntimeError("No Geiger 2018 programmed device found")
     
    def getInterval(self):
        """Returns the duration of next interval between events in microseconds.  It may raise an exception if an overrun is detected.  An overrun happens when events arise to quickly and the Arduino cannot get data out fast enough to prevent data loss.
"""
        resp = self.handle.readline()
        if 2 & self.debug: print("read '%s'"%(resp))
        if b"\r\n" != resp[-2:]:
            if b"\r" == resp[-1:]: # stupid readline, do your job ... one @##$@ job!
                resp2 = self.handle.readline()
                if b"\n" != resp2:
                    raise RuntimeError("Incomplete line read")
                resp = resp + resp2
        if b"Overrun\r\n" == resp:
            raise RuntimeError("Arduino reports overrun")
        return int(resp)
 
    def backlog(self):
        """Returns the number of bytes which are waiting in the input queue.  This is important because if the Arduino is producing a great deal of data, even though the Arduino has faithfully sent all the data to the computer, the OS may toss the data if no one is picking it up at the same rate.
"""
        return self.handle.in_waiting
     
def plot_histogram(data):
    """
This is an ugly hack to make a realtime histogram, since I can find no way of making the matplotlib.pyplot.hist() update in realtime.
    data should be a vector of intervals, which will be analysed into a histogram.
"""
    counts,edges = n.histogram(data)
    nn = len(counts)
    x = n.zeros(3*nn+1)
    y = n.zeros(3*nn+1)
    for i in range(nn):
        x[3*i] = edges[i]
        y[3*i] = 0
        x[3*i+1] = edges[i]
        y[3*i+1] = counts[i]
        x[3*i+2] = edges[i+1]
        y[3*i+2] = counts[i]
        x[3*nn] = edges[nn]
        y[3*nn] = 0
    p.xlim(x.min(),x.max())
    p.ylim(0,y.max()+1)
    line.set_xdata(x)
    line.set_ydata(y)
    p.draw()
    p.pause(0.001)
         
arduino = Arduino(2)
 
'''******  THESE ARE THE ONLY VALUES YOU NEED TO CHANGE'''
N = 100         # number of intervals to be recorded
replicas = 2        # number of replicas to record
'''******                                           '''
 
 
 
intervals = n.ones((replicas,N)) # allocate space for interval measurements
 
graphics = 1   # set this to zero to suppress the display of the histogram
if graphics:
    p.ion()
    p.xlabel = "Interval between events (s)"
    p.ylabel = "Frequency"
    line, = p.plot(intervals[0,:])
     
for i in range(replicas):
    for interval in range(N):
        intervals[i,interval] = 1e-6*arduino.getInterval()
        # Only update the histogram if there is little risk
        # of the input buffer overflowing.
        if graphics and arduino.backlog() < 10:
            plot_histogram(intervals[i,:interval])
         
 
        #Save the file and close the serial device:
fileName = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + "_DWELL_TIME_DATA"
n.savetxt(fileName,intervals)
arduino.handle.close()
