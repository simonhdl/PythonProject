from SJPCM import serial_ports
print "Available Serial Port: ", list(serial_ports())

class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print self.data

x = FirstClass()
x.setdata("ADV")

x.display()
