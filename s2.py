#!/usr/bin/env python

import sp
import sq
import fp

def line_div(wordlist):
    result = []
    wl = wordlist.rstrip('\n')
    rl = wl.split(' ')
    num = 0
    for substr in rl:
        if(substr == ''):
            continue
        t = substr.split('/')
        if(len(t)!=1):
            result.append([num,t[0],t[1]])
            num += 1
    return result

def line_del_other(wordlist):
	result = ''
	for line in wordlist:
		result = result + line[1]
	return result

def sprocess(rlist):
    if(rlist == []):
        return []
    ret = []
    #print rlist
    for line in rlist:
        r0 = line[0]
        r1 = line[1]
        r2 = line[2][1]
        r3 = line[3][0]
        r4 = line[3][2] * r2
        r5 = line[3][1]
        if(r0 == ''):
            continue
        #print r0+r3
        t = sp.get_word_leibie(r4,r5)
        if(t != ''):
            print t
        r = [r0+t,r4]
        ret.append(r)
    return ret

def senprocess(infile,_dbcn,_cur):
    srcline = fp.readfile(infile)
    srclength = len(srcline)

    i = 0
    s = 0
    p_index = 0
    n_index = 0
    index = 0
    singleuser = []
    alluser = []
    usrdata = ''
    itemname = ''
    comments_pos = ''
    comments_neg = ''
    __abool = 0

    while (i < srclength):
        line = srcline[i]
        print i
        #if( i*1000 % srclength < 100 ):
        #    print float(i)/float(srclength)
        i += 1
        if ( s == 0):
            itemname = line.rstrip('\n')
            s += 1
            continue

        if ( s == 1):
            t = line.rstrip('\n')
            userdata = (t.split(' '))[1]
            s += 1
            continue

        s += 1
        if (line == '##\n' or line == '##'):
            #insert comment
            #insert
            #print comments
            sq.insert_item_comment_2(_dbcn,_cur,'comment2',userdata,itemname,
                                   comments_pos,comments_neg)
            comments_pos = ''
            comments_neg = ''
            s = 0
            index = 0
            continue
        
        line = line_div(line)
        tt = line
        '''if(comments != ''):
            comments = comments + ';' + line_del_other(line)
        else:
            comments = line_del_other(line)'''

        r = sp.sentence(line)
        w = sprocess(r)
        #print w
        if (w == []):
            index += 1
            continue
        for line in w:
            __abool += line[1]
            __bool = 1
            if(line[1] > 0):
                __bool = 0
            elif (line[1] < 0):
                __bool = 1
            else:
                continue

            sq.insert_comment_attr(_dbcn,_cur,'com_com',i,line[0],userdata,index,__bool)
        line = tt
        if(__abool > 0):
            if(comments_pos != ''):
                comments_pos = comments_pos + ';' + line_del_other(line)
            else:
                comments_pos = line_del_other(line)
        if(__abool < 0):
            if(comments_neg != ''):
                comments_neg = comments_neg + ';' + line_del_other(line)
            else:
                comments_neg = line_del_other(line)
        __abool = 0
        index  += 1
        
dc = sq.dbstart('sentiment')
cur = sq.cursor(dc)
sq.clear_table(dc,cur,'comment2')
sq.clear_table(dc,cur,'com_com')
#sq.clear_table(dc,cur,'attr')
#sq.clear_table(dc,cur,'attr_index')
senprocess('pr.txt',dc,cur)
sq.dbstop(dc,cur)
