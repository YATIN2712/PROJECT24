# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 11:51:42 2024

@author: yatin
"""

import os
import ply.lex as lex
import ply.yacc as yacc
from urllib.request import Request, urlopen
req = Request('https://en.wikipedia.org/wiki/2020_Summer_Olympics',headers ={'User-Agent':'Google/1.0'})
webpage = urlopen(req).read()
mydata = webpage.decode("utf8")
f=open('webpage.html','w',encoding="utf-8")
f.write(mydata)
f.close