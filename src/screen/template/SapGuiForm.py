'''
Created on 17/06/2015

@author: thales
'''
import wx


class SapGuiForm(wx.Panel):

    def __init__(self, *args, **kwargs):
        super(SapGuiForm, self).__init__(*args, **kwargs)
        self.createControls()
        self.bindEvents()
        self.doLayout()

    def createControls(self):
        raise NotImplementedError

    def bindEvents(self):
        raise NotImplementedError

    def doLayout(self):
        raise NotImplementedError

    def createMenu(self):
        pass

    def fillInitialData(self, AbapObject):
        pass
