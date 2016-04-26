# -*- coding: utf-8 -*-

import types

def _print(item):
    if(type(item) == types.IntType):
        print item,
        return
    if(type(item) == types.FloatType):
        print item,
        return
    if(type(item) == types.LongType):
        print item,
        return
    if(type(item) == types.StringType):
        if(item == ''):
            return
        print item,
        return
    if(type(item) == types.ListType):
        for line in item:
            _print(line)
        print ''
        return
    if(type(item) == types.TupleType):
        for line in item:
            _print(line)
        return
    
def _writefile(item,file_pointer):
    if(type(item) == types.IntType):
        file_pointer.write(str(item) +' ')
        return
    if(type(item) == types.FloatType):
        file_pointer.write(str(item)+' ')
        return
    if(type(item) == types.LongType):
        file_pointer.write(str(item)+' ')
        return
    if(type(item) == types.StringType):
        file_pointer.write(item+' ')
        return
    if(type(item) == types.ListType):
        for line in item:
            _writefile(item,file_pointer)
        file_pointer.write('\n')
        return
    if(type(item) == types.TupleType):
        for line in item:
            _writefile(item,file_pointer)
        file_pointer.write('\n')
        return