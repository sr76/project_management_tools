#!/usr/bin/python
import os
from lxml import etree
import runsarr
import sys

runs = runsarr.runsarr()

runs.sort(lambda x, y: cmp(x[2],y[2]))

args = sys.argv[1:]

narg=len(args)


for run in runs:
    s_project=run[0]
    s_tstamp=run[1]
    s_index=run[2]
    s_description=run[3]
    s_path=run[4]
    s_status=run[5]
    s_importance=run[6]

    printrun = 0

    if narg == 0:
        printrun = 1

 
    if "-s" in args:
        if s_status in args:
            printrun = 1
            
    if "-p" in args:
        if s_project in args:
            printrun = 1

    if "-i" in args:
        if s_importance in args:
            printrun = 1
    
    if ("-p" in args) and ("-i" in args):
        printrun=0
        if s_project in args and s_importance in args:
            printrun = 1
    
    if printrun:
        print "***************************"
        print "PROJECT:",s_project
        print "TSTAMP:",s_tstamp
        print "INDEX:",s_index
        print "DESCRIPTION:", s_description
        print "PATH:", s_path
        print "STATUS:", s_status
        print "IMPORTANCE:", s_importance
        print "***************************\n"
