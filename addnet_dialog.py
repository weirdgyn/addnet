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
        self.modules = self.board.GetModules()
        self.SetTitle("AddNet (v{0})".format(__version__))
        self.Bind(wx.EVT_CLOSE, self.onCloseWindow)
        self.SelectedPad = None
        self.SelectedModule = None
        self.m_cbModule.Bind(wx.EVT_COMBOBOX, self.onModuleSelect)
        self.m_cbPad.Bind(wx.EVT_COMBOBOX, self.onPadSelect)
        self.m_btnCancel.Bind(wx.EVT_BUTTON, self.onCloseWindow)
        self.m_btnOk.Bind(wx.EVT_BUTTON, self.onProcessAction)
        self.PopulateModules()

    def onProcessAction(self, event):
        self.AddNet()

    def onCloseWindow(self, event):
        self.Destroy()

    def onModuleSelect(self, event):
        self.PopulatePads()

    def onPadSelect(self, event):
        self.SelectPad()

    def SelectPad(self):
        if not self.SelectedModule == None:
            pads = self.SelectedModule.Pads()
            for pad in pads:
                if pad.GetName() == self.m_cbPad.GetStringSelection():
                    self.SelectedPad = pad
                    self.m_txtPadNet.ChangeValue(pad.GetNetname())
                    break
        else:
            self.SelectedPad = None       

    def PopulatePads(self):
        self.m_cbPad.Clear()
        self.m_txtPadNet.Clear()
        self.SelectedModule = None
        self.SelectedPad = None
        for mod in self.modules:
            if mod.GetReference() == self.m_cbModule.GetStringSelection():
                self.SelectedModule = mod
                pads = mod.Pads()
                for pad in pads:
                    pad_name = pad.GetName()
                    if pad_name != "" and pad_name != None:
                        self.m_cbPad.Append(pad_name)
                if not self.m_cbPad.IsEmpty():
                    self.m_cbPad.SetSelection(0)
                    self.SelectPad()
                break

    def PopulateModules(self):
        for mod in self.modules:
            self.m_cbModule.Append(mod.GetReference())
        if not self.m_cbModule.IsEmpty():
            self.m_cbModule.SetSelection(0)
        self.PopulatePads()

    def AddNet(self):
        netname = self.m_txtNetName.GetLineText(0)
        if netname == "":
            wx.MessageBox("Please set a netname")
            return
        if self.SelectedModule == None or self.SelectedPad == None:
            wx.MessageBox("Please select a module and a pad")
            return
        netcode = -1
        for mod in self.modules:
            pads = mod.Pads()
            for pad in pads:
                net = pad.GetNet()
                nc = net.GetNet()
                if nc > netcode:
                    netcode = nc
        netcode += 1
        newnet = pcbnew.NETINFO_ITEM(self.board, netname, netcode)
        self.SelectedPad.SetNet(newnet)
        #self.SelectedPad.SetNetCode(netcode)
        wx.MessageBox("Net %s:%d have been set to: %s->%s" % (netname, netcode, self.SelectedModule.GetReference(), self.SelectedPad.GetName()))
        #Todo: save/reload board?
        self.Destroy()

def InitAddNetDialog(board):
    """Launch the dialog"""
    dlg = AddNetDialog(board)
    dlg.Show(True)
    return dlg
