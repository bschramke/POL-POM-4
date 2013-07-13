#!/usr/bin/python
# -*- coding:Utf-8 -*-

# Copyright (C) 2008 Pâris Quentin
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.



import wx


from services.Environment import *
from services.ConfigService import *

from views.UIHelper import UIHelper


class Text(wx.StaticText):
    def __init__(self, panel, text = "", pos = (20,80), size = (480,275)):
        self.uiHelper = UIHelper()
        wx.StaticText.__init__(self, panel, -1, text, pos, size, style=wx.ST_NO_AUTORESIZE)