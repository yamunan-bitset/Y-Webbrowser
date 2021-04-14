#!/usr/bin/python3

from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtWebEngineWidgets import * 
from PyQt5.QtPrintSupport import * 
import os
import sys

from window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Web Browser")
    window = MainWindow()
    app.exec_()
