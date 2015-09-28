'''
Created on 25/09/2015

@author: thales
'''

import wx.dataview

from screen.template.SapGuiForm import SapGuiForm


class ShowMessageClassForm(SapGuiForm):
    '''
    classdocs
    '''

    def createControls(self):

        self.messageClassLabel = wx.StaticText(self, label=_("Message class"))
        self.messageClassTextCtrl = wx.TextCtrl(self)

        self.listCtrl = wx.dataview.DataViewListCtrl(self)
        self.listCtrl.AppendTextColumn(_("Language"))
        self.listCtrl.AppendTextColumn(_("Message number"))
        self.listCtrl.AppendTextColumn(_("Text"))

    def bindEvents(self):
        pass

    def doLayout(self):

        boxSizer = wx.BoxSizer(orient=wx.VERTICAL)
        for control, options in \
                [(self.messageClassLabel, {}),
                 (self.messageClassTextCtrl, {}),
                 (self.listCtrl, {'proportion': 1, 'flag': wx.EXPAND})]:
            boxSizer.Add(control, **options)

        self.SetSizerAndFit(boxSizer)

    def fillInitialData(self, AbapObject):

        self.messageClassTextCtrl.SetValue(AbapObject.name)

        for language in AbapObject.language_mapping.keys():
            for message in AbapObject.language_mapping[language].values():
                itemValues = [
                    message.language,
                    message.number,
                    message.text,
                ]
                self.listCtrl.AppendItem(values=itemValues)
