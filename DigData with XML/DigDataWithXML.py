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
FailFormat = easyxf( 'font: colour black, height 150;' 'pattern: pattern solid, fore_colour red;' 'alignment: horizontal center;' )
NormalFormat = easyxf( 'font: colour black, height 150;' 'pattern: fore_colour white;' 'alignment: horizontal center;' )
PassFormat = easyxf ( 'font: colour black, height 150;' 'pattern: pattern solid, fore_colour green;' 'alignment: horizontal center;' )
# Define variable
PF = []
temp = []
TestTime = []
PartNumber = []
Result = []
Num = 0
Num2 = 0
Counter = 0
# Dictionary for storing the Product type
ProductName = {1:"Null", 2:"Null", 3:"Null", 4:"Null", 5:"Null", 6:"Null", 7:"Null", 8:"Null", 9:"Null", 10:"Null", 11:"Null", 12:"Null", 13:"Null", 14:"Null", 15:"Null"}
# Dictionary for storing the Station type which product line use
StationName = {1:"Null", 2:"Null", 3:"Null", 4:"Null", 5:"Null", 6:"Null", 7:"Null", 8:"Null", 9:"Null", 10:"Null", 11:"Null", 12:"Null", 13:"Null", 14:"Null", 15:"Null"}
# Dictionary for storing the Model type one product may have
ModelName = {1:"Null", 2:"Null", 3:"Null", 4:"Null", 5:"Null", 6:"Null", 7:"Null", 8:"Null", 9:"Null", 10:"Null", 11:"Null", 12:"Null", 13:"Null", 14:"Null", 15:"Null"}
ProductLineNum = []
ProductList = []
StationLineNum = []
StationList = []
ModelIndex = []
ModelMenu = []
ModelList = ""
# Save the string index for title
TitleIndex = []
TitleList = {1:"Null", 2:"Null", 3:"Null", 4:"Null", 5:"Null", 6:"Null", 7:"Null", 8:"Null", 9:"Null", 10:"Null", 11:"Null", 12:"Null", 13:"Null", 14:"Null", 15:"Null", 16:"Null", 17:"Null", 18:"Null", 19:"Null", 20:"Null", 21:"Null", 22:"Null", 23:"Null", 24:"Null", 25:"Null", 26:"Null", 27:"Null", 28:"Null", 29:"Null", 30:"Null"}
# Save the cell location index for cell which we want to extract
CellIndex = []
CellList = {1:"Null", 2:"Null", 3:"Null", 4:"Null", 5:"Null", 6:"Null", 7:"Null", 8:"Null", 9:"Null", 10:"Null", 11:"Null", 12:"Null", 13:"Null", 14:"Null", 15:"Null", 16:"Null", 17:"Null", 18:"Null", 19:"Null", 20:"Null", 21:"Null", 22:"Null", 23:"Null", 24:"Null", 25:"Null", 26:"Null", 27:"Null", 28:"Null", 29:"Null", 30:"Null"}
TargetLineNum = 0
ProductType = 0
StationType = 0
FixtureType = 1
# Convert the XLS coordinator to number
Coordinator = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26, 'AA':27, 'AB':28, 'AC':29, 'AD':30}
Coor_X = 0
Coor_Y = 0

#==========================================
# Define Function for conversion location
#==========================================
def StrConversionX ( InputStr ):
    return Coordinator.get(InputStr[0])
def StrConversionY ( InputStr ):
    return int(InputStr[1:])



#if __name__ == "__main__":
#    app_input1 = wx.PySimpleApp()
#    dialog = wx.TextEntryDialog(None, "Please Input Sheet Name:", "Text Entry", "", style=wx.OK|wx.CANCEL)
#    if dialog.ShowModal() == wx.ID_OK:
#        #print "You entered: %s" % dialog.GetValue()
#        SheetName = dialog.GetValue()
#    dialog.Destroy()
SheetName = "TestData"
Sheet2Name = "Summary"

if __name__ == "__main__":
    app_input2 = wx.PySimpleApp()
    #dialog = wx.TextEntryDialog(None, "Please Input CSV file Path:", "Text Entry", "", style=wx.OK|wx.CANCEL)
    dialog = wx.FileDialog(None, message="Choose the directory of the CSV files.", defaultDir="", defaultFile="", wildcard="*.csv*", style=0)
    dialog.Center()
    if dialog.ShowModal() == wx.ID_OK:
        TargetPath = dialog.GetDirectory()
    else:
        exit()
    dialog.Destroy()


# Input File name and sheet name by user
#FileName = raw_input("Please Input File Name: ")
#SheetName = raw_input("Please Input Sheet Name: ")
#TargetPath = raw_input("Please Input CSV file Path: ")

#########################################################
f=open('Config.v','r')
# Fatch the Product list
for line in f:
    Num +=1
    if line[0]=='P':
        Counter += 1
        ProductName[Counter] = line
        ProductLineNum.append(Num)
        #print(Counter)
        #print(Num)
        
