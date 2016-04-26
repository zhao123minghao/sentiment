#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sp
import ts
import fp

wordlist = []

def lineprocess(wl):
    return sp.lineprocess(wl)

def wordrocess(wr):
    s = None
    wordname = wr[1]
    wordattr = wr[2]
    for line in wordlist:
        if(wordattr == line[0]):
            s = line
            
    if(s == None):
        wordlist.append([wordattr,[[wordname,1]]])
        return
    words = s[1]
    for word in words:
        if(word[0] == wordname):
            word[1] += 1
            return
    words.append([wordname,1])
    
    
def process(srcline):
    i = 0
    s = 0
    srclength = len(srcline)
    while (i < srclength):
        line = srcline[i]
        i += 1
        if ( s == 0 or s == 1):
            userdata = line
            s += 1
            continue

        if (line == '##\n'):
            s = 0
            continue
        sl = lineprocess(line)
        for lstr in sl:
            wordrocess(lstr)
        

tl = fp.readfile('sent_test_b.txt')
process(tl)
ts._print(wordlist)