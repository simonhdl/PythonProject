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
import xml.etree.ElementTree as ET

# Import Excel Library
from tempfile import TemporaryFile
from xlwt import Workbook, easyxf
from xlwt import Pattern, Font
from xlwt import Borders, XFStyle
from xlwt import Row
from xlwt.Utils import rowcol_to_cell
from xlrd import open_workbook
from xlutils.copy import copy


# Define cell font and color in excel
#TitleFormat = easyxf( 'font: colour black, height 200, bold True;' 'pattern: pattern solid, fore_colour ice_blue;' 'alignment: horizontal center;' 'borders: left thick, right thick, top thick, bottom thick;')
TitleFormat2 = easyxf( 'font: colour black, height 220, bold True;' 'pattern: pattern solid, fore_colour ice_blue;' 'alignment: horizontal center, vertical center;' 'borders: left thick, right thick, top thick, bottom thick;')
#FailFormat = easyxf( 'font: colour black, height 150;' 'pattern: pattern solid, fore_colour red;' 'alignment: horizontal center;' )
NormalFormat = easyxf( 'font: colour black, height 160;' 'pattern: fore_colour white;' 'alignment: horizontal left;' )
NormalFormat2 = easyxf( 'font: colour black, height 160;' 'pattern: fore_colour gray25;' 'alignment: horizontal left;' )
#PassFormat = easyxf ( 'font: colour black, height 150;' 'pattern: pattern solid, fore_colour green;' 'alignment: horizontal center;' )


light_blue = easyxf( 'font: colour black, height 160;' 'pattern: pattern solid, fore_colour light_blue;' 'alignment: horizontal left;' 'borders: left thin, right thin, top thin, bottom thin;')
light_green = easyxf( 'font: colour black, height 160;' 'pattern: pattern solid, fore_colour light_green;' 'alignment: horizontal left;' 'borders: left thin, right thin, top thin, bottom thin;')
light_orange = easyxf( 'font: colour black, height 160;' 'pattern: pattern solid, fore_colour light_orange;' 'alignment: horizontal left;' 'borders: left thin, right thin, top thin, bottom thin;')
light_turquoise = easyxf( 'font: colour black, height 160;' 'pattern: pattern solid, fore_colour light_turquoise;' 'alignment: horizontal left;' 'borders: left thin, right thin, top thin, bottom thin;')
light_yellow = easyxf( 'font: colour black, height 160;' 'pattern: pattern solid, fore_colour light_yellow;' 'alignment: horizontal left;' 'borders: left thin, right thin, top thin, bottom thin;')
lime = easyxf( 'font: colour black, height 160;' 'pattern: pattern solid, fore_colour lime;' 'alignment: horizontal left;' 'borders: left thin, right thin, top thin, bottom thin;')
olive_ega = easyxf( 'font: colour black, height 160;' 'pattern: pattern solid, fore_colour olive_ega;' 'alignment: horizontal left;' 'borders: left thin, right thin, top thin, bottom thin;')
olive_green = easyxf( 'font: colour black, height 160;' 'pattern: pattern solid, fore_colour olive_green;' 'alignment: horizontal left;' 'borders: left thin, right thin, top thin, bottom thin;')
orange = easyxf( 'font: colour black, height 160;' 'pattern: pattern solid, fore_colour orange;' 'alignment: horizontal left;' 'borders: left thin, right thin, top thin, bottom thin;')
pale_blue = easyxf( 'font: colour black, height 160;' 'pattern: pattern solid, fore_colour pale_blue;' 'alignment: horizontal left;' 'borders: left thin, right thin, top thin, bottom thin;')
periwinkle = easyxf( 'font: colour black, height 160;' 'pattern: pattern solid, fore_colour periwinkle;' 'alignment: horizontal left;' 'borders: left thin, right thin, top thin, bottom thin;')
ice_blue = easyxf( 'font: colour black, height 160;' 'pattern: pattern solid, fore_colour ice_blue;' 'alignment: horizontal left;' 'borders: left thin, right thin, top thin, bottom thin;')
indigo = easyxf( 'font: colour black, height 160;' 'pattern: pattern solid, fore_colour indigo;' 'alignment: horizontal left;' 'borders: left thin, right thin, top thin, bottom thin;')
ivory = easyxf( 'font: colour black, height 160;' 'pattern: pattern solid, fore_colour ivory;' 'alignment: horizontal left;' 'borders: left thin, right thin, top thin, bottom thin;')
lavender = easyxf( 'font: colour black, height 160;' 'pattern: pattern solid, fore_colour lavender;' 'alignment: horizontal left;' 'borders: left thin, right thin, top thin, bottom thin;')

