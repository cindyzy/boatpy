# -*- coding: utf-8 -*-

"""
Module implementing jiance.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Ui_jiance import Ui_jiance


class jiance(QDialog, Ui_jiance):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(jiance, self).__init__(parent)
        self.setupUi(self)
