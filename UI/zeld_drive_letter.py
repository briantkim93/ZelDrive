# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drive_letter.ui'
#
# Created: Wed May 06 18:25:22 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import driveoptions
import controller

class Ui_Zeld_drive_letter(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_Zeld_drive_letter, self).__init__()
        self.setupUi(self)

    def setupUi(self, Zeld_drive_letter):
        Zeld_drive_letter.setObjectName("Zeld_drive_letter")
        Zeld_drive_letter.resize(670, 476)
        Zeld_drive_letter.setMaximumSize(QtCore.QSize(670, 476))
        self.centralwidget = QtGui.QWidget(Zeld_drive_letter)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 371, 51))
        self.label.setObjectName("label")
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(240, 110, 151, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 110, 121, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 240, 101, 31))
        self.pushButton.setObjectName("pushButton")
        Zeld_drive_letter.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Zeld_drive_letter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 21))
        self.menubar.setObjectName("menubar")
        Zeld_drive_letter.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Zeld_drive_letter)
        self.statusbar.setObjectName("statusbar")
        Zeld_drive_letter.setStatusBar(self.statusbar)

        self.get_drive_options()

        self.retranslateUi(Zeld_drive_letter)
        QtCore.QMetaObject.connectSlotsByName(Zeld_drive_letter)
        self.pushButton.clicked.connect(lambda: self.get_drive_options)

    def get_drive_options(self):
        """
        get all the available letters and add them to the combo
        :return: void
        """

        dlist = driveoptions.get_letter_options()
        for elem in dlist:
            self.comboBox.addItem(elem)

    def retranslateUi(self, Zeld_drive_letter):
        """
        :type self:object
        """
        Zeld_drive_letter.setWindowTitle(QtGui.QApplication.translate("Zeld_drive_letter", "Choose drive letter", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Zeld_drive_letter", "We need you to choose a drive letter where you can access your files.\n"
"We have provided you a list of the letters of which you can choose from", None, QtGui.QApplication.UnicodeUTF8))

        self.label_2.setText(QtGui.QApplication.translate("Zeld_drive_letter", "Please choose a letter :", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Zeld_drive_letter", "Confirm", None, QtGui.QApplication.UnicodeUTF8))

    def send_chosen_letter(self):
        """
        Send's the chosen letter
        :return: void
        """
        choice = str(self.comboBox.currentText())
        choice = 0x0000 + ord(choice)

        controller.connect()
        res = controller.set_drive_letter(choice)
        if res == "0x0":
            driveoptions.save_letter_option(choice)
            self.close()
        else:
            self.label.setText("The drive program was not tracebale. Sorry but you\
             could consider reinstalling your ZelDrive.\nThanks")