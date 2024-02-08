# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 12:15:48 2024

@author: yatin
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 08:03:39 2024

@author: yatin
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 15:36:14 2024

@author: yatin
"""

import ply.lex as lex
import ply.yacc as yacc

###DEFINING TOKENS###
tokens = ('BEGINTABLE', 
'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW',
'OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF',
'CONTENT', 'OPENDATA', 'CLOSEDATA' ,'OPENSPAN',
'CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE', 'OPENP','CLOSEP')
t_ignore = '\t'

###############Tokenizer Rules################
def t_BEGINTABLE(t):
     r'<h3><span.class="mw-headline".id="1_January">1.January</span>'
     return t

def t_OPENTABLE(t):
    r'<tbody[^>]*>'
    return t

def t_CLOSETABLE(t):
    r'</tbody[^>]*>'
    return t

def t_OPENP(t):
    r'<p[^>]*>'
    return t

def t_CLOSEP(t):
    r'</p[^>]*>'
    return t



def t_OPENROW(t):
    r'<tr[^>]*>'
    return t

def t_CLOSEROW(t):
    r'</tr[^>]*>'
    return t

def t_OPENHEADER(t):
    r'<th[^>]*>'
    return t

def t_CLOSEHEADER(t):
    r'</th[^>]*>'
    return t

def t_OPENHREF(t):
    r'<a[^>]*>'
    return t

def t_CLOSEHREF(t):
    r'</a[^>]*>'
    return t

def t_OPENDATA(t):
    r'<td[^>]*>'
    return t

def t_CLOSEDATA(t):
    r'</td[^>]*>'
    return t

def t_CONTENT(t):
    r'[A-Za-z0-9,]+'
    return t

def t_OPENDIV(t):
    r'<div[^>]*>'

def t_CLOSEDIV(t):
    r'</div[^>]*>'

def t_OPENSTYLE(t):
    r'<style[^>]*>'

def t_CLOSESTYLE(t):
    r'</style[^>]*>'

def t_OPENSPAN(t):
    r'<span[^>]*>'

def t_CLOSESPAN(t):
    r'</span[^>]*>'

def t_GARBAGE(t):
    r'<[^>]*>'

def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
											#GRAMMAR RULES
def p_start(p):
    '''start : table'''
    p[0] = p[1]
    

def p_skiptag(p):
    '''skiptag : CONTENT skiptag empty
               | OPENHREF skiptag
               | CLOSEHREF skiptag
               | empty'''
    if len(p) == 4:
            print(p[1])

def p_table(p):
    '''table : BEGINTABLE skiptag OPENP skiptag CLOSEP'''





def p_empty(p):
    '''empty :'''
    pass

def p_content(p):
    '''content : CONTENT
               | empty'''
    p[0] = p[1]

def p_error(p):
    pass

#########DRIVER FUNCTION#######
def main():
    file_obj= open('jan2020.html','r',encoding="utf-8")
    data=file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    for tok in lexer:
        print(tok)
    parser = yacc.yacc()
    def extract_data(parser):
        
        result = parser.parse(data)
        print("Result:", result)
    # Menu loop
    while True:
        print("\nMenu:")
        print("1. Extract Data")
        print("2. Quit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            extract_data(parser)
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
            
    

    
    file_obj.close()
if __name__ == '__main__':
        main()
    



