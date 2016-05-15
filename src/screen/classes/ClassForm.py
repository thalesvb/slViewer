'''
Created on 17/06/2015

@author: thales
'''

import wx.dataview

from custom_widgets.AbapCodeEditor import AbapCodeEditor
import helper.HelperFunctions
from screen.template.SapGuiForm import SapGuiForm


class ShowClassForm(SapGuiForm):

    def createControls(self):
        self.classLabel = wx.StaticText(self, label=_("Interface / Class"))
        self.classTextCtrl = wx.TextCtrl(self)

        self.notebook = wx.Notebook(self)
        self.nbCharacteristicsPage = self.NbCharacteristicsPage(self.notebook)
        self.notebook.AddPage(self.nbCharacteristicsPage, _("Properties"))
        nbInterfacesPage = self.NbInterfacesPage(self.notebook)
        self.notebook.AddPage(nbInterfacesPage, _("Interfaces"))
        self.nbAttributesPage = self.NbAttributesPage(self.notebook)
        self.notebook.AddPage(self.nbAttributesPage, _("Attributes"))
        self.nbMethodsPage = self.NbMethodsPage(self.notebook)
        self.notebook.AddPage(self.nbMethodsPage, _("Methods"))
        nbEventsPage = self.NbEventsPage(self.notebook)
        self.notebook.AddPage(nbEventsPage, _("Events"))
        nbTypesPage = self.NbTypesPage(self.notebook)
        self.notebook.AddPage(nbTypesPage, _("Types"))
        nbAliasesPage = self.NbAliasesPage(self.notebook)
        self.notebook.AddPage(nbAliasesPage, _("Aliases"))

    def createMenu(self):
        SapGuiForm.createMenu(self)
        menuBar = wx.MenuBar()
        
        #Menu GoTo
        gotoMenu = wx.Menu()
        localImplMenuItem = gotoMenu.Append(id=wx.NewId(),
                                            item=_("Local implementation"),
                                            helpString=_("Local implementation"))
        self.GetParent().Bind(wx.EVT_MENU,
                              self.OnShowLocalImplementation,
                              id=localImplMenuItem.GetId())

        localMacrosMenuItem = gotoMenu.Append(id=wx.NewId(),
                                              item=_("Local macros"),
                                              helpString=_("Local macros"))
        self.GetParent().Bind(wx.EVT_MENU,
                              self.OnShowLocalMacros,
                              id=localMacrosMenuItem.GetId())

        localTypesMenuItem = gotoMenu.Append(id=wx.NewId(),
                                             item=_("Local types"),
                                             helpString=_("Local types"))
        self.GetParent().Bind(wx.EVT_MENU,
                              self.OnShowLocalTypes,
                              id=localTypesMenuItem.GetId())
        
        menuBar.Append(gotoMenu, _("Go to"))
        self.GetParent().SetMenuBar(menuBar)

    def bindEvents(self):
        pass

    def doLayout(self):
        boxSizer = wx.BoxSizer(orient=wx.VERTICAL)
        boxSizer.Add(self.classLabel, 0, wx.ALL)
        boxSizer.Add(self.classTextCtrl, 0, wx.EXPAND)
        boxSizer.Add(self.notebook, 1, wx.EXPAND)
        self.SetSizer(boxSizer)

    class NbCharacteristicsPage(SapGuiForm):
        ''' Characteristics tab '''

        def createControls(self):
            self.descriptionLabel = wx.StaticText(self,
                                                  label=_("Description"))
            self.descriptionTextCtrl = wx.TextCtrl(self)

            self.packageLabel = wx.StaticText(self,
                                              label=_("Package"))
            self.packageTextCtrl = wx.TextCtrl(self)
            # Disable package since salink doesn't import it.
            self.packageTextCtrl.Enable(False)
            self.originalLanguageLabel = wx.StaticText(self,
                                                       label=_("Original language"))
            self.originalLanguageTextCtrl = wx.TextCtrl(self)
            self.createdByLabel = wx.StaticText(self,
                                                label=_("Created"))
            self.createdByUserTextCtrl = wx.TextCtrl(self)
            self.createdOnDateCtrl = wx.TextCtrl(self)
            self.changedByLabel = wx.StaticText(self,
                                                label=_("Last change"))
            self.changedByUserTextCtrl = wx.TextCtrl(self)
            self.changedOnDateCtrl = wx.TextCtrl(self)

        def bindEvents(self):
            pass

        def doLayout(self):
            boxSizer = wx.BoxSizer(orient=wx.VERTICAL)

            for control, options in \
                    [(self.descriptionLabel, {}),
                     (self.descriptionTextCtrl, {'flag': wx.EXPAND}),
                     (self.packageLabel, {}),
                     (self.packageTextCtrl, {'flag': wx.EXPAND}),
                     (self.originalLanguageLabel, {}),
                     (self.originalLanguageTextCtrl, {'flag': wx.EXPAND}),
                     (self.createdByLabel, {}),
                     (self.createdByUserTextCtrl, {'flag': wx.EXPAND}),
                     (self.createdOnDateCtrl, {'flag': wx.EXPAND}),
                     (self.changedByLabel, {}),
                     (self.changedByUserTextCtrl, {'flag': wx.EXPAND}),
                     (self.changedOnDateCtrl, {'flag': wx.EXPAND})]:
                boxSizer.Add(control, **options)

            self.SetSizerAndFit(boxSizer)

    class NbInterfacesPage(SapGuiForm):
        ''' Interfaces tab '''

        def createControls(self):
            self.listCtrl = wx.dataview.DataViewListCtrl(self)
            self.listCtrl.AppendTextColumn(_("Interface"))
            self.listCtrl.AppendToggleColumn(_("Modeled only"))
            self.listCtrl.AppendTextColumn(_("Description"))

        def bindEvents(self):
            pass

        def doLayout(self):
            boxSizer = wx.BoxSizer(orient=wx.VERTICAL)

            for control, options in \
                    [(self.listCtrl, {'proportion': 1, 'flag': wx.EXPAND})]:
                boxSizer.Add(control, **options)

            self.SetSizerAndFit(boxSizer)

    class NbAttributesPage(SapGuiForm):
        ''' Attributes tab '''

        def createControls(self):
            self.listCtrl = wx.dataview.DataViewListCtrl(self)
            self.listCtrl.AppendTextColumn(_("Attribute"))
            self.listCtrl.AppendTextColumn(_("Level"))
            self.listCtrl.AppendTextColumn(_("Visibility"))
            self.listCtrl.AppendToggleColumn(_("Read-Only"))
            self.listCtrl.AppendTextColumn(_("Typing"))
            self.listCtrl.AppendTextColumn(_("Associated type"))
            self.listCtrl.AppendTextColumn("")
            self.listCtrl.AppendTextColumn(_("Description"))
            self.listCtrl.AppendTextColumn(_("Initial value"))

        def bindEvents(self):
            pass

        def doLayout(self):
            boxSizer = wx.BoxSizer(orient=wx.VERTICAL)

            for control, options in \
                    [(self.listCtrl, {'proportion': 1, 'flag': wx.EXPAND})]:
                boxSizer.Add(control, **options)

            self.SetSizerAndFit(boxSizer)

    class NbMethodsPage(SapGuiForm):
        ''' Methods tab '''

        def createControls(self):
            self.listCtrl = wx.dataview.DataViewListCtrl(self)
            self.listCtrl.AppendTextColumn(_("Method"))
            self.listCtrl.AppendTextColumn(_("Level"))
            self.listCtrl.AppendTextColumn(_("Visibility"))
            self.listCtrl.AppendTextColumn(_("Method type"))
            self.listCtrl.AppendTextColumn(_("Description"))

        def bindEvents(self):
            # Register event to handle double click on a item from methods list.
            self.Bind(wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED,
                      self.OnMethodListClick,
                      self.listCtrl)

        def doLayout(self):
            boxSizer = wx.BoxSizer(orient=wx.VERTICAL)

            for control, options in \
                    [(self.listCtrl, {'proportion': 1, 'flag': wx.EXPAND})]:
                boxSizer.Add(control, **options)

            self.SetSizerAndFit(boxSizer)

        def OnMethodListClick(self, event):
            itemClicked = event.GetItem()
            itemRow = self.listCtrl.ItemToRow(itemClicked)
            methodName = self.listCtrl.GetTextValue(itemRow, 0)
            method = self.GetParent().GetParent().currentClass.methods[methodName]
            (helper.HelperFunctions.
             navigate_to_screen(ObjectName=methodName,
                                ObjectTypeKey=(helper.HelperFunctions.
                                               ClickableObject.CLASS_METHOD),
                                Frame=self.GetParent().GetParent().GetParent(),
                                ObjectOriginFile=None,
                                AbapObject=method))

    class NbEventsPage(SapGuiForm):
        ''' Events tab '''

        def createControls(self):
            self.listCtrl = wx.dataview.DataViewListCtrl(self)
            self.listCtrl.AppendTextColumn(_("Event"))
            self.listCtrl.AppendTextColumn(_("Type"))
            self.listCtrl.AppendTextColumn(_("Description"))

        def bindEvents(self):
            pass

        def doLayout(self):
            boxSizer = wx.BoxSizer(orient=wx.VERTICAL)

            for control, options in \
                    [(self.listCtrl, {'proportion': 1, 'flag': wx.EXPAND})]:
                boxSizer.Add(control, **options)

            self.SetSizerAndFit(boxSizer)

    class NbTypesPage(SapGuiForm):
        ''' Types tab '''

        def createControls(self):
            self.listCtrl = wx.dataview.DataViewListCtrl(self)
            self.listCtrl.AppendTextColumn(_("Type"))
            self.listCtrl.AppendTextColumn(_("Typing"))
            self.listCtrl.AppendTextColumn(_("Associated type"))
            self.listCtrl.AppendTextColumn("")
            self.listCtrl.AppendTextColumn(_("Description"))

        def bindEvents(self):
            pass

        def doLayout(self):
            boxSizer = wx.BoxSizer(orient=wx.VERTICAL)

            for control, options in \
                    [(self.listCtrl, {'proportion': 1, 'flag': wx.EXPAND})]:
                boxSizer.Add(control, **options)

            self.SetSizerAndFit(boxSizer)

    class NbAliasesPage(SapGuiForm):
        ''' Aliases tab '''

        def createControls(self):
            self.listCtrl = wx.dataview.DataViewListCtrl(self)
            self.listCtrl.AppendTextColumn(_("Interface component"))
            self.listCtrl.AppendTextColumn("")
            self.listCtrl.AppendTextColumn(_("Alias"))

        def bindEvents(self):
            pass

        def doLayout(self):
            boxSizer = wx.BoxSizer(orient=wx.VERTICAL)

            for control, options in \
                    [(self.listCtrl, {'proportion': 1, 'flag': wx.EXPAND})]:
                boxSizer.Add(control, **options)

            self.SetSizerAndFit(boxSizer)

    def fillInitialData(self, AbapObject):
        self.__current_class = AbapObject
        self.classTextCtrl.SetValue(AbapObject.name)

        characteristics = self.nbCharacteristicsPage
        characteristics.descriptionTextCtrl.SetValue(AbapObject.description)
        # characteristics.packageTextCtrl.SetValue(AbapObject.package)
        characteristics.originalLanguageTextCtrl.SetValue(AbapObject.original_language)
        characteristics.createdByUserTextCtrl.SetValue(AbapObject.created_by)
        characteristics.createdOnDateCtrl.SetValue(AbapObject.created_on)
        characteristics.changedByUserTextCtrl.SetValue(AbapObject.changed_by)
        characteristics.changedOnDateCtrl.SetValue(AbapObject.changed_on)

        attributes = self.nbAttributesPage
        for attribute in AbapObject.attributes.values():
            itemData = [
                attribute.name,
                helper.HelperFunctions.i18nHelper.decl_type(CodeDeclType=attribute.decl_type),
                helper.HelperFunctions.i18nHelper.exposure(CodeExposure=attribute.exposure),
                False,
                helper.HelperFunctions.i18nHelper.typType(CodeTypType=attribute.typType),
                attribute.type,
                "",
                attribute.description,
                ""
            ]
            attributes.listCtrl.AppendItem(itemData)

        methods = self.nbMethodsPage
        for method in AbapObject.methods.values():
            itemValues = [
                method.name,
                helper.HelperFunctions.i18nHelper.mtdDeclType(CodeMtdDeclType=method.decl_type),
                helper.HelperFunctions.i18nHelper.exposure(CodeExposure=method.exposure),
                "",
                method.description
            ]
            methods.listCtrl.AppendItem(values=itemValues)

    @property
    def currentClass(self):
        #FIXME: change to "__model" attribute name
        return self.__current_class
    
    def OnShowLocalImplementation(self, event):
        (helper.HelperFunctions.
             navigate_to_screen(ObjectName=None,
                                ObjectTypeKey=(helper.HelperFunctions.
                                               ClickableObject.CLASS_LOCAL_IMPLEMENTATION),
                                Frame=self.GetParent(),
                                ObjectOriginFile=None,
                                AbapObject=self.__current_class.local_implementation))

    def OnShowLocalMacros(self, event):
        (helper.HelperFunctions.
             navigate_to_screen(ObjectName=None,
                                ObjectTypeKey=(helper.HelperFunctions.
                                               ClickableObject.CLASS_LOCAL_MACROS),
                                Frame=self.GetParent(),
                                ObjectOriginFile=None,
                                AbapObject=self.__current_class.local_macros))

    def OnShowLocalTypes(self, event):
        (helper.HelperFunctions.
             navigate_to_screen(ObjectName=None,
                                ObjectTypeKey=(helper.HelperFunctions.
                                               ClickableObject.CLASS_LOCAL_TYPES),
                                Frame=self.GetParent(),
                                ObjectOriginFile=None,
                                AbapObject=self.__current_class.local_types))

