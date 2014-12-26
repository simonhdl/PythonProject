import os
import serial
import time
import PyQt4, PyQt4.QtGui, PyQt4.QtCore, sys
from serial.tools import list_ports
from PyQt4 import QtCore, QtGui


# Define Global Variable
SJP_SerialNumber = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00] # Store the connected Smart Jack Pro Serial number
FixtureDiscovered = [] # Store the Fixture SN which have been discover
FixtureSN = []
SearchRange = [[0x000000000000, 0xFFFFFFFFFFFF]] # Initial Search Range
global ser
global SJP_SN
global ComPort

def serial_ports(self):
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
    Payload = []
    SJPSendPacket(0x0A, Payload )

def Receive_Get_SerialNumber():
    global SJP_SerialNumber
    global SJP_SN
    
    try:
        s=ser.read(50)
    except serial.SerialException:
        pass
        
    if s=="" or len(list(s))<6: #invalid data
        return 0
    
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

def Open_SJP ():
    """
    Search each available com port for SJP, if SN read back positive, then connect to this com port as SJP.
    """
    global ser
    global SJP_SN
    global ComPort
    if os.name == 'nt':
        # windows
        for i in range(256):
            try:
                ser = serial.Serial(i, timeout = 0.05)
                ComPort = i
                Send_Get_SerialNumber()
                if(Receive_Get_SerialNumber()):
                    return 1
                ser.close()
                #print 'COM' + str(i + 1)
            except serial.SerialException:
                pass
    else:
        # unix
        for port in list_ports.comports():
            print port[0]
    return 0

def Close_SJP():
    """
    Close com port which attached to SJP
    """
    global ser
    ser.close()

def FastConnect():
    """
    Debug use. For un-handle connection exception
    """
    global ComPort
    global ser
    try:
        ser.close()
        time.sleep(0.5)
        ser = serial.Serial(ComPort, timeout = 0.05)
    except:
        pass

def Send_DMX_Packet (payload):
    """
    Send normal DMX512 packet to SJP
    """
    DMXPacket = [0x00]
    DMXPacket.extend(payload) 
    SJPSendPacket(0x06, DMXPacket)
    
def SJPSendPacket (type, payload):
    """
    Construct a Smart Jack pro packet and send out.
    """
    SJPPacket = []
    global ser
    SJPPacketHeader = 0x7E
    SJPPacketType = type
    SJPPacketLenLSB = (len(payload))&0xFF 
    SJPPacketLenMSB = (len(payload)>>8)&0xFF
    SJPPacketEnder = 0xE7
    
    SJPPacket.append(SJPPacketHeader)
    SJPPacket.append(SJPPacketType)
    SJPPacket.append(SJPPacketLenLSB)
    SJPPacket.append(SJPPacketLenMSB)
    if(len(payload)>0):
        SJPPacket += payload
    SJPPacket.append(SJPPacketEnder)
    #UART Send out the packet
    time.sleep(0.02) # need delay!! dont know why
    try:
        ser.write(SJPPacket)
    except NameError:
        pass
    #print SJPPacket
    
def Send_Unmute_Command ():
    """
    This is a BROADCAST command that every fixture on the bus will act. but not reply.
    """
    Payload = []
    CheckSum = 0
    RDMStartCode = [0xCC] # RDM Start Code 0xCC
    RDMMessage1 = [0x01, 0x18] # RDM packet length 24
    RDMDestination_ID = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF] # Destination UID, it is a broadcast command
    RDMSource_ID = SJP_SerialNumber # Source UID
    RDMMessage2 = [0x00, 0x01, 0x00, 0x00, 0x00, 0x10, 0x00, 0x03] # RDM message
    RDMMessage3 = [0x00]
    RDMChecksum = []
    RDMPacket = RDMStartCode + RDMMessage1 + RDMDestination_ID + RDMSource_ID + RDMMessage2 + RDMMessage3

    RDMChecksum = RDMCheckSumCalculate(RDMPacket)
    
    Payload = RDMPacket + RDMChecksum
    SJPSendPacket(0x07, Payload )
    