ProductLineNum.append(Num)
#print(ProductName)
#print(ProductLineNum)
Num = 0
Counter = 0
#print("*******************************************")
#print("Input the Index to Choose the Product Name:")
for item in ProductName:
    if ProductName[item] != "Null" :
        ProductList.append(ProductName[item])
        #print(item,ProductName[item])

if __name__=="__main__":
    app0 = wx.PySimpleApp()
    choices = ProductList
    dialog = wx.SingleChoiceDialog(None, "Input the Index to Choose the Product Name:", "Product Name", choices)
    dialog.Center()
    if dialog.ShowModal()==wx.ID_OK:
        #print("Your Select: %s\n" %dialog.GetStringSelection())
        TempSelection = dialog.GetStringSelection()
        for key in ProductName.keys():
            if(TempSelection == ProductName[key]):
                ProductType = key
                #print(key)
    else:
        exit()
    dialog.Destroy()

#ProductType = input()
#print(ProductLineNum[ProductType-1])
#print(ProductLineNum[ProductType])

#########################################################
f=open('Config.v','r')
# Fatch the Test Station List which Product is selected
for line in f:
    Num +=1
    if (Num >= ProductLineNum[ProductType-1]) and (Num <= ProductLineNum[ProductType]) :
        if line[0] == 'S':
            Counter += 1
            StationName[Counter] = line
            StationLineNum.append(Num)
        if line == "END\n":
            Counter += 1
            StationName[Counter] = "Null"
            StationLineNum.append(Num)
#print(StationName)
#print(StationLineNum)
Num = 0
Counter = 0
#print("*******************************************")
#print("Input the Index to Choose the Test Station Name:")
for item in StationName:
    if StationName[item] != "Null" :
        StationList.append(StationName[item])
        #print(item,StationName[item])
        
if __name__=="__main__":
    app1 = wx.PySimpleApp()
    choices = StationList
    dialog = wx.SingleChoiceDialog(None, "Input the Index to Choose the Station Name:", "Station Name", choices)
    dialog.Center()
    if dialog.ShowModal()==wx.ID_OK:
        #print("Your Select: %s\n" %dialog.GetStringSelection())
        TempSelection = dialog.GetStringSelection()
        for key in StationName.keys():
            if(TempSelection == StationName[key]):
                StationType = key
                #print(key)
    else:
        exit()
    dialog.Destroy()

#StationType = input()
#print(StationLineNum[StationType-1])
#print(StationLineNum[StationType])

#########################################################
f=open('Config.v','r')
# Fatch the Fixture Model List which Station is selected
for line in f:
    Num +=1
    if (Num >= StationLineNum[StationType-1]) and (Num <= StationLineNum[StationType]) :
        if line[0] == 'M':
            ModelList = line;
            TargetLineNum = Num
#print(ModelList)
Num = 0
Counter = 0

if ModelList != "MODEL:NULL\n":
    for item in ModelList:
        if item == ':':
            Counter = 1
            ModelIndex.append(Num)
        if item == ';':
            #ModelName[Counter]=ModelList
            ModelIndex.append(Num)
            ModelName[Counter]=ModelList[ModelIndex[Counter-1]+1 : ModelIndex[Counter]]
            Counter +=1
        Num +=1
    #print("*******************************************")
    #print("Input the Index to Choose the Fixture Type:")
    for item in ModelName:
        if ModelName[item] != "Null" :
            ModelMenu.append(ModelName[item])
            #print(item,ModelName[item])

    if __name__=="__main__":
        app2 = wx.PySimpleApp()
        #choices = StationList
        dialog = wx.SingleChoiceDialog(None, "Input the Index to Choose the Fixture Type:", "Fixture Type", ModelMenu)
        dialog.Center()
        if dialog.ShowModal()==wx.ID_OK:
            #print("Your Select: %s\n" %dialog.GetStringSelection())
            TempSelection = dialog.GetStringSelection()
            for key in ModelName.keys():
                if(TempSelection == ModelName[key]):
                    FixtureType = key
                    #print(key)
        else:
            exit()
        dialog.Destroy()
    #FixtureType = input()
#print("*******************************************")

Num = 0
Counter = 0
#########################################################
f=open('Config.v','r')
for line in f:
    Num += 1
    if Num == TargetLineNum+FixtureType*2-1 :
        #print(Num)
        # Fatch the Title List and Generate the xls title
        for item in line :
            if item == ':':
                Counter = 1
                TitleIndex.append(Num2)
            if item == ';':
                TitleIndex.append(Num2)
                TitleList[Counter]=line[TitleIndex[Counter-1]+1 : TitleIndex[Counter]]
                Counter +=1
            Num2 +=1
        Counter = 0
        Num2 = 0
    if Num == TargetLineNum+FixtureType*2:
        #print(Num)
        # Fatch the Cell List and Generate the xls title
        for item in line :
            if item == ':':
                Counter = 1
                CellIndex.append(Num2)
            if item == ';':
                CellIndex.append(Num2)
                CellList[Counter]=line[CellIndex[Counter-1]+1 : CellIndex[Counter]]
                Counter +=1
            Num2 +=1
        Counter = 0
        Num2 = 0
