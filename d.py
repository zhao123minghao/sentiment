# -*- coding: utf-8 -*- 

file1 = open('/home/zhao/项目/python/sentiment/a.txt','r')
lines = file1.readlines()

wordattr = []
wordexample = []

file2 = open('ns.txt','w')
for line in lines:
	tmp = line.rstrip('\n')
	strs = tmp.split(' ')
	for strw in strs:
		tmp2 = strw.split('/')
		#print tmp2 
		if(len(tmp2) == 2):
			x = tmp2[1]
		else:
			x = '0'
		#if(x == 'a' or x == 'ad'):
		if(x == 'n'):
		#if( x == 'v' or x == 'vn' or x == 'vd'):
			if(tmp2[0] not in wordexample):
				wordexample.append(tmp2[0])
				file2.writelines(tmp2[0]+'\n')
				#print tmp2[0]
file1.close()
file2.close()
