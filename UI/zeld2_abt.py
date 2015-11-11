# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zeld2_abt.ui'
#
# Created: Sat Aug 22 12:38:53 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_zeld2_abt(object):
    def setupUi(self, zeld2_abt):
        zeld2_abt.setObjectName("zeld2_abt")
        zeld2_abt.resize(625, 410)
        zeld2_abt.setMinimumSize(QtCore.QSize(625, 410))
        zeld2_abt.setMaximumSize(QtCore.QSize(625, 410))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphics/img/image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        zeld2_abt.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(zeld2_abt)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 481, 271))
        self.label.setText("")
        self.label.setObjectName("label")
        self.ok_btn = QtGui.QPushButton(self.centralwidget)
        self.ok_btn.setGeometry(QtCore.QRect(290, 330, 75, 23))
        self.ok_btn.setObjectName("ok_btn")
        zeld2_abt.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(zeld2_abt)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 625, 21))
        self.menubar.setObjectName("menubar")
        zeld2_abt.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(zeld2_abt)
        self.statusbar.setObjectName("statusbar")
        zeld2_abt.setStatusBar(self.statusbar)

        self.retranslateUi(zeld2_abt)
        QtCore.QMetaObject.connectSlotsByName(zeld2_abt)

    def retranslateUi(self, zeld2_abt):
        zeld2_abt.setWindowTitle(QtGui.QApplication.translate("zeld2_abt", "About ZelDrive", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_btn.setText(QtGui.QApplication.translate("zeld2_abt", "OK", None, QtGui.QApplication.UnicodeUTF8))

