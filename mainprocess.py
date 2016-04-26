# -*- coding: utf-8 -*-

#this is the mainprocess.py
#this file is to chaieve the the main part

import pp
import fp
import sp
import ar
import sys
import os
import ui
import platform

#maybe I import too many file more than I expected.

def getsystemdata():
	uname = platform.uname()
	plat = uname[0]
	py_main_version = platform._sys_version()[0]
	py_sub_version = platform._sys_version()[1]
	return (plat,py_main_version,py_sub_version)

def preprocess(filename):
	psymlist = fp.readfile(filename)
	psen = pp.preprocess(psymlist)
	fp.writefile('pr.txt',psen)
	return 'pr.txt'

def sen_pro(filename):
	return sp.senprocess(filename,'sent_b.txt')
	
def getresult(filename,slist):
	if(filename != ''):
		sl = fp.readfile(filename)
	else:
		sl = slist
	#print sl 
	ar.arprocess(sl,filename)
	#print 'i'
	return filename

def restodb(filename):
	print filename
	return True

def argcprocess(ar):
	length = len(ar)
	
	i = 1
	inputfile = ''
	outputfile = ''
	dictfile = ''
	DB = False
	_in = 0
	_out = 0
	_d = 0
	j = 1
	_dict = 0

	while(i < length):
		line = ar[i]
		if ( line == '-I'):
			_in += 1
			if(_in > 1):
				print 'invail arguement'
				exit()
			i += 1
			inputfile = ar[i]
			if(not os.path.isfile(inputfile)):
				print 'file don\'t exist'
				exit()


		elif ( line == '-O'):
			_out += 1
			if(_out > 1):
				print 'invail arguement'
				exit()
			i += 1
			outputfile = ar[i]
			if(not os.path.isfile(outputfile)):
				print 'file don\'t exist'
				exit()

		elif (line == '-D'):
			_d += 1
			if(_d > 1):
				print 'invail arguement'
				exit()
			DB = True

		elif ( line == '-j'):
			i += 1
			try:
				j = int(ar[i])
			except Exception, e:
				print 'invail arguement'

		#this dictonary is just sentiment words  dictionary
		elif( line == '-d'):
			_dict += 1
			if(_dict > 1):
				print 'invail arguement'
				exit()
			i += 1
			dictfile = ar[i]
			if(not os.path.isfile(dictfile)):
				print 'file don\'t exist'
				exit()
		elif (line == '-t'):
			i += 1
			testfile = ar[i]
			if(not os.path.isfile(testfile)):
				print '\t\ttest file don\'t exist'
				sys.exit(0)
			predfile = preprocess(testfile)
			srlist = sen_pro(predfile)
			print srlist
			sys.exit(0)
		else:
			if(_in == 0):
				if(os.path.isfile(line)):
					inputfile = line
					_in += 1
				else:
					print 'we dont\'t know ' + line
					exit()

		i += 1
	if(inputfile == ''):
		print 'you need to add a input file by \'-I\''

	if(_out == 0 and _d == 0):
		print '\tno output file selected,we will save it into database'
		DB = True

	if(inputfile == outputfile):
		print '''\tinput file and output file are the same,we \
will overwrite the input file,we don\'t suggest.'''

	return [inputfile,outputfile,DB,j,dictfile]


def allprocess(rlist):
	#cache file would be cleaned automatically
	dbresult = False
	prefile = rlist[0]
	outfile = rlist[1]
	DBuse = rlist[2]
	core_use = rlist[3]
	dictfile = rlist[4]

	predfile = preprocess(prefile)
	srfile = sen_pro(senfile)
	result = getresult(srfile)

	if(DBuse):
		dbresult = restodb(result)

	if(outfile != ''):
		ar.saveoutfile(result,outfile)
	else:
		if (dbresult):
			print 'We can\'t write to your database.'
			ar.saveoutfile(result,'result.txt')
			print 'We have written to \'result.txt\''


def is_first_use():
	usr_home = os.path.expanduser('~')
	sp_folder = usr_home + '/.sentiment'
	if(not os.path.lexists(sp_folder)):
		return True
	sp_settings = sp_folder + '/settings'
	if(not os.path.isfile(sp_settings)):
		return True
	return False

def first_use():
	usr_home = os.path.expanduser('~')
	sp_folder = usr_home + '/.sentiment'
	sp_settings = sp_folder + '/settings'
	if(not os.path.lexists(sp_folder)):
		os.mkdir(sp_folder)
	sp_dbset = sp_folder + '/.dbset'
	if(not os.path.isfile(sp_dbset)):
		db_settings = ui.dbset_ui()
		
	if(db_settings == None):
		db_use = 'no'
	else:
		t = ''
		for line in db_settings:
			t += line
			t += '\t'
			
		fp.writefile(sp_dbset,t)
		db_use = 'yes'
	
	fp.writefile(sp_settings,'database:'+db_use+'\n')
	
	adj_dict_file = sp_folder + '/adj.txt'
	if(os.path.isfile(adj_dict_file)):
		fp.appendfile(sp_settings,'adj_dict:' + adj_dict_file+'\n')
	else:
		fp.appendfile(sp_settings,'adj_dict:' + 'no\n')

	adv_dict_file = sp_folder + '/adv.txt'
	if(os.path.isfile(adv_dict_file)):
		fp.appendfile(sp_settings,'adv_dict:' + adv_dict_file+'\n')
	else:
		fp.appendfile(sp_settings,'adv_dict:' + 'no\n')
		
	n_dict_file = sp_folder + '/n.txt'
	if(os.path.isfile(n_dict_file)):
		fp.appendfile(sp_settings,'noun_dict:' + n_dict_file+'\n')
	else:
		fp.appendfile(sp_settings,'noun_dict:' + 'no\n')
		
	v_dict_file = sp_folder + '/v.txt'
	if(os.path.isfile(v_dict_file)):
		fp.appendfile(sp_settings,'verb_dict:' + v_dict_file+'\n')
	else:
		fp.appendfile(sp_settings,'verb_dict:' + 'no\n')
		
	en_dict_file = sp_folder + '/en.txt'
	if(os.path.isfile(n_dict_file)):
		fp.appendfile(sp_settings,'en_dict:' + n_dict_file+'\n')
	else:
		fp.appendfile(sp_settings,'en_dict:' + 'no\n')