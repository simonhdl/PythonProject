# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\310098157\Dropbox\Works@PCK\Engineering\Working Directory\Software Project\Python Project\ChromatisityDataAnalyze\CDAMainWin.ui'
#
# Created: Thu Aug 28 11:13:17 2014
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1072, 581)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.CIE1976_Label = QtGui.QLabel(self.centralWidget)
        self.CIE1976_Label.setGeometry(QtCore.QRect(10, 60, 512, 512))
        self.CIE1976_Label.setFrameShape(QtGui.QFrame.Box)
        self.CIE1976_Label.setText(_fromUtf8(""))
        self.CIE1976_Label.setObjectName(_fromUtf8("CIE1976_Label"))
        self.Intensity_Label = QtGui.QLabel(self.centralWidget)
        self.Intensity_Label.setGeometry(QtCore.QRect(550, 60, 512, 512))
        self.Intensity_Label.setFrameShape(QtGui.QFrame.Box)
        self.Intensity_Label.setText(_fromUtf8(""))
        self.Intensity_Label.setObjectName(_fromUtf8("Intensity_Label"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(550, 40, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line = QtGui.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(10, 30, 1051, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Chromatisity Data Analyze Tool", None))
        self.label.setText(_translate("MainWindow", "CIE1976", None))
        self.label_2.setText(_translate("MainWindow", "Intensity", None))
        self.pushButton.setText(_translate("MainWindow", "Load File", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

