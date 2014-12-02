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
global TargetToSetUID
global Counter

BroadcastUID = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
TargetToSetUID =[]
TestCounterOK = 0
TestCounterNG = 0

# Vaya Play dont need this
'''
LogFileName = 'LogFile_'+time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))+'.txt'
f = open("Report\\"+LogFileName, 'w')
'''

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
        #for item in CMList:
        #    self.comboBox_CMList.addItem(item)
        self.setWindowIcon(PyQt4.QtGui.QIcon("Data/Vaya.png"))
        #Update the Date
        i = datetime.date.today()
        ProductDate = date.isoformat(i)
        #self.lineEdit_Today.setText(ProductDate)
        #self.lineEdit_UID.setReadOnly(True)
        self.tableWidget_DiscoverFixtures.resizeColumnsToContents()
        #self.tabWidget.setEnabled(False)
        #self.tabWidget.setTabEnabled(0, False)
        #self.tabWidget.setTabEnabled(1, False)
        self.pushButton_washstart.setEnabled(True)
        self.pushButton_washstop.setEnabled(False)
        self.horizontalSlider_2.setEnabled(True)
        #calculate and set the channel number at channel test page
        for r in range(32):
            for c in range(16):
                t = r*16 + c + 1
                item = PyQt4.QtGui.QTableWidgetItem(str(t))
                self.tableWidget_channeltest.setItem(r, c, item)
        
        
        #Show the SJP device picture but not connect
        self.label_Device_Status_2.setText('No Smart Jack Pro Connected')
        self.DisconnectDeviceButton.setEnabled(False)
        self.ConnectDeviceButton.setEnabled(True)

        self.tabWidget.setTabEnabled(0, False)
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabEnabled(2, False)
        self.tabWidget.setTabEnabled(3, False)
        self.label_Device_Status_2.setStyleSheet("QLabel { background-color: rgb(255, 255, 255) }")
 
        pixmap = PyQt4.QtGui.QPixmap( 'Data//sjp_off.jpg' )
        PP = PyQt4.QtGui.QImage( pixmap )
        self.label_SJP.setPixmap(pixmap)

    def closeEvent(self, event):
        #SJPControl.Close_SJP()
        #file close before quit
        #f.close()
        pass
        
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
        if(SJPControl.Open_SJP()==1):
            self.label_Device_Status_2.setText('Connected SN:'+SJPControl.SJP_SN)
            self.DisconnectDeviceButton.setEnabled(True)
            self.ConnectDeviceButton.setEnabled(False)
            #self.tabWidget.setEnabled(True)
            self.tabWidget.setTabEnabled(0, True)
            self.tabWidget.setTabEnabled(1, True)
            self.tabWidget.setTabEnabled(2, True)
            self.tabWidget.setTabEnabled(3, True)
            self.label_Device_Status_2.setStyleSheet("QLabel { background-color: rgb(0, 255, 0) }")
            pixmap = PyQt4.QtGui.QPixmap( 'Data//sjp_on.jpg' )
            PP = PyQt4.QtGui.QImage( pixmap )
            self.label_SJP.setPixmap(pixmap)
        else:
            self.label_Device_Status_2.setText('No Smart Jack Pro Connected')
            self.DisconnectDeviceButton.setEnabled(False)
            self.ConnectDeviceButton.setEnabled(True)
            #self.tabWidget.setEnabled(False)
            self.tabWidget.setTabEnabled(0, False)
            self.tabWidget.setTabEnabled(1, False)
            self.tabWidget.setTabEnabled(2, False)
            self.tabWidget.setTabEnabled(3, False)
            self.label_Device_Status_2.setStyleSheet("QLabel { background-color: rgb(255, 255, 255) }")
            pixmap = PyQt4.QtGui.QPixmap( 'Data//sjp_off.jpg' )
            PP = PyQt4.QtGui.QImage( pixmap )
            self.label_SJP.setPixmap(pixmap)
        
    @pyqtSignature("")
    def on_DisconnectDeviceButton_clicked(self):
        SJPControl.Close_SJP()
        self.label_Device_Status_2.setText('No Smart Jack Pro Connected')
        self.DisconnectDeviceButton.setEnabled(False)
        self.ConnectDeviceButton.setEnabled(True)
        #self.tabWidget.setEnabled(False)
        self.tabWidget.setTabEnabled(0, False)
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabEnabled(2, False)
        self.tabWidget.setTabEnabled(3, False)
        self.label_Device_Status_2.setStyleSheet("QLabel { background-color: rgb(255, 255, 255) }")
        pixmap = PyQt4.QtGui.QPixmap( 'Data//sjp_off.jpg' )
        PP = PyQt4.QtGui.QImage( pixmap )
        self.label_SJP.setPixmap(pixmap)


