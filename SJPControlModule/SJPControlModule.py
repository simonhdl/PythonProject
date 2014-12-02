import os
import serial
import time

from serial.tools import list_ports

# Define Global Variable
SJP_SerialNumber = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
DiscoveryLowerBond = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
DiscoveryUpperBond = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
FixtureDiscovered = []

def serial_ports():
    """
    Returns a generator for all available serial ports
    """
    if os.name == 'nt':
        # windows
        for i in range(256):
            try:
                s = serial.Serial(i)
                s.close()
                yield 'COM' + str(i + 1)
            except serial.SerialException:
                pass
    else:
        # unix
        for port in list_ports.comports():
            yield port[0]


def Send_DMX_Packet():
    """
    Send Channel Output
    """
    SJPDMXPacket = []
    SJPDMXPacketHeader = 0x7E
    SJPDMXPacketType = 0x06 # Label = 6  DMX Packet Type
    SJPDMXPacketLenLSB = 0x01 # 0x201 --- 513 Byte including Start Code 0x00
    SJPDMXPacketLenMSB = 0x02
    SJPDMXPacketStartCode = 0x00
    DMXMessage = []
    SJPDMXPacketEnder = 0xE7
    for j in range(512):
        DMXMessage.append(0x00)

    Channel = raw_input("INPUT CHANNEL: ")
    if Channel == '1' :
        DMXMessage[0] = 0xFF
        DMXMessage[1] = 0x00
        DMXMessage[2] = 0x00
    elif Channel == '2':
        DMXMessage[0] = 0x00
        DMXMessage[1] = 0xFF
        DMXMessage[2] = 0x00
    elif Channel == '3':
        DMXMessage[0] = 0x00
        DMXMessage[1] = 0x00
        DMXMessage[2] = 0xFF
        
    SJPDMXPacket.append(SJPDMXPacketHeader)
    SJPDMXPacket.append(SJPDMXPacketType)
    SJPDMXPacket.append(SJPDMXPacketLenLSB)
    SJPDMXPacket.append(SJPDMXPacketLenMSB)
    SJPDMXPacket.append(SJPDMXPacketStartCode)
    SJPDMXPacket +=DMXMessage
    SJPDMXPacket.append(SJPDMXPacketEnder)
    return SJPDMXPacket


def Send_DiscoverCMD(choose) :
    """
    Send Discovery Command/ Mute Command/ Un mute Command
    """
    if choose == 1 : # Send UN-MUTE Command
        SJPDMXPacket = []
        CheckSum = 0
        SJPDMXPacketHeader = 0x7E
        SJPDMXPacketType = 0x07 #Lable=11 Send RDM Discovery Request
        SJPDMXPacketLenLSB = 0x1A # Packet length 26
        SJPDMXPacketLenMSB = 0x00
        SJPDMXPacketStartCode = 0xCC # RDM Start Code 0xCC
        RDMMessage1 = [0x01, 0x18] # RDM packet length 24
        RDMDestination_ID = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF] # Destination UID
        RDMSource_ID = SJP_SerialNumber # Source UID
        RDMMessage2 = [0x00, 0x01, 0x00, 0x00, 0x00, 0x10, 0x00, 0x03] # RDM message
        RDMMessage3 = [0x00]
        RDMChecksum = []
        SJPDMXPacketEnder = 0xE7

        RDMPacket = RDMMessage1 + RDMDestination_ID + RDMSource_ID + RDMMessage2 + RDMMessage3
        for i in range(len(RDMPacket)):
            CheckSum += RDMPacket[i]
        CheckSum += SJPDMXPacketStartCode
        RDMChecksum = [CheckSum>>8 & 0xFF, CheckSum & 0xFF]
    
        SJPDMXPacket.append(SJPDMXPacketHeader)
        SJPDMXPacket.append(SJPDMXPacketType)
        SJPDMXPacket.append(SJPDMXPacketLenLSB)
        SJPDMXPacket.append(SJPDMXPacketLenMSB)
        SJPDMXPacket.append(SJPDMXPacketStartCode)
        SJPDMXPacket += (RDMMessage1 + RDMDestination_ID + RDMSource_ID + RDMMessage2 + RDMMessage3 + RDMChecksum)
        SJPDMXPacket.append(SJPDMXPacketEnder)
    
    elif choose == 2 : # Send DISCOVERY Command
        SJPDMXPacket = []
        CheckSum = 0
        SJPDMXPacketHeader = 0x7E
        SJPDMXPacketType = 0x0B #Lable=11 Send RDM Discovery Request
        SJPDMXPacketLenLSB = 0x26 # Packet Length 38
        SJPDMXPacketLenMSB = 0x00
        SJPDMXPacketStartCode = 0xCC
        RDMMessage1 = [0x01, 0x24]
        RDMDestination_ID = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        RDMSource_ID = SJP_SerialNumber
        RDMMessage2 = [0x01, 0x01, 0x00, 0x00, 0x00, 0x10, 0x00, 0x01]
        RDMMessage3 = [0x0C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF] # Length , lower bond and upper bond
        RDMChecksum = []
        SJPDMXPacketEnder = 0xE7

        RDMPacket = RDMMessage1 + RDMDestination_ID + RDMSource_ID + RDMMessage2 + RDMMessage3
        for i in range(len(RDMPacket)):
            CheckSum += RDMPacket[i]
        CheckSum += SJPDMXPacketStartCode
        RDMChecksum = [CheckSum>>8 & 0xFF, CheckSum & 0xFF]
    
        SJPDMXPacket.append(SJPDMXPacketHeader)
        SJPDMXPacket.append(SJPDMXPacketType)
        SJPDMXPacket.append(SJPDMXPacketLenLSB)
        SJPDMXPacket.append(SJPDMXPacketLenMSB)
        SJPDMXPacket.append(SJPDMXPacketStartCode)
        SJPDMXPacket += (RDMMessage1 + RDMDestination_ID + RDMSource_ID + RDMMessage2 + RDMMessage3 + RDMChecksum)
        SJPDMXPacket.append(SJPDMXPacketEnder)

    elif choose == 3: # Send MUTE Command
        SJPDMXPacket = []
        CheckSum = 0
        SJPDMXPacketHeader = 0x7E
        SJPDMXPacketType = 0x07 #Lable=11 Send RDM Discovery Request
        SJPDMXPacketLenLSB = 0x1A
        SJPDMXPacketLenMSB = 0x00
        SJPDMXPacketStartCode = 0xCC
        RDMMessage1 = [0x01, 0x18]
        RDMDestination_ID = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF] #
        RDMSource_ID = SJP_SerialNumber
        RDMMessage2 = [0x00, 0x01, 0x00, 0x00, 0x00, 0x10, 0x00, 0x02]
        RDMMessage3 = [0x00]
        RDMChecksum = []
        SJPDMXPacketEnder = 0xE7

        RDMPacket = RDMMessage1 + RDMDestination_ID + RDMSource_ID + RDMMessage2 + RDMMessage3
        for i in range(len(RDMPacket)):
            CheckSum += RDMPacket[i]
        CheckSum += SJPDMXPacketStartCode
        RDMChecksum = [CheckSum>>8 & 0xFF, CheckSum & 0xFF]
    
        SJPDMXPacket.append(SJPDMXPacketHeader)
        SJPDMXPacket.append(SJPDMXPacketType)
        SJPDMXPacket.append(SJPDMXPacketLenLSB)
        SJPDMXPacket.append(SJPDMXPacketLenMSB)
        SJPDMXPacket.append(SJPDMXPacketStartCode)
        SJPDMXPacket += (RDMMessage1 + RDMDestination_ID + RDMSource_ID + RDMMessage2 + RDMMessage3 + RDMChecksum)
        SJPDMXPacket.append(SJPDMXPacketEnder)
    
    return SJPDMXPacket

