# -*- coding: utf-8 -*-

#this is the ar.py
#this file is to calculate the result

import sp
import ts
import fp
import types

def wcompare(_src,_det):
	return sp.wcompare(_src,_det)

class other_detail(object):
	def __init__(self,name):
		super(other_detail,self).__init__()
		self.name = name
		self.count = 0
		self.list = []
		
	def inc(self):
		self.count += 1
		
	def addword(self,name,sent):
		self.inc()
		if(sent == 0):
			return 0
		__list__ = self.list
		r = []
		for line in __list__:
			if(line[0] == name or wcompare(line[0],name)):
				#print line[0],name
				line[1] += sent
				return
		self.list.append([name,sent])
		
	def get_name(self):
		return self.name
		
	def __print__(self):
		print self.name,self.count
		for line in self.list:
			print '[',line[0],line[1],']',
		print ''

	'''def addname(self, name,other_name,sent):
		li = self.list
		for line in li:
			if(line.get_name() == name):
				line.addname(other_name,sent)
				return
		oth = other_detail(other_name)
		oth.addword(other_name,sent)
		self.list.append(oth)'''
		
class item(object):
	'''This is class item,
	it will record item'''
	def __init__(self,name):
		super(item, self).__init__()
		self.name = name
		self.feature = []
		self.positive = []
		self.negative = []
		self.comment = []
		self.usercount = 0
		
	def cal(self):
		if(self.usercount < 10):
			return '<10'
		li = ''
		n_times = self.usercount
		n = n_times/10
		
		feature_list = self.feature
		print '######',self.name,self.usercount
		for line in feature_list:
			if (line.get_times() > n):
				f = float(line.get_times())/n_times
				if(line.get_label() != ''):
					li = li + line.get_label() + '('+str('%.2f' %f)+')'+';'
				print line.get_label()
				line.print_feature()
		return li
		
		
	def set_feature(self,feature_list):
		self.feature = feature_list
		
	def insert_feature(self,feature):
		self.feature.append(feature)
		
	def insert_positive(self,positive):
		self.feature.append(positive)
		
	def insert_negative(self,negative):
		self.feature.append(negative)
		
	def insert_comment(self,comment):
		self.feature.append(comment)
		
	def set_usercount(self, num):
		self.usercount = num
		
	def get_name(self):
		return self.name
	
#use for test
	def print_item():
		print self.name
		self.feature.print_feature()
		ts._print(self.positive)
		ts._print(self.positive)
		ts._print(self.positive)
		
	def get_count(self):
		return self.usercount
	
	
def insert_item(item_list,_item):
	item_list.append(_item)
	
class feature(object):
	"""class feature"""
	def __init__(self,name):
		super(feature, self).__init__()
		self.label = name
		self.mainlist = []
		self.list = []
		self.times = 0

	def get_label(self):
		return self.label

	def times_inc(self):
		self.times += 1

	def get_times(self):
		return self.times

	def insert(self,rlist):
			
		r1 = rlist[0]
		#if(r1 == ''):
		#	self.insert_main_list(rlist)
		#	return
		self.insert_list(rlist)
		self.times_inc()
		
	def get_all_data(self):
		#we use this function for test
		print 'name:' + self.label
		mainlist = self.mainlist
		for line in mainlist:
			print line
		__list__ = self.list 
		for line in __list__:
			print line

	def insert_main_list(self,rlist):
		#no other word
		#adv
			
		r0 = rlist[2][0]
		#adv sent
		r1 = rlist[2][1]
		#word name
		r2 = rlist[3][0]
		#word sent
		r3 = rlist[3][2] * r1
		rl = self.mainlist

		item = []
		for line in rl:
			if(line[0] == r2 or wcompare(line[0],r2)):
				line[1] = line[1] + r3
				line[2] = line[2] + 1 
				return
		if (item == []):
			item = [r2,r3,0]
			rl.append(item)

	def insert_list(self,rlist):
		#other word
		#
		r = rlist[0]
		r0 = rlist[1]
		#adv_sent
		r1 = rlist[2][1]
		#sent_word
		r2 = rlist[3][0]
		#sent
		r3 = rlist[3][2] * r1

		rl = self.list
		for line in rl:
			if(line.get_name() == r0):
				line.addword(r2,r3)
				return
		new_detail = other_detail(r0)
		new_detail.addword(r2,r3)
		rl.append(new_detail)

		'''item = []
		length = len(rl)
		for line in rl:
			i = 2
			length = len(line)
			while(i < length):
				li = line[i]
				i += 1
				if (li[0] == r2 or wcompare(li[0],r2)):
					lines = li[2]
					item = lines
					for lin in lines:
						if (lin[0] == r2):
							lin[1] = lin[1] + r3
							lin[2] = lin[2] + 1
							li[1] = li[1] + 1
							return

		if (item != []):
			item.append([r2,r3,0])
		else:
			t = [r1,0,[[r2,r3,0]]]
			rl.append(t)'''
			
	def print_feature(self):
		if(self.times < 5):
			return
		print 'feature:',self.label,self.times,len(self.list)
		#ts._print(self.mainlist)
		for line in self.list:
			line.__print__()
		
			
