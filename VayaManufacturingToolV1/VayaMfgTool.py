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
import Ui_Info
import Ui_IdInput
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

#CMList = [['000', 'Opulent'], ['001', 'SSZ'], ['010', 'Primo'], ['011', 'AVC'], ['100', 'VTECH'], ['101', 'SengLED'], ['110', 'QiRui'], ['111', 'BOI']]
# stands for 000,001,010,011,100,101,110,111
CMList = ['Opulent', 'SSZ', 'Primo', 'AVC', 'VTECH', 'SengLED', 'QiRui', 'BOI']
SoftwareVersion = 'V1.1.0'

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
        
        #Update CM List into ComboBox
        for item in CMList:
            self.comboBox_CMList.addItem(item)
        
        #Update the Date
        i = datetime.date.today()
        ProductDate = date.isoformat(i)
        self.lineEdit_Today.setText(ProductDate)
        
        self.lineEdit_UID.setReadOnly(True)
        self.tableWidget_DiscoverFixtures.resizeColumnsToContents()
        self.tabWidget.setEnabled(False)
        self.pushButton_test_2.setEnabled(False)
        self.setWindowIcon(PyQt4.QtGui.QIcon("Data/Vaya.png"))
        self.pushButton_washstart.setEnabled(True)
        self.pushButton_washstop.setEnabled(False)
        
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
        
        DD = EnterOperatorID(parent = self)
        DD.show()
        
        # Record History
        f.write(time.strftime('%Y/%m/%d_%H:%M:%S',time.localtime(time.time()))+' Software Startup. '+'\n')
        
        self.ConnectDeviceButton.setEnabled(False)

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
        
