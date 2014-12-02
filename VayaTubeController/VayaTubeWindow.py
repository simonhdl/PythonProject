# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import PyQt4, PyQt4.QtGui, PyQt4.QtCore, sys
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_VayaTubeWindow import Ui_Dialog

import SJPControl
Resolution = ['1', '2', '4', '8']

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
        self.pushButton_Prog.setEnabled(False)
        for item in Resolution:
            self.comboBox.addItem(item)
    
    @pyqtSignature("")
    def on_connect_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if(SJPControl.Open_SJP()==1):
            self.label_status.setStyleSheet("QLabel { background-color: rgb(0, 255, 0) }")
            self.pushButton_Prog.setEnabled(True)
        else:
            self.label_status.setStyleSheet("QLabel { background-color: rgb(255, 255, 255) }")
            self.pushButton_Prog.setEnabled(False)
    
    @pyqtSignature("")
    def on_disconnect_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        SJPControl.Close_SJP()
        self.label_status.setStyleSheet("QLabel { background-color: rgb(255, 255, 255) }")
        self.pushButton_Prog.setEnabled(False)
    
    @pyqtSignature("")
    def on_pushButton_Prog_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        DMXPacket = [0xAF] # MAGIC_SC
        NodeStr1 = self.spinBox_nodeStr1.value()*3
        NodeStr2 = self.spinBox_nodeStr2.value()*3
        Offset = self.spinBox_basenum.value()-1
        Resolution = self.comboBox.currentIndex()
        if(self.checkBox.checkState()!=0):
            Resolution=0xFF
        StartupR = self.spinBox_startupR.value()
        StartupG = self.spinBox_startupG.value()
        StartupB = self.spinBox_startupB.value()
        payload = [0x43, 0x4B, NodeStr1, NodeStr2, Offset, Resolution, StartupR, StartupG, StartupB, 0xAF]
        DMXPacket.extend(payload) 
        SJPControl.SJPSendPacket(0x06, DMXPacket)
        SJPControl.Send_Get_SerialNumber()



if __name__ == "__main__":
    import sys
    app = PyQt4.QtGui.QApplication(sys.argv)
    #Dialog = PyQt4.QtGui.QDialog()
    ui = Dialog()
    #ui.setupUi(Dialog)
    #Dialog.show()
    ui.show()
    sys.exit(app.exec_())
