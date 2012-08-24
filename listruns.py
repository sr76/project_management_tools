#!/usr/bin/python
import os
from lxml import etree
import runsarr


runs = runsarr.runsarr()

runs.sort(lambda x, y: cmp(x[2],y[2]))

for run in runs:
    s_project=run[0]
    s_tstamp=run[1]
    s_index=run[2]
    s_description=run[3]
    s_path=run[4]
    s_status=run[5]
    s_importance=run[6]

    print "***************************"
    print "PROJECT:",s_project
    print "TSTAMP:",s_tstamp
    print "INDEX:",s_index
    print "DESCRIPTION:", s_description
    print "PATH:", s_path
    print "***************************\n"


