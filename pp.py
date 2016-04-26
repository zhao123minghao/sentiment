# -*- coding: utf-8 -*-

import fp
import os

sendivs = ['.' , '?' , '!' , ';' , ':' , '~' , '`' , '  ' , '\t',
	'\xE3\x80\x82','\xEF\xBC\x9F','\xEF\xBC\x81','\xEF\xBC\x9B','\xEF\xBC\x9A','\xEF\xBD\x9E',
	'\xA1\xA3','\xA3\xBF','\xA3\xA1','\xA3\xBB','\xA3\xBA','\xA1\xAB',
	'<br/>']


def sensplit(src,sl):
	result = []
	for line in sl:
		src=src.replace(line,'##')
	src = src.replace(' ',',')
	result = src.split('##')
	return result

def senlist(sl):
	length = len(sl)
	i = 0
	while (i < length):
		sl[i] = sl[i] .lstrip(' ')+ '\n'
		i += 1
	return sl

def cutemptyline(sl):
	length = len(sl)
	i = 0
	while (i < length):
		if(sl[i] == '\n'):
			del sl[i]
			length -= 1
			#print 'l'
		else:
			i += 1
	return sl

def preprocess(symlist):
	result = []
	message = []
	tmp = []
	for line in symlist:
		lines = line.split('\t')
		length = len(lines)
		if(length > 2):
			i = 2
	#_filename = '/home/zhao/data/t/'+lines[0]+'.txt'
			message.append(lines[0])
			#print lines[0]
			message.append(lines[1])

			while( i < length):
				sens = lines[i]
				i += 1
				sens = sens.rstrip('\r\n')
				sens = sensplit(sens,sendivs)
				senlist(sens)

				tmp += sens

			tmp.append("##\n")

	fp.writefile('tmp.txt',tmp)

	if(os.path.isfile('tmp2.txt')):
		os.remove('tmp2.txt')

	divword('tmp.txt','tmp2.txt')

	tmp2 = fp.readfile('tmp2.txt')

	mlength = len(message)
	tlength = len(tmp2)
	ml = 0
	tl = 0

	#print message
	while (ml < mlength):
		result.append(message[ml].lstrip(' ') + '\n')
		ml += 1
		result.append(message[ml].lstrip(' ') + '\n')
		ml += 1
		while (tl < tlength):
			line = tmp2[tl]
			tl += 1
			if( line == '' or line == '\n' ):
				continue
			if( line == '#/un #/un \n'):
				result.append('##\n')
				break
			result.append(line)

	cutemptyline(result)
	if(os.path.isfile('tmp.txt')):
		os.remove('tmp.txt')
	if(os.path.isfile('tmp2.txt')):
		os.remove('tmp2.txt')

	return result

def divword(inputfile, outputfile):
	cmdline = 'scws -i '+ inputfile + ' -o ' + outputfile  + ''' \
-c utf-8 -A -d /home/zhao/dict/dict_chs_utf8.txt \
-r /usr/local/etc/rules.utf8.ini -N'''
	var = os.popen(cmdline).read()
	return var