# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import PyQt4.QtGui, PyQt4.QtCore, sys

from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature

from Ui_CDAMainWin import Ui_MainWindow

import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pylab import *



class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
        #Show the SJP device picture but not connect
        pixmap = PyQt4.QtGui.QPixmap( 'CIE_1976_UCS.png' )
        PP = PyQt4.QtGui.QImage( pixmap )
        self.CIE1976_Label.setPixmap(pixmap)
        
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        PlotDemo()
        pixmap = PyQt4.QtGui.QPixmap( 'a.png' )
        PP = PyQt4.QtGui.QImage( pixmap )
        self.Intensity_Label.setPixmap(pixmap)

def PlotDemo ():
    '''
    delta = 0.025
    x = y = np.arange(-3.0, 3.0, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
    Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
    Z = Z2-Z1  # difference of Gaussians

    im = plt.imshow(Z, interpolation='bilinear', cmap=cm.RdYlGn,
                origin='lower', extent=[-3,3,-3,3],
                vmax=abs(Z).max(), vmin=-abs(Z).max())


    '''
    
    #plt.show()
    img = plt.imread('CIE_1976_UCS.png')
    plt.imshow(img, zorder =0, alpha =0.5, interpolation='nearest')
    
    
    plt.xlabel("u'")
    plt.ylabel("V'")
    plt.title("Chromatisity CIE 1976")
    plt.xlim(0, 0.6)
    plt.ylim(0, 0.6)
    plt.plot(0.111, 0.222, '.',  alpha =0.5)
    
    
    
    plt.savefig('a.png',  transparent=True)
    plt.show()
    
    
'''
dt = 0.01
t = arange(0,10,dt)
nse = randn(len(t))
r = exp(-t/0.05)

cnse = convolve(nse, r)*dt
cnse = cnse[:len(t)]
s = 0.1*sin(2*pi*t) + cnse

subplot(211)
plot(t,s)
subplot(212)
psd(s, 512, 1/dt)
'''

if __name__ == "__main__":
    app2 = PyQt4.QtGui.QApplication(sys.argv)
    ui = MainWindow() #should use local class
    ui.show()

    sys.exit(app2.exec_())
