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

    ##[INFO ] 2018-01-11 00:14:24.436 [qtp101478235-44] LogFilter - Response: | REQUEST ID=1353 | URI=/subscriptionservice/v1/users/saket.pathak08@gmail.com%23vj/unpaidinvoices | Time Taken : 2ms; | PAYLOAD=[] 
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




###TEMP
## scp akapil@zbill103.qa.sbs.bf1.yahoo.com:~/bill-2018-01-11.log ~/
'''
>>> import sys, re
>>> pattern = 'URI=(.*?)\s\|\sTime Taken : (.*?)ms'
>>> regex = re.compile(pattern) 
>>> data={}
>>> 
>>> for x in range(1,5):
        print "Loop:", x
...     line=raw_input("Enter string:")
...     match = regex.search(line)
...     if match:
...         print match.groups()
...         key = match.group(1)
            print "existing value:", data.get(key, 0)
            value = data.get(key, 0) + 1
...         data.update({key:value})
...         print data

'''

'(\/\w+)?'



####Prog 2
'''
import sys, re
for x in range(1,5):
    line=raw_input("Enter string:")
    pattern=raw_input("Enter pattern:")
    match=re.search(pattern,line)
    if match:
        print "Found match..."
        print match.group()


'''


