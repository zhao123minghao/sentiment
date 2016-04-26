#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sq
import fp
import os

if(os.path.isfile('/home/zhao/sw/v.txt')):
    os.remove('/home/zhao/sw/v.txt')
    
if(os.path.isfile('/home/zhao/sw/adj.txt')):
    os.remove('/home/zhao/sw/adj.txt')
    
if(os.path.isfile('/home/zhao/sw/adv.txt')):
    os.remove('/home/zhao/sw/adv.txt')

cn = sq.dbstart('sentiment')
cr = sq.cursor(cn)

#rl = sq.get_sentiment_word_attr(cn,cr,'sent_word','v')
rl = sq.get_sent_word(cn,cr,'sent_word')
lr = ''

for line in rl:
    wordfile = '/home/zhao/sw/'+ line[1].encode('utf8') + '.txt'
    comment = line[3].encode('utf8')
    if(comment == ''):
        comment = 'None'
    lr = line[0].encode('utf8') +' '+ str(line[2]) +' '+ comment +'\n'
    fp.appendfile(wordfile,lr)

#print lr
#fp.writefile('v.txt',lr)
sq.dbstop(cn,cr)