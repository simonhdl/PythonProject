#Config Parse

# Import Library
import csv
import sys
import os
import glob
import time

ProductList = []
ProductLineNum = []
StationList = []
StationLineNum= []
ModelList = []
ModelLineNum = []

def readProductList ():
    CfgFile = open('Config.v','r')
    for (num, value) in enumerate(CfgFile):
        if 'PRODUCT' in value:
            ProductList.append(value[8:])
            ProductLineNum.append(num)
    close('Config.v')
        
def readStationList ():
    CfgFile = open('Config.v', 'r')
    for (num, value) in enumerate(CfgFile):
        if 'STATION' in value:
            StationList.append(value[8:])
            StationLineNum.append(num)
    close('Config.v')
    

