# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zeld2_imp_d.ui'
#
# Created: Sat Aug 22 12:39:38 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_zeld2_imp_d(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_zeld2_imp_d, self).__init__()
        self.setupUi(self)

    def setupUi(self, zeld2_imp_d):
        zeld2_imp_d.setObjectName("zeld2_imp_d")
        zeld2_imp_d.resize(721, 438)
        zeld2_imp_d.setMinimumSize(QtCore.QSize(721, 438))
        zeld2_imp_d.setMaximumSize(QtCore.QSize(721, 438))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphics/img/image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        zeld2_imp_d.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(zeld2_imp_d)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 661, 361))
        self.groupBox.setObjectName("groupBox")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(80, 90, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.email_box = QtGui.QLineEdit(self.groupBox)
        self.email_box.setGeometry(QtCore.QRect(150, 90, 271, 31))
        self.email_box.setObjectName("email_box")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pwd_box = QtGui.QLineEdit(self.groupBox)
        self.pwd_box.setGeometry(QtCore.QRect(150, 150, 271, 31))
        self.pwd_box.setEchoMode(QtGui.QLineEdit.Password)
        self.pwd_box.setObjectName("pwd_box")
        self.imp_btn = QtGui.QPushButton(self.groupBox)
        self.imp_btn.setGeometry(QtCore.QRect(150, 240, 141, 31))
        self.imp_btn.setObjectName("imp_btn")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 30, 331, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        zeld2_imp_d.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(zeld2_imp_d)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 721, 21))
        self.menubar.setObjectName("menubar")
        zeld2_imp_d.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(zeld2_imp_d)
        self.statusbar.setObjectName("statusbar")
        zeld2_imp_d.setStatusBar(self.statusbar)

        self.retranslateUi(zeld2_imp_d)
        QtCore.QMetaObject.connectSlotsByName(zeld2_imp_d)

    def retranslateUi(self, zeld2_imp_d):
        zeld2_imp_d.setWindowTitle(QtGui.QApplication.translate("zeld2_imp_d", "ZelDrive Import Drive", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("zeld2_imp_d", "Import your drive", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("zeld2_imp_d", "Email :", None, QtGui.QApplication.UnicodeUTF8))
        self.email_box.setPlaceholderText(QtGui.QApplication.translate("zeld2_imp_d", "Enter your email", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("zeld2_imp_d", "Password  :", None, QtGui.QApplication.UnicodeUTF8))
        self.pwd_box.setPlaceholderText(QtGui.QApplication.translate("zeld2_imp_d", "Enter your password", None, QtGui.QApplication.UnicodeUTF8))
        self.imp_btn.setText(QtGui.QApplication.translate("zeld2_imp_d", "Start Import", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("zeld2_imp_d", "<html><head/><body><p><span style=\" font-weight:600; color:#0055ff;\">Hint</span><span style=\" color:#0055ff;\">: Use the email and password you used to register at ZelDrive</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

