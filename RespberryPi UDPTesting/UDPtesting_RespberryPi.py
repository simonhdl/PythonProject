import socket
import string
import time
import os,sys

#os.system('netsh int ip set address name="LSE" source=static addr=10.1.3.100 mask=255.0.0.0')

MESSAGE = ""
MESSAGE_Q = []
MESSAGE_QC = []
#############################################################################################################################
UDP_IP = "10.255.255.255"	#Broadcast IP address
UDP_PORT = 6038#UDP Port for Kinet
MAGIC_NUM = [ 0x04, 0x01, 0xDC, 0x4A ]#Magic Number
KINET_VER = [0x01, 0x00 ]#Kinet Version
KINET_PACK_TYPE_OUT = [ 0x08, 0x01 ]#Kinet Packet Type for Port Out
KINET_PACK_TYPE_SYNC = [ 0x09, 0x01 ]#Kinet Packet Type for Port Out
KINET_SEQ = [ 0x00, 0x00, 0x00, 0x00 ]#Kinet Sequence Number
KINET_UNIVERSE = [ 0xFF, 0xFF, 0xFF, 0xFF ]#Kinet Universe
KINET_SYNC_PAD = [ 0x00, 0x00, 0x00, 0x00 ]#Kinet Sync Pad
KINET_PORT = [ 0x01 ]#Port Number
KINET_PAD = [ 0x00 ] #Not Used
KINET_FLAG = [ 0x00, 0x00 ]#Kinet Flag
KINET_DMX_LEN = [ 0x00, 0x02 ]#DMX Packet Length
KINET_DMX_SC = [0x00, 0x00]#DMX Start Code
KINET_DMX_DATA = []#DMX Data packet
KINET_DMX_DATA_TEMP = []#DMX Data packet

#############################################################################################################################
for i in range(0, 512):
    KINET_DMX_DATA.append(0x00)
for i in range(0, 513):
    KINET_DMX_DATA_TEMP.append(0x00)
    
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
time.sleep(1)



def CAPacketOutput ( RED, GREEN, BLUE ):
    global MESSAGE_Q
    global MESSAGE_QC
    global MESSAGE
    for i in range(170):
        KINET_DMX_DATA[3*i+0] = RED
        KINET_DMX_DATA[3*i+1] = GREEN
        KINET_DMX_DATA[3*i+2] = BLUE
    
    
    for port in range(1,16,1):
        KINET_PORT[0] = port
        MESSAGE_Q = MAGIC_NUM + KINET_VER + KINET_PACK_TYPE_OUT + KINET_SEQ + KINET_UNIVERSE + KINET_PORT + KINET_PAD + KINET_FLAG + KINET_DMX_LEN + KINET_DMX_SC + KINET_DMX_DATA
        for item in MESSAGE_Q:
            MESSAGE_QC.append(chr(item))
        MESSAGE = ''.join(MESSAGE_QC)
            # the UDP Packet out
        sock.sendto(MESSAGE, (UDP_IP,UDP_PORT))
        MESSAGE_Q = []
        MESSAGE_QC = []
        MESSAGE = ""
    
def CAPacketSync ():
    global MESSAGE_Q
    global MESSAGE_QC
    global MESSAGE
    
    MESSAGE_Q = MAGIC_NUM + KINET_VER + KINET_PACK_TYPE_SYNC + KINET_SEQ + KINET_SYNC_PAD
    for item in MESSAGE_Q:
        MESSAGE_QC.append(chr(item))
    MESSAGE = ''.join(MESSAGE_QC)
	# the UDP Packet out
    sock.sendto(MESSAGE, (UDP_IP,UDP_PORT))
    MESSAGE_Q = []
    MESSAGE_QC = []
    MESSAGE = ""

def ColorWash ():
    RED = 0xFF
    GREEN = 0x00
    BLUE = 0x00
    STEP = 6
    print "Color Wash"
    for i in range(6):
        if i==0:
            for j in range(0, 256, STEP):
                CAPacketOutput(0xFF, j, 0x00)
                CAPacketSync()
        GREEN = 0xFF

        if i==1:
            for j in range(255, -1, -(STEP)):
                CAPacketOutput(j, 0xFF, 0x00)
                CAPacketSync()
        RED = 0x00
                
        if i==2:
            for j in range(0, 256, STEP):
                CAPacketOutput(0x00, 0xFF, j)
                CAPacketSync()
        BLUE = 0xFF
                
        if i==3:
            for j in range(255, -1, -(STEP)):
                CAPacketOutput(0x00, j, 0xFF)
                CAPacketSync()
        GREEN = 0x00

        if i==4:
            for j in range(0, 256, STEP):
                CAPacketOutput(j, 0x00, 0xFF)
                CAPacketSync()
        RED = 0xFF

        if i==5:
            for j in range(255, -1, -(STEP)):
                CAPacketOutput(0xFF, 0x00, j)
                CAPacketSync()
        BLUE = 0x00


