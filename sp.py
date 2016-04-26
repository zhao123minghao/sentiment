# -*- coding: utf-8 -*-

#this file is sp.py
#important
#by this file,we can get the main keyword,minor keyword,sent word
#and the sent of the word

import re
import string
import wp
import fp
import types
import ts
import copy

endict = {}
ndict = wp.dictstart('/home/zhao/data/d/n.txt')
jdict = wp.dictstart('/home/zhao/data/d/adj.txt')
ddict = wp.dictstart('/home/zhao/data/d/adv.txt')
vdict = wp.dictstart('/home/zhao/data/d/v.txt')
nd = wp.ndictstart('/home/zhao/data/d/nd.txt')
addtiondict = []
#print ddict

def cutlongsen(_list):
	return []

def sentence(_list):
	rlist = []
	subindex = []
	listlen = len(_list)
	#print _list
	i = 1
	for line in _list:
		#print type(line)
		if(line[1] == ',' or line[1] == '\xEF\xBC\x8C' or line[1] == '\xA3\xAC'):
			subindex.append(i)
		i += 1
	s = len(subindex)
	if( s == 0):
		subindex.append(listlen)
	t = subsentence(_list[0:subindex[0]],1)
	if(t != [] and t != None):
		rlist.append(t)
	
	i = 1
	while(i < s - 1):
		#print s,i,subindex
		t = subsentence(_list[subindex[i]:subindex[i+1]],2)
		if(t != [] and t != None and (t[2][0]!='' or t[3][0] != '')):
			rlist.append(t)
		i += 1
	if(i < s and subindex[i] != listlen-1):
		t = subsentence(_list[subindex[i]:listlen-1],2)
		if(t != [] and t != None and (t[2][0]!='' or t[3][0] != '')):
			rlist.append(t)
	last = ''
	for line in rlist:
		if(line[0] == ''):
			line[0] = last
		else:
			last = line[0]
	
	return rlist

