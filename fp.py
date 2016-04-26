# -*- coding: utf-8 -*-

def readfile(filename):
    myfile = open(filename,'r')
    _ret = myfile.readlines()
    myfile.close()
    return _ret

def writefile(filename,_list):    
    myfile = open(filename,'w')
    myfile.writelines(_list)
    myfile.close()

def appendfile(filename,_list):    
    myfile = open(filename,'a+')
    myfile.writelines(_list)
    myfile.close()

def mysplit(src,sl):
    result = []
    for line in sl:
        src=src.replace(line,'##')
    result = src.split('##')
    return result