##########################################################################################################
# Configuration Tab
##########################################################################################################
    @pyqtSignature("")
    def on_GenerateUID_clicked(self):
        """
        Slot documentation goes here.
        """
        global VayaSN
        global VayaSNNum
        
        # Calculation the UID based on the data code from 2000-01-01
        today = datetime.date.today()
        someday = datetime.date(2000, 1, 1)
        diff = today - someday
        DayCount = diff.days +1
        DAYS = bin(DayCount)
        DC= DAYS[-13:]
        DCLen = len(DC)
        MFGID = '000101' #fixed MFG ID
        DATECODE = '00000000000001'
        FID = bin(self.comboBox_CMList.currentIndex())
        FID = FID[2:]
        if(len(FID)==1):
            FID = '00'+FID
        elif(len(FID)==2):
            FID = '0'+FID
        SN = '000000001'
        DATECODE = DATECODE.replace(DATECODE[-(DCLen):],DC)
        VayaSNTemp = MFGID + DATECODE + FID + SN
        
        num = 0
        for i in range(32):
            num = num+int(VayaSNTemp[i])*(2**(31-i))
        
        VayaSNNum = num
        VayaSN = hex(VayaSNNum)
        VayaSN = VayaSN.upper()
        VayaSN = VayaSN[2:10]
        #print "Generate UID of Today : ",VayaSN
        self.lineEdit_UID.setText("5068:"+VayaSN)
        
        VayaSN = hex(VayaSNNum+self.spinBox.value()-1)
        VayaSN = VayaSN.upper()
        VayaSN = VayaSN[2:10]
        self.lineEdit_ProgramUID.setText("5068:"+VayaSN)

    @pyqtSignature("int")
    def on_spinBox_valueChanged(self, p0):
        VayaSN = hex(VayaSNNum+self.spinBox.value()-1)
        VayaSN = VayaSN.upper()
        VayaSN = VayaSN[2:10]
        self.lineEdit_ProgramUID.setText("5068:"+VayaSN)

    @pyqtSignature("int")
    def on_comboBox_CMList_currentIndexChanged(self, index):
        global VayaSN
        global VayaSNNum
        
        today = datetime.date.today()
        someday = datetime.date(2000, 1, 1)
        diff = today - someday
        DayCount = diff.days +1
        DAYS = bin(DayCount)
        DC= DAYS[-13:]
        DCLen = len(DC)
        MFGID = '000101'
        DATECODE = '00000000000001'
        FID = bin(self.comboBox_CMList.currentIndex())
        FID = FID[2:]
        if(len(FID)==1):
            FID = '00'+FID
        elif(len(FID)==2):
            FID = '0'+FID
        SN = '000000001'
        DATECODE = DATECODE.replace(DATECODE[-(DCLen):],DC)
        VayaSNTemp = MFGID + DATECODE + FID + SN
        
        num = 0
        for i in range(32):
            num = num+int(VayaSNTemp[i])*(2**(31-i))
        
        VayaSNNum = num
        VayaSN = hex(VayaSNNum)
        VayaSN = VayaSN.upper()
        VayaSN = VayaSN[2:10]
        #print "Generate UID of Today : ",VayaSN
        self.lineEdit_UID.setText("5068:"+VayaSN)
        
        VayaSN = hex(VayaSNNum+self.spinBox.value()-1)
        VayaSN = VayaSN.upper()
        VayaSN = VayaSN[2:10]
        self.lineEdit_ProgramUID.setText("5068:"+VayaSN)
        
        
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
        if len(UUID)!= 13 :
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
        for i in range(5, 13, 2):
            TempCode = UUID[i:i+2]
            SingleCode = 0x00

            IDC1 = PyQt4.QtCore.QChar(TempCode[0])
            IDC2 = PyQt4.QtCore.QChar(TempCode[1])
            if IDC1.isDigit():
                SingleCode = IDC1.digitValue()*16
            else:
                SingleCode = (ord(IDC1.toAscii())-55)*16
                
            if IDC2.isDigit():
                SingleCode += IDC2.digitValue()
            else:
                SingleCode += (ord(IDC2.toAscii())-55)

            TargetSetUID.append(SingleCode)
        
        TargetSetUID = [0x50,  0x68] + TargetSetUID
        #print TargetSetUID
        #print NewModel
        SJPControl.RDM_Set_NewUID(BroadcastUID, TargetSetUID)
        time.sleep(0.5)#must have delay!!
        for i in range(len(NewModel), 32):
            NewModel +=' '
        SJPControl.RDM_Set_Model_Description (TargetSetUID, NewModel)
        
        time.sleep(1.0)
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
        
        
    @pyqtSignature("")
    def on_pushButton_GetPara_clicked(self):
        TargetUID = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        try:
            SJPControl.RDM_Get_Device_Info(TargetUID)
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
        
        #print "Get Parameter"
        time.sleep(0.2)
        
        GetModel = SJPControl.RDM_Get_Device_Model_Description(TargetUID)
        time.sleep(0.2)
        GetUID = SJPControl.RDM_Get_UID(TargetUID)
        #print GetModel,  GetUID
        self.comboBox_ModelList.clear()
        self.comboBox_ModelList.addItem(GetModel)
        
        if GetUID != 0 :
            TempUID = [GetUID]
            SJPControl.ConvertSN2ASCII(TempUID)
            #print SJPControl.FixtureSN
            #print SJPControl.FixtureSN[0][5:]
            self.lineEdit_ProgramUID.setText("5068:"+SJPControl.FixtureSN[0][5:])
            IDSeq = ((GetUID[-2]&0x01)<<8)+GetUID[-1]
            #print IDSeq
            CMID = (GetUID[-2]&0x0E)>>1
            #print CMID
            
            #if the function not for CM
            #self.comboBox_CMList.setCurrentIndex(CMID)
            #self.spinBox.setValue(IDSeq)
            self.lineEdit_foot.setText('3')
            
    @pyqtSignature("")
    def on_pushButton_CH1_clicked(self):
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
            
        payload = [0xFF]
        restdata = [0x00]*511
        payload.extend(restdata)
        SJPControl.Send_DMX_Packet(payload)
    
    @pyqtSignature("")
    def on_pushButton_CH2_clicked(self):
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
            
        payload = [0x00, 0xFF]
        restdata = [0x00]*510
        payload.extend(restdata)
        SJPControl.Send_DMX_Packet(payload)
    
    @pyqtSignature("")
    def on_pushButton_CH3_clicked(self):
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
            
        payload = [0x00, 0x00, 0xFF]
        restdata = [0x00]*509
        payload.extend(restdata)
        SJPControl.Send_DMX_Packet(payload)
    
    @pyqtSignature("")
    def on_pushButton_CH4_clicked(self):
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
            
        payload = [0x00, 0x00, 0x00, 0xFF]
        restdata = [0x00]*508
        payload.extend(restdata)
        SJPControl.Send_DMX_Packet(payload)

    @pyqtSignature("")
    def on_pushButton_ALLON_clicked(self):
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
            
        payload = [0xFF]*512
        SJPControl.Send_DMX_Packet(payload)
        
    @pyqtSignature("")
    def on_pushButton_ALLOFF_clicked(self):
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
            
        payload = [0x00]*512
        SJPControl.Send_DMX_Packet(payload)

    @pyqtSignature("")
    def on_pushButton_test_clicked(self):
        '''
        global TestCounterOK, TestCounterNG
        TargetUID = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        GetUID = SJPControl.RDM_Get_UID(TargetUID)
        if GetUID == 0 :
            TestCounterNG += 1
            self.lcdNumber_2.display(TestCounterNG)
        else:
            TestCounterOK += 1
            self.lcdNumber.display(TestCounterOK)
        f.write(time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))+' Test Communication \n')    
        '''
        self.frame.setEnabled(False)
        self.frame_2.setEnabled(False)
        self.pushButton_test.setEnabled(False)
        self.pushButton_test_2.setEnabled(True)
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabEnabled(2, False)
        self.tabWidget.setTabEnabled(3, False)
        self.tabWidget.setTabEnabled(4, False)
        global t
        #print WashDelay
        t = threading.Thread(target=self.CommuncationTest,  args=("COMTEST", self))
        #print "START"
        t.start()
        
    @pyqtSignature("")
    def on_pushButton_test_2_clicked(self):
        global TestCounterOK, TestCounterNG
        global t
        try:
            t.stop()
        except:
            SJPControl.FastConnect()
            pass
    
        self.frame.setEnabled(True)
        self.frame_2.setEnabled(True)
        self.pushButton_test.setEnabled(True)
        self.pushButton_test_2.setEnabled(False)
        TestCounterOK = 0
        TestCounterNG = 0
        self.lcdNumber_2.display(TestCounterNG)
        self.lcdNumber.display(TestCounterOK)
        
        self.tabWidget.setTabEnabled(1, True)
        self.tabWidget.setTabEnabled(2, True)
        self.tabWidget.setTabEnabled(3, True)
        self.tabWidget.setTabEnabled(4, True)

    def CommuncationTest (Name, Delay, self):
        global TestCounterOK, TestCounterNG
        TargetUID = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        TestCounterNG = -1
        while 1:
            GetUID = SJPControl.RDM_Get_UID(TargetUID)
            if GetUID == 0 :
                TestCounterNG += 1
                self.lcdNumber_2.display(TestCounterNG)
            else:
                TestCounterOK += 1
                self.lcdNumber.display(TestCounterOK)
            #print TestCounterOK, TestCounterNG
            time.sleep(0.05)
    
    
            
