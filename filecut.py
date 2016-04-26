#!/usr/bin/env python

import fp
flist = fp.readfile('a.txt')
fp.writefile('sent_test_b.txt',flist[:15000])