FormatColor = [ light_blue, light_green, light_orange, light_turquoise, light_yellow, lime, olive_ega, olive_green, orange, pale_blue, periwinkle, ice_blue, indigo, ivory, lavender ]


#RootDir = 'C:\\Users\\310098157\\Dropbox\\Works@PCK\\Engineering\\Working Directory\\Projects\\'
#VersionFilrDir = 'C:\\Users\\310098157\\Dropbox\\Works@PCK\\Engineering\\Working Directory\\Projects\\PCK_Test_Station_Version_Information.xls'
RootDir = 'C:\\Users\\310098157\\Simon Working Folder\\Z Cypher\Software Test Scripts'
VersionFilrDir = 'C:\\Users\\310098157\\Simon Working Folder\\Z Cypher\Software Test Scripts\\PCK_Test_Station_Version_Information.xls'

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
sheet1.write(0,0,'Product Cat.',TitleFormat2)
sheet1.col(0).width = 5000

sheet1.write(0,1,'Script File Name',TitleFormat2)
sheet1.col(1).width = 12000
sheet1.write(0,2,'Modified Date',TitleFormat2)
sheet1.col(2).width = 5000
sheet1.write(0,3,'SVN Revision',TitleFormat2)
sheet1.col(3).width = 5000
sheet1.write(0,4,'SVN Commit Date',TitleFormat2)
sheet1.col(4).width = 12000

sheet1.row(0).height_mismatch = True
sheet1.row(0).height = 256*2

Num = 0

reader = csv.reader(open("FileList.csv"), delimiter=",")
for row in reader:
    for root, dirs, files in os.walk(RootDir):
        for name in files:  #
            if row[0] in name :
                Num += 1

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
                sheet1.row(Num).write(1, name, FormatColor[int(row[2])])
                sheet1.row(Num).write(2, FinalFormatDate + ',' + FinalFormatTime, FormatColor[int(row[2])])

                tree = ET.parse(root+'\\'+name)
                sheet1.row(Num).write(0, row[1], FormatColor[int(row[2])])

                XMLroot = tree.getroot()
                for child in XMLroot:
                    if 'rev' in child.attrib:
                        TitleTXT = child.attrib['rev']
                        sheet1.row(Num).write(3, TitleTXT, FormatColor[int(row[2])])
                    if 'date' in child.attrib:
                        TitleTXT = child.attrib['date']
                        sheet1.row(Num).write(4, TitleTXT, FormatColor[int(row[2])])

                    XMLTag = child.tag
                    if XMLTag == 'SVN_Rev':
                        sheet1.row(Num).write(3, XMLroot.find('SVN_Rev').text, FormatColor[int(row[2])])
                        sheet1.row(Num).write(4, XMLroot.find('SVN_Date').text, FormatColor[int(row[2])])



book.save('C:\\Users\\310098157\\Simon Working Folder\\Z Cypher\Software Test Scripts\\PCK_Test_Station_Version_Information.xls')
book.save('X:\\Electrical Engineering Department\Manufacturing Test SW\\PCK_Test_Station_Version_Information.xls')
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