def Send_Get_SerialNumber() :
    """

    """
    SJPDMXPacket = []
    SJPDMXPacketHeader = 0x7E
    SJPDMXPacketType = 0x0A #Lable=10 Get widget serial number request
    SJPDMXPacketLenLSB = 0x00
    SJPDMXPacketLenMSB = 0x00
    SJPDMXPacketEnder = 0xE7

    SJPDMXPacket.append(SJPDMXPacketHeader)
    SJPDMXPacket.append(SJPDMXPacketType)
    SJPDMXPacket.append(SJPDMXPacketLenLSB)
    SJPDMXPacket.append(SJPDMXPacketLenMSB)
    SJPDMXPacket.append(SJPDMXPacketEnder)
                    
    return SJPDMXPacket

def Receive_Get_SerialNumber(s):
    global SJP_SerialNumber
    S = []
    SJP_SN = ""
    SJP_SerialNumber = [0x00, 0x00]
    for c in s:
        S.append(ord(c))
    for i in range(7,3,-1):
        if S[i]<10:
            A = str(hex(S[i]))
            SJP_SN +=  ('0'+A[2:3])
        else:
            A = str(hex(S[i]))
            SJP_SN += A[2:4]
        SJP_SerialNumber.append(S[i])
    return SJP_SN

def Handle_DiscoverPacket(s):
    """
    """
    S = []
    DiscRespond = []
    DiscoverdSN = []
    Checksum = 0
    for c in s:
        S.append(ord(c))
    if S[0]==126: # valid RDM Packet
        DiscRespond = S[5:29]
        for i in range(8,20):
            Checksum += DiscRespond[i]
        if ((Checksum>>8 | 0xAA)==DiscRespond[20])and((Checksum>>8 | 0x55)==DiscRespond[21])and((Checksum &0xFF | 0xAA)==DiscRespond[22])and((Checksum&0xFF | 0x55)==DiscRespond[23]) :
            for i in range(6):
                DiscoverdSN.append((DiscRespond[2*i + 8] & DiscRespond[2*i+1 + 8]))
            FixtureDiscovered.append(DiscoverdSN)
            print FixtureDiscovered
            return 1
        else:
            return 0

def DiscoveryProcess():
    pass



#################################################################################################
print "Available Serial Port: ", list(serial_ports())
ser = serial.Serial(4, timeout = 0.5)
print "Smart Jack Pro Serial Port: ", ser.name
ser.write(Send_Get_SerialNumber())
s=ser.read(50)
print "Smart Jack Pro Serial Number: ", Receive_Get_SerialNumber(s)
print SJP_SerialNumber


ser.write(Send_DiscoverCMD(1))
s=ser.read(100)



ser.write(Send_DiscoverCMD(2))
s=ser.read(100)

if(Handle_DiscoverPacket(s)==0):
    print "NOT MATCH"
ser.close()

    
