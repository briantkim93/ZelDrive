__author__ = 'kim'

import socket
import sqlite3

host = "127.0.0.1"
port = 12209

msg_path = "C:/Users/Kim/workspace/lservd32/Release/messages.db"



class UserInfo:
    def __init__(self, email, space, used_space, available_space):
        self.email = email
        self.space = space
        self.used_space = used_space
        self.available_space = available_space


def init():
    sock.send("1")
    base_case = sock.recv(3)
    sock.close()

    if base_case == "0xf":
        return -1
    else:
        return 0


def register_usr(email, _pass, space):

    dat = "%s\n%s\n%s" % (email, _pass, space)
    with open(msg_path, "w") as f:
        f.write(dat)

    r = socket.socket()
    r.connect((host, port))
    r.send("2")
    r.close()


def get_rootdir():
    r = socket.socket()
    r.connect((host, port))
    r.send("2")
    rootdir = r.recv(256)
    r.close()
    return rootdir


def import_data(root):
    with open(msg_path, "w") as f:
        f.write(root)

    r = socket.socket()
    r.connect((host, port))
    r.send("3")
    r.recv(3)
    r.close()


def set_cache_size(cache):
    with open(msg_path, "w") as f:
        f.write(cache)

    r = socket.socket()
    r.connect((host, port))
    r.send("4")
    r.recv(3)
    r.close()


def clear_cache():
    r = socket.socket()
    r.connect((host, port))
    r.send("5")
    r.recv(3)
    r.close()


def set_tgroup(tgroup):
    with open(msg_path, "w") as f:
        f.write(str(tgroup))

    r = socket.socket()
    r.connect((host, port))
    r.send("6")
    r.recv(3)
    r.close()

def set_space(space):
    with open(msg_path, "w") as f:
        f.write(str(space))

    r = socket.socket()
    r.connect((host, port))
    r.send("7")
    r.recv(3)
    r.close()


def set_drive_letter(letter):
    with open(msg_path, "w") as f:
        f.write(str(letter))

    r = socket.socket()
    r.connect((host, port))
    r.send("8")
    r.recv(3)
    r.close()


def read_cache():
    global sock
    sock.send("16")
    cache = sock.recv(20)
    cache = int(cache)
    sock.close()
    return cache


def read_tgroup():
    global sock
    sock.send("17")
    tgroup = sock.recv(5)
    tgroup = int(tgroup)
    sock.close()
    return tgroup


def read_user_info():
    global sock
    sock.send("18")
    email = sock.recv(256)
    tspace = int(sock.recv(20))
    tuspace = int(sock.recv(20))
    taspace = int(sock.recv(20))
    user = UserInfo(email, tspace, tuspace, taspace)
    sock.close()
    return user

def set_proxy_data(proxyhost, proxyport, username=None, pwd=None):
    proxystr = ""
    proxyhost = str(proxyhost)
    ip_fragments = proxyhost.split(".")

    if len(proxyhost) == 0 or len(proxyport) == 0 or len(ip_fragments) < 4:
        return False

    if username is not None:
        proxystr = username

    if pwd is not None:
        proxystr += ":" + pwd

    proxystr += "@" + proxyhost + ":" + proxyport

    dat = "%s" % proxystr
    with open(msg_path, "w") as f:
        f.write(dat)

    r = socket.socket()
    r.connect((host, port))
    r.send("19")
    r.close()