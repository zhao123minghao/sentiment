# -*- coding: utf-8 -*-

#this file is st.py
#by this file we can get settings file

import fp

def get_settings(set_list):
    settings = []
    for line in set_list:
        line = line.rstrip('\n')
        tmp = line.split(':')
        settings.append([tmp[0],tmp[1]])
    return settings

def test():
    lines = fp.readfile('/home/zhao/.sentiment/settings')
    print get_settings(lines)