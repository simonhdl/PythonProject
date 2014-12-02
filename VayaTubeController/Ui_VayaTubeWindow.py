# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\310098157\Dropbox\Works@PCK\Engineering\Working Directory\Software Project\Python Project\VayaTubeController\VayaTubeWindow.ui'
#
# Created: Thu May 15 16:04:27 2014
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 299)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.connect = QtGui.QPushButton(Dialog)
        self.connect.setGeometry(QtCore.QRect(20, 12, 75, 31))
        self.connect.setObjectName(_fromUtf8("connect"))
        self.disconnect = QtGui.QPushButton(Dialog)
        self.disconnect.setGeometry(QtCore.QRect(100, 12, 75, 31))
        self.disconnect.setObjectName(_fromUtf8("disconnect"))
        self.label_status = QtGui.QLabel(Dialog)
        self.label_status.setGeometry(QtCore.QRect(190, 10, 31, 31))
        self.label_status.setFrameShape(QtGui.QFrame.Box)
        self.label_status.setText(_fromUtf8(""))
        self.label_status.setObjectName(_fromUtf8("label_status"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 141, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 141, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.spinBox_nodeStr1 = QtGui.QSpinBox(Dialog)
        self.spinBox_nodeStr1.setGeometry(QtCore.QRect(160, 60, 51, 31))
        self.spinBox_nodeStr1.setMinimum(1)
        self.spinBox_nodeStr1.setMaximum(80)
        self.spinBox_nodeStr1.setProperty("value", 80)
        self.spinBox_nodeStr1.setObjectName(_fromUtf8("spinBox_nodeStr1"))
        self.spinBox_nodeStr2 = QtGui.QSpinBox(Dialog)
        self.spinBox_nodeStr2.setGeometry(QtCore.QRect(160, 100, 51, 31))
        self.spinBox_nodeStr2.setMinimum(1)
        self.spinBox_nodeStr2.setMaximum(80)
        self.spinBox_nodeStr2.setProperty("value", 80)
        self.spinBox_nodeStr2.setObjectName(_fromUtf8("spinBox_nodeStr2"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 71, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(100, 140, 51, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.spinBox_startupR = QtGui.QSpinBox(Dialog)
        self.spinBox_startupR.setGeometry(QtCore.QRect(100, 170, 51, 31))
        self.spinBox_startupR.setMinimum(0)
        self.spinBox_startupR.setMaximum(255)
        self.spinBox_startupR.setProperty("value", 0)
        self.spinBox_startupR.setObjectName(_fromUtf8("spinBox_startupR"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(160, 140, 51, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.spinBox_startupG = QtGui.QSpinBox(Dialog)
        self.spinBox_startupG.setGeometry(QtCore.QRect(160, 170, 51, 31))
        self.spinBox_startupG.setMinimum(0)
        self.spinBox_startupG.setMaximum(255)
        self.spinBox_startupG.setProperty("value", 0)
        self.spinBox_startupG.setObjectName(_fromUtf8("spinBox_startupG"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(220, 140, 51, 31))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.spinBox_startupB = QtGui.QSpinBox(Dialog)
        self.spinBox_startupB.setGeometry(QtCore.QRect(220, 170, 51, 31))
        self.spinBox_startupB.setMinimum(0)
        self.spinBox_startupB.setMaximum(255)
        self.spinBox_startupB.setProperty("value", 0)
        self.spinBox_startupB.setObjectName(_fromUtf8("spinBox_startupB"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(20, 220, 91, 31))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.spinBox_basenum = QtGui.QSpinBox(Dialog)
        self.spinBox_basenum.setGeometry(QtCore.QRect(120, 220, 51, 31))
        self.spinBox_basenum.setMinimum(1)
        self.spinBox_basenum.setMaximum(170)
        self.spinBox_basenum.setProperty("value", 1)
        self.spinBox_basenum.setObjectName(_fromUtf8("spinBox_basenum"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 260, 91, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.pushButton_Prog = QtGui.QPushButton(Dialog)
        self.pushButton_Prog.setGeometry(QtCore.QRect(270, 220, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Prog.setFont(font)
        self.pushButton_Prog.setObjectName(_fromUtf8("pushButton_Prog"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 40, 381, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(10, 130, 381, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(10, 200, 381, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(190, 270, 111, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(90, 261, 69, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Vaya Tube Controller Configuration", None))
        self.connect.setText(_translate("Dialog", "Connect", None))
        self.disconnect.setText(_translate("Dialog", "Disconnect", None))
        self.label_2.setText(_translate("Dialog", "Node Number for String 1 :", None))
        self.label_3.setText(_translate("Dialog", "Node Number for String 2 :", None))
        self.label_4.setText(_translate("Dialog", "Start Up Color", None))
        self.label_5.setText(_translate("Dialog", "RED", None))
        self.label_6.setText(_translate("Dialog", "GREEN", None))
        self.label_7.setText(_translate("Dialog", "BLUE", None))
        self.label_8.setText(_translate("Dialog", "Base Light Number", None))
        self.label_9.setText(_translate("Dialog", "Resolution", None))
        self.pushButton_Prog.setText(_translate("Dialog", "Programm", None))
        self.checkBox.setText(_translate("Dialog", "All Same Address", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

