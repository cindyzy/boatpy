# -*- coding: utf-8 -*-

"""
Module implementing kh.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from .Ui_kh import Ui_kh


class kh(QMainWindow, Ui_kh):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(kh, self).__init__(parent)
        self.setupUi(self)
