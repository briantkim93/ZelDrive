# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../zeld_data_not_found.ui'
#
# Created: Tue Feb 24 05:21:47 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

import zeld_registration, zeld_data_import

class Ui_Imp_Reg_Dialog(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_Imp_Reg_Dialog, self).__init__()
        self.setupUi(self)

    def setupUi(self, Imp_Reg_Dialog):
        Imp_Reg_Dialog.setObjectName("Imp_Reg_Dialog")
        Imp_Reg_Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Imp_Reg_Dialog.resize(517, 235)
        self.centralwidget = QtGui.QWidget(Imp_Reg_Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 471, 101))
        self.label.setObjectName("label")
        self.regbtn = QtGui.QPushButton(self.centralwidget)
        self.regbtn.setGeometry(QtCore.QRect(120, 170, 75, 23))
        self.regbtn.setObjectName("regbtn")
        self.imp_btn = QtGui.QPushButton(self.centralwidget)
        self.imp_btn.setGeometry(QtCore.QRect(260, 170, 75, 23))
        self.imp_btn.setObjectName("imp_btn")
        Imp_Reg_Dialog.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Imp_Reg_Dialog)
        self.statusbar.setObjectName("statusbar")
        Imp_Reg_Dialog.setStatusBar(self.statusbar)

        self.retranslateUi(Imp_Reg_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Imp_Reg_Dialog)

    def retranslateUi(self, Imp_Reg_Dialog):
        Imp_Reg_Dialog.setWindowTitle(QtGui.QApplication.translate("Imp_Reg_Dialog", "Data not found", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Imp_Reg_Dialog", "<html><head/><body><p>A loaded drive wasn\'t found. You may do one of the following: </p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you don\'t have an existing ZelDrive account, just click register </li><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you have an existing ZeldDrive account, just click import data to import your data</li></ul></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.regbtn.setText(QtGui.QApplication.translate("Imp_Reg_Dialog", "Register", None, QtGui.QApplication.UnicodeUTF8))
        self.imp_btn.setText(QtGui.QApplication.translate("Imp_Reg_Dialog", "Import Data", None, QtGui.QApplication.UnicodeUTF8))
        self.regbtn.clicked.connect(lambda: self.launch_reg())
        self.imp_btn.clicked.connect(lambda: self.launch_imp())



    def launch_reg(self):
        self.reg = zeld_registration.Ui_Zeld_Register()
        self.reg.show()


    def launch_imp(self):
        self.dataimp = zeld_data_import.Ui_Zeld_Data_Import()
        self.dataimp.show()





