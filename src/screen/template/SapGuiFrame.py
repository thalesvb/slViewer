'''
Created on 17/06/2015

@author: thales
'''

import wx
from screen.easy_access.EasyAccessForm import EasyAccessForm


class SapGuiFrame(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(SapGuiFrame, self).__init__(*args, **kwargs)
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.createToolBar()
        self.__currentForm = EasyAccessForm(self)
        self.layout()

        self.__stackLoadedForms = []

    def createToolBar(self):
        '''The toolbar here must be created using panels (ref: http://zetcode.com/wxpython/skeletons/ , Firefox skeleton)'''
        tb = wx.Panel(self, -1)
        tb_ico_size = wx.Size(24, 24)
        self.toolBar = tb
        # Buttons declaration
        continueButton = wx.Button(tb, label=_("Enter"))
        continueButton.Enable(enable=False)

        command = wx.ComboBox(tb)
        command.Enable(enable=False)

        saveButton = wx.BitmapButton(tb, bitmap=wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR, size=tb_ico_size))
        saveButton.SetToolTip(wx.ToolTip(_("Save")))
        saveButton.Enable(enable=False)
        # TODO: Separator

        self.backButton = wx.BitmapButton(tb, bitmap=wx.ArtProvider.GetBitmap(wx.ART_GO_BACK, wx.ART_TOOLBAR, size=tb_ico_size))
        self.backButton.SetToolTip(wx.ToolTip(_("Back")))
        self.backButton.Enable(enable=False)
        self.Bind(wx.EVT_BUTTON, self.onToolBarBackButton, self.backButton)

        endButton = wx.BitmapButton(tb, bitmap=wx.ArtProvider.GetBitmap(wx.ART_GO_TO_PARENT, wx.ART_TOOLBAR, size=tb_ico_size))
        endButton.SetToolTip(wx.ToolTip(_("Exit")))
        endButton.Enable(enable=False)

        cancelButton = wx.BitmapButton(tb, bitmap=wx.ArtProvider.GetBitmap(wx.ART_ERROR, wx.ART_TOOLBAR, size=tb_ico_size))
        cancelButton.SetToolTip(wx.ToolTip(_("Cancel")))
        cancelButton.Enable(enable=False)

        # TODO: Separator
        printButton = wx.BitmapButton(tb, bitmap=wx.ArtProvider.GetBitmap(wx.ART_PRINT, wx.ART_TOOLBAR, size=tb_ico_size))
        printButton.SetToolTip(wx.ToolTip(_("Print")))
        printButton.Enable(enable=False)

        findButton = wx.BitmapButton(tb, bitmap=wx.ArtProvider.GetBitmap(wx.ART_FIND, wx.ART_TOOLBAR, size=tb_ico_size))
        findButton.SetToolTip(wx.ToolTip(_("Find")))
        findButton.Enable(enable=False)

        findAgainButton = wx.BitmapButton(tb, bitmap=wx.ArtProvider.GetBitmap(wx.ART_FIND_AND_REPLACE, wx.ART_TOOLBAR, size=tb_ico_size))
        findAgainButton.SetToolTip(wx.ToolTip(_("Find next")))
        findAgainButton.Enable(enable=False)

        # Include buttons in boxsizer
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(continueButton)
        hbox.Add(command, 1, wx.TOP, 4)
        hbox.Add(saveButton)
        hbox.Add(self.backButton)
        hbox.Add(endButton)
        hbox.Add(cancelButton)
        hbox.Add(printButton)
        hbox.Add(findButton)
        hbox.Add(findAgainButton)

        tb.SetSizer(hbox)

    def layout(self):
        self.vbox.Add(self.toolBar, proportion=0, flag=wx.EXPAND)
        self.vbox.Add(window=self.__currentForm, proportion=1, flag=wx.EXPAND)
        self.SetSizerAndFit(self.vbox)
        self.Layout()

    def switchView(self, View):
        self.vbox.Clear()
        self.vbox.Add(window=self.toolBar, proportion=0, flag=wx.EXPAND)
        self.vbox.Add(window=View, proportion=1, flag=wx.EXPAND | wx.GROW)
        self.SetSizerAndFit(self.vbox)
        self.Layout()
        self.__stackLoadedForms.append(View)

    def loadNewView(self, View):
        self.vbox.Replace(oldwin=self.__currentForm,
                          newwin=View,
                          recursive=False)
        self.__stackLoadedForms.append(self.__currentForm)
        self.__currentForm.Hide()
        self.__currentForm = View
        self.backButton.Enable(enable=True)
        self.Layout()

    def onToolBarBackButton(self, event):
        viewPoped = self.__stackLoadedForms.pop()
        if len(self.__stackLoadedForms) == 0:
            self.backButton.Enable(enable=False)
        self.vbox.Replace(oldwin=self.__currentForm,
                          newwin=viewPoped,
                          recursive=False)
        self.__currentForm.Hide()
        self.__currentForm = viewPoped
        self.__currentForm.createMenu()
        self.__currentForm.Show()
        self.Layout()
