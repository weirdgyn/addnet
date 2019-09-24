# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import sys

###########################################################################
## Class addnet_gui
###########################################################################

class addnet_gui ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add Net", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )

		if sys.version_info[0] == 2:
			self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		else:
			self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bMainSizer = wx.BoxSizer( wx.VERTICAL )

		bHSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_lblNetName = wx.StaticText( self, wx.ID_ANY, u"Net name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lblNetName.Wrap( -1 )

		bHSizer1.Add( self.m_lblNetName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL, 5 )

		self.m_txtNetName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bHSizer1.Add( self.m_txtNetName, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )


		bMainSizer.Add( bHSizer1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		bHSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_lblModule = wx.StaticText( self, wx.ID_ANY, u"Module / pad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lblModule.Wrap( -1 )

		bHSizer3.Add( self.m_lblModule, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		m_cbModuleChoices = []
		self.m_cbModule = wx.ComboBox( self, wx.ID_ANY, u"--", wx.DefaultPosition, wx.DefaultSize, m_cbModuleChoices, wx.CB_DROPDOWN|wx.CB_READONLY )
		bHSizer3.Add( self.m_cbModule, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		m_cbPadChoices = []
		self.m_cbPad = wx.ComboBox( self, wx.ID_ANY, u"--", wx.DefaultPosition, wx.DefaultSize, m_cbPadChoices, wx.CB_DROPDOWN|wx.CB_READONLY )
		bHSizer3.Add( self.m_cbPad, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_txtPadNet = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bHSizer3.Add( self.m_txtPadNet, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )


		bMainSizer.Add( bHSizer3, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		bHSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_btnOk = wx.Button( self, wx.ID_ANY, u"&Ok", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_btnOk.SetDefault()
		bHSizer2.Add( self.m_btnOk, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_btnCancel = wx.Button( self, wx.ID_ANY, u"&Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bHSizer2.Add( self.m_btnCancel, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bMainSizer.Add( bHSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.SetFocus()
		self.m_txtNetName.SetFocus()

		self.SetSizer( bMainSizer )
		self.Layout()
		bMainSizer.Fit( self )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