## return = [main_noun,[noun],(adv,grade),(sentiment word,attr,grade)]
def subsentence(_list,attr):
	if(_list == []):
		return None
	#print _list
	propert = 0  #for attr 'p'
	rlist = []
	
	length = len(_list)
	nflocation = length
	vflocation = length
	other_tmp = ''
	other_flag = 0
	nf = ''
	vf = ''
	ntimes = 1
	nc = 0
	
	sen = 0
	index = 0
	
	n_other = ''
	adv_d = ('',1)
	sen_w = ('','a',1)
	a_d = []
	v_n = ''
	a_n = ''
	
	missword = 0
	length = len(_list)
	#print _list
	while (index < length):
		tt = _list[index]
		line = copy.deepcopy(tt)

		lastline = wp.getlastline(_list,index)
		nextline = wp.getnextline(_list,index)
		wattr = line[2]
	#word noun process
		if(wattr == 'n' or wattr == 'nz' or wattr == 'ng'):
			#print line[2]
			if(nf == '' and nflocation == length and propert == 0):
				line[1] = wp.ndictsearch(line[1],nd)
				if(line[1] != ''):
					nf = line[1]
					nflocation = line[0]
			#other word
			if(nf != '' and propert == 0 \
				and nflocation < vflocation \
				and other_flag == 0 \
				and line[0] != nflocation):
				other_tmp = line[1]
				other_flag = 1
			elif(nf != '' and propert == 0 \
				and nflocation < vflocation \
				and other_flag != 0 \
				and line[0] != nflocation):
				if(nc == index-1):
				##
					ntimes += 1
					nc += 1
					other_flag += 1
					other_tmp += line[1]
			else:
				pass
			
			sen = wp.nounprocess(line[1],ndict)
			if(sen == 0):
			   sen = wp.verbprocess(line[1],vdict)
			if(sen != 0):
				if(sen_w[0] == ''):
					sen_w = (line[1],'n',sen)
				else:
					sen_w = (sen_w[0],sen_w[1],sen_w[2]*sen)
				#rlist.append((line[2],'n',sen))
	#word verb
		if(wattr == 'v'or wattr == 'vn'):
			ntimes = 0
			if(wattr == 'vn'):
				line[1] = wp.ndictsearch(line[1],nd)
				if(line[1] != ''):
					v_n = line[1]
					#print 'vn:yes'
			if(vf=='' and vflocation == length ):
				vf = line[1]
				vflocation = line[0]
				if(nflocation > vflocation and nflocation != length):
					#print vf,nf
					nf = ''
					nflocation = length
					
			sen = wp.verbprocess(line[1],vdict)
			if(sen != 0):
				if(sen_w[0] == ''):
					sen_w = (line[1],'v',sen)
				else:
					sen_w = (sen_w[0],sen_w[1],sen_w[2]*sen)

	#word adj
		if(wattr == 'a' or wattr == 'an'):
			ntimes = 0
			if(wattr == 'an'):
				line[1] = wp.ndictsearch(line[1],nd)
				if(line[1] != ''):
					a_n = line[1]
			sen = wp.adjprocess(line[1],jdict)
			#print sen
			if(sen != 0.0):
				if(sen_w[0] == ''):
					sen_w = (line[1],'a',sen)
				else:
					#print sen_w[0],line[2]
					if(sen_w[1] != 'a'):
						sen_w = (line[1],'a',sen* sen_w[2])
					else:
						sen_w = (sen_w[0],sen_w[1],sen_w[2]*sen)
					print sen_w[0]
			#rlist.append((line[1],'a',sen))
	#word is adv or adj we need to have a decision
		if(wattr == 'ad'):
			sen = wp.adjprocess(line[1],jdict)
			if(sen == 0.0):
				sen = wp.advprocess(line[1],ddict)
				if(sen != 0.0):
					a_d = [line[1],'ad',sen]
			else:
				a_d = [line[1],'ad',sen]
	#word adv
		if(wattr == 'd'):
			ntimes = 0
			if(sen_w[0] == ''):
				sen = wp.advprocess(line[1],ddict)
				if(sen == 0):
					sen = 1
				adv_d = (line[1],sen)
			#rlist.append((line[1],'d',sen))
	#word passivity
		if(wattr == 'p'):
			ntimes = 0
			ps = wp.pprocess(line[1],jdict)
			if(ps == 1):
				# 'ba' ;cut the noun and verb
				nf = ''
				vf = ''
				nflocation = length
				vflocation = length
				rlist = []
			elif(ps == 2):
				propert = 10 #'bei';
			else:
				ki = 0 #ki is temp
	#word in english
		if(wattr == 'en'):
			ntimes = 0
			wp.enprocess(line[0],endict)
			#special sentences
	#word uj 'de'
		if(wattr == 'uj'):
			ntimes += 1
			nc += 1
			
		if(wattr == 'f'):
			nflocation = length
			vflocation = length
			other_tmp = ''
			other_flag = 0
			nf = ''
			vf = ''
			ntimes = 1
			nc = 0
			
			n_other = ''
			adv_d = ('',1)
			sen_w = ('','a',1)
			a_d = []
			v_n = ''
			a_n = ''
	
	#word we don't know
		if(wattr == '@'):
			ntimes = 0
			missword += 1

		if(missword >= 3):
			return []
		index += 1
		sen = 0
		
	if(a_d != []):
		if(sen_w[0] == ''):
			sen_w = (a_d[0],'a',a_d[2])
		if(adv_d[0] == ''):
			adv_d = (a_d[0],a_d[2])
	if(nf == ''):
		if(v_n != ''):
			nf = v_n
			#print 'vn:yes'
		elif(a_n != ''):
			nf = a_n
		else:
			pass
	if(sen_w[0] == ''):
		return None

	n_other = other_tmp
	rlist.append(nf)
	rlist.append(n_other)
	rlist.append(adv_d)
	rlist.append(sen_w)

	return rlist

def wcompare(_src,_det):
	i = 0
	if(_src == _det):
		return True
	for word1 in _src:
		for word2 in _det:
			if(word1 == word2):
				i += 1
	#print i
	if( (len(_src) == 3 or len(_det) == 3) and i == 3):
		return True	
	if( i > 3 and i% 3 == 0):
		return True
	return False