def Send_Mute_Command (TargetUID):
    """
    Input parameter: Tartget UID that will be muted.
    After mute, the fixture will not respond to any RDM command until reset.
    """
    Payload = []
    CheckSum = 0
    RDMStartCode = [0xCC] # RDM Start Code 0xCC
    RDMMessage1 = [0x01, 0x18] # RDM packet length 24
    RDMDestination_ID = TargetUID
    RDMSource_ID = SJP_SerialNumber # Source UID
    RDMMessage2 = [0x00, 0x01, 0x00, 0x00, 0x00, 0x10, 0x00, 0x02] # RDM message
    RDMMessage3 = [0x00]
    RDMChecksum = []
    RDMPacket = RDMStartCode + RDMMessage1 + RDMDestination_ID + RDMSource_ID + RDMMessage2 + RDMMessage3

    RDMChecksum = RDMCheckSumCalculate(RDMPacket)
    Payload = RDMPacket + RDMChecksum
    SJPSendPacket(0x07, Payload )

def Send_Discovery_Command (LowBond, UpBond):
    """
    Send Discovery Command between the given address range.
    The fixtures between this range will respond.
    """
    Payload = []
    CheckSum = 0
    RDMStartCode = [0xCC] # RDM Start Code 0xCC
    RDMMessage1 = [0x01, 0x24] # RDM packet length 24
    RDMDestination_ID = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
    RDMSource_ID = SJP_SerialNumber # Source UID
    RDMMessage2 = [0x01, 0x01, 0x00, 0x00, 0x00, 0x10, 0x00, 0x01]
    LBHex = [(LowBond>>40&0xFF), (LowBond>>32&0xFF), (LowBond>>24&0xFF), (LowBond>>16&0xFF), (LowBond>>8&0xFF), (LowBond&0xFF)]
    UBHex = [(UpBond>>40&0xFF), (UpBond>>32&0xFF), (UpBond>>24&0xFF), (UpBond>>16&0xFF), (UpBond>>8&0xFF), (UpBond&0xFF)]
    RDMMessage3 = [0x0C] + LBHex + UBHex
    RDMChecksum = []
    RDMPacket = RDMStartCode + RDMMessage1 + RDMDestination_ID + RDMSource_ID + RDMMessage2 + RDMMessage3

    RDMChecksum = RDMCheckSumCalculate(RDMPacket)
    Payload = RDMPacket + RDMChecksum
    SJPSendPacket(0x0B, Payload )

def Handle_DiscoverPacket():
    """
    Analyze the receive packet to check if it is a valid discover respond packet.
    If valid, then add the fixture SN into discover fixture list.
    """
    global FixtureDiscovered
    global ser
    
    try:
        s=ser.read(50)
    except NameError:
        return 0
    
    if s=='':
        return 0
    if (ord(s[0])==0x7E and ord(s[1])==0x0C) :
        return 0
    
    S = []
    DiscRespond = []
    DiscoverdSN = []
    Checksum = 0
    for c in s:
        S.append(ord(c))
    if (S[0]==126) and (S[2] > 24): # valid RDM Packet
        DiscRespond = S[5:29] # vaild Respcond packet
        #print DiscRespond
        for i in range(8,20):
            Checksum += DiscRespond[i]
        #valid singel respond packet (Check sum OK)
        if ((Checksum>>8 | 0xAA)==DiscRespond[20])and((Checksum>>8 | 0x55)==DiscRespond[21])and((Checksum &0xFF | 0xAA)==DiscRespond[22])and((Checksum&0xFF | 0x55)==DiscRespond[23]) :
            for i in range(6):
                DiscoverdSN.append((DiscRespond[2*i + 8] & DiscRespond[2*i+1 + 8]))
            FixtureDiscovered.append(DiscoverdSN)
            return 1 # Single Fixture
        else:
            return 2 # Multiple Fixture

