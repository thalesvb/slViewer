'''
Created on 03/08/2015

@author: thales
'''

import wx
import wx.stc

from custom_widgets.CodeEditorBase import CodeEditorBase


class AbapCodeEditor(CodeEditorBase):

    __thresold_infinite_loop = 10

    def __init__(self, parent):
        super(AbapCodeEditor, self).__init__(parent)

        # Load Constants
        self._keywords = [
            'CONSTANTS',
            'MESSAGE',
            'FORM',
            'ENDFORM',
            'USING',
            'CHANGING',
            'CALL',
            'FUNCTION',
            'METHOD',
            'EXPORTING',
            'IMPORTING',
            'TABLES',
            'RECEIVING',
            'EXCEPTIONS',
            'OTHERS',
            'IF',
            'ELSEIF',
            'ELSE',
            'ENDIF',
            'RAISE',
            'EXCEPTION',
            'ID',
            'TYPE',
            'NUMBER',
            'WITH',
            'RAISING',
            'VALUE',
            'IS',
            'BOUND',
            '&&',
            '<>',
            '==',
            '<=',
            '>=',
            '<',
            '>',
            'NE',
            'EQ',
            'LE',
            'GE',
            'LT',
            'GT',
            'AND',
            'OR',
            'NOT',
            'IMPORT',
            'EXPORT',
            'FROM',
            'TO',
            'MEMORY',
            'ID',
            'INTERNAL',
            'TABLE',
            'DATABASE',
            'SHARED',
            'BUFFER',
        ]

        # Setup
        # self.SetLexer(wx.stc.STC_LEX_PYTHON)
        self.SetLexer(wx.stc.STC_LEX_CONTAINER)
        self.SetupKeywords()
        self.SetupStyles()
        self.BindInternalEvents()
        self.EnableLineNumbers(True)

    def SetupKeywords(self):
        """Sets up the lexers keywords"""
        kwlist = u" ".join(self._keywords)
        self.SetKeyWords(0, kwlist)

    def SetupStyles(self):
        """Sets up the lexers styles"""
        # Python styles
        faces = self.GetFaces()
        fonts = "face:%(font)s,size:%(size)d" % faces
        default = "fore:#000000," + fonts

        # Default
        self.StyleSetSpec(wx.stc.STC_P_DEFAULT, default)
        # Comments
        self.StyleSetSpec(wx.stc.STC_P_COMMENTLINE,
                          "fore:#777777,italic," + fonts)
        # Number
        self.StyleSetSpec(wx.stc.STC_P_NUMBER,
                          "fore:#007F7F," + fonts)
        # String
        self.StyleSetSpec(wx.stc.STC_P_STRING,
                          "fore:#007F00," + fonts)
        # Single quoted string
        self.StyleSetSpec(wx.stc.STC_P_CHARACTER,
                          "fore:#7F007F," + fonts)
        # Keyword
        self.StyleSetSpec(wx.stc.STC_P_WORD,
                          "fore:#00007F,bold," + fonts)
        # Triple quotes
        self.StyleSetSpec(wx.stc.STC_P_TRIPLE,
                          "fore:#7F0000," + fonts)
        # Triple double quotes
        self.StyleSetSpec(wx.stc.STC_P_TRIPLEDOUBLE,
                          "fore:#7F0000," + fonts)
        # Class name definition
        self.StyleSetSpec(wx.stc.STC_P_CLASSNAME,
                          "fore:#0000FF,bold," + fonts)
        # Function or method name definition
        self.StyleSetSpec(wx.stc.STC_P_DEFNAME,
                          "fore:#007F7F,bold," + fonts)
        # Operators
        self.StyleSetSpec(wx.stc.STC_P_OPERATOR, "bold," + fonts)
        # Identifiers
        self.StyleSetSpec(wx.stc.STC_P_IDENTIFIER, default)
        # Comment-blocks
        self.StyleSetSpec(wx.stc.STC_P_COMMENTBLOCK,
                          "fore:#7F7F7F," + fonts)
        # End of line where string is not closed
        eol_style = "fore:#000000,back:#E0C0E0,eol," + fonts
        self.StyleSetSpec(wx.stc.STC_P_STRINGEOL, eol_style)

    def BindInternalEvents(self):
        self.Bind(wx.stc.EVT_STC_STYLENEEDED, self.OnStyleNeeded)

    def OnStyleNeeded(self, event):
        counterDetectInfLoop = 0
        """
        This counter is a hack to avoid infinite loop freeze due
        the syntax parser not working correctly in some situations.
        It could be removed in a near future after all fixes
        in this parser, but I think it's better to still use it
        because abap syntax changes with updates, and this program
        should handle those syntax changes at all costs.
        """
        maxPosition = event.GetPosition()
        start = 0
        styled_pos = self.GetEndStyled()
        # self.StartStyling(styled_pos,0x1f)
        while styled_pos < maxPosition and counterDetectInfLoop < self.__thresold_infinite_loop:
            lineNr = self.LineFromPosition(styled_pos)
            line = self.GetLine(lineNr)
            lineStart = self.PositionFromLine(lineNr)
            self.StartStyling(lineStart, 0x1f)
            length = self.LineLength(lineNr)
            #print(lineNr, styled_pos, length, line)
            # time.sleep(1)
            while len(line) > 0:
                partition = line.partition(' ')
                # print(partition)
                token = partition[0]
                if len(token) > 0:
                    if (token.startswith('*') or token.startswith('"')):
                        self.OnStyleCommentary(len(line))
                        partition = ''.partition(' ')  # Partition reset, it was all commentaries
                    else:
                        if (token.endswith(':') or
                                token.endswith(':\n') or
                                token.endswith('.') or
                                token.endswith('.\n') or
                                token.endswith('\n')):

                            tokenAnalyze = token[:-1]

                        else:
                            tokenAnalyze = token

                        if tokenAnalyze.upper() in self._keywords:
                            self.OnStyleKeyword(token)
                        elif (tokenAnalyze.startswith("'") and tokenAnalyze.endswith("'")):
                            # Function name, method name, keys for keywords
                            self.OnStyleString(token)
                        else:
                            self.OnStyleDefault(len(token))

                        if not token.endswith('\n'):
                            # Style the space character
                            self.OnStyleDefault(1)
                else:
                    # Style the splitter character 'space'
                    self.OnStyleDefault(1)
                line = partition[2]

            if styled_pos == self.GetEndStyled():
                counterDetectInfLoop = counterDetectInfLoop + 1
            else:
                counterDetectInfLoop = 0

            styled_pos = self.GetEndStyled()

    def OnStyleCommentary(self, length):
        self.SetStyling(length, wx.stc.STC_P_COMMENTLINE)

    def OnStyleKeyword(self, keyword):
        keywordLength = len(keyword)
        self.SetStyling(keywordLength, wx.stc.STC_P_WORD)

    def OnStyleString(self, string):
        stringLength = len(string)
        self.SetStyling(stringLength, wx.stc.STC_P_STRING)

    def OnStyleDefault(self, length):
        self.SetStyling(length, wx.stc.STC_P_DEFAULT)
        return True

    def SetText(self, text):
        """
        The styling was made only to easy reading of code, without any deep
        concept of parser and compilators applied.
        It curently only works well when loading the full text into view.
        Modifying it inline breaks styling so I set currently as not editable
        (to allow selection, copy, and resizing).
        """
        super(AbapCodeEditor, self).SetText(text)
        self.SetEditable(False)
