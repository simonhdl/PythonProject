import socket
import string
import time
#UDP_IP = "10.4.16.197"

UDP_IP = "10.255.255.255"

#UDP_IP = "10.1.1.15"

UDP_PORT = 6038
MESSAGE = ""
MESSAGE_Q = []
MESSAGE_QC = []

MAGIC_NUM = [ 0x04, 0x01, 0xDC, 0x4A ]
KINET_VER = [0x01, 0x00]
KINET_PACK_TYPE = [ 0x08, 0x01]
KINET_SEQ = [ 0x00, 0x00, 0x00, 0x00]
KINET_PO_UNI = [ 0xFF, 0xFF, 0xFF, 0xFF ]
KINET_PO = [ 0x01, 0x00]
KINET_FLAG = [ 0x00, 0x00]
KINET_DMX_LEN = [ 0x00, 0x02 ]
KINET_DMX_SC = [0x00, 0x00]
KINET_DMX_DATA = []

for i in range(0, 512):
    KINET_DMX_DATA.append(0x00)


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for j in range (0, 3):

    KINET_DMX_DATA[0] = 0x00
    KINET_DMX_DATA[2] = 0x00
    KINET_DMX_DATA[4] = 0x00

    KINET_DMX_DATA[2*j] = 0xFF
    
    MESSAGE_Q = MAGIC_NUM + KINET_VER + KINET_PACK_TYPE + KINET_SEQ + KINET_PO_UNI + KINET_PO + KINET_FLAG + KINET_DMX_LEN + KINET_DMX_SC + KINET_DMX_DATA
    for item in MESSAGE_Q:
        MESSAGE_QC.append(chr(item))
    MESSAGE = ''.join(MESSAGE_QC)
    sock.sendto(MESSAGE, (UDP_IP,UDP_PORT))
    MESSAGE_Q = []
    MESSAGE_QC = []
    MESSAGE = ""
    
    time.sleep(1)

KINET_DMX_DATA[0] = 0xFF
KINET_DMX_DATA[2] = 0xFF
KINET_DMX_DATA[4] = 0xFF

'''   
MESSAGE_Q = MAGIC_NUM + KINET_VER + KINET_PACK_TYPE + KINET_SEQ + KINET_PO_UNI + KINET_PO + KINET_FLAG + KINET_DMX_LEN + KINET_DMX_SC + KINET_DMX_DATA
for item in MESSAGE_Q:
    MESSAGE_QC.append(chr(item))
MESSAGE = ''.join(MESSAGE_QC)
sock.sendto(MESSAGE, (UDP_IP,UDP_PORT))

KINET_DMX_DATA[0] = 0x00
KINET_DMX_DATA[2] = 0x00
KINET_DMX_DATA[4] = 0x00

MESSAGE_Q = []
MESSAGE_QC = []
MESSAGE = ""

time.sleep(1)
MESSAGE_Q = MAGIC_NUM + KINET_VER + KINET_PACK_TYPE + KINET_SEQ + KINET_PO_UNI + KINET_PO + KINET_FLAG + KINET_DMX_LEN + KINET_DMX_SC + KINET_DMX_DATA
for item in MESSAGE_Q:
    MESSAGE_QC.append(chr(item))
MESSAGE = ''.join(MESSAGE_QC)


for i in range(10000):
    print i
    print UDP_IP
    sock.sendto(MESSAGE, (UDP_IP,UDP_PORT))
    #time.sleep(1)


print "END"
'''
    


