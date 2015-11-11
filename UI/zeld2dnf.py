# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zeld2dnf.ui'
#
# Created: Sat Aug 22 12:41:05 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_zeld2_dnf(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_zeld2_dnf, self).__init__()
        self.setupUi(self)

    def setupUi(self, zeld2_dnf):
        zeld2_dnf.setObjectName("zeld2_dnf")
        zeld2_dnf.resize(563, 325)
        zeld2_dnf.setMinimumSize(QtCore.QSize(563, 325))
        zeld2_dnf.setMaximumSize(QtCore.QSize(563, 325))
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("graphics/img/image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        zeld2_dnf.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(zeld2_dnf)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 581, 161))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.reg_btn = QtGui.QPushButton(self.centralwidget)
        self.reg_btn.setGeometry(QtCore.QRect(80, 200, 91, 31))
        self.reg_btn.setObjectName("reg_btn")
        self.imp_btn = QtGui.QPushButton(self.centralwidget)
        self.imp_btn.setGeometry(QtCore.QRect(250, 200, 91, 31))
        self.imp_btn.setObjectName("imp_btn")
        zeld2_dnf.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(zeld2_dnf)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 21))
        self.menubar.setObjectName("menubar")
        zeld2_dnf.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(zeld2_dnf)
        self.statusbar.setObjectName("statusbar")
        zeld2_dnf.setStatusBar(self.statusbar)

        self.retranslateUi(zeld2_dnf)
        QtCore.QMetaObject.connectSlotsByName(zeld2_dnf)

        self.reg_btn.clicked.connect(self.launch_reg)
        self.imp_btn.clicked.connect(self.launch_imp_d)

    def retranslateUi(self, zeld2_dnf):
        zeld2_dnf.setWindowTitle(QtGui.QApplication.translate("zeld2_dnf", "ZelDrive -Oops!", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("zeld2_dnf", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#aa0000;\">Oops!</span></p><p><span style=\" font-size:11pt; color:#000000;\">No loaded drive was found on this device :(</span></p><p><br/><span style=\" font-size:11pt;\">1. </span><span style=\" font-size:11pt; color:#000000;\">Are you new? Did you just know about ZelDrive? Please click </span><span style=\" font-size:11pt; font-weight:600; color:#000000;\">Register</span></p><p><span style=\" font-size:11pt; color:#000000;\">2. Do you have an existing ZelDrive account? Please click </span><span style=\" font-size:11pt; font-weight:600; color:#000000;\">Import Drive</span></p><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.reg_btn.setText(QtGui.QApplication.translate("zeld2_dnf", "Register", None, QtGui.QApplication.UnicodeUTF8))
        self.imp_btn.setText(QtGui.QApplication.translate("zeld2_dnf", "Import Drive", None, QtGui.QApplication.UnicodeUTF8))

    def launch_reg(self):
        import zeld2reg
        self.reg = zeld2reg.Ui_zeld2_reg()
        self.reg.show()

    def launch_imp_d(self):
        import zeld2_imp_d
        self.imp_d = zeld2_imp_d.Ui_zeld2_imp_d()
        self.imp_d.show()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    obj = Ui_zeld2_dnf()
    obj.show()
    sys.exit(app.exec_())
