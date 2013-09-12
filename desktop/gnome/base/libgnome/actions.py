#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("libgnome/", "DG_DISABLE_DEPRECATED", filePattern = "Makefile\.(am|in)", deleteLine = True)
    autotools.autoreconf("-fiv")
    autotools.configure("--disable-static \
                         --disable-schemas-install \
                         --disable-esd")
    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("NEWS", "README", "ChangeLog", "AUTHORS")