Num = 0
Num2 = 0
Counter = 0
#########################################################
# Define xls sheet name
book = Workbook()
sheet1 = book.add_sheet(SheetName)
sheet2 = book.add_sheet(Sheet2Name)

# Write first row for Title
sheet1.write(0,0,'File Name',TitleFormat)
sheet1.col(0).width = 8000
sheet1.write(0,1,'Part Number',TitleFormat)
sheet1.col(1).width = 4000
sheet1.write(0,2,'P/F',TitleFormat)
sheet1.col(2).width = 3000
# Generate the title according to the configuration file
for item in TitleList:
    if TitleList[item] != "Null":
        sheet1.write(0,item+2,TitleList[item],TitleFormat)
        sheet1.col(item+2).width = 4000

#======================================================================
# Set the file path to upper directory
#print os.path.dirname(os.path.abspath(__file__))
#print os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  
#print os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
# Not use anymore
#======================================================================

#Search for every CSV file in this folder
#for fileName in glob.glob (r'../*.csv'):
for fileName in glob.glob (TargetPath+'/*.csv'):
    print(os.path.basename(fileName))
    Num = Num + 1 # File count for adding new row in xls file
    # Open CSV file and use ',' to seperate the column
    reader = csv.reader(open(fileName), delimiter=",")
    
    # First Column to Save File name instead of Serial No. or Test Time
    sheet1.row(Num).write(0, os.path.basename(fileName), NormalFormat)
    
    for row in reader: # search every row in the csv file
        #print row
        # If ROW not null and title is "Test Stop" or "Test Start Time"
        #if row != [] and ( row[0] == 'Test Stop' or row[0] == 'Test Start Time' ):
            #TestTime = row[1]
        #if reader.line_num == 9:
        if row != [] and row[0] == 'Part Number' :
            #print row
            PartNumber = row[1]
            sheet1.row(Num).write(1, PartNumber, NormalFormat)
        if row != [] and ( row[0] == 'OVERALL RESULT' or row[0] == 'DUT P/F' or row[0] == 'Overall Result' ) :
            #print row
            PF = row[1]
            #if PF == "FAIL" or PF == "Fail" or PF == "Failed" or PF == "F" or PF == "FAILED":
            if (PF.find('F')>0) or (PF.find('f')>0):
                sheet1.row(Num).write(2, PF, FailFormat)
            else:
                sheet1.row(Num).write(2, PF, PassFormat)

        for item in CellList:
            if CellList[item] != "Null":
                if reader.line_num == (StrConversionY(CellList[item])):
                    if(row != [] and len(row)>= StrConversionX(CellList[item])):
                        Result.append(row[StrConversionX(CellList[item])-1])
                
    if Result==[] : continue
    for i in range(0,len(Result)):
        #if Result[i] == "FAIL" or Result[i] == "Fail" or Result[i] == "Failed" or Result[i] == "F" or Result[i] == "FAILED":
        if (Result[i].find('F')>0) or (Result[i].find('f')>0):
            sheet1.row(Num).write(i+3, Result[i], FailFormat)
        else:
            if(str.isalpha(Result[i])): # if the contain is not numbers.
                sheet1.row(Num).write(i+3, Result[i], NormalFormat)
            elif(str.isspace(Result[i])): # if the contain is not numbers.
                sheet1.row(Num).write(i+3, Result[i], NormalFormat)
            else:
                sheet1.row(Num).write(i+3, float(Result[i]), NormalFormat)

    Result = []

# Save to excel file, Save to the result folder in target directory
if os.path.exists(TargetPath+'/Result/'):
    os.chdir(TargetPath+'/Result/')
else :
    os.makedirs(TargetPath+'/Result/')
    os.chdir(TargetPath+'/Result/')

################################################
# Enter File Name...
if __name__ == "__main__":
    app_input0 = wx.PySimpleApp()
    dialog = wx.TextEntryDialog(None, "Please Input File Name:", "File Name", "", style=wx.OK|wx.CANCEL)
    dialog.Center()
    if dialog.ShowModal() == wx.ID_OK:
        FileName = dialog.GetValue()
    else:
        exit()
    dialog.Destroy()

if os.path.isfile(FileName+'.xls'):
    book.save(FileName+'-'+time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))+'.xls')
else:
    book.save(FileName+'.xls')
    
book.save(TemporaryFile())

#print
#print("******************************")
#print("*      Conversion Done       *")
#print("******************************")
# Display confirm window after done.
class ButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'DigData', size=(200, 110))
        panel = wx.Panel(self, -1)
        self.button = wx.Button(panel, -1, "Done!", size=(80,30), pos=(60, 20))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()
    def OnClick(self, event):
        self.Close(True)
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = ButtonFrame()
    frame.Center()
    frame.Show()
    app.MainLoop()

    
