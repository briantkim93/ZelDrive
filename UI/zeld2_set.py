# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zeld2_set.ui'
#
# Created: Mon Aug 24 11:06:53 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_zeld2_set(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_zeld2_set, self).__init__()
        self.setupUi(self)
        self.proxy_settings = False

    def setupUi(self, zeld2_set):
        zeld2_set.setObjectName("zeld2_set")
        zeld2_set.resize(704, 705)
        zeld2_set.setMinimumSize(QtCore.QSize(704, 705))
        zeld2_set.setMaximumSize(QtCore.QSize(704, 705))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphics/img/image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        zeld2_set.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(zeld2_set)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 641, 121))
        self.groupBox.setObjectName("groupBox")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 531, 21))
        self.label.setObjectName("label")
        self.cache_box = QtGui.QLineEdit(self.groupBox)
        self.cache_box.setGeometry(QtCore.QRect(10, 50, 241, 31))
        self.cache_box.setObjectName("cache_box")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 461, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 160, 641, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 531, 21))
        self.label_3.setObjectName("label_3")
        self.drive_letter_box = QtGui.QComboBox(self.groupBox_2)
        self.drive_letter_box.setGeometry(QtCore.QRect(10, 50, 131, 22))
        self.drive_letter_box.setObjectName("drive_letter_box")
        self.drive_letter_box.addItem("")
        self.drive_letter_box.addItem("")
        self.drive_letter_box.addItem("")
        self.drive_letter_box.addItem("")
        self.drive_letter_box.addItem("")
        self.drive_letter_box.addItem("")
        self.drive_letter_box.addItem("")
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 280, 641, 141))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 591, 51))
        self.label_4.setObjectName("label_4")
        self.read_span_box = QtGui.QLineEdit(self.groupBox_3)
        self.read_span_box.setGeometry(QtCore.QRect(10, 80, 71, 31))
        self.read_span_box.setObjectName("read_span_box")
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(30, 440, 641, 171))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 611, 21))
        self.label_5.setObjectName("label_5")
        self.proxy_host_lbl = QtGui.QLabel(self.groupBox_4)
        self.proxy_host_lbl.setEnabled(False)
        self.proxy_host_lbl.setGeometry(QtCore.QRect(20, 70, 61, 16))
        self.proxy_host_lbl.setObjectName("proxy_host_lbl")
        self.proxy_host_box = QtGui.QLineEdit(self.groupBox_4)
        self.proxy_host_box.setEnabled(False)
        self.proxy_host_box.setGeometry(QtCore.QRect(90, 70, 211, 31))
        self.proxy_host_box.setObjectName("proxy_host_box")
        self.proxy_port_lbl = QtGui.QLabel(self.groupBox_4)
        self.proxy_port_lbl.setEnabled(False)
        self.proxy_port_lbl.setGeometry(QtCore.QRect(340, 70, 61, 16))
        self.proxy_port_lbl.setObjectName("proxy_port_lbl")
        self.proxy_port_box = QtGui.QLineEdit(self.groupBox_4)
        self.proxy_port_box.setEnabled(False)
        self.proxy_port_box.setGeometry(QtCore.QRect(410, 70, 81, 31))
        self.proxy_port_box.setObjectName("proxy_port_box")
        self.proxy_usr_lbl = QtGui.QLabel(self.groupBox_4)
        self.proxy_usr_lbl.setEnabled(False)
        self.proxy_usr_lbl.setGeometry(QtCore.QRect(20, 120, 61, 16))
        self.proxy_usr_lbl.setObjectName("proxy_usr_lbl")
        self.proxy_usr_box = QtGui.QLineEdit(self.groupBox_4)
        self.proxy_usr_box.setEnabled(False)
        self.proxy_usr_box.setGeometry(QtCore.QRect(90, 120, 211, 31))
        self.proxy_usr_box.setObjectName("proxy_usr_box")
        self.proxy_pwd_lbl = QtGui.QLabel(self.groupBox_4)
        self.proxy_pwd_lbl.setEnabled(False)
        self.proxy_pwd_lbl.setGeometry(QtCore.QRect(340, 120, 61, 16))
        self.proxy_pwd_lbl.setObjectName("proxy_pwd_lbl")
        self.proxy_pwd_box = QtGui.QLineEdit(self.groupBox_4)
        self.proxy_pwd_box.setEnabled(False)
        self.proxy_pwd_box.setGeometry(QtCore.QRect(410, 120, 191, 31))
        self.proxy_pwd_box.setEchoMode(QtGui.QLineEdit.Password)
        self.proxy_pwd_box.setObjectName("proxy_pwd_box")
        self.checkBox = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox.setGeometry(QtCore.QRect(10, 40, 121, 17))
        self.checkBox.setObjectName("checkBox")
        self.save_btn = QtGui.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(180, 630, 101, 31))
        self.save_btn.setObjectName("save_btn")
        zeld2_set.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(zeld2_set)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 704, 21))
        self.menubar.setObjectName("menubar")
        zeld2_set.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(zeld2_set)
        self.statusbar.setObjectName("statusbar")
        zeld2_set.setStatusBar(self.statusbar)

        self.retranslateUi(zeld2_set)
        QtCore.QMetaObject.connectSlotsByName(zeld2_set)

        self.checkBox.clicked.connect(self.proxy_set_active)

    def retranslateUi(self, zeld2_set):
        zeld2_set.setWindowTitle(QtGui.QApplication.translate("zeld2_set", "ZelDrive - Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("zeld2_set", "Cache", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("zeld2_set", "<html><head/><body><p><span style=\" color:#0055ff;\">Set the cache size in MB. Cache is the local store of the most frequently used files. </span><span style=\" font-weight:600; color:#0055ff;\">Hint:</span><span style=\" color:#0055ff;\"> 1024 MB = 1GB</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("zeld2_set", "<html><head/><body><p><span style=\" color:#aa0000;\">Please be aware that ZelDrive stores cache on your disk. Your local disk will be consumed!</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("zeld2_set", "Drive Letter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("zeld2_set", "<html><head/><body><p><span style=\" color:#0055ff;\">Set the drive letter that ZelDrive will place its files. The default is </span><span style=\" font-weight:600; color:#0055ff;\">Z</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.drive_letter_box.setItemText(0, QtGui.QApplication.translate("zeld2_set", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.drive_letter_box.setItemText(1, QtGui.QApplication.translate("zeld2_set", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.drive_letter_box.setItemText(2, QtGui.QApplication.translate("zeld2_set", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.drive_letter_box.setItemText(3, QtGui.QApplication.translate("zeld2_set", "G", None, QtGui.QApplication.UnicodeUTF8))
        self.drive_letter_box.setItemText(4, QtGui.QApplication.translate("zeld2_set", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.drive_letter_box.setItemText(5, QtGui.QApplication.translate("zeld2_set", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.drive_letter_box.setItemText(6, QtGui.QApplication.translate("zeld2_set", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("zeld2_set", "Read Span", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("zeld2_set", "<html><head/><body><p><span style=\" color:#0055ff;\">Read Span is the number of times we split a file for reading to improve read speeds</span></p><p><span style=\" font-weight:600; color:#0055ff;\">Hint: </span><span style=\" color:#0055ff;\">Large numbers can also negatively affect performance. Enter 0 for ZelDrive to choose the best value for you</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("zeld2_set", "Proxy Server Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("zeld2_set", "<html><head/><body><p><span style=\" color:#0055ff;\">Does your connection need a proxy server to connect to the internet?</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_host_lbl.setText(QtGui.QApplication.translate("zeld2_set", "Proxy Host:", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_port_lbl.setText(QtGui.QApplication.translate("zeld2_set", "Proxy Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_usr_lbl.setText(QtGui.QApplication.translate("zeld2_set", "Username:", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy_pwd_lbl.setText(QtGui.QApplication.translate("zeld2_set", "Password: ", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("zeld2_set", "Yes I use a proxy", None, QtGui.QApplication.UnicodeUTF8))
        self.save_btn.setText(QtGui.QApplication.translate("zeld2_set", "Save", None, QtGui.QApplication.UnicodeUTF8))

    def proxy_set_active(self):
        if not self.proxy_settings:
            self.proxy_host_lbl.setEnabled(True)
            self.proxy_host_box.setEnabled(True)
            self.proxy_port_lbl.setEnabled(True)
            self.proxy_port_box.setEnabled(True)
            self.proxy_usr_lbl.setEnabled(True)
            self.proxy_usr_box.setEnabled(True)
            self.proxy_pwd_lbl.setEnabled(True)
            self.proxy_pwd_box.setEnabled(True)
            self.proxy_settings = True
        else:
            self.proxy_host_lbl.setEnabled(False)
            self.proxy_host_box.setEnabled(False)
            self.proxy_port_lbl.setEnabled(False)
            self.proxy_port_box.setEnabled(False)
            self.proxy_usr_lbl.setEnabled(False)
            self.proxy_usr_box.setEnabled(False)
            self.proxy_pwd_lbl.setEnabled(False)
            self.proxy_pwd_box.setEnabled(False)
            self.proxy_settings = False
