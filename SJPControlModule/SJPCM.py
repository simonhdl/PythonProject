"""
This is for Smart Jack Pro Module
And 
"""
import os
import serial
import time

from serial.tools import list_ports

# Define Global Variable
SJP_SerialNumber = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00] # Store the connected Smart Jack Pro Serial number
FixtureDiscovered = [] # Store the Fixture SN which have been discover
SearchRange = [[0x000000000000, 0xFFFFFFFFFFFF]] # Initial Search Range

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

def Send_Get_SerialNumber() :
    """
    Send Command to SJP to get the SJP serial number
    """
    SJPPacket = []
    SJPPacketHeader = 0x7E
    SJPPacketType = 0x0A #Lable=10 Get widget serial number request
    SJPPacketLenLSB = 0x00
    SJPPacketLenMSB = 0x00
    SJPPacketEnder = 0xE7

    SJPPacket.append(SJPPacketHeader)
    SJPPacket.append(SJPPacketType)
    SJPPacket.append(SJPPacketLenLSB)
    SJPPacket.append(SJPPacketLenMSB)
    SJPPacket.append(SJPPacketEnder)
    #UART Send out the packet
    ser.write(SJPPacket)  
    return SJPPacket

def Receive_Get_SerialNumber():
    global SJP_SerialNumber
    s=ser.read(50)
    S = []
    SJP_SerialNumber = [0x00, 0x00] # SJP return 4bytes, but UID contain 6 bytes, so we add 2 bytes ahead
    SJP_SN = ""
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

def Send_Unmute_Command ():
    """
    This is a broadcase command that every fixture on the bus will act. but not reply
    """
    SJPPacket = []
    CheckSum = 0
    SJPPacketHeader = 0x7E
    SJPPacketType = 0x07 #Lable=11 Send RDM Discovery Request
    SJPPacketLenLSB = 0x1A # Packet length 26
    SJPPacketLenMSB = 0x00
    SJPPacketStartCode = 0xCC # RDM Start Code 0xCC
    RDMMessage1 = [0x01, 0x18] # RDM packet length 24
    RDMDestination_ID = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF] # Destination UID, it is a broadcast command
    RDMSource_ID = SJP_SerialNumber # Source UID
    RDMMessage2 = [0x00, 0x01, 0x00, 0x00, 0x00, 0x10, 0x00, 0x03] # RDM message
    RDMMessage3 = [0x00]
    RDMChecksum = []
    SJPPacketEnder = 0xE7

    RDMPacket = RDMMessage1 + RDMDestination_ID + RDMSource_ID + RDMMessage2 + RDMMessage3
    #Calculate the Checksum
    for i in range(len(RDMPacket)):
        CheckSum += RDMPacket[i]
    CheckSum += SJPPacketStartCode
    RDMChecksum = [CheckSum>>8 & 0xFF, CheckSum & 0xFF]
    
    SJPPacket.append(SJPPacketHeader)
    SJPPacket.append(SJPPacketType)
    SJPPacket.append(SJPPacketLenLSB)
    SJPPacket.append(SJPPacketLenMSB)
    SJPPacket.append(SJPPacketStartCode)
    SJPPacket += (RDMMessage1 + RDMDestination_ID + RDMSource_ID + RDMMessage2 + RDMMessage3 + RDMChecksum)
    SJPPacket.append(SJPPacketEnder)
    #UART Send out the packet
    time.sleep(0.05) # need delay!! dont know why
    ser.write(SJPPacket)


def Send_Mute_Command (TargetUID):
    """
    Input parameter: Tartget UID that will be muted.
    """
    SJPPacket = []
    CheckSum = 0
    SJPPacketHeader = 0x7E
    SJPPacketType = 0x07 #Lable=11 Send RDM Discovery Request
    SJPPacketLenLSB = 0x1A
    SJPPacketLenMSB = 0x00
    SJPPacketStartCode = 0xCC
    RDMMessage1 = [0x01, 0x18]
    RDMDestination_ID = TargetUID #
    RDMSource_ID = SJP_SerialNumber
    RDMMessage2 = [0x00, 0x01, 0x00, 0x00, 0x00, 0x10, 0x00, 0x02]
    RDMMessage3 = [0x00]
    RDMChecksum = []
    SJPPacketEnder = 0xE7

    RDMPacket = RDMMessage1 + RDMDestination_ID + RDMSource_ID + RDMMessage2 + RDMMessage3
    for i in range(len(RDMPacket)):
        CheckSum += RDMPacket[i]
    CheckSum += SJPPacketStartCode
    RDMChecksum = [CheckSum>>8 & 0xFF, CheckSum & 0xFF]
    
    SJPPacket.append(SJPPacketHeader)
    SJPPacket.append(SJPPacketType)
    SJPPacket.append(SJPPacketLenLSB)
    SJPPacket.append(SJPPacketLenMSB)
    SJPPacket.append(SJPPacketStartCode)
    SJPPacket += (RDMMessage1 + RDMDestination_ID + RDMSource_ID + RDMMessage2 + RDMMessage3 + RDMChecksum)
    SJPPacket.append(SJPPacketEnder)
    #UART Send out the packet
    time.sleep(0.05) # need delay!! dont know why
    ser.write(SJPPacket)

