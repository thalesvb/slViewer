'''
Created on 17/06/2015

@author: thales
'''
import builtins
import sys
import os
import wx

from screen.template.SapGuiFrame import SapGuiFrame


if __name__ == '__main__':
    app = wx.App(0)

    # FIXME: Quick fix in wxLocale to work on windows when freezing app.
    lang_id = wx.LANGUAGE_DEFAULT
    locale = wx.Locale(lang_id)

    # Set definitions to use wxPython translation Services
    domain = "messages"
    basepath = os.path.abspath(os.path.dirname(sys.argv[0]))
    localedir = os.path.join(basepath, "locale")
    locale.AddCatalogLookupPathPrefix(localedir)
    locale.AddCatalog(domain)

    # Set '_' function to use wx.GetTranslation
    builtins.__dict__['_'] = wx.GetTranslation

    frame = SapGuiFrame(None, title=_("slViewer"))
    frame.Center()
    frame.Show()

    app.MainLoop()