##########################################################################################################
# Addressing Tab
##########################################################################################################

    @pyqtSignature("")
    def on_pushButton_Discover_clicked(self):
        
        for i in range(self.tableWidget_DiscoverFixtures.rowCount()+1):
            self.tableWidget_DiscoverFixtures.removeRow(0)
        
        #set cursor to wait shape
        self.setCursor(PyQt4.QtGui.QCursor(PyQt4.QtCore.Qt.WaitCursor))
        
        #print "Discovery starts at ", time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        Status = SJPControl.Process_Discovery()
        SJPControl.ConvertSN2ASCII(SJPControl.FixtureDiscovered)
        for item in SJPControl.FixtureSN:
            newItem = PyQt4.QtGui.QTableWidgetItem(item)  
            self.tableWidget_DiscoverFixtures.insertRow(SJPControl.FixtureSN.index(item))
            self.tableWidget_DiscoverFixtures.setItem(SJPControl.FixtureSN.index(item), 0, newItem)
        #print "Discovery ends at ", time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

        for item in SJPControl.FixtureDiscovered:
            newItem = PyQt4.QtGui.QTableWidgetItem(SJPControl.RDM_Get_DMX_Start_Address(item))
            self.tableWidget_DiscoverFixtures.setItem(SJPControl.FixtureDiscovered.index(item), 1, newItem)
            newItem2 = PyQt4.QtGui.QTableWidgetItem(SJPControl.RDM_Get_Device_Model_Description(item))
            self.tableWidget_DiscoverFixtures.setItem(SJPControl.FixtureDiscovered.index(item), 2, newItem2)
            DeviceInfo = list(SJPControl.RDM_Get_Device_Info(item))
            #print DeviceInfo[0:2]
            newItem3 = PyQt4.QtGui.QTableWidgetItem(SJPControl.ConvertRDMVersion2ASCII(DeviceInfo[0:2]))
            newItem4 = PyQt4.QtGui.QTableWidgetItem(SJPControl.ConvertFootprint2ASCII(DeviceInfo[11]))
            self.tableWidget_DiscoverFixtures.setItem(SJPControl.FixtureDiscovered.index(item), 3, newItem3)
            self.tableWidget_DiscoverFixtures.setItem(SJPControl.FixtureDiscovered.index(item), 4, newItem4)
            newItem5 = PyQt4.QtGui.QTableWidgetItem(SJPControl.RDM_Get_Software_Version(item))
            self.tableWidget_DiscoverFixtures.setItem(SJPControl.FixtureDiscovered.index(item), 5, newItem5)
            newItem6 = PyQt4.QtGui.QTableWidgetItem(SJPControl.RDM_Get_Mfg_Label(item))
            self.tableWidget_DiscoverFixtures.setItem(SJPControl.FixtureDiscovered.index(item), 6, newItem6)
            newItem7 = PyQt4.QtGui.QTableWidgetItem(SJPControl.RDM_Get_Device_Label(item))
            self.tableWidget_DiscoverFixtures.setItem(SJPControl.FixtureDiscovered.index(item), 7, newItem7)

        self.tableWidget_DiscoverFixtures.resizeColumnsToContents()
        #set cursor to normal arrow shape
        self.setCursor(PyQt4.QtGui.QCursor(PyQt4.QtCore.Qt.ArrowCursor))
        # Record History
        f.write(time.strftime('%Y/%m/%d_%H:%M:%S',time.localtime(time.time()))+' Discover Test.'+'\n')

    @pyqtSignature("")
    def on_Clear_clicked(self):
        
        for i in range(self.tableWidget_DiscoverFixtures.rowCount()+1):
            self.tableWidget_DiscoverFixtures.removeRow(0)
            
        pixmap = PyQt4.QtGui.QPixmap( '' )
        PP = PyQt4.QtGui.QImage( pixmap )
        self.label_fixture.setPixmap(pixmap)
        SJPControl.RDM_Set_Identify_Device(BroadcastUID,  [0x00])
        
    @pyqtSignature("int, int")
    def on_tableWidget_DiscoverFixtures_cellClicked(self, row, column):
        global BroadcastUID
        global TargetToSetUID
        
        FixtureUID = PyQt4.QtGui.QTableWidgetItem(self.tableWidget_DiscoverFixtures.item(row, 0))
        FixtureDMX = PyQt4.QtGui.QTableWidgetItem(self.tableWidget_DiscoverFixtures.item(row, 1))
        FixtureModel = PyQt4.QtGui.QTableWidgetItem(self.tableWidget_DiscoverFixtures.item(row, 2))
        FixtureFW = PyQt4.QtGui.QTableWidgetItem(self.tableWidget_DiscoverFixtures.item(row, 5))
        FixtureLabel = PyQt4.QtGui.QTableWidgetItem(self.tableWidget_DiscoverFixtures.item(row, 7))
        self.lineEdit_DMXAddr.setText(FixtureDMX.text())
        self.lineEdit_DeviceLabel.setText(FixtureLabel.text())
        
        T = str((int(FixtureDMX.text())+2)/3)
        self.lineEdit_LightNo.setText(T)
        TargetFilePrefix = FixtureModel.text()[0:4]
        TargetDir =  os.curdir+'\\Fixture Files'
        
        UIDPrefix = FixtureUID.text()[0:4]
        UIDSubfix = FixtureUID.text()[5:]
        UIDIdentify = FixtureUID.text()[0:4]+FixtureUID.text()[5:]
        
        SJPControl.RDM_Set_Identify_Device(BroadcastUID,  [0x00])
        IdentifyUID = []
        for i in range(0, 12, 2):
            TempCode = UIDIdentify[i:i+2]
            SingleCode = 0x00

            IDC1 = PyQt4.QtCore.QChar(TempCode[0])
            IDC2 = PyQt4.QtCore.QChar(TempCode[1])
            if IDC1.isDigit():
                SingleCode = IDC1.digitValue()*16
            else:
                SingleCode = (ord(IDC1.toAscii())-55)*16
                
            if IDC2.isDigit():
                SingleCode += IDC2.digitValue()
            else:
                SingleCode += (ord(IDC2.toAscii())-55)

            IdentifyUID.append(SingleCode)
        
        TargetToSetUID = IdentifyUID
        SJPControl.RDM_Set_Identify_Device(IdentifyUID,  [0x01])
        #print TargetFilePrefix.left(4)
        for root, dirs, files in os.walk(TargetDir):
            for name in files:
                #print name,  dirs,  root
                if TargetFilePrefix.left(4)==name[0:4]:
                    #print name
                    PPFileName = root+'\\'+name
                    #print PPFileName
                    PPParse.ParsePP(PPFileName)
                    #print "PPfile", PPParse.FWVersion
                    #print "DISfile", FixtureFW.text()[3:8]
                    if PPParse.FWVersion == FixtureFW.text()[3:8]:
                        pixmap = PyQt4.QtGui.QPixmap( 'data.BMP' )
                        PP = PyQt4.QtGui.QImage( pixmap )
                        self.label_fixture.setPixmap(pixmap)
                        return;
                    else:
                        pixmap = PyQt4.QtGui.QPixmap( '' )
                        PP = PyQt4.QtGui.QImage( pixmap )
                        self.label_fixture.setPixmap(pixmap)
                else:
                    pixmap = PyQt4.QtGui.QPixmap( '' )
                    PP = PyQt4.QtGui.QImage( pixmap )
                    self.label_fixture.setPixmap(pixmap)
        
    @pyqtSignature("")
    def on_pushButton_Export_clicked(self):
        DiscTable = self.tableWidget_DiscoverFixtures
        ExtractFile.ExportResult(DiscTable)
        PyQt4.QtGui.QMessageBox.information(self, "Done", "Export Done!." ,1, 0)
    
    @pyqtSignature("int")
    def on_tabWidget_currentChanged(self, int):
        if(self.tabWidget.currentIndex() == 1):
            TargetUID = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
            try:
                SJPControl.RDM_Set_Identify_Device(TargetUID,  [0x00])
            except:
                pass
        
        if self.pushButton_washstart.isEnabled()==False:
            global t
            global Counter
            self.pushButton_washstart.setEnabled(True)
            self.pushButton_washstop.setEnabled(False)
            self.horizontalSlider_2.setEnabled(True)
            #print SJPControl.ser.outWaiting()
            #while(SJPControl.ser.outWaiting()!=0):
            #    print SJPControl.ser.outWaiting()
            Counter = 1
            time.sleep(0.02)
            try:
                t.stop()
            except:
                SJPControl.FastConnect()
                pass
            
    @pyqtSignature("")
    def on_Button_DMXSet_clicked(self):
        global TargetToSetUID
        H = 0x00
        L = 0x00
        if self.lineEdit_DMXAddr.text().toUInt()[1] == False:
            PyQt4.QtGui.QMessageBox.warning(self, "Invalid Input", "DMX Start Address should be digit type." ,1, 0)
            return
        if int(self.lineEdit_DMXAddr.text())>510 or int(self.lineEdit_DMXAddr.text())<1 :
            PyQt4.QtGui.QMessageBox.warning(self, "Invalid Input", "Setting its address to over 510 will overflow the end of a DMX buffer." ,1, 0)
            return
            
        H = (int(self.lineEdit_DMXAddr.text())>>8) & 0x03
        L = (int(self.lineEdit_DMXAddr.text()))&0xFF
        #print H, L
        SJPControl.RDM_Set_DMX_Start_Address(TargetToSetUID, [H, L])
        self.lineEdit_LightNo.setText(str((int(self.lineEdit_DMXAddr.text())+2)/3))
        
    @pyqtSignature("")
    def on_Button_LightNo_clicked(self):
        global TargetToSetUID
        H = 0x00
        L = 0x00
        if self.lineEdit_LightNo.text().toUInt()[1] == False:
            PyQt4.QtGui.QMessageBox.warning(self, "Invalid Input", "Light Number should be digit type." ,1, 0)
            return
        if int(self.lineEdit_LightNo.text())>170 or int(self.lineEdit_LightNo.text())<1 :
            PyQt4.QtGui.QMessageBox.warning(self, "Invalid Input", "Setting its number to over 170 will overflow the end of a DMX buffer." ,1, 0)
            return
        
        
        H = ((int(self.lineEdit_LightNo.text())*3-2)>>8) & 0x03
        L = ((int(self.lineEdit_LightNo.text())*3-2))&0xFF

        SJPControl.RDM_Set_DMX_Start_Address(TargetToSetUID, [H, L])
        self.lineEdit_DMXAddr.setText(str((int(self.lineEdit_LightNo.text())*3-2)))
            
    @pyqtSignature("")
    def on_Button_LabelSet_clicked(self):
        global TargetToSetUID
        #print self.lineEdit_DeviceLabel.text()
        Payload = self.lineEdit_DeviceLabel.text()
        for i in range (len(self.lineEdit_DeviceLabel.text()), 10, 1):
            Payload.append(' ')

        SJPControl.RDM_Set_Device_Label(TargetToSetUID, Payload)
        
    
