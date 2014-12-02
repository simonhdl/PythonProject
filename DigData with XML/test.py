# Import Library
import csv
import sys
import os
import glob
import time
import wx
import xml.etree.ElementTree as ET

# Import Excel Library
from tempfile import TemporaryFile
from xlwt import Workbook
from xlwt import Workbook, easyxf
from xlwt import Pattern, Font
from xlwt.Utils import rowcol_to_cell
from xlrd import open_workbook
from xlutils.copy import copy


RootDir = 'C:\\Users\\310098157\\Dropbox\\Works@PCK\\Engineering\\Working Directory\\Software Project\\Python Project\\DigData with XML\\'
VersionFilrDir = 'C:\\SimonHe Working\\z MyCodes\\cypher\\Software Test Scripts\\PCK_Test_Station_Version_Information.xls'
XMLFileName = 'config.xml'
ProductName = []
StationName = []

tree = ET.parse(RootDir+XMLFileName)
XMLRoot = tree.getroot()
for child in XMLRoot:
    #print child.tag, child.attrib
    if child.tag == 'ProductList' :
        ProductName.append(child.attrib['ProductName'])
    for subchild in child:
        #print subchild.tag, subchild.attrib
        if subchild.tag == 'TestStation':
            StationName.append(subchild.attrib['StationName'])
        for subsubchild in subchild:
            if subsubchild.tag == '':
                

print ProductName
print StationName
