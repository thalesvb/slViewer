'''
Created on 30/06/2015

@author: thales
'''

import wx

from custom_widgets.AbapCodeEditor import AbapCodeEditor
from screen.template.SapGuiForm import SapGuiForm


class ShowProgramForm(SapGuiForm):
    '''
    classdocs
    '''

    def createControls(self):

        self.programLabel = wx.StaticText(self, label=_("Report"))
        self.programTextCtrl = wx.TextCtrl(self)

        self.sourceTextCtrl = AbapCodeEditor(self)

    def bindEvents(self):

        pass

    def doLayout(self):

        boxSizer = wx.BoxSizer(orient=wx.VERTICAL)

        for control, options in \
                [(self.programLabel, {}),
                 (self.programTextCtrl, {}),
                 (self.sourceTextCtrl, {'proportion': 1, 'flag': wx.EXPAND})]:
            boxSizer.Add(control, **options)

        self.SetSizerAndFit(boxSizer)

    def fillInitialData(self, AbapObject):

        self.programTextCtrl.SetValue(AbapObject.name)
        self.sourceTextCtrl.SetText(AbapObject.source_code.source_code)
