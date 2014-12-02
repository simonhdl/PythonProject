# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import PyQt4, PyQt4.QtGui, PyQt4.QtCore, sys

from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature

from Ui_VayaMfgMainWin import Ui_MainWindow

import SJPControl
import PPParse
import ExtractFile
import Ui_Info
import webbrowser


from datetime import date
import datetime
import time
import threading

import os
#CMList = [['000', 'Opulent'], ['001', 'SSZ'], ['010', 'Primo'], ['011', 'AVC'], ['100', 'VTECH'], ['101', 'SengLED'], ['110', 'QiRui'], ['111', 'BOI']]
CMList = ['Opulent', 'SSZ', 'Primo', 'AVC', 'VTECH', 'SengLED', 'QiRui', 'BOI']

global VayaSN
global VayaSNNum
global TestCounterOK, TestCounterNG
global t
global BroadcastUID
BroadcastUID = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
TestCounterOK = 0
TestCounterNG = 0

LogFileName = 'LogFile_'+time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))+'.txt'
f = open("Report\\"+LogFileName, 'w')

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
        
        #Update CM List into ComboBox
        for item in CMList:
            self.comboBox_CMList.addItem(item)
        
        #Update the Date
        i = datetime.date.today()
        ProductDate = date.isoformat(i)
        self.lineEdit_Today.setText(ProductDate)
        self.lineEdit_UID.setReadOnly(True)
        #self.tableWidget_DiscoverFixtures.resizeColumnsToContents()
        self.tabWidget.setEnabled(False)
        self.pushButton_test_2.setEnabled(False)
        self.setWindowIcon(PyQt4.QtGui.QIcon("Data/Vaya.png"))
        '''
        for r in range(32):
            for c in range(16):
                t = r*16 + c + 1
                item = PyQt4.QtGui.QTableWidgetItem(str(t))
                self.tableWidget_channeltest.setItem(r, c, item)
        '''
        
        #Show the SJP device picture but not connect
        pixmap = PyQt4.QtGui.QPixmap( 'Data//sjp_off.jpg' )
        PP = PyQt4.QtGui.QImage( pixmap )
        self.label_SJP.setPixmap(pixmap)
        '''
        pixmap = PyQt4.QtGui.QPixmap( 'Data//vaya cfg tool.bmp' )
        PP = PyQt4.QtGui.QImage( pixmap )
        self.label_logo.setPixmap(pixmap)
        '''
    def closeEvent(self, event):
        #SJPControl.Close_SJP()
        #file close before quit
        f.close()
        
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
        Slot documentation goes here.
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
        else:
            self.label_Device_Status_2.setText('No Smart Jack Pro Connected')
            self.DisconnectDeviceButton.setEnabled(False)
            self.ConnectDeviceButton.setEnabled(True)
            self.tabWidget.setEnabled(False)
            self.label_Device_Status_2.setStyleSheet("QLabel { background-color: rgb(255, 255, 255) }")
            pixmap = PyQt4.QtGui.QPixmap( 'Data//sjp_off.jpg' )
            PP = PyQt4.QtGui.QImage( pixmap )
            self.label_SJP.setPixmap(pixmap)
        
    @pyqtSignature("")
    def on_DisconnectDeviceButton_clicked(self):
        """
        Slot documentation goes here.
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
        self.lineEdit_ProgramUID.setText(VayaSN)

    @pyqtSignature("int")
    def on_spinBox_valueChanged(self, p0):
        VayaSN = hex(VayaSNNum+self.spinBox.value()-1)
        VayaSN = VayaSN.upper()
        VayaSN = VayaSN[2:10]
        self.lineEdit_ProgramUID.setText(VayaSN)

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
        self.lineEdit_ProgramUID.setText(VayaSN)
        
        
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
        PPFileName = PyQt4.QtGui.QFileDialog.getOpenFileName(self, self.tr("Please Select The PP File."), "", self.tr("PP files (*.PP)"))
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
        self.label_35.setPixmap(pixmap)
        
        

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
        for item in UUID:
            if PyQt4.QtCore.QChar(item).isDigit():
                continue
            elif item!='A' and item!='B' and  item!='C' and  item!='D' and  item!='E' and  item!='F' and  item!='a' and   item!='b' and  item!='c' and  item!='d' and  item!='e' and  item!='f' :
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
            f.write(time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))+' Set Fixture Parameter OK'+' '+UUID+' '+NewModel+'\n')
        else :
            PyQt4.QtGui.QMessageBox.information(self, "Fail", "Set Parameters Fail!" ,1, 0)
            f.write(time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))+' Set Fixture Parameter FAIL'+' '+UUID+' '+NewModel+'\n')
        
        
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
        print GetModel,  GetUID
        self.comboBox_ModelList.clear()
        self.comboBox_ModelList.addItem(GetModel)
        
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
            self.comboBox_CMList.setCurrentIndex(CMID)
            self.spinBox.setValue(IDSeq)
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

    def CommuncationTest (Name, Delay, self):
        global TestCounterOK, TestCounterNG
        TargetUID = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        while 1:
            GetUID = SJPControl.RDM_Get_UID(TargetUID)
            if GetUID == 0 :
                TestCounterNG += 1
                self.lcdNumber_2.display(TestCounterNG)
            else:
                TestCounterOK += 1
                self.lcdNumber.display(TestCounterOK)
            print TestCounterOK, TestCounterNG
            time.sleep(0.05)
    
    
    
if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)
    ui = MainWindow() #should use local class
    ui.show()
    #f.close()
    sys.exit(app.exec_())
