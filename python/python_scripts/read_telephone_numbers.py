#!/usr/bin/python

import sys, re

fileName = sys.argv[1]
print "File name :", fileName


f = open(fileName)
for line in iter(f):
    #print line

    ### REGEX EXPLAINED
    ### Country code: 
    ### 0/1 occurance of '+' followed by 0/1 occurance of any digit followed by 0 to 2 occurance of whitespace as a group
    ### Phone number: 
    ### followed by 0/1 occurance of '(' followed by 3 digits followed by 0/1 occurance of ')' followed by 0-to-2 occurance of whitespace
    ### followed by 0/1 occurance of '-' followed by 3 digits ollowed by 0/1 occurance of '-' followed by 4 digits
    
    ##phoneNumRegex = re.compile(r'[\+?\d{0,1}\s{0,2}\.?]\(?\d{3}\)?\s{0,2}-?\d{3}-?\d{4}')  # r=raw string, \d
    phoneNumRegex = re.compile(r'\+?\d{0,1}\.?\s{0,2}]\(?\d{3}\)?\s{0,2}-?\d{3}-?\d{4}')  # r=raw string, \d
    
    
    
    ## Here re.findall() will return list.
    ## Loop through to print each string 
    for match in phoneNumRegex.findall(line):
        print match
    
f.close()