def Process_Discovery ():
    """
    Algorithm for discovery process.
    """
    global SearchRange
    global FixtureDiscovered
    SearchRange = [[0x000000000000, 0xFFFFFFFFFFFF]] # Original Search Range
    FixtureDiscovered = [] # Fixture that discovered should be empty at the beginning 
    NoRespondRange = [] # Also record down the no fixture range.
    MultipleFlag = 0
    CompleteFlag = 0
    
    Send_Unmute_Command ()
    while CompleteFlag==0:
        # Remove the NoRespondRange in SearchRange, the process will not send discover packet in this range.
        for item in NoRespondRange:
            if(item in SearchRange):
                SearchRange.remove(item)
        NoRespondRange = [] # Empty the NoRespondRange
        for item in SearchRange:
            #print "Current Search Range is : ", item
            for i in range(32): # ??? One range search 32 times???
                time.sleep(0.05)
                Send_Discovery_Command(item[0],item[1]) # Select one range and send the discover command, then wait for feedback
                Result = Handle_DiscoverPacket()
                if( Result == 0 ):
                    #print "No Fixture in this range"
                    NoRespondRange.append(item)
                    CompleteFlag = 1
                    break
                elif ( Result == 1 ):
                    #print "One Fixture Found : ", FixtureDiscovered[-1]
                    Send_Mute_Command (FixtureDiscovered[-1])
                    CompleteFlag = 0 # not exit the loop because sometimes the response delay for different fixture is different. You need to search more than one time.
                elif ( Result == 2 ):
                    #print "Multiple Fixtures in this range"
                    MultipleFlag = 1
                    CompleteFlag = 0
                    break
            
            if MultipleFlag == 1:
                # Divide the Search Range and Update Search Range
                tempitem = [0,0]
                tempitem[0]=item[0]
                tempitem[1]=(item[0]+item[1])/2
                newitem = [ (item[0]+item[1])/2 +1, item[1] ]
                SearchRange.insert( SearchRange.index(item)+1, newitem)
                SearchRange[SearchRange.index(item)] = tempitem
                MultipleFlag = 0
                break # since we change the Search Range, we re-start the process.
    

def RDMCheckSumCalculate (payload):
    """
    Calculate the RDM packet Checksum.
    """
    CheckSum = 0
    CS = []
    for i in range(len(payload)):
        CheckSum += payload[i]
    CS = [CheckSum>>8 & 0xFF, CheckSum & 0xFF]
    return CS

def RDMCheckSumCheck (payload):
    """
    Verify the Checksum of the received RDM packet.
    """
    CheckSum = 0
    CS = []
    for i in range(len(payload)-2):
        CheckSum += payload[i]
    CS = [CheckSum>>8 & 0xFF, CheckSum & 0xFF]
    if(CS == payload[len(payload)-2: len(payload)]):
        return 1
    else:
        return 0

"""
PARAMETER ID LIST
0001 DISC_UNIQUE_BRANCH
0002 DISC_MUTE
0003 DISC_UNMUTE
0050 SUPPORTED_PARAMETERS
0051 PARAMETERS_DESCRIPTION
0060 DEVICE_INFO
0080 DEVICE_MODEL_DESCRIPTION
0081 MFG_LABEL
00C0 SOFTWARE_VERSION_LABEL
00F0 DMX_START_ADDRESS
1000 IDENTIFY_DEVICE
"""
def Send_RDM_GetCommand (TartgetUID, para, payload):
    """
    Get Command is to get the parameters from the fixture.
    """
    RDMPacket = []
    RDMStartCode = [0xCC]
    RDMSubStartCode = [0x01]
    RDMMsgLength = [0x00]
    RDMDestinationUID = TartgetUID
    RDMSourceUID = SJP_SerialNumber
    RDMTransNum = [0x00]
    RDMPortID = [0x00]
    RDMMsgCount = [0x01] # Must start from 0x01
    RDMSubDevice = [0x00, 0x00]
    RDMCmdClass = [0x20] # Get Command 0x20, GetCommand Respond 0x21
    RDMParaID = [0x00,0x00]
    RDMParaLength = [0x00]
    RDMParaData = payload
    RDMChecksum = [0x00, 0x00]

    RDMParaID = para
    
    RDMPacket = RDMStartCode + RDMSubStartCode + RDMMsgLength + RDMDestinationUID + RDMSourceUID \
                + RDMTransNum + RDMPortID + RDMMsgCount + RDMSubDevice + RDMCmdClass + RDMParaID + \
                RDMParaLength + RDMParaData
    RDMPacket[2] = len(RDMPacket)
    RDMChecksum = RDMCheckSumCalculate(RDMPacket)
    Payload = RDMPacket + RDMChecksum
    SJPSendPacket(0x07, Payload )

