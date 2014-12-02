# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\310098157\Dropbox\Works@PCK\Engineering\Working Directory\Software Project\Python Project\VayaManufacturingToolV1\IdInput.ui'
#
# Created: Thu Jun 26 11:46:20 2014
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

class Ui_EnterOperatorID(object):
    def setupUi(self, EnterOperatorID):
        EnterOperatorID.setObjectName(_fromUtf8("EnterOperatorID"))
        EnterOperatorID.resize(221, 125)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EnterOperatorID.sizePolicy().hasHeightForWidth())
        EnterOperatorID.setSizePolicy(sizePolicy)
        EnterOperatorID.setMinimumSize(QtCore.QSize(221, 125))
        EnterOperatorID.setMaximumSize(QtCore.QSize(221, 125))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("CK.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EnterOperatorID.setWindowIcon(icon)
        EnterOperatorID.setAutoFillBackground(False)
        EnterOperatorID.setSizeGripEnabled(False)
        EnterOperatorID.setModal(False)
        self.label = QtGui.QLabel(EnterOperatorID)
        self.label.setGeometry(QtCore.QRect(10, 10, 241, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(EnterOperatorID)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(EnterOperatorID)
        self.pushButton.setGeometry(QtCore.QRect(10, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(EnterOperatorID)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(EnterOperatorID)
        QtCore.QMetaObject.connectSlotsByName(EnterOperatorID)

    def retranslateUi(self, EnterOperatorID):
        EnterOperatorID.setWindowTitle(_translate("EnterOperatorID", "Enter Operator ID", None))
        self.label.setText(_translate("EnterOperatorID", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Please Enter Operator ID :</span><br/></p></body></html>", None))
        self.pushButton.setText(_translate("EnterOperatorID", "OK", None))
        self.pushButton_2.setText(_translate("EnterOperatorID", "Quit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    EnterOperatorID = QtGui.QDialog()
    ui = Ui_EnterOperatorID()
    ui.setupUi(EnterOperatorID)
    EnterOperatorID.show()
    sys.exit(app.exec_())

