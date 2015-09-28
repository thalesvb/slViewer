'''
Created on 17/06/2015

@author: thales
'''

import wx

import slpyser
from helper.ObjectsBuffer import ObjectsBuffer, ObjectBufferType
from helper.HelperFunctions import ClickableObject, navigate_to_screen
from screen.template.SapGuiForm import SapGuiForm


class EasyAccessForm(SapGuiForm):

    def createControls(self):

        self.saplinkFilesTree = wx.TreeCtrl(self)
        self.rootOpenedFiles = self.saplinkFilesTree.AddRoot(text=_("Opened files"))

        self.createMenu()

    def bindEvents(self):

        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED,
                  self.OnSaplinkTreeDoubleClick,
                  self.saplinkFilesTree)

    def createMenu(self):

        menuBar = wx.MenuBar()

        # Menu File
        fileMenu = wx.Menu()
        openFileMenuItem = fileMenu.Append(id=wx.ID_OPEN,
                                           item=_("Open file..."),
                                           helpString=_("Open SapLink file"))
        self.GetParent().Bind(wx.EVT_MENU, self.OnOpenFileMenuItem, id=wx.ID_OPEN)
        menuBar.Append(fileMenu, _("File"))

        self.GetParent().SetMenuBar(menuBar)

    def doLayout(self):

        boxSizer = wx.BoxSizer(orient=wx.VERTICAL)

        for control, options in \
                [(self.saplinkFilesTree, {'flag': wx.EXPAND, 'proportion': 1})]:
            boxSizer.Add(control, **options)

        self.SetSizerAndFit(boxSizer)

    def createNewNodeForFile(self, SapLinkFile):
        tree = self.saplinkFilesTree

        rootFile = tree.AppendItem(parent=self.rootOpenedFiles,
                                   text=SapLinkFile.file_path)

        nodeClasses = tree.AppendItem(parent=rootFile,
                                      text=_("Classes"))
        for objClass in SapLinkFile.classes.values():
            leafClass = tree.AppendItem(parent=nodeClasses,
                                        text=objClass.name,
                                        data=[SapLinkFile.file_path,
                                              ClickableObject.CLASS])

        nodeFunctionGroups = tree.AppendItem(parent=rootFile,
                                             text=_("Function Groups"))
        for objFunctionGroup in SapLinkFile.function_groups.values():
            nodeFunctionGroup = tree.AppendItem(parent=nodeFunctionGroups,
                                                text=objFunctionGroup.name,
                                                data=ClickableObject.FUNCTION_GROUP)
            nodeFunctionModules = tree.AppendItem(parent=nodeFunctionGroup,
                                                  text=_("Function Modules"),
                                                  data=None)
            for objFunctionModule in objFunctionGroup.function_modules.values():
                leafFunctionModule = tree.AppendItem(parent=nodeFunctionModules,
                                                     text=objFunctionModule.name,
                                                     data=[SapLinkFile.file_path,
                                                           ClickableObject.FUNCTION])

        nodePrograms = tree.AppendItem(parent=rootFile, text=_("Reports"))
        for objProgram in SapLinkFile.programs.values():
            leafProgram = tree.AppendItem(parent=nodePrograms,
                                          text=objProgram.name,
                                          data=[SapLinkFile.file_path,
                                                ClickableObject.PROGRAM])

        nodeMessageClasses = tree.AppendItem(parent=rootFile, text=_("Message classes"))
        for msgClass in SapLinkFile.message_classes.values():
            leafMsgClass = tree.AppendItem(parent=nodeMessageClasses,
                                           text=msgClass.name,
                                           data=[SapLinkFile.file_path,
                                                 ClickableObject.MESSAGE_CLASS])

    def OnOpenFileMenuItem(self, event):
        wildcardSapLinkFiles = [
            "{0:s} (*.nugg;*.slnk)|*.nugg;*.slnk".format(_("SapLink files")),
        ]
        openFileDialog = wx.FileDialog(parent=self,
                                       message=_("Open file..."),
                                       wildcard="|".join(wildcardSapLinkFiles),
                                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if openFileDialog.ShowModal() != wx.ID_CANCEL:
            filePath = openFileDialog.GetPath()
            # File will be parsed...
            SapLinkFile = slpyser.parse(filePath)
            # ... and parser result stored in app global buffer.
            ObjectsBuffer(ObjectBufferType.SAPLINKFILE)[filePath] = SapLinkFile

            self.createNewNodeForFile(SapLinkFile=SapLinkFile)

    def OnSaplinkTreeDoubleClick(self, event):
        clickedObject = event.GetItem()
        objectName = self.saplinkFilesTree.GetItemText(clickedObject)
        itemData = self.saplinkFilesTree.GetItemData(clickedObject)
        originFile = itemData[0]
        objectTypeKey = itemData[1]
        navigate_to_screen(ObjectName=objectName,
                           ObjectTypeKey=objectTypeKey,
                           ObjectOriginFile=originFile,
                           Frame=self.GetParent())