def Send_RDM_SetCommand (TartgetUID, para, payload):
    """
    Set Command is the command to set parameter to the fixture.
    """
    RDMPacket = []
    RDMStartCode = [0xCC]
    RDMSubStartCode = [0x01]
    RDMMsgLength = [0x00]
    RDMDestinationUID = TartgetUID
    RDMSourceUID = SJP_SerialNumber
    RDMTransNum = [0x00]
    RDMPortID = [0x00]
    RDMMsgCount = [0x00]
    RDMSubDevice = [0x00, 0x00]
    RDMCmdClass = [0x30] # Set Command 0x30, GetCommand Respond 0x31
    RDMParaID = [0x00,0x00]
    RDMParaLength = [0x00]
    RDMParaData = payload
    RDMChecksum = [0x00, 0x00]

    RDMParaID = para
    
    RDMPacket = RDMStartCode + RDMSubStartCode + RDMMsgLength + RDMDestinationUID + RDMSourceUID \
                + RDMTransNum + RDMPortID + RDMMsgCount + RDMSubDevice + RDMCmdClass + RDMParaID + \
                RDMParaLength + RDMParaData
    RDMPacket[2] = len(RDMPacket)
    RDMChecksum = RDMCheckSumCalculate(RDMPacket)
    Payload = RDMPacket + RDMChecksum
    SJPSendPacket(0x07, Payload )
    
def Handle_RDM_Command ():
    """
    Process the RDM received packet
    """
    try:
        s=ser.read(500)
    except :
        return 0
        
    # Is valid SJP Packet?
    if s=='' :
        return 0
    if (ord(s[0])==0x7E and ord(s[1])==0x0C) or (ord(s[1])!= 0x05) or (ord(s[0])!=0x7E and ord(s[-1])!=0xE7) or s=='':
        return 0
    if s==0:
        return 0
    S = []
    RDMPacket = []
    Checksum = 0
    RDMFlag = 0
    RDMCount = 0
    DataRecv = ''
    DatainStr = ''
    for c in s:
        S.append(ord(c))
    for item in S:
        if(item==0xCC):
            RDMFlag = 1
        if(RDMFlag==1):
            RDMPacket.append(item)
            RDMCount +=1
        if(len(RDMPacket)>2):
            if((RDMCount-2)==RDMPacket[2]):
                RDMFlag=0
                RDMCount=0
                break
    if RDMCheckSumCheck(RDMPacket):
        #print RDMPacket
        s = ""
        #print "Smart Jack Pro ID : ", RDMPacket[3:9]
        #print "Vaya Fixture ID : ", RDMPacket[9:15]
        #print RDMPacket
        if RDMPacket[20]==0x21 : # GET COMMAND
            #print "GET CMD : "
            #print "PARA ID : ", RDMPacket[21:23]
            #print "DATA : ", RDMPacket[24:24+RDMPacket[23]]
            DataRecv = RDMPacket[24:24+RDMPacket[23]]
            #for item in RDMPacket[24:24+RDMPacket[23]]:
            #    s +=chr(item) 
            #print "DATA in STRING : ", s
        elif RDMPacket[20]==0x31 : # SET COMMAND
            #print "SET CMD : "
            #print "PARA ID : ", RDMPacket[21:23]
            #print "DATA : ", RDMPacket[24:24+RDMPacket[23]]
            DataRecv = RDMPacket[24:24+RDMPacket[23]]
            #for item in RDMPacket[24:24+RDMPacket[23]]:
            #    s +=chr(item) 
            #print "DATA in STRING : ", s
        return DataRecv
    else:
        print "PACKET RECEIVE NG"

###################################################################
def RDM_Get_Supported_Para (TargetUID):
    """
    RDM command to get the fixture support parameter list.
    """
    para = [0x00, 0x50]
    payload = []
    Send_RDM_GetCommand(TargetUID, para, payload)
    Handle_RDM_Command()

###################################################################
def RDM_Get_Para_Description (TargetUID):
    """
    RDM command to get the fixture parameters description.
    """
    para = [0x00, 0x51]
    payload = []
    Send_RDM_GetCommand(TargetUID, para, payload)
    Handle_RDM_Command()

###################################################################
def RDM_Get_Device_Info (TargetUID):
    """
    RDM command to get the fixture device information.
    """
    para = [0x00, 0x60]
    payload = []
    Send_RDM_GetCommand(TargetUID, para, payload)
    return Handle_RDM_Command()

###################################################################
def RDM_Get_Device_Model_Description (TargetUID):
    """
    RDM command to get the fixture model description.
    """
    para = [0x00, 0x80]
    payload = []
    s = ""
    Send_RDM_GetCommand(TargetUID, para, payload)
    DataRev = Handle_RDM_Command()
    #print DataRev
    if DataRev ==0:
        return ''
    for item in DataRev:
        s +=chr(item)
    return s

