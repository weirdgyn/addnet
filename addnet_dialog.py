#!/usr/bin/env python

# AddNet for pcbnew 
# This is the plugin WX dialog
# (c) Michele Santucci 2019
#

import wx
import pcbnew

from addnet_gui import addnet_gui

__version__ = "0.1"

class AddNetDialog(addnet_gui):
    """Class that gathers all the Gui control"""

    def __init__(self, board):
        """Init the brand new instance"""
        super(AddNetDialog, self).__init__(None)
        self.board = pcbnew.GetBoard()
        modules = board.GetModules()
        for mod in modules:
            self.m_cbComponent.Append(mod.GetReference())

        self.SetTitle("AddNet (v{0})".format(__version__))
        self.Bind(wx.EVT_CLOSE, self.onCloseWindow)
        self.m_cbComponent.Bind(wx.EVT_COMBOBOX, self.onComponentSelect)
        self.m_btnCancel.Bind(wx.EVT_BUTTON, self.onCloseWindow)
        self.m_btnOk.Bind(wx.EVT_BUTTON, self.onProcessAction)

    def onProcessAction(self, event):
        """Executes the requested action"""
        self.Destroy()

    def onCloseWindow(self, event):
        self.Destroy()

    def onComponentSelect(self, event):
        modules = self.board.GetModules()
        for mod in modules:
            if mod.GetReference() == self.m_cbComponent.GetStringSelection():
                for pad in mod.Pads():
                    self.m_cbPad.Append("1")
                break


def InitAddNetDialog(board):
    """Launch the dialog"""
    dlg = AddNetDialog(board)
    dlg.Show(True)
    return dlg
