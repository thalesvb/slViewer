'''
Created on 17/06/2015

@author: thales
'''
from enum import Enum

from screen.classes.ClassForm import ShowClassForm, ShowClassMethodSourceForm,\
    ShowClassLocalImplementation, ShowClassLocalMacros, ShowClassLocalTypes
from screen.functions.FunctionForm import ShowFunctionForm
from helper.ObjectsBuffer import ObjectsBuffer, ObjectBufferType
from builtins import RuntimeError
from screen.programs.ProgramForm import ShowProgramForm
from screen.message_classes.MessageClassForm import ShowMessageClassForm


class ClickableObject(Enum):
        CLASS = 1
        CLASS_LOCAL_IMPLEMENTATION = 2
        CLASS_LOCAL_MACROS = 3
        CLASS_LOCAL_TYPES = 4
        CLASS_METHOD = 5
        FUNCTION_GROUP = 6
        FUNCTION = 7
        MESSAGE_CLASS = 8
        PROGRAM = 9

__map_clickableObject__ = {
  ClickableObject.CLASS: [ShowClassForm, 'classes'],
  ClickableObject.CLASS_LOCAL_IMPLEMENTATION:[ShowClassLocalImplementation, None],
  ClickableObject.CLASS_LOCAL_MACROS: [ShowClassLocalMacros, None],
  ClickableObject.CLASS_LOCAL_TYPES: [ShowClassLocalTypes, None],
  ClickableObject.CLASS_METHOD: [ShowClassMethodSourceForm, None],
  ClickableObject.FUNCTION: [ShowFunctionForm, 'function_modules'],
  ClickableObject.MESSAGE_CLASS: [ShowMessageClassForm, 'message_classes'],
  ClickableObject.PROGRAM: [ShowProgramForm, 'programs'],
}
'''Buffer store list with following information: Form, bufferAttribute'''


def navigate_to_screen(ObjectName,
                       ObjectTypeKey,
                       Frame,
                       ObjectOriginFile=None,
                       AbapObject=None):
    '''Easy navigate to screens, using data references from SapLink file or from
     Python objects.'''
    clickableObjectAttr = __map_clickableObject__.get(ObjectTypeKey, None)
    if clickableObjectAttr is None:
        return

    if ObjectOriginFile is not None:
        # Find object which ObjectName represent
        slinkBuffer = (ObjectsBuffer(ObjectBufferType.SAPLINKFILE).
                       get(ObjectOriginFile))
        # Read internal attribute from slinkBuffer using internal dict mapping
        # of attributes, to allow simplification of code.
        objBuffer = getattr(slinkBuffer, clickableObjectAttr[1])[ObjectName]
    elif AbapObject is not None:
        objBuffer = AbapObject
    else:
        raise RuntimeError

    formInstance = clickableObjectAttr[0](Frame)
    formInstance.fillInitialData(objBuffer)
    Frame.loadNewView(formInstance)


class i18nHelper:

    class ABAP_Class:
        class ABAP_Class_Attribute:
            DECL_TYPE = {
                '0': 'Instance Attribute',
                '1': 'Static Attribute',
                '2': 'Constant'
            }

        class ABAP_Class_Method:
            EXPOSURE = {
                '0': 'Private',
                '1': 'Protected',
                '2': 'Public'
            }
            MTDTYPE = {
                '0': 'Instance Method',
                '1': 'Static Method'
            }
            pass
        pass

    class ABAP_Calls_Parameter:
        PARDECLTYP = {
            '0': 'Importing',
            '1': 'Exporting',
            '2': 'Changing',
            '3': 'Returning',
            'EXCP': 'Exception',
        }
        PARPASSTYP = {}
        TYPTYPE = {
            '0': 'Like',
            '1': 'Type',
            '3': 'Type Ref To'
        }

    class ABAP_Program:
        SUBC = {
            '1': 'Executable program',
            'I': 'INCLUDE program',
            'M': 'Module Pool',
            'F': 'Function group',
            'S': 'Subroutine Pool',
            'K': 'Class pool',
            'T': 'Type Pool',
            'X': 'XSLT Program'
        }
        '''SUBC: Program type.'''
        RSTAT = {
            'P': 'SAP Standard Production Program',
            'K': 'Customer Production Program',
            'S': 'System Program',
            'T': 'Test Program'
        }
        '''RSTAT: Program status.'''

    @staticmethod
    def parameterDeclType(CodeParDeclTyp):
        return (i18nHelper.
                ABAP_Calls_Parameter.
                PARDECLTYP.get(CodeParDeclTyp, ''))

    @staticmethod
    def decl_type(CodeDeclType):
        return (i18nHelper.
                ABAP_Class.
                ABAP_Class_Attribute.
                DECL_TYPE.get(CodeDeclType, ''))

    @staticmethod
    def mtdDeclType(CodeMtdDeclType):
        return (i18nHelper.
                ABAP_Class.
                ABAP_Class_Method.
                MTDTYPE.get(CodeMtdDeclType, ''))

    @staticmethod
    def exposure(CodeExposure):
        return (i18nHelper.
                ABAP_Class.
                ABAP_Class_Method.
                EXPOSURE.get(CodeExposure, ''))

    @staticmethod
    def typType(CodeTypType):
        return (i18nHelper.
                ABAP_Calls_Parameter.
                TYPTYPE.get(CodeTypType, ''))
