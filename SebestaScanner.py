# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 18:21:51 2014

@author: VenkataPradeep
SebestaScanner for lexical and syntax analysis
"""
import sys

# global variables
global LETTER
global DIGIT
global UNKNOWN
global EOF

global INT_LIT
global IDENT
global ASSIGN_OP
global ADD_OP
global SUB_OP
global MULT_OP
global DIV_OP
global LEFT_PAREN
global RIGHT_PAREN

# getchar() - a function to get nextchar of the input and determine its character class
def getchar():
    globals()["nextchar"] = in_fp.read(1)   # to read characters from the file    
    if globals()["nextchar"] != "":             # condition to check for EOF
        if globals()["nextchar"].isalpha():     # condition to check if nextchar is alphabet
            globals()["charclass"] = LETTER
        elif globals()["nextchar"].isdigit():   # condition to check if nextchar is digit
            globals()["charclass"] = DIGIT
        else:
            globals()["charclass"] = UNKNOWN
    else:
        globals()["charclass"] = EOF

# lex() - a simple lexical analyser for arithmetic expressions
def lex():
    globals()["lexlen"] = 0
    getnonblank()
    if globals()["charclass"] == LETTER:
        addchar()
        getchar()
        while ((globals()["charclass"] == LETTER) or (globals()["charclass"] == DIGIT)):
            addchar()
            getchar()
        globals()["nexttoken"] = IDENT
    elif globals()["charclass"] == DIGIT:
        addchar()
        getchar()
        while ((globals()["charclass"] == LETTER) or (globals()["charclass"] == DIGIT)):
            addchar()
            getchar()
        globals()["nexttoken"] = INT_LIT
    elif globals()["charclass"] == UNKNOWN:
        lookup(globals()["nextchar"])
        getchar()
    else:
        globals()["nexttoken"] = EOF
        globals()["lexeme"] = "EOF"
    print "Next Token is: ", globals()["nexttoken"] , ", Next Lexeme is: ", globals()["lexeme"]
    globals()["lexeme"] = ""
    return globals()["nexttoken"] 

# addchar() - Function to add nextchar to lexeme
def addchar():
    global lexlen
    if globals()["lexlen"] <= 98:
        globals()["lexeme"] += globals()["nextchar"]
        globals()["lexlen"] += 1
    else:
        print "Error - lexeme is too long \n"

#getnonblank() - a function to call getchar() until it returns a non-white space character
def getnonblank():
    while globals()["nextchar"].isspace():
        getchar()

# lookup() - a function to lookup operators and parantheses and return the token
def lookup(ch):
    if ch == "(":
        addchar()
        globals()["nexttoken"] = LEFT_PAREN
    elif ch == ")":
        addchar()
        globals()["nexttoken"] = RIGHT_PAREN
    elif ch == "+":
        addchar()
        globals()["nexttoken"] = ADD_OP
    elif ch == "-":
        addchar()
        globals()["nexttoken"] = SUB_OP
    elif ch == "*":
        addchar()
        globals()["nexttoken"] = MULT_OP
    elif ch == "/":
        addchar()
        globals()["nexttoken"] = DIV_OP
    else:
        addchar()
        globals()["nexttoken"] = EOF
    return globals()["nexttoken"]


# main function    
if __name__ == '__main__':
    
    # character classes
    LETTER = 0
    DIGIT = 1
    UNKNOWN = 99
    EOF = -1
    
    lexeme = ""    
    
    # token codes
    INT_LIT = 10
    IDENT = 11
    ASSIGN_OP = 20
    ADD_OP = 21
    SUB_OP = 22
    MULT_OP = 23
    DIV_OP = 24
    LEFT_PAREN = 25
    RIGHT_PAREN = 26
    
    parse = 0
    try:
        if len(sys.argv) == 2:              # to check whether input file is passed from command line
            in_fp = open(sys.argv[1],'r')
            parse = 1
        elif len(sys.argv) == 1:            # default input file in case of no input from command line
            in_fp = open('C:\\Users\\VenkataPradeep\\Desktop\\front.txt','r')
            parse = 1
        else:
            print "Usage:\n Python front.py[file-to-parse(optional,default = C:\\Users\\VenkataPradeep\\Desktop\\front.txt)]"
    except IOError:
        if len(sys.argv) == 2:
            print "File not found", sys.argv[1]
        else:
            print "File not found: front.txt"
    except:
            print "Expected error: ", sys.exc_info()[0]
            raise
    
    if parse:
        getchar()
        lex()
        while globals()["nexttoken"] != EOF:            # loops until token becomes -1 i.e end of file
            lex()
        in_fp.close()       # close the file








        
        
        
        
    
            
