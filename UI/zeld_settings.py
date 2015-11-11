# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../zeld_settings.ui'
#
# Created: Thu Feb 19 05:30:59 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import sys

class Ui_SettingsPanel(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_SettingsPanel, self).__init__()
        self.setupUi(self)

    def setupUi(self, SettingsPanel):
        SettingsPanel.setObjectName("SettingsPanel")
        SettingsPanel.setWindowModality(QtCore.Qt.ApplicationModal)
        SettingsPanel.resize(400, 300)
        SettingsPanel.setMaximumSize(QtCore.QSize(500, 500))
        self.groupBox = QtGui.QGroupBox(SettingsPanel)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 341, 101))
        self.groupBox.setObjectName("groupBox")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(100, 20, 91, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setInputMask("999999")
        self.clear_cache_btn = QtGui.QPushButton(self.groupBox)
        self.clear_cache_btn.setGeometry(QtCore.QRect(100, 60, 75, 31))
        self.clear_cache_btn.setObjectName("clear_cache_btn")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(180, 70, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(100, 40, 171, 16))
        self.label_3.setObjectName("label_3")
        self.groupBox_2 = QtGui.QGroupBox(SettingsPanel)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 120, 341, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 51, 16))
        self.label_4.setObjectName("label_4")
        self.spinBox = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox.setMaximum(1000)
        self.spinBox.setMinimum(50)
        self.spinBox.setGeometry(QtCore.QRect(70, 20, 61, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(70, 50, 251, 16))
        self.label_5.setObjectName("label_5")
        self.applysettingsbtn = QtGui.QPushButton(SettingsPanel)
        self.applysettingsbtn.setGeometry(QtCore.QRect(90, 240, 75, 23))
        self.applysettingsbtn.setObjectName("applysettingsbtn")
        self.cancel_settings_btn = QtGui.QPushButton(SettingsPanel)
        self.cancel_settings_btn.setGeometry(QtCore.QRect(200, 240, 75, 23))
        self.cancel_settings_btn.setObjectName("cancel_settings_btn")

        self.retranslateUi(SettingsPanel)
        QtCore.QMetaObject.connectSlotsByName(SettingsPanel)

    def retranslateUi(self, SettingsPanel):
        SettingsPanel.setWindowTitle(QtGui.QApplication.translate("SettingsPanel", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("SettingsPanel", "Cache", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SettingsPanel", "Cache size (MB) : ", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_cache_btn.setText(QtGui.QApplication.translate("SettingsPanel", "Clear Cache", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SettingsPanel", "Be very careful!", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("SettingsPanel", "* This will consumer your disk space", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("SettingsPanel", "Remote File Reading", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("SettingsPanel", "Threads : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("SettingsPanel", "* Use high numbers for more powerful computers", None, QtGui.QApplication.UnicodeUTF8))
        self.applysettingsbtn.setText(QtGui.QApplication.translate("SettingsPanel", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_settings_btn.setText(QtGui.QApplication.translate("SettingsPanel", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
