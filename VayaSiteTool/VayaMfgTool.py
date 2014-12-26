# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import PyQt4.QtGui, PyQt4.QtCore, sys

from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_VayaMfgMainWin import Ui_MainWindow
from Ui_IdInput import Ui_EnterOperatorID

import SJPControl
import PPParse
import ExtractFile
#import Ui_Info
#import Ui_IdInput
import webbrowser


from datetime import date
import datetime
import time
import threading

import os

########################################################################################
# Globe Variable and Constant
global VayaSN
global VayaSNNum
global TestCounterOK, TestCounterNG
global t
global BroadcastUID
global C

SoftwareVersion = 'V1.0.0'

BroadcastUID = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
TestCounterOK = 0
TestCounterNG = 0

LogFileName = 'LogFile_'+time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))+'.txt'
f = open("Logs\\"+LogFileName, 'w')

########################################################################################

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
        self.label_version.setText(SoftwareVersion)
        
        #Update the Date
        i = datetime.date.today()
        ProductDate = date.isoformat(i)
        self.lineEdit_Today.setText(ProductDate)
        
        self.tabWidget.setEnabled(False)
        self.setWindowIcon(PyQt4.QtGui.QIcon("Data/Vaya.png"))
        
        #Set the channel number from 1 to 512 at Channel Test Tab
        for r in range(32):
            for c in range(16):
                t = r*16 + c + 1
                item = PyQt4.QtGui.QTableWidgetItem(str(t))
                self.tableWidget_channeltest.setItem(r, c, item)
        
        
        #Show the SJP device picture but not connect
        pixmap = PyQt4.QtGui.QPixmap( 'Data//sjp_off.jpg' )
        PP = PyQt4.QtGui.QImage( pixmap )
        self.label_SJP.setPixmap(pixmap)
        
        # Record History
        f.write(time.strftime('%Y/%m/%d_%H:%M:%S',time.localtime(time.time()))+' Software Startup. '+'\n')
        
        self.ConnectDeviceButton.setEnabled(True)
        
        

    def closeEvent(self, event):
        #SJPControl.Close_SJP()
        #Log file close before quit
        # Record History
        
        f.write(time.strftime('%Y/%m/%d_%H:%M:%S',time.localtime(time.time()))+' Software Terminated.'+'\n')
        f.close()
        sys.exit(app2.exec_())
        
    #Show info msg of the software
    @pyqtSignature("")
    def on_commandLinkButton_info_clicked(self):
        Dialog = PyQt4.QtGui.QDialog()
        ui = Ui_Info.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.exec_()
        #Dialog.show()
    
    #open help file
    @pyqtSignature("")
    def on_commandLinkButton_help_clicked(self):
        webbrowser.open("Data\\User Manual.html")
        