##########################################################################################################
# Vaya Play Tab
##########################################################################################################
    def mouseMoveEvent (self, event):
        RED = 0x00
        GREEN = 0x00
        BLUE = 0x00
        GPosition = PyQt4.QtGui.QCursor.pos() # Get the mouse position of global
        LPosition = PyQt4.QtGui.QWidget.mapFromGlobal(self, GPosition) # Transfer to coordinator in side the Frame
        GamutX = LPosition.x()-27
        GamutY = LPosition.y()-108
        
        # if out side the Frame, then ignore
        if GamutX < 0 :
            GamutX = 0
        if GamutX > 765:
            GamutX = 765
        if GamutY < 0 :
            GamutY = 0
        if GamutY > 255:
            GamutY = 255

        self.label_cursur.setGeometry(PyQt4.QtCore.QRect(GamutX-4, GamutY-4, 8, 8))
        
        # Check the coordinator and convert to RGB value
        if GamutX<=127.5:
            RED = 0xFF
            GREEN = GamutX*2
            BLUE = 0x00
        elif GamutX>127.5 and GamutX<=255:
            RED = (255-GamutX)*2
            GREEN = 0xFF
            BLUE = 0x00
        elif GamutX>255 and GamutX<=382.5:
            RED = 0x00
            GREEN = 0xFF
            BLUE = (GamutX-255)*2
        elif GamutX>382.5 and GamutX<=510:
            RED = 0x00
            GREEN = (510-GamutX)*2
            BLUE = 0xFF
        elif GamutX>510 and GamutX<=637.5:
            RED = (GamutX-510)*2
            GREEN = 0x00
            BLUE = 0xFF
        elif GamutX>637.5 and GamutX<=765:
            RED = 0xFF
            GREEN = 0x00
            BLUE = (765-GamutX)*2
  
        if RED < GamutY :
            RED = GamutY
        if GREEN < GamutY:
            GREEN = GamutY
        if BLUE < GamutY:
            BLUE = GamutY
            
        self.lineEdit_R.setText(str(RED))
        self.horizontalSlider_R.setValue(RED)
        self.lineEdit_G.setText(str(GREEN))
        self.horizontalSlider_G.setValue(GREEN)
        self.lineEdit_B.setText(str(BLUE))
        self.horizontalSlider_B.setValue(BLUE)

        #CHUE, CSAT = HSLCalculaion(RED, GREEN, BLUE)
        #self.lineEdit_H.setText(str(int(CHUE)))
        #self.horizontalSlider_H.setValue(int(CHUE))
        #self.lineEdit_S.setText(str(int(CSAT*100)))
        #self.horizontalSlider_S.setValue(int(CSAT*100))
        '''
        payload = []
        restdata = [RED, GREEN, BLUE] * 170 + [RED, GREEN]
        payload.extend(restdata)
        SJPControl.Send_DMX_Packet(payload)
        '''
        t = threading.Thread(target=FixedColorOutput,  args=("FixedColorOutput", RED, GREEN, BLUE))
        #print "START"
        t.start()

    def mousePressEvent(self, event):
        
        # Should be stay in "Fixed Color Page"
        if self.tabWidget.currentIndex() != 2:
            return
        if self.tabWidget.isTabEnabled(2) == False:
            return
        
        RED = 0x00
        GREEN = 0x00
        BLUE = 0x00
        GPosition = PyQt4.QtGui.QCursor.pos() # Get the mouse position of global
        LPosition = PyQt4.QtGui.QWidget.mapFromGlobal(self, GPosition) # Transfer to coordinator in side the Frame
        GamutX = LPosition.x()-27
        GamutY = LPosition.y()-108
        
        # if out side the Frame, then ignore
        if GamutX < 0 :
            GamutX = 0
        if GamutX > 765:
            GamutX = 765
        if GamutY < 0 :
            GamutY = 0
        if GamutY > 255:
            GamutY = 255
            
        self.label_cursur.setGeometry(PyQt4.QtCore.QRect(GamutX-4, GamutY-4, 8, 8))
        
        # Check the coordinator and convert to RGB value
        if GamutX<=127.5:
            RED = 0xFF
            GREEN = GamutX*2
            BLUE = 0x00
        elif GamutX>127.5 and GamutX<=255:
            RED = (255-GamutX)*2
            GREEN = 0xFF
            BLUE = 0x00
        elif GamutX>255 and GamutX<=382.5:
            RED = 0x00
            GREEN = 0xFF
            BLUE = (GamutX-255)*2
        elif GamutX>382.5 and GamutX<=510:
            RED = 0x00
            GREEN = (510-GamutX)*2
            BLUE = 0xFF
        elif GamutX>510 and GamutX<=637.5:
            RED = (GamutX-510)*2
            GREEN = 0x00
            BLUE = 0xFF
        elif GamutX>637.5 and GamutX<=765:
            RED = 0xFF
            GREEN = 0x00
            BLUE = (765-GamutX)*2
  
        if RED < GamutY :
            RED = GamutY
        if GREEN < GamutY:
            GREEN = GamutY
        if BLUE < GamutY:
            BLUE = GamutY
            
        self.lineEdit_R.setText(str(RED))
        self.horizontalSlider_R.setValue(RED)
        self.lineEdit_G.setText(str(GREEN))
        self.horizontalSlider_G.setValue(GREEN)
        self.lineEdit_B.setText(str(BLUE))
        self.horizontalSlider_B.setValue(BLUE)
        
        payload = []
        restdata = [RED, GREEN, BLUE] * 170 + [RED, GREEN]
        payload.extend(restdata)
        SJPControl.Send_DMX_Packet(payload)
        
    @pyqtSignature("")
    def on_pushButton_washstart_clicked(self):
        global t
        self.pushButton_washstart.setEnabled(False)
        self.pushButton_washstop.setEnabled(True)
        self.horizontalSlider_2.setEnabled(False)
        WashDelay = self.horizontalSlider_2.value()
        #print WashDelay
        t = threading.Thread(target=WashEffect,  args=("WASHEFFECT", WashDelay))
        #print "START"
        t.start()
 

    @pyqtSignature("")
    def on_pushButton_washstop_clicked(self):
        global t
        global Counter
        self.pushButton_washstart.setEnabled(True)
        self.pushButton_washstop.setEnabled(False)
        self.horizontalSlider_2.setEnabled(True)
        Counter = 1
        time.sleep(0.02)
        try:
            t.stop()
        except:
            SJPControl.FastConnect()
            pass

        #print "STOP"
        
        
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
    
    @pyqtSignature("int")
    def on_toolBox_currentChanged(self, int):
        #print self.toolBox.currentIndex()
        if self.pushButton_washstart.isEnabled()==False:
            global t
            global Counter
            self.pushButton_washstart.setEnabled(True)
            self.pushButton_washstop.setEnabled(False)
            self.horizontalSlider_2.setEnabled(True)
            Counter = 1
            time.sleep(0.02)
            try:
                t.stop()
            except:
                SJPControl.FastConnect()
                pass

    
