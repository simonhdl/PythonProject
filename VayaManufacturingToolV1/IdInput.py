# -*- coding: utf-8 -*-

"""
Module implementing EnterOperatorID.
"""
import PyQt4.QtGui, PyQt4.QtCore, sys
import VayaMfgTool
import Ui_VayaMfgMainWin


from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_IdInput import Ui_EnterOperatorID

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
        app = PyQt4.QtGui.QApplication(sys.argv)
        ui = Ui_VayaMfgMainWin.Ui_MainWindow() #should use local class
        ui.show()
        sys.exit(app.exec_())

    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        sys.exit(app.exec_())


if __name__ == "__main__":
    app = PyQt4.QtGui.QApplication(sys.argv)
    ui = EnterOperatorID()
    ui.show()
    sys.exit(app.exec_())
