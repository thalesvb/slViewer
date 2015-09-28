'''
Created on 03/08/2015

@author: thales
'''

import wx, wx.stc as stc

class CodeEditorBase(stc.StyledTextCtrl):
    def __init__(self, parent):
        super(CodeEditorBase, self).__init__(parent)

        # Attributes
        font = wx.Font(10, wx.FONTFAMILY_MODERN,
                           wx.FONTSTYLE_NORMAL,
                           wx.FONTWEIGHT_NORMAL)
        self.face = font.GetFaceName()
        self.size = font.GetPointSize()

        # Setup
        self.SetupBaseStyles()

    def EnableLineNumbers(self, enable=True):
        """Enable/Disable line number margin"""
        if enable:
            self.SetMarginType(1, stc.STC_MARGIN_NUMBER)
            self.SetMarginMask(1, 0)
            self.SetMarginWidth(1, 25)
        else:
            self.SetMarginWidth(1, 0)

    def GetFaces(self):
        """Get font style dictionary"""
        return dict(font=self.face,
                    size=self.size)

    def SetupBaseStyles(self):
        """Sets up the the basic non lexer specific
        styles.
        """
        faces = self.GetFaces()
        default = "face:%(font)s,size:%(size)d" % faces
        self.StyleSetSpec(stc.STC_STYLE_DEFAULT, default)
        line = "back:#C0C0C0," + default
        self.StyleSetSpec(stc.STC_STYLE_LINENUMBER, line)
        self.StyleSetSpec(stc.STC_STYLE_CONTROLCHAR,
                          "face:%(font)s" % faces)
