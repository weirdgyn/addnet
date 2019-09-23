#!/usr/bin/env python

# AddNet for pcbnew
# This is the action plugin interface
# (c) Michele Santucci 2019
#

import wx
import os

from pcbnew import ActionPlugin, GetBoard
from addnet.addnet_dialog import InitAddNetDialog

__version__ = "0.1"

class AddNetPlugin(ActionPlugin):
    """Class that gathers the actionplugin stuff"""
    def defaults(self):
        self.name = "AddNet"
        self.category = "Modify PCB"
        self.description = "Add a Net to a PCB"
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'addnet.png')

    def Run(self):
        InitAddNetDialog(GetBoard())
