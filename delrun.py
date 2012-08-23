#!/usr/bin/python
import sys
import runsarr
import os

scwd = str(os.getcwd()).split("/")
if scwd[len(scwd)-1]!="runs":
    print "You are not in a runs directory"
    sys.exit()

narg=len(sys.argv)

if narg < 2:
    print "Number of arguments less than 1"
    print "USAGE:"
    print "$>delrun.py index1 index2 ..."
    print "where indexi is the index of the run, which you can find by running listruns.py"
    sys.exit()

runs=runsarr.runsarr()

for run in runs:
    s_project=run[0]
    s_tstamp=run[1]
    index=int(run[2])
    s_description=run[3]
    s_path=run[4]

    if str(index) in sys.argv[1:]:
        print "********** DELETED RUN *****************"
        print "PROJECT:",s_project
        print "TSTAMP:",s_tstamp
        print "INDEX:",index
        print "DESCRIPTION:", s_description
        print "PATH:", s_path
        print "***************************************\n"

        os.system("rm -r %s"%(s_path))
