# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zeld2_imp_p.ui'
#
# Created: Sat Aug 22 12:40:15 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_zeld2_imp_p(object):
    def setupUi(self, zeld2_imp_p):
        zeld2_imp_p.setObjectName("zeld2_imp_p")
        zeld2_imp_p.resize(764, 372)
        zeld2_imp_p.setMinimumSize(QtCore.QSize(764, 372))
        zeld2_imp_p.setMaximumSize(QtCore.QSize(764, 372))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphics/img/image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        zeld2_imp_p.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(zeld2_imp_p)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 711, 201))
        self.label.setObjectName("label")
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(40, 250, 681, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.fin_btn = QtGui.QPushButton(self.centralwidget)
        self.fin_btn.setEnabled(False)
        self.fin_btn.setGeometry(QtCore.QRect(260, 300, 75, 23))
        self.fin_btn.setAutoDefault(True)
        self.fin_btn.setFlat(False)
        self.fin_btn.setObjectName("fin_btn")
        zeld2_imp_p.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(zeld2_imp_p)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 21))
        self.menubar.setObjectName("menubar")
        zeld2_imp_p.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(zeld2_imp_p)
        self.statusbar.setObjectName("statusbar")
        zeld2_imp_p.setStatusBar(self.statusbar)

        self.retranslateUi(zeld2_imp_p)
        QtCore.QMetaObject.connectSlotsByName(zeld2_imp_p)

    def retranslateUi(self, zeld2_imp_p):
        zeld2_imp_p.setWindowTitle(QtGui.QApplication.translate("zeld2_imp_p", "ZelDrive - Drive Import", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("zeld2_imp_p", "<html><head/><body><p><span style=\" font-size:11pt;\">Please be patient as we import your drive..</span></p><p><span style=\" font-size:12pt; text-decoration: underline; color:#aa0000;\">Tips</span></p><p><span style=\" font-size:10pt; color:#000000;\">1. The blue bar below shows your drive import progress</span></p><p><span style=\" font-size:10pt; color:#000000;\">2. The time taken to import your drive depends on the number of files you have, not the total size of the files <br/>    or the total space consumed in your drive</span></p><p><span style=\" font-size:10pt; color:#000000;\">3. Importing drives clears existing cache! If this is not a shared device, don\'t do this often</span></p><p><span style=\" font-size:10pt; color:#000000;\">4. When the blue bar below is full and indicates 100%, click </span><span style=\" font-size:10pt; font-weight:600; color:#000000;\">Finish</span></p><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.fin_btn.setText(QtGui.QApplication.translate("zeld2_imp_p", "Finish", None, QtGui.QApplication.UnicodeUTF8))

