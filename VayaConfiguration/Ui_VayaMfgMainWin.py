# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\310098157\Dropbox\Works@PCK\Engineering\Working Directory\Software Project\Python Project\VayaConfiguration\VayaMfgMainWin.ui'
#
# Created: Wed Mar 26 11:37:05 2014
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
        MainWindow.resize(825, 715)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../../../Pictures/CK.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.ConnectDeviceButton = QtGui.QPushButton(self.centralWidget)
        self.ConnectDeviceButton.setGeometry(QtCore.QRect(10, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ConnectDeviceButton.setFont(font)
        self.ConnectDeviceButton.setObjectName(_fromUtf8("ConnectDeviceButton"))
        self.label_Device_Status = QtGui.QLabel(self.centralWidget)
        self.label_Device_Status.setGeometry(QtCore.QRect(570, 11, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_Device_Status.setFont(font)
        self.label_Device_Status.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_Device_Status.setObjectName(_fromUtf8("label_Device_Status"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 60, 801, 601))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.configuration = QtGui.QWidget()
        self.configuration.setObjectName(_fromUtf8("configuration"))
        self.frame = QtGui.QFrame(self.configuration)
        self.frame.setGeometry(QtCore.QRect(10, 30, 771, 101))
        self.frame.setStyleSheet(_fromUtf8(""))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(1)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(330, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(210, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.frame)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(480, 10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_UID = QtGui.QLineEdit(self.frame)
        self.lineEdit_UID.setGeometry(QtCore.QRect(280, 60, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_UID.setFont(font)
        self.lineEdit_UID.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_UID.setObjectName(_fromUtf8("lineEdit_UID"))
        self.GenerateUID = QtGui.QPushButton(self.frame)
        self.GenerateUID.setGeometry(QtCore.QRect(420, 60, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GenerateUID.setFont(font)
        self.GenerateUID.setObjectName(_fromUtf8("GenerateUID"))
        self.comboBox_CMList = QtGui.QComboBox(self.frame)
        self.comboBox_CMList.setGeometry(QtCore.QRect(80, 60, 91, 31))
        self.comboBox_CMList.setObjectName(_fromUtf8("comboBox_CMList"))
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(250, 60, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.textBrowser = QtGui.QTextBrowser(self.frame)
        self.textBrowser.setEnabled(False)
        self.textBrowser.setGeometry(QtCore.QRect(540, 5, 221, 91))
        self.textBrowser.setFrameShape(QtGui.QFrame.Box)
        self.textBrowser.setFrameShadow(QtGui.QFrame.Plain)
        self.textBrowser.setLineWidth(1)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_2 = QtGui.QLabel(self.configuration)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 771, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("background-color: rgb(130, 200, 255);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.frame_2 = QtGui.QFrame(self.configuration)
        self.frame_2.setGeometry(QtCore.QRect(10, 160, 771, 221))
        self.frame_2.setStyleSheet(_fromUtf8(""))
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setMidLineWidth(1)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_13 = QtGui.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_Today = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_Today.setEnabled(True)
        self.lineEdit_Today.setGeometry(QtCore.QRect(105, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_Today.setFont(font)
        self.lineEdit_Today.setText(_fromUtf8(""))
        self.lineEdit_Today.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Today.setReadOnly(True)
        self.lineEdit_Today.setObjectName(_fromUtf8("lineEdit_Today"))
        self.pushButton_SelectPP = QtGui.QPushButton(self.frame_2)
        self.pushButton_SelectPP.setGeometry(QtCore.QRect(330, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_SelectPP.setFont(font)
        self.pushButton_SelectPP.setObjectName(_fromUtf8("pushButton_SelectPP"))
        self.pushButton_SetPara = QtGui.QPushButton(self.frame_2)
        self.pushButton_SetPara.setGeometry(QtCore.QRect(20, 170, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_SetPara.setFont(font)
        self.pushButton_SetPara.setObjectName(_fromUtf8("pushButton_SetPara"))
        self.pushButton_GetPara = QtGui.QPushButton(self.frame_2)
        self.pushButton_GetPara.setGeometry(QtCore.QRect(240, 170, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_GetPara.setFont(font)
        self.pushButton_GetPara.setObjectName(_fromUtf8("pushButton_GetPara"))
        self.comboBox_ModelList = QtGui.QComboBox(self.frame_2)
        self.comboBox_ModelList.setGeometry(QtCore.QRect(115, 50, 201, 31))
        self.comboBox_ModelList.setObjectName(_fromUtf8("comboBox_ModelList"))
        self.label_19 = QtGui.QLabel(self.frame_2)
        self.label_19.setGeometry(QtCore.QRect(10, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.frame_2)
        self.label_20.setGeometry(QtCore.QRect(300, 130, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.frame_2)
        self.label_21.setGeometry(QtCore.QRect(240, 90, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.spinBox = QtGui.QSpinBox(self.frame_2)
        self.spinBox.setGeometry(QtCore.QRect(400, 90, 51, 31))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(511)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.lineEdit_foot = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_foot.setEnabled(True)
        self.lineEdit_foot.setGeometry(QtCore.QRect(400, 130, 51, 31))
        self.lineEdit_foot.setText(_fromUtf8(""))
        self.lineEdit_foot.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_foot.setReadOnly(True)
        self.lineEdit_foot.setObjectName(_fromUtf8("lineEdit_foot"))
        self.label_22 = QtGui.QLabel(self.frame_2)
        self.label_22.setGeometry(QtCore.QRect(10, 130, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.lineEdit_FixtureModel = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_FixtureModel.setEnabled(True)
        self.lineEdit_FixtureModel.setGeometry(QtCore.QRect(90, 130, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_FixtureModel.setFont(font)
        self.lineEdit_FixtureModel.setText(_fromUtf8(""))
        self.lineEdit_FixtureModel.setReadOnly(True)
        self.lineEdit_FixtureModel.setObjectName(_fromUtf8("lineEdit_FixtureModel"))
        self.label_35 = QtGui.QLabel(self.frame_2)
        self.label_35.setGeometry(QtCore.QRect(460, 10, 300, 200))
        self.label_35.setStyleSheet(_fromUtf8("background-color: rgb(216, 216, 216);"))
        self.label_35.setFrameShape(QtGui.QFrame.Box)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.label_36 = QtGui.QLabel(self.frame_2)
        self.label_36.setGeometry(QtCore.QRect(10, 90, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.lineEdit_ProgramUID = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_ProgramUID.setGeometry(QtCore.QRect(90, 90, 141, 31))
        self.lineEdit_ProgramUID.setObjectName(_fromUtf8("lineEdit_ProgramUID"))
        self.lineEdit_3 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 90, 51, 31))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_PPname = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_PPname.setGeometry(QtCore.QRect(290, 10, 161, 31))
        self.lineEdit_PPname.setReadOnly(True)
        self.lineEdit_PPname.setObjectName(_fromUtf8("lineEdit_PPname"))
        self.label_17 = QtGui.QLabel(self.frame_2)
        self.label_17.setGeometry(QtCore.QRect(230, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.configuration)
        self.label_18.setGeometry(QtCore.QRect(10, 140, 771, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(_fromUtf8("background-color: rgb(130, 200, 255);"))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.frame_3 = QtGui.QFrame(self.configuration)
        self.frame_3.setGeometry(QtCore.QRect(10, 410, 771, 141))
        self.frame_3.setStyleSheet(_fromUtf8(""))
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setLineWidth(1)
        self.frame_3.setMidLineWidth(1)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.pushButton_CH1 = QtGui.QPushButton(self.frame_3)
        self.pushButton_CH1.setGeometry(QtCore.QRect(10, 20, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_CH1.setFont(font)
        self.pushButton_CH1.setObjectName(_fromUtf8("pushButton_CH1"))
        self.pushButton_CH2 = QtGui.QPushButton(self.frame_3)
        self.pushButton_CH2.setGeometry(QtCore.QRect(140, 20, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_CH2.setFont(font)
        self.pushButton_CH2.setObjectName(_fromUtf8("pushButton_CH2"))
        self.pushButton_CH3 = QtGui.QPushButton(self.frame_3)
        self.pushButton_CH3.setGeometry(QtCore.QRect(270, 20, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_CH3.setFont(font)
        self.pushButton_CH3.setObjectName(_fromUtf8("pushButton_CH3"))
        self.pushButton_CH4 = QtGui.QPushButton(self.frame_3)
        self.pushButton_CH4.setGeometry(QtCore.QRect(10, 90, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_CH4.setFont(font)
        self.pushButton_CH4.setObjectName(_fromUtf8("pushButton_CH4"))
        self.pushButton_ALLON = QtGui.QPushButton(self.frame_3)
        self.pushButton_ALLON.setGeometry(QtCore.QRect(140, 90, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_ALLON.setFont(font)
        self.pushButton_ALLON.setObjectName(_fromUtf8("pushButton_ALLON"))
        self.pushButton_ALLOFF = QtGui.QPushButton(self.frame_3)
        self.pushButton_ALLOFF.setGeometry(QtCore.QRect(270, 90, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_ALLOFF.setFont(font)
        self.pushButton_ALLOFF.setObjectName(_fromUtf8("pushButton_ALLOFF"))
        self.label_14 = QtGui.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(410, 20, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(_fromUtf8("background-color: rgb(230, 230, 230);"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.frame_3)
        self.label_15.setGeometry(QtCore.QRect(420, 66, 131, 21))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.frame_3)
        self.label_16.setGeometry(QtCore.QRect(420, 90, 111, 31))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.frame_4 = QtGui.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(410, 40, 351, 91))
        self.frame_4.setStyleSheet(_fromUtf8(""))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.lcdNumber_2 = QtGui.QLCDNumber(self.frame_4)
        self.lcdNumber_2.setGeometry(QtCore.QRect(130, 50, 64, 31))
        self.lcdNumber_2.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.pushButton_test = QtGui.QPushButton(self.frame_4)
        self.pushButton_test.setGeometry(QtCore.QRect(230, 20, 75, 23))
        self.pushButton_test.setObjectName(_fromUtf8("pushButton_test"))
        self.pushButton_test_2 = QtGui.QPushButton(self.frame_4)
        self.pushButton_test_2.setGeometry(QtCore.QRect(230, 50, 75, 23))
        self.pushButton_test_2.setObjectName(_fromUtf8("pushButton_test_2"))
        self.lcdNumber = QtGui.QLCDNumber(self.frame_3)
        self.lcdNumber.setGeometry(QtCore.QRect(540, 60, 64, 31))
        self.lcdNumber.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.label_24 = QtGui.QLabel(self.configuration)
        self.label_24.setGeometry(QtCore.QRect(10, 390, 771, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(11)
        font.setItalic(True)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet(_fromUtf8("background-color: rgb(130, 200, 255);"))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.tabWidget.addTab(self.configuration, _fromUtf8(""))
        self.DisconnectDeviceButton = QtGui.QPushButton(self.centralWidget)
        self.DisconnectDeviceButton.setEnabled(False)
        self.DisconnectDeviceButton.setGeometry(QtCore.QRect(140, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DisconnectDeviceButton.setFont(font)
        self.DisconnectDeviceButton.setObjectName(_fromUtf8("DisconnectDeviceButton"))
        self.label_Device_Status_2 = QtGui.QLabel(self.centralWidget)
        self.label_Device_Status_2.setGeometry(QtCore.QRect(620, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_Device_Status_2.setFont(font)
        self.label_Device_Status_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label_Device_Status_2.setFrameShape(QtGui.QFrame.Box)
        self.label_Device_Status_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Device_Status_2.setObjectName(_fromUtf8("label_Device_Status_2"))
        self.line = QtGui.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(7, 40, 811, 20))
        self.line.setFrameShadow(QtGui.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_34 = QtGui.QLabel(self.centralWidget)
        self.label_34.setGeometry(QtCore.QRect(510, 680, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.commandLinkButton_info = QtGui.QCommandLinkButton(self.centralWidget)
        self.commandLinkButton_info.setGeometry(QtCore.QRect(10, 670, 61, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(8)
        self.commandLinkButton_info.setFont(font)
        self.commandLinkButton_info.setIconSize(QtCore.QSize(15, 15))
        self.commandLinkButton_info.setCheckable(False)
        self.commandLinkButton_info.setAutoDefault(False)
        self.commandLinkButton_info.setDefault(False)
        self.commandLinkButton_info.setObjectName(_fromUtf8("commandLinkButton_info"))
        self.frame_7 = QtGui.QFrame(self.centralWidget)
        self.frame_7.setGeometry(QtCore.QRect(480, 680, 31, 21))
        self.frame_7.setStyleSheet(_fromUtf8("image: url(:/logo/CK.ico);"))
        self.frame_7.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.commandLinkButton_help = QtGui.QCommandLinkButton(self.centralWidget)
        self.commandLinkButton_help.setGeometry(QtCore.QRect(80, 670, 61, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(8)
        self.commandLinkButton_help.setFont(font)
        self.commandLinkButton_help.setIconSize(QtCore.QSize(15, 15))
        self.commandLinkButton_help.setCheckable(False)
        self.commandLinkButton_help.setAutoDefault(False)
        self.commandLinkButton_help.setDefault(False)
        self.commandLinkButton_help.setObjectName(_fromUtf8("commandLinkButton_help"))
        self.label_SJP = QtGui.QLabel(self.centralWidget)
        self.label_SJP.setGeometry(QtCore.QRect(540, 10, 31, 31))
        self.label_SJP.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_SJP.setLineWidth(1)
        self.label_SJP.setText(_fromUtf8(""))
        self.label_SJP.setObjectName(_fromUtf8("label_SJP"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Vaya Configuration", None))
        self.ConnectDeviceButton.setText(_translate("MainWindow", "Connect", None))
        self.label_Device_Status.setText(_translate("MainWindow", " Status:", None))
        self.label_3.setText(_translate("MainWindow", "ESTA Manufacturer ID for PHILIPS", None))
        self.label_4.setText(_translate("MainWindow", "Manufacturer Site ID", None))
        self.label_6.setText(_translate("MainWindow", "Select CM", None))
        self.lineEdit.setText(_translate("MainWindow", "5068", None))
        self.lineEdit_2.setText(_translate("MainWindow", "05", None))
        self.lineEdit_UID.setText(_translate("MainWindow", "5068:________", None))
        self.GenerateUID.setText(_translate("MainWindow", "Generate UID", None))
        self.label_8.setText(_translate("MainWindow", "UID", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">NOTE:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">&gt; The first UID of the day will be generated based on Factory ID and Date Code.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">&gt; Check the Date and Supply Factory</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">&gt; Connect </span><span style=\" font-size:8pt; font-weight:600; color:#ff0000;\">One</span><span style=\" font-size:8pt;\"> unit when using Configuration Tool</span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#284664;\">Parameter</span></p></body></html>", None))
        self.label_13.setText(_translate("MainWindow", "Production Date", None))
        self.pushButton_SelectPP.setText(_translate("MainWindow", "Select Profile", None))
        self.pushButton_SetPara.setText(_translate("MainWindow", "Set Parameters", None))
        self.pushButton_GetPara.setText(_translate("MainWindow", "Get Parameters", None))
        self.label_19.setText(_translate("MainWindow", "Model Description", None))
        self.label_20.setText(_translate("MainWindow", "DMX Footprint", None))
        self.label_21.setText(_translate("MainWindow", "Sequence Number (1-511)", None))
        self.label_22.setText(_translate("MainWindow", "Fixture Model", None))
        self.label_35.setText(_translate("MainWindow", "Fixture Image Displays Here", None))
        self.label_36.setText(_translate("MainWindow", "UID", None))
        self.lineEdit_3.setText(_translate("MainWindow", "5068:", None))
        self.label_17.setText(_translate("MainWindow", "File Name", None))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#284664;\">Basic</span></p></body></html>", None))
        self.pushButton_CH1.setText(_translate("MainWindow", "Channel 1", None))
        self.pushButton_CH2.setText(_translate("MainWindow", "Channel 2", None))
        self.pushButton_CH3.setText(_translate("MainWindow", "Channel 3", None))
        self.pushButton_CH4.setText(_translate("MainWindow", "Channel 4", None))
        self.pushButton_ALLON.setText(_translate("MainWindow", "ALL ON", None))
        self.pushButton_ALLOFF.setText(_translate("MainWindow", "ALL OFF", None))
        self.label_14.setText(_translate("MainWindow", " RS485 Reliability Test", None))
        self.label_15.setText(_translate("MainWindow", "Successful Transfer", None))
        self.label_16.setText(_translate("MainWindow", "Failed Transfer", None))
        self.pushButton_test.setText(_translate("MainWindow", "Start", None))
        self.pushButton_test_2.setText(_translate("MainWindow", "Stop", None))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#284664;\">DMX Test</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.configuration), _translate("MainWindow", "Configuration", None))
        self.DisconnectDeviceButton.setText(_translate("MainWindow", "Disconnect", None))
        self.label_Device_Status_2.setText(_translate("MainWindow", "No Smart Jack Pro Connected", None))
        self.label_34.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#4891d9;\">Philips Solid State Lighting Solutions</span></p></body></html>", None))
        self.commandLinkButton_info.setText(_translate("MainWindow", "Info", None))
        self.commandLinkButton_help.setText(_translate("MainWindow", "Help", None))

import gamut_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