##########################################################################################################
# Addressing Tab
##########################################################################################################

    @pyqtSignature("")
    def on_pushButton_Discover_clicked(self):
        #set cursor to wait shape
        self.setCursor(PyQt4.QtGui.QCursor(PyQt4.QtCore.Qt.WaitCursor))
        
        for i in range(self.tableWidget_DiscoverFixtures.rowCount()+1):
            self.tableWidget_DiscoverFixtures.removeRow(0)
        
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
        print TargetFilePrefix.left(4)
        for root, dirs, files in os.walk(TargetDir):
            for name in files:
                if TargetFilePrefix.left(4)==name[0:4]:
                    #print name
                    PPFileName = TargetDir+'\\'+name
                    PPParse.ParsePP(PPFileName)
                    print "PPfile", PPParse.FWVersion
                    print "DISfile", FixtureFW.text()[3:8]
                    if PPParse.FWVersion == FixtureFW.text()[3:8]:
                        pixmap = PyQt4.QtGui.QPixmap( 'data.BMP' )
                        PP = PyQt4.QtGui.QImage( pixmap )
                        self.label_fixture.setPixmap(pixmap)
                        break;
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

    def mousePressEvent(self, event):
        # Should be stay in "Fixed Color Page"
        if self.tabWidget.currentIndex() != 1:
            return
        if self.tabWidget.isTabEnabled(1) == False:
            return
            
        RED = 0x00
        GREEN = 0x00
        BLUE = 0x00
        GPosition = PyQt4.QtGui.QCursor.pos() # Get the mouse position of global
        LPosition = PyQt4.QtGui.QWidget.mapFromGlobal(self, GPosition) # Transfer to coordinator in side the Frame
        GamutX = LPosition.x()-31
        GamutY = LPosition.y()-114

        #print GamutX, GamutY
        # if out side the Frame, then ignore
        if GamutX < 0 or GamutX >765:
            return
        if GamutY <0 or GamutY > 255:
            return
        
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
        
        payload = []
        restdata = [RED, GREEN, BLUE] * 170 + [RED, GREEN]
        payload.extend(restdata)
        SJPControl.Send_DMX_Packet(payload)
        self.label_cursur.setGeometry(PyQt4.QtCore.QRect(GamutX, GamutY, 8, 8))
       
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
                    print ROW, COL
                    ChannelValue[ROW*16+COL] = self.horizontalSlider_value.value()
        SJPControl.Send_DMX_Packet(ChannelValue)
        
        
    @pyqtSignature("")
    def on_pushButton_testchannelAllOff_clicked(self):
        print "All Off"
        for ROW in range(32):
            for COL in range(16):
                ChannelItem = self.tableWidget_channeltest.item(ROW, COL)
                ChannelItem.setSelected(False)
        payload = [0x00]*512
        SJPControl.Send_DMX_Packet(payload)
        
    @pyqtSignature("")
    def on_pushButton_testchannelAllOn_clicked(self):
        print "All On"
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
                    print ROW, COL
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
    
def WashEffect (Name, delay):
    RED = 0xFF
    GREEN = 0x00
    BLUE = 0x00
    STEP = int(100/(delay*5))
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
if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)
    ui = MainWindow() #should use local class
    ui.show()
    sys.exit(app.exec_())
