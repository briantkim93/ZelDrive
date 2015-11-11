__author__ = 'Kim'

'''
Available letters for mounting
'''

import win32api
import sqlite3


def get_letter_options():
    """
    This gets all the available letters that can be used
    to mount our filesystem
    :return: list of letters available for use
    """

    ascii = []
    used_ascii = []
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    for d in drives:
        used_ascii.append(d[0])

    for elem in range(0x41, 0x5b, 0x1):
        ascii.append(chr(elem))

    return reversed(list(set(ascii) - set(used_ascii)))


def save_letter_option(choice_letter):
    """
    Save the letter of choice by the use to mount
    :param choice_letter:
    :return: void
    """

    sql = "CREATE TABLE IF NOT EXISTS usrparam(email VARCHAR(255) NOT NULL, names VARCHAR(255) NOT NULL," \
          "password VARCHAR(255) NOT NULL, rootdir VARCHAR(255) NOT NULL," \
          "total_space UNSIGNED BIG INT NOT NULL, used_space UNSIGNED BIG INT NOT NULL," \
          "free_space UNSIGNED BIG INT NOT NULL, total_cache UNSIGNED BIG INT NOT NULL," \
          "used_cache UNSIGNED BIG INT NOT NULL, free_cache UNSIGNED BIG INT NOT NULL," \
          "thread_group INTEGER NOT NOT NULL, drive_letter BIGINT NOT NULL DEFAULT 0)"

    db = sqlite3.connect("sysparams.sys")
    db.execute(sql)
    db.execute("INSERT INTO usrparam (drive_letter) VALUES (?)", choice_letter)



def letter_is_set():
    """
    check if user has set a mount point letter
    :return: boolean
    """

    db = sqlite3.connect("sysparams.sys")
    cursor = db.execute("SELECT drive_letter FROM usrparam")
    row = cursor.fetchone()
    if len(row[0]) == 0:
        return False

    return True
