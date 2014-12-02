from uuid import getnode as get_mac
import string

mac = get_mac()

print mac
print hex(mac)


MacString = hex(mac).upper()[2:-1]

print MacString

#Divide into 4 segments
MacString1 = "0x"+MacString[:3]
MacString2 = "0x"+MacString[3:6]
MacString3 = "0x"+MacString[6:9]
MacString4 = "0x"+MacString[9:]

print MacString1,MacString2,MacString3,MacString4

#Change order
TempCode1 = [MacString2,MacString3,MacString4,MacString1]
print TempCode1

#Convert to int
TempCode2 = [int(TempCode1[0],0), int(TempCode1[1],0), int(TempCode1[2],0), int(TempCode1[3],0)]
print TempCode2

#Convert to String
TempCode3 = [str(TempCode2[0]), str(TempCode2[1]), str(TempCode2[2]), str(TempCode2[3])]
for item in TempCode3:
    if len(item) == 1:
        TempCode3[TempCode3.index(item)]='000'+item
    elif len(item) == 2:
        TempCode3[TempCode3.index(item)]='00'+item
    elif len(item) == 3:
        TempCode3[TempCode3.index(item)]='0'+item
        
print TempCode3



