
import wx

# begin wxGlade: extracode
# end wxGlade
# For Extract the CSV data to generate a new xls file for data analyze
# Author : Simon He
# 1st Edition: 2012-12-02
# 2ed Edition: 2013-02-22 / add read config file

# Import Library
import csv
import sys
import os
import glob
import time
import wx

# Import Excel Library
from tempfile import TemporaryFile
from xlwt import Workbook
from xlwt import Workbook, easyxf
from xlwt import Pattern, Font
from xlwt.Utils import rowcol_to_cell

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
ProductName = {1:"Null", 2:"Null", 3:"Null", 4:"Null", 5:"Null", 6:"Null", 7:"Null", 8:"Null", 9:"Null", 10:"Null", 11:"Null", 12:"Null", 13:"Null", 14:"Null", 15:"Null", 16:"Null", 17:"Null", 18:"Null", 19:"Null", 20:"Null", 21:"Null", 22:"Null", 23:"Null", 24:"Null", 25:"Null", 26:"Null", 27:"Null", 28:"Null", 29:"Null", 30:"Null"}
# Dictionary for storing the Station type which product line use
StationName = {1:"Null", 2:"Null", 3:"Null", 4:"Null", 5:"Null", 6:"Null", 7:"Null", 8:"Null", 9:"Null", 10:"Null", 11:"Null", 12:"Null", 13:"Null", 14:"Null", 15:"Null", 16:"Null", 17:"Null", 18:"Null", 19:"Null", 20:"Null", 21:"Null", 22:"Null", 23:"Null", 24:"Null", 25:"Null", 26:"Null", 27:"Null", 28:"Null", 29:"Null", 30:"Null"}
# Dictionary for storing the Model type one product may have
ModelName = {1:"Null", 2:"Null", 3:"Null", 4:"Null", 5:"Null", 6:"Null", 7:"Null", 8:"Null", 9:"Null", 10:"Null", 11:"Null", 12:"Null", 13:"Null", 14:"Null", 15:"Null", 16:"Null", 17:"Null", 18:"Null", 19:"Null", 20:"Null", 21:"Null", 22:"Null", 23:"Null", 24:"Null", 25:"Null", 26:"Null", 27:"Null", 28:"Null", 29:"Null", 30:"Null"}
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



