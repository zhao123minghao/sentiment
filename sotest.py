# -*- coding: utf-8 -*-

from ctypes import * 
import os

class Scws_t_Pointer(Structure):  
    _fields_ = [("name", c_char * 20), ("age", c_int)]  

scwslib = cdll.LoadLibrary('/usr/local/lib/libscws.so.1.1.0')

scws = scwslib.scws_new()

scwslib.scws_set_charset(scws,'utf-8')
scwslib.scws_set_dict(scws,'utf-8')
scwslib.scws_set_rule(scws,'utf-8')

scwslib.scws_send_text(s, text, strlen(text))

result = scwslib.scws_get_result(scws)

