__author__ = 'Kim'

import py2exe, sys
from distutils.core import setup


sys.argv.append("py2exe")
setup(console=["zeld.py"])
