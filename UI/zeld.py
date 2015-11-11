# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../zeld.ui'
#
# Created: Thu Feb 19 05:28:17 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import sys, controller

import zeld_about, zeld_data_import, zeld_data_not_found, zeld_registration, zeld_settings, zeld_drive_letter
import db_access


class Ui_ZelDrive(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_ZelDrive, self).__init__()

        self.setupUi(self)
        self.load_info()

    def setupUi(self, ZelDrive):

        ZelDrive.setObjectName("ZelDrive")
        ZelDrive.setEnabled(True)
        ZelDrive.resize(529, 422)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ZelDrive.sizePolicy().hasHeightForWidth())
        ZelDrive.setSizePolicy(sizePolicy)
        ZelDrive.setMaximumSize(QtCore.QSize(529, 422))
        self.centralwidget = QtGui.QWidget(ZelDrive)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(100, 20, 291, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.label_4)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.label_6)
        self.label_8 = QtGui.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtGui.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.label_9)
        self.formLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(100, 140, 291, 81))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_3 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.progressBar = QtGui.QProgressBar(self.formLayoutWidget_2)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.progressBar)
        self.label_7 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.refresh_btn = QtGui.QPushButton(self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(410, 20, 51, 23))
        self.refresh_btn.setObjectName("refresh_btn")
        ZelDrive.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(ZelDrive)
        self.statusbar.setObjectName("statusbar")
        ZelDrive.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(ZelDrive)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuData = QtGui.QMenu(self.menubar)
        self.menuData.setObjectName("menuData")
        ZelDrive.setMenuBar(self.menubar)
        self.actionFAQs = QtGui.QAction(ZelDrive)
        self.actionFAQs.setObjectName("actionFAQs")
        self.actionAbout_ZelDrive = QtGui.QAction(ZelDrive)
        self.actionAbout_ZelDrive.setObjectName("actionAbout_ZelDrive")
        self.actionPurchase_Space = QtGui.QAction(ZelDrive)
        self.actionPurchase_Space.setObjectName("actionPurchase_Space")
        self.actionSettings = QtGui.QAction(ZelDrive)
        self.actionSettings.setObjectName("actionSettings")
        self.actionImport_Data = QtGui.QAction(ZelDrive)
        self.actionImport_Data.setObjectName("actionImport_Data")
        self.actionExit = QtGui.QAction(ZelDrive)
        self.actionExit.setObjectName("actionExit")
        self.actionWhat_s_ZelDrive = QtGui.QAction(ZelDrive)
        self.actionWhat_s_ZelDrive.setObjectName("actionWhat_s_ZelDrive")
        self.actionCheck_for_updates = QtGui.QAction(ZelDrive)
        self.actionCheck_for_updates.setObjectName("actionCheck_for_updates")
        self.actionTerms_and_Conditions = QtGui.QAction(ZelDrive)
        self.actionTerms_and_Conditions.setObjectName("actionTerms_and_Conditions")
        self.actionSet_drive_Letter = QtGui.QAction(ZelDrive)
        self.actionSet_drive_Letter.setObjectName("actionSet_drive_letter")
        self.menuHelp.addAction(self.actionWhat_s_ZelDrive)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionPurchase_Space)
        self.menuHelp.addAction(self.actionCheck_for_updates)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionFAQs)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionTerms_and_Conditions)
        self.menuHelp.addAction(self.actionAbout_ZelDrive)
        self.menuSettings.addAction(self.actionSettings)
        self.menuSettings.addAction(self.actionSet_drive_Letter)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionExit)
        self.menuData.addAction(self.actionImport_Data)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(ZelDrive)
        QtCore.QMetaObject.connectSlotsByName(ZelDrive)

    def retranslateUi(self, ZelDrive):
        ZelDrive.setWindowTitle(QtGui.QApplication.translate("ZelDrive", "ZelDrive Control Panel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ZelDrive", "Total Space : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ZelDrive", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ZelDrive", "Used Space :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ZelDrive", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ZelDrive", "Free Space  :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ZelDrive", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ZelDrive", "User  : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ZelDrive", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ZelDrive", "Disk Usage : ", None, QtGui.QApplication.UnicodeUTF8))
        self.refresh_btn.setText(QtGui.QApplication.translate("ZelDrive", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("ZelDrive", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate("ZelDrive", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menuData.setTitle(QtGui.QApplication.translate("ZelDrive", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFAQs.setText(QtGui.QApplication.translate("ZelDrive", "FAQs", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_ZelDrive.setText(QtGui.QApplication.translate("ZelDrive", "About ZelDrive", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPurchase_Space.setText(QtGui.QApplication.translate("ZelDrive", "Purchase Space", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("ZelDrive", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport_Data.setText(QtGui.QApplication.translate("ZelDrive", "Import Data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("ZelDrive", "Exit ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionWhat_s_ZelDrive.setText(QtGui.QApplication.translate("ZelDrive", "What\'s ZelDrive?", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCheck_for_updates.setText(QtGui.QApplication.translate("ZelDrive", "Check for updates", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTerms_and_Conditions.setText(QtGui.QApplication.translate("ZelDrive", "Terms and Conditions", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSet_drive_Letter.setText(QtGui.QApplication.translate("ZelDrive", "Choose Drive Letter", None, QtGui.QApplication.UnicodeUTF8))

        self.refresh_btn.clicked.connect(lambda: self.load_info())
        self.actionImport_Data.triggered.connect(lambda: self.launch_import_data())
        self.actionAbout_ZelDrive.triggered.connect(lambda: self.launch_about())
        self.actionSettings.triggered.connect(lambda: self.launch_settings())
        self.actionSet_drive_Letter.triggered.connect(lambda: self.launch_drive_letter())

    def launch_data_not_found(self):
        self.dnf = zeld_data_not_found.Ui_Imp_Reg_Dialog()
        self.dnf.show()

    def launch_about(self):
        self.about = zeld_about.Ui_Zeld_About()
        self.about.show()

    def launch_settings(self):
        self.settings = zeld_settings.Ui_SettingsPanel()
        self.settings.show()

    def launch_register(self):
        self.reg = zeld_registration.Ui_Zeld_Register()
        self.reg.show()

    def launch_import_data(self):
        self.imp = zeld_data_import.Ui_Zeld_Data_Import()
        self.imp.show()

    def launch_drive_letter(self):
        self.driveletter = zeld_drive_letter.Ui_Zeld_drive_letter()
        self.driveletter.show()

    def load_info(self):
        """controller.connect()
        user_exists = -1
        user_exists = controller.main()

        if user_exists == -1:
            self.launch_data_not_found()
            self.hide()
            self.close()
        else:
            info, res = controller.read_user_info()
            self.label_2.setText(info.space)
            self.label_4.setText(info.used_space)
            self.label_6.setText(info.available_space)
            self.label_9.setText(info.email)
            self.progressBar.setProperty("value", (info.used_space / info.space) * 100)"""
        pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    print "Launching ZelDrive GUI in a few .."
    obj = Ui_ZelDrive()
    obj.show()
    sys.exit(app.exec_())