def FixedColorOutput (Name, R, G, B):
    payload = []
    restdata = [R, G, B] * 170 + [R, G]
    payload.extend(restdata)
    SJPControl.Send_DMX_Packet(payload)
    
def WashEffect (Name, delay):
    RED = 0xFF
    GREEN = 0x00
    BLUE = 0x00
    STEP = int(160/(delay*5))
    #print "WASH EFFECT"
    global Counter
    Counter = 0
    while Counter == 0:
        for i in range(6):
            if i==0:
                for j in range(0, 256, STEP):
                    payload = []
                    GREEN = j
                    restdata = [RED, GREEN, BLUE] * 170
                    payload.extend(restdata)
                    SJPControl.Send_DMX_Packet(payload)
                    if(Counter == 1):
                        return
                GREEN = 0xFF

            if i==1:
                for j in range(255, -1, -(STEP)):
                    payload = []
                    RED = j
                    restdata = [RED, GREEN, BLUE] * 170
                    payload.extend(restdata)
                    SJPControl.Send_DMX_Packet(payload)
                    if(Counter == 1):
                        return
                RED = 0x00
                
            if i==2:
                for j in range(0, 256, STEP):
                    payload = []
                    BLUE = j
                    restdata = [RED, GREEN, BLUE] * 170
                    payload.extend(restdata)
                    SJPControl.Send_DMX_Packet(payload)
                    if(Counter == 1):
                        return
                BLUE = 0xFF
                
            if i==3:
                for j in range(255, -1, -(STEP)):
                    payload = []
                    GREEN = j
                    restdata = [RED, GREEN, BLUE] * 170
                    payload.extend(restdata)
                    SJPControl.Send_DMX_Packet(payload)
                    if(Counter == 1):
                        return
                GREEN = 0x00

            if i==4:
                for j in range(0, 256, STEP):
                    payload = []
                    RED = j
                    restdata = [RED, GREEN, BLUE] * 170
                    payload.extend(restdata)
                    SJPControl.Send_DMX_Packet(payload)
                    if(Counter == 1):
                        return
                RED = 0xFF

            if i==5:
                for j in range(255, -1, -(STEP)):
                    payload = []
                    BLUE = j
                    restdata = [RED, GREEN, BLUE] * 170
                    payload.extend(restdata)
                    SJPControl.Send_DMX_Packet(payload)
                    if(Counter == 1):
                        return
                BLUE = 0x00