class ShowClassMethodSourceForm(SapGuiForm):

    def createControls(self):
        self.parametersListCtrl = wx.dataview.DataViewListCtrl(self)
        self.parametersListCtrl.AppendTextColumn(_("Type"))
        self.parametersListCtrl.AppendTextColumn(_("Parameter"))
        self.parametersListCtrl.AppendTextColumn(_("Associated type"))
        self.sourceTextCtrl = AbapCodeEditor(self)

    def bindEvents(self):
        pass

    def doLayout(self):
        boxSizer = wx.BoxSizer(orient=wx.VERTICAL)

        for control, options in \
                [(self.parametersListCtrl, {'proportion': 1, 'flag': wx.EXPAND}),
                 (self.sourceTextCtrl, {'proportion': 1, 'flag': wx.EXPAND})]:
            boxSizer.Add(control, **options)

        self.SetSizerAndFit(boxSizer)

    def fillInitialData(self, AbapObject):
        for parameter in AbapObject.parameters.values():
            itemValues = [
                helper.HelperFunctions.i18nHelper.parameterDeclType(CodeParDeclTyp=parameter.declaration_type),
                parameter.name,
                parameter.type_
            ]
            self.parametersListCtrl.AppendItem(values=itemValues)
        self.sourceTextCtrl.SetText(AbapObject.source_code.source_code)

class ShowClassLocalImplementation(SapGuiForm):
    
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

        self.sourceTextCtrl.SetText(AbapObject.source_code)

class ShowClassLocalMacros(ShowClassLocalImplementation):
    pass

class ShowClassLocalTypes(ShowClassLocalImplementation):
    pass
