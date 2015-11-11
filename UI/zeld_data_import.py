# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../zeld_data_import.ui'
#
# Created: Thu Feb 19 05:29:31 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import controller, db_access

class Ui_Zeld_Data_Import(QtGui.QMainWindow):

    def __init__(self):
        super(Ui_Zeld_Data_Import, self).__init__()

        self.setupUi(self)
        db_access.init()

    def setupUi(self, Zeld_Data_Import):
        Zeld_Data_Import.setObjectName("Zeld_Data_Import")
        Zeld_Data_Import.setWindowModality(QtCore.Qt.ApplicationModal)
        Zeld_Data_Import.resize(454, 352)
        Zeld_Data_Import.setMaximumSize(QtCore.QSize(454, 352))
        self.centralwidget = QtGui.QWidget(Zeld_Data_Import)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 401, 321))
        self.groupBox.setObjectName("groupBox")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 361, 51))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 46, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 61, 16))
        self.label_3.setObjectName("label_3")
        self.email_field = QtGui.QLineEdit(self.groupBox)
        self.email_field.setGeometry(QtCore.QRect(120, 120, 191, 20))
        self.email_field.setObjectName("email_field")
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 81, 16))
        self.label_4.setObjectName("label_4")
        self.password_field = QtGui.QLineEdit(self.groupBox)
        self.password_field.setGeometry(QtCore.QRect(120, 150, 191, 20))
        self.password_field.setObjectName("password_field")
        self.import_data_btn = QtGui.QPushButton(self.groupBox)
        self.import_data_btn.setGeometry(QtCore.QRect(120, 200, 75, 23))
        self.import_data_btn.setObjectName("import_data_btn")
        self.import_progress_field = QtGui.QLabel(self.groupBox)
        self.import_progress_field.setGeometry(QtCore.QRect(120, 240, 71, 16))
        self.import_progress_field.setObjectName("import_progress_field")
        Zeld_Data_Import.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Zeld_Data_Import)
        self.statusbar.setObjectName("statusbar")
        Zeld_Data_Import.setStatusBar(self.statusbar)

        self.retranslateUi(Zeld_Data_Import)
        QtCore.QMetaObject.connectSlotsByName(Zeld_Data_Import)

    def retranslateUi(self, Zeld_Data_Import):
        Zeld_Data_Import.setWindowTitle(QtGui.QApplication.translate("Zeld_Data_Import", "Data Import", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Zeld_Data_Import", "Data Import", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Zeld_Data_Import", "Data importing process clears your cache.\n"
"When you reload your account\'s data, the cache will be recreated afresh\n"
"Be careful", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Zeld_Data_Import", "Tip:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Zeld_Data_Import", "Your Email :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Zeld_Data_Import", "Your Password :", None, QtGui.QApplication.UnicodeUTF8))
        self.import_data_btn.setText(QtGui.QApplication.translate("Zeld_Data_Import", "Import Data", None, QtGui.QApplication.UnicodeUTF8))
        self.import_progress_field.setText(QtGui.QApplication.translate("Zeld_Data_Import", "Progress shown here", None, QtGui.QApplication.UnicodeUTF8))

        self.import_data_btn.clicked.connect(lambda: self.imp_usr_data())


    def imp_usr_data(self):
        email = self.email_field.text()
        password = self.password_field.text()
        if not db_access.user_exists(email, password):
            self.import_progress_field.setText("That account doesn't exist")
            return

        self.import_progress_field.setText("Enquiring about account ..")
        root = db_access.get_root(email)
        self.import_progress_field.setText("Importing ..")
        res = controller.import_data(root)
        if res == "0x0":
            self.import_progress_field.setText("Data import successful")
            space = db_access.get_space(email)
            controller.set_space(space)
        else:
            self.import_progress_field.setText("Data import failed. Check <font><ol>"
                                               "<li>your internet connection<li><li>that the drive is started</li>"
                                               "</ol></font>")