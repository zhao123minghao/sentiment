# -*- coding: utf-8 -*-

import sq
import fp

conn = sq.dbstart('sentiment')
cur = sq.cursor(conn)

nfile = fp.readfile('/home/zhao/dict/a.txt')
wordattr = 'adj'

length = len(nfile)

def create_words(wl,start,end):
	i = start
	while i < end:
		line = wl[i]
		tmp = line.split('\t')
		
		s = raw_input(str(i)+' '+tmp[0] + '\t')
		if (s == '-'):
			s = -1
		if (s == ''):
			s = 1
		sen = float(s)
		sq.insert_sentiment_word(conn,cur,'sent_word',tmp[0],wordattr,sen,'')
		i += 1

#sq.insert_user_data(conn,cur,'sent_user','111111','','','')
#create_words(nfile,401,length)
#print sq.get_sentiment_word(conn,cur,'sent_word','齐全')
print sq.get_user_data(conn,cur,'sent_userd','aaaa')


sq.dbstop(conn,cur)
