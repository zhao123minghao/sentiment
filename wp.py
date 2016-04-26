# -*- coding: utf-8 -*- 
# just for utf-8 code
# if gbk code,you need to tansform
import sys
import os

def getlastline(_list,_index):
    if( _index == 0):
        return None
    return _list[_index-1]

def getnextline(_list,_index):
    if( _index >= len(_list) -1 ):
        return None
    return _list[_index+1]

def getnextnline(_list,_index,n):
    if( _index+n>= len(_list)):
        return None
    return _list[_index+n]

def getlastnline(_list,_index,n):
    if( _index-n < 0):
        return None
    return _list[_index+n]

def getlocation(_list,_label):
    i = 0
    for line in _list:
        if( line[1] == _label):
             return i
        return -1


def attrdictinit():
    return []

def wordprocess(_word,_wdict):
    if(_word in _wdict):
        return _wdict[_word][0]
    return 0

def wordp(_word,_wdict):
    if(_word in _wdict):
        return _wdict[_word][1]
    return ''


def adjprocess(word,wdict):
    return wordprocess(word,wdict)

def nounprocess(word,wdict):
    return wordprocess(word,wdict)

def verbprocess(word,wdict):
    return wordprocess(word,wdict)

def advprocess(word,wdict):
    return wordprocess(word,wdict)

def pprocess(word,wdict):
    if(word == '\xb0\xd1' or word == '\xe6\x8a\x8a'):
        return 1
    if(word == '\xb1\xbb' or word == '\xe8\xa2\xab'):
        return 2
    return 0

def ujprocess(word):
    return []
# n + uj + n
# adj + uj + n
# adj + uj

def enprocess(ws,enwordlist):
    if(ws in enwordlist):
        return 'n'
    return 'un'

def dictstart(dfname):
    dictfile = open(dfname,'r')
    dictstr = dictfile.readlines()
    dict = {}
    for line in dictstr:
        tmp1 = line.rstrip('\n')
        tmp2 = tmp1.split(' ')
        wstr = tmp2[0]
        try:
        	p = float(tmp2[1])
        except Exception,e:
            print 'error word',tmp2[0]
            continue
        if(tmp2[2] == 'None'):
            tmp2[2] = ''
        dict[wstr] = [p,tmp2[2]]
#print dict
    dictfile.close()
    return dict

def ndictstart(dfname):
    dictfile = open(dfname,'r')
    dictstr = dictfile.readlines()
    dict = {}
    for line in dictstr:
        tmp1 = line.rstrip('\n')
        tmp2 = tmp1.split(' ')
        wstr = tmp2[0]
        try:
            dict[wstr] = tmp2[1]
        except Exception,e:
            print wstr
#print dict
    dictfile.close()
    return dict

def ndictsearch(_name,_dict):
    if(_name in _dict):
        return _dict[_name]
    return ''