#_s = [n,adj,sen]
#list[i] = [n,adj,sen,count]
def addsenlist(_list,_s):
	if(_s == []):
		return None
	nl = -1
	al = -1
	count = 1
	_all = len(_list)
	while( count < _all):
		line = _list[count]
		con1 = wcompare(line[0],_s[0])
		con2 = wcompare(line[1],_s[1])
		if(con1 and con2):
			nl = al = count
			break
		#else if(con)
		count += 1
	if( nl == al and nl != -1):
		_list[nl][3] += 1
		_list[nl][2] += _s[2]
	else:
		#print _s[0],_s[1]
		_list.append([_s[0],_s[1],_s[2],1])
			#_list.append()

def senlist(_list,_dict):
	if(_list == [] or _list == None):
		return None
	#print _list
	for sublist in _list:
		t1 = sublist[0]
		#if(t1 != ''):
		if(t1 not in _dict):
			#print _dict
			pre = [1]
			_dict[t1] = pre
		else:
			_dict[t1][0] += 1
			pre = _dict[t1]
		t2 = sublist[1]
		t3 = sublist[2]
		t4 = sublist[3]
		sen = t3[1] * t4[2]
		addsenlist(pre,[t2,t4,sen])
	# print sen

def single_user(senslist):
	sens = []
	for line in senslist:
		sens += sentence(line)
	return sens

def lineprocess(wordlist):
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
		
def senprocess(infile,outfile):
	srcline = fp.readfile(infile)
	srclength = len(srcline)

	i = 0
	s = 0
	singleuser = []
	alluser = []
	usrdata = ''
	itemname = ''

	while (i < srclength):
		line = srcline[i]
		#if( i*1000 % srclength < 100 ):
		#	print float(i)/float(srclength)
		i += 1
		if ( s == 0):
			userdata = line
			s += 1
			continue

		if ( s == 1):
			itemname = line
			s += 1
			continue

		s += 1

		if (line == '##\n'):
			alluser.append(userdata )#+ '\n')
			alluser.append(itemname )#+ '\n')
			alluser += single_user(singleuser)
			alluser.append('##\n')
			singleuser = []
			s = 0
			#break

		singleuser.append(lineprocess(line))

	##--test--##
	#ts._print(alluser)
	output_test_file(outfile,alluser)
	return alluser
	#here we not just for test
	#print alluser
			

def before():
	str1 = fp.readfile(infile)
	predict = {}
	for line in str1:
		tmp1 = line.rstrip('\x0d\n')
		tmp2 = tmp1.rstrip(';\x0d/un')
		tmp3 = tmp2.split(' ')
		num = 0
		sublist = []
		for substr in tmp3:
			#print substr
			tmp4 = substr.split('/')
			if(len(tmp4)!=1):
				sublist.append((num,tmp4[0],tmp4[1]))
			num += 1
		t =  sentence(sublist)
		##
		senlist(t,predict)
	##
	pfile = open('p.txt','w')
	for line in predict:
		lines = ''
		lines = lines + line + ' '
		t = predict[line]
		t1 = t[0]
		if(t1 < 10):
			continue
		al = len(t)
		i = 1
		lines += str(t1)
		pfile.writelines(lines)
		while(i < al):
			lines = ''
			t2 = t[i]
			t3 = ' ' + t2[0] + ' '+ t2[1][0] + ' ' + str(t2[2])+' '+ str(t2[3])	
			lines += t3
			lines += '\n'
			pfile.writelines(lines)
			i += 1
	pfile.close()
#fp.writefile('p.txt', lines)

def addtion_dict(dictfile):
	if(dictfile == ''):
		return
	addtion_dict = wp.dictstart(dictfile)

def output_test_file(filename,rlist):
	out = ''
	for line in rlist:
		#print line
		if(type(line) == types.StringType):
			out += line
			continue

		out = out + line[0] + '\t'
		out = out + line[1] + '\t'
		out = out + line[2][0] + '\t'
		out = out + str(line[2][1]) + '\t'
		out = out + line[3][0] + '\t'
		out = out + line[3][1] + '\t'
		out = out + str(line[3][2])
		out += '\n'

	fp.writefile(filename,out)
	#print filename

def get_word_leibie(word,attr):
	if(attr == 'n'):
		t = wp.wordp(word,ndict)
	elif(attr == 'v'):
		t = wp.wordp(word,vdict)
	elif(attr == 'adj'):
		t = wp.wordp(word,jdict)
	elif(attr == 'adv'):
		t = wp.wordp(word,ddict)
	else:
		return ''
	return t