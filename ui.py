# -*- coding: utf-8 -*-

#this file is ui.py
#this file is used to setup the ui in the shell

import sys
import os
import types
import getpass


def user_interface(ar):
	argc = len(ar)
	if(argc == 1):
		s_input = raw_input('''\n\t\t1.Start at first step(comment prepare)\n\n\
		2.Start at sencond step(input the data file)\n\n\
		3.Start at third step(collate the result)\n\n\
		\tPlease input your selection:  ''')

		while (s_input != '1' and s_input != '2' and s_input != '3'):
			s_input = raw_input('\n\t\tInput error.Please input again.  ')
		return int(s_input)
	if(argc > 1):
		return -argc

def pre_ui():
	input_file = raw_input('''\n\t\
	Please input a file name:(default:test.txt)''')

	if(input_file == ''):
		return '/home/zhao/data/qq.txt'

	while (not os.path.isfile(input_file)):
		input_file = raw_input('\n\tFile don\'t exit,input again  ')
		
	return input_file

def senpro_ui(filename):
	if(filename != ''):
		return filename

	filename = raw_input('''\n\t\
	Please input a file name:(default:sent_test_b.txt)  ''')

	if(filename == ''):
		return 'sent_test_b.txt'

	while (not os.path.isfile(filename)):
		filename = raw_input('\n\tFile don\'t exit,input again  ')
	return filename

def collect_ui(filename):
	if(type(filename) != types.StringType):
		return ''
	if(filename == ''):
		filename = raw_input('''\n\t\
	Please input a file name or database:(default:database)''')

		while (not os.path.isfile(filename)):
			
			filename = raw_input('''\n\tFile don\'t exit,\
input again,you can choose database  ''')

			if (filename == ''):
				return 'DataBase'
	return filename

def dbset_ui():
	unconnected = True
	print 'we will setup a link to connect data base'
	yn = raw_input('please press N to skip,other key to continue')
	
	if(yn == 'n' or yn == 'N'):
		return None
	
	print ''
	
	while (unconnected):
		
		site = raw_input('Please input your database server address:')

		while (type(port) != types.IntType):
			port = raw_input('port(default:3306)')
			if (port == ''):
				port = 3306
			else:
				try:
					port = int(port)
				except Exception, e:
					print 'Input error:Please input again'
		user = raw_input('user name:')
		passwd = getpass.getpass('password:')
		database = raw_input('DataBase name(default:sentiment<creat>):')
		if(database == ''):
			database = 'sentiment'
		charset = raw_input('charset(default:utf-8):')
		while (charset == ''):
			
			if(charset == ''):
				charset = 'sentiment'
			elif(charset == 'gbk' or charset == 'gb2312' or charset == 'latin'):
				pass
			else:
				print 'we don\'t know or we don\'t support your input:'
				charset = ''

	return [site,str(port),user,passwd,database,charset]