##########################################################################################################
# Device Connect
##########################################################################################################
    @pyqtSignature("")
    def on_ConnectDeviceButton_clicked(self):
        """
        Connect the Smart Jack Pro.
        """
        if(SJPControl.Open_SJP()==1):
            self.label_Device_Status_2.setText('Connected SN:'+SJPControl.SJP_SN)
            self.DisconnectDeviceButton.setEnabled(True)
            self.ConnectDeviceButton.setEnabled(False)
            self.tabWidget.setEnabled(True)
            self.label_Device_Status_2.setStyleSheet("QLabel { background-color: rgb(0, 255, 0) }")
            pixmap = PyQt4.QtGui.QPixmap( 'Data//sjp_on.jpg' )
            PP = PyQt4.QtGui.QImage( pixmap )
            self.label_SJP.setPixmap(pixmap)
            # Record History
            f.write(time.strftime('%Y/%m/%d_%H:%M:%S',time.localtime(time.time()))+' Smart Jack Pro Connected:'+SJPControl.SJP_SN+'\n')
            
        else:
            self.label_Device_Status_2.setText('No Smart Jack Pro Connected')
            self.DisconnectDeviceButton.setEnabled(False)
            self.ConnectDeviceButton.setEnabled(True)
            self.tabWidget.setEnabled(False)
            self.label_Device_Status_2.setStyleSheet("QLabel { background-color: rgb(255, 255, 255) }")
            pixmap = PyQt4.QtGui.QPixmap( 'Data//sjp_off.jpg' )
            PP = PyQt4.QtGui.QImage( pixmap )
            self.label_SJP.setPixmap(pixmap)
            PyQt4.QtGui.QMessageBox.warning(self, "Warning", "No SJP Detected. \nPlease Check the USB Cable \nOr Device Driver." ,1, 0)
        
    @pyqtSignature("")
    def on_DisconnectDeviceButton_clicked(self):
        """
        Disconnect the Smart Jack Pro.
        """
        SJPControl.Close_SJP()
        self.label_Device_Status_2.setText('No Smart Jack Pro Connected')
        self.DisconnectDeviceButton.setEnabled(False)
        self.ConnectDeviceButton.setEnabled(True)
        self.tabWidget.setEnabled(False)
        self.label_Device_Status_2.setStyleSheet("QLabel { background-color: rgb(255, 255, 255) }")
        pixmap = PyQt4.QtGui.QPixmap( 'Data//sjp_off.jpg' )
        PP = PyQt4.QtGui.QImage( pixmap )
        self.label_SJP.setPixmap(pixmap)
        
        
    @pyqtSignature("int")
    def on_comboBox_ModelList_currentIndexChanged(self, index):
        try:
            self.lineEdit_foot.setText(str(PPParse.FootprintList[self.comboBox_ModelList.currentIndex()]))
        except:
            self.lineEdit_foot.setText('3')
        
    @pyqtSignature("")
    def on_pushButton_SelectPP_clicked(self):
        """
        Slot documentation goes here.
        """
        self.comboBox_ModelList.clear()
        PPFileName = PyQt4.QtGui.QFileDialog.getOpenFileName(self, self.tr("Please Select The PP File."), ".//Fixture Files", self.tr("PP files (*.PP)"))
        #print PPFileName
        if PPFileName=='':
            return
        
        self.lineEdit_PPname.setText(PPFileName[-17:])
        
        PPParse.ParsePP(PPFileName)
        
        self.lineEdit_FixtureModel.setText(PPParse.FixtureName)
        for item in PPParse.ModelList:
            self.comboBox_ModelList.addItem(item)
        
        self.comboBox_ModelList.setCurrentIndex(5) # default set to RGB model
        print PPParse.FootprintList
        self.lineEdit_foot.setText(str(PPParse.FootprintList[5]))
        pixmap = PyQt4.QtGui.QPixmap( 'data.BMP' )
        PP = PyQt4.QtGui.QImage( pixmap )
        self.Config_PP.setPixmap(pixmap)
        # Record History
        f.write(time.strftime('%Y/%m/%d_%H:%M:%S',time.localtime(time.time()))+' Selected PP file:'+PPFileName[-17:]+'\n')
        

    @pyqtSignature("")
    def on_pushButton_SetPara_clicked(self):
        try:
            SJPControl.Send_Get_SerialNumber()
        except:
            PyQt4.QtGui.QMessageBox.warning(self, "Warning", "SJP Communication ERROR, Please Try to re-connect" ,1, 0)
            SJPControl.Close_SJP()
            self.label_Device_Status_2.setText('No Smart Jack Pro Connected')
            self.DisconnectDeviceButton.setEnabled(False)
            self.ConnectDeviceButton.setEnabled(True)
            #self.tabWidget.setEnabled(False)
            self.label_Device_Status_2.setStyleSheet("QLabel { background-color: rgb(255, 255, 255) }")
            pixmap = PyQt4.QtGui.QPixmap( 'Data//sjp_off.jpg' )
            PP = PyQt4.QtGui.QImage( pixmap )
            self.label_SJP.setPixmap(pixmap)
            return
            
        global BroadcastUID
        #print "This will set new UID and Model Description"
        #Make sure the parameters are valid!!!
        if self.lineEdit_ProgramUID.text() == "" or self.comboBox_ModelList.count()==0:
            #print "No SN Assign"
            PyQt4.QtGui.QMessageBox.warning(self, "Warning", "No SN Assigned!" ,1, 0)
            return
        UUID = self.lineEdit_ProgramUID.text()
        if len(UUID)!= 8 :
            #print "UID Length ERROR"
            PyQt4.QtGui.QMessageBox.warning(self, "Warning", "UID Length Not Match!" ,1, 0)
            return
        for item in UUID:
            if PyQt4.QtCore.QChar(item).isDigit():
                continue
            elif item!='A' and item!='B' and  item!='C' and  item!='D' and  item!='E' and  item!='F' and  item!='a' and   item!='b' and  item!='c' and  item!='d' and  item!='e' and  item!='f' and item!=':':
                #print "UID Format ERROR"
                PyQt4.QtGui.QMessageBox.warning(self, "Warning", "UID Format Not Match!" ,1, 0)
                return
        
        NewModel = self.comboBox_ModelList.currentText()
        if NewModel =='':
            PyQt4.QtGui.QMessageBox.warning(self, "Warning", "Missing Model Description!" ,1, 0)
            return
            
        TargetSetUID = []
        for i in range(0, 8, 2): 
            TempCode = UUID[i:i+2]
            SingleCode = 0x00

            IDC1 = PyQt4.QtCore.QChar(TempCode[0])
            IDC2 = PyQt4.QtCore.QChar(TempCode[1])
            if IDC1.isDigit():
                SingleCode = IDC1.digitValue()*16
            elif IDC1.isLower():
                SingleCode = (ord((IDC1.toUpper()).toAscii())-55)*16
            else:
                SingleCode = (ord(IDC1.toAscii())-55)*16
            
            if IDC2.isDigit():
                SingleCode += IDC2.digitValue()
            elif IDC2.isLower():
                SingleCode += (ord((IDC2.toUpper()).toAscii())-55)
            else:
                SingleCode += (ord(IDC2.toAscii())-55)

            TargetSetUID.append(SingleCode)
            
        TargetSetUID = [0x50,  0x68] + TargetSetUID
        #print TargetSetUID
        #print NewModel
        
        time.sleep(0.5)
        SJPControl.RDM_Set_NumOfOutput(TargetSetUID,  0x03)
        
        time.sleep(1)#must have delay!!
        for i in range(len(NewModel), 32):
            NewModel +=' '
        SJPControl.RDM_Set_Model_Description (TargetSetUID, NewModel)
        
        
        time.sleep(1.5)
        GetModel = SJPControl.RDM_Get_Device_Model_Description(TargetSetUID)
        #print GetModel
        #print "G:", GetModel[0:len(NewModel)]
        #print "N:", NewModel[0:len(NewModel)]
        if GetModel[0:len(NewModel)]==NewModel[0:len(NewModel)]:
            PyQt4.QtGui.QMessageBox.information(self, "OK", "Set Parameters OK!" ,1, 0)
            self.lineEdit_ProgramUID.setText('') #After set successfully, empty the input
            # Record History
            f.write(time.strftime('%Y/%m/%d_%H:%M:%S',time.localtime(time.time()))+' Set Fixture Parameter OK'+' '+UUID+' '+NewModel+'.\n')
        else :
            PyQt4.QtGui.QMessageBox.critical(self, "Fail", "Set Parameters Fail!" ,1, 0)
            # Record History
            f.write(time.strftime('%Y/%m/%d_%H:%M:%S',time.localtime(time.time()))+' Set Fixture Parameter FAIL'+' '+UUID+' '+NewModel+'.\n')
        
        self.comboBox_ModelList.clear()
        self.lineEdit_PPname.setText('')
        self.lineEdit_foot.setText('')
        self.lineEdit_FixtureModel.setText('')
        pixmap = PyQt4.QtGui.QPixmap( '' )
        PP = PyQt4.QtGui.QImage( pixmap )
        self.Config_PP.setPixmap(pixmap)
        
        
    @pyqtSignature("")
    def on_pushButton_GetPara_clicked(self):
        CheckFixture = []
        UUID=self.lineEdit_ProgramUID.text()
        TargetUID = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        self.Readback_UID.setText('-')
        self.Readback_DMX.setText('-')
        self.Readback_Model.setText('-')
        self.Readback_MID.setText('-')
        self.Readback_Footprint.setText('-')
        self.Readback_FWversion.setText('-')
        self.Readback_RDMversion.setText('-')
        self.Readback_Device.setText('-')
        
        if self.lineEdit_ProgramUID.text() == "" :
        #print "No SN Assign"
            PyQt4.QtGui.QMessageBox.warning(self, "Warning", "No SN Assigned!" ,1, 0)
            return
        UUID = self.lineEdit_ProgramUID.text()
        if len(UUID)!= 8 :
            #print "UID Length ERROR"
            PyQt4.QtGui.QMessageBox.warning(self, "Warning", "UID Length Not Match!" ,1, 0)
            return
        for item in UUID:
            if PyQt4.QtCore.QChar(item).isDigit():
                continue
            elif item!='A' and item!='B' and  item!='C' and  item!='D' and  item!='E' and  item!='F' and  item!='a' and   item!='b' and  item!='c' and  item!='d' and  item!='e' and  item!='f' and item!=':':
                #print "UID Format ERROR"
                PyQt4.QtGui.QMessageBox.warning(self, "Warning", "UID Format Not Match!" ,1, 0)
                return
                
        TargetUID = []
        for i in range(0, 8, 2): 
            TempCode = UUID[i:i+2]
            SingleCode = 0x00

            IDC1 = PyQt4.QtCore.QChar(TempCode[0])
            IDC2 = PyQt4.QtCore.QChar(TempCode[1])
            if IDC1.isDigit():
                SingleCode = IDC1.digitValue()*16
            elif IDC1.isLower():
                SingleCode = (ord((IDC1.toUpper()).toAscii())-55)*16
            else:
                SingleCode = (ord(IDC1.toAscii())-55)*16
            
            if IDC2.isDigit():
                SingleCode += IDC2.digitValue()
            elif IDC2.isLower():
                SingleCode += (ord((IDC2.toUpper()).toAscii())-55)
            else:
                SingleCode += (ord(IDC2.toAscii())-55)

            TargetUID.append(SingleCode)
            
        TargetUID = [0x50,  0x68] + TargetUID
        
        try:
            CheckFixture = SJPControl.RDM_Get_Device_Info(TargetUID)
        except:
            PyQt4.QtGui.QMessageBox.warning(self, "Warning", "SJP Communication ERROR, Please Try to re-connect" ,1, 0)
            SJPControl.Close_SJP()
            self.label_Device_Status_2.setText('No Smart Jack Pro Connected')
            self.DisconnectDeviceButton.setEnabled(False)
            self.ConnectDeviceButton.setEnabled(True)
            #self.tabWidget.setEnabled(False)
            self.label_Device_Status_2.setStyleSheet("QLabel { background-color: rgb(255, 255, 255) }")
            pixmap = PyQt4.QtGui.QPixmap( 'Data//sjp_off.jpg' )
            PP = PyQt4.QtGui.QImage( pixmap )
            self.label_SJP.setPixmap(pixmap)
            return
        
        print CheckFixture
        if CheckFixture == 0:
            PyQt4.QtGui.QMessageBox.warning(self, "Warning", "No Unit Found!" ,1, 0)
            return
            
        #GetModel = SJPControl.RDM_Get_Device_Model_Description(TargetUID)
        time.sleep(0.2)
        GetUID = SJPControl.RDM_Get_UID(TargetUID)
        #print GetModel,  GetUID
        self.comboBox_ModelList.clear()
        #self.comboBox_ModelList.addItem(GetModel)
        #self.Readback_Model.setText(GetModel)
        
        self.Readback_UID.setText(UUID.toUpper())
        newItem = PyQt4.QtGui.QTableWidgetItem(SJPControl.RDM_Get_DMX_Start_Address(TargetUID))
        self.Readback_DMX.setText(newItem.text())
        newItem2 = PyQt4.QtGui.QTableWidgetItem(SJPControl.RDM_Get_Device_Model_Description(TargetUID))
        self.Readback_Model.setText(newItem2.text())
        DeviceInfo = list(SJPControl.RDM_Get_Device_Info(TargetUID))
        newItem3 = PyQt4.QtGui.QTableWidgetItem(SJPControl.ConvertRDMVersion2ASCII(DeviceInfo[0:2]))
        newItem4 = PyQt4.QtGui.QTableWidgetItem(SJPControl.ConvertFootprint2ASCII(DeviceInfo[11]))
        self.Readback_RDMversion.setText(newItem3.text())
        self.Readback_Footprint.setText(newItem4.text())
        newItem5 = PyQt4.QtGui.QTableWidgetItem(SJPControl.RDM_Get_Software_Version(TargetUID))
        self.Readback_FWversion.setText(newItem5.text())
        newItem6 = PyQt4.QtGui.QTableWidgetItem(SJPControl.RDM_Get_Mfg_Label(TargetUID))
        self.Readback_MID.setText(newItem6.text())
        newItem7 = PyQt4.QtGui.QTableWidgetItem(SJPControl.RDM_Get_Device_Label(TargetUID))
        self.Readback_Device.setText(newItem7.text())
        
        
        if GetUID != 0 :
            TempUID = [GetUID]
            SJPControl.ConvertSN2ASCII(TempUID)
            #print SJPControl.FixtureSN
            #print SJPControl.FixtureSN[0][5:]
            self.lineEdit_ProgramUID.setText(SJPControl.FixtureSN[0][5:])
            IDSeq = ((GetUID[-2]&0x01)<<8)+GetUID[-1]
            #print IDSeq
            CMID = (GetUID[-2]&0x0E)>>1
            #print CMID
            
            #if the function not for CM
            #self.comboBox_CMList.setCurrentIndex(CMID)
            #self.spinBox.setValue(IDSeq)
            self.lineEdit_foot.setText(' ')
        else:
            PyQt4.QtGui.QMessageBox.warning(self, "Warning", "Can not read Fixture Parameter." ,1, 0)
            

    @pyqtSignature("int, int")
    def on_tableWidget_channeltest_cellPressed(self, row, column):
        ChannelValue = [0x00]*512
        for ROW in range(32):
            for COL in range(16):
                ChannelItem = self.tableWidget_channeltest.item(ROW, COL)
                if self.tableWidget_channeltest.isItemSelected(ChannelItem):
                    #print ROW, COL
                    ChannelValue[ROW*16+COL] = self.horizontalSlider_value.value()
        SJPControl.Send_DMX_Packet(ChannelValue)
        
        
    @pyqtSignature("")
    def on_pushButton_testchannelAllOff_clicked(self):
        #print "All Off"
        for ROW in range(32):
            for COL in range(16):
                ChannelItem = self.tableWidget_channeltest.item(ROW, COL)
                ChannelItem.setSelected(False)
        payload = [0x00]*512
        SJPControl.Send_DMX_Packet(payload)
        
    @pyqtSignature("")
    def on_pushButton_testchannelAllOn_clicked(self):
        #print "All On"
        for ROW in range(32):
            for COL in range(16):
                ChannelItem = self.tableWidget_channeltest.item(ROW, COL)
                ChannelItem.setSelected(True)
        payload = [0xFF]*512
        SJPControl.Send_DMX_Packet(payload)

    @pyqtSignature("int")
    def on_horizontalSlider_2_valueChanged(self, int):
        #print self.horizontalSlider_2.value()
        self.label_10.setText(str(self.horizontalSlider_2.value()))
        
    @pyqtSignature("int")
    def on_horizontalSlider_value_valueChanged(self, int):
        self.spinBox_2.setValue(self.horizontalSlider_value.value())
        
        ChannelValue = [0x00]*512
        for ROW in range(32):
            for COL in range(16):
                ChannelItem = self.tableWidget_channeltest.item(ROW, COL)
                if self.tableWidget_channeltest.isItemSelected(ChannelItem):
                    #print ROW, COL
                    ChannelValue[ROW*16+COL] = self.horizontalSlider_value.value()
        SJPControl.Send_DMX_Packet(ChannelValue)
    

    
def FixedColorOutput (Name, R, G, B):
    payload = []
    restdata = [R, G, B] * 170 + [R, G]
    payload.extend(restdata)
    SJPControl.Send_DMX_Packet(payload)
    
    
 
if __name__ == "__main__":

    app2 = PyQt4.QtGui.QApplication(sys.argv)
    ui2 = MainWindow() #should use local class
    ui2.show()

    sys.exit(app2.exec_())
    
    
    
    
    
