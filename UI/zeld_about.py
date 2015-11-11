# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../zeld_about.ui'
#
# Created: Thu Feb 19 05:28:57 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import sys


class Ui_Zeld_About(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_Zeld_About, self).__init__()
        self.setupUi(self)

    def setupUi(self, Zeld_About):
        Zeld_About.setObjectName("Zeld_About")
        Zeld_About.setWindowModality(QtCore.Qt.ApplicationModal)
        Zeld_About.resize(376, 296)
        Zeld_About.setMaximumSize(QtCore.QSize(376, 296))
        self.centralwidget = QtGui.QWidget(Zeld_About)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 130, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 230, 181, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 150, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 170, 251, 51))
        self.label_4.setObjectName("label_4")
        Zeld_About.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Zeld_About)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 376, 21))
        self.menubar.setObjectName("menubar")
        Zeld_About.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Zeld_About)
        self.statusbar.setObjectName("statusbar")
        Zeld_About.setStatusBar(self.statusbar)

        self.retranslateUi(Zeld_About)
        QtCore.QMetaObject.connectSlotsByName(Zeld_About)

    def retranslateUi(self, Zeld_About):
        Zeld_About.setWindowTitle(QtGui.QApplication.translate("Zeld_About", "About ZelDrive", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Zeld_About", "ZelDrive 1.0 alpha", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Zeld_About", "A product by ZelDrive, Inc <font>&copy;</font> 2015", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Zeld_About", "ZelFS 1.0 beta", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Zeld_About", "This product has been protected from copying\n"
"by law. Those found copying will face legal penalties ", None, QtGui.QApplication.UnicodeUTF8))