###################################################################
def RDM_Get_Mfg_Label (TargetUID):
    """
    RDM command to get the fixture manufacturing label (Not use).
    """
    para = [0x00, 0x81]
    payload = []
    s = ""
    Send_RDM_GetCommand(TargetUID, para, payload)
    DataRev = Handle_RDM_Command()
    #print DataRev
    if DataRev ==0:
        return ''
    for item in DataRev:
        s +=chr(item)
    return s

###################################################################
def RDM_Get_Device_Label (TargetUID):
    """
    RDM command to get the fixture device label.
    """
    para = [0x00, 0x82]
    payload = []
    s = ""
    Send_RDM_GetCommand(TargetUID, para, payload)
    DataRev = Handle_RDM_Command()
    #print DataRev
    if DataRev ==0:
        return ''
    for item in DataRev:
        s +=chr(item)
    return s
    
###################################################################
def RDM_Get_Software_Version (TargetUID):
    """
    RDM command to get the fixture software version.
    """
    para = [0x00, 0xC0]
    payload = []
    s = ""
    Send_RDM_GetCommand(TargetUID, para, payload)
    DataRev = Handle_RDM_Command()
    for item in DataRev:
        s +=chr(item)
    return s
    
###################################################################
def RDM_Get_DMX_Start_Address (TargetUID):
    """
    RDM command to get the fixture DMX start address.
    """
    DataRev = ''
    FixtureAddr = 0
    para = [0x00, 0xF0]
    payload = []
    Send_RDM_GetCommand(TargetUID, para, payload)
    DataRev = Handle_RDM_Command()
    FixtureAddr = DataRev[0]<<8 | DataRev[1]
    return str(FixtureAddr)

###################################################################
def RDM_Get_UID (TargetUID):
    """
    RDM command to get the fixture UID (Serial Number).
    """
    DataRev = ''
    FixtureAddr = 0
    para = [0xA0, 0x01]
    payload = []
    Send_RDM_GetCommand(TargetUID, para, payload)
    DataRev = Handle_RDM_Command()
    #print DataRev
    return DataRev
    
###################################################################
def RDM_Get_Identify_Device (TargetUID):
    """
    RDM command to Get the fixture identify status.
    """
    para = [0x10, 0x00]
    payload = []
    Send_RDM_GetCommand(TargetUID, para, payload)
    Handle_RDM_Command()

###################################################################
def RDM_Set_Identify_Device (TargetUID, OnOff):
    """
    RDM command to tell fixture to identify itself.
    """
    para = [0x10, 0x00]
    payload = OnOff
    Send_RDM_SetCommand(TargetUID, para, payload)
    Handle_RDM_Command()

###################################################################
def RDM_Set_DMX_Start_Address (TargetUID, DMXStartAddress):
    """
    RDM command to set the fixture DMX start address.
    """
    para = [0x00, 0xF0]
    payload = DMXStartAddress
    Send_RDM_SetCommand(TargetUID, para, payload)
    Handle_RDM_Command()

###################################################################
def RDM_Set_NewUID (TargetUID, NewUID):
    """
    RDM command to set the fixture UID (Serial Number).
    """
    para = [0xA0, 0x00]
    payload = []
    Send_RDM_SetCommand(TargetUID, para, payload)
    time.sleep(0.05)
    para = [0xA0, 0x01]
    payload = NewUID
    Send_RDM_SetCommand(TargetUID, para, payload)
    Handle_RDM_Command()

###################################################################
def RDM_Set_Model_Description (TargetUID, NewModel):
    """
    RDM command to set the fixture model description.
    """
    para = [0x00, 0x80]
    payload = []
    payloadTemp = list(NewModel)
 
    for item in payloadTemp:
        #print item
        #QString -> QByteArray -> QChar -> int -> char -> hex ...... stupid!!
        DataTemp = ord(chr(PyQt4.QtCore.QChar(item.toAscii()).unicode()))
        #print DataTemp
        #payload.append((item.toAscii()).toHex())
        payload.append(DataTemp)
        #payload.append(ord(item))
    #print payload

    Send_RDM_SetCommand(TargetUID, para, payload)
    Handle_RDM_Command()

