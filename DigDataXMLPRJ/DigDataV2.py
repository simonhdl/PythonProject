# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import PyQt4, PyQt4.QtGui, PyQt4.QtCore, sys
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import QDir
from PyQt4.QtCore import QFile

from Ui_MainMenu import Ui_Dialog

# Import Library
import csv
import sys
import os
import glob
import time
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
ItemFailFormat = easyxf( 'font: colour red, height 150;' 'pattern: fore_colour white;' 'alignment: horizontal center;' )
# Define variable
SheetName = "TestData"
Sheet2Name = "Summary"

PF = []
temp = []
TestTime = []
PartNumber = []
Result = []
Num = 0
Num2 = 0
Counter = 0

# Save the string index for title
TitleList = []
TitleIndex = []
# Save the cell location index for cell which we want to extract
CellList = []

# Locate the xml location
#RootDir = 'C:\\Users\\310098157\\Dropbox\\Works@PCK\\Engineering\\Working Directory\\Software Project\\Python Project\\DigData with XML\\'
RootDir = ''
XMLFileName = 'config.xml'
FolderDir = ''

################################################################################
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

################################################################################
# Define Function for conversion location
Coordinator = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26, 'AA':27, 'AB':28, 'AC':29, 'AD':30, 'AE':31, 'AF':32, 'AG':33, 'AH':34, 'AI':35, 'AJ':36, 'AK':37, 'AL':38, 'AM':39, 'AN':40, 'AO':41, 'AP':42, 'AQ':43, 'AR':44, 'AS':45, 'AT':46, 'AU':47, 'AV':48, 'AW':49, 'AX':50}                                                 
Coor_X = 0
Coor_Y = 0
def StrConversionX ( InputStr ):
    if InputStr[1].isalpha():
        return Coordinator.get(InputStr[0:2])
    else:
        return Coordinator.get(InputStr[0])
def StrConversionY ( InputStr ):
    if InputStr[1].isalpha():
        return int(InputStr[2:])
    else:
        return int(InputStr[1:])



