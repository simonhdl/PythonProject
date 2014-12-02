# Import Library
import csv
import sys
import os
import glob
import time

import shutil



RootDir = 'C:\\SimonHe Working\\z MyCodes\\cypher\\Software Test Scripts\\'
VersionFileDir = 'V:\\!Manufacturing Test Software\\Test Script\\'


for root, dirs, files in os.walk(VersionFileDir):
    for name in files:  #
        if name[-3:]!='xml':
            continue
        print name, root[44:]
        ModifyTime = os.stat(root+'\\'+name)
        AbbModifyTime = time.localtime(ModifyTime.st_mtime)
        ModifyTimeSVN = os.stat(RootDir+root[43:]+'\\'+name)
        AbbModifyTimeSVN = time.localtime(ModifyTimeSVN.st_mtime)
        if AbbModifyTime==AbbModifyTimeSVN:
            print "Match!"
        elif AbbModifyTime>AbbModifyTimeSVN:
            print "Newer"
        elif AbbModifyTime<AbbModifyTimeSVN:
            shutil.copy(RootDir+root[43:]+'\\'+name,root+'\\')
            print "Older"
            
