#!/usr/bin/python

import os, signal, sys

searchStr=sys.argv[1]

def check_kill_process(pstring):
    for line in os.popen("ps ax | grep " + pstring + " | grep -v -e grep -e python"):
        print line
        fields = line.split()
        pid = fields[0]
        print "Killing process with pid :", pid
        os.kill(int(pid), signal.SIGKILL)
        
check_kill_process(searchStr)