def ChasingRainbow ():
    global MESSAGE_Q
    global MESSAGE_QC
    global MESSAGE
    global KINET_DMX_DATA
    global KINET_DMX_DATA_TEMP
    print "Chasing Rainbow"
    MESSAGE_Q = []
    MESSAGE_QC = []
    MESSAGE = ""
    RED = 0xFF
    GREEN = 0x00
    BLUE = 0x00

    for i in range(0, 28, 1):
        KINET_DMX_DATA[3*i+0] = RED
        KINET_DMX_DATA[3*i+1] = GREEN + 9*i
        KINET_DMX_DATA[3*i+2] = BLUE
        
    RED = 0xFF
    GREEN = 0xFF
    BLUE = 0x00
    for i in range(0, 28, 1):
        KINET_DMX_DATA[3*(i+28)+0] = RED - 9*i
        KINET_DMX_DATA[3*(i+28)+1] = GREEN
        KINET_DMX_DATA[3*(i+28)+2] = BLUE

    RED = 0x00
    GREEN = 0xFF
    BLUE = 0x00
    for i in range(0, 28, 1):
        KINET_DMX_DATA[3*(i+56)+0] = RED 
        KINET_DMX_DATA[3*(i+56)+1] = GREEN 
        KINET_DMX_DATA[3*(i+56)+2] = BLUE + 9*i

    RED = 0x00
    GREEN = 0xFF
    BLUE = 0xFF
    for i in range(0, 28, 1):
        KINET_DMX_DATA[3*(i+84)+0] = RED 
        KINET_DMX_DATA[3*(i+84)+1] = GREEN - 9*i
        KINET_DMX_DATA[3*(i+84)+2] = BLUE

    RED = 0x00
    GREEN = 0x00
    BLUE = 0xFF
    for i in range(0, 28, 1):
        KINET_DMX_DATA[3*(i+112)+0] = RED + 9*i
        KINET_DMX_DATA[3*(i+112)+1] = GREEN
        KINET_DMX_DATA[3*(i+112)+2] = BLUE

    RED = 0xFF
    GREEN = 0x00
    BLUE = 0xFF
    for i in range(0, 28, 1):
        KINET_DMX_DATA[3*(i+140)+0] = RED 
        KINET_DMX_DATA[3*(i+140)+1] = GREEN
        KINET_DMX_DATA[3*(i+140)+2] = BLUE - 9*i

    #504
    KINET_DMX_DATA[3*(28+140)+0] = 0xFF  
    KINET_DMX_DATA[3*(28+140)+1] = 0x00
    KINET_DMX_DATA[3*(28+140)+2] = 0x00
    #507
    KINET_DMX_DATA[3*(28+140)+0] = 0xFF  
    KINET_DMX_DATA[3*(28+140)+1] = 0x00
    KINET_DMX_DATA[3*(28+140)+2] = 0x00
    #510
    KINET_DMX_DATA[3*(28+140)+0] = 0xFF  
    KINET_DMX_DATA[3*(28+140)+1] = 0x00
    KINET_DMX_DATA[3*(28+140)+2] = 0x00

    
    KINET_PORT[0] =0x01
    
    for j in range(170):
        for port in range(1,16,1):
            KINET_PORT[0] = port
            MESSAGE_Q = MAGIC_NUM + KINET_VER + KINET_PACK_TYPE_OUT + KINET_SEQ + KINET_UNIVERSE + KINET_PORT + KINET_PAD + KINET_FLAG + KINET_DMX_LEN + KINET_DMX_SC + KINET_DMX_DATA
            for item in MESSAGE_Q:
                MESSAGE_QC.append(chr(item))
            MESSAGE = ''.join(MESSAGE_QC)
                # the UDP Packet out
            sock.sendto(MESSAGE, (UDP_IP,UDP_PORT))
            MESSAGE_Q = []
            MESSAGE_QC = []
            MESSAGE = ""

        for k in range(170):
            
            KINET_DMX_DATA_TEMP[3*(k+1)] = KINET_DMX_DATA[3*k]
            KINET_DMX_DATA_TEMP[3*(k+1)+1] = KINET_DMX_DATA[3*k+1]
            KINET_DMX_DATA_TEMP[3*(k+1)+2] = KINET_DMX_DATA[3*k+2]
            
            
        KINET_DMX_DATA_TEMP[0] = KINET_DMX_DATA[3*168]
        KINET_DMX_DATA_TEMP[1] = KINET_DMX_DATA[3*168+1]
        KINET_DMX_DATA_TEMP[2] = KINET_DMX_DATA[3*168+2]

        for k in range(0, 512):
            KINET_DMX_DATA[k] = KINET_DMX_DATA_TEMP[k]
        time.sleep(0.02)

        CAPacketSync()

        



while(True):

    CAPacketOutput(0xFF, 0x00, 0x00)
    CAPacketSync()
    time.sleep(2)
    CAPacketOutput(0x00, 0xFF, 0x00)
    CAPacketSync()
    time.sleep(2)
    CAPacketOutput(0x00, 0x00, 0xFF)
    CAPacketSync()
    time.sleep(2)
    CAPacketOutput(0xFF, 0xFF, 0xFF)
    CAPacketSync()
    time.sleep(2)

    ColorWash()
    time.sleep(2)
    ChasingRainbow()
    time.sleep(2)
    

