'''
Created on 17/06/2015

@author: thales
'''

import wx.dataview

from custom_widgets.AbapCodeEditor import AbapCodeEditor
from screen.template.SapGuiForm import SapGuiForm


class ShowFunctionForm(SapGuiForm):

    def createControls(self):
        self.functionLabel = wx.StaticText(self, label=_("Function module"))
        self.functionTextCtrl = wx.TextCtrl(self)

        self.notebook = wx.Notebook(self)
        self.nbCharacteristicsPage = self.NbCharacteristicsPage(self.notebook)
        self.notebook.AddPage(self.nbCharacteristicsPage, _("Properties"))
        self.nbImportingPage = self.NbImportingPage(self.notebook)
        self.notebook.AddPage(self.nbImportingPage, _("Import"))
        self.nbExportingPage = self.NbExportingPage(self.notebook)
        self.notebook.AddPage(self.nbExportingPage, _("Export"))
        self.nbChangingPage = self.NbChangingPage(self.notebook)
        self.notebook.AddPage(self.nbChangingPage, _("Changing"))
        self.nbTablesPage = self.NbTablesPage(self.notebook)
        self.notebook.AddPage(self.nbTablesPage, _("Tables"))
        self.nbExceptionsPage = self.NbExceptionsPage(self.notebook)
        self.notebook.AddPage(self.nbExceptionsPage, _("Exceptions"))
        self.nbSourceCodePage = self.NbSourceCodePage(self.notebook)
        self.notebook.AddPage(self.nbSourceCodePage, _("Source code"))

        self.createMenu()

    def bindEvents(self):
        pass

    def doLayout(self):
        boxSizer = wx.BoxSizer(orient=wx.VERTICAL)
        boxSizer.Add(self.functionLabel, 1, wx.ALL)
        boxSizer.Add(self.functionTextCtrl, 1, wx.ALL)
        boxSizer.Add(self.notebook, 1, wx.EXPAND)
        self.SetSizer(boxSizer)

    def createMenu(self):
        menuBar = wx.MenuBar()

        # Menu 'Go To'
        gotoMenu = wx.Menu()
        globalDataMenuItem = gotoMenu.Append(id=wx.NewId(), item=_("Global data"), helpString=_("Go to global data"))
        globalDataMenuItem.Enable(False)
        mainProgramMenuItem = gotoMenu.Append(id=wx.NewId(), item=_("Main program"), helpString=_("Go to main program"))
        mainProgramMenuItem.Enable(False)
        objectCatalogEntryMenuItem = gotoMenu.Append(id=wx.NewId(), item=_("Object Directory Entry"), helpString="")
        objectCatalogEntryMenuItem.Enable(False)
        documentationMenuItem = gotoMenu.Append(id=wx.NewId(), item=_("Documentation"), helpString="")
        documentationMenuItem.Enable(False)
        goBackMenuItem = gotoMenu.Append(id=wx.NewId(), item=_("Back"), helpString="")
        goBackMenuItem.Enable(False)
        menuBar.Append(gotoMenu, _("Goto"))

        # Menu 'Utilities'
        utilitiesMenu = wx.Menu()
        showObjectsListMenuItem = utilitiesMenu.Append(id=wx.NewId(), item=_("Display object list"), helpString="")
        showObjectsListMenuItem.Enable(False)
        whereUsageListMenuItem = utilitiesMenu.Append(id=wx.NewId(), item=_("Where-Used list"), helpString="")
        whereUsageListMenuItem.Enable(False)

        # Menu 'Utilities' - Submenu 'Other Utilities'
        otherUtilitiesSubMenu = wx.Menu()
        splitScreenMenuItem = otherUtilitiesSubMenu.Append(id=wx.NewId(), item=_("Splitscreen Editor"), helpString="")
        splitScreenMenuItem.Enable(False)
        downloadMenuItem = otherUtilitiesSubMenu.Append(id=wx.NewId(), item=_("Download"), helpString="")
        downloadMenuItem.Enable(False)
        utilitiesMenu.Append(wx.NewId(), item=_("More utilities"), subMenu=otherUtilitiesSubMenu)

        menuBar.Append(utilitiesMenu, _("Utilities"))

        self.GetParent().SetMenuBar(menuBar)

    class NbCharacteristicsPage(SapGuiForm):

        def createControls(self):

            # Classification
            self.functionGroupLabel = wx.StaticText(self, label=_("Function Group"))
            self.functionGroupTextCtrl = wx.TextCtrl(self)
            self.functionGroupDescriptionTextCtrl = wx.TextCtrl(self)
            self.functionDescriptionLabel = wx.StaticText(self, label=_("Short text"))
            self.functionDescriptionTextCtrl = wx.TextCtrl(self)

            # Process Type
            self.processTypeRadioBox = wx.RadioBox(self, choices=[_("Normal function module"), _("Remote-Enabled module"), _("Update module")])
            self.moduleUpdateRadioBox = wx.RadioBox(self, choices=[_("Start immediately"), _("Immediate start, no restart"), _("Start delayed"), _("Coll.run")])
            self.basXMLSupportedCheckBox = wx.CheckBox(self, label=_("basXML supported"))

            # General Data
            self.createdByLabel = wx.StaticText(self, label=_("Person responsible"))
            self.createdByTextCtrl = wx.TextCtrl(self)
            self.changedByLabel = wx.StaticText(self, label=_("Last changed by"))
            self.changedByTextCtrl = wx.TextCtrl(self)
            self.changedOnLabel = wx.StaticText(self, label=_("Changed on"))
            self.changedOnDateCtrl = wx.TextCtrl(self)
            self.packageLabel = wx.StaticText(self, label=_("Package"))
            self.packageTextCtrl = wx.TextCtrl(self)
            self.programNameLabel = wx.StaticText(self, label=_("Program name"))
            self.programNameTextCtrl = wx.TextCtrl(self)
            self.includeNameLabel = wx.StaticText(self, label=_("Include name"))
            self.includeNameTextCtrl = wx.TextCtrl(self)
            self.originalLanguageLabel = wx.StaticText(self, label=_("Original language"))
            self.originalLanguageTextCtrl = wx.TextCtrl(self)
            self.notReleasedLabel = wx.StaticText(self, label=_("Not released"))
            self.processBlockedCheckBox = wx.CheckBox(self, label=_("Edit lock"))
            self.globalCheckBox = wx.CheckBox(self, label=_("Global"))

        def bindEvents(self):
            pass

        def doLayout(self):

            boxSizer = wx.BoxSizer(orient=wx.VERTICAL)

            for control, options in \
                    [(self.functionGroupLabel, {}),
                     (self.functionGroupTextCtrl, {}),
                     (self.functionGroupDescriptionTextCtrl, {}),
                     (self.functionDescriptionLabel, {}),
                     (self.functionDescriptionTextCtrl, {}),

                     (self.processTypeRadioBox, {}),
                     (self.moduleUpdateRadioBox, {}),
                     (self.basXMLSupportedCheckBox, {}),

                     (self.createdByLabel, {}),
                     (self.createdByTextCtrl, {}),
                     (self.changedByLabel, {}),
                     (self.changedByTextCtrl, {}),
                     (self.changedOnLabel, {}),
                     (self.changedOnDateCtrl, {}),
                     (self.packageLabel, {}),
                     (self.packageTextCtrl, {}),
                     (self.programNameLabel, {}),
                     (self.programNameTextCtrl, {}),
                     (self.includeNameLabel, {}),
                     (self.includeNameTextCtrl, {}),
                     (self.originalLanguageLabel, {}),
                     (self.originalLanguageTextCtrl, {}),
                     (self.notReleasedLabel, {}),
                     (self.processBlockedCheckBox, {}),
                     (self.globalCheckBox, {})]:

                boxSizer.Add(control, **options)

            self.SetSizerAndFit(boxSizer)

    class NbImportingPage(SapGuiForm):

        def createControls(self):

            self.listCtrl = wx.dataview.DataViewListCtrl(self)
            self.listCtrl.AppendTextColumn(_("Parameter name"))
            self.listCtrl.AppendTextColumn(_("Typing"))
            self.listCtrl.AppendTextColumn(_("Associated type"))
            self.listCtrl.AppendTextColumn(_("Default value"))
            self.listCtrl.AppendToggleColumn(_("Optional"))
            self.listCtrl.AppendToggleColumn(_("Pass value"))
            self.listCtrl.AppendTextColumn(_("Short text"))
            self.listCtrl.AppendTextColumn(_("Long text"))

        def bindEvents(self):

            pass

        def doLayout(self):

            boxSizer = wx.BoxSizer(orient=wx.VERTICAL)

            for control, options in \
                    [(self.listCtrl, {'proportion': 1, 'flag': wx.EXPAND})]:
                boxSizer.Add(control, **options)

            self.SetSizerAndFit(boxSizer)

    class NbExportingPage(SapGuiForm):

        def createControls(self):

            self.listCtrl = wx.dataview.DataViewListCtrl(self)
            self.listCtrl.AppendTextColumn(_("Parameter name"))
            self.listCtrl.AppendTextColumn(_("Typing"))
            self.listCtrl.AppendTextColumn(_("Associated type"))
            self.listCtrl.AppendToggleColumn(_("Pass value"))
            self.listCtrl.AppendTextColumn(_("Short text"))
            self.listCtrl.AppendTextColumn(_("Long text"))

        def bindEvents(self):

            pass

        def doLayout(self):

            boxSizer = wx.BoxSizer(orient=wx.VERTICAL)

            for control, options in \
                    [(self.listCtrl, {'proportion': 1, 'flag': wx.EXPAND})]:
                boxSizer.Add(control, **options)

            self.SetSizerAndFit(boxSizer)

    class NbChangingPage(SapGuiForm):

        def createControls(self):

            self.listCtrl = wx.dataview.DataViewListCtrl(self)
            self.listCtrl.AppendTextColumn(_("Parameter name"))
            self.listCtrl.AppendTextColumn(_("Typing"))
            self.listCtrl.AppendTextColumn(_("Associated type"))
            self.listCtrl.AppendTextColumn(_("Default value"))
            self.listCtrl.AppendToggleColumn(_("Optional"))
            self.listCtrl.AppendToggleColumn(_("Pass value"))
            self.listCtrl.AppendTextColumn(_("Short text"))
            self.listCtrl.AppendTextColumn(_("Long text"))

        def bindEvents(self):

            pass

        def doLayout(self):

            boxSizer = wx.BoxSizer(orient=wx.VERTICAL)

            for control, options in \
                    [(self.listCtrl, {'proportion': 1, 'flag': wx.EXPAND})]:
                boxSizer.Add(control, **options)

            self.SetSizerAndFit(boxSizer)

    class NbTablesPage(SapGuiForm):

        def createControls(self):

            self.listCtrl = wx.dataview.DataViewListCtrl(self)
            self.listCtrl.AppendTextColumn(_("Parameter name"))
            self.listCtrl.AppendTextColumn(_("Typing"))
            self.listCtrl.AppendTextColumn(_("Associated type"))
            self.listCtrl.AppendToggleColumn(_("Optional"))
            self.listCtrl.AppendTextColumn(_("Short text"))
            self.listCtrl.AppendTextColumn(_("Long text"))

        def bindEvents(self):

            pass

        def doLayout(self):

            boxSizer = wx.BoxSizer(orient=wx.VERTICAL)

            for control, options in \
                    [(self.listCtrl, {'proportion': 1, 'flag': wx.EXPAND})]:
                boxSizer.Add(control, **options)

            self.SetSizerAndFit(boxSizer)

    class NbExceptionsPage(SapGuiForm):

        def createControls(self):

            self.listCtrl = wx.dataview.DataViewListCtrl(self)
            self.listCtrl.AppendTextColumn(_("Exception"))
            self.listCtrl.AppendTextColumn(_("Short text"))
            self.listCtrl.AppendTextColumn(_("Long text"))

        def bindEvents(self):

            pass

        def doLayout(self):

            boxSizer = wx.BoxSizer(orient=wx.VERTICAL)

            for control, options in \
                    [(self.listCtrl, {'proportion': 1, 'flag': wx.EXPAND})]:
                boxSizer.Add(control, **options)

            self.SetSizerAndFit(boxSizer)

    class NbSourceCodePage(SapGuiForm):

        def createControls(self):

            self.sourceTextCtrl = AbapCodeEditor(self)

        def bindEvents(self):

            pass

        def doLayout(self):

            boxSizer = wx.BoxSizer(orient=wx.VERTICAL)

            for control, options in \
                    [(self.sourceTextCtrl, {'proportion': 1, 'flag': wx.EXPAND})]:
                boxSizer.Add(control, **options)

            self.SetSizerAndFit(boxSizer)

    def fillInitialData(self, AbapObject):

        self.functionTextCtrl.SetValue(AbapObject.name)

        characteristics = self.nbCharacteristicsPage
        if AbapObject.function_group is not None:
            characteristics.functionGroupTextCtrl.SetValue(AbapObject.function_group.name)
            characteristics.functionGroupDescriptionTextCtrl.SetValue(AbapObject.function_group.description)
        characteristics.functionDescriptionTextCtrl.SetValue(AbapObject.description)

        importingPage = self.nbImportingPage
        for importingParam in AbapObject.parameters_importing.values():
            itemValues = [
                importingParam.name,
                "",
                importingParam.typ,
                importingParam.default_value,
                (importingParam.is_optional == 'X'),
                (importingParam.is_reference != 'X'),
                "",
                "",
            ]
            importingPage.listCtrl.AppendItem(values=itemValues)

        exportingPage = self.nbExportingPage
        for exportingParam in AbapObject.parameters_exporting.values():
            itemValues = [
                exportingParam.name,
                "",
                exportingParam.typ,
                (exportingParam.is_reference != 'X'),
                "",
                "",
            ]
            exportingPage.listCtrl.AppendItem(values=itemValues)

        changingPage = self.nbChangingPage
        for changingParam in AbapObject.parameters_changing.values():
            itemValues = [
                changingParam.name,
                "",
                changingParam.typ,
                changingParam.default_value,
                (changingParam.is_optional == 'X'),
                (changingParam.is_reference != 'X'),
                "",
                "",
            ]
            changingPage.listCtrl.AppendItem(values=itemValues)

        tablesPage = self.nbTablesPage
        for tablesParam in AbapObject.parameters_tables.values():
            itemValues = [
                tablesParam.name,
                "",
                tablesParam.typ,
                (tablesParam.is_optional == 'X'),
                "",
                "",
            ]
            tablesPage.listCtrl.AppendItem(values=itemValues)

        exceptionsPage = self.nbExceptionsPage
        for exception in AbapObject.exceptions.values():
            itemValues = [
                exception,
                "",
                "",
            ]
            exceptionsPage.listCtrl.AppendItem(values=itemValues)

        source = self.nbSourceCodePage
        source.sourceTextCtrl.SetText(AbapObject.source_code.source_code)
