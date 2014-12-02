# This will extract the discover fixture list to a excel file

# Import Library
#import csv
import sys
import os
import glob
import time

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
FailFormat = easyxf( 'font: colour black, height 150;' 'pattern: pattern solid, fore_colour red;' 'alignment: horizontal center;' )
NormalFormat = easyxf( 'font: colour black, height 150;' 'pattern: fore_colour white;' 'alignment: horizontal center;' )
PassFormat = easyxf ( 'font: colour black, height 150;' 'pattern: pattern solid, fore_colour green;' 'alignment: horizontal center;' )
ItemFailFormat = easyxf( 'font: colour red, height 150;' 'pattern: fore_colour white;' 'alignment: horizontal center;' )
# Define variable
SheetName = "Discovery Report"


book = Workbook()
sheet1 = book.add_sheet(SheetName, cell_overwrite_ok=True)

# Write first row for Title
sheet1.write(0,0,'No.',TitleFormat)
sheet1.col(0).width = 1000
sheet1.write(0,1,'UID',TitleFormat)
sheet1.col(1).width = 4000
sheet1.write(0,2,'DMX',TitleFormat)
sheet1.col(2).width = 2000
sheet1.write(0,3,'Fixture Type',TitleFormat)
sheet1.col(3).width = 6500
sheet1.write(0,4,'RDM Ver.',TitleFormat)
sheet1.col(4).width = 2000
sheet1.write(0,5,'Footprint',TitleFormat)
sheet1.col(5).width = 2000
sheet1.write(0,6,'FW Ver.',TitleFormat)
sheet1.col(6).width = 5000
sheet1.write(0,7,'MFG ID',TitleFormat)
sheet1.col(7).width = 5000
sheet1.write(0,8,'DEV LBL',TitleFormat)
sheet1.col(8).width = 5000

def ExportResult (DiscTable):
    FileName = 'Discovery_Result'
    RowCount = DiscTable.rowCount()
    if RowCount == 0 :
        print "No Fixture Discovered"
    else:
        for i in range(RowCount):
            print DiscTable.item(i, 0).text(), DiscTable.item(i, 1).text(), DiscTable.item(i, 2).text(), DiscTable.item(i, 3).text(), DiscTable.item(i, 4).text(), DiscTable.item(i, 5).text()
            sheet1.row(i+1).write(0, str(i+1), NormalFormat)
            sheet1.row(i+1).write(1, str(DiscTable.item(i, 0).text()), NormalFormat)
            sheet1.row(i+1).write(2, str(DiscTable.item(i, 1).text()), NormalFormat)
            sheet1.row(i+1).write(3, str(DiscTable.item(i, 2).text()), NormalFormat)
            sheet1.row(i+1).write(4, str(DiscTable.item(i, 3).text()), NormalFormat)
            sheet1.row(i+1).write(5, str(DiscTable.item(i, 4).text()), NormalFormat)
            sheet1.row(i+1).write(6, str(DiscTable.item(i, 5).text()), NormalFormat)
            sheet1.row(i+1).write(7, str(DiscTable.item(i, 6).text()), NormalFormat)
            sheet1.row(i+1).write(8, str(DiscTable.item(i, 7).text()), NormalFormat)
            
    book.save('Report\\'+FileName+'-'+time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))+'.xls')
    book.save(TemporaryFile())
    
    
    
    
    
    
