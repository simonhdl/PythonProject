# -*- coding: utf-8 -*-

"""
Module implementing MTDEmain.
"""
import PyQt4, PyQt4.QtGui, sys

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_MTDE import Ui_MTDEmain

#import CfgParse

# Import Library
import csv
import sys
import os
import glob
import time

ProductList = []
ProductLineNum = []
StationList = []
StationLineNum= []
ModelList = []
ModelLineNum = []


def readProductList ():
    CfgFile = open('Config.v','r')
    for (num, value) in enumerate(CfgFile):
        if 'PRODUCT' in value:
            ProductList.append(value[8:-1])
            ProductLineNum.append(num)
    CfgFile.close()
    
    
class MTDEmain(QDialog, Ui_MTDEmain):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        readProductList()
        for item in ProductList:
            self.comboBox.addItem(item)
            print(item)
        
    @pyqtSignature("")
    def on_buttonOpen_clicked(self):
        FolderDir = PyQt4.QtGui.QFileDialog.getExistingDirectory(self, self.tr("Please Select the CSV file Folder."))
        self.lineEdit.setText(FolderDir)

if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)
    ui = MTDEmain()
    ui.show()
    sys.exit(app.exec_())
