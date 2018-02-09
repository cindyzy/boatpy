# -*- coding: utf-8 -*-

"""
Module implementing picshow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Ui_picshow import Ui_picshow


class picshow(QDialog, Ui_picshow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(picshow, self).__init__(parent)
        self.setupUi(self)
