# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\310098157\Dropbox\Works@PCK\Engineering\Working Directory\Software Project\Python Project\VayaPlay\VayaMfgMainWin.ui'
#
# Created: Wed Mar 26 14:10:19 2014
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
        MainWindow.resize(820, 715)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(820, 715))
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
        self.addressing = QtGui.QWidget()
        self.addressing.setObjectName(_fromUtf8("addressing"))
        self.tableWidget_DiscoverFixtures = QtGui.QTableWidget(self.addressing)
        self.tableWidget_DiscoverFixtures.setGeometry(QtCore.QRect(10, 10, 781, 291))
        self.tableWidget_DiscoverFixtures.setStyleSheet(_fromUtf8(""))
        self.tableWidget_DiscoverFixtures.setObjectName(_fromUtf8("tableWidget_DiscoverFixtures"))
        self.tableWidget_DiscoverFixtures.setColumnCount(8)
        self.tableWidget_DiscoverFixtures.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_DiscoverFixtures.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_DiscoverFixtures.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_DiscoverFixtures.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_DiscoverFixtures.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_DiscoverFixtures.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_DiscoverFixtures.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_DiscoverFixtures.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_DiscoverFixtures.setHorizontalHeaderItem(7, item)
        self.pushButton_Discover = QtGui.QPushButton(self.addressing)
        self.pushButton_Discover.setGeometry(QtCore.QRect(380, 520, 181, 41))
        self.pushButton_Discover.setObjectName(_fromUtf8("pushButton_Discover"))
        self.tabWidget_2 = QtGui.QTabWidget(self.addressing)
        self.tabWidget_2.setGeometry(QtCore.QRect(370, 310, 411, 201))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_23 = QtGui.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(30, 10, 141, 20))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.lineEdit_DMXAddr = QtGui.QLineEdit(self.tab)
        self.lineEdit_DMXAddr.setEnabled(True)
        self.lineEdit_DMXAddr.setGeometry(QtCore.QRect(30, 30, 181, 31))
        self.lineEdit_DMXAddr.setObjectName(_fromUtf8("lineEdit_DMXAddr"))
        self.Button_DMXSet = QtGui.QPushButton(self.tab)
        self.Button_DMXSet.setEnabled(True)
        self.Button_DMXSet.setGeometry(QtCore.QRect(240, 30, 101, 31))
        self.Button_DMXSet.setObjectName(_fromUtf8("Button_DMXSet"))
        self.label_25 = QtGui.QLabel(self.tab)
        self.label_25.setGeometry(QtCore.QRect(30, 110, 141, 20))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.lineEdit_DeviceLabel = QtGui.QLineEdit(self.tab)
        self.lineEdit_DeviceLabel.setEnabled(True)
        self.lineEdit_DeviceLabel.setGeometry(QtCore.QRect(30, 130, 181, 31))
        self.lineEdit_DeviceLabel.setObjectName(_fromUtf8("lineEdit_DeviceLabel"))
        self.Button_LabelSet = QtGui.QPushButton(self.tab)
        self.Button_LabelSet.setEnabled(True)
        self.Button_LabelSet.setGeometry(QtCore.QRect(240, 130, 101, 31))
        self.Button_LabelSet.setObjectName(_fromUtf8("Button_LabelSet"))
        self.label_24 = QtGui.QLabel(self.tab)
        self.label_24.setGeometry(QtCore.QRect(30, 60, 141, 20))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.lineEdit_LightNo = QtGui.QLineEdit(self.tab)
        self.lineEdit_LightNo.setEnabled(True)
        self.lineEdit_LightNo.setGeometry(QtCore.QRect(30, 80, 181, 31))
        self.lineEdit_LightNo.setObjectName(_fromUtf8("lineEdit_LightNo"))
        self.Button_LightNo = QtGui.QPushButton(self.tab)
        self.Button_LightNo.setEnabled(True)
        self.Button_LightNo.setGeometry(QtCore.QRect(240, 80, 101, 31))
        self.Button_LightNo.setObjectName(_fromUtf8("Button_LightNo"))
        self.tabWidget_2.addTab(self.tab, _fromUtf8(""))
        self.pushButton_Export = QtGui.QPushButton(self.addressing)
        self.pushButton_Export.setGeometry(QtCore.QRect(590, 520, 181, 41))
        self.pushButton_Export.setObjectName(_fromUtf8("pushButton_Export"))
        self.label_fixture = QtGui.QLabel(self.addressing)
        self.label_fixture.setGeometry(QtCore.QRect(20, 319, 341, 241))
        self.label_fixture.setFrameShape(QtGui.QFrame.Box)
        self.label_fixture.setFrameShadow(QtGui.QFrame.Plain)
        self.label_fixture.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fixture.setObjectName(_fromUtf8("label_fixture"))
        self.tabWidget.addTab(self.addressing, _fromUtf8(""))
        self.fixedcolor = QtGui.QWidget()
        self.fixedcolor.setObjectName(_fromUtf8("fixedcolor"))
        self.lineEdit_R = QtGui.QLineEdit(self.fixedcolor)
        self.lineEdit_R.setEnabled(False)
        self.lineEdit_R.setGeometry(QtCore.QRect(295, 350, 41, 20))
        self.lineEdit_R.setObjectName(_fromUtf8("lineEdit_R"))
        self.horizontalSlider_B = QtGui.QSlider(self.fixedcolor)
        self.horizontalSlider_B.setEnabled(False)
        self.horizontalSlider_B.setGeometry(QtCore.QRect(45, 410, 241, 19))
        self.horizontalSlider_B.setMaximum(255)
        self.horizontalSlider_B.setProperty("value", 255)
        self.horizontalSlider_B.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_B.setObjectName(_fromUtf8("horizontalSlider_B"))
        self.lineEdit_B = QtGui.QLineEdit(self.fixedcolor)
        self.lineEdit_B.setEnabled(False)
        self.lineEdit_B.setGeometry(QtCore.QRect(295, 410, 41, 20))
        self.lineEdit_B.setObjectName(_fromUtf8("lineEdit_B"))
        self.horizontalSlider_G = QtGui.QSlider(self.fixedcolor)
        self.horizontalSlider_G.setEnabled(False)
        self.horizontalSlider_G.setGeometry(QtCore.QRect(45, 380, 241, 19))
        self.horizontalSlider_G.setMaximum(255)
        self.horizontalSlider_G.setProperty("value", 255)
        self.horizontalSlider_G.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_G.setObjectName(_fromUtf8("horizontalSlider_G"))
        self.horizontalSlider_R = QtGui.QSlider(self.fixedcolor)
        self.horizontalSlider_R.setEnabled(False)
        self.horizontalSlider_R.setGeometry(QtCore.QRect(45, 350, 241, 19))
        self.horizontalSlider_R.setMaximum(255)
        self.horizontalSlider_R.setProperty("value", 255)
        self.horizontalSlider_R.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_R.setObjectName(_fromUtf8("horizontalSlider_R"))
        self.label_31 = QtGui.QLabel(self.fixedcolor)
        self.label_31.setGeometry(QtCore.QRect(15, 350, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.label_32 = QtGui.QLabel(self.fixedcolor)
        self.label_32.setGeometry(QtCore.QRect(15, 380, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.lineEdit_G = QtGui.QLineEdit(self.fixedcolor)
        self.lineEdit_G.setEnabled(False)
        self.lineEdit_G.setGeometry(QtCore.QRect(295, 380, 41, 20))
        self.lineEdit_G.setObjectName(_fromUtf8("lineEdit_G"))
        self.label_33 = QtGui.QLabel(self.fixedcolor)
        self.label_33.setGeometry(QtCore.QRect(15, 410, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.hueView = QtGui.QFrame(self.fixedcolor)
        self.hueView.setGeometry(QtCore.QRect(15, 25, 765, 260))
        self.hueView.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.hueView.setMouseTracking(True)
        self.hueView.setStyleSheet(_fromUtf8("image: url(:/HueView/GAMUT.PNG);"))
        self.hueView.setFrameShape(QtGui.QFrame.Box)
        self.hueView.setFrameShadow(QtGui.QFrame.Raised)
        self.hueView.setLineWidth(2)
        self.hueView.setObjectName(_fromUtf8("hueView"))
        self.label_cursur = QtGui.QLabel(self.hueView)
        self.label_cursur.setGeometry(QtCore.QRect(0, 255, 8, 8))
        self.label_cursur.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label_cursur.setFrameShape(QtGui.QFrame.Box)
        self.label_cursur.setLineWidth(2)
        self.label_cursur.setText(_fromUtf8(""))
        self.label_cursur.setObjectName(_fromUtf8("label_cursur"))
        self.tabWidget.addTab(self.fixedcolor, _fromUtf8(""))
        self.colorwash = QtGui.QWidget()
        self.colorwash.setObjectName(_fromUtf8("colorwash"))
        self.label_2 = QtGui.QLabel(self.colorwash)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_washstop = QtGui.QPushButton(self.colorwash)
        self.pushButton_washstop.setGeometry(QtCore.QRect(670, 110, 101, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_washstop.sizePolicy().hasHeightForWidth())
        self.pushButton_washstop.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_washstop.setFont(font)
        self.pushButton_washstop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_washstop.setAutoDefault(False)
        self.pushButton_washstop.setDefault(False)
        self.pushButton_washstop.setFlat(False)
        self.pushButton_washstop.setObjectName(_fromUtf8("pushButton_washstop"))
        self.frame_wash = QtGui.QFrame(self.colorwash)
        self.frame_wash.setGeometry(QtCore.QRect(10, 30, 771, 31))
        self.frame_wash.setStyleSheet(_fromUtf8(""))
        self.frame_wash.setFrameShape(QtGui.QFrame.Box)
        self.frame_wash.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_wash.setObjectName(_fromUtf8("frame_wash"))
        self.label_10 = QtGui.QLabel(self.colorwash)
        self.label_10.setGeometry(QtCore.QRect(600, 80, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setFrameShape(QtGui.QFrame.Box)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalSlider_2 = QtGui.QSlider(self.colorwash)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(110, 80, 471, 20))
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setMaximum(30)
        self.horizontalSlider_2.setPageStep(1)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setTickPosition(QtGui.QSlider.NoTicks)
        self.horizontalSlider_2.setTickInterval(0)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.label_6 = QtGui.QLabel(self.colorwash)
        self.label_6.setGeometry(QtCore.QRect(640, 80, 46, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton_washstart = QtGui.QPushButton(self.colorwash)
        self.pushButton_washstart.setGeometry(QtCore.QRect(560, 110, 101, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_washstart.setFont(font)
        self.pushButton_washstart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_washstart.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_washstart.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_washstart.setAcceptDrops(False)
        self.pushButton_washstart.setAutoFillBackground(False)
        self.pushButton_washstart.setStyleSheet(_fromUtf8(""))
        self.pushButton_washstart.setAutoDefault(False)
        self.pushButton_washstart.setDefault(False)
        self.pushButton_washstart.setFlat(False)
        self.pushButton_washstart.setObjectName(_fromUtf8("pushButton_washstart"))
        self.tabWidget.addTab(self.colorwash, _fromUtf8(""))
        self.channeltest = QtGui.QWidget()
        self.channeltest.setObjectName(_fromUtf8("channeltest"))
        self.label_35 = QtGui.QLabel(self.channeltest)
        self.label_35.setGeometry(QtCore.QRect(20, 480, 46, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.horizontalSlider_value = QtGui.QSlider(self.channeltest)
        self.horizontalSlider_value.setGeometry(QtCore.QRect(70, 480, 160, 21))
        self.horizontalSlider_value.setMaximum(255)
        self.horizontalSlider_value.setProperty("value", 255)
        self.horizontalSlider_value.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_value.setObjectName(_fromUtf8("horizontalSlider_value"))
        self.pushButton_testchannelAllOn = QtGui.QPushButton(self.channeltest)
        self.pushButton_testchannelAllOn.setGeometry(QtCore.QRect(644, 470, 131, 31))
        self.pushButton_testchannelAllOn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_testchannelAllOn.setDefault(False)
        self.pushButton_testchannelAllOn.setFlat(False)
        self.pushButton_testchannelAllOn.setObjectName(_fromUtf8("pushButton_testchannelAllOn"))
        self.tableWidget_channeltest = QtGui.QTableWidget(self.channeltest)
        self.tableWidget_channeltest.setEnabled(True)
        self.tableWidget_channeltest.setGeometry(QtCore.QRect(10, 20, 782, 421))
        self.tableWidget_channeltest.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tableWidget_channeltest.setStyleSheet(_fromUtf8(""))
        self.tableWidget_channeltest.setFrameShape(QtGui.QFrame.NoFrame)
        self.tableWidget_channeltest.setLineWidth(1)
        self.tableWidget_channeltest.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_channeltest.setDragDropOverwriteMode(False)
        self.tableWidget_channeltest.setShowGrid(True)
        self.tableWidget_channeltest.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_channeltest.setRowCount(32)
        self.tableWidget_channeltest.setColumnCount(16)
        self.tableWidget_channeltest.setObjectName(_fromUtf8("tableWidget_channeltest"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setVerticalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setVerticalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setVerticalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setVerticalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setVerticalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setVerticalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setVerticalHeaderItem(16, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tableWidget_channeltest.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setHorizontalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setHorizontalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setKerning(False)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_channeltest.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setItem(0, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setItem(0, 5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setItem(0, 6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setItem(0, 7, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_channeltest.setItem(0, 8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setItem(0, 9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setItem(0, 10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setItem(0, 11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setItem(0, 12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setItem(0, 13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setItem(0, 14, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setItem(0, 15, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setItem(1, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_channeltest.setItem(31, 14, item)
        self.tableWidget_channeltest.horizontalHeader().setVisible(False)
        self.tableWidget_channeltest.horizontalHeader().setDefaultSectionSize(47)
        self.tableWidget_channeltest.horizontalHeader().setHighlightSections(True)
        self.tableWidget_channeltest.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_channeltest.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_channeltest.verticalHeader().setVisible(False)
        self.spinBox_2 = QtGui.QSpinBox(self.channeltest)
        self.spinBox_2.setEnabled(False)
        self.spinBox_2.setGeometry(QtCore.QRect(240, 480, 42, 22))
        self.spinBox_2.setMaximum(255)
        self.spinBox_2.setProperty("value", 255)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.pushButton_testchannelAllOff = QtGui.QPushButton(self.channeltest)
        self.pushButton_testchannelAllOff.setGeometry(QtCore.QRect(500, 470, 131, 31))
        self.pushButton_testchannelAllOff.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_testchannelAllOff.setAutoDefault(False)
        self.pushButton_testchannelAllOff.setDefault(False)
        self.pushButton_testchannelAllOff.setFlat(False)
        self.pushButton_testchannelAllOff.setObjectName(_fromUtf8("pushButton_testchannelAllOff"))
        self.tabWidget.addTab(self.channeltest, _fromUtf8(""))
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
        self.label_SJP.setText(_fromUtf8(""))
        self.label_SJP.setObjectName(_fromUtf8("label_SJP"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Vaya Play", None))
        self.ConnectDeviceButton.setText(_translate("MainWindow", "Connect", None))
        self.label_Device_Status.setText(_translate("MainWindow", " Status:", None))
        item = self.tableWidget_DiscoverFixtures.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "UID", None))
        item = self.tableWidget_DiscoverFixtures.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "DMX", None))
        item = self.tableWidget_DiscoverFixtures.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Fixture Type", None))
        item = self.tableWidget_DiscoverFixtures.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "RDM Version", None))
        item = self.tableWidget_DiscoverFixtures.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Footprint", None))
        item = self.tableWidget_DiscoverFixtures.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Firmware Version", None))
        item = self.tableWidget_DiscoverFixtures.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Manufacture ID", None))
        item = self.tableWidget_DiscoverFixtures.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Device Label", None))
        self.pushButton_Discover.setText(_translate("MainWindow", "Discover", None))
        self.label_23.setText(_translate("MainWindow", "DMX Start Address", None))
        self.Button_DMXSet.setText(_translate("MainWindow", "Set", None))
        self.label_25.setText(_translate("MainWindow", "Device Label", None))
        self.Button_LabelSet.setText(_translate("MainWindow", "Set", None))
        self.label_24.setText(_translate("MainWindow", "Light Number", None))
        self.Button_LightNo.setToolTip(_translate("MainWindow", "<html><head/><body><p>Light Number is only valid if ALL lights have exactly 3 Channels</p></body></html>", None))
        self.Button_LightNo.setText(_translate("MainWindow", "Set", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Basic Settings", None))
        self.pushButton_Export.setText(_translate("MainWindow", "Export Report", None))
        self.label_fixture.setText(_translate("MainWindow", "Fixture Display", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.addressing), _translate("MainWindow", "Addressing", None))
        self.lineEdit_R.setText(_translate("MainWindow", "255", None))
        self.lineEdit_B.setText(_translate("MainWindow", "255", None))
        self.label_31.setText(_translate("MainWindow", "R", None))
        self.label_32.setText(_translate("MainWindow", "G", None))
        self.lineEdit_G.setText(_translate("MainWindow", "255", None))
        self.label_33.setText(_translate("MainWindow", "B", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fixedcolor), _translate("MainWindow", "Fixed Color", None))
        self.label_2.setText(_translate("MainWindow", "Color Cycle", None))
        self.pushButton_washstop.setText(_translate("MainWindow", "Stop", None))
        self.label_10.setText(_translate("MainWindow", "1 ", None))
        self.label_6.setText(_translate("MainWindow", "Second", None))
        self.pushButton_washstart.setText(_translate("MainWindow", "Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.colorwash), _translate("MainWindow", "Color Wash", None))
        self.label_35.setText(_translate("MainWindow", "Value", None))
        self.pushButton_testchannelAllOn.setText(_translate("MainWindow", "ALL ON", None))
        self.tableWidget_channeltest.setSortingEnabled(False)
        item = self.tableWidget_channeltest.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1", None))
        item = self.tableWidget_channeltest.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2", None))
        item = self.tableWidget_channeltest.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3", None))
        item = self.tableWidget_channeltest.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4", None))
        item = self.tableWidget_channeltest.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5", None))
        item = self.tableWidget_channeltest.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6", None))
        item = self.tableWidget_channeltest.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7", None))
        item = self.tableWidget_channeltest.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8", None))
        item = self.tableWidget_channeltest.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "10", None))
        item = self.tableWidget_channeltest.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "12", None))
        item = self.tableWidget_channeltest.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "13", None))
        item = self.tableWidget_channeltest.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "14", None))
        item = self.tableWidget_channeltest.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "15", None))
        item = self.tableWidget_channeltest.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "16", None))
        item = self.tableWidget_channeltest.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "17", None))
        item = self.tableWidget_channeltest.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "18", None))
        item = self.tableWidget_channeltest.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "20", None))
        item = self.tableWidget_channeltest.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1", None))
        item = self.tableWidget_channeltest.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "2", None))
        item = self.tableWidget_channeltest.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "3", None))
        item = self.tableWidget_channeltest.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "4", None))
        item = self.tableWidget_channeltest.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "5", None))
        item = self.tableWidget_channeltest.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "6", None))
        item = self.tableWidget_channeltest.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "7", None))
        item = self.tableWidget_channeltest.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "8", None))
        item = self.tableWidget_channeltest.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "9", None))
        item = self.tableWidget_channeltest.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "10", None))
        item = self.tableWidget_channeltest.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "11", None))
        item = self.tableWidget_channeltest.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "12", None))
        item = self.tableWidget_channeltest.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "13", None))
        item = self.tableWidget_channeltest.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "14", None))
        item = self.tableWidget_channeltest.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "16", None))
        __sortingEnabled = self.tableWidget_channeltest.isSortingEnabled()
        self.tableWidget_channeltest.setSortingEnabled(False)
        item = self.tableWidget_channeltest.item(0, 0)
        item.setText(_translate("MainWindow", "1", None))
        item = self.tableWidget_channeltest.item(0, 1)
        item.setText(_translate("MainWindow", "2", None))
        item = self.tableWidget_channeltest.item(0, 2)
        item.setText(_translate("MainWindow", "3", None))
        item = self.tableWidget_channeltest.item(0, 3)
        item.setText(_translate("MainWindow", "4", None))
        item = self.tableWidget_channeltest.item(0, 4)
        item.setText(_translate("MainWindow", "5", None))
        item = self.tableWidget_channeltest.item(0, 5)
        item.setText(_translate("MainWindow", "6", None))
        item = self.tableWidget_channeltest.item(0, 6)
        item.setText(_translate("MainWindow", "7", None))
        item = self.tableWidget_channeltest.item(0, 7)
        item.setText(_translate("MainWindow", "8", None))
        item = self.tableWidget_channeltest.item(0, 8)
        item.setText(_translate("MainWindow", "9", None))
        item = self.tableWidget_channeltest.item(0, 9)
        item.setText(_translate("MainWindow", "10", None))
        item = self.tableWidget_channeltest.item(0, 10)
        item.setText(_translate("MainWindow", "11", None))
        item = self.tableWidget_channeltest.item(0, 11)
        item.setText(_translate("MainWindow", "12", None))
        item = self.tableWidget_channeltest.item(0, 12)
        item.setText(_translate("MainWindow", "13", None))
        item = self.tableWidget_channeltest.item(0, 13)
        item.setText(_translate("MainWindow", "14", None))
        item = self.tableWidget_channeltest.item(0, 14)
        item.setText(_translate("MainWindow", "15", None))
        item = self.tableWidget_channeltest.item(0, 15)
        item.setText(_translate("MainWindow", "16", None))
        item = self.tableWidget_channeltest.item(31, 14)
        item.setText(_translate("MainWindow", "512", None))
        self.tableWidget_channeltest.setSortingEnabled(__sortingEnabled)
        self.pushButton_testchannelAllOff.setText(_translate("MainWindow", "ALL OFF", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.channeltest), _translate("MainWindow", "Channel Test", None))
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

