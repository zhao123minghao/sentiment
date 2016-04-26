#!/usr/bin/env python
# -*- coding: utf-8 -*-

#this is main.py
#this file contains the function main()

import time
import sys
import ui
import mainprocess


def main():
	argv = sys.argv

	select = ui.user_interface(argv)

	predfile = ''
	srfile = ''
	srlist = []
	result = ''

	starttime = 0

	system_data = mainprocess.getsystemdata() 

	if(select > 0):

		#first step
		if(select < 2):
			prefile = ui.pre_ui()
			starttime = time.time()
			predfile = mainprocess.preprocess(prefile)
		#second step
		if(select < 3):
			senfile = ui.senpro_ui(predfile)
			if(starttime == 0):
				starttime = time.time()
			srlist = mainprocess.sen_pro(senfile)
			
		#third step
		if(select < 4):
			srfile = ui.collect_ui(srlist)
			if(starttime == 0):
				starttime = time.time()
			resfile = mainprocess.getresult(srfile,srlist)
			mainprocess.restodb(resfile)
			
		#all step with argv
	if(select < 0):
		if(starttime == 0):
			starttime = time.time()
		r = mainprocess.argcprocess(argv)
		mainprocess.allprocess(r)

	endtime = time.time()
	execute_time = endtime - starttime
	print 'Time lasts for',execute_time,'s'

def process():
	if(mainprocess.is_first_use()):
		#try to init when first use
		mainprocess.first_use()
			
	main()
