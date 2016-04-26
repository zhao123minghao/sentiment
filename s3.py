#!/usr/bin/env python

import sp
import sq
import fp
import time

sets = []

def add_sets(userid,feature):
    for line in sets:
        if(line[0] == userid and line[1] == feature):
            return False
    sets.append([userid,feature])
    return True

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
    comments = ''
    comments_pos = ''
    comments_neg = ''

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
            sq.insert_item_comment_2(_dbcn,_cur,'comment3',userdata,itemname,
                                   comments,comments_pos,comments_neg)
            comments = ''
            comments_pos = ''
            comments_neg = ''
            s = 0
            index = 0
            p_index = 0
            n_index = 0
            continue
        
        line = line_div(line)
        tt = line
        if(comments != ''):
            comments = comments + ';' + line_del_other(line)
        else:
            comments = line_del_other(line)

        r = sp.sentence(line)
        w = sprocess(r)
        #print w
        if (w == []):
            index += 1
            continue
        for line in w:
            __bool = 1
            
            if(line[1] > 0):
                __bool = 0
                p_index  += 1
                if(add_sets(userdata,line[0])):
                    sq.insert_comment_attr(_dbcn,_cur,'com_com',i,line[0],userdata,p_index,__bool)
                line = tt
                if(comments_pos != ''):
                    comments_pos = comments_pos + ';' + line_del_other(line)
                else:
                    comments_pos = line_del_other(line)
            elif (line[1] < 0):
                __bool = 1
                n_index += 1
                if(add_sets(userdata,line[0])):
                    sq.insert_comment_attr(_dbcn,_cur,'com_com',i,line[0],userdata,n_index,__bool)
                line = tt
                if(comments_neg != ''):
                    comments_neg = comments_neg + ';' + line_del_other(line)
                else:
                    comments_neg = line_del_other(line)
            else:
                continue
        
        index  += 1
starttime = time.time()
dc = sq.dbstart('sentiment')
cur = sq.cursor(dc)
sq.clear_table(dc,cur,'comment3')
sq.clear_table(dc,cur,'com_com')
#sq.clear_table(dc,cur,'attr')
#sq.clear_table(dc,cur,'attr_index')
senprocess('p.txt',dc,cur)
sq.dbstop(dc,cur)
endtime = time.time()
execute_time = endtime - starttime
print 'Time lasts for',execute_time,'s'

