# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zeld_main.ui'
#
# Created: Sat Jul 25 10:33:33 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui, QtWebKit

class Ui_zeld_main(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_zeld_main, self).__init__()
        self.setupUi(self)

    def setupUi(self, zeld_main):
        zeld_main.setObjectName("zeld_main")
        zeld_main.resize(800, 600)
        self.centralwidget = QtGui.QWidget(zeld_main)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.centralwidget.setAutoFillBackground(True)
        p = self.centralwidget.palette()
        p.setColor(self.centralwidget.backgroundRole(), QtCore.Qt.darkMagenta)
        self.centralwidget.setPalette(p)

        self.webform = QtWebKit.QWebView(self.centralwidget)
        self.webform.setGeometry(QtCore.QRect(0, 0, 800, 21))

        self.gridLayout.addWidget(self.webform, 0, 0, 1, 1)

        zeld_main.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(zeld_main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        zeld_main.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(zeld_main)
        self.statusbar.setObjectName("statusbar")
        zeld_main.setStatusBar(self.statusbar)
        self.actionSettings = QtGui.QAction(zeld_main)
        self.actionSettings.setObjectName("actionSettings")
        self.actionRegister = QtGui.QAction(zeld_main)
        self.actionRegister.setObjectName("actionRegister")
        self.actionImport_Drive = QtGui.QAction(zeld_main)
        self.actionImport_Drive.setObjectName("actionImport_Drive")
        self.actionExit = QtGui.QAction(zeld_main)
        self.actionExit.setObjectName("actionExit")
        self.actionSettings_2 = QtGui.QAction(zeld_main)
        self.actionSettings_2.setObjectName("actionSettings_2")
        self.actionWhat_s_ZelDrive = QtGui.QAction(zeld_main)
        self.actionWhat_s_ZelDrive.setObjectName("actionWhat_s_ZelDrive")
        self.actionPurchase_Space = QtGui.QAction(zeld_main)
        self.actionPurchase_Space.setObjectName("actionPurchase_Space")
        self.actionCheck_for_updates = QtGui.QAction(zeld_main)
        self.actionCheck_for_updates.setObjectName("actionCheck_for_updates")
        self.actionFAQs = QtGui.QAction(zeld_main)
        self.actionFAQs.setObjectName("actionFAQs")
        self.actionTerms_and_Conditions = QtGui.QAction(zeld_main)
        self.actionTerms_and_Conditions.setObjectName("actionTerms_and_Conditions")
        self.actionAbout_ZelDrive = QtGui.QAction(zeld_main)
        self.actionAbout_ZelDrive.setObjectName("actionAbout_ZelDrive")
        self.menuFile.addAction(self.actionRegister)
        self.menuFile.addAction(self.actionImport_Drive)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuTools.addAction(self.actionSettings_2)
        self.menuHelp.addAction(self.actionWhat_s_ZelDrive)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionPurchase_Space)
        self.menuHelp.addAction(self.actionCheck_for_updates)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionFAQs)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionTerms_and_Conditions)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_ZelDrive)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(zeld_main)
        QtCore.QMetaObject.connectSlotsByName(zeld_main)

        self.webform.load("webform/reg.html")

        self.actionExit.triggered.connect(lambda: self.close())
        self.actionRegister.triggered.connect(self.load_reg_page)
        self.actionImport_Drive.triggered.connect(self.load_import_page)
        self.actionSettings_2.triggered.connect(self.load_settings_page)

    def retranslateUi(self, zeld_main):
        zeld_main.setWindowTitle(QtGui.QApplication.translate("zeld_main", "ZelDrive Panel", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("zeld_main", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("zeld_main", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("zeld_main", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("zeld_main", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRegister.setText(QtGui.QApplication.translate("zeld_main", "Register to ZelDrive", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport_Drive.setText(QtGui.QApplication.translate("zeld_main", "Import Drive", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("zeld_main", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings_2.setText(QtGui.QApplication.translate("zeld_main", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWhat_s_ZelDrive.setText(QtGui.QApplication.translate("zeld_main", "What\'s ZelDrive", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPurchase_Space.setText(QtGui.QApplication.translate("zeld_main", "Purchase space", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCheck_for_updates.setText(QtGui.QApplication.translate("zeld_main", "Check for updates", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFAQs.setText(QtGui.QApplication.translate("zeld_main", "FAQs", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTerms_and_Conditions.setText(QtGui.QApplication.translate("zeld_main", "Terms and Conditions", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_ZelDrive.setText(QtGui.QApplication.translate("zeld_main", "About ZelDrive", None, QtGui.QApplication.UnicodeUTF8))

    def load_reg_page(self):
        self.webform.load("webform/reg.html")

    def load_import_page(self):
        self.webform.load("webform/import.html")

    def load_settings_page(self):
        self.webform.load("webform/settings.html")


import sys
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    obj = Ui_zeld_main()
    obj.show()
    sys.exit(app.exec_())