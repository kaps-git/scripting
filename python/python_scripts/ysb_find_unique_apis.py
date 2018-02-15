#!/usr/bin/python
##./ysb_find_unique_apis.py 'URI=(.*?)\s\|\sTime Taken : (.*?)ms' ../testdata_python/bill-2018-01-11.log

import sys, re

pattern = sys.argv[1]
fileName = sys.argv[2]

print "Pattern :", pattern
print "File name :", fileName

#Create dictionary object
data = {}

f = open(fileName, "r")

for line in iter(f):

    ## Pattern : 'URI=(.*?)\s\|\sTime Taken : (.*?)ms'
  
    regex = re.compile(pattern) 
    match = regex.search(line)

    if match:
        key = match.group(1) 
        data[key] = data.get(key, 0) + 1
     
f.close()

##print dictionary based on sorted key

for key in sorted(data.iterkeys()):
    print "%s : %s" % (key, data[key])