def Send_Discovery_Command (LowBond, UpBond):
    """

    """
    SJPPacket = []
    CheckSum = 0
    SJPPacketHeader = 0x7E
    SJPPacketType = 0x0B #Lable=11 Send RDM Discovery Request
    SJPPacketLenLSB = 0x26 # Packet Length 38
    SJPPacketLenMSB = 0x00
    SJPPacketStartCode = 0xCC
    RDMMessage1 = [0x01, 0x24]
    RDMDestination_ID = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
    RDMSource_ID = SJP_SerialNumber
    RDMMessage2 = [0x01, 0x01, 0x00, 0x00, 0x00, 0x10, 0x00, 0x01]
    LBHex = [(LowBond>>40&0xFF), (LowBond>>32&0xFF), (LowBond>>24&0xFF), (LowBond>>16&0xFF), (LowBond>>8&0xFF), (LowBond&0xFF)]
    UBHex = [(UpBond>>40&0xFF), (UpBond>>32&0xFF), (UpBond>>24&0xFF), (UpBond>>16&0xFF), (UpBond>>8&0xFF), (UpBond&0xFF)]
    #RDMMessage3 = [0x0C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF] # Length , lower bond and upper bond
    RDMMessage3 = [0x0C] + LBHex + UBHex
    RDMChecksum = []
    SJPPacketEnder = 0xE7

    RDMPacket = RDMMessage1 + RDMDestination_ID + RDMSource_ID + RDMMessage2 + RDMMessage3
    for i in range(len(RDMPacket)):
        CheckSum += RDMPacket[i]
    CheckSum += SJPPacketStartCode
    RDMChecksum = [CheckSum>>8 & 0xFF, CheckSum & 0xFF]
    
    SJPPacket.append(SJPPacketHeader)
    SJPPacket.append(SJPPacketType)
    SJPPacket.append(SJPPacketLenLSB)
    SJPPacket.append(SJPPacketLenMSB)
    SJPPacket.append(SJPPacketStartCode)
    SJPPacket += (RDMMessage1 + RDMDestination_ID + RDMSource_ID + RDMMessage2 + RDMMessage3 + RDMChecksum)
    SJPPacket.append(SJPPacketEnder)
    #UART Send out the packet
    time.sleep(0.01) # need delay!! dont know why
    ser.write(SJPPacket)


def Handle_DiscoverPacket():
    """
    """
    global FixtureDiscovered
    s=ser.read(50)
    if (ord(s[0])==0x7E and ord(s[1])==0x0C) :
        return 0
    
    S = []
    DiscRespond = []
    DiscoverdSN = []
    Checksum = 0
    for c in s:
        S.append(ord(c))
    if S[0]==126: # valid RDM Packet
        DiscRespond = S[5:29]
        #print DiscRespond
        for i in range(8,20):
            Checksum += DiscRespond[i]
        if ((Checksum>>8 | 0xAA)==DiscRespond[20])and((Checksum>>8 | 0x55)==DiscRespond[21])and((Checksum &0xFF | 0xAA)==DiscRespond[22])and((Checksum&0xFF | 0x55)==DiscRespond[23]) :
            for i in range(6):
                DiscoverdSN.append((DiscRespond[2*i + 8] & DiscRespond[2*i+1 + 8]))
            FixtureDiscovered.append(DiscoverdSN)
            return 1
        else:
            return 2

def Process_Discovery ():
    """

    """
    global SearchRange
    global FixtureDiscovered
    NoRespondRange = []
    MultipleFlag = 0
    CompleteFlag = 0
    Send_Unmute_Command ()
    
    while CompleteFlag==0:
        #print "All Search Range is : ", SearchRange
        for item in NoRespondRange:
            if(item in SearchRange):
                SearchRange.remove(item)
        NoRespondRange = []
        for item in SearchRange:
            #print "Current Search Range is : ", item
            for i in range(32):
                #time.sleep(0.1)
                Send_Discovery_Command(item[0],item[1])
                
                Result = Handle_DiscoverPacket()
                if( Result == 0 ):
                    #print "No Fixture in this range"
                    NoRespondRange.append(item)
                    CompleteFlag = 1
                    break
                elif ( Result == 1 ):
                    #print "One Fixture Found : ", FixtureDiscovered[-1]
                    Send_Mute_Command (FixtureDiscovered[-1])
                    CompleteFlag = 0
                elif ( Result == 2 ):
                    #print "Multiple Fixtures in this range"
                    MultipleFlag = 1
                    CompleteFlag = 0
                    break
            if MultipleFlag == 1:
                # Update Search Range
                tempitem = [0,0]
                tempitem[0]=item[0]
                tempitem[1]=(item[0]+item[1])/2
                newitem = [ (item[0]+item[1])/2 +1, item[1] ]
                SearchRange.insert( SearchRange.index(item)+1, newitem)
                SearchRange[SearchRange.index(item)] = tempitem
                MultipleFlag = 0
                
                break
            
"""
if __name__ == '__main__':
    
    print "Available Serial Port: ", list(serial_ports())
    ser = serial.Serial(4, timeout = 0.05)
    print "Smart Jack Pro Serial Port: ", ser.name
    Send_Get_SerialNumber()
    print "Smart Jack Pro Serial Number: ", Receive_Get_SerialNumber()
    print SJP_SerialNumber
    raw_input("Press Enter to Start Discover!")
    Status = Process_Discovery()
    print FixtureDiscovered
    ser.close()
"""
