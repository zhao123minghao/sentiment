#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import sp
import pp
import fp
import step2
import ts

def sensplit(_src):
    return pp.sensplit(_src,pp.sendivs)

argv = sys.argv
if(len(argv) < 2):
    print 'we need an arguement'
    sys.exit(0)
filename = argv[1]
if(not os.path.isfile(filename)):
    print '\t\ttest file don\'t exist'
    sys.exit(0)

plist = fp.readfile(filename)
slist = []
for line in plist:
    slist += sensplit(line)
r = ''
for line in slist:
    r = r + line + '\n'
fp.writefile('__tmp1.txt',r)
if(os.path.isfile('__tmp.txt')):
    os.remove('__tmp.txt')

pp.divword('__tmp1.txt','__tmp.txt')
slist = fp.readfile('__tmp.txt')
sl = []
tmp = []
i = 0
length = len(slist)
while( i < length):
    sens = slist[i]
    i += 1
    #print line
    line = step2.line_div(sens)
    tmp.append(line)
#ts._print(tmp)
rmp = []
for line in tmp:
    #print line
    rmp += sp.sentence(line)
#print rmp
for line in plist:
    print line
    
for line in rmp:
    #print line
    if(line == []):
        continue
    if(line[0] == '' or line[3][0] == ''):
        continue
    print line[0],line[3][0],line[2][1]*line[3][2]