#!/usr/bin/python
import sys
import os

scwd = str(os.getcwd())

narg=len(sys.argv)

if narg != 2:
    print "Number of arguments not 1"
    print "USAGE:"
    print "$>newproject.py projname"
    print "where projname is the name of your new project"
    sys.exit()



projname = sys.argv[1]

dirlist = []
for dirn in os.listdir(scwd):
    if os.path.isdir(dirn):
        dirlist.append(dirn)

if projname in dirlist:
    print "The project name that you provided is already in use."
    print "Please provide a different name."
    sys.exit()
    
os.system("mkdir %s"%(projname))
os.system("mkdir %s/runs"%(projname))
os.system("mkdir %s/scripts"%(projname))
os.system("mkdir %s/results"%(projname))
os.system("mkdir %s/reports"%(projname))

print "Project created successfully."

