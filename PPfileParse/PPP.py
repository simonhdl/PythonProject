import os
import cProfile
import re
import binascii


filename = '0027_BCP_1_7_0.PP'
with open(filename, 'rb') as f:
    content = f.read()
    PPname = ""
    print len(content)
    for i in range(0x20):
        if(ord(content[i])==0x00):
            continue
        #print content[i]
        PPname += content[i]
    print PPname

    FixtureName = ""
    for i in range(0xa0, 0xbF):
        if(ord(content[i])==0x00):
            continue
        FixtureName += content[i]
    print FixtureName
    
    Model1 = ""
    for i in range(0x980, 0x99F):
        if(ord(content[i])==0x00):
            continue
        Model1 += content[i]
    print Model1

    Model2 = ""
    for i in range(0x9A0, 0x9bF):
        if(ord(content[i])==0x00):
            continue
        Model2 += content[i]
    print Model2

    Model3 = ""
    for i in range(0x9c0, 0x9dF):
        if(ord(content[i])==0x00):
            continue
        Model3 += content[i]
    print Model3

    Model4 = ""
    for i in range(0x9e0, 0x9ff):
        if(ord(content[i])==0x00):
            continue
        Model4 += content[i]
    print Model4

    Model5 = ""
    for i in range(0xa00, 0xa1F):
        if(ord(content[i])==0x00):
            continue
        Model5 += content[i]
    print Model5

    Model6 = ""
    for i in range(0xa20, 0xa3F):
        if(ord(content[i])==0x00):
            continue
        Model6 += content[i]
    print Model6

    file_object  = open('data.BMP', 'wb')
    PPBMP = content[0xd90:]
    file_object.write(PPBMP)  
    file_object.close() 


