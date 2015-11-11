__author__ = 'Kim'

import socket, sys
from PySide import QtGui

import zeld_data_not_found as zdnf
import zeld_drive_letter as zdl

sock = socket.socket()


sock.bind(("127.0.0.1", 12208))

sock.listen(2)

app = QtGui.QApplication(sys.argv)

while True:
    c, addr = sock.accept()
    print addr
    cmd = c.recv(4)

    cmd = int(cmd)

    # import or register distress
    if cmd == 0xff0 or cmd == 0xff1:
        obj = zdnf.Ui_Imp_Reg_Dialog()
        obj.show()
        app.exec_()
        print "sending back success bit"
        c.send("0x1")

    # drive letter distress
    elif cmd == 0xff2:
        obj = zdl.Ui_Zeld_drive_letter()
        obj.show()
        app.exec_()
        c.send("0x1")