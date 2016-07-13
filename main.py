# -*- coding: utf-8 -*-
'''
    script.matchcenter - Football information for Kodi
    A program addon that can be mapped to a key on your remote to display football information.
    Livescores, Event details, Line-ups, League tables, next and previous matches by team. Follow what
    others are saying about the match in twitter.
    Copyright (C) 2016 enen92

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import thesportsdb
import xbmcgui
import xbmc
import sys
from resources.lib import livescores
from resources.lib import leaguetables
from resources.lib import eventdetails
from resources.lib import mainmenu
from resources.lib import ignoreleagues
from resources.lib.utilities import keymapeditor
from resources.lib.utilities.common_addon import *
 
def get_params():
    pairsofparams = []
    if len(sys.argv) >= 2:
        params=sys.argv[1]
        pairsofparams=params.split('/')
        pairsofparams = [parm for parm in pairsofparams if parm]
    return pairsofparams

params=get_params()

if not params:
    mainmenu.start()
else:
    if params[0] == 'ignoreleagues':
        ignoreleagues.start()
    elif params[0] == 'keymapeditor':
        keymapeditor.run()


try: xbmcplugin.endOfDirectory(int(sys.argv[1]))
except: sys.exit(0)

