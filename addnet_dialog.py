#!/usr/bin/env python

# AddNet for pcbnew 
# This is the plugin WX dialog
# (c) Michele Santucci 2019
#

import wx

from addnet.addnet_gui import addnet_gui
from addnet.addnet_plugin import __version__

class AddNetDialog(addnet_gui):
    """Class that gathers all the Gui control"""

    def __init__(self, board):
        """Init the brand new instance"""
        super(AddNetDialog, self).__init__(None)
        self.board = board
        self.SetTitle("AddNet (v{0})".format(__version__))
        self.Bind(wx.EVT_CLOSE, self.onCloseWindow)
        self.m_btnCancel.Bind(wx.EVT_BUTTON, self.onCloseWindow)
        self.m_btnOk.Bind(wx.EVT_BUTTON, self.onProcessAction)

    def onProcessAction(self, event):
        """Executes the requested action"""
        self.Destroy()

    def onCloseWindow(self, event):
        self.Destroy()


def InitAddNetDialog(board):
    """Launch the dialog"""
    dlg = AddNetDialog(board)
    dlg.Show(True)
    return dlg