def single_feature_ar(feature_list,user_comments):
	line = user_comments
	r0 = line[0]	#label
	r1 = line[1]	#other word
	r2 = line[2][0]	#adv
	r3 = line[2][1]	#sent
	r4 = line[3][0]	#sent_word
	r5 = line[3][1]	#word attr
	r6 = line[3][2]	#sent

	if(r4 == ''):
		return None
			
	arres = None
			
	for ln in feature_list:
		if(r0 == ln.get_label() or wcompare(r0,ln.get_label())):
			arres = ln
			break
		
	if(arres == None):
		new_feature = feature(r0)
		
		new_feature.insert(line)
		feature_list.append(new_feature)
	else:
		arres.insert(line)
		
	#return new_feature 

def arprocess(sl,filename):

	length = len(sl)
	usercount = 0
	i = 0
	itemname = ''
	usrname = ''
	tmp1 = 0
	allist = []
	single_item = ''
	_item = None
	item_list = []
	#print sl
	while (i < length):
		#print length,i,len(sl)
		line = sl[i]
		if (type(line) == types.StringType):
			line = line.rstrip('\n')
			line = line.lstrip(' ')
			if (line == '##'):
				#print 's',
				usercount += 1
				i += 1
				continue
			if(tmp1 == 0):
				itemname = line
				if(itemname != single_item):
					if(_item != None):
						_item.set_usercount(usercount)
						item_list.append(_item)
						#for line in allist:
						#	line.print_feature()
						allist = []
					usercount = 0
					_item = item(itemname)
					_item.set_feature(allist)
					single_item = itemname
				tmp1 = 1
				i += 1
				continue
			if(tmp1 == 1):
				usrname = line
				tmp1 = 0
				i += 1
				continue
		if (type(line) == types.ListType):
			single_feature_ar(allist,line)
			
		i += 1
	_item.set_usercount(usercount)
	item_list.append(_item)
	tm = ''
	for __item in item_list:
		tm = tm + __item.get_name() + ':'+__item.cal() + '\n'
	
	fp.writefile('ss',tm)
	return item_list
	#for line in allist:
		#line.print_feature()
	
def old():
	predict = {}
	#add  item to the dictionary
	for line in sl:
		sp.senlist(line,predict)
	#
	result = []

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
		
		while(i < al):
			lines = ''
			t2 = t[i]
			t3 = ' ' + t2[0] + ' '+ t2[1][0] + ' ' + str(t2[2])+' '+ str(t2[3])	
			lines += t3
			lines += '\n'
			
			i += 1

	return result

def saveoutfile(r,filename):
	rl = ''
	for line in r:
		rl = rl + line[0] + '\n'
		rl = rl + line[1] + '\n'
		rl = rl + line[2] + '\n'
		rl = rl + line[3] + '\n'
		rl = rl + line[4] + '\n'

	fp.writefile(filename,rl)