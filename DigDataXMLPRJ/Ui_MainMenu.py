# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\310098157\Dropbox\Works@PCK\Engineering\Working Directory\Software Project\Python Project\DigDataXMLPRJ\MainMenu.ui'
#
# Created: Wed Dec 18 11:22:08 2013
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
        Dialog.resize(788, 354)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("CK.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 251, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.ProductBox = QtGui.QComboBox(self.groupBox)
        self.ProductBox.setGeometry(QtCore.QRect(10, 40, 231, 22))
        self.ProductBox.setObjectName(_fromUtf8("ProductBox"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(270, 50, 251, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.StationBox = QtGui.QComboBox(self.groupBox_2)
        self.StationBox.setGeometry(QtCore.QRect(10, 40, 231, 22))
        self.StationBox.setObjectName(_fromUtf8("StationBox"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(530, 50, 251, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.ModelBox = QtGui.QComboBox(self.groupBox_3)
        self.ModelBox.setGeometry(QtCore.QRect(10, 40, 231, 22))
        self.ModelBox.setObjectName(_fromUtf8("ModelBox"))
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 150, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.pushButton = QtGui.QPushButton(self.groupBox_4)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit.setGeometry(QtCore.QRect(110, 30, 281, 25))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.groupBox_5 = QtGui.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 230, 431, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 30, 381, 25))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(self.groupBox_5)
        self.label.setGeometry(QtCore.QRect(400, 31, 31, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 310, 91, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 310, 91, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(453, 150, 321, 131))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 471, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setMargin(4)
        self.label_2.setIndent(1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(470, 300, 311, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(540, 330, 241, 20))
        self.label_3.setFrameShape(QtGui.QFrame.Box)
        self.label_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_3.setLineWidth(1)
        self.label_3.setMidLineWidth(1)
        self.label_3.setMargin(3)
        self.label_3.setIndent(1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(570, 10, 211, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.ProductBox, QtCore.SIGNAL(_fromUtf8("activated(QString)")), Dialog.raise_)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.open)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "DigData", None))
        self.groupBox.setTitle(_translate("Dialog", "1. Select Product", None))
        self.groupBox_2.setTitle(_translate("Dialog", "2. Select Test Station", None))
        self.groupBox_3.setTitle(_translate("Dialog", "3. Select Model", None))
        self.groupBox_4.setTitle(_translate("Dialog", "4. Select Data Folder", None))
        self.pushButton.setText(_translate("Dialog", "Select", None))
        self.groupBox_5.setTitle(_translate("Dialog", "5. Output File Name", None))
        self.label.setText(_translate("Dialog", ".XLS", None))
        self.pushButton_2.setText(_translate("Dialog", "OK", None))
        self.pushButton_3.setText(_translate("Dialog", "Exit", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; color:#ff5500;\">DigData </span><span style=\" font-size:16pt; color:#00557f;\">Data Extractor for PCK Test Report  </span><span style=\" color:#00557f; vertical-align:sub;\">v2.0</span></p></body></html>", None))
        self.label_3.setText(_translate("Dialog", " Email: simon.dl.he@philips.com   /  2013-12-12", None))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Philips Solid State Lighting Solutions</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

