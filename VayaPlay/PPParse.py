import os
import cProfile
import re
import binascii

global ModelList
global FootprintList
global FixtureName
global FWVersion

def ParsePP (filename):
    global ModelList
    global FixtureName
    global FootprintList
    global FWVersion
    
    ModelList = []
    FootprintList = []
    with open(filename, 'rb') as f:
        content = f.read()
        PPname = ""
        #print len(content)
        for i in range(0x20):
            if(ord(content[i])==0x00):
                continue
            #print content[i]
            PPname += content[i]
        #print PPname

        FWVersion = ""
        FWVersion = PPname[17]+'.'+PPname[19]+'.'+PPname[21]
        
        FixtureName = ""
        for i in range(0xa0, 0xbF):
            if(ord(content[i])==0x00):
                continue
            FixtureName += content[i]
        #print FixtureName
    
        Model1 = ""
        for i in range(0x980, 0x99F):
            if(ord(content[i])==0x00):
                continue
            Model1 += content[i]
        FootList1 = ord(content[0x99E])
        #print Model1

        Model2 = ""
        for i in range(0x9A0, 0x9bF):
            if(ord(content[i])==0x00):
                continue
            Model2 += content[i]
        FootList2 = ord(content[0x9bE])
        #print Model2

        Model3 = ""
        for i in range(0x9c0, 0x9dF):
            if(ord(content[i])==0x00):
                continue
            Model3 += content[i]
        FootList3 = ord(content[0x9dE])
        #print Model3

        Model4 = ""
        for i in range(0x9e0, 0x9ff):
            if(ord(content[i])==0x00):
                continue
            Model4 += content[i]
        FootList4 = ord(content[0x9fE])
        #print Model4

        Model5 = ""
        for i in range(0xa00, 0xa1F):
            if(ord(content[i])==0x00):
                continue
            Model5 += content[i]
        FootList5 = ord(content[0xa1E])
        #print Model5

        Model6 = ""
        for i in range(0xa20, 0xa3F):
            if(ord(content[i])==0x00):
                continue
            Model6 += content[i]
        FootList6 = ord(content[0xa3E])
        #print Model6

        ModelList = [Model1[:-1], Model2[:-1], Model3[:-1], Model4[:-1], Model5[:-1], Model6[:-1]]
        FootprintList = [FootList1, FootList2, FootList3, FootList4, FootList5, FootList6]
        file_object  = open('data.BMP', 'wb')
        PPBMP = content[0xd90:]
        file_object.write(PPBMP)  
        file_object.close() 


