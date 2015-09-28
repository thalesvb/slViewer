'''
Created on 17/06/2015

@author: thales
'''
from enum import Enum

_ObjectsBufferMemory = {}


class ObjectBufferType(Enum):
    SAPLINKFILE = 1


class ObjectsBuffer:
    '''
    Objects buffer using singleton pattern
    '''

    def __new__(cls, ObjectBufferType):
        if ObjectBufferType in _ObjectsBufferMemory:
            return _ObjectsBufferMemory[ObjectBufferType]
        self = {}
        _ObjectsBufferMemory[ObjectBufferType] = self
        return self