###################################################################
def RDM_Set_Device_Label (TargetUID, NewMfgLabel):
    """
    RDM command to set the fixture device label.
    """
    para = [0x00, 0x82]
    payload = []
    payloadTemp = list(NewMfgLabel)
    for item in payloadTemp:
        #print item
        #QString -> QByteArray -> QChar -> int -> char -> hex ...... stupid!!
        DataTemp = ord(chr(PyQt4.QtCore.QChar(item.toAscii()).unicode()))
        #print DataTemp
        #payload.append((item.toAscii()).toHex())
        payload.append(DataTemp)
        #payload.append(ord(item))
    #print payload

    Send_RDM_SetCommand(TargetUID, para, payload)
    Handle_RDM_Command()
####################################################################


def RDM_Set_NumOfOutput (TargetUID, Number):
    """
    RDM command to set the fixture UID (Serial Number).
    """
    para = [0xA0, 0x00]
    payload = []
    Send_RDM_SetCommand(TargetUID, para, payload)
    time.sleep(0.05)
    para = [0xA0, 0x0B]
    payload = [Number]
    Send_RDM_SetCommand(TargetUID, para, payload)
    Handle_RDM_Command()
    
###################################################################
def ConvertSN2ASCII (SN):
    """
    Small function to convert the fixture Serial number information to ascii code.
    """
    global FixtureSN
    FixtureSN = []
    for item in SN:
        tempSN = ''
        i=0
        for item2 in item:
            temp = hex(item2)
            i+=1
            if len(temp)==3:
                tempSN += '0'+temp[2:]
            else:
                tempSN += temp[2:]
            if i==2:
                tempSN += ':'
        FixtureSN.append(tempSN.upper())
            

def ConvertRDMVersion2ASCII (S):
    """
    Small function to convert the fixture RDM version information to ascii code.
    """
    i=0
    tempS = ''
    for item in S:
        temp = hex(item)
        i+=1
        if len(temp)==3:
            tempS += '0'+temp[2:]
        else:
            tempS += temp[2:]
        if i==1:
            tempS += '.'
    return tempS
    
def ConvertFootprint2ASCII (S):
    """
    Small function to convert the fixture footprint information to ascii code.
    """
    tempS = ''
    temp = hex(S)
    if len(temp)==3:
        tempS += '0'+temp[2:]
    else:
        tempS += temp[2:]
    return tempS



  
    
    
if __name__ == '__main__':
    
    print "Available Serial Port: ", list(serial_ports())
    ser = serial.Serial(4, timeout = 0.05)
    print "Smart Jack Pro Serial Port: ", ser.name
    Send_Get_SerialNumber()
    print "Smart Jack Pro Serial Number: ", Receive_Get_SerialNumber()
    print SJP_SerialNumber
    
    raw_input("Press Enter to Start Discover!")
    print "Discovery starts at ", time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    Status = Process_Discovery()

    for item in FixtureDiscovered:
        print FixtureDiscovered.index(item), ":" , item
        
    print "Discovery ends at ", time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    
    
    """
    raw_input("Press Enter to Start RDM!")
    TargetFixture = [0x50, 0x68, 0x15, 0x39, 0x89, 0x5A]
    print "\nREAD DEVICE INFO"
    RDM_Get_Device_Info(TargetFixture)
    print "\nREAD DEVICE MODEL"
    RDM_Get_Device_Model_Description(TargetFixture)
    print "\nREAD SOFTWARE VERSION"
    RDM_Get_Software_Version(TargetFixture)
    print "\nREAD SUPPORT PARA"
    RDM_Get_Supported_Para(TargetFixture)
    print "\nREAD PARA DESCRIPTION"
    RDM_Get_Para_Description(TargetFixture)
    print "\nREAD MANUFACTURING LABEL"
    RDM_Get_Mfg_Label(TargetFixture)
    print "\nREAD DMX START ADDRESS"
    RDM_Get_DMX_Start_Address(TargetFixture)

    #print "\nSET NEW UID"
    #RDM_Set_NewUID(TargetFixture, [0x50, 0x68, 0x15, 0x39, 0x89, 0x5A])
    print "\nSET NEW MODEL NAME"
    RDM_Set_Model_Description (TargetFixture, '0027_PHILIPS_BCP_SZ_RGB         ')
    """
    #RDM_Get_UID([0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])
    ser.close()