class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.label_1 = wx.StaticText(self, -1, "Select the CSV Folder")
        self.panel_1 = wx.Panel(self, -1)
        self.panel_2 = wx.Panel(self, -1)
        self.panel_3 = wx.Panel(self, -1)
        self.TextFolder = wx.TextCtrl(self, -1, "")
        self.ButtonOpen = wx.Button(self, -1, "Open")
        self.label_2 = wx.StaticText(self, -1, "1. Product Name")
        self.label_3 = wx.StaticText(self, -1, "2. Station Name")
        self.label_4 = wx.StaticText(self, -1, "3. Fixture Type")
        self.ProductCombo = wx.ComboBox(self, -1, choices=ProductList, style=wx.CB_DROPDOWN)
        self.StationCombo = wx.ComboBox(self, -1, choices=StationList, style=wx.CB_DROPDOWN)
        self.FixtureCombo = wx.ComboBox(self, -1, choices=ModelMenu, style=wx.CB_DROPDOWN)
        self.label_5 = wx.StaticText(self, -1, "Enter File Name")
        self.panel_4 = wx.Panel(self, -1)
        self.panel_7 = wx.Panel(self, -1)
        self.TextFileName = wx.TextCtrl(self, -1, "")
        self.panel_5 = wx.Panel(self, -1)
        self.panel_8 = wx.Panel(self, -1)
        self.ButtonOk = wx.Button(self, -1, "OK")
        self.panel_6 = wx.Panel(self, -1)
        self.ButtonCancel = wx.Button(self, -1, "Quit")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.Click, self.ButtonOpen)
        self.Bind(wx.EVT_COMBOBOX, self.ProductChoose, self.ProductCombo)
        self.Bind(wx.EVT_COMBOBOX, self.StationChoose, self.StationCombo)
        self.Bind(wx.EVT_COMBOBOX, self.FixtureChoose, self.FixtureCombo)
        self.Bind(wx.EVT_BUTTON, self.Exit, self.ButtonCancel)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("CK Test Data Extractor V1.1")
        self.SetSize((650, 300))
        self.label_1.SetMinSize((125, 16))
        self.label_1.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.TextFolder.SetMinSize((400, -1))
        self.label_2.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.label_3.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.label_4.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.ProductCombo.SetMinSize((200, 21))
        self.StationCombo.SetMinSize((200, 21))
        self.FixtureCombo.SetMinSize((200, 21))
        self.label_5.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.TextFileName.SetMinSize((200, -1))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(7, 3, 0, 0)
        grid_sizer_1.Add(self.label_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.panel_2, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.panel_3, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.TextFolder, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 1)
        grid_sizer_1.Add(self.ButtonOpen, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.label_2, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add(self.label_3, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add(self.label_4, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add(self.ProductCombo, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.StationCombo, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.FixtureCombo, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.label_5, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add(self.panel_4, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.panel_7, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.TextFileName, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.panel_5, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.panel_8, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.ButtonOk, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.panel_6, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.ButtonCancel, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def Exit(self, event):  # wxGlade: MyFrame.<event_handler>
        exit()

    def Click(self, event):  # wxGlade: MyFrame.<event_handler>
        app_input2 = wx.PySimpleApp()
        #dialog = wx.TextEntryDialog(None, "Please Input CSV file Path:", "Text Entry", "", style=wx.OK|wx.CANCEL)
        dialog = wx.FileDialog(None, message="Choose the directory of the CSV files.", defaultDir="", defaultFile="", wildcard="*.csv*", style=0)
        dialog.Center()
        if dialog.ShowModal() == wx.ID_OK:
            #print ¡±You entered: %s¡± % dialog.GetValue()
            TargetPath = dialog.GetDirectory()
            self.TextFolder.Value = TargetPath

##################################################################################################################

    def ProductChoose(self, event):  # wxGlade: MyFrame.<event_handler>
        print(self.ProductCombo.Value)
        # Re-init the list
        #StationName = {1:"Null", 2:"Null", 3:"Null", 4:"Null", 5:"Null", 6:"Null", 7:"Null", 8:"Null", 9:"Null", 10:"Null", 11:"Null", 12:"Null", 13:"Null", 14:"Null", 15:"Null", 16:"Null", 17:"Null", 18:"Null", 19:"Null", 20:"Null", 21:"Null", 22:"Null", 23:"Null", 24:"Null", 25:"Null", 26:"Null", 27:"Null", 28:"Null", 29:"Null", 30:"Null"}
        StationList = [] 
        TempSelection = self.ProductCombo.Value
        for key in ProductName.keys():
            if(TempSelection == ProductName[key]):
                ProductType = key
                print(key)
                
        f=open('Config.v','r')
        TempNum = 0
        TempCounter = 0
        # Fatch the Test Station List which Product is selected
        for line in f:
            TempNum +=1
            if (TempNum >= ProductLineNum[ProductType-1]) and (TempNum <= ProductLineNum[ProductType]) :
                if line[0] == 'S':
                    TempCounter += 1
                    StationName[TempCounter] = line
                    StationLineNum.append(TempNum)
                if line == "END\n":
                    TempCounter += 1
                    StationName[TempCounter] = "Null"
                    StationLineNum.append(TempNum)
        #print(StationName)
        #print(StationLineNum)
        TempNum = 0
        TempCounter = 0
        #print("*******************************************")
        #print("Input the Index to Choose the Test Station Name:")
        for item in StationName:
            if StationName[item] != "Null" :
                StationList.append(StationName[item])
                #print(item,StationName[item])
        self.StationCombo.Clear()
        self.StationCombo.AppendItems(StationList)
        
##################################################################################################################
        
    def StationChoose(self, event):  # wxGlade: MyFrame.<event_handler>
        print(self.StationCombo.Value)
        # Re-init the list
        #ModelName = {1:"Null", 2:"Null", 3:"Null", 4:"Null", 5:"Null", 6:"Null", 7:"Null", 8:"Null", 9:"Null", 10:"Null", 11:"Null", 12:"Null", 13:"Null", 14:"Null", 15:"Null", 16:"Null", 17:"Null", 18:"Null", 19:"Null", 20:"Null", 21:"Null", 22:"Null", 23:"Null", 24:"Null", 25:"Null", 26:"Null", 27:"Null", 28:"Null", 29:"Null", 30:"Null"}
        ModelMenu = []
        ModelIndex = []
        TempModelList = ""
        TempStationType = 0
        TempSelection = self.StationCombo.Value
        for key in StationName.keys():
            if(TempSelection == StationName[key]):
                TempStationType = key
                print(key)
                
        f=open('Config.v','r')
        TempNum = 0
        TempCounter = 0
        TempModelList = ""
        # Fatch the Fixture Model List which Station is selected
        for line in f:
            TempNum +=1
            if (TempNum >= StationLineNum[TempStationType-1]) and (TempNum <= StationLineNum[TempStationType]) :
                if line[0] == 'M':
                    TempModelList = line;
                    TargetLineNum = TempNum
        TempNum = 0
        TempCounter = 0

        if ModelList != "MODEL:NULL\n":
            for item in TempModelList:
                if item == ':':
                    TempCounter = 1
                    ModelIndex.append(TempNum)
                if item == ';':
                    #ModelName[Counter]=ModelList
                    ModelIndex.append(TempNum)
                    ModelName[TempCounter]=TempModelList[ModelIndex[TempCounter-1]+1 : ModelIndex[TempCounter]]
                    TempCounter +=1
                TempNum +=1
            #print("*******************************************")
            #print("Input the Index to Choose the Fixture Type:")
            for item in ModelName:
                if ModelName[item] != "Null" :
                    ModelMenu.append(ModelName[item])
                    #print(item,ModelName[item])

        self.FixtureCombo.Clear()
        self.FixtureCombo.AppendItems(ModelMenu)

##################################################################################################################

    def FixtureChoose(self, event):
        print(self.FixtureCombo.Value)
        print(ModelName)
        
# end of class MyFrame
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Center()
    frame_1.Show()
    app.MainLoop()