class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        ProductList = []
        self.ProductBox.addItem(' ')
        try:
            tree = ET.parse(RootDir+XMLFileName)
            XMLRoot = tree.getroot()
            for child in XMLRoot:
                #print child.tag, child.attrib
                if child.tag == 'ProductList' :
                    ProductList.append(child.attrib['ProductName'])
        except IOError:
            PyQt4.QtGui.QMessageBox.warning(self, "Missing Config file",
                                "Please locate valid config file."
                                 ,1, 0)
            sys.exit(app.exec_())
            
        for item in ProductList:
            self.ProductBox.addItem(item)
    
    @pyqtSignature("QString")
    def on_ProductBox_activated(self, index):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        StationList = []
        
        tree = ET.parse(RootDir+XMLFileName)
        XMLRoot = tree.getroot()
        for child in XMLRoot:
            if ((child.tag == 'ProductList') and (child.attrib['ProductName'] == self.ProductBox.currentText()))  :
                for subchild in child:
                #print subchild.tag, subchild.attrib
                    if subchild.tag == 'TestStation':
                        StationList.append(subchild.attrib['StationName'])
        
        self.StationBox.clear()
        self.StationBox.addItem(' ')
        for item in StationList:
            self.StationBox.addItem(item)

    @pyqtSignature("QString")
    def on_StationBox_activated(self, index):
        """
        Slot documentation goes here.
        """
        ModelList = []
        
        tree = ET.parse(RootDir+XMLFileName)
        XMLRoot = tree.getroot()
        for child in XMLRoot:
            if ((child.tag == 'ProductList') and (child.attrib['ProductName'] == self.ProductBox.currentText()))  :
                for subchild in child:

                    if (subchild.tag == 'TestStation') and (subchild.attrib['StationName'] == self.StationBox.currentText()):
                        for subsubchild in subchild:
                            if subsubchild.tag =='ModelList':
                                ModelList.append(subsubchild.attrib['Name'])
        
        self.ModelBox.clear()
        self.ModelBox.addItem('')
        for item in ModelList:
            self.ModelBox.addItem(item)

    @pyqtSignature("QString")
    def on_ModelBox_activated(self, p0):
        """
        Slot documentation goes here.
        """
        global TitleIndex
        global CellIndex
        TitleIndex = []
        CellIndex = []
        tree = ET.parse(RootDir+XMLFileName)
        XMLRoot = tree.getroot()
        for child in XMLRoot:
            if ((child.tag == 'ProductList') and (child.attrib['ProductName'] == self.ProductBox.currentText()))  :
                for subchild in child:
                    if (subchild.tag == 'TestStation') and (subchild.attrib['StationName'] == self.StationBox.currentText()):
                        for subsubchild in subchild:
                            if (subsubchild.tag =='ModelList') and (subsubchild.attrib['Name'] == self.ModelBox.currentText()):
                                for subsubsubchild in subsubchild:
                                    if subsubsubchild.tag == 'ReportData' :
                                        TitleIndex.append(subsubsubchild.attrib['Title'])
                                        CellIndex.append(subsubsubchild.attrib['Cell'])
        #print TitleIndex
        #print CellIndex
        self.textEdit.clear()
        DataLog1 = ', '.join(TitleIndex)
        DataLog2 = ', '.join(CellIndex)
        DataLog3 = DataLog1+'\n'+DataLog2
        self.textEdit.setText(DataLog3)
          
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        ProgBarValue =0
        FolderDir = PyQt4.QtGui.QFileDialog.getExistingDirectory(self, self.tr("Please Select the CSV file Folder."), "" ,PyQt4.QtGui.QFileDialog.ShowDirsOnly)
        self.lineEdit.setText(FolderDir)
        
        JuFolder = QDir(FolderDir)
        JuFolder.setCurrent(FolderDir)
        for fileName in glob.glob( '*.csv'):
            ProgBarValue = ProgBarValue +1
                
        if ProgBarValue == 0:
            PyQt4.QtGui.QMessageBox.warning(self, "No CSV Files", "This folder contains no CSV files, please select again." ,1, 0)
        
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        PF = ''
        Result = []
        ProgBarValue = 0
        # TODO: not implemented yet
        if self.StationBox.count() == 0:
            PyQt4.QtGui.QMessageBox.warning(self, "Not select Station or Model yet",
                                "Please select correct Station name and Model Name."
                                   ,1, 0)
        if self.lineEdit_2.text() == '':
            PyQt4.QtGui.QMessageBox.warning(self, "Missing file name",
                                "Please input the file name."
                                 ,1, 0)
        else:                      
            FileName = self.lineEdit_2.text()
            FolderDir = self.lineEdit.text()
            CurrentFolder = QDir(FolderDir)
            ResultFolder = QDir(FolderDir + "\\Result\\" )
            ResultFolder2 = FolderDir + "\\Result\\"
            CurrentFile = QFile(FileName+".xls")

            # Generate the title according to the configuration file
            print TitleIndex
            for item in TitleIndex:
                if item != "Null":
                    sheet1.write(0,TitleIndex.index(item)+3,item,TitleFormat)
                    sheet1.col(TitleIndex.index(item)+3).width = 4000

            ResultFolder.setCurrent(FolderDir)
            for fileName in glob.glob( '*.csv'):
                ProgBarValue = ProgBarValue +1
                
            if ProgBarValue == 0:
                    PyQt4.QtGui.QMessageBox.warning(self, "No CSV Files",
                                "This folder contains no CSV files, please select again."
                                 ,1, 0)
                                 
            for fileName in glob.glob( '*.csv'):
                Num = glob.glob( '*.csv').index(fileName)+1
                print glob.glob( '*.csv').index(fileName), ":", fileName
                self.progressBar.setValue(round(float(Num)/float(ProgBarValue)*100))
                
                # Open CSV file and use ',' to seperate the column
                reader = csv.reader(open(fileName), delimiter=",")
                # First Column to Save File name instead of Serial No. or Test Time
                sheet1.row(Num).write(0, fileName, NormalFormat)

                for row in reader: # search every row in the csv file
                    if row != [] and row[0] == 'Part Number' :
                        PartNumber = row[1]
                        sheet1.row(Num).write(1, PartNumber, NormalFormat)
                    if row != [] and ( row[0] == 'OVERALL RESULT' or row[0] == 'DUT P/F' or row[0] == 'Overall Result' ) :
                        PF = row[1]
                        if (PF.find('F')>0) or (PF.find('f')>0):
                            sheet1.row(Num).write(2, PF, FailFormat)
                        else:
                            sheet1.row(Num).write(2, PF, PassFormat)
                    
                    for item in CellIndex:
                        if item != "Null":
                            if reader.line_num == (StrConversionY(item)):
                                if(row != [] and len(row)>= StrConversionX(item)):
                                    #Result.append(row[StrConversionX(item)-1])
                                    TempResult = row[StrConversionX(item)-1]
                                    if (TempResult.find('F')>0) or (TempResult.find('f')>0):
                                        sheet1.row(Num).write(CellIndex.index(item)+3, TempResult, FailFormat)
                                    else:
                                        if(str.isalpha(TempResult) or str.istitle(TempResult)): # if the contain is not numbers.
                                            sheet1.row(Num).write(CellIndex.index(item)+3, TempResult, NormalFormat)
                                        elif(str.isspace(TempResult)): # if the contain is not numbers.
                                            sheet1.row(Num).write(CellIndex.index(item)+3, TempResult, NormalFormat)
                                        else:
                                            if row[StrConversionX(item)].find('F')>0 :
                                                sheet1.row(Num).write(CellIndex.index(item)+3, float(TempResult), ItemFailFormat)
                                            else:
                                                sheet1.row(Num).write(CellIndex.index(item)+3, float(TempResult), NormalFormat)
                
                if Result==[] : continue
                #for i in range(0,len(Result)):
                #    if (Result[i].find('F')>0) or (Result[i].find('f')>0):
                #        sheet1.row(Num).write(i+3, Result[i], FailFormat)
                #    else:
                #        if(str.isalpha(Result[i])): # if the contain is not numbers.
                #            sheet1.row(Num).write(i+3, Result[i], NormalFormat)
                #        elif(str.isspace(Result[i])): # if the contain is not numbers.
                #            sheet1.row(Num).write(i+3, Result[i], NormalFormat)
                #        else:
                #            sheet1.row(Num).write(i+3, float(Result[i]), NormalFormat)

                #Result = []
                self.textEdit.append(fileName)
                
            ##################################################################    
            #Save to excel file, Save to the result folder in target directory
            if not(ResultFolder.exists()):
                CurrentFolder.mkdir(FolderDir+"\\Result\\")

            ResultFolder.setCurrent(ResultFolder2) # Set to the working folder!!
            if CurrentFile.exists():
                book.save(FileName+'-'+time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))+'.xls')
            else:
                book.save(FileName+'.xls')

            book.save(TemporaryFile())

            PyQt4.QtGui.QMessageBox.warning(self, "Done",
                                "Conversion Done!."
                                 ,1, 0)
            sys.exit(app.exec_())
    
    @pyqtSignature("")
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        sys.exit(app.exec_())

if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)
    ui = Dialog()
    ui.show()
    sys.exit(app.exec_())
    

