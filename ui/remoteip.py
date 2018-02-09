# -*- coding: utf-8 -*-

"""
Module implementing remoteip.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_remoteip import Ui_remoteip


class remoteip(QDialog, Ui_remoteip):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(remoteip, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_buttonBox_accepted(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