def HSLCalculaion ( R,  G,  B):
    R = float(R)
    G = float(G)
    B = float(B)
    Rprime = R/255
    Gprime = G/255
    Bprime = B/255
    #print Rprime, Gprime, Bprime
    Cmax = max(Rprime, Gprime, Bprime)
    Cmin = min(Rprime, Gprime, Bprime)
    Delta = Cmax-Cmin
    #print Cmax, Cmin, Delta
    '''
    if(Cmax==Rprime):
        Hue = 60*(((Gprime-Bprime)/Delta)%6)
    elif(Cmax==Gprime):
        Hue = 60*(((Bprime-Rprime)/Delta)+2)
    else:
        Hue = 60*(((Rprime-Gprime)/Delta)+4)

    Brightness = (Cmax+Cmin)/2
    
    if(Delta==0):
        Sat = 0
    else:
        Sat = Delta/(1-abs(2*Brightness-1))
    
    #print "Hue: ", Hue
    #print "Sat: ", Sat
    return Hue, Sat
    '''
    
class EnterOperatorID(QDialog, Ui_EnterOperatorID):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        ui2.ConnectDeviceButton.setEnabled(True)
        ui2.label_operator.setText('Operator: '+self.lineEdit.text())
        # Record History
        f.write(time.strftime('%Y/%m/%d_%H:%M:%S',time.localtime(time.time()))+' Operator ID: '+self.lineEdit.text()+'.\n')
        self.setVisible(False)
    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        #print "EXIT Program"
        self.close()
        sys.exit(app2.exec_())
        
    @pyqtSignature("")
    def closeEvent(self,  event):
        sys.exit(app2.exec_())
        
if __name__ == "__main__":

    app2 = PyQt4.QtGui.QApplication(sys.argv)
    ui2 = MainWindow() #should use local class
    ui2.show()

    sys.exit(app2.exec_())
    
    
    
    
    
