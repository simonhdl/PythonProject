# Short Script for extract the file name and modified date to xls file
# For file version tracking
# 2013-05-17

# Add xml parser function to get the SVN rev and date and author info
# 2013-11-22


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


# Define cell font and color in excel
TitleFormat = easyxf( 'font: colour black, height 150;' 'pattern: pattern solid, fore_colour gray25;' 'alignment: horizontal center;' )
#FailFormat = easyxf( 'font: colour black, height 150;' 'pattern: pattern solid, fore_colour red;' 'alignment: horizontal center;' )
NormalFormat = easyxf( 'font: colour black, height 150;' 'pattern: fore_colour white;' 'alignment: horizontal center;' )
#PassFormat = easyxf ( 'font: colour black, height 150;' 'pattern: pattern solid, fore_colour green;' 'alignment: horizontal center;' )

#RootDir = 'C:\\Users\\310098157\\Dropbox\\Works@PCK\\Engineering\\Working Directory\\Projects\\'
#VersionFilrDir = 'C:\\Users\\310098157\\Dropbox\\Works@PCK\\Engineering\\Working Directory\\Projects\\PCK_Test_Station_Version_Information.xls'
RootDir = 'C:\\SimonHe Working\\z MyCodes\\cypher\\Software Test Scripts\\'
VersionFilrDir = 'C:\\SimonHe Working\\z MyCodes\\cypher\\Software Test Scripts\\PCK_Test_Station_Version_Information.xls'

#DirList = os.listdir(RootDir)

#for item in DirList:
#    #print item
#    if os.path.isdir(RootDir+item) :
#        RootDir = RootDir+item
#        os.chdir(RootDir)
#    else :
#        ModifyTime = os.stat(RootDir+item)
#        AbbModifyTime = time.localtime(ModifyTime.st_mtime)
#        FinalFormatDate = str(AbbModifyTime.tm_year) + '-' + str(AbbModifyTime.tm_mon) + '-' + str(AbbModifyTime.tm_mday)
#        FinalFormatTime = str(AbbModifyTime.tm_hour) + ':' + str(AbbModifyTime.tm_min) + ':' + str(AbbModifyTime.tm_sec)
#        print(item, FinalFormatDate + ',' + FinalFormatTime)

#########################################################
# Define xls sheet name
book = Workbook()
sheet1 = book.add_sheet('File Name and File Date')

# Write first row for Title
sheet1.write(0,0,'File Name',TitleFormat)
sheet1.col(0).width = 15000
sheet1.write(0,1,'File Date',TitleFormat)
sheet1.col(1).width = 8000
sheet1.write(0,2,'File Folder',TitleFormat)
sheet1.col(2).width = 20000
sheet1.write(0,3,'SVN Revision',TitleFormat)
sheet1.col(3).width = 8000
sheet1.write(0,4,'SVN Commit Date',TitleFormat)
sheet1.col(4).width = 20000

Num = 0


for root, dirs, files in os.walk(RootDir):
    #print root          # 
    #for name in dirs:   # 
    #    print '[D]',name
    
    for name in files:  #
        if '.xml' in name :
            Num += 1
            #print root+name
            ModifyTime = os.stat(root+'\\'+name)
            AbbModifyTime = time.localtime(ModifyTime.st_mtime)
            if len(str(AbbModifyTime.tm_mon))<2 :
                MonthStr = '0'+str(AbbModifyTime.tm_mon)
            else:
                MonthStr = str(AbbModifyTime.tm_mon)
            if len(str(AbbModifyTime.tm_mday))<2 :
                DayStr = '0'+str(AbbModifyTime.tm_mday)
            else:
                DayStr = str(AbbModifyTime.tm_mday)
            if len(str(AbbModifyTime.tm_hour))<2 :
                HourStr = '0'+str(AbbModifyTime.tm_hour)
            else:
                HourStr = str(AbbModifyTime.tm_hour)
            if len(str(AbbModifyTime.tm_min))<2 :
                MinStr = '0'+str(AbbModifyTime.tm_min)
            else:
                MinStr = str(AbbModifyTime.tm_min)
            if len(str(AbbModifyTime.tm_sec))<2 :
                SecStr = '0'+str(AbbModifyTime.tm_sec)
            else:
                SecStr = str(AbbModifyTime.tm_sec)
            FinalFormatDate = str(AbbModifyTime.tm_year) + '-' + MonthStr + '-' + DayStr
            FinalFormatTime = HourStr + ':' + MinStr + ':' + SecStr
            print(name, FinalFormatDate + ',' + FinalFormatTime)
            sheet1.row(Num).write(0, name, NormalFormat)
            sheet1.row(Num).write(1, FinalFormatDate + ',' + FinalFormatTime, NormalFormat)

            tree = ET.parse(root+'\\'+name)
            sheet1.row(Num).write(2, root, NormalFormat)
            XMLroot = tree.getroot()
            for child in XMLroot:
                if 'rev' in child.attrib:
                    TitleTXT = child.attrib['rev']
                    sheet1.row(Num).write(3, TitleTXT, NormalFormat)
                if 'date' in child.attrib:
                    TitleTXT = child.attrib['date']
                    sheet1.row(Num).write(4, TitleTXT, NormalFormat)
                XMLTag = child.tag
                if XMLTag == 'SVN_Rev':
                    sheet1.row(Num).write(3, XMLroot.find('SVN_Rev').text, NormalFormat)
                    sheet1.row(Num).write(4, XMLroot.find('SVN_Date').text, NormalFormat)

book.save('A.xls')

#rb = open_workbook(VersionFilrDir)
#for s in rb.sheets():
#    print 'Sheet:', s.name
#    for row in range(s.nrows):
#        for col in range(s.ncols):
#            if s.cell(row,col).value == 'FTE-MRG3-Power Supply PCA.xml' :
#                print s.cell(1, 3).value, s.cell(row, col+1).value
#                s.cell(row, col+1).value = 'AA'

#wb = copy(rb)

#wb.save(VersionFilrDir)

