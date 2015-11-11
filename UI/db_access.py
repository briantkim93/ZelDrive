__author__ = 'bkim'

import MySQLdb as mysql
import hashlib

cursor, db = None, None


def init():
    global cursor
    global db
    db = mysql.connect("localhost", "root", "")
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS zeldrive_db")
    db = mysql.connect("localhost", "root", "", "zeldrive_db")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS zeldrive_comm (id INT(255) NOT NULL AUTO_INCREMENT PRIMARY KEY,"
                   "_email VARCHAR(255) NOT NULL, _pass VARCHAR(255) NOT NULL, _root VARCHAR(255) NOT NULL,"
                   " _names VARCHAR(255), _space BIGINT NOT NULL)")


def close():
    db.close()


def add_user(names, email, password, root):
    global cursor
    sha_meth = hashlib.sha512(password)
    hashpass = sha_meth.hexdigest()
    space = 1024 * 1024 * 1024 * 50
    print "adding to db now"

    try:
        cursor.execute("INSERT INTO zeldrive_comm(_email, _pass, _space, _root, _names)"
                       "VALUES ('%s','%s','%ld','%s','%s')"
                       % (email, hashpass, space, root, names))
        db.commit()

    except mysql.Error, e:
        print "error occured during insert %s " % e.message
        db.rollback()

    print "finished adding into db"


def user_exists(email, password):
    global cursor
    password = hashlib.sha512(password)
    cursor.execute("SELECT * FROM zeldrive_comm WHERE _email = '%s' AND _pass = '%s' " % (email, password))
    res = cursor.fetchall()
    if len(res) == 0:
        return False

    return True


def email_exists(email):
    global cursor
    cursor.execute("SELECT * FROM zeldrive_comm WHERE _email = '%s' " % email)
    res = cursor.fetchall()

    if len(res) == 0:
        return False

    return True


def get_root(email):
    global cursor
    cursor.execute("SELECT _root FROM zeldrive_comm WHERE _email = '%s' " % email)
    res = cursor.fetchone()
    return res[0]

def get_pass(email):
    global cursor
    cursor.execute("SELECT _pass FROM zeldrive_comm WHERE _email = '%s' " % email)
    res = cursor.fetchone()
    return res[0]

def get_space(email):
    global cursor
    cursor.execute("SELECT _space FROM zeldrive_comm WHERE _email = '%s'" % email)
    res = cursor.fetchone()
    return res[0]


def set_space(email, space):
    global cursor
    cursor.execute("UPDATE zeldrive_comm SET _space = %ld WHERE _email = '%s' " % (space, email))






