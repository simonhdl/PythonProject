# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\310098157\Dropbox\Works@PCK\Engineering\Working Directory\Software Project\Python Project\MTDE UI\MTDE.ui'
#
# Created: Thu May 02 16:31:31 2013
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

class Ui_MTDEmain(object):
    def setupUi(self, MTDEmain):
        MTDEmain.setObjectName(_fromUtf8("MTDEmain"))
        MTDEmain.resize(700, 260)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("KinetProtocolTester_V2.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MTDEmain.setWindowIcon(icon)
        self.label = QtGui.QLabel(MTDEmain)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(10, 220, 241, 21))
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtGui.QFrame.Box)
        self.label.setFrameShadow(QtGui.QFrame.Plain)
        self.label.setScaledContents(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(MTDEmain)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 531, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(MTDEmain)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 170, 591, 20))
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.comboBox = QtGui.QComboBox(MTDEmain)
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QtCore.QRect(19, 100, 200, 22))
        self.comboBox.setMouseTracking(False)
        self.comboBox.setAcceptDrops(True)
        self.comboBox.setEditable(True)
        self.comboBox.setModelColumn(0)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox_2 = QtGui.QComboBox(MTDEmain)
        self.comboBox_2.setGeometry(QtCore.QRect(248, 100, 200, 22))
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_3 = QtGui.QComboBox(MTDEmain)
        self.comboBox_3.setGeometry(QtCore.QRect(480, 100, 200, 22))
        self.comboBox_3.setEditable(True)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.groupBox = QtGui.QGroupBox(MTDEmain)
        self.groupBox.setGeometry(QtCore.QRect(9, 10, 681, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.buttonOpen = QtGui.QPushButton(self.groupBox)
        self.buttonOpen.setGeometry(QtCore.QRect(560, 20, 101, 23))
        self.buttonOpen.setObjectName(_fromUtf8("buttonOpen"))
        self.groupBox_2 = QtGui.QGroupBox(MTDEmain)
        self.groupBox_2.setGeometry(QtCore.QRect(9, 80, 221, 61))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.groupBox_3 = QtGui.QGroupBox(MTDEmain)
        self.groupBox_3.setGeometry(QtCore.QRect(240, 80, 221, 61))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.groupBox_4 = QtGui.QGroupBox(MTDEmain)
        self.groupBox_4.setGeometry(QtCore.QRect(470, 80, 221, 61))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.groupBox_5 = QtGui.QGroupBox(MTDEmain)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 150, 681, 51))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_2 = QtGui.QLabel(self.groupBox_5)
        self.label_2.setGeometry(QtCore.QRect(610, 23, 46, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.buttonOK = QtGui.QPushButton(MTDEmain)
        self.buttonOK.setGeometry(QtCore.QRect(510, 220, 75, 23))
        self.buttonOK.setObjectName(_fromUtf8("buttonOK"))
        self.buttonCancel = QtGui.QPushButton(MTDEmain)
        self.buttonCancel.setGeometry(QtCore.QRect(600, 220, 75, 23))
        self.buttonCancel.setObjectName(_fromUtf8("buttonCancel"))

        self.retranslateUi(MTDEmain)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QObject.connect(self.buttonOK, QtCore.SIGNAL(_fromUtf8("clicked()")), MTDEmain.close)
        QtCore.QObject.connect(self.buttonCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), MTDEmain.close)
        QtCore.QMetaObject.connectSlotsByName(MTDEmain)
        MTDEmain.setTabOrder(self.lineEdit, self.buttonOpen)
        MTDEmain.setTabOrder(self.buttonOpen, self.comboBox)
        MTDEmain.setTabOrder(self.comboBox, self.comboBox_2)
        MTDEmain.setTabOrder(self.comboBox_2, self.comboBox_3)
        MTDEmain.setTabOrder(self.comboBox_3, self.lineEdit_2)
        MTDEmain.setTabOrder(self.lineEdit_2, self.buttonOK)
        MTDEmain.setTabOrder(self.buttonOK, self.buttonCancel)

    def retranslateUi(self, MTDEmain):
        MTDEmain.setWindowTitle(_translate("MTDEmain", "Manufactoring Test Data Extractor", None))
        self.label.setText(_translate("MTDEmain", "CK Manufactoring Test Data Extractor Tool V1.0", None))
        self.groupBox.setTitle(_translate("MTDEmain", "1. Select CSV File Location", None))
        self.buttonOpen.setText(_translate("MTDEmain", "Open", None))
        self.groupBox_2.setTitle(_translate("MTDEmain", "2. Select Product", None))
        self.groupBox_3.setTitle(_translate("MTDEmain", "3. Select Station", None))
        self.groupBox_4.setTitle(_translate("MTDEmain", "4. Select Type", None))
        self.groupBox_5.setTitle(_translate("MTDEmain", "5. Enter Outupt File Name", None))
        self.label_2.setText(_translate("MTDEmain", ".XLS", None))
        self.buttonOK.setText(_translate("MTDEmain", "OK", None))
        self.buttonCancel.setText(_translate("MTDEmain", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MTDEmain = QtGui.QDialog()
    ui = Ui_MTDEmain()
    ui.setupUi(MTDEmain)
    MTDEmain.show()
    sys.exit(app.exec_())

