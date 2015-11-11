# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../zeld_registration.ui'
#
# Created: Thu Feb 19 05:30:33 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import controller, db_access, time, hashlib


class Ui_Zeld_Register(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_Zeld_Register, self).__init__()
        self.setupUi(self)

        db_access.init()

    def setupUi(self, Zeld_Register):
        Zeld_Register.setObjectName("Zeld_Register")
        Zeld_Register.setWindowModality(QtCore.Qt.ApplicationModal)
        Zeld_Register.resize(500, 500)
        Zeld_Register.setMaximumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtGui.QWidget(Zeld_Register)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 30, 441, 421))
        self.groupBox.setObjectName("groupBox")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 60, 46, 13))
        self.label.setObjectName("label")
        self.names_field = QtGui.QLineEdit(self.groupBox)
        self.names_field.setGeometry(QtCore.QRect(120, 60, 261, 31))
        self.names_field.setObjectName("names_field")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 61, 16))
        self.label_2.setObjectName("label_2")
        self.email_field = QtGui.QLineEdit(self.groupBox)
        self.email_field.setGeometry(QtCore.QRect(120, 120, 261, 31))
        self.email_field.setObjectName("email_field")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 51, 16))
        self.label_3.setObjectName("label_3")
        self.password_field = QtGui.QLineEdit(self.groupBox)
        self.password_field.setGeometry(QtCore.QRect(120, 180, 261, 31))
        self.password_field.setObjectName("password_field")
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 240, 101, 16))
        self.label_4.setObjectName("label_4")
        self.cpassword_field = QtGui.QLineEdit(self.groupBox)
        self.cpassword_field.setGeometry(QtCore.QRect(120, 240, 261, 31))
        self.cpassword_field.setObjectName("cpassword_field")
        self.join_btn = QtGui.QPushButton(self.groupBox)
        self.join_btn.setGeometry(QtCore.QRect(120, 300, 111, 31))
        self.join_btn.setObjectName("join_btn")
        self.results_pane = QtGui.QLabel(self.groupBox)
        self.results_pane.setGeometry(QtCore.QRect(270, 310, 81, 16))
        self.results_pane.setObjectName("results_pane")
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(40, 390, 101, 16))
        self.label_5.setObjectName("label_5")
        Zeld_Register.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Zeld_Register)
        self.statusbar.setObjectName("statusbar")
        Zeld_Register.setStatusBar(self.statusbar)

        self.retranslateUi(Zeld_Register)
        QtCore.QMetaObject.connectSlotsByName(Zeld_Register)

    def retranslateUi(self, Zeld_Register):
        Zeld_Register.setWindowTitle(QtGui.QApplication.translate("Zeld_Register", "ZelDrive Registration", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Zeld_Register", "Welcome to ZelDrive", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Zeld_Register", "Names : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Zeld_Register", "Your Email : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Zeld_Register", "Password : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Zeld_Register", "Confirm Password :", None, QtGui.QApplication.UnicodeUTF8))
        self.join_btn.setText(QtGui.QApplication.translate("Zeld_Register", "Join ZelDrive", None, QtGui.QApplication.UnicodeUTF8))
        self.results_pane.setText(QtGui.QApplication.translate("Zeld_Register", "", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Zeld_Register", "Just Too Elegant", None, QtGui.QApplication.UnicodeUTF8))

        self.join_btn.clicked.connect(lambda: self.reg_user())


    def reg_user(self):
        names = self.names_field.text()
        email = self.email_field.text()
        pass1 = self.password_field.text()
        pass2 = self.cpassword_field.text()

        if len(str(names).strip()) == 0 or len(str(email).strip()) == 0 or len(str(pass1).strip()) == 0 or len(str(pass2).strip()) == 0:
            return

        if pass1 != pass2:
            self.results_pane.setText("Please make sure your passwords match")
            return

        self.results_pane.setText("Processing ..")

        res = db_access.email_exists(email)
        if res:
            self.results_pane.setText("Sorry that email already exist. Choose another one")
            return

        self.results_pane.setText("Setting up ..")
        space = 1024 * 1024 * 1024 * 40
        space = "%ld" % space
        _pass = hashlib.sha512(pass1)
        _pass = _pass.hexdigest()
        # controller.connect()
        controller.register_usr(email, _pass, str(space))
        # root = controller.get_rootdir()

        # print root

        self.results_pane.setText("Finishing ..")
        # db_access.add_user(names, email, pass1, root)
        self.results_pane.setText("Huge Success!")
        print "Huge success"
        time.sleep(1)
        self.close()

    def __del__(self):
        db_access.close()
